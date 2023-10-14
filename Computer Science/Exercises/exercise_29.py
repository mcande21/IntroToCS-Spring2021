def run_length_encode(s):
    """
    Produce a run-length encoded string
    :param s: (str) a string with (hopefully) many repeated
    letters
    :return: a run-length encoded version of s
    """
    run_code = ""
    counter = 1
    # for i in range(len(s)):
    #     if run_code.find(s[i]) == -1:
    #         run_code += s[i]
    #     elif run_code.find(s[i]) != -1:
    #         counter = 0
    #         old_i = s[i]
    #         while old_i == s[i]:
    #             counter += 1
    #             old_i = s[counter]
    #         run_code += (s[i], counter)
    # return run_code

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            counter += 1
        else:
            run_code += s[i-1] + str(counter)
            counter = 1
    run_code += s[len(s)-1] + str(counter)
    return run_code

print(run_length_encode("aaabccddeeeeffgghhijklmmmmnooo"))