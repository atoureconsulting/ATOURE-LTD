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

**Canva master invoice book found** (link user provided, design
"Invoices", 22 invoices spanning Sept 2023 to July 2026) — this is the
single most useful source found so far. Extracted every invoice dated
inside period A01 into
`accounting/periods/2023-09-11_2024-09-10/profit-and-loss.md`. This
raises several important issues:

1. **VAT charged inconsistently.** Some invoices charge 20% VAT/tax
   (Chicken Shop invoices #4, #5), most charge 0%. **Need to confirm: is
   Atoure Ltd VAT-registered?** If not registered, it should not be
   charging VAT on any invoice — the "20%" charged on the Chicken Shop
   invoices would need explaining (possibly mislabeled as "Tax" when it
   was actually a different kind of markup, or the company was
   VAT-registered for part of this period and this wasn't accounted for
   elsewhere). This needs resolving before finalising the P&L, and
   separately affects whether a VAT return is also owed to HMRC (a
   distinct filing from Corporation Tax).

2. **Possible duplicate: invoices #4 and #5.** Both dated 29/11/23, both
   billed to "Chicken Shop", both "Content Creation Services", both
   carrying the identical additional note ("9 Short Form Content
   Videos... Payment split in two. 1st payment £10,000 30th November,
   2nd Payment £5,000 7th January"). This note describes ONE deal worth
   £15,000 paid in two installments — but it's attached to BOTH invoices
   rather than one invoice for £10,000 and a second for the remaining
   £5,000 with a different note. **Need to confirm with user: is this
   one deal worth £15,000 total (net), correctly represented by two
   invoices for the two installments? Or has the same £5,000 second
   installment been invoiced twice by mistake?** Treating as two
   genuine, non-overlapping invoices (£15,000 total net) unless told
   otherwise — flagged clearly so this isn't silently double-counted.

3. **Payment destination.** Every invoice in this book — including ones
   from 2023 and ones from 2026 — directs payment to a personal
   Santander or Revolut personal account in the name of Abdul-Malik
   Toure, never to a Revolut Business account in Atoure Ltd's name
   (except the one exception: invoice #8, April 2025, which does list
   the Revolut Business account — but that invoice falls outside both
   of our periods). **This means client income for period A01 almost
   certainly did NOT go through the Revolut Business account, and
   needs the personal Santander account statement to trace.** This
   also raises a real question for the accountant: money earned by the
   company but received into the director's personal account should
   normally be recorded as company income with a corresponding
   director's loan account entry (the company effectively "lent" that
   cash to the director, or it's treated as him collecting on the
   company's behalf) — not just left unaccounted for. Flagging for
   accountant input on the cleanest way to treat this retroactively.

4. **Not yet checked which invoices were actually paid.** An issued
   invoice is not automatically realised income — need bank evidence
   these were paid, or to treat unpaid ones as debtors/bad debt instead
   of revenue.

**Revised total picture so far for period A01 (pending resolution of the
above):** roughly £16,680 net GBP + €3,000 (two euro invoices, FX
pending) from invoiced work, against HMRC's £38,159 estimate — still
likely lower than HMRC's figure once real expenses are deducted, but
**meaningfully higher than the "under £15k/year" figure discussed
earlier** — worth flagging back to user directly, not just filing away.

**RESOLVED — Chicken Shop invoices #4/#5 are NOT a duplicate.** User
confirmed: together they represent one £15,000 net (+£3,000 VAT) deal,
and Atoure only retained a 15% commission/margin on it, paying the
majority out to a talent/creator (invoice payment details list a Natwest
account in the name of Isaac Ajimotokin, consistent with "Manikeisaac
LTD" appearing elsewhere in these records as a talent/client Atoure
works with).

**OPEN — need to confirm cash flow direction for the Chicken Shop deal
before finalising P&L treatment:**
- **Option A:** Chicken Shop paid the full £15,000+VAT to Atoure, Atoure
  paid ~85% out to the talent, keeping 15% (~£2,250) as commission. →
  P&L shows £15,000 income AND a corresponding ~£12,750 expense
  (talent/pass-through payment), netting to ~£2,250 real profit
  contribution from this deal.
- **Option B:** Chicken Shop paid the talent directly (per the Natwest
  details on the invoice), and only Atoure's 15% commission (~£2,250)
  ever reached Atoure. → The £15,000 was never Atoure's money; only the
  £2,250 commission belongs on Atoure's P&L as income, with nothing to
  offset since Atoure never held the rest.
- Both scenarios land on a similar real profit contribution from this
  specific deal (~£2,250), but they present very differently on the
  P&L/turnover figure, which matters for things like the VAT
  registration threshold check (turnover including the full £15,000 vs.
  only the £2,250 commission) and for how the CT600 turnover box is
  completed. **Waiting on user to confirm which happened.**
- **Still also need:** was this commission (~£2,250, or whichever figure
  is confirmed) actually received/paid? Same paid/unpaid question as the
  other invoices applies here too.

**RESOLVED — Option B confirmed by user.** Chicken Shop paid the
talent/creator directly; only Atoure's 15% commission (£2,250, i.e. 15%
of the £15,000 net deal value) ever reached Atoure. The £15,000+VAT
shown on invoices #4/#5 is NOT Atoure income or expense — it documents a
deal Atoure brokered as agent, not cash that passed through Atoure's own
accounts. Corrected in
`accounting/periods/2023-09-11_2024-09-10/profit-and-loss.md`: this line
now shows £2,250.00 income (commission only), not £15,000.

**Effect on total picture:** period A01 net income drops from the
earlier (incorrect) ~£16,680 figure to approximately **£3,930 + €3,000**
(£500 + £70 + £1,000 + £2,250 + £110, plus the two pending €1,500
invoices). This lands much closer to the "under £15k/year" figure
discussed earlier in the conversation, and is far below HMRC's £38,159
estimate.

**Lesson for the rest of the invoice list:** given this correction,
worth double-checking whether ANY of the other invoices in the Canva
book (in either period) also represent brokered/agency deals rather than
direct income — i.e. don't assume every invoice's face value is Atoure's
own income without checking. Flagging as a general open question rather
than re-litigating each one individually unless the user raises it.

**RESOLVED — payment status for all period A01 invoices**, confirmed
partly by user and partly by visually checking the Canva design's page
thumbnails for "PAID" stamps (fetched via Canva `read-design` with
`thumbnails` filter — the stamps are a visual overlay that didn't appear
in the text extraction, so this required a visual check):

- #1 Connect SARL £500 — PAID (stamp visible)
- #2 Manikeisaac LTD £70 — PAID (stamp visible)
- #3 Reality Entertainment £1,000 — UNPAID (user confirmed; no stamp)
- #4/#5 Chicken Shop commission £2,250 — PAID (stamps visible on both
  underlying invoices)
