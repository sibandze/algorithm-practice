import os

# List of problem numbers
problem_numbers = [1,3,4,11,22,50]
# Maximum number of digits for padding zeros
max_digits = 4

for problem_number in problem_numbers:
    # Create folder name with leading zeros
    folder_name = f"problem{str(problem_number)}"

    # Create folder
    os.makedirs(folder_name, exist_ok=True)

    # Create README.md file
    with open(os.path.join(folder_name, "README.md"), "w") as f:
        f.write("TODO:")                 

    # Create solution.py file
    with open(os.path.join(folder_name, "solution.py"), "w") as f:
        f.write("# Solution for problem {}\n".format(problem_number))

    print(f"Folder created: {folder_name}")
