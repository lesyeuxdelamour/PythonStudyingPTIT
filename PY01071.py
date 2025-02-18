def check(s):
    return "yes" if s[-3:].lower() == ".py" else "no"

print(check(input()))