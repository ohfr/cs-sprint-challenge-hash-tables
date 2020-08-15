def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    # lookup = {}

    # result = []

    # for item in a:
    #     lookup[item] = 0

    # for key in lookup.keys():
    #     if key >= 1:
    #         search = key * -1

    #         if search in lookup:
    #             result.append(key)
    
    # return result


    # can also separate postivies and negatives for no checking for positives
    positives = {}
    negatives = {}

    result = []

    for item in a:
        if item >= 1:
            positives[item] = 0
        else:
            negatives[item] = 0

    for key in positives.keys():
        if key * -1 in negatives:
            result.append(key)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
