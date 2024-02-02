  x=input("Would you like to create one?Y or N:")
    if x.lower()=="y":
         # Create a new file
        f = open("demofile.txt","x")#f = open("demofile.txt", "w")
        #f.close
        print(f.write("Put content here!"))
        #open and read the file after the overwriting:
        f = open("demofile.txt", "r")
        print(f.read())
        f.close()
    else:
        print("Goodbye.")
