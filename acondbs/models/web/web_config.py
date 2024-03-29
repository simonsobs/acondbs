import json

from acondbs.db.sa import sa
from acondbs.models.funcs import shorten


class WebConfig(sa.Model):  # type: ignore
    __tablename__ = "web_config"
    id_ = sa.Column(sa.Integer(), primary_key=True)
    json = sa.Column(sa.Text())

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.id_!r} {self._json_repr!r}>"

    @property
    def _json_repr(self) -> str:
        try:
            most_compact = json.dumps(json.loads(self.json), indent=None)
            return shorten(most_compact, width=20)
        except BaseException:
            pass

        try:
            return shorten(repr(self.json), width=20)
        except BaseException:
            pass

        return self.json
