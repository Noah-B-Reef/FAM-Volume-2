def smallestPair(L):
    """
        Summary: Find the closest pair of points in a list n-points
        Input: List of n-points from a plane
        Output: The two points that have the smallest Euclidean distance
    """

    # Initialization
    n = len(L)
    i = 0
    smallest_distance = 1e6

    while i < (n-1):
        j = i + 1
        while j < n:
            distance = (L[i][0] - L[j][0])**2 + (L[i][1] - L[j][1])**2
            if distance < smallest_distance:
                smallest_distance = distance
                a = L[i]
                b = L[j]

            j += 1
        i += 1
    return a,b

