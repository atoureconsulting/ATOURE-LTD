# Atoure Ltd — Accounting Catch-Up Notes

This file is the running decision log for the corporation tax catch-up work.
Every judgement call, assumption, or open question is recorded here with
justification, so the accountant (and you) can see exactly why a number is
what it is — nothing should be a black box.

**I am not a qualified accountant.** This is a structured drafting exercise
to make the real accountant's job fast and cheap. Every figure here needs
their review before anything is filed with HMRC or Companies House.

---

## 1. Situation as understood from HMRC correspondence (2 Sept 2026 issue date)

HMRC has issued **determinations** (estimates, not real figures) because no
Company Tax Return has ever been filed for Atoure Ltd. Two accounting
periods are open:

| Ref suffix | Period | HMRC's estimated profit | HMRC's estimated tax | Tax-related penalty | Flat-rate penalty | Interest (as of issue) | Total demanded |
|---|---|---|---|---|---|---|---|
| ...A01 | 11 Sept 2023 – 10 Sept 2024 (12 months) | £38,159 | £9,539.75 | £953.97 | £200.00 (implied) | £921.64 | £11,615.36 |
| ...A02 | 11 Sept 2024 – 30 Sept 2024 (19 days) | £3,180 | £795.00 | £79.50 | £200.00 (implied) | £73.20 | £1,147.70 |

**RESOLVED (confirmed from Certificate of Incorporation, Google Drive
"ATOURE LTD/ADMIN" folder):** Atoure Ltd was incorporated on
**11 September 2023** (company number **15129711**). Under Companies Act
2006, a company's first Accounting Reference Date defaults to the last day
of the month of its first anniversary of incorporation — here, **30
September 2024**. Companies House permits first-year accounts to cover up
to 18 months, but HMRC's system only accepts CT accounting periods of a
maximum of 12 months, so it automatically splits a first year longer than
12 months into two CT periods. That's exactly what happened: the 12-month
period (11 Sept 2023–10 Sept 2024, ref ...A01) plus the 19-day remainder
up to the ARD (11–30 Sept 2024, ref ...A02). No error on HMRC's part, and
no separate ARD change — this is standard for a first-year company. Both
periods still need their own P&L/CT workings as already scaffolded, but a
single set of first-year statutory accounts (11 Sept 2023–30 Sept 2024)
filed at Companies House is likely to cover the combined period — to
confirm with accountant.

Key dates:
- Notice to file issued: 20 October 2024
- Return due (period A01): 10 September 2025
- Return due (period A02): 30 September 2025
- Normal due date for tax payment (period A01): 11 June 2025
- Normal due date for tax payment (period A02): 1 July 2025
- Penalty determination due date: 2 October 2026
- **These are all already overdue — filing the real return is time-critical
  to stop further interest accruing on the (likely inflated) estimated
  amounts.**

**Working assumption:** You've told me the business does not make more than
~£15,000/year. HMRC's determination figures (£38,159 and £3,180) are
placeholder estimates used specifically to compel filing — they are *not*
based on any real data from the business. Once real accounts are filed,
these determinations are automatically superseded (per CT620 notice text:
"a completed company tax return can displace it").

---

## 2. Data received so far

**Companies House Confirmation Statement** (Drive: "ATOURE LTD" folder,
filed 23/09/2024, statement date 10/09/2024): confirms company is in good
standing at Companies House as of that date. SIC code 70229 — Management
consultancy activities other than financial management. This is a
*separate* filing obligation from Corporation Tax (goes to Companies
House, not HMRC) — worth checking whether a confirmation statement is also
now overdue for the following year, alongside the accounts.

**"Ashton Hall Tour" expense reconciliation spreadsheets** (Drive, ~20
versions found, most recent/complete: "Ashton_Hall_Tour_Expense_
Reconciliation OFFICIAL"): **NOT RELEVANT to the two overdue CT
periods.** This tracks a client project (Ashton Hall / "Ash Fitness")
running **27 June 2026 – 12 July 2026**, with the reconciliation itself
dated up to 11 Sept 2026 — entirely outside the 11 Sept 2023–30 Sept 2024
window we're filing for. Net figures for reference (not part of this
filing): total client billing £33,000 (agency fee) + reimbursed
expenses, paid off in full by 4 Sept 2026. **Keep this data for a future
accounting period's return, once we get there** — logged here so it isn't
lost, but excluded from the current two periods' P&L.

**Sales invoice found (in-period):** "IV1-Connect.pdf" (Drive:
ATOURE LTD/ATOURE MANAGEMENT & CONSULTING/Invoices), dated **12 September
2023** — falls inside period A01. Invoice #1, billed to "Connect" (Guadeloupe,
FWI), for "Translation Services", £500, 0% tax, total £500. Payment
details on invoice: Santander account in the name of Abdul-Malik Toure
(personal account, not a listed business account) — **flag for user: was
this £500 paid into a personal or business account? Needed to trace it on
a bank statement and to check if it should route through a director's
loan account.**

