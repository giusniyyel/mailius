#  Copyright (c) 2025 Giusniyyel
#
#  This source code is licensed. For terms of use, redistribution, and contributions,
#  please visit: https://giusniyyel.dev/software/license
from config.settings import SENDER_EMAIL, RECIPIENT_EMAILS, PRODUCT_NAME, \
  MAILGUN_DOMAIN, MAILGUN_API_KEY, MAILGUN_BASE_URL
from emailing.service import EmailService
from services.scrapper import scrape_reddit
from services.summarizer import get_summaries

if __name__ == "__main__":
  print("🚀 Starting the Reddit News Digest process...")

  print("🔍 Start searching for Reddit posts...")
  posts = scrape_reddit()
  print(f"✅ Scraped {sum(len(sub_posts) for sub_posts in posts.values())} Reddit posts.")

  print("📝 Start summarizing posts...")
  summaries = get_summaries(posts)
  print(f"✅ Summarized {sum(len(posts) for posts in summaries.values())} posts.")

  print("📧 Preparing to send digest...")
  svc = EmailService(
      from_email=SENDER_EMAIL,
      to_emails=RECIPIENT_EMAILS,
      product_name=PRODUCT_NAME,
      mailgun_domain=MAILGUN_DOMAIN,
      mailgun_api_key=MAILGUN_API_KEY,
      mailgun_base_url=MAILGUN_BASE_URL
  )

  print("📤 Sending digest...")
  svc.send_digest(summaries)
  print("✅ Digest sent successfully.")
