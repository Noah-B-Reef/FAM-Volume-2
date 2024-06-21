def subtractTwo(a,b):
    '''
    Summary: Takes in two single digit lists representing multi-digit integers, and returns the resulting difference of a-b
    Input: a,b - two single digit lists representing integer values
    Output: A list of single digits representing the difference of a-b
    '''

    # Prepend zeros to the shorter list to align with the longer list
    delta = abs(len(a)-len(b))
    if len(a) >= len(b):
        b = delta * [0] + b
    else:
        a = delta * [0] + a

    # set intial values
    i = len(a) - 1
 
    
    # substract each pair from right to left
    while i >= 0:
        a[i] = a[i] - b[i]
        i -= 1
    return a

print(subtractTwo([3,0,0], [5,0,0]))