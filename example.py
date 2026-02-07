inventory ={
    "BMW"
    "BUGATTI"
    "MERCEDEZ"
    "FERRARI"
}
def show_in_stock(stock_dict):
    print("items in stock")
    for item, quantity in stock_dict.items():
        if quantity > 0:
            print(f"- {item}; {quantity}")
show_in_stock (inventory)                

