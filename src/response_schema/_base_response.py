import requests
import pandas as pd
from typing import Union
import xml.etree.ElementTree as ET

import fields as f
import utils

"""
Base class for interpreting and manipulating a response. Each of the four data
types should inherit this class.
"""

class ResponseParser():
    format: f.Format
    response: Union[dict, ET.ElementTree]

    def __init__(self, response: requests.Response, format: f.Format) -> None:
        """
        Load the response data based on the type of the request -- JSON or XML.
        """
        self.format = format
        if self.format == f.Format.XML:
            self.response = ET.fromstring(response.text)
        elif self.format == f.Format.JSON:
            self.response = response.json()
    
    @property
    def next_url(self) -> str:
        """
        The API response includes a URL that's supposed to be requested the for 
        updates. Extracts that URL based on the format.
        """
        if self.format == f.Format.XML:
            next_url_elem = self.response.find('{http://www.w3.org/2005/Atom}link')
            if next_url_elem is None or next_url_elem.get("rel") != "next":
                return None
            else:
                return next_url_elem.get("href")
        elif self.format == f.Format.JSON:
            return self.response.get("nextrequest")

    def to_dataframe(self) -> pd.DataFrame:
        """
        Convert the response into a data frame output.
        """
        if self.format == f.Format.JSON:
            return utils.flatten_json(self.response)
        if self.format == f.Format.XML:
            raise Exception("Not implemented yet.")

    def to_csv(self, path: str) -> None:
        """
        Save the response as a CSV.
        """
        df = self.to_dataframe()
        df.to_csv(path)