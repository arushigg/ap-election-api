from enum import Enum

# Required fields for an elections request

class Format(Enum):
    JSON = "application/json"
    XML = "application/xml"

class Version(Enum):
    V2 = "v2"
    V3 = "v3"

class DataType(Enum):
    ELECS = "elections"
    ELEC_REPORTS = "reports"
    ADV_TURNOUT = "advance_turnout"
    DELEGATES = "delegates"

# Optional fields for an elections request 

class State(Enum):
    AL = "AL"
    AK = "AK"
    AZ = "AZ"
    AR = "AR"
    CA = "CA"
    CO = "CO"
    CT = "CT"
    DE = "DE"
    FL = "FL"
    GA = "GA"
    HI = "HI"
    ID = "ID"
    IL = "IL"
    IN = "IN"
    IA = "IA"
    KS = "KS"
    KY = "KY"
    LA = "LA"
    ME = "ME"
    MD = "MD"
    MA = "MA"
    MI = "MI"
    MN = "MN"
    MS = "MS"
    MO = "MO"
    MT = "MT"
    NE = "NE"
    NV = "NV"
    NH = "NH"
    NJ = "NJ"
    NM = "NM"
    NY = "NY"
    NC = "NC"
    ND = "ND"
    OH = "OH"
    OK = "OK"
    OR = "OR"
    PA = "PA"
    RI = "RI"
    SC = "SC"
    SD = "SD"
    TN = "TN"
    TX = "TX"
    UT = "UT"
    VT = "VT"
    VA = "VA"
    WA = "WA"
    WV = "WV"
    WI = "WI"
    WY = "WY"
    US = "US"

