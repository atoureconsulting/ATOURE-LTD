# Balance Sheet — Atoure Ltd

A balance sheet is a snapshot at a single date (not a period), so this
covers the position **as at 10 September 2024** (end of the 12-month
period) and **as at 30 September 2024** (end of the stub period), plus
opening position at incorporation for reference.

Status: **Period A01 (10 Sept 2024) drafted from real data below — Period
A02 (30 Sept 2024) still pending that period's own reconciliation.**

## Assets

| | At incorporation (2023) | 10 Sept 2024 | 30 Sept 2024 |
|---|---|---|---|
| Cash at bank | 0.00 | 0.00 (no separate company account existed — see note) | pending |
| Debtors — trade (money owed to the company) | 0.00 | 0.00 (the two unpaid invoices, £2,246.99 total, are already written off as bad debt in the P&L, so carried at nil) | pending |
| Debtors — director's loan account (director owes company) | 0.00 | 2,498.16 (see working below) | pending |
| Fixed assets (equipment etc.) | 0.00 | 0.00 (none purchased this period) | pending |
| **Total assets** | **0.00** | **2,498.16** | pending |

## Liabilities

| | At incorporation (2023) | 10 Sept 2024 | 30 Sept 2024 |
|---|---|---|---|
| Creditors (money the company owes, excl. tax) | 0.00 | 0.00 | pending |
| Corporation tax owed to HMRC | 0.00 | 474.65 (see corporation-tax-workings.md) | pending |
| **Total liabilities** | **0.00** | **474.65** | pending |

## Equity

| | At incorporation (2023) | 10 Sept 2024 | 30 Sept 2024 |
|---|---|---|---|
| Share capital | 0.00 (see note — not yet confirmed with user) | 0.00 | pending |
| Retained profit/(loss) | 0.00 | 2,498.16 (net trading profit) − 474.65 (tax) = **2,023.51** | pending |
| **Total equity** | **0.00** | **2,023.51** | pending |

**Balances:** Assets (£2,498.16) = Liabilities (£474.65) + Equity
(£2,023.51) ✓. Share capital assumed £0/nominal — needs confirming
against the Certificate of Incorporation or Companies House record
(typically £1–£100 for a company this size); if it turns out to be a
non-nil amount, that value would need to be added to assets (as cash
received for shares, if actually paid) or otherwise reconciled.
**Flagged for accountant, not resolved here.**

## Director's loan account / capital introduced / distributions

Since Atoure Ltd has no separate business bank account for this
period, all client income landed in the director's personal Santander
account, and all business expenses were also paid from personal funds.
This account reconstructs the net effect:

| Description | Amount £ |
|---|---|
| Client cash received into director's personal account (cash-basis, matched income only — excludes the two unpaid/written-off invoices) | 4,796.99 |
| Less: genuine business expenses paid personally by director (Companies House fee, Berlin trip, Dubai trip flights/transport/hotels, H3G business share) | (1,986.83) |
| Less: personal living expenses the director confirms were paid from this same client income (groceries, regular living costs) | (2,810.16) |
| **Net (should be ~nil — client cash fully accounted for)** | **0.00** |
| Add: home working allowance owed by company to director (not yet paid) | 312.00 |
| **Net director's loan account position: director owes company** | **2,498.16** |

**Important flag for the accountant — do not resolve without
professional advice:**

The £2,810.16 the director drew for personal living expenses **exceeds
the company's actual profit for the period (£2,498.16)**. This means:

1. It **cannot simply be treated as a dividend** — dividends can only
   be paid out of distributable (actual, already-earned) profit, and
   this exceeds that.
2. It **was not run through PAYE payroll** as salary.
3. The technically correct treatment right now is an **overdrawn
   director's loan account**. Under UK tax rules, if a director's loan
   is not repaid within 9 months of the end of the accounting period,
   the company becomes liable for an additional **S455 tax charge of
   32.5%** on the outstanding balance (repayable to the company once
   the loan itself is repaid, but a real cost while outstanding).

Options an accountant would normally consider: formally declare part
of this as salary (with retrospective PAYE implications) or as a
dividend up to the distributable profit limit with the remainder
treated as a loan, negotiate repayment before the 9-month deadline, or
accept the S455 charge as a temporary cost. **This decision needs the
accountant's input — not made here.**

| Date | Description | In (company owes you) £ | Out (you owe company / drawn) £ | Running balance £ |
|---|---|---|---|---|
| various | Business expenses paid personally by director (see profit-and-loss.md for full breakdown) | 1,986.83 | | |
| various | Home working allowance (flat rate, owed not yet paid) | 312.00 | | |
| various | Personal living expenses drawn from client income | | 2,810.16 | |
| **10 Sept 2024** | **Net — director owes company** | **2,298.83** | **2,810.16** | **(2,498.16)** |
