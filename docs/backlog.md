# Product Backlog

Format: As a [who], I want [what], so that [why]. Each story has acceptance criteria (AC) that can be checked yes or no.
Priority: Must = project fails without it. Should = strong version. Could = drop first.
Personas: Maintainer (Leisha), Business owner (small cafe or gym owner), Reviewer (outside person checking the work).

## Batch 1: Data foundation (Week 2)

### US-01 Track every source file
As the maintainer, I want a manifest of every PDF with its URL, download date, and checksum, so that I can prove which files produced each number.
- AC: data/manifest.csv has one row per PDF in data/raw.
- AC: the sha256 column matches the file on disk.
- AC: the manifest records which months the city still lists.
- Priority: Must. Week 2.

### US-02 Parse the issued-permit reports
As the maintainer, I want each Issued report turned into one row per permit, so that I can count growth by district and month.
- AC: April 2026 produces 185 rows, matching the printed grand total.
- AC: a trailing * on a permit number is removed and stored as a separate hold flag.
- AC: a permit split across a page break appears exactly once.
- Priority: Must. Week 2.

### US-03 Parse the finaled-permit reports
As the maintainer, I want each Finaled report turned into one row per permit with its Issue Date and Finaled Date, so that I can measure how long homes take to finish.
- AC: April 2026 produces 90 rows, matching the printed grand total.
- AC: Issue Date and Finaled Date are real dates, and none is missing.
- Priority: Must. Week 2.

### US-04 Reconcile to the printed totals
As a reviewer, I want every parsed month checked against the totals printed in the report, so that I can trust the data without redoing the work.
- AC: docs/validation_log.md lists, for each month, parsed versus printed counts by district and the grand total.
- AC: every mismatch has a written explanation.
- Priority: Must. Week 2.

## Batch 2: Analysis (Weeks 3 and 4)

### US-05 Rebuild the database with one command
As a reviewer, I want one command that rebuilds the whole database from the raw PDFs, so that I can check the project myself.
- AC: running the documented command on a fresh clone creates the SQLite database with no manual steps.
- AC: docs/data_dictionary.md describes every column, its type, and its source.
- Priority: Must. Week 3.

### US-06 See growth by district and month
As a business owner, I want to see how many new single-family homes were permitted each month in each district, so that I can see where building is happening.
- AC: a SQL query in sql/ returns permits issued per month by district, using the KPI 1 definition in docs/kpis.md.
- AC: a chart shows the result, and its title states the finding in a sentence.
- Priority: Must. Week 3.

### US-07 Know how long homes take to finish
As a business owner, I want to know how many days pass between a permit being issued and the home being finaled, so that I can estimate when new residents will arrive.
- AC: median issue-to-final lag is reported by district, with the number of permits behind each figure.
- AC: the 180-day completion rate only includes months at least 180 days old.
- Priority: Should. Week 3.

### US-08 Count the homes still to come
As a business owner, I want to know how many approved homes are still unbuilt in each district, so that I can see whether growth will continue.
- AC: every tract in the pipeline report is matched to a district, and the match table is checked by hand.
- AC: remaining units equal approved units minus permits already issued, per the KPI 5 definition.
- Priority: Should. Week 4.

## Batch 3: Decision and delivery (Weeks 4 to 6)

### US-09 Add price and household context
As a business owner, I want home values and household income next to the permit counts, so that I can see who the new residents are likely to be.
- AC: Zillow home values and Census ACS income are shown by area, with the ACS margin of error visible.
- AC: a triangulation table names one primary source for each metric and says why.
- Priority: Should. Week 4.

### US-10 Rank the districts, and show how stable the ranking is
As a business owner, I want one opportunity score per district, so that I can compare places quickly, and I want to know whether the ranking holds up if the weights change.
- AC: the score formula and weights are written down in docs/.
- AC: the ranking is recomputed with the weights changed, and the result shows whether the top district stays on top.
- AC: the forecast reports its backtest error.
- Priority: Should. Week 5.

### US-11 Answer the question in two minutes
As a business owner, I want a dashboard that opens on a recommended district, so that I can decide without reading the data.
- AC: the first screen names the recommended district and the main reason.
- AC: every chart title states a finding in a sentence.
- AC: a footnote states the main limit of the data.
- Priority: Must. Week 6.

### US-12 Let a stranger rebuild it and read it
As a reviewer, I want a README I can follow and a one-page memo, so that I can judge the work without asking questions.
- AC: someone outside the project follows the README and rebuilds the database and dashboard without help.
- AC: the memo gives one recommendation, three numbered findings, and its limits.
- AC: at least one person outside the project has read the memo.
- Priority: Must. Week 6.
