# FlattenMDB-Niamh-Murtagh
Flatten JSON objects challenge 

I interpretted the assignment to read a JSON object from an input file and output a flattened version to an output file.
I wrote the program in python.
I used the JSON library to parse the objects. I accepted two arguments as input from the command line the input file containing the origional JSON object and the output file name. I used a recurisive function to loop through the object, check if it has children and flatten them. This function used a helper function and returned the flattened object. This is then written to the output file. 
I have included three input files as test cases. I did not have access to linux enviroment so I used windows command prompt to test this. I inlcuded all of the tests in a batch file that can be run from the windows command prompt. I have also submitted the output files from these test cases.
I had to research about JSON objects as I had never used them before, but after this it took me about 2 hours to complete.
