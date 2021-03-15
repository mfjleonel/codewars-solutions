# Return if a given word is a anagram of another.
# Note: Anagrams are case-insensitive.


def is_anagram(test, original):
    test = test.lower()
    original = original.lower()
    anagram = True
    if len(original) == len(test):
        for i in test:
            if i not in original:
                anagram = False
        for i in original:
            if i not in test:
                anagram = False
    else:
        anagram = False
    return anagram


# Examples:
#  "foefet" is an anagram of "toffee"
#  "Buckethead" is an anagram of "DeathCubeK"
