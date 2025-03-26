# generate_binary_strings Function
def generate_binary_strings(n, result=''):
    
    # Base case
    if len(result) == n:
        print(result)
        return

    # Append '0' to the string and recurse
    generate_binary_strings(n, result + '0')

    # Append '1' to the string and recurse
    generate_binary_strings(n, result + '1')


if _name_ == "_main_":
    n = 2  # number of bits
    generate_binary_strings(n)