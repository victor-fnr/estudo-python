# %%

A = 1
B = 5

print(A)
print(B)

# %%

C = A
A = B
B = C

print(A)
print(B)

# %%

A, B = B, A

print(A)
print(B)

# %%

a, b, *resto = 1, 2, 3, 4, 5, 6, 7
print(a, b, resto)

# %%
*resto, a, b = 1, 2, 3, 4, 5, 6, 7
print(a, b, resto)

# %%
a, *resto, b = 1, 2, 3, 4, 5, 6, 7
print(a, b, resto)


# %%

def soma(a, *args):
    return a + sum(args)

soma(1, 2, 4, 5)

# %%

def soma_quatro(a, b, c, d):
    return a + b + c + d

values = [1, 2, 3, 4]
soma_quatro(*values)

# %%
soma(*values)