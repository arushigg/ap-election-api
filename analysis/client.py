import requests
import utils
import exceptions
import time
from typing import Union
import logging
import xml.etree.ElementTree as ET

from param_schema._base_param import QueryParameters
from param_schema import elections, election_reports, adv_turnout, delegates
from _fields import Format, DataType
from response_schema._base_response import ResponseParser
from response_schema.elections import ElectionsResponse

"""
A class for interacting with the API. Manages requests and responses.
"""

class APIClient:
    api_key: str
    format: Format
    headers: dict[str]
    queries: dict[str]
    logger: logging.Logger

    def __init__(self, api_key: str, format: Format = Format.XML, logger: logging.Logger = None):
        """
        Create the client with your API key and desired response format. Can optionally provide a 
        logger object
        """
        self.api_key = api_key
        self.format = format
        self.logger = logger

        self.headers = {
            "x-api-key": self.api_key,
            "Accept-Encoding": "gzip", # i don't get this yet
            "Accept": format.value, # default is xml
        }
        # track the URL for each request -- if we're requesting the same data again we
        # want to use a URL from the previous response
        # structure is standard URL > next URL
        self.queries = dict()

    def _get_url_for_query(self, params: QueryParameters) -> str:
        """
        If the same query has gone through, pull the nextrequest url, otherwise send
        the standard one.
        """
        next_url = self.queries.get(params.full_url)
        if next_url is None:
            return params.full_url
        else:
            if self.logger is not None:
                self.logger.info(
                    f"Retrieved request URL from a previous query with the same parameters: {next_url}"
                )
            return next_url
    
    def _request_url_for_query(self, url: str) -> requests.Response:
        """
        Send the request and handle the response.
        """
        if self.logger is not None:
            self.logger.info(f"Sending request to {url}")
        response_raw = requests.get(url=url, headers=self.headers)
        # raises an error if the request didn't go through
        utils.handle_error_codes(response_raw)
        return response_raw

    def query(self, params: QueryParameters, num_retries: int = 3) -> list[ResponseParser]:
        """
        Makes a request for a given set of parameters. If the quota limit is exceeded, waits
        and retries. Returns a list of the responses.
        """
        # loads the request URL
        req_url = self._get_url_for_query(params)
        
        # api docs recommend waiting 5-10s for a quota limit exceeded error
        tries_so_far = 0
        while tries_so_far < num_retries:
            try:
                response_raw = self._request_url_for_query(req_url)
                break
            except exceptions.QuotaLimitExceededError:
                if self.logger is not None:
                    self.logger.info(f"Exceeded the quota limit. Will retry in 5 seconds...")
                time.sleep(5)
                tries_so_far += 1
        
        if isinstance(params, elections.ElectionParameters):
            resp = ElectionsResponse(response_raw, self.format)

            # record the returned next URL if it exists, otherwise raise a warning
            if resp.next_url is None:
                raise exceptions.NoNextURLWarning()
            else:
                if self.logger is not None:
                    self.logger.info(f"Saved a URL for the next request with these parameters.")
                self.queries[params.full_url] = resp.next_url
            
            # when a response is truncated, you're supposed to keep requesting the same data until the
            # flag becomes false
            if resp.is_truncated():
                if self.logger is not None:
                    self.logger.info("Response was truncated, will resend the request.")
                # uses recursion -- does this work!?
                return [resp] + self.query(params)
            else:
                return [resp]
    
        # TODO: for each data type, we need to implement the response class and handle 
        # the response appropriately
        elif isinstance(params, election_reports.ElectionReportParameters):
            pass
        elif isinstance(params, adv_turnout.AdvTurnoutParameters):
            pass
        elif isinstance(params, delegates.DelegateParameters):
            pass

        return response_raw