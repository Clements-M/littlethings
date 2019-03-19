#########################################################
# STEP 0 - The boring stuff
# from magic get sorcery
import sys
import json
import re
# Setup our things and buckets
# when did you come from, where did you go...
find_my_file_here = "my_notes.txt"  # default file name
write_my_file_here = "my_page.html"  # default file name
my_todos = []
my_content = []
#########################################################

#########################################################
# STEP 1.0
# Read a file so we can use it
print(f"- Loading littlething file...")  # open the file, and say we are
my_notes = open(find_my_file_here, "rt")  # magic to summon a file
# read the entire file into one place in the program
my_notes_content = my_notes.read()
my_notes.close()  # clean up after ourselves, close the file
#########################################################

# TEMPORARY CODE. Just to check our progress
# give it a new name because why not, then let's write it out
htmltemplate = my_notes_content

#########################################################
# STEP 1.1
# will a file into existence, write onto it our stuff
print(f"- Write littlething output file...")
with open(write_my_file_here, 'w') as the_file:
    the_file.write(htmltemplate)
print(f"silent")