**Drive search assessment:** the "ATOURE LTD" Drive folder is real and
useful for company registration documents (incorporation certificate,
confirmation statement) and at least one sales invoice, but the wider
Google Drive (outside that folder) is dominated by unrelated client/
project files (influencer marketing campaigns — "ManlikeIsaac", "AFCON",
"Trenderz", event guestlists, etc.) with no clear separation between
personal and business content, and no bank statements found by search.
**Conclusion: bank statements are not in Drive** (or not findable by
filename/content search) — need to be obtained directly from the bank
(online banking export) rather than hunted for further here. Continuing
to crawl the wider Drive is not an efficient way to build the P&L.

**Revolut Business statement received** (saved to
`accounting/source-data/bank-statements/Revolut_Business_ATOURE_LTD_
stmt-gen-2026-09-15.pdf`) — three currency sub-accounts (GBP, EUR, USD),
only GBP has any activity. **The statement's earliest transaction is 14
September 2024** — despite the document header claiming coverage from
16 August 2024, nothing appears before 14 Sept, suggesting the account
was opened/funded around then (or an earlier statement page is needed to
be sure).

This gives us real, bank-sourced figures for **period A02 (11–30 Sept
2024)**:
- Income: £50.00 (14 Sept 2024, from "Ermal Alija")
- Expenses: £38.58 (two SumUp card payments to "Amilcare Rimol", 16 and
  19 Sept 2024)
- **Net profit: £11.42** — compare to HMRC's assumed £3,180. Real
  corporation tax on this would be about **£2.17** (19% small-profits
  rate) vs HMRC's £795.00 estimate.
- Logged in `accounting/periods/2024-09-11_2024-09-30/profit-and-loss.md`
  and `corporation-tax-workings.md`.

**Period A01 (11 Sept 2023 – 10 Sept 2024) still has NO source data** —
this statement doesn't cover that window. **Action needed: get an
earlier Revolut Business statement (or confirm the account didn't exist
yet, in which case all activity for period A01 would have gone through
the personal account or elsewhere).**

**Open questions raised by this statement:**
1. Who is "Ermal Alija" and what was the £50 payment for (14 Sept 2024)?
2. What is "Amilcare Rimol" (via SumUp card reader) — a supplier, or
   could this be a merchant name unrelated to genuine business expense?
3. Statement also shows (outside our two periods, Jan–Jul 2025) a
   recurring pattern of "MOS/MOR to/from Abdul Malik Toure • Baba" —
   this looks like director's loan account activity (money moving
   between the company and the director personally). Not part of this
   filing but worth setting up proper DLA tracking for future periods —
   see `accounting/periods/balance-sheet.md`.
4. Also outside our two periods but worth flagging: two client payments
   received via "THE PARCHE NETWORK" and "DAZN LIMITED" in Nov 2024–Jan
   2025, paired with payments out to "Manlikeisaac LTD" — looks like
   Atoure Ltd was acting as an intermediary/agent for another company's
   invoices. If this pattern also occurred inside periods A01/A02, it
   would need careful treatment (agency income vs. pass-through, not
   necessarily all counted as Atoure's own trading profit). Not seen
   inside our two periods on this statement, but flagged in case a
   personal-account or earlier-period equivalent turns up.

**Still needed:**
- Earlier bank statement/records covering 11 Sept 2023 – 13 Sept 2024
  (period A01 in full, plus the first 3 days of A02)
- Personal bank account statements covering the same window (user
  confirmed personal account was also used for business at times)
- Clarification on the open questions above

## 3. Assumptions log

_(to be filled in as figures are built)_

## 4. Open questions for the user / accountant

1. Confirm actual company incorporation date and Companies House Accounting
   Reference Date (ARD) — needed to explain the split A01/A02 periods.
2. Is Atoure Ltd VAT-registered? (Affects whether we need VAT reconciliation
   as well as CT.)
3. Any distributions (dividends) taken, or capital/loans introduced by you
   as director/shareholder, during either period?
4. Any expenses paid personally (not through the business bank account) that
   should be claimed back / recorded as director's loan repayments?
5. Was there a reason the returns were missed (illness, house move, not
   knowing about the filing requirement, etc.)? This matters for the
   reasonable-excuse appeal on the penalties.

---

## 5. Change log

- **[date TBC by session]** Repo structure created: `accounting/periods/`
  (one folder per accounting period), `accounting/source-data/` (raw
  statements/receipts as provided), `accounting/hmrc-correspondence/`
  (scans of the letters already received), `accounting/drafts/` (P&L,
  balance sheet, CT600 figures, appeal letter drafts).
