# Дорешивание, AC, Принята

def f(s, l, c1, c2, s1, s2, op):
    if l == n:
        if (c1 == c2) and (s1 == s2):
            print(s)
        return

    if l == 0:
        f(s + '[', l + 1, c1, c2, s1 + 1, s2, op + '[')
        f(s + '(', l + 1, c1 + 1, c2, s1, s2, op + '(')

    elif s[-1] == '[':
        f(s + '[', l + 1, c1, c2, s1 + 1, s2, op + '[')
        f(s + ']', l + 1, c1, c2, s1, s2 + 1, op[:-1])
        f(s + '(', l + 1, c1 + 1, c2, s1, s2, op + '(')

    elif s[-1] == '(':
        f(s + '(', l + 1, c1 + 1, c2, s1, s2, op + '(')
        f(s + ')', l + 1, c1, c2 + 1, s1, s2, op[:-1])
        f(s + '[', l + 1, c1, c2, s1 + 1, s2, op + '[')

    elif (s[-1] == ']') or (s[-1] == ')'):
        f(s + '[', l + 1, c1, c2, s1 + 1, s2, op + '[')
        f(s + '(', l + 1, c1 + 1, c2, s1, s2, op + '(')
        if (s1 > s2) and (op[-1] == '['):
            f(s + ']', l + 1, c1, c2, s1, s2 + 1, op[:-1])
        if (c1 > c2) and (op[-1] == '('):
            f(s + ')', l + 1, c1, c2 + 1, s1, s2, op[:-1])


n = int(input())
f('', 0, 0, 0, 0, 0, '')

