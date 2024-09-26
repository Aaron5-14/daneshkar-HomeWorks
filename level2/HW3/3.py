"""
Name: Ali Shirazi Zamani
Level: 2
Homework: 3
Exercise: 3 
To do: Why does the assert in apply_discount function below not work?
fix the function and check if assert is a good way to do validation.
"""

def appy_discount(price: int, discount: float = 0.0) -> int:
    """Apply Discount Percent and Calculate Final Price"""
    final_price = int(price * (1 - discount))
    assert(0 < final_price <= price, "Why this AssertionError never Raised!")
    return final_price

# Removed parantheses from assert:
def apply_discount_assert_fixed(price : int, discount: float = 0.0) -> int:
    """Apply Discount Percent and Calculate Final Price"""
    final_price = int(price * (1- discount))
    assert 0 < final_price <= price, "Removed Parantheses for This AssertionError to Work!"
    return final_price

# After executing using -O parameter it seems that assert is not executed. 
# After further research it seems assert is IGNORED automatically when 
# python wants to do optimization of the bytecode. so it is better to use 
# assert only for debugging and finding errors in development phase.
# Below we can just make it so for wrong inputs the fucntion returns 
# -1 to signal error.
def apply_discount_rewritten(price: int, discount: float = 0.0) -> int:
    """Apply Discount Percent and Calculate Final Price"""

    # Filter all possible instances where (0 < final_price <= price) is false
    if price < 0 or discount < 0 or discount > 1:
        print("ValueError: Invalid inputs in apply_discount function.")
        return -1
    
    final_price = int(price * (1- discount))
    return final_price
