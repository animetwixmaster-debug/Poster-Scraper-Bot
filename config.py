from dotenv import load_dotenv
import os

load_dotenv("../config.env", override=True)  
load_dotenv("config.env", override=True) 

class Config:
    API_ID = int(os.environ.get("25210379", 0))
    API_HASH = os.environ.get("2f43e4bccc419e3b7e28e3219bb1d68c", "")
    BOT_TOKEN = os.environ.get("8776719581:AAFsgBz1VGO2mSwPwU7wnc2cLjHtYBTn-E0", "")
    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Nandu")
    OWNER_ID = int(os.environ.get("1856765089", 0))
    SUDO_USERS = (
        list(map(int, os.environ.get("SUDO_USERS", "").split()))
        if os.environ.get("SUDO_USERS")
        else []
    )
    AUTH_CHATS = (
        list(map(int, os.environ.get("AUTH_CHATS", "-1003846600411").split()))
        if os.environ.get("AUTH_CHATS")
        else []
    )
    # For Koyeb/render 
    WEB_SERVER = os.environ.get("WEB_SERVER", "false").lower() == "true" # Set True if deploying on koyeb/render else False
    PING_URL = os.environ.get("PING_URL", "https://poster-scraper-bot-2.onrender.com") # koyeb/render's base url
    PING_TIME = int(os.environ.get("PING_TIME", 300))
    PORT = int(os.environ.get("PORT", 8080))
   
    PUBLIC_MODE = os.environ.get("PUBLIC_MODE", "False").lower() == "true"
    TIMEZONE = os.environ.get("TIMEZONE", "Asia/Kolkata")
    
    # TMDB Token is optional bot will use third party proxy (https://tmdbapi.the-zake.workers.dev) if u don't want to set TMDB token 
    TMDB_ACCESS_TOKEN = os.environ.get("TMDB_ACCESS_TOKEN", "")
    
    UPSTREAM_REPO = os.environ.get("UPSTREAM_REPO", "https://github.com/the-piro/pstr")
    UPSTREAM_BRANCH = os.environ.get("UPSTREAM_BRANCH", "main")

    OTT_TEMPLATE = """
<b>📺 Source:</b> {source}
<b>🎬 Title:</b> {title}
<b>📅 Year:</b> {year}
<b>🎞 Type:</b> {type}

<b>🔗 Original URL:</b>
<code>{original_url}</code>

<b>🖼 Posters:</b>
{poster_lines}
""".strip()
    
    IMDB_TEMPLATE = """
<b>🎬 {title}</b> <i>({year})</i>

⭐ <b>Rating:</b> <code>{rating}</code>  
🎭 <b>Genre:</b> {genres}  
🗣 <b>Language:</b> {languages}  
🌍 <b>Country:</b> {countries}  
📅 <b>Release:</b> {release_date}

<b>👥 Cast:</b> {cast}  
🎬 <b>Director:</b> {director}  
🧠 <b>Writer:</b> {writer}

🕒 <b>Runtime:</b> {runtime}  
📦 <b>Box Office:</b> {box_office}  
🎥 <b>Type:</b> {kind}

<b>📝 Story:</b>
<blockquote>{plot}</blockquote>

🔗 <b>IMDb:</b> {url}

<a href="{url_cast}">👀 Full Cast</a> • <a href="{url_releaseinfo}">📅 Release Info</a>
"""
    ANILIST_TEMPLATE = """
<b>🎌 {title}</b> <i>({year})</i>
<code>{romaji}</code>
{native}

🛰 <b>Status:</b> {status} • {season}
🎬 <b>Format:</b> {format}  
📺 <b>Episodes:</b> {episodes} × {duration}
⭐ <b>Score:</b> <code>{score}</code> {score_rank}
📈 <b>Popularity:</b> {popularity} {pop_rank}
💖 <b>Favorites:</b> {favourites}

🎭 <b>Genres:</b> {genres}
🏢 <b>Studio:</b> {studio}
⏭ <b>Next Episode:</b> {next_ep}
📅 <b>Aired:</b> {aired}

🧾 <b>Also known as:</b> {alt_titles}

<b>📝 Synopsis:</b>
<blockquote>{description}</blockquote>

🔗 <b>Links:</b> <a href="{anilist_url}">AniList</a>{mal_link}{ext_links}
"""
    
    BYPASS_TEMPLATE = """
<b>✦ Bypass Result ✦</b>

{header_block}

{meta_block}
<b>╭╴Links:</b>
{links_block}

<b>✺ Original URL:</b>
<code>{original_url}</code>

<blockquote>Bot By ➤ @NaChannel4</blockquote>
""".strip()

    POSER_TEMPLATE = """
{title}

{landscape}

• Logos PNG:
<blockquote expandable>
{logos}
</blockquote>

• Portrait Posters:
<blockquote expandable>
{posters}
</blockquote>

<blockquote>Bot By ➤ @NaChannel4</blockquote>
""".strip()
