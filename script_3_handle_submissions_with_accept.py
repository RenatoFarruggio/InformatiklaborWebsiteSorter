import os
import shutil

def copy_folders_with_accept_file(base_data_path, source_subfolder, destination_subfolder):
    """
    Copies all folders that contain 'accept.txt' from the source subfolder within the base data folder 
    to a new destination subfolder, asks for user confirmation if the destination subfolder already exists.
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

    # Copy only folders that contain 'accept.txt'
    for folder_name in os.listdir(source_path):
        source_folder = os.path.join(source_path, folder_name)
        accept_file_path = os.path.join(source_folder, 'accept.txt')
        destination_folder = os.path.join(destination_path, folder_name)

        if os.path.isdir(source_folder) and os.path.exists(accept_file_path):
            shutil.copytree(source_folder, destination_folder)

    print("Folders with 'accept.txt' copied to destination successfully.")

# Define the base 'data' folder path
base_data_path = 'data'

# Define the source and destination subfolders
source_subfolder = '2_Extracted'
destination_subfolder = '3_Accepted'

# Usage
copy_folders_with_accept_file(base_data_path, source_subfolder, destination_subfolder)
