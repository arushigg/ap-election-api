from typing import Union
from datetime import datetime
from dataclasses import dataclass

import fields as f
import exceptions as e
from _base_param import QueryParameters, OPT_PARAM_SUPERSET, create_optional_param_dict

@dataclass
class ElectionReportParameters(QueryParameters):
    DATA_TYPE = f.DataType.ELEC_REPORTS

    # required parameters for any query
    version: f.Version = f.Version.V3

    # optional parameters
    results_type: f.ResultsType = f.ResultsType.LIVE
    election_date: datetime = None
    state: f.State = None
    type: Union[f.ReportType, list[f.ReportType]] = None
    subtype: Union[f.ReportSubType, list[f.ReportSubType]] = None

    def __post_init__(self):
        # only two types supported
        if self.results_type != f.ResultsType.LIVE or self.results_type != f.ResultsType.TEST:
            raise e.InvalidParameterError(self.results_type, "Invalid parameter: results_type must be live or test.")
        
        # 2016-11-08 is the earliest report date, except 2012-11-06
        if (
            self.election_date is not None and 
            self.election_date < datetime(2016, 11, 8) and
            self.election_date != datetime(2012, 11, 6)
        ):
            raise e.InvalidParameterError(
                self.election_date, "Invalid parameter: election_date must be after Nov. 8, 2016 or Nov. 6, 2012."
            )
        
        # the 'US' code only applies to the general presidential election
        if self.state == f.State.US or (isinstance(self.state, list) and f.State.US in self.state):
            if self.election_date.year % 4 != 0:
                raise e.InvalidParameterError(
                    self.state, "Invalid parameter: The state can only be 'US' in the general election of a presidential year."
                )
        
        if self.type == f.ReportType.CALENDAR or self.type == f.ReportType.CANDIDATES:
            if self.election_date.year < 2020:
                raise e.InvalidParameterError(
                    self.election_date, "Invalid parameter: Election calendar and candidate reports are only available 2020 and later."
                )

        if self.subtype is not None:
            # in v2, subtype requires type
            if self.version == f.Version.V2 and self.type is None:
                raise e.InvalidParameterError(
                    self.subtype, "Invalid parameter: In v2, report subtype can only be used with a report type."
                )
            # if both are specified, type and subtype should match
            elif self.type is not None:
                valid_subtypes = f.TYPE_TO_SUBTYPE_MAP[self.type]
                if not self.subtype in valid_subtypes:
                    raise e.InvalidParameterError(
                        self.subtype, "Invalid parameter: Report subtype does not match report type."
                    )

    @property
    def base_url(self) -> str:
        return f"https://api.ap.org/{self.version.value}/reports"

    @property
    def optional_param_dict(self) -> dict:
        ELECTION_REPORT_OPT_PARAMS = ["results_type", "election_date", "state", "type", "subtype"]
        param_dict = {var: OPT_PARAM_SUPERSET[var] for var in ELECTION_REPORT_OPT_PARAMS}
        return create_optional_param_dict(self, param_dict)