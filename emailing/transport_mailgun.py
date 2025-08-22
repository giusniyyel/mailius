#  Copyright (c) 2025 Giusniyyel
#
#  This source code is licensed. For terms of use, redistribution, and contributions,
#  please visit: https://giusniyyel.dev/software/license
import requests


class MailgunTransport:
  """
  Thin wrapper around the Mailgun HTTP API.
  """

  def __init__(self, domain: str, api_key: str, base_url: str):
    self.domain = domain
    self.api_key = api_key
    self.base_url = base_url.rstrip("/")

  def send(
      self,
      *,
      from_email: str,
      to_email: str,
      subject: str,
      text_body: str,
      html_body: str
  ) -> None:
    endpoint = f"{self.base_url}/v3/{self.domain}/messages"

    data = [
      ("from", from_email),
      ("to", to_email),
      ("subject", subject),
      ("text", text_body),
      ("html", html_body),
    ]
    resp = requests.post(endpoint, auth=("api", self.api_key), data=data, timeout=20)
    resp.raise_for_status()
