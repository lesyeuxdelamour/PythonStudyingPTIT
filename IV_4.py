def _sinusoid_():
	word = max(input().split(), key = len)
	print(word, len(word))

if __name__ == "__main__":
    _sinusoid_()