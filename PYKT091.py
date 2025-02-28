from collections import Counter

def isPalindrome(s):
    return s == s[::-1]

def _sinusoid_():
    with open("VANBAN.in", "r") as file:
        a = []
        for line in file:
            a += line.split()
        freq = Counter([x for x in a if isPalindrome(x)])
        maxLen = max(map(len, freq))
        for words, count in freq.items():
            if len(words) == maxLen:
                print(words, count)

if __name__ == "__main__":
    _sinusoid_()