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

        return price


try:
    # Prompt the user for the original price
    original_price = float(input("Enter the original price of the item: "))
    

    discount_percentage = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount_percentage)

    # Print the result based on whether a discount was applied
    if final_price < original_price:
        print(f"\nOriginal price: ${original_price:.2f}")
        print(f"Discount applied: {discount_percentage:.2f}%")
        print(f"Final price after discount: ${final_price:.2f}")
    else:
        print(f"\nOriginal price: ${original_price:.2f}")
        print("No discount was applied because the percentage was less than 20%.")
        print(f"Final price: ${final_price:.2f}")

except ValueError:
    # Handling cases where the user enters non-numeric input
    print("\nInvalid input. Please enter valid numbers for price and discount.")
