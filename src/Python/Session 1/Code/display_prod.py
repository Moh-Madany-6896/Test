from prettytable import PrettyTable

def Display_Products (Products):
    table = PrettyTable ()
    table.field_names = ["ID", "Product Name", "Price '$'", "Stock 'Units'"]