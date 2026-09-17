# CT600 — Figures to Hand to Accountant (or Enter into Filing Software)

Status: **BOTH PERIODS FINAL — P&L complete and bank-verified for A01
and A02**

This is not the CT600 form itself (that's filed digitally, in specific
software, in iXBRL format) — it's the set of figures your accountant needs
to complete boxes on the CT600, laid out per period, so they don't have to
derive them from scratch.

## Period 1: 11 Sept 2023 – 10 Sept 2024 (ref ...A01) — FINAL

| CT600 box (approx.) | Description | Value |
|---|---|---|
| Box 30 | Turnover | £7,043.98 |
| Box 155 | Trading profit | £2,498.16 |
| Box 165 | Profits chargeable to Corporation Tax | £2,498.16 |
| Box 475/480-ish | Corporation Tax chargeable | £474.65 |
| — | Rate applied | 19% (small profits rate — see corporation-tax-workings.md) |

Full backing detail (every income/expense line, source documents, FX
methodology) is in
`../periods/2023-09-11_2024-09-10/profit-and-loss.md` and
`../periods/2023-09-11_2024-09-10/corporation-tax-workings.md`.

## Period 2: 11 Sept 2024 – 30 Sept 2024 (ref ...A02) — FINAL

| CT600 box (approx.) | Description | Value |
|---|---|---|
| Box 30 | Turnover | £50.00 |
| Box 155 | Trading profit | £41.37 |
| Box 165 | Profits chargeable to Corporation Tax | £41.37 |
| Box 475/480-ish | Corporation Tax chargeable | £7.86 |
| — | Rate applied | 19% (small profits rate) |

Full backing detail is in
`../periods/2024-09-11_2024-09-30/profit-and-loss.md` and
`../periods/2024-09-11_2024-09-30/corporation-tax-workings.md`.

**Note:** exact box numbers depend on the CT600 version/software in use —
treat the labels as the important part; your accountant or filing software
will map them to the right boxes.

## Combined total across both periods

| | A01 | A02 | Combined |
|---|---|---|---|
| Turnover | £7,043.98 | £50.00 | £7,093.98 |
| Profit | £2,498.16 | £41.37 | £2,539.53 |
| Corporation tax | £474.65 | £7.86 | **£482.51** |

Compare to HMRC's combined determination: £38,159 + £3,180 = £41,339
profit assumed, £9,539.75 + £795.00 = **£10,334.75 tax assumed**. The
real combined tax due (£482.51) is about **4.7%** of HMRC's estimate.
