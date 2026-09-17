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

## 7b. Balance sheet fully rolled forward to 30 Sept 2024 — everything locked

Completed the last open item: rolled the balance sheet forward from
Period A01 (10 Sept 2024, post-dividend) through Period A02's activity
to 30 Sept 2024.

**Method:** traced actual cash movements for A02 — the £50 client
payment and £38.58 personal SumUp purchases both went through the real
Revolut Business account (closing balance £11.42 per the statement,
confirmed as genuine company cash at bank for the first time in either
period). The £8.63 H3G business-share was paid personally by the
director via Santander (company owes director). Net A02 director's
loan movement: director owes company £29.95 (38.58 − 8.63).

**Combined DLA at 30 Sept 2024: £504.60** (£474.65 from A01 + £29.95
from A02) — owed by the director to the company.

Final 30 Sept 2024 balance sheet: assets £829.02 (£1 share capital +
£11.42 real cash at bank + £312 cash held from A01 + £504.60 DLA
receivable), liabilities £794.51 (£312 home allowance + £474.65 A01
tax + £7.86 A02 tax), equity £34.51 (£1 share capital + £33.51 A02
retained profit, since A01's retained profit was fully distributed via
the dividend). Balances exactly (829.02 = 794.51 + 34.51).

**This completes both periods A01 and A02 in full** — P&L, corporation
tax workings, CT600 figures, and balance sheet are all done, locked,
and internally consistent for the whole company history to date
(incorporation through 30 Sept 2024).

## 7a. Period A02 finalised — all open questions resolved

User confirmed the remaining items:
- Ermal Alija (£50 income): a client — income confirmed as recorded.
- PayPal *Payin3 (£11.33): confirmed personal, not claimed.
- SumUp *Amilcare Rimol[a] (£15.63 + £22.95 = £38.58, 16 & 19 Sept
  2024): user confirmed these were likely personal purchases made
  during the hospital admission, paid via the Revolut Business
  account (both dates fall within the 7-25 Sept hospitalisation).
  Removed from expenses (not a business cost) and instead tracked as
  a director's loan item — same treatment logic as period A01's
  overdrawn loan (business funds used for a personal purchase).

Updated `profit-and-loss.md`: total expenses now just £8.63 (H3G phone
at 50%), net profit **£41.37** (up from the earlier £(8.54) draft).
Updated `corporation-tax-workings.md`: tax due £7.86 (19% x £41.37).
Updated `CT600-figures.md` with final A02 figures and a combined
total across both periods: **£482.51 total corporation tax due**
across A01+A02, versus HMRC's combined £10,334.75 assumption (~4.7%).

Status changed to COMPLETE. Both periods A01 and A02 are now fully
reconciled, bank-verified, and locked. Still outstanding: the £38.58
(A02) and £474.65 (A01) director's loan items need reflecting in a
combined/updated balance sheet — balance-sheet.md's 30 Sept 2024
column is still marked "pending" and needs this update next.

## 7. Period A02 reconciled against all three accounts

Checked all three bank accounts for the 11-30 Sept 2024 window
(previously only Revolut Business had been checked):

- **Revolut Personal:** full review confirms no business activity.
  Notably, this account shows near-daily "Royal Free Hospital" charges
  from 17-29 Sept 2024 and support payments from "Menardin" — directly
  consistent with the director's hospitalisation (7-25 Sept 2024, see
  section 6o) overlapping this exact period. Good independent
  corroboration of the illness timeline from a completely different
  data source.
- **Santander:** statement for 11 Sept-10 Oct 2024 checked. Found real
  activity previously missed: H3G phone direct debit (£17.26, 50%
  business use per the established A01 rate = £8.63) and a PayPal
  "Pay-in-3" charge (£11.33, purpose unknown — need to ask user). Also
  a £10 transfer to the director's own Revolut account — correctly
  excluded as an internal transfer, not an expense.
- **Revolut Business:** unchanged, already fully reviewed in 6c/6g.

Updated `profit-and-loss.md` for period A02: total expenses now
£58.54 (was £38.58), and the period now shows a small loss of £(8.54)
rather than a £11.42 profit. Two open questions remain before this is
final: who "Ermal Alija" is (the £50 income), and what the PayPal
Pay-in-3 charge was for.

