import random


# Mutate the imb file
def generate_file(filename):
    with open(filename, 'w') as f:
        f.write(str(random.randint(0, 100)))


# Read a file from the disk
def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()


if __name__ == '__main__':
    # Generate imb files
    for i in range(0, 100):
        generate_file('beings/being' + str(i) + '.imb')

	while 


