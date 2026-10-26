# Day 1 Checklist (Wed Oct 21, about 2 hours)

Done = the repo is public on GitHub with one commit.

## 1. Install (30 min)

- [ ] Python 3.11 or newer (`python3 --version`)
- [ ] VS Code, with the Python and Jupyter extensions
- [ ] Git (`git --version`)
- [ ] A free GitHub account
- [ ] DB Browser for SQLite (for looking at your database later)

## 2. Set up the project folder (20 min)

Unzip the starter kit, then from a terminal:

```
cd lathrop-growth-tracker
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

- [ ] `pip install` finished without errors
- [ ] Open the folder in VS Code and select the `.venv` interpreter

## 3. Put it on GitHub (30 min)

- [ ] On github.com, create a new **public** repository named `lathrop-growth-tracker`. Do not add a README there; you already have one.
- [ ] Then, in your terminal:

```
git init
git add .
git commit -m "Initial project scaffold"
git branch -M main
git remote add origin https://github.com/<your-username>/lathrop-growth-tracker.git
git push -u origin main
```

- [ ] Refresh the GitHub page and confirm the files are there

## 4. Make it yours (30 min)

- [ ] Replace the business question in `README.md` with your first draft (you will refine it Friday)
- [ ] Add your first entry to `docs/weekly_log.md` (done, blocked, next)
- [ ] Commit and push: `git add . && git commit -m "Draft business question and first log entry" && git push`

## If something goes wrong

- **`python3` not found on Windows:** try `py -3` instead.
- **Permission error on `pip install`:** make sure the virtual environment is activated (you should see `(.venv)` in your prompt).
- **GitHub asks for a password:** use a personal access token or sign in with GitHub Desktop.
- Write the problem and the fix in `docs/weekly_log.md`. Troubleshooting notes are good evidence of how you work.

## Tomorrow (Thu Oct 22)

Download three monthly permit PDFs from the City of Lathrop Building Department's permit reports page and fill in `docs/source_notes.md`.
