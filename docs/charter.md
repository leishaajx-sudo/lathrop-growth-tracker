# Project Charter: Lathrop Growth Tracker

**Owner:** Leisha Jhamb  **Start:** Oct 26, 2026  **Target finish:** Dec 6, 2026  **Version:** 1.0 (draft)

## 1. Business question

Which district of Lathrop has the strongest and most reliable new-housing growth, so a small local business can decide where to open in the next 12 months?

## 2. Decision and stakeholder persona

- **Persona:** The owner of a small cafe or fitness studio in the Lathrop area.
- **Decision they face:** Which district to open in within the next 12 months.
- **What they would do differently:** Choose the district where finished homes are arriving fastest and building will continue, instead of going by reputation or general population figures.

## 3. Scope

| In scope | Out of scope |
| --- | --- |
| Monthly City of Lathrop permit reports (issued and finaled), all districts | Address-level or parcel-level site selection |
| City residential pipeline report (approved projects and units) | Financial projections for a specific business |
| Home values (Zillow) and household data (Census ACS) as context | Foot-traffic, sales, or customer data |
| A district opportunity score with sensitivity testing | Predicting home prices |

## 4. Success criteria

1. For every report parsed, the district counts and the grand total match the totals printed in the report, and every mismatch is explained in `docs/validation_log.md`.
2. Someone else can rebuild the database and dashboard from the README alone.
3. A one-page memo recommends one district, gives three numbered findings, states its limits, and has been reviewed by at least one person outside the project.

## 5. Deliverables and dates

| Deliverable | Due | Done when |
| --- | --- | --- |
| Charter, KPI definitions, backlog, interview requests sent | Nov 1 | All four exist in the repo |
| Clean permit database with data dictionary | Nov 8 | One command rebuilds it from the raw PDFs |
| SQL queries and EDA notebook | Nov 15 | Five findings, each with a number |
| Context layers and source triangulation | Nov 22 | Written reason for the primary source of each metric |
| Opportunity score, sensitivity analysis, forecast | Nov 29 | Rank stability and backtest error reported |
| Dashboard, one-page memo, polished repo | Dec 6 | A friend can reproduce it from the README |

## 6. Data sources

| Source | Use | Known weakness |
| --- | --- | --- |
| City monthly permit reports, issued and finaled (PDF) | Core dataset | Layout quirks; permits split across pages; older months may be unavailable |
| City residential pipeline report (PDF, Aug 2025 edition) | Remaining building ahead | May overlap with permits already issued |
| Zillow Home Value Index (CSV) | Price context | An index, not actual sale prices |
| Census ACS 5-year (API) | Income, household size, tenure | Lags fast-growing areas; has margins of error |

## 7. Assumptions

- A finaled new single-family permit means a household moves in within a few months.
- Base-case occupancy of finished homes is 90% (tested at 80% and 100%).
- The permit reports are complete and accurate for the months they cover.

## 8. Risks and responses

| Risk | Likelihood (L/M/H) | Impact (L/M/H) | Response |
| --- | --- | --- | --- |
| Only recent months are available (older links return 404) | M | H | Confirm available months in Week 2; shrink the trend and forecast work to match |
| PDF layout changes between months | M | H | Parse a sample of every month early; log exceptions |
| Permits split across page breaks or text collides | H | M | Parse words by position, as one stream across pages |
| Public sources disagree on prices and income | H | M | Triangulation table; one primary source per metric |
| Interviews fall through | M | M | Send five requests; use public city staff material as a fallback |
| Scope creep | H | M | Context layers (Week 4) and score and forecast (Week 5) shrink first; the Week 2-3 parser and validation work is never cut |

## 9. Stakeholders and interviews

| Name or role | Why them | Contacted (date) | Interview (date) | Notes file |
| --- | --- | --- | --- | --- |
| City of Lathrop Economic Development | Official view of growth and business support | Oct 29 | | |
| Chamber of Commerce | Voice of local small businesses | Oct 29 | | |
| Reena, realtor | Buyer demand by area | Oct 29 | | |
| David, realtor | Buyer demand and new-home sales | Oct 29 | | |
| Local gym (info@ contact) | A small owner's view of choosing a location | Oct 29 | | |

## 10. How we will work

- One commit per day, with a message that says what changed and why.
- Three lines in `docs/weekly_log.md` after every session: done, blocked, next.
- A decision log entry whenever scope, a KPI, or a method changes.
- A Sunday retro: shipped, slipped, decisions, risks, next week.
