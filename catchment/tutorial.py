#def greet(name: str) -> None:
#    """Say hello to everyone"""
#    print("Hi " + name)
#
#greet("World")
#
#def greetAll(names: list[str]) -> None:
#    for name in names:
#        print("Hello " + name)
#
#greetAll(["Naomi","Chris","Anna","Terry"])

#x: dict[str, float] = {"field1": 2.0, "field2": 3.0}

def myDiv(x : float, y : float) -> (float | None):
    if y != 0: 
        return x / y
    else: 
        return None

print(myDiv(44.0,26.0))

myDict: dict[str, float | str] = {"temp" : 233, "units" : "celcius"}

def myAbs(x : float) -> float:
    """Take the absolute of the floating-point input"""
    if x < 0:
        return(-x)
    else:
        return(x)
    
print(myAbs(2.3))
print(myAbs(-11.2))

#reveal_type(x)

from typing import TYPE_CHECKING