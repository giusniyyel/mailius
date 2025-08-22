#  Copyright (c) 2025 Giusniyyel
#
#  This source code is licensed. For terms of use, redistribution, and contributions,
#  please visit: https://giusniyyel.dev/software/license
from openai import OpenAI
from openai.types.chat import ChatCompletionMessage, \
  ChatCompletionUserMessageParam, ChatCompletionSystemMessageParam

from config.settings import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def summarize_posts(title, body=None, subreddit=None):
  text = f"Title: {title}\n"
  if body:
    text += f"Body: {body}\n"
  if subreddit:
    text += f"Subreddit: {subreddit}\n"

  response = client.chat.completions.create(
      model="gpt-4o-mini",  # fast and cheap
      messages=[
        ChatCompletionSystemMessageParam(
            role="system",
            content="""You are an AI assistant summarizing Reddit posts.
            Inputs: subreddit, title, body (optional).
            Style: reporter-like, direct, concise, clear.
            Task: Summarize in 2–3 sentences (≤40 words), skimmable.
            Rules:
            - Context + key facts only; prefer body over title.
            - Use ONLY given text; no filler or commentary.
            - If subjective/first-person → user’s post; if factual/event → news.
            - Treat bracket tags ([KDE],[OC], etc.) as context, not sources.
            - Output ONLY the summary.
            """
        ),
        ChatCompletionUserMessageParam(role="user", content=text)
      ],
      temperature=0.3
  )

  return response.choices[0].message.content.strip()


def get_summaries(posts):
  summaries = {}
  for sub_name, sub_posts in posts.items():
    summaries[sub_name] = []
    for post in sub_posts:
      title = post.get("title")
      body = post.get("selftext")
      summary = summarize_posts(title, body, sub_name)
      summaries[sub_name].append({
        "title": title,
        "summary": summary,
        "url": post.get("url"),
        "score": post.get("score"),
        "permalink": post.get("permalink"),
        "created_utc": post.get("created_utc"),
        "author": post.get("author")
      })

  return summaries
