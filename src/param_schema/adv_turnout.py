from typing import Union
from datetime import datetime
from dataclasses import dataclass

import fields as f
import exceptions as e
from _base_param import QueryParameters, OPT_PARAM_SUPERSET, create_optional_param_dict


@dataclass
class AdvTurnoutParameters(QueryParameters):

    # required parameters
    election_date: datetime
    version: f.Version = f.Version.V3

    # optional parameters
    state: Union[f.State, list[f.State]] = None
    level: f.Level = f.Level.STATE

    def __post_init__(self):
        if self.level != f.Level.STATE and self.level != f.Level.REPORTING_UNITS:
            raise e.InvalidParameterError(self.level, "Invalid parameter: Level must be state or reporting unit.")

    @property
    def base_url(self) -> str:
        formatted_date = self.election_date.strftime("%Y-%m-%d")
        return f"https://api.ap.org/{self.version.value}/elections/{formatted_date}/advance"

    @property
    def optional_param_dict(self) -> dict:
        ADV_VOTES_OPT_PARAMS = ["state", "level"]
        param_dict = {var: OPT_PARAM_SUPERSET[var] for var in ADV_VOTES_OPT_PARAMS}
        return create_optional_param_dict(self, param_dict)  