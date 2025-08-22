#  Copyright (c) 2025 Giusniyyel
#
#  This source code is licensed. For terms of use, redistribution, and contributions,
#  please visit: https://giusniyyel.dev/software/license
from datetime import timezone, datetime

import praw

from config.settings import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, \
  REDDIT_USER_AGENT

# -------------------
# CONFIG
# -------------------
SCRAPE_CONFIG = {
  "time_filter": "day",  # day, week, month, year, all
  "posts_per_subreddit": 3,
  "default_fields": ["title", "selftext", "url", "score", "permalink", "created_utc", "author"],
  "subreddits": [
    "news",
    "mexico",
    "internationalnews",
    "unixporn",
    "uxdesign",
    "springboot",
    "python",
    "resumes",
    "kotlinmultiplatform"
  ]
}

SUBREDDIT_EMOJIS = {
  "news": "📰",
  "mexico": "🇲🇽",
  "internationalnews": "🌍",
  "unixporn": "💻",
  "uxdesign": "🎨",
  "springboot": "☕",
  "python": "🐍",
  "resumes": "📄",
  "kotlinmultiplatform": "📱",
  "hackintosh": "🍏",
  # fallback default
  "_default": "📌"
}

# -------------------
# REDDIT CLIENT
# -------------------
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT
)


# -------------------
# HELPERS
# -------------------
def format_post(post, fields):
  """Extract and format fields from a Reddit post."""
  entry = {}
  for field in fields:
    if field == "permalink":
      value = f"https://reddit.com{post.permalink}"
    elif field == "created_utc":
      value = datetime.fromtimestamp(
          post.created_utc, tz=timezone.utc
      ).strftime("%Y-%m-%d %H:%M:%S UTC")
    elif field == "author":
      value = post.author.name if post.author else "[deleted]"
    else:
      value = getattr(post, field, None)
    entry[field] = value
  return entry


def get_subreddit_posts(subreddit_name, config, today):
  """Fetch top posts for a single subreddit."""
  subreddit = reddit.subreddit(subreddit_name)
  posts_data = []

  for post in subreddit.top(
      time_filter=config["time_filter"],
      limit=config["posts_per_subreddit"] * 3,
  ):
    post_date = datetime.fromtimestamp(post.created_utc, tz=timezone.utc).date()
    if post_date == today:
      posts_data.append(format_post(post, config["default_fields"]))
    if len(posts_data) >= config["posts_per_subreddit"]:
      break

  return posts_data


# -------------------
# MAIN FUNCTION
# -------------------
def scrape_reddit():
  today = datetime.now(timezone.utc).date()
  results = {}

  for sub_name in SCRAPE_CONFIG["subreddits"]:
    posts = get_subreddit_posts(sub_name, SCRAPE_CONFIG, today)
    if posts:
      results[sub_name] = posts

  return results
