def is_unique_chars(s):
    """
    Return True if all the characters in the string s are
    unique.
    If you happen to already know other Python data structures
    such as lists, dictionaries, or sets, you may not use them
    :param s: (str) a string
    :return: True if the characters in s are unique
    """
    check = ""
    for i in range(len(s)):
        if check.find(s[i]) == -1:
            check += s[i]
    if len(check) == len(s):
        return True
    else:
        return False

print(is_unique_chars("abcde"))
print(is_unique_chars("abded"))