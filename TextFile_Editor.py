
# The files i need to work with have numbers as names
# it make the process easy 
fileIndex = 1 


# We will use that number in the string Nlink
Number = 1


while fileIndex < 6 :

    # Formated strings cant be used directly on list
    NLink = f'    "Link" : "https://Link_placeHolder/{Number}.jpg",\n'
    
    # Link stores the data, and we can use this on our list
    Link = NLink


    # Openning your file for reading to store the lines
    with open(f"C:\\Cteste\\Original\\{fileIndex}.json", "r+") as f:
        
        # Create an list with all string information of the file
        lines = f.readlines()


        # Open a new file for writing 
        with open(f"C:\\Cteste\\New\\{fileIndex}.json", "w")as f2 :

            
            # Insert the link at especifc position in the list
            # in my case  index 2
            lines.insert(2, Link)


            # Write everything on the file, them close the files
            for i in lines :
                f2.write(i)


    # add to index
    fileIndex += 1

    # add to number
    Number += 1