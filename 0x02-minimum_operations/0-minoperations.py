#!/usr/bin/python3
def minOperations(n):
    if n <= 0:
        return 0
    
    operations = 0
    copy = 1  # The current number of characters in the clipboard
    chars = 1  # The current number of characters in the text file
    
    while chars < n:
        if n % chars == 0:  # If n is divisible by the current number of characters
            copy = chars
        chars += copy
        operations += 1
    
    return operations
    