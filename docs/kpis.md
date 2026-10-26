# KPI Definitions

*Draft Fri Oct 23. Edit each definition so that two people calculating it from the same data would get the same number. Revisit after interviews in Week 3.*

| KPI | Formula | Grain | Source | Why it matters | Known weakness |
| --- | --- | --- | --- | --- | --- |
| Permits issued per month | Count of distinct permits with an issue date in the month | Month x district x work-class group | Monthly "issued" reports | Leading indicator of construction activity | Permits are not completed homes |
| Issue-to-final lag (days) | Median of (finaled date - issue date) | Issue quarter x district, new single-family only | Issued and finaled reports, joined on permit number | Shows how long a permit takes to become a home | Recent permits have not finished yet (censored) |
| Completion ratio | Permits finaled in the trailing 6 months / permits issued in the trailing 6 months | Month x district | Both reports | Shows whether permits are turning into finished homes | Timing mismatch between issue and final |
| Average valuation of new-home permits | Mean valuation of new single-family permits | Quarter x district | Issued reports | Rough proxy for home size and price tier | Valuation is the applicant's estimate |
| Remaining pipeline units | Approved units in the pipeline report not yet permitted | Tract x district | Residential pipeline report | How much building is still ahead | May overlap with permits already issued |

## Definitions to decide (answer in the decision log)

- Which work classes count as "new single-family" (production new-family-dwelling only, or also custom)?
- Do duplex permits count as one permit or two units?
- Which districts are "residential" for the opportunity score?
