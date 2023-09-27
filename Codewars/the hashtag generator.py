def generate_hashtag(to_formate : str) -> str:
    if len(to_formate) == 0:
        return 0
    tmp = to_formate.split()
    fixed_str = ''.join([x[0].upper()+x[1:].lower() for x in tmp])
    to_push = "#" + fixed_str
    if len(to_push) > 140:
        return 0
    return to_push

print(generate_hashtag(" fdg dfh  sd sfhdfh sd hdfhdfh"))

#It must start with a hashtag (#).
#All words must have their first letter capitalized.
#If the final result is longer than 140 chars it must return false.
#If the input or the result is an empty string it must return false.