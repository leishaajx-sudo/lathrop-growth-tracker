# Lathrop Growth Tracker

An independent analytics project that turns the City of Lathrop's public building-permit reports into a clean database and dashboard, to help a local business decide where to locate as River Islands and the rest of Lathrop grow.

> **Status:** Week 1 of 6 (started Oct 21, 2026). Update the table below every Sunday.

| Week | Dates | Milestone | Status |
| --- | --- | --- | --- |
| 1 | Oct 21 - Oct 25 | Charter, KPI definitions, backlog, interview outreach | In progress |
| 2 | Oct 26 - Nov 1 | Permit PDFs downloaded, parsed, reconciled to printed totals | Not started |
| 3 | Nov 2 - Nov 8 | Clean data model, 10 SQL queries, EDA notebook | Not started |
| 4 | Nov 9 - Nov 15 | Pipeline, Zillow, and Census layers; source triangulation | Not started |
| 5 | Nov 16 - Nov 22 | Opportunity score, sensitivity analysis, forecast | Not started |
| 6 | Nov 23 - Nov 29 | Dashboard, one-page memo, repo polish | Not started |

## Business question

Where in Lathrop is housing growth turning into customer demand, and which district should a new local business (for example, a cafe or fitness studio) prioritize?

*(Edit this after you write `docs/charter.md` on Friday.)*

## Key findings

*(Fill in during Week 6. Three findings, one line each, each with a number and a link to the query or notebook that produced it.)*

1. TBD
2. TBD
3. TBD

## Data sources

| Source | What it provides | Format | Notes |
| --- | --- | --- | --- |
| City of Lathrop, monthly permit reports | Permits issued and permits finaled, by district | PDF | One file per month per report type; file names are inconsistent |
| City of Lathrop, residential project pipeline report | Approved projects by tract, builder, and units | PDF | Check for a newer edition than Aug 2025 |
| City of Lathrop, economic development update | Population, growth ranking, household size | PDF | Council meeting item, Aug 10, 2026 |
| Zillow Research Data (ZHVI) | Home value index by city and ZIP code | CSV | Download in Week 4 |
| U.S. Census Bureau, ACS 5-year | Income, tenure, age, household size, with margins of error | API | Free API key; ACS lags fast-growing areas |

## Repository structure

```
lathrop-growth-tracker/
  README.md
  requirements.txt
  data/
    raw/          original PDFs and downloads (not tracked by git)
    clean/        cleaned tables and exports
    manifest.csv  one row per downloaded file: type, month, URL, hash
  src/            parser and pipeline code
  tests/          pytest tests for the parser and scoring function
  sql/            numbered SQL files (schema, queries)
  notebooks/      exploratory analysis
  dashboard/      dashboard file and screenshots
  docs/           charter, KPIs, logs, memo, data dictionary
```

## How to reproduce

*(Fill in as you build. A friend should be able to run these from a clean checkout.)*

```
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
# 1. download PDFs listed in data/manifest.csv   -> TBD command
# 2. parse PDFs into the database                -> TBD command
# 3. run SQL and notebooks                       -> TBD command
```

## Methods and assumptions

*(Summarize in Week 6. Link to `docs/cleaning_rules.md`, `docs/source_triangulation.md`, and `docs/scoring_method.md`.)*

## Limitations

*(Be specific. Examples: permits are a leading indicator, not residents; ACS lags new development; fewer than three years of monthly data limits forecasting; pipeline units may overlap with permits already issued.)*

## About

Independent student project by Leisha Jhamb using only public data. Not affiliated with, or endorsed by, the City of Lathrop, River Islands, or any business named in the data.
