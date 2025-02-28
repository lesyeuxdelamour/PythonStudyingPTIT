import re

def _sinusoid_():
    inp = ""
    while True:
        try:
            inp += input() + ' '
        except EOFError:
            break
    inp = re.split(r'[.?!]', inp)
    for sen in inp:
        print(' '.join(sen.split()).capitalize())

if __name__ == "__main__":
    _sinusoid_()