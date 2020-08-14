def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    lookup = {}

    ans = None
    for i in range(length):
        lookup[weights[i]] = i
    
    for i in range(length):
        search = (limit - weights[i])
        if search in lookup:
            # it's almost guaranteed to see the smallest index first..
            # biggest = max(lookup[search],i)
            # smallest = min(lookup[search], i)
            ans = (lookup[search],i)
            break


    return ans


print(get_indices_of_item_weights([ 4, 6, 10, 15, 16 ], 5, 21))