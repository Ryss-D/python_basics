#from python 3.5 we have now a way to make type hingitn

from typing import List

def list_avg(sequence: list) -> float:
    return sum(sequence)/len(sequence)

#iff we are talking about of a return type method inside a class ieg
##Perro class and we want to say that the returning is of this same typo
## we should use method(arg) -> "Perro"