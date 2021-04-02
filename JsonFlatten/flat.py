import json
import sys


def flatten_json(b):
    ans = {}  # storing the flattened obj

    def flatten(i, na=''):  # pass in the first element of the JSON and a space --helper function

        if type(i) is dict:  # dict values stored as key: pairs
            for a in i:  # while there is 'children'
                flatten(i[a],
                        na + a + '.')  # recursively call the function to flatten any subsequent pairs in the object
                # add the dot each time so if there was more then 2 nested objects it
                # would keep adding
        else:
            ans[na[:-1]] = i  # if there is no more 'children' print the value

    flatten(b)
    return ans


inputfile = str(sys.argv[1])
outputfile = str(sys.argv[2])
f = open(inputfile,)
# returns JSON object as a dictionary
data = json.load(f)
with open(outputfile, "w") as outfile:
    # Iterating through the json list
    # for i in data:
    outfile.write(json.dumps(flatten_json(data)))

# Closing file
f.close()
