# Corporation Tax Workings — Period 11 Sept 2023 to 10 Sept 2024

HMRC company tax reference: 623 24114 14574 A 01
Status: **FINAL — profit-and-loss.md is complete, figures below are
locked**

This period spans two UK financial years (FY2023: 1 Apr 2023–31 Mar 2024,
and FY2024: 1 Apr 2024–31 Mar 2025), so profit is technically
time-apportioned between them, same as HMRC did in their determination.
In practice this doesn't change the outcome here: the small profits rate
(19%) applies to both FY2023 and FY2024 portions, since actual profit
(£2,498.16 for the whole period) is nowhere near the £50,000 annual
threshold even before apportioning it — so a single 19% rate applies to
the whole period without needing marginal relief.

**Correction:** this file previously showed profit of £2,531.17. That
figure was based on a stale £1,280.00 estimate for the Invoice #10 bad
debt in profit-and-loss.md that was superseded when the FX conversion
was finalised at £1,246.99 (a £33.01 difference) — the income total in
that file wasn't updated at the time. Corrected here to the final
profit figure, £2,498.16. See notes.md for the full correction log.

## Step 1 — Apportionment of profit across financial years

| Financial year starting | Days in this CT period within that FY | Profit apportioned (£) | Rate | Tax (£) |
|---|---|---|---|---|
| 1 April 2023 (11 Sept 2023 – 31 Mar 2024) | 203 days | 1,385.61 | 19% | 263.27 |
| 1 April 2024 (1 Apr 2024 – 10 Sept 2024) | 163 days | 1,112.55 | 19% | 211.38 |
| **Total** | 366 days | **£2,498.16** | | **£474.65** |

(Profit apportioned pro-rata by days: £2,498.16 × 203/366 = £1,385.61;
£2,498.16 × 163/366 = £1,112.55.)

## Note on rate — Small Profits Rate vs Main Rate

UK corporation tax rates (FY2023 and FY2024):
- **Small profits rate: 19%** — applies where augmented profits are
  £50,000 or less (annual limit, apportioned for short periods / for the
  number of associated companies)
- **Main rate: 25%** — applies where augmented profits exceed £250,000
- **Marginal relief** — tapers the rate between £50,000 and £250,000

HMRC's determination assumed the full **25% main rate** on £38,159 —
this looks wrong on its face, since £38,159 is well under the £50,000
small profits threshold. **This is exactly the kind of overstatement a
real filed return corrects** — if the company has no associated companies,
the real rate due on actual profit (once known) should be **19%**, not 25%,
cutting the tax bill by roughly 24% relative to what HMRC assumed, on top
of the profit figure itself likely being much lower than £38,159.

**Open question:** does Atoure Ltd have any associated companies (e.g.
other companies under common control)? This affects whether the £50,000
small-profits threshold is divided between them. Assumed "no" — even if
there were one or two associated companies, the threshold divided
between them would still be far above this period's actual profit, so
this assumption doesn't put the 19% rate at risk. Flag for the
accountant to confirm formally.

## Step 2 — Tax payable

| | £ |
|---|---|
| Corporation tax chargeable | 474.65 |
| Less: marginal relief (not applicable — profit well under £50,000) | 0.00 |
| **Net corporation tax liability** | **474.65** |

## Comparison to HMRC's determination

| | HMRC determination | Our final calculation |
|---|---|---|
| Profit | £38,159 | £2,498.16 |
| Rate applied | 25% (flat) | 19% (small profits rate) |
| Tax | £9,539.75 | **£474.65** |

**The real corporation tax due for this period is £474.65 — about 5% of
HMRC's determination of £9,539.75.** This is the figure that should go
on the actual Company Tax Return, superseding HMRC's estimate once
filed.
