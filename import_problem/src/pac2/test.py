case = 2
if case == 1:
    # right: absolut path
    import sys
    sys.path.append('F:\python test\import_problem\src')
    from pac1.mod1 import func1 # ignore this warning 
elif case == 2:
    # wrong: relativ path
    from ..pac1.mod1 import func1
print(func1())