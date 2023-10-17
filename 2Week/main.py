def test_function(numbers):
    chars = [chr(num) for num in numbers]
    string = ''.join(chars)
    lower_string = string.lower()
    result_string = lower_string[2:10] * 2

    return result_string

# List are base on the ascii code
# chr functions to get ascii https://www.w3schools.com/python/ref_func_chr.asp
