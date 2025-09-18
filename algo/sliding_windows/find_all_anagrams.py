def is_same_word(word1: str, word2: str) -> bool:
    return sorted(word1) == sorted(word2)


# print(is_same_word("bab", "abc"))


# cbaebabacd
# abc
def find_all_anagrams(original: str, check: str) -> list[int]:
    """
    Given a string original and a string check, find the starting index of all substrings of original that is an anagram of check. The output must be sorted in ascending order.

    Parameters
    original: A string
    check: A string
    Result
    A list of integers representing the starting indices of all anagrams of check.
    """
    res = []
    start = 0
    while start < len(original) - len(check) + 1:
        s = original[start : start + len(check)]
        print(start, s, check)
        if is_same_word(s, check):
            res.append(start)

        start += 1

    return res


print(find_all_anagrams("cbaebabacd", "abc"))
# print(find_all_anagrams("abab", "ab"))
# print(find_all_anagrams("nabanabannaabbaanana", "banana"))
