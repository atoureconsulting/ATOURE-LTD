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
| 11 Apr 2024 | £1,246.99 | "TRANSFER FROM CONNECT SARL IMM DES GENERAT" | ✅ **RESOLVED — confirmed by user as payment for Invoice #9 (Corporate Bookkeeping and Archiving, €1,500), received as an advance before the invoice was formally raised on 2 May 2024.** £1,246.99 ≈ €1,500 at the GBP/EUR rate around that date, consistent. Invoice #9 marked PAID on Canva. |

**No payment found** from Reality Entertainment (invoice #3, £1,000) —
consistent with user's confirmation it's unpaid.
**RESOLVED:** Invoice #9 (Corporate Bookkeeping and Archiving, €1,500) is
confirmed PAID (the 11 Apr 2024 receipt above, paid in advance of the
invoice date). Invoice #10 (Chauffering & Security Services, €1,500)
remains unpaid — treated as a bad debt candidate below.

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

**RESOLVED — user confirms £2,750 is correct.** This replaces the earlier
£2,250 estimate; the Chicken Shop deal's real net contribution to income
is £2,750, per the four transactions above.

## Income actually received (bank-verified, accruals basis)

| | £ |
|---|---|
| Connect SARL (5 Oct 2023) | 500.00 |
| Manikeisaac / Ajimotokin "LEADS" (11 Oct 2023) | 70.00 |
| Chicken Shop deal, net (30 Nov 2023 – 5 Jan 2024) | 2,750.00 |
| Dapaah International (8 Mar 2024) | 110.00 |
| Connect SARL — Invoice #9, paid in advance (11 Apr 2024) | 1,246.99 |
| **Subtotal, matched/confirmed income** | **£4,676.99** |
| Invoice #2a — "LEADS" receipt (28 Oct 2023), invoice now issued and marked paid on Canva | 120.00 |
| **Total received income** | **£4,796.99** |

## Invoiced but unpaid — bad debt candidates

| | £ / € |
|---|---|
| #3 Reality Entertainment | £1,000.00 |
| #10 Chauffering & Security Services (Connect SARL) | €1,500.00 |

Under accruals-basis accounting, these are recognised as income when
invoiced, then offset by a bad debt expense once confirmed unlikely to
be paid — netting to roughly nil effect on profit, but the technically
correct presentation. User confirmed these as unlikely to be paid.
FX conversion for Invoice #10 (€1,500) still needed (roughly
£1,280–£1,290 estimated).

## Expenses

| Date | Payee | Category | Amount (£) | Notes |
|---|---|---|---|---|
| 9 Sept 2023 | Companies House | Company filing fee | 12.00 | "CARD PAYMENT TO COMPANIESHOUSE WEB FIL" — genuine, small business expense, confirmed on bank statement |
| 6 Nov 2023 (recognised) | Reality Entertainment (bad debt) | Bad debt write-off | 1,000.00 | Offsets the unpaid #3 invoice recognised as income above |
| 2 May 2024 (recognised) | Connect SARL (bad debt) | Bad debt write-off | ~1,280.00 | Offsets unpaid Invoice #10 — FX conversion pending |
| various | H3G (phone) | Direct debit, ~£16–17/month × 12 months, **50% business use (user-confirmed)** | ~97.50 | £16.25/month average × 12 = £195/year, × 50% = £97.50. See notes.md and user-facing answer below on evidencing the 50% estimate |
| 2 Sept 2023 (deemed 11 Sept 2023) | Ryanair | Travel — pre-trading expense | 167.35 | Round-trip London Stansted–Berlin, 2–7 Sept 2023, for the Connect SARL job (Invoice #9, the £1,246.99 income recognised above). **Pre-trading expense**: incurred just before incorporation (11 Sept 2023) but wholly for the trade that generated confirmed income in this period, so treated as incurred on day 1 of trading under the pre-trading expenditure rule. Source: Ryanair itinerary email, booking ref RENH9F, passenger Mr Abdul-Malik Toure, paid via Apple Pay Mastercard ending 8931 |
| various | American Express / Capital One | Card repayments, £100–£500/instance | not counted | Looks like personal credit card repayments (the underlying purchases aren't visible), not treated as a business expense without more detail — **flag for user: any of this business-related?** |
| | | **Other genuine operating expenses (equipment, software, travel specific to client work)** | **0.00** | **Still not found on this account.** Nearly everything else visible is personal spending (Uber, restaurants, TfL, Halal Meat shops, PayPal purchases) |

**Total expenses counted so far: £2,556.85** (Companies House fee + two
bad debt write-offs + H3G at 50% apportionment + Berlin flight)

## Net profit / (loss)

| | £ (approx.) |
|---|---|
| Total income (bank-verified, incl. unpaid invoice recognised on accruals basis) | 7,076.99 |
| Total expenses (bad debts + Companies House fee + H3G apportioned + Berlin flight) | 2,556.85 |
| **Net trading profit / (loss) so far** | **≈ 4,520.14** |

This is provisional. Compare to HMRC's £38,159 estimate — **already
about 13% of it**, and this is before adding the H3G phone bill
apportionment (which would reduce this further), resolving the
remaining £120 unexplained receipt (an invoice for it will add to
income), or finding any further genuine business expenses.

Compare to HMRC's determination for this period: **£38,159** (see
`../../hmrc-correspondence/07_CT620-determination_A01_period_p1.jpg`).

## Open questions — status

1. ~~£120 received 28 Oct 2023~~ — **RESOLVED:** user issued a new
   invoice on Canva for £120 (matching the "LEADS" pattern of invoice
   #2), marked paid.
2. ~~£1,246.99 received 11 Apr 2024~~ — **RESOLVED:** confirmed as
   advance payment for Invoice #9 (Corporate Bookkeeping and Archiving),
   now marked paid on Canva. Invoice #10 (Chauffering & Security
   Services) remains unpaid — bad debt.
3. ~~Chicken Shop net £2,750~~ — **RESOLVED, confirmed correct by user.**
4. ~~H3G phone line (~£16–17/month)~~ — **RESOLVED: 50% business use
   confirmed by user.** Apportioned at £97.50/year (50% of ~£195/year).
   See notes.md and user-facing answer on evidencing this to HMRC.
5. Still need: any other genuine operating expenses (equipment,
   software, subscriptions specifically for the business) not visible
   on this personal account — e.g. did any business costs go through
   the Revolut Business account instead, inside this period? (The
   Revolut Business statement obtained earlier only covered from 14
   Sept 2024 onward, so period A01 isn't covered by it.)
6. ~~Berlin flight, 2–7 Sept 2023, £167.35~~ — **RESOLVED:** user
   confirms this trip was for the Connect SARL job (Invoice #9).
   Claimed as a pre-trading expense, deemed incurred on 11 Sept 2023.
   Other flights found on the personal Revolut account (28 Nov 2023,
   9 Jan 2024, 2 May 2024, 9 May 2024, 29 Jun 2024, 1 Jul 2024, 12 Jul
   2024, 17 Jul 2024, 24 Jul 2024) — **still need user confirmation on
   business purpose for each before claiming.**

## Notes / assumptions for this period

- See `/notes.md` sections 6a–6b for the full reconciliation log.
