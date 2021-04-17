a = lambda b: b + 7
b = lambda a, c: a + c

print(a(4))
print(b(4, 45))


def ghost_number(n):
    return lambda f: f * n


double_num = ghost_number(2)

print(double_num(20))
