import requests
import pandas as pd
from typing import Union
import xml.etree.ElementTree as ET

import _fields as f
from response_schema._base_response import ResponseParser

class ElectionsResponse(ResponseParser):
    format: f.Format
    response: Union[dict, ET.ElementTree]

    def is_truncated(self) -> bool:
        """
        The response might be truncated if it's long, in which case the client
        should keep requesting the next URL to get complete data.
        """
        if self.format == f.Format.XML:
            key = "IsTruncated"
        elif self.format == f.Format.JSON:
            key = "isTruncated"
        return self.response.get(key) == "true"