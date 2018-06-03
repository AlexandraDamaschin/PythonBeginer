# Read from a file
# specify path and r-read only(by default)
f = open('hello_file', 'r')
file_data = f.read()
f.close()

print(file_data)