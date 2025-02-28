def _sinusoid_():
    inp = []
    while True:
        try:
            inp.append(input())
        except EOFError:
            break
    for sen in inp:
        if sen[-1] in ".!?":
            punc = sen[-1]
            sen = sen[:-1]
        else:
            punc = '.'
        tmp = sen.split()
        print(' '.join(tmp).capitalize() + punc)

if __name__ == "__main__":
    _sinusoid_()