def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    index = 0
    projects = {}
    user_projects = {}
    
    while index < len(data):
        line = data[index]
        if line == '1': 
            valid_users = {user for user, projects in user_projects.items() if len(projects) == 1}
            project_counts = {}
            for project, users in projects.items():
                valid_count = 0
                for user in users:
                    if user in valid_users:
                        valid_count += 1
                project_counts[project] = valid_count
            
            sorted_projects = sorted(project_counts.items(), key=lambda x: (-x[1], x[0]))
            for project, count in sorted_projects:
                print(f"{project} {count}")
            
            projects = {}
            user_projects = {}
            index += 1
            continue
        elif line == '0': 
            break

        if line.isupper():  
            current_project = line
            projects[current_project] = set()
        else: 
            if line not in user_projects:
                user_projects[line] = set()
            user_projects[line].add(current_project)
            projects[current_project].add(line)
        index += 1

if __name__ == "__main__":
    main()