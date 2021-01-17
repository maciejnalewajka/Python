#NWD
def gcd(a, b):
    while b != 0:
        b, a = a % b, b
    return a

# NWW
def lcm(a, b):
    return abs( a * b / gcd(a, b) )

# Hanoi
def hanoi(n, source, helper, target):
    if n > 0:
        hanoi(n - 1, source, target, helper)
        if source:
            target.append(source.pop())
        hanoi(n - 1, helper, source, target)

# Anagram
def delSpac(s):
    s_new = s.replace(" ","")
    return s_new

def anagram(s1,s2):
    alist1 = list(delSpac(s1))
    alist2 = list(delSpac(s2))
    alist1.sort()
    alist2.sort()
    pos = 0
    matches = True
    while pos < len(delSpac(s1)) and matches:
        if alist1[pos]==alist2[pos]:
            pos = pos + 1
        else:
            matches = False
    return matches
