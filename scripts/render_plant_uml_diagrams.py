import os
import subprocess
import shutil

# Get the absolute path of the PlantUML jar file
plant_uml_jar_path = os.path.abspath(os.path.join(os.getcwd(), '..', 'dependencies', 'plantuml-1.2024.7.jar'))

# Define the directory to render from and the output diagrams directory
dir_to_render_from = "../plant_uml_diagrams"
output_diagrams_dir = os.path.join(dir_to_render_from, "rendered_diagrams")

# Ensure the output diagrams directory exists
os.makedirs(output_diagrams_dir, exist_ok=True)

# Clear the contents of the diagrams directory
for filename in os.listdir(output_diagrams_dir):
    file_path = os.path.join(output_diagrams_dir, filename)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)  # Remove files
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)  # Remove directories
    except Exception as e:
        print(f"Failed to delete {file_path}. Reason: {e}")

def validate_plantuml_syntax(file_path):
    try:
        # Run PlantUML in check-only mode to validate syntax
        result = subprocess.run(['java', '-jar', plant_uml_jar_path, '-checkonly', file_path], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Syntax for {file_path} is correct.")
            return True
        else:
            print(f"Syntax error in {file_path}: {result.stderr}")
            return False
    except Exception as e:
        print(f"An error occurred during syntax validation: {e}")
        return False

def render_plantuml(file_path):
    try:
        # Run PlantUML to render the file
        result = subprocess.run(['java', '-jar', plant_uml_jar_path, file_path, '-o', output_diagrams_dir], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Successfully rendered {file_path} to {output_diagrams_dir}")
        else:
            print(f"Error rendering {file_path}: {result.stderr}")
    except Exception as e:
        print(f"An error occurred: {e}")

def process_puml_files(dir_to_render_from):
    # Iterate over all files in the current directory
    for file_name in os.listdir(dir_to_render_from):
        if file_name.endswith('.puml'):
            file_path = os.path.join(dir_to_render_from, file_name)
            
            # Validate and render the PlantUML file
            if validate_plantuml_syntax(file_path):
                render_plantuml(file_path)
            else:
                print(f"Skipping rendering for {file_path} due to syntax errors.")

# Run the function to process all .puml files in the current folder
if __name__ == "__main__":
    process_puml_files(dir_to_render_from)
