# KPI Definitions

Draft v1, Oct 28, 2026. Revisit after interviews.

| # | KPI | Formula | Grain | Source | Known weakness |
| --- | --- | --- | --- | --- | --- |
| 1 | Permits issued per month | Count of distinct permits (permit # without the trailing *) with an Issue Date in the month | Month x district x work-class group | Issued reports | Permits are not finished homes |
| 2 | Issue-to-final lag (days) | Median of (Finaled Date - Issue Date) | Finaled month x district, new single-family only | Finaled reports (they include Issue Date) | Counts only completed permits, so slow permits still open are missing |
| 3 | 180-day completion rate | New single-family permits issued in month M and finaled within 180 days, divided by new single-family permits issued in month M | Issue month x district; only months at least 180 days old | Issued reports joined to finaled reports on permit # | Needs enough months of history; older reports may be unavailable |
| 4 | Average valuation, new homes | Mean Valuation of new single-family permits | Issue quarter x district | Issued reports | Valuation is the applicant's estimate |
| 5 | Remaining pipeline units | Approved units in the pipeline report minus permits already issued for those tracts | Tract x district | Pipeline report + issued reports | May overlap with permits already issued; match tracts by hand |

Supporting measure: permits finaled per month (distinct permits with a Finaled Date in the month, from finaled reports). It feeds the new-resident estimate in Week 4.

## Worked example (April 2026 reports, all work classes)

- Issued: 185 permits; Stewart Tract 52. Share = 52 / 185 = 28.1%.
- Finaled: 90 permits; Stewart Tract 38. Share = 38 / 90 = 42.2%.

## Definitions (proposed; revisit after cleaning the data)

- New single-family = Workclass "BLD_NFD - New Family Dwelling (Production)". Duplexes and other multi-unit buildings are tracked separately.
- A duplex building counts as one permit; unit counts come from the description text later.
- Residential districts = every district except the business parks and "Data Conversion". Confirm after cleaning.
