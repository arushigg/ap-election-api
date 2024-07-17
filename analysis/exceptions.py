"""
Define custom exceptions to give users a more specific picture of what's gone wrong.
"""

# i think there's room to make this more descriptive -- maybe take a dictionary
# of parameter name to parameter value? 
class InvalidParameterError(Exception):
   def __init__(self, parameter=None, message="Invalid parameter"):
        self.parameter = parameter
        self.message = message
        super().__init__(self.message)

class InvalidAPIKeyError(Exception):
   def __init__(self, message="Invalid API key"):
        self.message = message
        super().__init__(self.message)

class QuotaLimitExceededError(Exception):
  def __init__(self, message="Quota limit exceeded, try again in 5-10s"):
        self.message = message
        super().__init__(self.message)

class RequestMethodNotSupportedError(Exception):
   def __init__(self, message="Request method not supported, only GET requests allowed"):
        self.message = message
        super().__init__(self.message)

class RequestTooLongError(Exception):
   def __init__(self, message="Request is too long, URI cannot be over 6000 characters"):
        self.message = message
        super().__init__(self.message)

class ServerError(Exception):
   def __init__(self, message="Server error, contact AP"):
        self.message = message
        super().__init__(self.message)

class BadGatewayError(Exception):
   def __init__(self, message="Bad gateway, contact AP"):
        self.message = message
        super().__init__(self.message)

class ServiceUnavailableError(Exception):
   def __init__(self, message="Service unavailable, contact AP"):
        self.message = message
        super().__init__(self.message)

class GatewayTimeoutError(Exception):
   def __init__(self, message="Gateway timeout, contact AP"):
        self.message = message
        super().__init__(self.message)

# not sure if this breaks the code, but i think it should just log a warning 
# and move on
class NoNextURLWarning(Warning):
    def __init__(self, message="Response does not include a URL for updates"):
        self.message = message
        super().__init__(self.message)