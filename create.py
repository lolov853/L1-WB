import os

# Define the directory where you want to create the files
directory = '.'  # Current directory, change this if you want a different directory

# Loop to create files from l1_1.go to l1_26.go
for i in range(1, 27):
    filename = f'l1_{i}.go'
    filepath = os.path.join(directory, filename)

    # Create the file
    with open(filepath, 'w') as file:
        pass

    print(f'Created file: {filepath}')

print('All files created successfully.')
