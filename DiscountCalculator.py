def calculate_discount(price, discount_percent):
    """
    Calculates the final price after a discount.

    Args:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage.

    Returns:
        float: The final price after applying the discount, or the original price
               if the discount is less than 20%.
    """
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Calculate and return the final price
        final_price = price - discount_amount
        return final_price
    else:
