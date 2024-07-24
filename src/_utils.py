import requests
import pandas as pd
import src.exceptions as exceptions
from src.response_schema._base_response import ResponseParser

def handle_error_codes(response: requests.Response) -> None:
    """
    Throw an error based on the status codes. Does nothing for a 200 code.
    Based on this: https://developer.ap.org/ap-elections-api/docs/index.html#t=API_Codes.htm
    """
    if response.status_code == 200:
        return
    elif response.status_code == 400:
        raise exceptions.InvalidParameterError()
    elif response.status_code == 401:
        raise exceptions.InvalidAPIKeyError()
    elif response.status_code == 403:
        raise exceptions.QuotaLimitExceededError()
    elif response.status_code == 405:
        raise exceptions.RequestMethodNotSupportedError()
    elif response.status_code == 414:
        raise exceptions.RequestTooLongError()
    elif response.status_code == 500:
        raise exceptions.ServerError()
    elif response.status_code == 502:
        raise exceptions.BadGatewayError()
    elif response.status_code == 503:
        raise exceptions.ServiceUnavailableError()
    elif response.status_code == 504:
        raise exceptions.GatewayTimeoutError()
    else:
        raise Exception(f"Unknown status code {response.status_code}.")
    


def merge_responses(resp_1: ResponseParser, resp_2: ResponseParser) -> ResponseParser:
    """
    Concatenate the data from different responses. Imagining this would be most useful when
    there's a truncated response that requires the same request to go out multiple times.
    """
    pass


def flatten_json(jdict: dict) -> pd.DataFrame:
    """
    Flatten a nested JSON without any knowledge of its structure, returning it as a
    dictionary. Note the naming convention -- when a sub-dict is expanded, its name is
    added to the front of the column name (eg. the key "first" in the list "candidates" 
    would become column "candidates.first")
    """
    if len(jdict) == 0:
        return pd.DataFrame()

    # helper function to expand one column of a dataframe
    def expand_df(df, col):
        row_dfs = []
        for _, row in df.iterrows():
            # expand the target cell into a df
            row_df = pd.json_normalize(row[col])
            if len(row_df) == 0:
                row[col] = None
                row_dfs.append(pd.DataFrame(row).T)
                break
            # rename the new child columns as parent.child
            row_df = row_df.rename(columns=(lambda x: f"{col}.{x}"))
            # copy the rest of the row so it can be reattached to the expanded df
            meta_row = pd.DataFrame(row.drop(col)).T
            expand_row = pd.concat([meta_row] * len(row_df), axis=0, ignore_index=True)
            # combine and store the new df corresponding to the row
            combined = pd.concat([row_df, expand_row], axis=1)
            row_dfs.append(combined)
        
        # If there aren't any rows, set the input column to None & return the original df
        if len(row_dfs) == 0:
            df[col] = None
            return df
        else:
            return pd.concat(row_dfs, ignore_index=True)

    # converts the json to a df without unnesting
    df = pd.json_normalize(jdict)
    while True:
        # go through each column to check if it's a list
        for col in df.columns:
            if isinstance(df[col].iloc[0], list):
                # if it is, expand that column and start going through the columns
                # from the beginning again
                df = expand_df(df, col)
                break
        # if we got through all the columns, there's no more to unnest
        if col == df.columns[-1]:
            return df