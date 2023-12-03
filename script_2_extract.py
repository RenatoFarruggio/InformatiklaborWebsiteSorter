import os
import shutil

def extract_files_to_folder(base_data_path, source_subfolder, destination_subfolder):
    """
    Moves all files from the source folder within the base data folder to a new destination subfolder.
    Asks for user confirmation if the destination subfolder already exists.
    """

    # Define source and destination paths using the base data path
    source_path = os.path.join(base_data_path, source_subfolder)
    destination_path = os.path.join(base_data_path, destination_subfolder)

    def user_confirmation(prompt):
        """Asks user for confirmation with a y/n prompt."""
        while True:
            choice = input(prompt).lower()
            if choice in ['y', 'n']:
                return choice == 'y'
            print("Please respond with 'y' or 'n'.")

    # Check if destination folder exists and get user confirmation to replace
    if os.path.exists(destination_path):
        if user_confirmation(f"The folder '{destination_path}' already exists. Replace it? (y/n): "):
            shutil.rmtree(destination_path)  # Remove the existing directory
            print(f"Deleted the existing '{destination_path}' folder.")
        else:
            print("Operation aborted.")
            return

    # Create the destination folder
    os.makedirs(destination_path, exist_ok=True)

    # Copy all files from source to destination
    for file_name in os.listdir(source_path):
        source_file = os.path.join(source_path, file_name)
        destination_file = os.path.join(destination_path, file_name)
        shutil.copytree(source_file, destination_file)
        

    print("Files moved to destination folder successfully.")

# Define the base 'data' folder path
base_data_path = 'data'

# Define the source and destination subfolders
source_subfolder = 'Original'
destination_subfolder = 'Extracted'

# Usage
extract_files_to_folder(base_data_path, source_subfolder, destination_subfolder)
