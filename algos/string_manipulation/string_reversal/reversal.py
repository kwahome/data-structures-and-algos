def inplace_reverse(string):
    string = list(string)
    length = len(string)
    # walk towards the middle, from both sides
    for left in range(length//2):
        right = length - left - 1
        string[left], string[right] = string[right], string[left]
    return "".join(string)
