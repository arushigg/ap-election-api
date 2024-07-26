from typing import Union
from datetime import datetime
from dataclasses import dataclass, field

import fields as f
import exceptions as e
from _base_param import QueryParameters, OPT_PARAM_SUPERSET, create_optional_param_dict


@dataclass
class DelegateParameters(QueryParameters):

    # required parameters
    election_date: datetime
    version: f.Version = f.Version.V3

    # optional parameters
    party: Union[f.Party, set[f.Party]] = field(default_factory=lambda: {f.Party.DEMOCRATIC, f.Party.REPUBLICAN})
    type: f.DelegateType = f.DelegateType.SUMMARY
    results_type: f.ResultsType = f.ResultsType.LIVE

    def __post_init__(self):
        # has to be one or both of the two major parties
        if not set(self.party).issubset({f.Party.DEMOCRATIC, f.Party.REPUBLICAN}):
            raise e.InvalidParameterError(self.party, "Invalid parameter: Part must be Democratic or Republican")
        
        if self.results_type != f.ResultsType.LIVE and self.results_type != f.ResultsType.TEST:
            raise e.InvalidParameterError(self.results_type, "Invalid parameter: Results type must be live or test")

    @property
    def base_url(self) -> str:
        return f"https://api.ap.org/{self.version.value}/elections/delegates/{self.election_date.year}"

    @property
    def optional_param_dict(self) -> dict:
        DELEGATE_OPT_PARAMS = ["party", "type", "results_type"]
        param_dict = {var: OPT_PARAM_SUPERSET[var] for var in DELEGATE_OPT_PARAMS}
        return create_optional_param_dict(self, param_dict)  