## 6s. All three documents signed

User confirmed the dividend board minute, dividend voucher, and
penalty appeal letter are all signed and saved in their Google Drive.
Status: dividend paperwork is now legally effective (dated 17 Sept
2026); appeal letter is ready to post to HMRC (deadline 2 Oct 2026).
Remaining work is the appeal letter's physical posting, plus the
larger remaining items: Period A02 reconciliation, statutory accounts,
actual CT600 filing, and accountant engagement.

## 6r. Dividend paperwork finalised, ready to sign (Option B chosen)

User confirmed they want to just sign the dividend paperwork
(£2,023.51, covering the distributable-profit portion) and leave the
remaining £474.65 as a loan, accepting the ~£154.26 S455 charge rather
than repaying immediately — a legitimate, previously-presented option.

Filled in today's actual date (17 September 2026) on both
`dividend-board-minute.md` and `dividend-voucher.md`, changed their
status from DRAFT to READY TO SIGN. No further edits needed from me —
user just needs to print and sign both.

Also directly addressed a hypothetical the user raised beforehand:
whether creating a document now but dating it September 2024 (or
locating a document that never really existed from that date) would
avoid the S455 charge. Declined to help with backdating/fabricating a
document, explained this would be false accounting/potential fraud,
and that the financial stakes (~£154) don't justify the risk. User
confirmed they were only asking hypothetically, not requesting this.

## 6q. Dividend paperwork drafted

Drafted the two documents needed to formalise the £2,023.51 dividend
(the distributable-profit portion of the DLA, per 6l/6m): a written
resolution of the sole director (`dividend-board-minute.md`) and a
dividend voucher (`dividend-voucher.md`), both in `accounting/drafts/`.

Key decision, flagged clearly in both documents: **dated with the
real signing date, not backdated into 2024** — dividends cannot be
legally backdated. Explained to user that this means the dividend
formally clears the loan going forward, but does not retroactively
fix Period A01's S455 exposure (that deadline already passed before
today), which remains a separate issue covered in the penalty
appeal/balance sheet notes. Satisfied by set-off against the DLA
rather than a fresh cash payment, since the money was already drawn.

Both documents still need: today's actual date filled in, and the
user's signature. Recommended accountant review before signing,
particularly given the unusual timing (declared ~2 years after the
period it relates to).

## 6p. Illness narrative extended (3-week prodrome + infection); images redacted and pushed

