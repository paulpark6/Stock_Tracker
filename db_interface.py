import xlrd
import xlsxwriter

columns = ["ID", "Item Name", "Buy Price", "Sell Price" ,"Quantity"]

def write_to_database(item_name, buy_price, sell_price , quantity):
    existing_data = read_from_database()

    # place to store workbook after edits 
    wb = xlsxwriter.Workbook("./DataBase/transactions.xlsx")
    ws = wb.add_worksheet()


    # write existing data
    len_row = len(existing_data)
    len_col = len(existing_data[0])
    if len(existing_data) != 0:
        for row in range(len_row):
            for col in range(len_col):
                ws.write(row, col, existing_data[row][col])

    # write headers
    n = len(columns)
    for col in range(n):
        ws.write(0,col,columns[col])

    # write new data
    if len_row == 0:
        len_row = 1
    # writing id first
    ws.write(len_row, 0, len_row)
    # writing item name
    ws.write(len_row, 1, item_name)
    # buy price    
    ws.write(len_row, 2, buy_price)
    # sell price
    ws.write(len_row, 3, sell_price)
    # quantity
    ws.write(len_row, 3, quantity)

    # save file
    wb.close() # make sure to close the wb to see the changes and save the edits

def read_from_database():
    # work book from excel, open it at the addresss
    wb = xlrd.open_workbook("./DataBase/transactions.xlsx")
    # choose which sheet to read from from the work book
    ws = wb.sheet_by_index(0) # 0 is going to be first sheet, 1 is second sheet ... and so on

    #  Columns are [ID, item name, buy price, quantity]
    all_rows = [] # empty list that will store all the rows in the excel file
    # each row will be a list, all rows will have list of each row
    for row in range(ws.nrows): # .nrows -> how many rows we actaully have
        current_row = []
        for col in range(len(columns)):
            current_row.append(ws.cell_value(row,col)) # .cell_value("which row", "which column")
        all_rows.append(current_row)
    return all_rows
