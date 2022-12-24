import xlsxwriter
import xlrd

def write_db_test():
    wb = xlrd.open_workbook("./DataBase/transactions.xlsx")
    print(wb)
