#########################################################
# Step 1 Setup and Inputs
#########################################################
# from magic get sorcery
import sys
import json
import re
# Setup our things and buckets
find_my_file_here = "my_notes.txt"  # default file name
write_my_file_here = "my_page.html"  # default file name
my_todos = []
my_content = []
# open the file, and say we are
print(f"- Loading littlething file...")
# magic to summon a file
my_notes = open(find_my_file_here, "rt")
# read the entire file into one place in the program
my_notes_content = my_notes.read()
# clean up after ourselves, close the file
my_notes.close()
#########################################################
# Step 2 Do stuff with inputs
#########################################################
my_notes_content_array = my_notes_content.split(
    '\n')  # make each line an array item
g_current_lineno = 0  # line counter
for line in my_notes_content_array:
    g_current_lineno = g_current_lineno + 1
    if "todo" in line.lower():  # check lowercased line for todo
        my_todos.append(line)  # add line to todos
        print(f"{line} (Line #: {g_current_lineno})")
    else:
        my_content.append(line)  # add line to general content
        print(f"Read Line {g_current_lineno}")
#########################################################


#########################################################
# STEP 3 Let's make it more human
# get HTML template (note, you're using deep sorcery here)
# the template you're loading is made of a lot of other
# incantations we wont cover here. But you can learn. I promise.
#
# same magic as before, read in the file
print(f"- Loading littlething template file...")
# go up a folder, then into static, then find that htmle
in_file = open("../static/littlething_template.html", "rt")
# read it in
htmltemplate = in_file.read()
# close it up
in_file.close()
# attach our work to the magic (find and replacing text)
htmltemplate = htmltemplate.replace("[MY_TODOS]", '<br>'.join(my_todos))
htmltemplate = htmltemplate.replace("[MY_CONTENT]", '<br>'.join(my_content))
#########################################################


#########################################################
# From Step 1 - will a file into existence, write onto it our stuff
print(f"- Write littlething output file...")
with open(write_my_file_here, 'w') as the_file:
    the_file.write(htmltemplate)
print(f"silent")
