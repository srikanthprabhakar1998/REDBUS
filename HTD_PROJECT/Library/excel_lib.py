import xlrd
from Library.config import Configuration


class ReadExcel:
    def read_testdata(self, sheetname):

        wd = xlrd.open_workbook(Configuration.TEST_DATA)
        ws = wd.sheet_by_name(sheetname)
        columns = ws.ncols
        rows = ws.get_rows()
        header = next(rows)
        data = []

        for row in rows:
            values = ()
            for j in range(columns):
                values += (row[j].value,)
            data.append(values)
        return data

    def read_locator(self, sheetname):

        wd = xlrd.open_workbook(Configuration.LOCATOR_PATH)
        ws = wd.sheet_by_name(sheetname)
        rows = ws.get_rows()
        header = next(rows)
        d = {}
        for row in rows:
            d[row[0].value] = (row[1].value, row[2].value)
        return d