class OfficeID(Enum):
    ATTORNEY_GENERAL = 'A'
    APPELLATE_COURT_CLERK = 'ACC'
    AGRICULTURE_COMMISSIONER = 'AGC'
    ASSESSOR = 'ASR'
    AUDITOR = 'AUD'
    SUPREME_COURT = 'B'
    BESE_BOARD = 'BEB'
    BOARD_OF_APPEALS = 'BOA'
    BOARD_OF_EQUALIZATION = 'BOE'
    BOARD_OF_GOVERNORS = 'BOG'
    BOARD_OF_SUPERVISORS = 'BOS'
    BOARD_OF_TRUSTEES = 'BOT'
    COMPTROLLER = 'C'
    CITY_ATTORNEY = 'CAT'
    COUNTY_AUDITOR = 'CAU'
    COUNTY_BOARD = 'CBD'
    CIRCUIT_COURT_CLERK = 'CCC'
    COUNTY_CHARTER_COMMISSION = 'CCH'
    CITY_CLERK = 'CCK'
    CITY_COMMISSIONER = 'CCM'
    COUNTY_COUNCIL = 'CCO'
    CITY_COMPTROLLER = 'CCP'
    COUNTY_COURT = 'CCR'
    CIRCUIT_COURT = 'CCT'
    COUNTY_CEO = 'CEO'
    CHANCERY_COURT = 'CHA'
    CHARTER_COMMISSION = 'CHC'
    INSURANCE_COMMISSIONER = 'CI'
    CIVIL_APPEALS_COURT = 'CIV'
    COUNTY_JUSTICE_JUDGE = 'CJJ'
    CLERK_OF_COURTS = 'CKC'
    COUNTY_LEGISLATURE = 'CLG'
    COURT_OF_COMMON_PLEAS = 'CMP'
    COUNTY_ATTORNEY = 'COA'
    COUNTY_CLERK = 'COC'
    COUNTY_JUDGE = 'COJ'
    COUNTY_COMMISSIONER = 'COM'
    CONSTABLE = 'CON'
    COUNTY_CORONER = 'COR'
    COUNTY_ASSESSOR = 'COS'
    COUNTY_TREASURER = 'COT'
    CORPORATION_COMMISSIONER = 'CPC'
    CITY_RECORDER = 'CRD'
    COUNTY_RECORDER = 'CRE'
    CRIMINAL_APPEALS_COURT = 'CRI'
    CLERK_OF_THE_SUPREME_JUDICIAL_COURT = 'CSJ'
    COUNTY_SUPERVISOR = 'CSP'
    COUNTY_SURVEYOR = 'CSR'
    COUNTY_SCHOOL_SUPERINTENDENT = 'CSU'
    CITY_TREASURER = 'CTS'
    DISTRICT_ATTORNEY = 'D'
    DELEGATE_EQUIVALENTS = 'DGE'
    DISTRICT_DELEGATE = 'DTD'
    EXECUTIVE_COUNCIL = 'EXC'
    COUNTY_EXECUTIVE = 'F'
    FAMILY_COURT = 'FCT'
    FIRE_PROTECTION_DISTRICT = 'FPD'
    GOVERNOR = 'G'
    US_HOUSE = 'H'
    HAWAIIAN_AFFAIRS = 'HIA'
    HIGHWAY_COMMISSIONER = 'HWC'
    BALLOT_MEASURE = 'I'
    APPEALS_COURT = 'J'
    JUDGE_OF_PROBATE = 'JPB'
    JUSTICE_OF_THE_PEACE = 'JTP'
    LIEUTENANT_GOVERNOR = 'L'
    LAND_COMMISSIONER = 'LAC'
    LABOR_COMMISSIONER = 'LBC'
    MAYOR = 'M'
    MAGISTRATE = 'MAG'
    MUNICIPAL_COURT_JUDGE = 'MCJ'
    MINE_INSPECTOR = 'MIN'
    CITY_COUNCIL = 'N'
    NEW_YORK_CITY_CIVIL_COURT = 'NCC'
    NEBRASKA_PUBLIC_POWER = 'NPP'
    ORPHANS_COURT = 'OCT'
    PRESIDENT = 'P'
    PUBLIC_ADMINISTRATOR = 'PAD'
    PUBLIC_ADVOCATE = 'PAV'
    PUBLIC_DEFENDER = 'PDF'
    PUBLIC_EDUCATION_COMMISSION = 'PEC'
    POLICE_COUNCIL = 'POC'
    PUBLIC_REGULATION_COMMISSION = 'PRC'
    PUBLIC_SERVICE_COMMISSION = 'PS'
    PUBLIC_SAFETY_COMMISSION = 'PSC'
    DELEGATES = 'Q'
    BOROUGH_PRESIDENT = 'R'
    REGISTER_OF_PROBATE = 'ROP'
    REGISTER_OF_WILLS = 'ROW'
    RAILROAD_COMMISSIONER = 'RR'
    RURAL_TRANSPORTATION_DISTRICT = 'RTD'
    US_SENATE = 'S'
    STATE_BOARD_OF_EDUCATION = 'SBE'
    STATE_BOARD_OF_REGENTS = 'SBR'
    SCHOOL_BOARD = 'SCB'
    SUPERIOR_COURT_CLERK = 'SCK'
    SHADOW_REPRESENTATIVE = 'SDR'
    SHADOW_SENATOR = 'SDS'
    SCHOOL_DISTRICT_TRUSTEE = 'SDT'
    SELECTMAN = 'SEL'
    SHERIFF = 'SHF'
    SUPERVISOR_OF_ELECS = 'SOE'
    SUPERIOR_COURT = 'SPC'
    SECRETARY_OF_STATE = 'SS'
    SUPREME_COURT_CLERK = 'SUC'
    SUPERINTENDENT_OF_EDUCATION = 'SUE'
    TREASURER = 'T'
    TAX_COURT = 'TAX'
    TOWN_ADMINISTRATOR = 'TOA'
    TOWN_BOARD = 'TOB'
    TRANSPORTATION_COMMISSIONER = 'TRC'
    TAX_COMMISSIONER = 'TXC'
    SURROGATE = 'U'
    UNIVERSITY_REGENTS = 'UR'
    US_DELEGATE = 'USD'
    DISTRICT_COURT = 'W'
    WATER_COMMISSIONER = 'WAC'
    STATE_HOUSE = 'Y'
    STATE_SENATE = 'Z'

