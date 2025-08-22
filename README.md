# 📬 Daily Reddit News Digest (Mailius)

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![License](https://img.shields.io/badge/license-Custom-green.svg)

## 📖 Overview
**Mailius** is a Python-based application that automatically collects, summarizes, and delivers trending posts from Reddit straight to your inbox. It saves you from endless scrolling and provides a clean, daily digest of what’s happening across the subreddits you care about most.

---

## 🌍 The Problem It Solves

Reddit is one of the fastest places to discover what’s new and what’s trending, but manually browsing it every day is **time-consuming and overwhelming**.  
This project was born from a simple need:

> *I wanted to stay informed about news and trends without spending hours scrolling through Reddit threads.*

Mailius automates that process by:
1. Fetching Reddit’s top posts of the day.
2. Summarizing them into concise, skimmable descriptions with **OpenAI GPT-4o Mini**.
3. Wrapping them in a **beautifully designed HTML and text email** using Jinja2.
4. Delivering them reliably through **Mailgun**.

---

## 🏗️ Why This Architecture?

### Reasoning
The architecture follows a **modular and layered design** that ensures:
- **Separation of concerns**: scraping, summarizing, rendering, and sending are handled independently.
- **Scalability**: easily extendable (e.g., add new transports like SendGrid or other sources beyond Reddit).
- **Maintainability**: each module has a clear purpose, reducing complexity.
- **Security**: sensitive credentials are stored in environment variables via `.env`.

### Components
- **Reddit Scraper**
    - Library: [PRAW](https://praw.readthedocs.io/)
    - Reason: Simplifies working with Reddit’s API. Handles authentication, subreddit navigation, and post fetching in a clean, Pythonic way.

- **Summarizer**
    - Library: [OpenAI API](https://platform.openai.com/) (GPT-4o Mini)
    - Reason: Generates concise, clear summaries for posts. Ensures information is digestible in under 15 seconds.

- **Email Renderer**
    - Library: [Jinja2](https://jinja.palletsprojects.com/)
    - Reason: Keeps presentation (HTML/text templates) separate from logic. Provides clean and customizable formatting.

- **Email Transport**
    - Library: [Mailgun](https://www.mailgun.com/)
    - Reason: Reliable and developer-friendly email API. Offers robust delivery, detailed logs, and integration flexibility.

---

## 📂 Project Structure
```
mailius/
├── config/              # Settings and environment configuration
├── emailing/            # Rendering + sending (Jinja2 + Mailgun)
│   ├── templates/       # Email templates (.j2 files)
├── services/            # Scraper, summarizer, affirmation service
├── utils/               # Helpers and shared utilities
├── main.py              # Entry point
├── requirements.txt     # Dependencies
└── README.md
```

---

## ⚙️ Setup Instructions

### Prerequisites
- Python 3.9 or higher
- Pip (Python’s package manager)
- Mailgun account (for sending emails)
- OpenAI API key (for summaries)
- Reddit API credentials (client ID, client secret, user agent)

### Steps
1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/daily-reddit-news-digest.git
   cd daily-reddit-news-digest
   ```

2. **Set up a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
    - Create a `.env` file in the project root.
    - Use `.env.example` as a reference.
    - Add your keys:
      ```env
      MAILGUN_API_KEY=your_key
      MAILGUN_DOMAIN=news.giusniyyel.dev
      OPENAI_API_KEY=your_openai_key
      REDDIT_CLIENT_ID=your_id
      REDDIT_CLIENT_SECRET=your_secret
      REDDIT_USER_AGENT=DailyRedditDigest/0.1
      ```

5. **Run the application**
   ```bash
   python main.py
   ```

---

## 🖼️ Demo Screenshot

Here’s an example of how the **Daily Reddit News Digest** looks when delivered to your inbox:

![Demo Screenshot](assets/mailius_working.png)

> ✨ The email includes subreddit sections, post summaries, links, and a positive affirmation, all beautifully formatted.

---

## 🔄 What Happens Behind the Scenes
1. The application fetches with **praw** the top posts from configured subreddits.
2. Posts are summarized via **OpenAI GPT-4o Mini**.
3. A digest email is generated using **Jinja2 templates** (HTML + plain text).
4. The email is delivered to recipients using **Mailgun**.

---

## 📦 Dependencies
- **praw** → Interacting with Reddit’s API
- **requests** → Fetching affirmations and APIs
- **jinja2** → Email rendering engine
- **openai** → Summarization using GPT-4o Mini
- **python-dotenv** → Manage `.env` variables

---

## 📜 License
This project is licensed under the terms specified in the LICENSE file.  
For more details, visit [giusniyyel.dev/software/license](https://giusniyyel.dev/software/license).

# ❤️ **Credits**  
Created with passion by **Giusniyyel** to make staying updated a joy instead of a chore.  
Daily news, but simplified, summarized, and beautifully delivered.  