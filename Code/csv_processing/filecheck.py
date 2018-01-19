import os

for f in os.listdir('.'):               #Inside the parenthesis should be the file path. '.' is the current directory.
    if(f.endswith(".tiff")):            #Add more if statements as necessary for more file types
        print(f)                        #Do something to the file if the file type matches.
    elif(f.endswith(".csv")):
        print(f)