class Winner(Enum):
    DECLARED = "X"
    RUNOFF = "R"
    NOT_DECLARED = "U"
    ALL = "A"

class RaceType(Enum):
    GENERAL_ELEC = 'G'
    SPECIAL_GENERAL_ELEC = 'W'
    GENERAL_ELEC_RUNOFF = 'H'
    NON_PARTISAN_ELEC = 'L'
    NON_PARTISAN_SPECIAL_ELEC = 'T'
    JUDICIAL_RETENTION_ELEC = 'RET'
    ALL_PARTY_PRIM = 'APP'
    ALL_PARTY_SPECIAL_PRIM = 'SAP'
    NON_PARTISAN_PRIM = 'N'
    DEM_PRIM = 'D'
    DEM_PRIM_RUNOFF = 'U'
    DEM_SPECIAL_PRIM = 'J'
    DEM_SPECIAL_PRIM_RUNOFF = 'A'
    DEM_CAUCUSES = 'E'
    DEM_CONVENTION = 'E'
    DEM_DELEGATE_ELEC = 'E'
    DEM_CAUCUSES_FIRST_ALIGNMENT = 'E'
    DEM_CAUCUSES_FINAL_ALIGNMENT = 'E'
    REP_PRIM = 'R'
    REP_PRIM_RUNOFF = 'V'
    REP_SPECIAL_PRIM = 'K'
    REP_SPECIAL_PRIM_RUNOFF = 'B'
    REP_CAUCUSES = 'S'
    REP_CONVENTION = 'S'
    REP_DELEGATE_ELEC = 'S'
    AMERICAN_HERITAGE_PARTY_PRIM = 'AHP'
    AMERICAN_INDEPENDENT_PRIM = 'AIP'
    ALASKAN_INDEPENDENCE_PRIM = 'AkI'
    BEST_PRIM = 'Bst'
    CONSERVATIVE_PRIM = 'Con'
    CONSTITUTION_PRIM = 'Cst'
    FREE_ENERGY_PARTY_PRIM = 'FEP'
    GREEN_PRIM = 'Grn'
    GRASSROOTS_LEGALIZE_CANNABIS_PARTY_PRIM = 'GRP'
    INDEPENDENT_AMERICAN_PRIM = 'IAP'
    INDEPENDENT_PRIM = 'Ind'
    INDEPENDENCE_PARTY_PRIM = 'InP'
    INDEPENDENT_PARTY_PRIM = 'IP'
    LIBERAL_PRIM = 'Lbl'
    FARMER_LABOR_PRIM = 'LFM'
    LIBERTARIAN_PRIM = 'Lib'
    MOUNTAIN_PARTY_PRIM = 'Mnt'
    NEBRASKA_PRIM = 'Neb'
    NATURAL_LAW_PARTY_PRIM = 'NLP'
    NEW_PERSPECTIVE_PRIM = 'NwP'
    ORANGE_TAXPAYERS_PRIM = 'OTx'
    PERSONAL_CHOICE_PRIM = 'PCH'
    PEACE_AND_FREEDOM_PRIM = 'PFP'
    PROGRESSIVE_PRIM = 'Prg'
    REFORM_PARTY_PRIM = 'RP'
    REP_MODERATE_PRIM = 'RpM'
    RIGHT_TO_LIFE_PRIM = 'RTL'
    SERVE_AMERICA_MOVEMENT_PRIM = 'SAM'
    STATEHOOD_PARTY_PRIM = 'Sta'
    SOCIALIST_WORKERS_PARTY_PRIM = 'SWP'
    TERM_LIMITS_PRIM = 'TLm'
    UNITED_ADVOCACY_PRIM = 'UAd'
    US_TAXPAYERS_PARTY_PRIM = 'UST'
    UNITED_UTAH_PRIM = 'UUt'
    UNITED_UTAH_SPECIAL_PRIM = 'UUt'
    WOMENS_EQUALITY_PARTY_PRIM = 'WEq'
    WORKING_FAMILIES_PRIM = 'WF'
    OTHER_PRIM = 'C'
    OTHER_PRIM_RUNOFF = 'I'
    OTHER_SPECIAL_PRIM = 'OS'

