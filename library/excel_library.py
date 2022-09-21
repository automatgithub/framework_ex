import xlrd



def read_locators(filepath,sheetname):
    workbook = xlrd.open_workbook(filepath)
    worksheet = workbook.sheet_by_name(sheetname)

    rows = worksheet.get_rows()
    header = next(rows)

    d = {row[0].value:(row[1].value,row[2].value) for row in rows}
    return d


def read_test_data(filepath,sheetname):
    workbook = xlrd.open_workbook(filepath)
    worksheet = workbook.sheet_by_name(sheetname)

    rows = worksheet.get_rows()
    header = next(rows)
    data = [(row[0].value,row[1].value) for row in rows]
    return data

