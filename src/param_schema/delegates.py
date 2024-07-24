import src._fields as f
from typing import Union
from src.exceptions import InvalidParameterError
from src.param_schema._base_param import QueryParameters, OPT_PARAM_SUPERSET, create_optional_param_dict
from datetime import datetime

class DelegateParameters(QueryParameters):
    DATA_TYPE = f.DataType.DELEGATES

    # required parameters
    election_date: datetime
    version: f.Version = f.Version.V3

    # optional parameters
    party: Union[f.Party, list[f.Party]] = [f.Party.DEMOCRATIC, f.Party.REPUBLICAN]
    type: f.DelegateType = f.DelegateType.SUMMARY
    results_type: f.ResultsType = f.ResultsType.LIVE

    def __post_init__(self):
        # has to be one or both of the two major parties
        if self.party not in [f.Party.DEMOCRATIC, f.Party.REPUBLICAN, [f.Party.DEMOCRATIC, f.Party.REPUBLICAN]]:
            raise InvalidParameterError(self.party, "Invalid parameter: Part must be Democratic or Republican")
        
        if self.results_type != f.ResultsType.LIVE and self.results_type != f.ResultsType.TEST:
            raise InvalidParameterError(self.results_type, "Invalid parameter: Results type must be live or test")

    @property
    def base_url(self) -> str:
        return f"https://api.ap.org/{self.version.value}/elections/delegates/{self.election_date.year}"

    @property
    def optional_param_dict(self) -> dict:
        DELEGATE_OPT_PARAMS = ["party", "type", "results_type"]
        param_dict = {var: OPT_PARAM_SUPERSET[var] for var in DELEGATE_OPT_PARAMS}
        return create_optional_param_dict(self, param_dict)  