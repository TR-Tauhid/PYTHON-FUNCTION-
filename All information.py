print(r"input of any functions \n will not work")
print("This is the line \n breaker")

import keyword

print(keyword.kwlist)    # Shows the keyword libreary
print(keyword.iskeyword("And"))   # Checks if And is a keyword


def add(a, b):
    a = 10
    

    """Return the sum of given arguments."""
    return a + b

print(add(10,200))