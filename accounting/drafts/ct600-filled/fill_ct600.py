import fitz  # pymupdf

SRC = '/root/.claude/uploads/90b53ef5-dbc5-5037-8388-3b680a6b79cc/30ed4667-ct600.pdf'

FONT = 'helv'
SIZE_DIGIT = 10.5
SIZE_TEXT = 10
COLOR = (0, 0, 0.55)  # dark blue ink, distinguishes from printed black form text

def get_digit_cells(page, y_anchor, tol=2.2):
    cells = []
    for d in page.get_drawings():
        r = d['rect']
        if abs(r.y0 - y_anchor) <= tol and 12.5 <= r.width <= 16 and 14 <= r.height <= 18:
            cells.append((round(r.x0, 2), round(r.y0, 2), round(r.x1, 2), round(r.y1, 2)))
    cells.sort()
    return cells

def put_char(page, cell, ch, size=SIZE_DIGIT):
    x0, y0, x1, y1 = cell
    cx = (x0 + x1) / 2
    # baseline roughly 3.2pt above cell bottom for this font/size
    by = y1 - 4.0
    tw = fitz.get_text_length(ch, fontname=FONT, fontsize=size)
    page.insert_text((cx - tw / 2, by), ch, fontname=FONT, fontsize=size, color=COLOR)

def fill_money_row(page, y_anchor, pounds_str, pence_str='00'):
    """pounds_str: e.g. '7043' (no separators). pence_str: 2 digits."""
    cells = get_digit_cells(page, y_anchor)
    assert len(cells) >= 3, f'expected money row at y={y_anchor}, got {len(cells)} cells'
    pound_cells = cells[1:-2]   # drop leading £-symbol cell, drop trailing 2 pence cells
    pence_cells = cells[-2:]
    if len(pounds_str) > len(pound_cells):
        raise ValueError(f'pounds value {pounds_str} too long for {len(pound_cells)} cells at y={y_anchor}')
    used = pound_cells[-len(pounds_str):]
    for ch, cell in zip(pounds_str, used):
        put_char(page, cell, ch)
    for ch, cell in zip(pence_str, pence_cells):
        put_char(page, cell, ch)

def fill_digit_group(page, cells, value_str):
    assert len(value_str) == len(cells), (value_str, len(cells))
    for ch, cell in zip(value_str, cells):
        put_char(page, cell, ch)

def fill_open_box(page, x0, y0, x1, y1, text, align='right', size=SIZE_TEXT, pad=4):
    tw = fitz.get_text_length(text, fontname=FONT, fontsize=size)
    by = y1 - (y1 - y0) / 2 - size * 0.32
    if align == 'right':
        tx = x1 - pad - tw
    elif align == 'left':
        tx = x0 + pad
    else:
        tx = x0 + (x1 - x0 - tw) / 2
    page.insert_text((tx, by), text, fontname=FONT, fontsize=size, color=COLOR)

def money_to_parts(value):
    """£1234.5 -> ('1234','50')"""
    cents = round(value * 100)
    pounds, pence = divmod(cents, 100)
    return str(pounds), f'{pence:02d}'

def tick(page, x0, y0, x1, y1):
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    size = 11
    tw = fitz.get_text_length('X', fontname=FONT, fontsize=size)
    page.insert_text((cx - tw / 2, cy + size * 0.32), 'X', fontname=FONT, fontsize=size, color=COLOR)


COMPANY_NAME = 'Atoure Ltd'
COMPANY_NO = '15129711'
UTR = '2411414574'
TYPE_CODE = '00'
DECL_NAME = 'Abdul-Malik Baba Toure'
DECL_STATUS = 'Director'
DECL_DATE = '28092026'  # DD MM YYYY, no separators, 8 digits

# Row y-anchors (top y0 of the digit-cell row), confirmed against the real form
Y = {
    'name_box': (210.5, 234.4, 538.6, 250.9),
    'regno': 258.4,
    'utr': 283.9,
    'type': 308.7,
    'date_from': 517.0,
    'date_to': 517.0,
    'box80': (525.2, 73.5, 538.8, 90.0),
    'box145': 565.6,
    'box155': 648.0,
    'box165': 713.2,
    'box235': 559.1,
    'box300': 266.8,
    'box315': 371.8,
    'box326': (488.6, 499.3, 539.0, 515.8),
    'box329': (523.6, 574.3, 537.3, 590.8),
    'box430': 74.0,
    'box435': 98.5,
    'box440': 122.9,
    'box475': 593.7,
    'box510': 194.7,
    'box525': 280.3,
    'box528': 406.4,
    'box600': 245.6,
    'decl_name_box': (63.4, 697.0, 539.1, 713.6),
    'decl_date': 737.4,
    'decl_status_box': (63.4, 777.7, 539.1, 794.2),
}

