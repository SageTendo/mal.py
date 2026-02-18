from aiohttp import ClientResponse


class HTTPError(Exception):
    """Generic HTTP exception error"""

    def __init__(self, response: ClientResponse, message: str, code: int):
        self.response: ClientResponse = response
        self.message: str = message
        self.code: int = code
        super().__init__(message)

    def __str__(self):
        return f"HTTP {self.code}: {self.message}"


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

    def __init__(self, response: ClientResponse, message: str):
        super().__init__(response, message, 400)


class UnauthorizedError(HTTPError):
    """Exception when the API returns a 401 status code"""

    def __init__(self, response: ClientResponse, message: str):
        super().__init__(response, message, 401)


class ForbiddenError(HTTPError):
    """Exception when the API returns a 403 status code"""

    def __init__(self, response: ClientResponse, message: str):
        super().__init__(response, message, 403)


class NotFoundError(HTTPError):
    """Exception when the API returns a 404 status code"""

    def __init__(self, response: ClientResponse, message: str):
        super().__init__(response, message, 404)
