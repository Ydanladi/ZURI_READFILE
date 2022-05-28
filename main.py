# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

filename = "filename.txt"
#assigning filename to a text variable in same project folder
def read_file_content(filename):
    #opening file to read contents saved in filename.txt
        f=open(filename,"r") 
    #reading contents
        var2 =f.read()
        #closing my file
        f.close() 
        return var2 
#the return values of the function is save in var3
var3=read_file_content(filename)
print(var3)
PROBLEM.2
def count_words():
    #text = read_file_content("./story.txt")
    file = open("story.txt", "r")
    content = file.read().split()
    #create dictionary to assign each       
    keySum={} 
    freq=0
    for i in (content):
        if i not in keySum:
            freq=1
            keySum[i]=freq
        elif i in keySum:
            freq+=1
            keySum[i]=freq 
    print(keySum)
    file.close()
    #return {"as": 10, "would": 20}
count_words()
     