# Date digit cells, page 0 (from direct inspection — not auto-derived since they're grouped DD/MM/YYYY)
DATE_FROM_CELLS = {
    'DD': [(63.1, 517.0, 76.8, 533.5), (78.7, 517.0, 92.4, 533.5)],
    'MM': [(101.4, 517.0, 115.1, 533.5), (117.0, 517.0, 130.6, 533.5)],
    'YYYY': [(139.6, 517.0, 153.3, 533.5), (155.2, 517.0, 168.9, 533.5),
             (170.8, 517.0, 184.5, 533.5), (186.4, 517.0, 200.1, 533.5)],
}
DATE_TO_CELLS = {
    'DD': [(401.6, 517.0, 415.2, 533.5), (417.2, 517.0, 430.8, 533.5)],
    'MM': [(439.8, 517.0, 453.5, 533.5), (455.4, 517.0, 469.1, 533.5)],
    'YYYY': [(478.1, 517.0, 491.8, 533.5), (493.7, 517.0, 507.4, 533.5),
             (509.3, 517.0, 523.0, 533.5), (524.9, 517.0, 538.5, 533.5)],
}
DECL_DATE_CELLS = [
    (63.4, 737.4, 77.1, 753.9), (79.0, 737.4, 92.7, 753.9),
    (101.7, 737.4, 115.3, 753.9), (117.3, 737.4, 130.9, 753.9),
    (139.9, 737.4, 153.6, 753.9), (155.5, 737.4, 169.2, 753.9),
    (171.1, 737.4, 184.8, 753.9), (186.7, 737.4, 200.4, 753.9),
]

REGNO_CELLS_Y = 258.4
REGNO_X = [415.3, 430.9, 446.5, 462.1, 477.7, 493.2, 508.8, 524.4]
UTR_X = [384.8, 400.4, 416.0, 431.6, 447.2, 462.8, 478.4, 494.0, 509.6, 525.2]
TYPE_X = [509.6, 525.2]

# Tax-calc table (page idx 3) — open boxes, not digit grids
TAXCALC_ROWS = {
    'block1': {'y0': 662.8, 'y1': 686.2},  # boxes 330/335/340/345
    'block2': {'y0': 733.0, 'y1': 756.4},  # boxes 380/385/390/395
}
TAXCALC_COLS = {
    'fy': (71.6, 134.4),
    'amount': (166.8, 305.4),
    'rate': (341.6, 403.1),
    'tax': (438.5, 558.4),
}


def date_ddmmyyyy(d, m, y):
    return f'{d:02d}', f'{m:02d}', f'{y:04d}'


