def inplace_reverse(string):
    string = list(string)
    length = len(string)
    for index in range(length//2):
        string[index], string[length - index - 1] = string[length - index - 1], string[index]
    return "".join(string)
