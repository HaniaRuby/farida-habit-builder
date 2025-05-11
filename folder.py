import os

def print_project_structure(path, prefix=""):
    """
    Recursively prints the structure of a project directory in a tree-like format.
    
    :param path: The root directory to start scanning from.
    :param prefix: Used internally for indentation during recursion.
    """
    # Get the list of items (files and directories) in the current path
    items = os.listdir(path)
    items.sort()  # Sort items alphabetically
    
    for index, item in enumerate(items):
        # Full path of the current item
        full_path = os.path.join(path, item)
        
        # Check if this is the last item in the current directory
        is_last = index == len(items) - 1
        
        # Print the current item with appropriate indentation
        if os.path.isdir(full_path):
            print(f"{prefix}├── {item}/")
            # Update the prefix for subdirectories
            new_prefix = prefix + "│   " if not is_last else prefix + "    "
            print_project_structure(full_path, new_prefix)
        else:
            # Print files
            print(f"{prefix}└── {item}" if is_last else f"{prefix}├── {item}")

# Specify the root directory of your project
project_root = "E:/HTML/Another One/github/farida-habit-builder"  # Replace with the actual path to your project

# Start printing the project structure
print(project_root + "/")
print_project_structure(project_root)