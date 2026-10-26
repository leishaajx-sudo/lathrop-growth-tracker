# Project Charter: Lathrop Growth Tracker

*Fill in every section marked with a prompt. Target: one page. Finish by Fri Oct 23. Delete the prompts when you are done.*

**Owner:** Leisha Jhamb  **Start:** Oct 21, 2026  **Target finish:** Nov 29, 2026  **Version:** 0.1

## 1. Business question

*One sentence. Use the form "Where/Which/How ..., so that [someone] can [decide something]."*

## 2. Decision and stakeholder persona

*Who makes the decision this project supports? Give them a role, a situation, and a deadline. Example: "An owner of a small cafe or fitness studio deciding which Lathrop district to open in within the next 12 months."*

- **Persona:**
- **Decision they face:**
- **What they would do differently based on the answer:**

## 3. Scope

| In scope | Out of scope |
| --- | --- |
| Residential and commercial permits in the city's monthly reports | Parcel-level or address-level site selection |
| *(add)* | Financial projections for a specific business |
| *(add)* | *(add)* |

## 4. Success criteria

*Three statements a reviewer could check. Example: "The parsed permit counts match the district totals printed in at least 95% of monthly reports."*

1.
2.
3.

## 5. Deliverables and dates

| Deliverable | Due | Done when |
| --- | --- | --- |
| Clean permit database with data dictionary | Nov 1 | One command rebuilds it from the raw PDFs |
| SQL queries and EDA notebook | Nov 8 | Five findings, each with a number |
| Context layers and source triangulation | Nov 15 | Written reason for the primary source of each metric |
| Opportunity score, sensitivity analysis, forecast | Nov 22 | Rank stability and backtest error reported |
| Dashboard, one-page memo, polished repo | Nov 29 | A friend can reproduce it from the README |

## 6. Data sources

*List each source, what you will use it for, and one known weakness. Start from the table in the README.*

## 7. Assumptions

*What are you assuming that could be wrong? Example: "Finaled permits for new single-family homes indicate households moving in within a few months."*

-

## 8. Risks and responses

| Risk | Likelihood (L/M/H) | Impact (L/M/H) | Response |
| --- | --- | --- | --- |
| PDF layout changes between months | M | H | Parse a sample of every month early; log exceptions |
| Some months are missing or labeled inconsistently | H | M | Build the manifest by hand; state gaps in the memo |
| Public sources disagree on prices and income | H | M | Triangulation table; pick one primary source per metric |
| Interviews fall through | M | M | Send five requests; ask the city's public staff for questions by email |
| Scope creep | H | M | Weeks 4 and 5 are stretch goals; drop them before the validation work |

## 9. Stakeholders and interviews

| Name or role | Why them | Contacted (date) | Interview (date) | Notes file |
| --- | --- | --- | --- | --- |
| | | | | |

## 10. How we will work

- One commit per day, with a message that says what changed and why.
- Three lines in `docs/weekly_log.md` after every session: done, blocked, next.
- A decision log entry whenever scope, a KPI, or a method changes.
- A Sunday retro: shipped, slipped, decisions, risks, next week.