class Party(Enum):
    ALOHA_AINA = "AAP"
    AMERICAN_HERITAGE = "AHP"
    AMERICAN_INDEPENDENT = "AIP"
    ALASKAN_INDEPENDENCE = "AkI"
    ALLIANCE = "AlP"
    AMERICAN_CONSTITUTION = "AmC"
    AMERICAN_SOLIDARITY = "ASP"
    APPROVAL_VOTING = "AVP"
    BREAD_AND_ROSES = "BdR"
    BEST = "Bst"
    COMMUNIST = "Cmt"
    CONSERVATIVE = "Con"
    CONSTITUTION = "Cst"
    DC_STATEHOOD_GREEN = "DCG"
    DEMOCRATIC = "Dem"
    ECOLOGY_PARTY_OF_FLORIDA = "EPF"
    FREE_ENERGY = "FEP"
    FREEDOM = "Fre"
    REPUBLICAN = "GOP"
    GREEN_MOUNTAIN_PEACE_AND_JUSTICE = "GPJ"
    GREEN = "Grn"
    GRASSROOTS_LEGALIZE_CANNABIS = "GrP"
    INDEPENDENT_AMERICAN = "IAP"
    MAINE_GREEN_INDEPENDENT = "IGr"
    INDEPENDENCE_ALLIANCE_PARTY_OF_MINNESOTA = "InA"
    INDEPENDENT = "Ind"
    INDEPENDENCE_PARTY = "InP"
    INDEPENDENT_PARTY = "IP"
    INDEPENDENT_PARTY_OF_DELAWARE = "IPD"
    JUSTICE = "JP"
    KEYSTONE_PARTY_OF_PENNSYLVANIA = "Key"
    LABOR = "Lab"
    LIBERAL = "Lbl"
    MINNESOTA_DEMOCRATIC_FARMER_LABOR = "LFM"
    LIBERTARIAN = "Lib"
    LEGAL_MARIJUANA_NOW = "LMN"
    MOUNTAIN = "Mnt"
    NEBRASKA = "Neb"
    NATURAL_LAW = "NLP"
    NO = "NO" # for ballot measures
    NONE_OF_THE_ABOVE = "Non"
    NON_PARTISAN = "NP"
    NO_PARTY_AFFILIATION = "NPA"
    NO_PARTY_DESIGNATION = "NPD"
    NO_PARTY_PREFERENCE = "NPP"
    NEW_PERSPECTIVE = "NwP"
    OTHER = "Oth"
    ORANGE_TAXPAYERS = "OTx"
    PACIFIC_GREEN = "PaG"
    PATRIOT = "Pat"
    PERSONAL_CHOICE = "PCh"
    PETITIONING_CANDIDATE = "PeC"
    PEACE_AND_FREEDOM = "PFP"
    PROGRESSIVE = "Prg"
    PARTY_FOR_SOCIALISM_AND_LIBERATION = "PSL"
    REFORM_PARTY = "RP"
    REPUBLICAN_MODERATE = "RpM"
    RIGHT_TO_LIFE = "RTL"
    SERVE_AMERICA_MOVEMENT = "SAM"
    SOCIALIST_EQUALITY = "SEP"
    STATEHOOD = "Sta"
    SOCIALIST_WORKERS_PARTY = "SWP"
    TO_BE_DETERMINED = "TBD"
    TERM_LIMITS = "TLm"
    UNITED_ADVOCACY = "UAd"
    UNITED_CITIZENS = "UCz"
    UNDECLARED = "Udl"
    UNAFFILIATED = "Una"
    UNENROLLED = "Unr"
    US_TAXPAYERS = "UST"
    UNITY = "Uty"
    UNITED_UTAH = "UUt"
    VETERANS_PARTY_OF_AMERICA = "Vet"
    WORKING_CLASS = "WCP"
    WOMENS_EQUALITY = "WEq"
    WORKING_FAMILIES = "WF"
    WRITE_IN = "WrI"
    WE_THE_PEOPLE = "WTP"
    YES = "Yes" # for ballot measures

    # there are other, older codes not listed here

