#Read

with open("file.txt","r") as f:
    #first = f.readline()
    #second = f.readline()
    wholething = f.read()
    print(wholething)

#Second Way

with open("file.txt","r") as f1:
    for line in f1:
        print(line)
#Write
with open("file2.txt","w") as f2:
    f2.write("Hello, World!\n")
    f2.write("This is a new line\n")
    f2.write("This another new line\n")


#Append
with open("file2.txt","a") as f3:
    f3.write("Yet another line\n")
    f3.write("One last line\n")
