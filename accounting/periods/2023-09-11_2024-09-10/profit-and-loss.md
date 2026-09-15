# Profit & Loss — Period 11 Sept 2023 to 10 Sept 2024

HMRC company tax reference: 623 24114 14574 A 01
Status: **DRAFT — bank-verified for income; still missing genuine
operating expenses**

## Income — reconciled against Santander bank statements (real, primary source)

Source: Santander statements, sort code 09 01 29, Aug 2023 – Sept 2024
(saved to `accounting/source-data/bank-statements/santander/`). This is
the account every invoice in the Canva book directs payment to, so it is
the authoritative source — the invoice book and its "PAID" stamps are
useful corroboration but the bank statement is what actually happened.

| Date received | Amount | Description on statement | Matches invoice? |
|---|---|---|---|
| 5 Oct 2023 | £500.00 | "TRANSFER FROM CONNECT SARL" | ✅ Invoice #1 (£500, Translation Services) |
| 11 Oct 2023 | £70.00 | "FASTER PAYMENTS RECEIPT REF.LEADS FROM AJIMOTOKIN I" | ✅ Invoice #2 (£70, Lead Generation) |
| 28 Oct 2023 | £120.00 | "FASTER PAYMENTS RECEIPT REF.LEADS FROM AJIMOTOKIN I" | ❓ **No matching invoice — open question below** |
| 30 Nov 2023 | £2,000.00 | "FASTER PAYMENTS RECEIPT REF.Chicken Shop FROM AJIMOTOKIN IE" | Part of Chicken Shop deal — see below |
| 1 Dec 2023 | (£500.00) paid out | "BILL PAYMENT ... TO ISAAC AJIMOTOKIN REFERENCE amellia" | Part of Chicken Shop deal — see below |
| 27 Dec 2023 | £250.00 | "FASTER PAYMENTS RECEIPT REF.CHICKEN SHOP FROM AJIMOTOKIN IE" | Part of Chicken Shop deal — see below |
| 5 Jan 2024 | £1,000.00 | "FASTER PAYMENTS RECEIPT REF.CHICKEN SHOP FROM AJIMOTOKIN IE" | Part of Chicken Shop deal — see below |
| 8 Mar 2024 | £110.00 | "FASTER PAYMENTS RECEIPT REF.VALENTINES SHOOT FROM DAPAAH INTERNATIONAL GROUP LIMITED" | ✅ Invoice #6 (£110, Valentines Shoot Cast) |
| 11 Apr 2024 | £1,246.99 | "TRANSFER FROM CONNECT SARL IMM DES GENERAT" | ❓ **No matching invoice — open question below (predates invoices #9/#10, which are dated 2 May 2024 and marked unpaid)** |

**No payment found** from Reality Entertainment (invoice #3, £1,000) —
consistent with user's confirmation it's unpaid.
**No payment found** matching invoices #9/#10 (the two €1,500 Connect
SARL invoices dated 2 May 2024) — consistent with user's confirmation
they're unpaid. (The 11 Apr £1,246.99 receipt is a *different*, earlier,
unexplained payment — see below.)

### Chicken Shop deal — net cash actually received

Four related transactions between 30 Nov 2023 and 5 Jan 2024, all
referencing "Chicken Shop" and involving Isaac Ajimotokin:

| Date | In/Out | Amount |
|---|---|---|
| 30 Nov 2023 | In | £2,000.00 |
| 1 Dec 2023 | Out | (£500.00) |
| 27 Dec 2023 | In | £250.00 |
| 5 Jan 2024 | In | £1,000.00 |
| **Net** | | **£2,750.00** |

**This does not match the £2,250 "15% commission" figure previously
calculated in this file** (based on the user's "Option B" explanation —
that the client paid the talent directly and only Atoure's commission
reached Atoure). The real bank evidence shows a more complex flow: money
moving both ways between Atoure and Ajimotokin, netting to £2,750, not a
single clean £2,250 commission receipt. **Flagging for user: does £2,750
look right for what Atoure actually kept from this deal, or does the
£500 paid out on 1 Dec need a different explanation (e.g. a refund,
expense recharge, or the two "leads" payments in the table above also
being related to this same relationship with Ajimotokin)?**

## Income actually received (bank-verified, accruals basis)

