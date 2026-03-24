shopping_list = [
    {"name":"Rice", "price":50, "quantity":2}, 
    {"name":"Wheat", "price":30, "quantity":3}
] 
print("Shopping List:")
print(shopping_list)

def calculate_total_bill():
    total_bill=0
    for item in shopping_list:
        total_bill += item["price"] * item["quantity"]
    print("Total Bill:",total_bill)
calculate_total_bill()

shopping_list.pop(0)
print("After Removing Rice:")
print(shopping_list)    