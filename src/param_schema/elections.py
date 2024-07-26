from typing import Union
from datetime import datetime
from dataclasses import dataclass

import fields as f
import exceptions as e
from _base_param import QueryParameters, OPT_PARAM_SUPERSET, create_optional_param_dict


@dataclass
class ElectionParameters(QueryParameters):

    # required parameters for any query
    election_date: datetime
    version: f.Version = f.Version.V3

    # optional parameters
    race_id: Union[int, list[int]] = None
    ru_id: Union[int, list[int]] = None
    state: Union[f.State, list[f.State]] = None
    office_id: Union[f.OfficeID, list[f.OfficeID]] = None
    winner: f.Winner = f.Winner.ALL
    race_type: f.RaceType = None
    party: f.Party = None
    uncontested: f.Uncontested = f.Uncontested.ALL
    national: f.National = f.National.ALL
    seat_num: int = None
    seat_name: str = None
    results_type: f.ResultsType = f.ResultsType.LIVE
    vote_type: f.VoteType = f.VoteType.RETURN_TOGETHER
    adv_report: f.AdvReport = f.AdvReport.NO_ADV_VOTES
    level: f.Level = f.Level.STATE
    candidate_info: f.CandidateInfo = None
    set_zero_counts: f.SetZeroCounts = f.SetZeroCounts.FALSE
    omit_results: f.OmitResults = f.OmitResults.FALSE

    def __post_init__(self):

        # race and reporting unit IDs require a single state to be specified
        if self.race_id is not None or self.ru_id is not None:
            if (
                self.state is None or 
                self.state == f.State.US or 
                self.state[0] == f.State.US or
                len(self.state) != 1
            ):
                raise e.InvalidParameterError("Invalid parameter: Race and reporting unit IDs require exactly one state.")
        
        # the 'US' code only applies to the general presidential election
        if self.state == f.State.US or (isinstance(self.state, list) and f.State.US in self.state):
            if self.election_date.year % 4 != 0:
                raise e.InvalidParameterError(
                    self.state, "Invalid parameter: The state can only be 'US' in the general election of a presidential year."
                )
        
        # set zero counts and omit results are mutually exclusive
        if self.set_zero_counts == f.SetZeroCounts.TRUE and self.omit_results == f.OmitResults.TRUE:
            raise e.InvalidParameterError(
                [self.set_zero_counts, self.omit_results],
                "Invalid parameter: set_zero_counts and omit_results are mutually exclusive."
            )

    @property
    def base_url(self) -> str:
        formatted_date = self.election_date.strftime("%Y-%m-%d")
        return f"https://api.ap.org/{self.version.value}/elections/{formatted_date}"

    @property
    def optional_param_dict(self) -> dict:
        ELECTION_OPT_PARAMS = [
            "race_id",
            "ru_id",
            "state",
            "office_id",
            "winner",
            "race_type",
            "party",
            "uncontested",
            "national",
            "seat_num",
            "seat_name",
            "results_type",
            "vote_type",
            "adv_report",
            "level",
            "candidate_info",
            "set_zero_counts",
            "omit_results"
        ]
        param_dict = {var: OPT_PARAM_SUPERSET[var] for var in ELECTION_OPT_PARAMS}
        return create_optional_param_dict(self, param_dict)