from prettytable import PrettyTable

def Display_Products (Products):
    if not Products:
        print("⚠️ No products to display.")
        return None
    table = PrettyTable ()
    table.field_names = ["ID", "Product Name", "Price '$'", "Stock 'Units'", "Category"]
    table.title = "📦 PRODUCTS INVENTORY"
    for x in Products:
        try:
            table.add_row ([x ["id"], str (x ["name"]).capitalize (), f"{x ["price"]:.2f}", int (x ["stock"]), str (x ["category"]).capitalize()])
        except (ValueError, TypeError):
            print(f"⚠️ Skipping invalid product data: {x}")
            continue
    print (table)