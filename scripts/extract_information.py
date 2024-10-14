import os
import json

def extract_descriptions_from_json(folder_path):
    descriptions = []

    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            file_path = os.path.join(folder_path, filename)
            
            # Open and load the JSON file
            with open(file_path, 'r') as file:
                try:
                    data = json.load(file)
                    
                    # Get the dataset ID
                    dataset_id = data.get("dataset", {}).get("id", "Unknown Dataset")

                    # Extract the "dataset_description" field
                    dataset_description = data.get("dataset", {}).get("dataset_description", {})
                    if dataset_description:
                        descriptions.append({"dataset_id": dataset_id, "description": dataset_description})
                except json.JSONDecodeError:
                    print(f"Error decoding JSON from file: {file_path}")
    
    return descriptions

# Folder path where your JSON files are stored
folder_path = '.'

# Extract descriptions
all_descriptions = extract_descriptions_from_json(folder_path)

# Print the extracted dataset descriptions with dataset origin
for desc in all_descriptions:
    dataset_id = desc['dataset_id']
    description = desc['description']
    simplified = description.get('simplified', 'No simplified description')
    detailed = description.get('detailed', 'No detailed description')
    print(f"Dataset ID: {dataset_id}\nSimplified Description: {simplified}\nDetailed Description: {detailed}\n")
