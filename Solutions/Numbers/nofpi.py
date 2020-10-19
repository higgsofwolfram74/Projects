try:
    # import version included with old SymPy
    from sympy.mpmath import mp
except ImportError:
    # import newer version
    from mpmath import mp

print("how many digits of pi do you want? I can give you that many digits up to 1000")

#with imported library we can set precision of pi with mp.dps
mp.dps = input("- ")

print(mp.pi)
