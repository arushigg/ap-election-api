from dataclasses import dataclass, fields
import _fields as f
from abc import ABC, abstractmethod
from enum import Enum
from urllib.parse import urlencode

"""
Base dataclass for defining the parameters of a request. Each of the four types of
data should inherit this class, define the optional fields, assemble URLs, and 
run data validation checks accordingly.
"""

@dataclass
class QueryParameters(ABC):

    @abstractmethod
    def __post_init__(self):
        """
        Called right after creating the instance. Any conditions to validate the parameters 
        can go here. Should raise exceptions defined in exceptions.py.
        """
        pass

    @property
    @abstractmethod
    def base_url(self) -> str:
        """
        Convert the election date & version into the base URL.
        """
        pass

    @property
    @abstractmethod
    def optional_param_dict(self) -> dict:
        """
        Get a dictionary of the optional parameters and their values to pass to a request.
        """
        pass

    @property
    def full_url(self):
        """
        Construct the full URL using the required and optional parameters.
        """
        return f"{self.base_url}?{urlencode(self.optional_param_dict)}"

# map the Python parameter name to the request parameter name
OPT_PARAM_SUPERSET = {
    "race_id": "raceID",
    "ru_id": "reportingUnitID",
    "state": "statePostal",
    "office_id": "officeID",
    "winner": "winner",
    "race_type": "raceTypeID",
    "party": "party",
    "uncontested": "uncontested",
    "national": "national",
    "seat_num": "seatNum",
    "seat_name": "seatName",
    "results_type": "resultsType",
    "vote_type": "votetypes",
    "adv_report": "avotes",
    "level": "level",
    "candidate_info": "candidateInfo",
    "set_zero_counts": "setZeroCounts",
    "omit_results": "omitResults",
    "election_date": "electionDate",
    "type": "type",
    "subtype": "subtype",
}

def create_optional_param_dict(params: QueryParameters, var_to_url_name: dict[str]) -> dict:
    """
    Convert the optional parameters into a dictionary for requests.get. Only
    include parameters that take on a non-default value. Requires a dictionary mapping
    each dataclass variable name to the corresponding parameter name in the API.
    """
    param_dict = {}
    for f in fields(params):
        # only care about the explicitly named variables
        if f.name not in var_to_url_name.keys():
            continue
        value = getattr(params, f.name)
        # since there's a limit on the number of characters, only be explicit about
        # non-default parameters
        if value is not f.default:
            # need to get the underlying value if it's an enum
            if isinstance(value, Enum):
                param_dict[var_to_url_name[f.name]] = value.value
            else:
                param_dict[var_to_url_name[f.name]] = value
    return param_dict