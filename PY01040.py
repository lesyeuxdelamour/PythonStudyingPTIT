def divide(s):
    return s[:len(s) // 2], s[len(s) // 2:]

def rotate(s):
    total = sum(ord(i) - ord('A') for i in s)
    return ''.join(chr((ord(i) - ord('A') + total) % 26 + ord('A')) for i in s)

def merge(s1, s2):
    return ''.join(chr((ord(s1[i]) + ord(s2[i]) - 2 * ord('A')) % 26 + ord('A')) for i in range(len(s1)))

def DRM(s):
    s1, s2 = (rotate(i) for i in divide(s))
    return merge(s1, s2)

def _sinusoid_():
    for _ in range(int(input())):
        s = input()
        print(DRM(s))

if __name__ == "__main__":
    _sinusoid_()