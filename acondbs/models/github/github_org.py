from ...db.sa import sa

##__________________________________________________________________||
class GitHubOrg(sa.Model):
    __tablename__ = 'github_orgs'
    org_id = sa.Column(sa.Integer(), primary_key=True)
    login = sa.Column(sa.Text(), nullable=False)

    def __repr__(self):
        return f'<{self.__class__.__name__} {self.login!r}>'

##__________________________________________________________________||
