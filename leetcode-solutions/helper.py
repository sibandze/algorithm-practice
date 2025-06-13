import os

# List of problem numbers
with open('problems.txt', 'r') as file:
    problem_numbers = list(set(map(int, file.read().split())))

# Maximum number of digits for padding zeros
max_digits = 4

for problem_number in problem_numbers:
    # Create folder name with leading zeros
    folder_name = f"problem{str(problem_number).zfill(max_digits)}"

    # Create folder
    os.makedirs(folder_name, exist_ok=True)

    # Create README.md file
    with open(os.path.join(folder_name, "README.md"), "w") as f:
        f.write("TODO:")                 

                             
    with open(os.path.join(folder_name, "# Problem {problem_number}\n"))

    # Create solution.py file
    with open(os.path.join(folder_name, "solution.py"), "w") as f:
        f.write("# Solution for problem {}\n".format(problem_number))

    print(f"Folder created: {folder_name}")
