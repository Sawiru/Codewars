#task
# Give you two strings: s1 and s2. If they are opposite, return true; otherwise, return false. Note: The result should be a boolean value, instead of a string.

# The opposite means: All letters of the two strings are the same, but the case is opposite. you can assume that the string only contains letters or it's a empty string. Also take note of the edge case - if both strings are empty then you should return false/False.

def is_opposite(s1,s2):
    if not s1 or not s2:
        return False
    if len(s1) != len(s2):
        return False
    
    for c1, c2 in zip(s1,s2):
        if c1.lower() != c2.lower() or c1 == c2:
            return False
    
    return True

#best case code

def is_opposite(s1, s2):
    return False if not(s1 or s2) else s1.swapcase() == s2