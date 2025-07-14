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

def main():
    root_dir = '.'  # Change this to the directory containing your problem folders
    completed, incomplete = get_problem_status(root_dir)
    
    print(f"Completed Problems: {len(completed)}")
    print(sorted(completed))
    print(f"\nIncomplete Problems: {len(incomplete)}")
    print(sorted(incomplete))

if __name__ == "__main__":
    main()
