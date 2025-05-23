# Author: <Antim Pal>
# Date: <21-04-2025>
# Description: Write a Python program to split a string and append it to another string.
# Input: "Hello World", "Python"
# Output: "Hello World Python"
# Example: "Hello World" + "Python" = "Hello World Python"
# Input: "Hello World", "Python"
# Output: "Hello World Python"


def split_and_append(str1, str2):
    """
    This function takes two strings, splits the first string into words,
    and appends the second string to the first string.
    
    :param str1: The first string to be split
    :param str2: The second string to be appended
    :return: The combined string
    """
    # Split the first string into words
    words = str1.split()
    
    # Append the second string to the first string
    result = ' '.join(words) + ' ' + str2
    
    return result


# Test the function
str1 = "Hello World"
str2 = "Python"
result = split_and_append(str1, str2)
print(result)  # Output: "Hello World Python"

# Function to test the split_and_append function with different inputs
def test_split_and_append():
    assert split_and_append("Hello World", "Python") == "Hello World Python"
    assert split_and_append("Good Morning", "Everyone") == "Good Morning Everyone"
    assert split_and_append("Welcome to", "Python Programming") == "Welcome to Python Programming"
    assert split_and_append("Split this string", "and append") == "Split this string and append"
    assert split_and_append("", "Empty String") == " Empty String"
    assert split_and_append("SingleWord", "") == "SingleWord "
    print("All tests passed!")


test_split_and_append()