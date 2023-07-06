from collections import namedtuple

from pydantic import BaseModel
from pydantic.types import condecimal


class Geo(BaseModel):
    lat: condecimal(ge=-90, le=90)
    lon: condecimal(ge=-180, le=180)


class ForecastRequest(BaseModel):
    from_ts: int
    to_ts: int
    g: Geo


Header = namedtuple("header",
                    ["min_y", "max_y",
                     "min_x", "max_x",
                     "dy", "dx",
                     "multiplier",
                     "empty_value"])
