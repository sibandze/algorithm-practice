import os

def get_problem_status(root_dir):
    completed_problems = []
    incomplete_problems = []
    
    for folder in os.listdir(root_dir):
        if os.path.isdir(os.path.join(root_dir, folder)):
            problem_number = folder.replace('problem', '')
            try:
                problem_number = int(problem_number)
            except ValueError:
                continue  # Skip folders that don't match the 'problemXXXX' pattern
                
            folder_path = os.path.join(root_dir, folder)
            files = os.listdir(folder_path)
            problem_files = [file for file in files if file.endswith('.py') or file.endswith('.java') or file.endswith('.cpp')]
            
            if not problem_files:
                continue  # Skip folders with no solution files
                
            all_solutions_complete = True
            for file in problem_files:
                file_path = os.path.join(folder_path, file)
                with open(file_path, 'r') as f:
                    lines = f.readlines()
                    if len(lines) < 3:
                        all_solutions_complete = False
                        break
            
            if all_solutions_complete:
                completed_problems.append(problem_number)
            else:
                incomplete_problems.append(problem_number)
    
    return completed_problems, incomplete_problems

def create_new_folders(problem_numbers):
    # Maximum number of digits for padding zeros
    max_digits = 4

    for problem_number in problem_numbers:
        # Create folder name with leading zeros
        folder_name = f"problem{str(problem_number).zfill(max_digits)}"
        
        try:
            # Create folder
            os.makedirs(folder_name)

            # Create README.md file
            with open(os.path.join(folder_name, "README.md"), "w") as f:
                f.write("TODO:")

            # Create solution.py file
            with open(os.path.join(folder_name, "solution.py"), "w") as f:
                f.write("# Solution for problem {}\n".format(problem_number))

            print(f"Folder created: {folder_name}")
        except FileExistsError:
            print(f"Folder {folder_name} already exists")

def main():
    root_dir = '.'  # Change this to the directory containing your problem folders
    completed, incomplete = get_problem_status(root_dir)
    
    print(f"Completed Problems: {len(completed)}")
    print(sorted(completed))
    print(f"\nIncomplete Problems: {len(incomplete)}")
    print(sorted(incomplete))
    print()
    problems = [3625, 2211, 3432, 3623, 2141, 1590, 3512, 2435, 1015, 1018, 1262, 1930, 1437, 1513, 2169, 3461]
    create_new_folders(problems)
if __name__ == "__main__":
    main()
