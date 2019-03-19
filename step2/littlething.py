#########################################################
# THIS IS ALL JUST STEP 1
# from magic get sorcery
import sys
import json
import re
# setup vars
find_my_file_here = "my_notes.txt"  # default file name
write_my_file_here = "my_page.html"  # default file name
my_todos = []
my_content = []
# open up our readin files
print(f"- Loading littlething file...")  # open the file, and say we are
my_notes = open(find_my_file_here, "rt")  # magic to summon a file
# read the entire file into one place in the program
my_notes_content = my_notes.read()
my_notes.close()  # clean up after ourselves, close the file
# That's step one done
#########################################################


#########################################################
# STEP 2 - doing the hard work
# scan the input line for littlething content
# make each line an array item
my_notes_content_array = my_notes_content.split('\n')
g_current_lineno = 0  # line counter
for line in my_notes_content_array:
    g_current_lineno = g_current_lineno + 1
    if "todo" in line.lower():  # check lowercased line for todo
        my_todos.append(line)  # add line to todos
        print(f"{line} (Line #: {g_current_lineno})")
    else:
        my_content.append(line)  # add line to general content
        print(f"Read Line {g_current_lineno}")
# That was step 2
#########################################################

# TEMPORARY CODE. Just to check our progress
# give it a new name because why not, then let's write it out
htmltemplate = '<br>'.join(my_todos) + '<br>' + '<br>'.join(my_content)


#########################################################
# Back to step 1, just writing it out
print(f"- Write littlething output file...")
with open(write_my_file_here, 'w') as the_file:
    the_file.write(htmltemplate)
print(f"silent")
