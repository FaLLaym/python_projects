# Define a function that takes an integer argument and 
# returns a logical value true or false depending on if the integer is a prime.

# Requirements:
# You can assume you will be given an integer input.
# You can not assume that the integer will be only positive. 
# You may be given negative numbers as well ( or 0 ).

# Example:
# is_prime(1)  /* false */
# is_prime(2)  /* true  */
# is_prime(-1) /* false */


def is_prime(x: int) -> bool:
    dive = set()
    try:
        for i in range(1, int(x**.5)+1):
            if x % i == 0:
                dive |= {i, x//i}
    except:
        ...
    finally:
        return 1 if len(dive)==2 else 0


