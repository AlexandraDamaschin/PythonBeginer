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
