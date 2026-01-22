from datetime import date, datetime
from typing import TYPE_CHECKING, Literal, Optional


if TYPE_CHECKING:
    from mal.client import Client

ImageSize = Literal["medium", "large"]
NSFW = Literal["white", "gray", "black"]


class Auth:
    """MyAnimeList authorization model"""

    def __init__(self, data):
        self._data = data

    @property
    def token_type(self) -> str:
        return self._data.get("token_type")

    @property
    def expires_in(self) -> int:
        return self._data.get("expires_in")

    @property
    def access_token(self) -> str:
        return self._data.get("access_token")

    @property
    def refresh_token(self) -> str:
        return self._data.get("refresh_token")

    def __repr__(self):
        return f"<Auth(token_type={self.token_type}, expires_in={self.expires_in}, access_token={self.access_token}, refresh_token={self.refresh_token})>"


class User:
    """MyAnimeList user model"""

    def __init__(self, data):
        self._data = data

    @property
    def id(self) -> str:
        return str(self._data.get("id"))

    @property
    def name(self) -> str:
        return self._data.get("name")

    @property
    def picture(self) -> Optional[str]:
        return self._data.get("picture")

    @property
    def gender(self) -> Optional[str]:
        return self._data.get("gender")

    @property
    def birthday(self) -> Optional[date]:
        try:
            date_string = self._data["birthday"]
            return date.fromisoformat(date_string)
        except (KeyError, TypeError, ValueError):
            return None

    @property
    def location(self) -> Optional[str]:
        return self._data.get("location")

    @property
    def joined_at(self) -> Optional[datetime]:
        try:
            date_string = self._data["joined_at"]
            return datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%SZ")
        except (KeyError, TypeError, ValueError):
            return None

    @property
    def anime_stats(self) -> Optional[dict]:
        return self._data.get("anime_stats")

    @property
    def timezone(self) -> Optional[str]:
        return self._data.get("timezone")

    @property
    def is_supporter(self) -> Optional[bool]:
        return self._data.get("is_following")

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name})>"


class Anime:
    """MyAnimeList anime model"""

    def __init__(self, data, *, client: Optional["Client"] = None):
        self._data = data
        self._client = client

    @property
    def id(self) -> str:
        return str(self._data.get("id"))

    @property
    def title(self) -> "Title":
        data = {
            "canonical": self._data.get("title"),
            "english": self._data.get("alternative_titles", {}).get("en"),
            "japanese": self._data.get("alternative_titles", {}).get("ja"),
            "synonyms": self._data.get("alternative_titles", {}).get("synonyms"),
        }
        return Title(data)

    def main_picture(self, size: ImageSize = "large") -> Optional[str]:
        return self._data.get("main_picture", {}).get(size)

    def pictures(self, size: ImageSize = "large") -> list[str]:
        return [
            image[size] for image in self._data.get("pictures", []) if image.get(size)
        ]

    @property
    def start_date(self) -> Optional[date]:
        try:
            date_string = self._data["start_date"]
            return date.fromisoformat(date_string)
        except (KeyError, TypeError, ValueError):
            return None

    @property
    def end_date(self) -> Optional[date]:
        try:
            date_string = self._data["end_date"]
            return date.fromisoformat(date_string)
        except (KeyError, TypeError, ValueError):
            return None

    @property
    def synopsis(self) -> Optional[str]:
        return self._data.get("synopsis")

    @property
    def mean(self) -> Optional[float]:
        return self._data.get("mean")

    @property
    def rank(self) -> Optional[int]:
        return self._data.get("rank")

    @property
    def popularity(self) -> Optional[int]:
        return self._data.get("popularity")

    @property
    def num_list_users(self) -> Optional[int]:
        return self._data.get("num_list_users")

    @property
    def num_scoring_users(self) -> int:
        return self._data.get("num_scoring_users")

    @property
    def nsfw(self) -> Optional[NSFW]:
        return self._data.get("nsfw")

    @property
    def genres(self) -> list[str]:
        return [genre["name"] for genre in self._data.get("genres", [])]

    @property
    def created_at(self) -> Optional[datetime]:
        try:
            date_string = self._data["created_at"]
            return datetime.fromisoformat(date_string)
        except (KeyError, TypeError, ValueError):
            return None

    @property
    def updated_at(self) -> Optional[datetime]:
        try:
            date_string = self._data["updated_at"]
            return datetime.fromisoformat(date_string)
        except (KeyError, TypeError, ValueError):
            return None

    @property
    def media_type(self) -> Optional[str]:
        return self._data.get("media_type")

    @property
    def status(self) -> Optional[str]:
        return self._data.get("status")

    @property
    def my_list_status(self) -> Optional[str]:
        return self._data.get("my_list_status")

    @property
    def num_episodes(self) -> Optional[int]:
        return self._data.get("num_episodes")

    @property
    def year(self) -> Optional[str]:
        return self._data.get("start_season", {}).get("year")

    @property
    def season(self) -> Optional[str]:
        return self._data.get("start_season", {}).get("season")

    @property
    def broadcast(self) -> Optional[str]:
        return self._data.get("broadcast")

    @property
    def source(self) -> Optional[str]:
        return self._data.get("source")

    @property
    def average_episode_duration(self) -> Optional[int]:
        return self._data.get("average_episode_duration")

    @property
    def rating(self) -> Optional[float]:
        return self._data.get("rating")

    @property
    def background(self) -> Optional[str]:
        return self._data.get("background")

    async def related_anime(self) -> list["Relation"]:
        data = self._data.get("related_anime", [])
        return [Relation(anime, client=self._client) for anime in data]

    def recommendations(self) -> Optional[list["Recommendation"]]:
        data = self._data.get("recommendations", [])
        return [Recommendation(anime, client=self._client) for anime in data]

    @property
    def statistics(self) -> Optional["Statistics"]:
        data = self._data.get("statistics")
        if not data:
            return None
        return Statistics(data)

    @property
    def studios(self) -> Optional[list[str]]:
        return [studio["name"] for studio in self._data.get("studios", [])]

    def __repr__(self):
        return f"<Anime(id={self.id}, title={self.title})>"


