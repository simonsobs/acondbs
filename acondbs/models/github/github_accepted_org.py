from ...db.sa import sa

##__________________________________________________________________||
class GitHubAcceptedOrg(sa.Model):
    __tablename__ = 'github_orgs'
    org_id = sa.Column(sa.Integer(), primary_key=True)
    login = sa.Column(sa.Text(), nullable=False)

##__________________________________________________________________||
