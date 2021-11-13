import collections


def is_anagram(first, second):
    if len(first) != len(second):
        return False
    else:
        return not collections.Counter(first) - collections.Counter(second)