class Uncontested(Enum):
    CONTESTED = "false"
    UNCONTESTED = "true"
    ALL = "all"

class National(Enum):
    NATIONAL = "true"
    STATE_AND_LOCAL = "false"
    ALL = "all"

class ResultsType(Enum):
    LIVE = "l"
    TEST = "t"
    CERTIFIED = "c"
    LIVE_THEN_CERTIFIED = "b"

class VoteType(Enum):
    RETURN_BY_TYPE = "true"
    RETURN_TOGETHER = "false"

class AdvReport(Enum):
    INCL_ADV_VOTES = "true"
    NO_ADV_VOTES = "false"

class Level(Enum):
    STATE = "state"
    REPORTING_UNITS = "RU"
    FIPS = "FIPScode"
    DISTRICT = "district"

class CandidateInfo(Enum):
    FULL = "full"
    BRIEF = "brief"

class SetZeroCounts(Enum):
    TRUE = "true"
    FALSE = "false"

class OmitResults(Enum):
    TRUE = "true"
    FALSE = "false"

# Fields for an election report request

class ReportType(Enum):
    DELEGATES = "delegates"
    DELEGATE_BREAKOUT = "delbreakout"
    PRESIDENTIAL = "pres"
    TREND = "trend"
    EST_VOTE_PCT = "EstimatedVotePercentage"
    CALENDAR = "calendar"
    CANDIDATES = "candidates"
    ADV_VOTES = "advvotes"
    AVAILABLE_VOTE_TYPES = "AvailableVoteTypes"
    PARTIES = "parties"
    POLL_HOURS = "pollhours"

class ReportSubType(Enum):
    # for ReportType.DELEGATES
    DEL_SUMMARY = "delsum"
    DEL_STATE = "delstate"
    DEL_SUPER = "delsuper"
    # for ReportType.DELEGATE_BREAKOUT
    DEL_BREAKOUT_2024 = "delbreakout2024"
    # for ReportType.PRESIDENTIAL
    PRES_STATE_BY_STATE = "statebystate_pres"
    PRES_SUMMARY = "pres_summary"
    PRES_SUMMARY_ALL = "pres_summary_all"
    # for ReportType.TREND
    GOVERNOR = "g"
    SENATE = "s"
    HOUSE = "h"
    # for ReportType.CALENDAR
    ELECTIONS_2024 = "elections2024"
    CUSTOMER_TESTING_2021 = "customertesting2021"
    # for ReportType.ADV_VOTES
    ADV_VOTING_RULES_2022_GE = "advvotingrules2022GE"
    # for ReportType.PARTIES
    PARTY_CODES = "partycodes"

TYPE_TO_SUBTYPE_MAP = {
    ReportType.DELEGATES: [
        ReportSubType.DEL_SUMMARY,
        ReportSubType.DEL_STATE,
        ReportSubType.DEL_SUPER
    ],
    ReportType.DELEGATE_BREAKOUT: [
        ReportSubType.DEL_BREAKOUT_2024
    ],
    ReportType.PRESIDENTIAL: [
        ReportSubType.PRES_STATE_BY_STATE,
        ReportSubType.PRES_SUMMARY,
        ReportSubType.PRES_SUMMARY_ALL
    ],
    ReportType.TREND: [
        ReportSubType.GOVERNOR,
        ReportSubType.SENATE,
        ReportSubType.HOUSE
    ],
    ReportType.CALENDAR: [
        ReportSubType.ELECTIONS_2024,
        ReportSubType.CUSTOMER_TESTING_2021
    ],
    ReportType.ADV_VOTES: [
        ReportSubType.ADV_VOTING_RULES_2022_GE
    ],
    ReportType.PARTIES: [
        ReportSubType.PARTY_CODES
    ]
}

# Fields for a delegates request

class DelegateType(Enum):
    SUMMARY = "summary"
    STATE = "state"
    SUPER = "super"