class Title:
    """Represents the title of an anime"""

    def __init__(self, data):
        self._data = data

    @property
    def canonical(self) -> Optional[str]:
        return self._data.get("canonical")

    @property
    def english(self) -> Optional[str]:
        return self._data.get("english")

    @property
    def japanese(self) -> Optional[str]:
        return self._data.get("japanese")

    @property
    def synonyms(self) -> Optional[list[str]]:
        return self._data.get("synonyms")

    def __str__(self):
        return f"{self.canonical}"

    def __repr__(self):
        return f"<Title(original={self.canonical}, english={self.english}, japanese={self.japanese})>"


class Statistics:
    """Represents the statistics of an anime"""

    def __init__(self, data):
        self._data = data

    @property
    def watching(self) -> int:
        return self._data.get("status", {}).get("watching")

    @property
    def completed(self) -> int:
        return self._data.get("status", {}).get("completed")

    @property
    def on_hold(self) -> int:
        return self._data.get("status", {}).get("on_hold")

    @property
    def dropped(self) -> int:
        return self._data.get("status", {}).get("dropped")

    @property
    def plan_to_watch(self) -> int:
        return self._data.get("status", {}).get("plan_to_watch")

    @property
    def users(self) -> int:
        return self._data.get("num_list_users")

    def __repr__(self):
        return f"<Statistics(watching={self.watching}, completed={self.completed}, on_hold={self.on_hold}, dropped={self.dropped}, plan_to_watch={self.plan_to_watch}, users={self.users})>"


class Relation:
    """Represents a relationship between anime, made by MAL"""

    def __init__(
        self,
        data,
        *,
        client: Optional["Client"] = None,
    ):
        self._data = data
        self._client: Optional["Client"] = client

    @property
    def id(self) -> str:
        return str(self._data.get("node", {}).get("id"))

    @property
    def title(self) -> str:
        return self._data.get("node", {}).get("title")

    @property
    def main_picture(self, size: ImageSize = "large") -> Optional[str]:
        return self._data.get("node", {}).get("main_picture", {}).get(size)

    @property
    def relation_type(self) -> str:
        return self._data.get("relation_type")

    @property
    def relation_type_formatted(self) -> str:
        return self._data.get("relation_type_formatted")

    async def anime(self) -> Optional[Anime]:
        if not self._client:
            raise ValueError("Client instance not provided for relation fetching")
        return await self._client.get_anime_details(anime_id=self.id)

    def __repr__(self):
        return f"<Relation(id={self.id}, relation_type={self.relation_type}, relation_type_formatted={self.relation_type_formatted})>"


class Recommendation:
    """Represents an anime recommendation, made by MAL"""

    def __init__(self, data, *, client: Optional["Client"] = None):
        self._data = data
        self._client = client

    @property
    def id(self) -> str:
        return str(self._data.get("node", {}).get("id"))

    @property
    def title(self) -> str:
        return self._data.get("node", {}).get("title")

    @property
    def main_picture(self, size: ImageSize = "large") -> Optional[str]:
        return self._data.get("node", {}).get("main_picture", {}).get(size)

    @property
    def num_recommendations(self) -> int:
        return self._data.get("num_recommendations")

    async def anime(self) -> Anime:
        if not self._client:
            raise ValueError("Client instance not provided to Recommendation instance")
        return await self._client.get_anime_details(anime_id=self.id)

    def __repr__(self):
        return f"<Recommendation(id={self.id}, title={self.title}, num_recommendations={self.num_recommendations})>"


class WatchStatus:
    """Represents as user's watch status for an anime"""

    def __init__(self, data, *, anime_id: str):
        self._data = data
        self._anime_id = anime_id

    @property
    def anime_id(self) -> str:
        return str(self._anime_id)

    @property
    def status(self) -> Optional[str]:
        return self._data.get("status")

    @property
    def score(self) -> int:
        return self._data.get("score")

    @property
    def num_episodes_watched(self) -> int:
        return self._data.get("num_episodes_watched")

    @property
    def is_rewatching(self) -> bool:
        return self._data.get("is_rewatching")

    @property
    def start_date(self) -> Optional[date]:
        try:
            date_string = self._data["start_date"]
            return date.fromisoformat(date_string)
        except (KeyError, TypeError, ValueError):
            return None

    @property
    def finish_date(self) -> Optional[date]:
        try:
            date_string = self._data["finish_date"]
            return date.fromisoformat(date_string)
        except (KeyError, TypeError, ValueError):
            return None

    @property
    def updated_at(self) -> Optional[datetime]:
        try:
            date_string = self._data["updated_at"]
            return datetime.fromisoformat(date_string)
        except (KeyError, TypeError, ValueError):
            return None

    @property
    def num_rewatches(self) -> int:
        return self._data.get("num_times_rewatched")

    @property
    def rewatch_value(self) -> int:
        return self._data.get("rewatch_value")

    @property
    def tags(self) -> list[str]:
        return self._data.get("tags")

    @property
    def comments(self) -> str:
        return self._data.get("comments")

    def __repr__(self):
        return f"<AnimeID={self.anime_id}, WatchStatus(status={self.status}, num_watched_episodes={self.num_episodes_watched}, start_date={self.start_date}, finish_date={self.finish_date})>"
