import random

def karatsuba_multiply(num1: int, num2: int) -> int:
    """
    Multiplies two numbers using the Karatsuba algorithm.

    The Karatsuba algorithm is a fast multiplication algorithm that uses
    a divide and conquer approach. It's generally faster than the
    "grade school" multiplication for large numbers.

    Args:
        num1: The first integer.
        num2: The second integer.

    Returns:
        The product of num1 and num2.
    """

    # Ensure num1 is the smaller number for simplicity in digit counting.
    # This isn't strictly necessary for the algorithm's correctness but
    # simplifies the length calculation of the smaller number.
    if num1 > num2:
        num1, num2 = num2, num1

    # Convert numbers to strings to easily get their length.
    # We use the length of the smaller number (num1) to determine the split point.
    num1_str = str(num1)
    num2_str = str(num2) # Not strictly used for length, but kept for clarity of process

    # Base case: If the numbers are single digits, perform direct multiplication.
    # This is the stopping condition for the recursion.
    if len(num1_str) == 1:
        return num1 * num2

    # Determine the split point. We aim to split the number roughly in half.
    # 'half_digits' represents the number of digits in the lower half.
    # If the total number of digits is odd, the higher half will have one more digit.
    half_digits = len(num1_str) // 2

    # Calculate the splitting power of 10. This is used to divide numbers.
    # For example, if n=4, m=10^(4//2) = 100.
    # If n=5, m=10^(5//2) = 10^2 = 100.
    split_power_of_10 = 10 ** half_digits

    # Split num1 into two parts:
    # num1_high: The higher part (e.g., for 1234, if split at 2 digits, num1_high = 12)
    # num1_low: The lower part (e.g., for 1234, if split at 2 digits, num1_low = 34)
    num1_high = num1 // split_power_of_10
    num1_low = num1 % split_power_of_10

    # Split num2 into two parts similarly.
    num2_high = num2 // split_power_of_10
    num2_low = num2 % split_power_of_10

    # --- Recursive Steps (The core of Karatsuba) ---

    # Step 1: Calculate A = multiply(x1, y1)
    # This is the product of the high parts of the numbers.
    product_high_parts = karatsuba_multiply(num1_high, num2_high)

    # Step 2: Calculate C = multiply(x0, y0)
    # This is the product of the low parts of the numbers.
    product_low_parts = karatsuba_multiply(num1_low, num2_low)

    # Step 3: Calculate B = multiply(x1+x0, y1+y0) - A - C
    # This is the clever part. (x1+x0)(y1+y0) = x1*y1 + x1*y0 + x0*y1 + x0*y0
    # So, (x1+x0)(y1+y0) - A - C = (x1*y1 + x1*y0 + x0*y1 + x0*y0) - x1*y1 - x0*y0
    # This leaves x1*y0 + x0*y1, which is the middle term.
    sum_of_high_and_low_1 = num1_high + num1_low
    sum_of_high_and_low_2 = num2_high + num2_low
    product_of_sums = karatsuba_multiply(sum_of_high_and_low_1, sum_of_high_and_low_2)

    # Calculate the middle term using the results from the three recursive calls.
    # middle_term = (x1+x0)(y1+y0) - x1*y1 - x0*y0
    middle_term = product_of_sums - product_high_parts - product_low_parts

    # --- Combine the results ---
    # The final product is A * (10^n) + B * (10^(n/2)) + C
    # where n is the original number of digits and n/2 is half_digits.
    # So, A * (10^(2*half_digits)) + B * (10^half_digits) + C
    # Note: 10^(2*half_digits) is simply split_power_of_10 squared.
    result = (product_high_parts * (split_power_of_10 ** 2)) + \
             (middle_term * split_power_of_10) + \
             product_low_parts

    return result

# Example Usage:
if __name__ == "__main__":
    num_digits = 16 # Adjust number of digits for testing large numbers
    x_rand = random.randint(10**(num_digits-1), 10**num_digits - 1)
    y_rand = random.randint(10**(num_digits-1), 10**num_digits - 1)
    print(f"Multiplying {x_rand} and {y_rand}")
    result_karatsuba = karatsuba_multiply(x_rand, y_rand)
    result_standard = x_rand * y_rand
    print(f"Karatsuba Result: {result_karatsuba}")
    print(f"Standard Result: {result_standard}")
    print(f"Results match: {result_karatsuba == result_standard}")

    # Test with specific numbers
    num_a = 123456
    num_b = 789012
    print(f"\nMultiplying {num_a} and {num_b}")
    result_k = karatsuba_multiply(num_a, num_b)
    result_s = num_a * num_b
    print(f"Karatsuba Result: {result_k}")
    print(f"Standard Result: {result_s}")
    print(f"Results match: {result_k == result_s}")

    num_a = 12
    num_b = 34
    print(f"\nMultiplying {num_a} and {num_b}")
    result_k = karatsuba_multiply(num_a, num_b)
    result_s = num_a * num_b
    print(f"Karatsuba Result: {result_k}")
    print(f"Standard Result: {result_s}")
    print(f"Results match: {result_k == result_s}")

    num_a = 5
    num_b = 7
    print(f"\nMultiplying {num_a} and {num_b}")
    result_k = karatsuba_multiply(num_a, num_b)
    result_s = num_a * num_b
    print(f"Karatsuba Result: {result_k}")
    print(f"Standard Result: {result_s}")
    print(f"Results match: {result_k == result_s}")
