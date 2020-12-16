from ..db.sa import sa

##__________________________________________________________________||
class GitHubUser(sa.Model):
    __tablename__ = 'github_users'
    user_id = sa.Column(sa.Integer(), primary_key=True)
    login = sa.Column(sa.Text(), nullable=False)

##__________________________________________________________________||