| | £ |
|---|---|
| Connect SARL (5 Oct 2023) | 500.00 |
| Manikeisaac / Ajimotokin "LEADS" (11 Oct 2023) | 70.00 |
| Chicken Shop deal, net (30 Nov 2023 – 5 Jan 2024) | 2,750.00 |
| Dapaah International (8 Mar 2024) | 110.00 |
| **Subtotal, invoices we can match** | **£3,430.00** |
| Unexplained "LEADS" receipt (28 Oct 2023) | 120.00 |
| Unexplained Connect SARL receipt (11 Apr 2024) | 1,246.99 |
| **Total received income, including unexplained items** | **£4,796.99** |

## Invoiced but unpaid — bad debt candidates

| | £ / € |
|---|---|
| #3 Reality Entertainment | £1,000.00 |
| #9 Connect SARL | €1,500.00 |
| #10 Connect SARL | €1,500.00 |

Under accruals-basis accounting, these are recognised as income when
invoiced, then offset by a bad debt expense once confirmed unlikely to
be paid — netting to roughly nil effect on profit, but the technically
correct presentation. User confirmed these as unlikely to be paid.
FX conversion for the two €1,500 invoices still needed (roughly
£1,280–£1,290 each estimated).

## Expenses

| Date | Payee | Category | Amount (£) | Notes |
|---|---|---|---|---|
| 9 Sept 2023 | Companies House | Company filing fee | 12.00 | "CARD PAYMENT TO COMPANIESHOUSE WEB FIL" — genuine, small business expense, confirmed on bank statement |
| 6 Nov 2023 (recognised) | Reality Entertainment (bad debt) | Bad debt write-off | 1,000.00 | Offsets the unpaid #3 invoice recognised as income above |
| 2 May 2024 (recognised) | Connect SARL (bad debt) | Bad debt write-off | ~1,280.00 | Offsets unpaid #9 — FX conversion pending |
| 2 May 2024 (recognised) | Connect SARL (bad debt) | Bad debt write-off | ~1,280.00 | Offsets unpaid #10 — FX conversion pending |
| various | H3G (phone) | Direct debit, ~£16–17/month | ~190.00 (12 months) | **Open question: is this a personal or business phone line?** Appears monthly throughout the account — if business use, it's a genuine deductible expense; if personal, it should be excluded (or apportioned) |
| various | American Express / Capital One | Card repayments, £100–£500/instance | not counted | Looks like personal credit card repayments (the underlying purchases aren't visible), not treated as a business expense without more detail — **flag for user: any of this business-related?** |
| | | **Other genuine operating expenses (equipment, software, travel specific to client work)** | **0.00** | **Still not found on this account.** Nearly everything else visible is personal spending (Uber, restaurants, TfL, Halal Meat shops, PayPal purchases) |

**Total expenses counted so far: £3,572.00** (Companies House fee +
three bad debt write-offs)

## Net profit / (loss)

| | £ (approx.) |
|---|---|
| Total income (bank-verified, incl. unpaid invoices recognised on accruals basis, incl. unexplained receipts) | 7,796.99 |
| Total expenses (bad debts + Companies House fee only) | 3,572.00 |
| **Net trading profit / (loss) so far** | **≈ 4,225.00** |

This is provisional. Compare to HMRC's £38,159 estimate — **already
about 11% of it**, and this is before resolving the H3G phone line
question, the two unexplained receipts, or finding any further genuine
business expenses (which would only reduce this further).

Compare to HMRC's determination for this period: **£38,159** (see
`../../hmrc-correspondence/07_CT620-determination_A01_period_p1.jpg`).

## Open questions raised by the Santander reconciliation

1. **£120 received 28 Oct 2023** ("LEADS" from Ajimotokin) — what was
   this for? No matching invoice.
2. **£1,246.99 received 11 Apr 2024** (Connect SARL) — what was this
   for? Predates invoices #9/#10 by 3 weeks, doesn't match their amounts
   even after FX conversion, and those two invoices are separately
   marked unpaid.
3. **Chicken Shop net £2,750** vs the previously assumed clean £2,250
   commission — does this look right, or does the £500 paid out on 1 Dec
   need separate explanation?
4. **H3G phone line (~£16–17/month)** — business or personal use?
5. Still need: any other genuine operating expenses (equipment,
   software, subscriptions specifically for the business) not visible
   on this personal account — e.g. did any business costs go through
   the Revolut Business account instead, inside this period? (The
   Revolut Business statement obtained earlier only covered from 14
   Sept 2024 onward, so period A01 isn't covered by it.)

## Notes / assumptions for this period

- See `/notes.md` sections 6a–6b for the full reconciliation log.
