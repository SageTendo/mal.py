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


class ForbiddenError(Exception):
    """Exception when the API returns a 403 status code"""

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
