from openpyxl import *
import pandas as pd


def load_worksheet(file, sheet=0, ignore_hidden_rows=True, **kwargs):
    wb = load_workbook(file)
    if isinstance(sheet, int):
        sheet = wb.sheetnames[sheet]
    
    ws = wb[sheet]
    data = []
    if ignore_hidden_rows:
        rows_to_use = [r for r in ws if not ws.row_dimensions[r[0].row].hidden]
    else:
        rows_to_use = [r for r in ws]

    for i, row in enumerate(rows_to_use):
        if i == 0:
            headers = [cell.value for cell in row]
        else:
            values = [cell.value for cell in row]
            data.append(values)

    return pd.DataFrame(data, columns=headers, **kwargs).dropna()