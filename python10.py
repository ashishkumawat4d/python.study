#                File Handling



#        What are files
        
        
#        files any name with an extension is
#        file9
       
       
#        Now that extension can be .py , .txt , .mp3 etc. and when we
#        want to handle these files we will use file handling.
        
        
#        File handling
        
#        File handling means Creating, Reading, Updating,
#        Deleting(CRUD) operations that we can perform in files.
        
        
        
#        We have to use open() function to open a file in python.

#        EXAMPLE



p = open('python09.py')


# print(p.read())


#        Now there are multiple modes to open the file.



#        Mode           |          Description
        
#        'r'            |      Read (default) – file must exist.                   
        
#        'w'            |      Write – creates file or overwrites.
        
#        'a'            |      Append – adds to end of file.
        
#        'x'            |      Create – creates a new file,fails if it exists            
                   






                
#        EXAMPLES -


#    1.'r'




file = open("python09.py", 'r')
print(file.read())





#    2.'w' --> creates file or overwrites





w = open("data.txt",'w')

w.write("hii this is ashish i am writing insude this filr")

w.close()



#   3. 'a'   
# Purpose: Adds data at the end of the file.



file = open("data.txt", "a")
file.write("Welcome to Python")
file.close()



#  4. 'x'  

# Purpose: Creates a new file.


file = open("newfile.txt", "x")
file.write("New file created.")
file.close()