- #6 Dapaah International £110 — PAID (stamp visible)
- #9 Connect SARL €1,500 — UNPAID (user confirmed; no stamp)
- #10 Connect SARL €1,500 — UNPAID (no stamp visible; user said "1.5k"
  singular when confirming Connect SARL was unpaid — **assumed this
  covers both €1,500 invoices since neither has a stamp, but flagging
  in case user only meant one of the two and the other was in fact
  paid**)

Updated `profit-and-loss.md` for period A01 with: received income
(£2,930.00 — invoices #1, #2, #4/#5 commission, #6), unpaid invoices
treated as bad debt (accruals-basis income of £1,000 + €3,000, offset by
an equal bad debt expense — nets to ~nil effect on profit but is the
technically correct presentation), giving a provisional net profit of
**≈£2,370** before genuine operating expenses are added (which are still
completely missing — see below).

**Biggest remaining gap: zero genuine operating expenses found for
period A01.** A trading company realistically has some running costs
(equipment, software, travel, phone, etc.) — need this from the user or
from bank statements (still waiting on personal Santander statements,
which is where the paid invoices' money should have landed).

**Still needed:**
- Personal Santander bank account statements covering 11 Sept 2023 – 30
  Sept 2024 (now clearly the priority — this is where client payments
  actually landed)
- Confirmation of VAT registration status
- Resolution of the Chicken Shop invoice #4/#5 duplication question
- Expenses for period A01 (none found yet at all — only income side so
  far)
- FX rate confirmation for the two €1,500 invoices (#9, #10, dated 2 May
  2024)

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

## 6b. Final resolutions for period A01 — invoice #9 vs #10, phone apportionment

User confirmed three outstanding items directly:

1. **£120 "LEADS" receipt (28 Oct 2023):** user issued a new invoice on
   Canva for £120 and marked it paid, matching the existing "LEADS"
   pattern from invoice #2. No longer an unexplained receipt.
2. **£1,246.99 advance payment (11 Apr 2024):** user confirmed this
   covers **Invoice #9 (Corporate Bookkeeping and Archiving, €1,500)**,
   marked paid on Canva. This means **Invoice #10 (Chauffering &
   Security Services, €1,500)** is the one that remains unpaid and is
   treated as a bad debt write-off.
3. **H3G phone bill apportionment:** user confirmed **50% business use**.
   Applied as 50% × ~£195/year (average ~£16.25/month × 12) ≈ £97.50
   deductible for the year. Added as a genuine expense line in
   `profit-and-loss.md`.

Updated `accounting/periods/2023-09-11_2024-09-10/profit-and-loss.md`
accordingly: total expenses now £2,389.50, net trading profit ≈ £4,687.49
(down slightly from £4,785.00 due to the added H3G expense; the £120
receipt was already counted in the total so no income change).

**User question: "how can i prove that i use my phone so that its
justifiable to them"** — answered in chat. HMRC does not generally
require pre-emptive documentary proof to submit a return; it wants a
reasonable, consistent, defensible estimate that would hold up if ever
queried. Practical ways to support it if asked later: review an itemised
H3G bill for business-related calls/texts/data usage in a representative
month; keep a simple ongoing note/diary of business vs personal use;
apply the same percentage consistently period to period rather than
varying it. This is flagged as a judgement-call area for the real
accountant to sanity-check, not something requiring exhaustive evidence
gathered now.

## 6a. Santander statements received — reconciling against invoices

Santander (personal current account, sort code 09 01 29) statements
received covering Aug 2023 – Sept 2024 (and beyond), saved to
`accounting/source-data/bank-statements/santander/`. This is where the
invoiced payments actually landed. Reconciling against the Canva invoice
book:

- **Invoice #1 (Connect SARL, £500, dated 12 Sept 2023):** confirmed
  received — "TRANSFER FROM CONNECT SARL BOULEVARD HANNE" £500.00,
  dated **5 Oct 2023** (not 12 Sept — paid ~3 weeks after invoice date).
- **Invoice #2 (Manikeisaac LTD, £70, dated 21 Sept 2023):** confirmed
  received — "FASTER PAYMENTS RECEIPT REF.LEADS FROM AJIMOTOKIN I" £70.00,
  dated **11 Oct 2023**.
- **NEW, unexplained income found:** "FASTER PAYMENTS RECEIPT REF.LEADS
  FROM AJIMOTOKIN I" **£120.00**, dated **28 Oct 2023** — no matching
  invoice in the Canva book. Same "LEADS" reference pattern as invoice
  #2. **Need to ask user: what was this for?** Possibly an unbilled
  second lead-gen payment.
- **CHICKEN SHOP DEAL — bank evidence CONTRADICTS the "Option B"
  conclusion from earlier in this conversation.** User confirmed
  "Option B" (client paid the talent directly, only Atoure's 15%
  commission — ~£2,250 — ever reached Atoure). But the bank shows:
  - **30 Nov 2023: £2,000.00 received**, "FASTER PAYMENTS RECEIPT
    REF.Chicken Shop FROM AJIMOTOKIN IE" — money received not from
    Chicken Shop directly, but from Ajimotokin (the talent/his company),
    referencing "Chicken Shop".
  - **1 Dec 2023: £500.00 paid out** to "ISAAC AJIMOTOKIN" (reference
    "amellia").
  - Net effect: **+£1,500** from this exchange, not the +£2,250
    previously assumed, and the mechanics look like Atoure received a
    payment *from* the talent's side referencing the deal, then paid
    some back — closer to a shared pass-through than a clean 15%
    commission received directly.
  - **This needs re-confirming with the user** — the earlier "Option B,
    commission only" conclusion in the Chicken Shop P&L entry
    (`accounting/periods/2023-09-11_2024-09-10/profit-and-loss.md`) may
    need correcting to reflect what the bank actually shows: **+£2,000
    in / −£500 out = net £1,500**, not a flat £2,250 commission.
    Flagging rather than silently changing the figure again — this has
    already been revised twice and needs a settled answer from the user
    before finalising.

**Real expenses now visible for the first time:** Companies House filing
fee (£12.00, 9 Sept 2023 — "CARD PAYMENT TO COMPANIESHOUSE WEB FIL"),
various card payments to American Express / Capital One (look like
personal credit card repayments, not obviously business), H3G (phone
bill) direct debits (~£16-26/month). **Most of this account's activity
looks like personal spending (Uber, restaurants, PayPal, TfL) with
occasional client payments landing in it** — consistent with the
company not having a clean separate business account for period A01.

## 6. Personal Revolut account statement (received, major finding)

3-year personal Revolut statement (GBP/EUR/crypto sub-accounts, 1 Sept
2023 – 15 Sept 2026) received and saved to
`accounting/source-data/bank-statements/`.

**Key finding: this account does NOT show any of the paid invoices**
(#1 Connect SARL £500, #2 Manikeisaac £70, #4/#5 Chicken Shop commission,
#6 Dapaah £110) — every one of those invoices specifies payment to a
**Santander account** (sort code 09-01-29), not this Revolut personal
account. This Revolut personal account is overwhelmingly personal living
expenses (halal meat shops, Uber, TfL, groceries, restaurants) with no
clear business activity inside period A01 (11 Sept 2023 – 10 Sept 2024).

**What this account does confirm:** a recurring pattern from ~Feb/Mar
2025 onward of "Transfer from ATOURE LTD" landing in this personal
account (£1,200, £40, £300, £20, £520, £28, £70 etc.), alongside many
"Payment from MR ABDUL-MALIK BABA TOURE" entries the other way. Looks
like an informal director's loan/drawings pattern — useful for a future
period's balance sheet, but all dated in 2025, **outside both A01 and
A02**, so not part of this filing.

**Critical gap confirmed: the Santander account (where all the paid
invoices actually landed) is still completely missing.** This is now
the single most important document still needed.

**Still needed, in priority order:**
1. **Santander bank statements, 11 Sept 2023 – 30 Sept 2024** — where
   Connect SARL, Manikeisaac, Reality Entertainment, Dapaah, and the
   Chicken Shop commission payments were all directed. Essential.
2. Genuine business operating expenses for period A01 (still zero found)
3. Resolution: was invoice #10 (second €1,500 Connect SARL) really
   unpaid, or did user mean only one of the two when confirming

## 5. Change log

- **[date TBC by session]** Repo structure created: `accounting/periods/`
  (one folder per accounting period), `accounting/source-data/` (raw
  statements/receipts as provided), `accounting/hmrc-correspondence/`
  (scans of the letters already received), `accounting/drafts/` (P&L,
  balance sheet, CT600 figures, appeal letter drafts).
