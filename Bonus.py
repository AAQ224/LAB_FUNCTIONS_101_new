code = None

def calculates_exact_digits(code, secret_code="4271"):
    """
    Calculates the number of exact digit matches between code and secret_code.
    Args:
        code (str): The code entered by the user.
        secret_code (str, default="4271"): The secret code to compare against.
    Returns:
        int: The number of digits that match in both value and position.
    """
    exact_count = 0
    for i in range(len(code)):
        if code[i] == secret_code[i]:
            exact_count += 1
    return exact_count

def calculates_misplaced_digits(code, secret_code="4271"):
    """
    Calculates the number of misplaced digit matches between code and secret_code.
    Args:
        code (str): The code entered by the user.
        secret_code (str, default="4271"): The secret code to compare against.
    Returns:
        int: The number of digits that match in value but not in position.
    """
    misplaced_count = 0
    for i in range(len(code)):
        if code[i] != secret_code[i] and code[i] in secret_code:
            misplaced_count += 1
    return misplaced_count


while code != "4271":
    code = input("Enter a secret code (4 characters): ")

    if len(code) != 4:
        print("Invalid code. Please enter exactly 4 characters.")
        continue
    else:
        exact_digits = calculates_exact_digits(code)
        misplaced_digits = calculates_misplaced_digits(code)

        print(f"Exact digits: {exact_digits}", end='    |    ')
        print(f"Misplaced digits: {misplaced_digits}")

