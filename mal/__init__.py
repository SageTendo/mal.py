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
    "Anime",
    "User",
    "Auth",
    "Relation",
    "Statistics",
    "Title",
    "WatchStatus",
    "NSFW",
    "ImageSize",
)

from .client import Client
from .errors import (
    BadRequestError,
    UnauthorizedError,
    ForbiddenError,
    NotFoundError,
    HTTPError,
)
from .models import (
    User,
    Auth,
    Anime,
    Relation,
    Statistics,
    Title,
    NSFW,
    ImageSize,
    WatchStatus,
)
