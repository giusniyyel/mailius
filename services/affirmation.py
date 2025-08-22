#  Copyright (c) 2025 Giusniyyel
#
#  This source code is licensed. For terms of use, redistribution, and contributions,
#  please visit: https://giusniyyel.dev/software/license
from __future__ import annotations

import requests

from config.settings import AFFIRMATION_API_URL

DEFAULT_AFFIRMATION_FALLBACK = "You are moving forward, one step at a time."


def get_affirmation(timeout_sec: float = 6.0) -> str:
  """
  Fetches a JSON from https://www.affirmations.dev/ and returns the `affirmation` value.
  Falls back to DEFAULT_FALLBACK on any error or missing key.
  """
  try:
    resp = requests.get(AFFIRMATION_API_URL, timeout=timeout_sec)
    resp.raise_for_status()
    data = resp.json()
    text = (data or {}).get("affirmation", "").strip()
    if text:
      # keep it single-line (email-header-friendly)
      return " ".join(text.split())
  except (requests.RequestException, ValueError, KeyError):
    pass
  return DEFAULT_AFFIRMATION_FALLBACK