User added two facts: (1) approximately 3 weeks of worsening symptoms
before the 7 Sept 2024 admission — this matches the ED triage note
verbatim ("2/52 nausea, fatigue, loss of appetite. 1/52 vomiting,
SOBOE"), so it's independently corroborated by the medical record
itself, not just self-reported; (2) explicitly asked not to forget the
hospital-acquired Staph Aureus Bacteraemia (line infection) that
extended the stay. Both added to `penalty-appeal-letter.md` — the
letter now describes the full arc: 3-week prodrome → emergency
admission → ICU → complicating infection → extended stay → discharge.

**Redaction:** per the user's "yes" to redacting, manually redacted
all 4 discharge letter images before committing — blacked out NHS
number, date of birth, home address, phone numbers (patient and GP),
and the GP's name/practice address in all four images, using PIL with
coordinates verified by cropping and re-reading each region until no
PII remained visible. Preserved all clinically/administratively
relevant content: admission date, discharge date, diagnosis, ward,
consultant, treatment. Original unredacted images were never
committed to git — only redacted versions were staged and pushed, so
there's no PII in git history. Renamed files to
`*-redacted.png` for clarity.

## 6o. Penalty appeal letter — verified with NHS discharge documentation

User provided 4 images of NHS discharge letters (Royal Free London NHS
Foundation Trust) confirming the reasonable excuse with exact dates:
- Admitted 7 September 2024 (Emergency Department, presenting with
  nausea/fatigue/vomiting, admitted directly to ICU)
- Diagnosed with diabetic ketoacidosis (confirmed 7 Sept 2024) and
  new-onset diabetes mellitus (confirmed 24 Sept 2024)
- Treated for a Staph Aureus Bacteraemia (line infection) during
  admission, PICC line inserted 20 Sept 2024, IV antibiotics
- Discharged 25 September 2024 — 18 days total inpatient

Saved the 4 images to
`accounting/source-data/reasonable-excuse-evidence/` (contains NHS
personal data — NHS number, DOB, home address, phone number — noted as
sensitive, kept in the repo as it's the user's own private repo and
this is their own medical evidence).

Updated `penalty-appeal-letter.md` with the exact dates and diagnosis,
replacing the earlier "approximately one month / one week in ICU"
placeholder with verified facts. Added a note on the strong timing
coincidence: hospitalisation (7-25 Sept 2024) falls almost exactly at
the boundary between Period A01 (ends 10 Sept 2024) and Period A02
(ends 30 Sept 2024) — the director was either hospitalised or newly
discharged right when both periods closed.

Remaining before sending: accountant sign-off, and a decision on
whether to enclose the NHS documents with the initial appeal or hold
them in reserve for if HMRC requests evidence.

## 6n. Penalty appeal letter — reasonable excuse filled in

User provided the real reason for the late filing: serious illness
requiring hospitalisation for approximately one month, including
around one week in ICU, during August/September 2024. This is a
genuine, HMRC-accepted category of reasonable excuse (serious illness
of the taxpayer/sole responsible officer), distinct from the
explicitly-rejected excuses like "didn't know" or "too busy."

Filled this into `accounting/drafts/penalty-appeal-letter.md`,
emphasizing that Atoure Ltd is a sole-director company with no other
officer able to act during the illness — strengthens the argument.
Still needed before sending: exact hospitalisation dates (currently a
placeholder), and ideally supporting medical documentation (discharge
letter or similar) to have ready if HMRC requests it. Not sent yet —
status remains DRAFT pending those details and accountant sign-off.

## 6m. Share capital confirmed — period A01 balance sheet fully locked

User confirmed 100% of shares held by director Abdul-Malik Baba Toure.
Found the exact share capital via Google Drive search: Articles of
Association state "the share capital of the Company is divided into
[100] shares of £[0.01] each" (£1.00 total), and the Memorandum of
Association confirms the sole subscriber is Abdul-Malik Toure —
consistent with 100% ownership.

Added £1.00 share capital to both sides of `balance-sheet.md` (assets:
called-up share capital; equity: share capital). Flagged one minor,
immaterial open point for the accountant: whether the £1.00 was
actually paid in cash at incorporation or remains called-up-but-unpaid
(common for nominal amounts this small) — doesn't affect any other
figure.

**This closes out the last open item on Period A01's balance sheet.**
Status changed to COMPLETE. Full picture for Period A01: assets
£787.65, liabilities £786.65, equity £1.00 (rising to £2,024.51 once
the £2,023.51 dividend is formally declared and paid, per 6l).

## 6l. DLA revised — user corrected personal spend to £2,498.16, not £2,810.16

User revisited the DLA figures and clarified: of the £2,810.16 residual
from the cash reconciliation, only **£2,498.16** was actually spent
personally (groceries/living costs) — the remaining **£312.00** is
still held, unspent, in the director's account. This is a genuine
correction to the fact pattern established in 6k, not a bookkeeping
error — logged as a fact change, not a mistake.

**Further correction on my part during this exchange:** initially
said £2,498.16 "exactly matches profit, so it's a clean dividend, no
issue." This was wrong — the amount legally available to distribute
as a dividend is the **post-tax retained profit** (£2,023.51), not the
pre-tax trading profit (£2,498.16), since the £474.65 tax portion was
never available to distribute. Caught and corrected before locking the
figures.

**Revised picture:**
- £312.00 — still held, unspent — just company cash, no issue
- £2,023.51 — covered by distributable profit — can be a clean
  dividend once board minute + voucher are done (not yet done)
- £474.65 — genuinely exceeds distributable profit — remains an
  overdrawn director's loan

This is a large improvement on the earlier £2,810.16 loan figure.
**S455 timing:** user asked whether repaying now avoids the S455
charge. Answered: likely no — the 9-month repayment deadline (10 June
2025) and the second grace period (repay before the CT600 filing
deadline, 10 Sept 2025) have both already passed, given how overdue
this filing already is. So the charge (~£154.26 = 32.5% × £474.65)
will likely still apply when the return is filed, refundable once the
loan is actually repaid. Flagged explicitly as something to confirm
with the accountant given the unusual interaction with an already
very-late filing — not stated with full certainty.

Updated `balance-sheet.md`: assets £786.65 (cash held £312 + DLA
receivable £474.65), liabilities £786.65 (home allowance owed £312 +
corp tax £474.65), equity £0 once the £2,023.51 dividend is declared
(otherwise sits as undistributed retained profit until that paperwork
is done).

## 6j. Correction: stale income figure found while building the DLA

While reconstructing the director's loan account (see below), cash-flow
arithmetic didn't match the balance-sheet-equation arithmetic by
exactly £33.01. Root cause: `profit-and-loss.md`'s "Total income" line
(£7,076.99) was calculated back when the Invoice #10 bad debt was still
an estimate (~£1,280.00) and was never updated when section 6i finalised
that FX conversion to £1,246.99 (a £33.01 difference). The "Total
received income" cash-basis subtotal (£4,796.99) was correct and
unaffected — only the accruals-basis grand total (which adds the two
written-off invoices on top) was stale.

**Fixed:** total income corrected to £7,043.98 (£4,796.99 + £1,000.00 +
£1,246.99). This cascades through:
- `profit-and-loss.md`: net profit corrected from £2,531.17 to
  **£2,498.16**
- `corporation-tax-workings.md`: tax corrected from £480.92 to
  **£474.65**
- `CT600-figures.md`: Period 1 boxes updated to match

This is a good illustration of why the DLA reconciliation is a useful
sanity check — it's what caught the stale figure. Both methods
(cash-flow and balance-sheet-equation) now agree exactly on £2,498.16.

## 6k. Director's loan account built — overdrawn, flagged for accountant

Since Atoure Ltd had no separate business bank account for period A01,
all client income landed in the director's personal Santander account
and all business expenses were also paid personally. Asked the user
directly whether the leftover client cash (after business expenses)
was spent personally. **User confirmed: yes, on groceries and regular
living expenses.**

Built the DLA as a reconciliation: £4,796.99 client cash in, £1,986.83
spent on confirmed business costs, leaving £2,810.16 spent personally.
Netted against £312.00 owed to the director for the home working
allowance (see 6h), giving a **net DLA position: director owes the
company £2,498.16**.

**Flagged, not resolved:** £2,810.16 of personal drawings exceeds the
period's actual profit (£2,498.16), so it can't simply be a dividend
(exceeds distributable profit) and wasn't run through PAYE either. The
technically correct treatment right now is an overdrawn director's
loan account, which risks a S455 tax charge (32.5% of the outstanding
balance) if not repaid within 9 months of the period end. Presented
the options (salary, dividend up to the limit, repayment, or accepting
S455) without choosing one — this is squarely something for the real
accountant to advise on, not a judgement call to make unilaterally.

Updated `balance-sheet.md` with the full picture: assets £2,498.16
(all DLA receivable), liabilities £474.65 (corp tax), equity £2,023.51
(retained profit). Balances correctly. Share capital still unconfirmed
— flagged separately.

## 6i. Period A01 finalised — FX conversions locked

Two remaining FX estimates finalised:

1. **Invoice #10 bad debt (€1,500):** rather than use a generic
   published rate, used the actual realized rate from the sister
   invoice (#9, identical €1,500 amount, same client Connect SARL,
   paid 11 Apr 2024 and converted by the bank to £1,246.99) — more
   directly evidenced for this specific client/invoice pair than a
   monthly table rate. Changed from ~£1,280.00 (estimate) to £1,246.99
   (final).
2. **Berlin Bolt/Uber (€35.30 + €168.93):** used HMRC's official
   published exchange rate for September 2023 (£1 = €1.1683, via web
   search of trade-tariff.service.gov.uk data). Bolt: £30.21 (was
   ~£30.44 estimate). Uber: £144.59 (was ~£145.63 estimate).

Updated `profit-and-loss.md`: total expenses £4,545.82, net trading
profit **£2,531.17** (final, not provisional) — compare to HMRC's
£38,159 estimate, ours is ≈6.6% of it. Status changed from DRAFT to
COMPLETE. Every open question in the file is now resolved and every
FX conversion is final rather than approximate.

Next for this period: finalise `corporation-tax-workings.md` with this
profit figure (small profits rate 19% applies, well under £50,000
threshold) and move on to `CT600-figures.md` and the balance sheet.
Period A02 (11-30 Sept 2024) still needs its own Santander
reconciliation before it can be considered final too.

## 6h. Period A01 closed out — hotels, home working, VAT, cards

Four remaining items resolved in one round with the user:

1. **Dubai hotels** — user confirmed "yes the hills" (referring to
   both Dubai hotel charges given the same confirmed-business-trip
   basis as the transport). Added Vida The Hills (£155.66) and Blu
   Oasis Desert Hotel (£6.50) as accommodation expenses.
2. **Use of home as office** — user confirmed working from home, and
   that the company's registered business address is the home address.
   Claimed HMRC's simplified flat rate for a director regularly
   working from home: £6/week x 52 weeks = £312.00. This rate needs no
   receipts or bill-apportionment evidence — it's a pre-agreed HMRC
   allowance, which directly answers the user's "how do I prove this"
   question.
3. **VAT** — user confirmed turnover well under £15,000/year, so no
   VAT registration required (threshold £85,000/£90,000). Noted as
   correctly unregistered.
4. **Amex/Capital One cards** — user confirmed they no longer have
   access to these card accounts, so the underlying purchases cannot
   be verified. Left out of the accounts entirely rather than
   estimated — the honest position given no evidence is obtainable.
5. **Equipment/software/subscriptions** — user confirmed none incurred
   (specifically ruled out website hosting).

Updated `profit-and-loss.md`: total expenses now £4,580.10, net trading
profit ≈ £2,496.89 (down from £2,971.05 due to the hotels + home
working allowance, partially offset by nothing new on income).

This effectively closes out Period A01's expense-gathering — every
open question in the file is now resolved. Remaining before this
period can be finalised: FX conversion of the €1,500 Invoice #10 bad
debt into GBP (currently an estimate), and then locking
`corporation-tax-workings.md` with the final profit figure.

## 6g. Dubai trip ground transport added

User asked to add Uber/taxi costs from business trips. Checked the
personal Revolut statement for the Dubai/Abu Dhabi window (9 May – 3
Jun 2024, matching the Emirates booking CSHGVS already claimed).

Found 25 ground transport transactions (Careem, Cars Taxi, Dubai Taxi,
Royal Smart Limousine, National Parking) totalling £244.56 across the
26-day window. Flagged to user that the same window also contained
non-transport personal-looking spend (a barbershop, a nightlife venue
twice, groceries, hotels in two cities) — asked directly whether the
whole trip was for the client or only part of it, given HMRC's
"wholly and exclusively" test. **User confirmed: the entire trip was
for the client.** Added the full £244.56 ground transport total to
`profit-and-loss.md` on that basis.

Updated totals: total expenses now £4,105.94, net trading profit
≈ £2,971.05. Note for the accountant: the non-transport spend in the
same window (salon, nightlife, groceries, hotels) was NOT added as an
expense — only ground transport was in scope of what the user asked to
add. If the trip really was wholly for the client, some of that other
spend (e.g. the hotels) could arguably also be examined, but this
wasn't asked for and hasn't been assessed.

## 6f. Remaining flights resolved as personal — flight review complete

User connected a second Gmail account (ambtzooleh@gmail.com, the
personal account used for travel bookings) to search for the last
unconfirmed flights.

Findings:
- **28 Nov 2023 Ryanair £184.80 + 9 Jan 2024 Ryanair £117.24:**
  Marrakesh trip. Reservation TI8YWS (London Stansted → Marrakesh, 1
  Jan 2024; originally due back 5 Jan) and a separate reservation
  CNFCQA (Marrakesh → London Stansted, 11 Jan 2024) — the return was
  extended, ~10-day stay in Marrakesh.
- **Also found while searching:** an October 2024 trip to Malaga/
  Marbella (TUI Airways booking 25706882, 13 Oct 2024, travelling with
  Isaac Ajimotokin and a Lovell Andrew Small; stayed at Hotel Puente
  Romano, Marbella). This is after both filing periods end (A01: 10
  Sept 2024, A02: 30 Sept 2024) — **out of scope for this filing**,
  logged for a future period, source emails not yet saved to the repo
  (only identified via search, not downloaded).
- Paris (Air France, 1-2 May 2024), the June/July Malaga trip (EasyJet
  29 Jun + Jet2 11 Jul 2024), and the two British Airways charges (17 &
  24 Jul 2024) were already identified destinations from earlier
  research.

**User confirmed: all of the above (Marrakesh, Paris, June/July Malaga,
both British Airways charges) were personal travel, not business.**
None of these are claimed as expenses. This closes out the flight
review for Period A01 — only the Berlin (pre-trading) and Dubai
(client) trips are claimed as travel expenses, per sections 6c-6e.

## 6e. Berlin trip ground transport (Bolt/Uber) added

User asked to search Gmail for flight emails. Gmail connector was
enabled; searched atoureconsulting@gmail.com for flight/travel
confirmations within Period A01/A02 plus surrounding dates. Found:
- Emirates original booking + change confirmation (already logged, 6d)
- Jet2 (3QXRL5), Malaga → London Stansted, 11 Jul 2024, €92.23
- EasyJet (K7P8LK3), London Gatwick → Malaga, 29 Jun 2024, £288.99
- Air France Paris boarding passes, 1-2 May 2024 (matches existing
  £25.70 entry)
- A Sept 2023 sent email "Berlin Transport + Plane Invoice" to
  connectsarl@hotmail.fr with 11 PDF attachments (Ryanair + 3 Bolt + 8
  Uber receipts) — the Gmail tools available only exposed attachment
  metadata, not content, so could not read the PDFs directly from
  Gmail. User downloaded and uploaded the zip of attachments directly.

**Malaga/Paris trip (Jun-Jul 2024) — still awaiting user confirmation
on business vs personal purpose.**

**Berlin trip receipts (zip uploaded, saved to
`accounting/source-data/receipts-and-invoices/berlin-trip-2023/`):**
extracted via pypdf. Ryanair confirmed matches existing entry (£167.35).
New: 3 Bolt receipts (€18.00, €8.30, €9.00 = €35.30) and 8 Uber
receipts, of which "uber 3.pdf" and "uber 4.pdf" are exact duplicates
(same trip, timestamp, fare €16.96) — counted once. 7 unique Uber fares:
€40.91, €23.90, €16.96, €6.00, €20.98, €17.25, €42.93 = €168.93.

Added to `profit-and-loss.md` under the same pre-trading expenditure
treatment as the Ryanair flight (deemed incurred 11 Sept 2023, wholly
for the Connect SARL job). FX converted at an approximate Sept 2023
rate (~1.16 EUR/GBP): Bolt ≈£30.44, Uber ≈£145.63 — flagged as
approximate, exact conversion pending for the accountant.

Updated totals: total expenses now £3,861.38, net trading profit
≈ £3,215.61.

## 6d. Dubai (Emirates) trip confirmed as business; Rome/Doha trips out of period

User provided 5 itinerary emails. Findings:

- **Ryanair Berlin (98a75a6e...eml):** exact duplicate of the booking
  already logged in 6c (RENH9F). No new information.
- **Emirates original booking (49bae582...eml, saved as
  `Emirates_Dubai_original_booking_CSHGVS.eml`):** booking ref CSHGVS,
  London Gatwick → Dubai, 8 May 2024, returning Dubai → London Heathrow
  originally 6 June 2024. £703.46 (matches the 9 May 2024 bank charge
  found earlier). Passenger: Mr Abdulmalik Toure.
- **Emirates change confirmation (d1a6eac2...eml, saved as
  `Emirates_Dubai_change_confirmation_CSHGVS.eml`):** same booking
  CSHGVS, return date changed to 3 June 2024. £425.00 (£350 fare
  difference + £75 change fee), paid via PayPal — matched to the 12 Jun
  2024 £425 "To Paypal Uk" transaction on the personal Revolut account.
  Dubai-dated spending also visible around 3 June 2024 (hotels, taxis,
  Amex) consistent with an actual trip taking place.
- **User confirmed: the Dubai trip was for a client (business).**
  Both the £703.46 original booking and the £425.00 change fee added to
  Period A01 expenses as confirmed business travel.
- **easyJet (a968e19e...eml) + Wizz Air (b141f467...eml):** same round
  trip, London Gatwick ↔ Rome Fiumicino, 17–18 Oct 2024, travelling with
  Isaac Ajimotokin (the Chicken Shop contact). €200.96 + £361.98. Dated
  after Period A02 ends (30 Sept 2024) — **out of scope for this
  filing**, saved to `accounting/source-data/invoices-out-of-period/`
  for a future period.
- **Gotogate (05b9d478...eml):** London Heathrow ↔ Doha, 26–29 Nov 2024,
  also with Isaac Ajimotokin, £1,195.99. Also out of scope, saved to
  the same out-of-period folder.

Updated `profit-and-loss.md`: total expenses now £3,685.31, net trading
profit ≈ £3,391.68 (down from £4,520.14 due to the added £1,128.46 in
Dubai trip costs). Still outstanding: business purpose confirmation for
the remaining 8 flights on the personal Revolut account within the
filing periods (see open question 7 in profit-and-loss.md).

## 6c. Flight expenses — Santander/Revolut Personal search, Berlin trip confirmed

User asked to look up all flight expenses paid in the bank statements.
Searched all Santander and both Revolut PDFs for airline/flight keywords
(pypdf text extraction). Result: **no flight charges on the Santander or
Revolut Business accounts** — all flight spending is on the **personal
Revolut account**, meaning any claimed as a business expense needs
treating as a director's expense/reimbursement, not a direct company
payment.

Flights found inside 11 Sept 2023 – 30 Sept 2024 (Period A01/A02):
28 Nov 2023 Ryanair £184.80; 9 Jan 2024 Ryanair £117.24; 2 May 2024 Air
France £25.70; 9 May 2024 Emirates £703.46 (ref "Airport baba"); 29 Jun
2024 EasyJet £288.99; 1 Jul 2024 EasyJet inflight £6.50; 12 Jul 2024
jet2.com £2.70 (ref "Airport job"); 17 Jul 2024 British Airways £17.50;
24 Jul 2024 British Airways £32.50 (ref "Flights"). None of these have
been confirmed as business yet — still need user to state purpose for
each.

**Berlin trip, resolved:** user provided a Ryanair itinerary email
(saved to
`accounting/source-data/receipts-and-invoices/Ryanair_Berlin_2-7Sept2023_itinerary.eml`)
— round-trip London Stansted–Berlin, **Sat 2 Sept 2023 to Thu 7 Sept
2023**, £167.35 total, passenger Mr Abdul-Malik Toure, booking ref
RENH9F. This is *before* incorporation (11 Sept 2023) and before both
accounting periods start. User confirmed this trip was for the Connect
SARL job (the one that produced the £1,246.99 payment / Invoice #9,
Corporate Bookkeeping and Archiving).

**Treatment decision:** claimed under the pre-trading expenditure rule
(CTA 2009 s.61) — costs incurred up to 7 years before a company starts
trading, wholly for the purpose of that trade, are treated as incurred
on the first day of the first accounting period. Deemed incurred 11
Sept 2023, added to Period A01 expenses at £167.35. This is a
reasonable, defensible position given the trip directly produced
confirmed invoiced income in this period — flagged for the real
accountant to confirm the treatment is correctly presented on the
CT600/accounts (may want a note in the accounts explaining the
pre-trading nature).

Updated `profit-and-loss.md`: total expenses now £2,556.85, net trading
profit ≈ £4,520.14.

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
