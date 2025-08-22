#  Copyright (c) 2025 Giusniyyel
#
#  This source code is licensed. For terms of use, redistribution, and contributions,
#  please visit: https://giusniyyel.dev/software/license
from __future__ import annotations
from datetime import datetime
from pathlib import Path
from typing import Dict
from jinja2 import Environment, FileSystemLoader, select_autoescape
from services.scrapper import SUBREDDIT_EMOJIS

def _env(templates_dir: str | Path) -> Environment:
  env = Environment(
      loader=FileSystemLoader(str(templates_dir)),
      autoescape=select_autoescape(enabled_extensions=("j2", "html", "xml")),
      trim_blocks=True,
      lstrip_blocks=True,
  )
  # Filters / globals for templates
  env.globals["SUBREDDIT_EMOJIS"] = SUBREDDIT_EMOJIS
  env.filters["default_if_empty"] = lambda v, d: v if (v is not None and str(v).strip()) else d
  return env

def render_email_html(
    product_name: str,
    summaries: Dict[str, list[dict]],
    run_dt: datetime,
    affirmation: str,
    *,
    templates_dir: str | Path = Path(__file__).with_suffix("").parent / "templates",
) -> str:
  env = _env(templates_dir)
  tpl = env.get_template("email.html.j2")
  html = tpl.render(
      product_name=product_name,
      summaries=summaries,
      run_dt=run_dt,
      affirmation=affirmation,
  )
  return html

def render_email_text(
    product_name: str,
    summaries: Dict[str, list[dict]],
    run_dt: datetime,
    affirmation: str,
    *,
    templates_dir: str | Path = Path(__file__).with_suffix("").parent / "templates",
) -> str:
  env = _env(templates_dir)
  tpl = env.get_template("email.txt.j2")
  text = tpl.render(
      product_name=product_name,
      summaries=summaries,
      run_dt=run_dt,
      affirmation=affirmation,
  )
  # ensure trailing newline stripped
  return text.strip()

