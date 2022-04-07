case = 2
if case == 1:
    # right
    from pac1.mod1 import func1
elif case == 2:
    # wrong, no known parent package
    from .pac1.mod1 import func1

print(func1())
