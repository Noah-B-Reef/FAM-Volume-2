def minElement(L):
    """
        Summary: Find the index of the minimum element in a list L
        Input: List of integers L
        Output: Index of the the minimum value in L
    """

    # Initialization
    n = len(L)
    min_index = 0 # keep track of the min element index
    min_element = L[min_index] # keep track of min element seen so far
    i = 1

    while i < n:
        if L[i] < min_element:
            min_index = i
            min_element = L[i]

        i += 1

    return min_index


