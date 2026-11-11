# Source Notes: City of Lathrop Permit PDFs

Inspected Oct 27, 2026.

## Files inspected

| File | Report | Period | Pages | Footer date | Grand total |
| --- | --- | --- | --- | --- | --- |
| 2026_april_permits_issued.pdf | Issued | 04/01/2026 to 04/30/2026 | 30 | May 05, 2026 | 185 |
| 2026_april_permits_completed.pdf | Finaled | 04/01/2026 to 04/30/2026 | 16 | June 11, 2026 | 90 |

Older links (Dec 2024 and Apr 2025 issued) returned a 404 page for me on Oct 26, 2026. Check which months the city still lists before building the manifest.

## Layout (same in both reports)

- Page 1: title bar, bar chart of permit counts by district, then permit rows. Every page repeats the title bar and column headers.
- Each permit = 3 grid rows + a blue italic Description line (can wrap to several lines).
  - Row 1: Permit #, Type, Workclass, Status, Main Address, Project, District, Parcel
  - Row 2: Application Date, Issue Date, Expiration, Last Inspection, Finaled Date, Applied Online
  - Row 3: Zone, Sq Ft, Valuation, Fee Total, Assigned To
- A blue banner starts each district section; the District column repeats the name.
- Dates are MM/DD/YYYY. Money has $ and commas.

## Printed totals (for validation)

- Per district: "PERMITS ISSUED FOR STEWART TRACT: 52" (finaled report: "PERMITS FINALED FOR STEWART TRACT: 38").
- Last page: "GRAND TOTAL OF PERMITS: 185" (issued) and "90" (finaled).
- Page 1 chart gives every district's count.
  - Issued: 6 + 1 + 6 + 109 + 10 + 1 + 52 = 185
  - Finaled: 14 + 1 + 9 + 19 + 7 + 1 + 1 + 38 = 90

## Differences between the reports

- Status is "Issued" vs "Complete". Finaled report has Finaled Date filled in and also shows Issue Date.
- Footer dates differ (May 05 vs June 11), so finaled dates in the issued report can be stale. Use the finaled report for finaled dates.
- District names differ: issued has CROSSROADS BUSINESS PARK and "SOUTH LATHROP - SLCC"; finaled has DATA CONVERSION - DISTRICT, NORTH HARLAN and "SOUTH LATHROP - NON SLCC". Standardize in cleaning.
- Lag examples (hand-calculated): RES-2025-01428 = 175 days; RES-2025-00818 = 224 days.

## Parser hazards

- Footnote: "* Indicates active hold(s) on this permit". Permit numbers can end in * (red), e.g. COM-2025-00735*. Strip it and store as has_hold.
- Description can be separated from its permit by a page break (top of issued page 30, finaled page 16).
- Text can wrap mid-word (BLD_COM_Additio / n/Alteration).
- Skip the repeated headers and the page-1 chart.
- Project column holds builder and tract (e.g. Pulte/Tract 3794/The Shores). Useful for builder analysis.
- Assigned To is a staff name. Not needed; drop it.
- Data quirk: RES-2026-00186 has Last Inspection 04/28/2026, before Issue Date 04/30/2026. Log in validation notes.

## pdfplumber test (Oct 27)

- extract_text() on page 2 is readable, but columns collide. Example: the Sq Ft "0" lands inside the Zone text ("Resid 0ential"). Use extract_words() with x-positions instead.
- A permit can split across a page break: row 1 at the bottom of page 1, rows 2-3 and description at the top of page 2. Parse all pages as one stream, anchored on permit numbers, after dropping repeated headers.
- extract_tables() returned 3 "tables" on page 2, not one clean grid of permits. Compare both methods in Week 2 before choosing.
- Full output saved in docs/pdfplumber_test_output.txt

## City permit report availability (checked Nov 10, 2026)
- The city's permit report page lists Jan to Oct 2026 only: 10 months, 20 PDFs (issued and finaled).
- 2024 and 2025 report URLs found through search return HTTP 404 (a 282-byte HTML error page, not a PDF). The city appears to have removed them.
- The Internet Archive Wayback Machine has no snapshot for any of the 9 finaled-report URLs tested.
- File names are inconsistent (YYYY-MM, YYYY_monthname, M.YY). data/manifest.csv takes the month from the file name using src/build_manifest.py.
- Consequence: no year-over-year or seasonal analysis. The forecast will be a simple trend with its limits stated.
- Next: ask City Economic Development (Nov 12 call) whether archived 2024 and 2025 reports exist.
