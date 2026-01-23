__title__ = "mal"
__version__ = "0.0.1"
__author__ = "SageTendo"
__license__ = "MIT"
__copyright__ = "Copyright 2026-present SageTendo"

__all__ = (
    "Client",
    "BadRequestError",
    "UnauthorizedError",
    "ForbiddenError",
    "NotFoundError",
    "HTTPError",
    "InputError",
    "AuthenticationError",
    "OAuthConfigError",
    "Anime",
    "User",
    "Auth",
    "Relation",
    "Statistics",
    "Title",
    "WatchStatus",
    "NSFW",
    "IMAGE_SIZE",
    "ANIME_STATUS",
    "USER_LIST_SORT",
    "USER_ANIME_STATUS",
    "MEDIA_TYPE",
    "ANIME_SOURCE",
    "ANIME_RATING",
    "RELATION_TYPE",
)

from .types import (
    IMAGE_SIZE,
    NSFW,
    ANIME_STATUS,
    USER_LIST_SORT,
    USER_ANIME_STATUS,
    MEDIA_TYPE,
    ANIME_SOURCE,
    ANIME_RATING,
    RELATION_TYPE,
)
from .client import Client
from .errors import (
    BadRequestError,
    UnauthorizedError,
    ForbiddenError,
    NotFoundError,
    HTTPError,
    InputError,
    AuthenticationError,
    OAuthConfigError,
)
from .models import (
    User,
    Auth,
    Anime,
    Relation,
    Statistics,
    Title,
    WatchStatus,
)
