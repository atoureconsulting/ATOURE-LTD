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
| 5–6 Sept 2023 (deemed 11 Sept 2023) | Bolt | Ground transport — pre-trading expense | ~30.44 (€35.30) | 3 Bolt rides in Berlin during the same trip (invoice #s 39177408-DE1123-446 €18.00, 47134568-DE1123-131 €8.30, 46856728-DE1123-102 €9.00). Same pre-trading treatment as the flight. FX approximate (Sept 2023 rate ~1.16), exact conversion pending |
| 2–7 Sept 2023 (deemed 11 Sept 2023) | Uber | Ground transport — pre-trading expense | ~145.63 (€168.93) | 7 unique Uber rides in Berlin during the same trip (an 8th receipt, "uber 3", was a duplicate of "uber 4" — same trip/timestamp/amount, counted once). Individual fares: €40.91, €23.90, €16.96, €6.00, €20.98, €17.25, €42.93. Same pre-trading treatment as the flight. FX approximate, exact conversion pending |
| 8 May 2024 | Emirates | Travel — client business trip (user-confirmed) | 703.46 | Original booking, London Gatwick–Dubai–London Heathrow, booking ref CSHGVS. User confirms this trip was for a client. Source: Emirates booking confirmation email |
| 12 Jun 2024 | Emirates (via PayPal) | Travel — flight change fee | 425.00 | Change fee for the same Dubai trip (CSHGVS): £350 fare difference + £75 change fee, moving return date to 3 June 2024. Paid via PayPal, matched to 12 Jun 2024 personal Revolut transaction |
| 9 May – 3 Jun 2024 | Careem / Cars Taxi / Dubai Taxi / Royal Smart Limousine / National Parking | Ground transport — client business trip (user-confirmed) | 244.56 | Dubai/Abu Dhabi ground transport for the same Emirates trip (booking CSHGVS). User confirmed the full trip was for the client. 25 transactions: £3.28, £14.43, £17.68, £16.07, £3.44, £6.34, £14.85, £25.77, £12.36, £2.59, £13.90, £0.84, £10.22, £7.86, £6.01, £1.85, £4.07, £12.14, £8.56, £10.99, £6.90, £8.43, £11.92, £23.77, £0.29 (personal Revolut statement) |
| 3 Jun 2024 | Vida The Hills Hotel | Accommodation — client business trip (user-confirmed) | 155.66 | Dubai hotel stay, same Emirates trip (booking CSHGVS) |
| 3 Jun 2024 | Blu Oasis Desert Hotel | Accommodation/excursion — client business trip (user-confirmed) | 6.50 | Same Dubai trip, small charge (possibly a desert excursion rather than a full stay) |
| various, deemed across the period | Use of home as office | Home working allowance | 312.00 | HMRC simplified flat rate for a director regularly working from home: £6/week × 52 weeks. No receipts or bill-splitting required under this flat rate — supported by the company's registered address being the director's home |
| various | American Express / Capital One | Card repayments, £100–£500/instance | not counted | User no longer has access to these card statements/accounts, so the underlying purchases can't be verified — **not claimed** |
| | | **Other genuine operating expenses (equipment, software, subscriptions)** | **0.00** | User confirmed no website hosting or other such costs incurred in this period |

**Total expenses counted so far: £4,580.10** (Companies House fee + two
bad debt write-offs + H3G at 50% apportionment + Berlin flight + Berlin
ground transport (Bolt/Uber) + Dubai trip flights + Dubai ground
transport + Dubai hotels + home working allowance)

## Net profit / (loss)

| | £ (approx.) |
|---|---|
| Total income (bank-verified, incl. unpaid invoice recognised on accruals basis) | 7,076.99 |
| Total expenses (bad debts + Companies House fee + H3G apportioned + Berlin flight + Berlin ground transport + Dubai flights + Dubai ground transport + Dubai hotels + home working allowance) | 4,580.10 |
| **Net trading profit / (loss) so far** | **≈ 2,496.89** |

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
5. ~~Other genuine operating expenses (equipment, software,
   subscriptions)~~ — **RESOLVED: user confirms none incurred** (no
   website hosting or similar costs this period).
6. ~~Berlin flight, 2–7 Sept 2023, £167.35~~ — **RESOLVED:** user
   confirms this trip was for the Connect SARL job (Invoice #9).
   Claimed as a pre-trading expense, deemed incurred on 11 Sept 2023.
7. ~~Dubai/Emirates flights, 8 May–3 Jun 2024, £703.46 + £425.00~~ —
   **RESOLVED:** user confirms this trip was for a client. Both the
   original booking and the change fee added as expenses.
8. ~~Berlin trip ground transport (Bolt/Uber)~~ — **RESOLVED:** 11
   receipts obtained (3 Bolt, 8 Uber, 2 duplicates), added under the
   same pre-trading expenditure treatment as the Berlin flight.
9. ~~Remaining flights~~ — **RESOLVED, all personal, NOT claimed:**
   - 28 Nov 2023 Ryanair £184.80 + 9 Jan 2024 Ryanair £117.24 —
     Marrakesh trip (reservations TI8YWS/CNFCQA, 1–11 Jan 2024)
   - 2 May 2024 Air France £25.70 — Paris
   - 29 Jun 2024 EasyJet £288.99 + 11 Jul 2024 Jet2 €92.23 — Malaga
   - 17 Jul 2024 + 24 Jul 2024 British Airways £17.50 + £32.50
   User confirmed all of the above were personal travel. No further
   flight expenses to add for Period A01 — the flight review is
   complete (Berlin and Dubai trips are the only claimed travel).
10. ~~Dubai hotels~~ — **RESOLVED:** user confirmed the full Dubai/Abu
    Dhabi trip was for the client. Vida The Hills (£155.66) and Blu
    Oasis Desert Hotel (£6.50) added as accommodation expenses.
11. ~~Use of home as office~~ — **RESOLVED:** user confirmed working
    from home; the company's registered address is the director's
    home. Claimed at HMRC's simplified flat rate (£6/week × 52 weeks =
    £312.00) — no receipts or bill-splitting required at this rate.
12. ~~VAT registration~~ — **RESOLVED:** user confirms turnover well
    under £15,000/year, far below the £85,000/£90,000 VAT registration
    threshold. Not VAT registered, correctly so.
13. ~~American Express / Capital One card spend~~ — **CLOSED, NOT
    CLAIMED:** user no longer has access to these card accounts/
    statements, so the underlying purchases can't be verified. Left
    out of the accounts rather than estimated.

## Notes / assumptions for this period

- See `/notes.md` sections 6a–6b for the full reconciliation log.
