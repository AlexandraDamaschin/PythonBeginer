# Read from a file
# specify path and r-read only(by default)
f = open('hello_file', 'r')
file_data = f.read()
# always close file because even not we will have Too Many Open Files
f.close()

print(file_data)

# Write to a file
# w- write, will delete everything from an existing file
# if it`s a new file, he will create it
f = open('hello_file2.txt', 'w')
f.write("Hello there!")
f.close()

# Writing to an existing file
# without deleting what it`s inside
f = open('hello_file2.txt', 'a')
f.write("Hello there from append!")
f.close()

# With = open and close a file
with open('hello_file', 'r') as f:
    # read is executing just in this block
    file_data = f.read()
    print(file_data)
# here the file is already closed

# Read a certain amount from the file
with open("camelot.txt") as song:
    print(song.read(2))
    print(song.read(8))
    print(song.read())

# .strip()= remove newline character attached
camelot_lines = []
with open("camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)


# Flying circus cast example
def create_cast_list(filename):
    cast_list = []
    # use with to open the file filename
    with open(filename) as f:
        # use the for loop syntax to process each line
        for line in f:
            # and add the actor name to cast_list
            name = line.split(",")[0]
            cast_list.append(name)

    return cast_list


# defining the name of the file
cast_list = create_cast_list('flying_circus_cast')
for actor in cast_list:
    print(actor)
