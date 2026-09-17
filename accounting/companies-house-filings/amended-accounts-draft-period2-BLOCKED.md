# Amended Statutory Accounts — Period Ended 30 September 2025 (Period 3)

Status: **BLOCKED — cannot safely draft yet.** Doing this from
incomplete data would repeat the exact mistake we're fixing (filing
figures that aren't actually derived from your bank records).

## What we already have (safe to use)

From `../periods/2024-10-01_2025-09-30/profit-and-loss.md`,
`corporation-tax-workings.md`, and `../periods/balance-sheet.md`:

| | £ |
|---|---|
| Net trading profit | 2,911.27 |
| Corporation tax | 553.14 |
| Distributable (post-tax) profit | 2,358.13 |
| Dividend declared 17 Sept 2026 | (2,278.00) |
| Retained profit this period | 80.13 |
| Director's loan account closing balance (director owes company) | 454.60 |
| Total equity at 30 Sept 2025 (£1.00 share capital + £33.51 b/f + £80.13) | 114.64 |

## What's still missing before this can be drafted

The balance sheet's asset side needs an actual **cash-at-bank figure**
across all accounts (Santander, Revolut Business, Revolut Personal) as
at 30 September 2025 — this was explicitly left as TBC in
`../periods/balance-sheet.md` because building it requires pulling the
exact closing balance from each account's statement covering that date,
which hasn't been done yet for this period.

**To unblock this:** confirm the closing balance on each account as at
30 September 2025 (or the nearest statement date either side of it),
from:
- Santander business-use account
- Revolut Business
- Revolut Personal (to the extent company funds passed through it)

Once those are confirmed, the balance sheet will balance as:
Total assets (cash + £454.60 DLA debtor) = Total liabilities (home
working allowance £312.00 + CT owed across all periods, ~£1,043.30 if
still unpaid) + Total equity (£114.64), and this document can be
completed in the same format as
`amended-accounts-draft-period1.md`.

**Do not file the original 20 June 2026 accounts as "correct" in the
meantime** — they contain the same category of fabricated figures as
the first filing (see `notes.md` section 9a) and should be treated as
needing replacement once the cash figures above are confirmed.