def fill_period(period_from, period_to, turnover, trading_profit, fy_rows, tax_total, out_path):
    """
    fy_rows: list of (fy_year:int, amount:float, rate:int, tax:float), 1 or 2 entries
    """
    doc = fitz.open(SRC)

    # --- Page 1 (idx 0): company info + period dates ---
    p0 = doc[0]
    fill_open_box(p0, *Y['name_box'], COMPANY_NAME, align='left')
    fill_digit_group(p0, [ (x, REGNO_CELLS_Y, x+13.6, REGNO_CELLS_Y+16.5) for x in REGNO_X ], COMPANY_NO)
    fill_digit_group(p0, [ (x, Y['utr'], x+13.6, Y['utr']+16.5) for x in UTR_X ], UTR)
    fill_digit_group(p0, [ (x, Y['type'], x+13.6, Y['type']+16.5) for x in TYPE_X ], TYPE_CODE)

    d, m, y = period_from
    dd, mm, yyyy = date_ddmmyyyy(d, m, y)
    fill_digit_group(p0, DATE_FROM_CELLS['DD'], dd)
    fill_digit_group(p0, DATE_FROM_CELLS['MM'], mm)
    fill_digit_group(p0, DATE_FROM_CELLS['YYYY'], yyyy)

    d, m, y = period_to
    dd, mm, yyyy = date_ddmmyyyy(d, m, y)
    fill_digit_group(p0, DATE_TO_CELLS['DD'], dd)
    fill_digit_group(p0, DATE_TO_CELLS['MM'], mm)
    fill_digit_group(p0, DATE_TO_CELLS['YYYY'], yyyy)

    # --- Page 2 (idx 1): box 80 tick, 145/155/165 ---
    p1 = doc[1]
    tick(p1, *Y['box80'])
    tp, tpence = money_to_parts(turnover)
    fill_money_row(p1, Y['box145'], tp, tpence)
    pp, ppence = money_to_parts(trading_profit)
    fill_money_row(p1, Y['box155'], pp, ppence)
    fill_money_row(p1, Y['box165'], pp, ppence)

    # --- Page 3 (idx 2): box 235 ---
    p2 = doc[2]
    fill_money_row(p2, Y['box235'], pp, ppence)

    # --- Page 4 (idx 3): 300/315/326/329 + tax-calc table ---
    p3 = doc[3]
    fill_money_row(p3, Y['box300'], pp, ppence)
    fill_money_row(p3, Y['box315'], pp, ppence)
    fill_open_box(p3, *Y['box326'], '0', align='right')
    tick(p3, *Y['box329'])

    blocks = ['block1', 'block2']
    for i, (fy, amount, rate, tax) in enumerate(fy_rows):
        blk = TAXCALC_ROWS[blocks[i]]
        y0, y1 = blk['y0'], blk['y1']
        fx0, fx1 = TAXCALC_COLS['fy']
        fill_open_box(p3, fx0, y0, fx1, y1, str(fy), align='left')
        ax0, ax1 = TAXCALC_COLS['amount']
        fill_open_box(p3, ax0, y0, ax1, y1, f'{amount:,.2f}', align='right')
        rx0, rx1 = TAXCALC_COLS['rate']
        fill_open_box(p3, rx0, y0, rx1, y1, str(rate), align='right')
        tx0, tx1 = TAXCALC_COLS['tax']
        fill_open_box(p3, tx0, y0, tx1, y1, f'{tax:,.2f}', align='right')

    # --- Page 5 (idx 4): 430/435/440/475 ---
    p4 = doc[4]
    totalp, totalpence = money_to_parts(tax_total)
    fill_money_row(p4, Y['box430'], totalp, totalpence)
    fill_money_row(p4, Y['box435'], '0', '00')
    fill_money_row(p4, Y['box440'], totalp, totalpence)
    fill_money_row(p4, Y['box475'], totalp, totalpence)

    # --- Page 6 (idx 5): 510/525/528 ---
    p5 = doc[5]
    fill_money_row(p5, Y['box510'], totalp, totalpence)
    fill_money_row(p5, Y['box525'], totalp, totalpence)
    fill_money_row(p5, Y['box528'], totalp, totalpence)

    # --- Page 7 (idx 6): 600 ---
    p6 = doc[6]
    fill_money_row(p6, Y['box600'], totalp, totalpence)

    # --- Page 12 (idx 11): declaration ---
    p11 = doc[11]
    fill_open_box(p11, *Y['decl_name_box'], DECL_NAME, align='left')
    fill_digit_group(p11, DECL_DATE_CELLS, DECL_DATE)
    fill_open_box(p11, *Y['decl_status_box'], DECL_STATUS, align='left')

    doc.save(out_path)
    doc.close()


if __name__ == '__main__':
    # A01 — 11 Sept 2023 to 10 Sept 2024
    fill_period(
        period_from=(11, 9, 2023), period_to=(10, 9, 2024),
        turnover=7043.98, trading_profit=2498.16,
        fy_rows=[(2023, 1385.61, 19, 263.27), (2024, 1112.55, 19, 211.38)],
        tax_total=474.65,
        out_path='/tmp/atoure-pdfs/CT600-A01-filled.pdf',
    )
    # A02 — 11 Sept 2024 to 30 Sept 2024
    fill_period(
        period_from=(11, 9, 2024), period_to=(30, 9, 2024),
        turnover=50.00, trading_profit=41.37,
        fy_rows=[(2024, 41.37, 19, 7.86)],
        tax_total=7.86,
        out_path='/tmp/atoure-pdfs/CT600-A02-filled.pdf',
    )
    # Period 3 — 1 Oct 2024 to 30 Sept 2025
    fill_period(
        period_from=(1, 10, 2024), period_to=(30, 9, 2025),
        turnover=3680.45, trading_profit=2911.27,
        fy_rows=[(2024, 1451.76, 19, 275.83), (2025, 1459.51, 19, 277.31)],
        tax_total=553.14,
        out_path='/tmp/atoure-pdfs/CT600-Period3-filled.pdf',
    )
    print('done')
