from aiohttp import ClientResponse


class HTTPError(Exception):
    """Generic HTTP exception error"""

    def __init__(self, response, message):
        self.response: ClientResponse = response
        self.message = message
        self.code = response.status
        super().__init__(response, message, response.status)


class InputError(Exception):
    """Exception when the input is invalid"""

    def __init__(self, message):
        self.message = message
        super().__init__(message)


class AuthenticationError(Exception):
    """Exception when the authentication fails"""

    def __init__(self, message):
        self.message = message
        super().__init__(message)


class OAuthConfigError(Exception):
    """Exception when the OAuth configuration is invalid"""

    def __init__(self, message):
        self.message = message
        super().__init__(message)


class BadRequestError(HTTPError):
    """Exception when the API returns a 400 status code"""

    def __init__(self, response, message):
        super().__init__(response, message)


class UnauthorizedError(HTTPError):
    """Exception when the API returns a 401 status code"""

    def __init__(self, response, message):
        super().__init__(response, message)


class ForbiddenError(HTTPError):
    """Exception when the API returns a 403 status code"""

    def __init__(self, response, message):
        super().__init__(response, message)


class NotFoundError(HTTPError):
    """Exception when the API returns a 404 status code"""

    def __init__(self, response, message):
        super().__init__(response, message)
