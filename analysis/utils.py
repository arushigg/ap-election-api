import requests
import json
import exceptions
from param_schema._base_param import QueryParameters
from dataclasses import fields
from enum import Enum
from response_schema._base_response import ResponseParser

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