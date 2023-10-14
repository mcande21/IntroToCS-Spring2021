# This function will return a unique list that is non dupplicate letters from a previous string


def unique_chars(s):
    """
    Return a string of all the unique characters from the
    given argument.
    If you happen to already know other Python data structures
    such as lists, dictionaries, or sets, you may not use them
    :param s: (str) a string
    :return: all of the unique characters in s
    """
    check = ""
    for i in range(len(s)):
        if check.find(s[i]) == -1:
            check += s[i]
    return check

print(unique_chars("abbdgfbgssdgfbwhj"))
