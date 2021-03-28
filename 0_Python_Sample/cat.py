@single_request_timeout.setter
def single_request_timeout(self, value):
    """The timeout (seconds) for a single HTTP REST API request."""
    check_type(value, int, optional=True)
    if value is not None and value <= 0:
        raise ValueError("single_request_timeout must be positive integer")
    self._single_request_timeout = value