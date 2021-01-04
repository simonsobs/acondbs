"""Operations on DB
"""

from flask import current_app

from ..db.sa import sa

from ..models import (
    GitHubOrg,
    GitHubUser,
    GitHubToken,
    GitHubOrgMembership
)

from . import call, query

##__________________________________________________________________||
def get_github_oauth_app_info():
    ret = dict(
        authorize_url=current_app.config['GITHUB_AUTH_AUTHORIZE_URL'],
        token_url=current_app.config['GITHUB_AUTH_TOKEN_URL'],
        client_id=current_app.config['GITHUB_AUTH_CLIENT_ID'],
        client_secret=current_app.config['GITHUB_AUTH_CLIENT_SECRET'],
        redirect_uri=current_app.config['GITHUB_AUTH_REDIRECT_URI']
    )
    return ret

##__________________________________________________________________||
def exchange_code_for_token(code):
    oauth_app_info = get_github_oauth_app_info()
    return call.exchange_code_for_token(
        code,
        token_url=oauth_app_info['token_url'],
        client_id=oauth_app_info['client_id'],
        client_secret=current_app.config['GITHUB_AUTH_CLIENT_SECRET'],
        redirect_uri=current_app.config['GITHUB_AUTH_REDIRECT_URI']
        )

##__________________________________________________________________||
def add_org(login):
    if GitHubOrg.query.filter_by(login=login).one_or_none() is not None:
        raise Exception(f'already exists: {login}')
    if not (tokens := GitHubToken.query.all()):
        raise Exception('No tokens available.')
    r = None
    for token in tokens:
        try:
            r = query.org(login, token.token)
        except:
            continue
        break
    if r is None:
        raise Exception(f'Unable to find an org: {login}')
    model = GitHubOrg(login=login, git_hub_id=r['id'])
    sa.session.add(model)
    sa.session.commit()
    return model

def delete_org(login):
    if (model := GitHubOrg.query.filter_by(login=login).one_or_none()) is None:
        raise Exception(f'does not exist: {login}')
    sa.session.delete(model)
    sa.session.commit()

##__________________________________________________________________||
def update_org_member_lists():
    if not (tokens := GitHubToken.query.filter(GitHubToken.scope.like('%read:org%')).all()):
        raise Exception('No tokens with relevant scopes available.')
    if not (orgs := GitHubOrg.query.all()):
        raise Exception('No orgs found.')
    with sa.session.no_autoflush:
        memberships = GitHubOrgMembership.query.all()
        for membership in memberships:
            sa.session.delete(membership)
        for org in orgs:
            edges = None
            for token in tokens:
                print(token.scope)
                try:
                    edges = query.org_members(org.login, token.token)
                except Exception as e:
                    print(e)
                    continue
                break
            if edges is None:
                raise Exception(f'Unable to find an org: {org.login}')
            for edge in edges:
                node = edge['node']
                if (member := GitHubUser.query.filter_by(git_hub_id=node['id']).one_or_none()) is None:
                    member = GitHubUser(git_hub_id=node['id'])
                member.login = node['login']
                member.name = node['name']
                member.avatar_url = node['avatarUrl']
                membership = GitHubOrgMembership(org=org, member=member)
                sa.session.add(membership)
    sa.session.commit()

##__________________________________________________________________||
def store_token_for_code(code):
    token_dict = exchange_code_for_token(code)
    viewer = query.viewer(token_dict['access_token'])
    if (user_model := GitHubUser.query.filter_by(git_hub_id=viewer['id']).one_or_none()) is None:
        user_model = GitHubUser(git_hub_id=viewer['id'])
    user_model.login = viewer['login']
    user_model.name = viewer['name']
    user_model.avatar_url = viewer['avatarUrl']
    token_model = GitHubToken(
        token=token_dict['access_token'],
        scope=token_dict['scope'],
        user=user_model)
    sa.session.add(token_model)
    sa.session.commit()

##__________________________________________________________________||
def authenticate(code):
    token_dict = exchange_code_for_token(code)
    viewer = query.viewer(token_dict['access_token'])
    if (user_model := GitHubUser.query.filter_by(git_hub_id=viewer['id']).one_or_none()) is None:
        raise Exception(f'{viewer["login"]} is not a member.')
    if not user_model.memberships:
        raise Exception(f'{viewer["login"]} is not a member!')
    # TODO Check a membership
    # print([m.org for m in user_model.memberships])
    user_model.login = viewer['login']
    user_model.name = viewer['name']
    user_model.avatar_url = viewer['avatarUrl']
    token_model = GitHubToken(
        token=token_dict['access_token'],
        scope=token_dict['scope'],
        user=user_model)
    sa.session.add(token_model)
    sa.session.commit()
    return token_dict

##__________________________________________________________________||
