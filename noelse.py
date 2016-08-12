"""this proves that you don't have to use else in a function to improve code
readability - just exit the code but it's perfectly fine to use else in loops
mark kevin """


def with_else(x):
    if x:
        return True
    else:
        return False


def without_else(x):
    if x:
        return True
    return False

## or if x:
##      return True
