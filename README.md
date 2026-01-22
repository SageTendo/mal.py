# mal.py

A basic async MyAnimeList (MAL) API wrapper for Python. Based off of [mal-stremio](https://github.com/SageTendo/mal-stremio-addon)'s MAL client.

Features:

- OAuth Flow
- Fetching User Details
- Fetching User Anime List
- Searching Anime
- Fetching Anime Details
- Updating Anime Watch Status
- Type Hinting
- JSON → Python objects

## Installation

```bash
pip install git+https://github.com/SageTendo/mal.py.git
```

## Usage

### OAuth Flow

```python
from mal import Client

client_id = "your_client_id"
client_secret = "your_client_secret"
redirect_uri = "http://localhost:5000/callback"

client = Client(
    client_id=client_id, client_secret=client_secret, callback_url=redirect_uri
)

auth_url, code_verifier = client.get_auth()
```

### Get User Details

```python
async def main():
  client_id = "your_client_id"
  client_secret = "your_client_secret"
  redirect_uri = "http://localhost:5000/callback"

  client = Client(
      client_id=client_id, client_secret=client_secret, callback_url=redirect_uri
  )

  user = await client.get_user_details(token=token)
  print(user)

asyncio.run(main())

# <User(id=1, name=SageTendo)>
```

### Get User Anime List

```python
async def main():
  client_id = "your_client_id"
  client_secret = "your_client_secret"
  redirect_uri = "http://localhost:5000/callback"

  client = Client(
      client_id=client_id, client_secret=client_secret, callback_url=redirect_uri
  )

  anime_list = await client.get_user_anime_list(token=token, limit=1)
  print(anime_list)

asyncio.run(main())

# [<Anime(id=1, title=Cowboy Bebop)>]
```

### Search Anime

```python
async def main():
  client_id = "your_client_id"
  client_secret = "your_client_secret"
  redirect_uri = "http://localhost:5000/callback"

  client = Client(
      client_id=client_id, client_secret=client_secret, callback_url=redirect_uri
  )

  anime_list = await client.search_anime(query="one piece", limit=1)
  print(anime_list)

asyncio.run(main())

# [<Anime(id=1, title=One Piece)>]
```

### Get Anime Details

```python
async def main():
  client_id = "your_client_id"
  client_secret = "your_client_secret"
  redirect_uri = "http://localhost:5000/callback"

  client = Client(
      client_id=client_id, client_secret=client_secret, callback_url=redirect_uri
  )

  anime = await client.get_anime_details(anime_id="1")
  print(anime.title)

asyncio.run(main())

# <Title(original=One Piece, english=One Piece, japanese=ワンピース)>
```

### Update Watched Status

```python
async def main():
  client_id = "your_client_id"
  client_secret = "your_client_secret"
  redirect_uri = "http://localhost:5000/callback"

  client = Client(
      client_id=client_id, client_secret=client_secret, callback_url=redirect_uri
  )

  watch_status = await client.update_watched_status(
    token=token,
    anime_id="1",
    episode=1,
    status="watching",
    start_date="2022-01-01",
  )
  print(watch_status)

asyncio.run(main())

# <WatchStatus(anime_id=1, status=watching, num_watched_episodes=1, start_date=2022-01-01, finish_date=None)>
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
