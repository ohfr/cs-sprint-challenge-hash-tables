# Your code here

import re

def finder(files, queries):
    """
    YOUR CODE HERE
    """

    # this passes small test, but way too slow for large test

    # this relies on files and queries being same length

    # i = 0
    # for key in lookup.keys():
    #     if re.search(r'{0}'.format(key), files[i]):
    #         result.append(files[i])
    #     i+=1

    # this is way slower but checks thoroughly

    # for file in files:
    #     for key in lookup.keys():
    #         if re.search(r'{0}'.format(key), file):
    #             result.append(file)
    

    lookup = {}
    result = []

    fileLookup = {}

    for item in queries:
        lookup[item] = 0

    for file in files:
        # finding the last index of '/'
        ind = file.rfind('/')
        search = file[ind+1:]
        if search in fileLookup:
            fileLookup[search].append(file)
        else:
            fileLookup[search] = [file]

    for key in lookup.keys():
        if key in fileLookup:
            for item in fileLookup[key]:
                    result.append(item)

    return result






if __name__ == "__main__":
    files = ['/dir256/dirb256/file256',
            '/dir256/file256', '/dir3490/dirb3490/file3490',
            '/dir3490/file3490', '/dir8192/dirb8192/file8192',
            '/dir8192/file8192']
    queries = [
        "file256","file3490", "file8192"
    ]
    print(finder(files, queries))
    
    st = 'random'
