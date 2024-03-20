def myDiv(x : float, y : float) -> (float | None):
    if y != 0: 
        return x / y
    else: 
        return None

print(myDiv(44.0,26.0))