class UnsupportedProviderException(Exception):
    """Raised when oAuth provider is not supported"""


class AuthenticationException(Exception):
    def __init__(self, message: str = "Authentication failed"):
        super().__init__(message)
