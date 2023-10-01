# In this example you have to validate if a user input string is alphanumeric. 
# The given string is not nil/null/NULL/None, so you don't have to check that.

# The string has the following conditions to be alphanumeric:

# At least one character ("" is not valid)
# Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
# No whitespaces / underscore


# It`s time to regular expressions!

def alphanumeric(password: str) -> bool:
    import re
    pattern = r"^[a-zA-Z0-9]+$"
    return bool(re.match(pattern, password))

# Or... We could use password.isalnum(), but it is very easy xD

print(alphanumeric("str0ngPassw2rd"))
print(alphanumeric("str0ngPass_w2rd"))


