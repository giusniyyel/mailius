#  Copyright (c) 2025 Giusniyyel
#
#  This source code is licensed. For terms of use, redistribution, and contributions,
#  please visit: https://giusniyyel.dev/software/license
from datetime import datetime, timezone
from typing import Dict, List, Optional, Sequence

from services.affirmation import get_affirmation
from emailing.renderer import render_email_html, render_email_text
from emailing.transport_mailgun import MailgunTransport


class EmailService:
  """
  Orchestrates rendering and transport; public API is send_digest(summaries).
  """

  def __init__(
      self,
      *,
      from_email: str,
      to_emails: Sequence[str] | str,
      product_name: str = "Daily Reddit News Digest",
      # Mailgun
      mailgun_domain: Optional[str] = None,
      mailgun_api_key: Optional[str] = None,
      mailgun_base_url: Optional[str] = None,
  ):
    self.from_email = from_email
    self.product_name = product_name

    # Normalize recipients immediately
    if isinstance(to_emails, str):
      self.to_emails = [e.strip() for e in to_emails.split(",") if e.strip()]
    else:
      self.to_emails = list(to_emails)

    self.transport = MailgunTransport(
        domain=mailgun_domain,
        api_key=mailgun_api_key,
        base_url=mailgun_base_url,
    )

  # ---------- public ----------
  def send_digest(self, summaries: Dict[str, List[dict]]) -> None:
    run_dt = datetime.now(timezone.utc)
    subject = f"📬 {self.product_name} — {run_dt.strftime('%B %d')}"
    affirmation = get_affirmation()  # < -- fetch once per run
    html_body = render_email_html(self.product_name, summaries, run_dt,
                                  affirmation)
    text_body = render_email_text(self.product_name, summaries, run_dt,
                                  affirmation)

    # Send the email to each recipient individually
    for addr in self.to_emails:
      self.transport.send(
          from_email=self.from_email,
          to_email=addr,
          subject=subject,
          text_body=text_body,
          html_body=html_body,
      )
