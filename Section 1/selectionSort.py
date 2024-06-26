
from minElement import *

def selectionSort(L):
    """
        Summary: Sort a list L using the Selection Sort Algorithm
        Input: A list L
        Output: A sorted version of the list L
    """
    # Initialization
    n = len(L)
    i = 0

    while i < (n-1):
        temp = L[i]
        min_index = i + minElement(L[i:])
        L[i] = L[min_index]
        L[min_index] = temp
        i += 1
    return L



