class BadRequestError(Exception):
    """Exception when the API returns a 400 status code"""

    def __init__(self, response, message):
        self.response = response
        self.message = message
        super().__init__(response, message)


class UnauthorizedError(Exception):
    """Exception when the API returns a 401 status code"""

    def __init__(self, response, message):
        self.response = response
        self.message = message
        super().__init__(response, message)


class NotFoundError(Exception):
    """Exception when the API returns a 404 status code"""

    def __init__(self, response, message):
        self.response = response
        self.message = message
        super().__init__(response, message)


class HTTPError(Exception):
    """Generic HTTP exception error when the API returns a non-200 status code"""

    def __init__(self, response, message):
        self.response = response
        self.message = message
        super().__init__(response, message)
