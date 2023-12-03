import os
import shutil

def copy_rename_folders_and_html(base_data_path, source_subfolder, destination_subfolder):
    """
    Copies folders containing 'accept.txt' from the source subfolder within the base data folder 
    to a new destination subfolder, renames the folders, and renames the .html file in each folder to 'index.html'.
    Prints the folder name if there isn't exactly one .html file.
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

    # Copy and rename folders, and rename .html file if it exists
    for folder_name in os.listdir(source_path):
        source_folder = os.path.join(source_path, folder_name)
        accept_file_path = os.path.join(source_folder, 'accept.txt')

        if os.path.isdir(source_folder) and os.path.exists(accept_file_path):
            # Split the folder name, remove last two elements, and rejoin
            new_folder_name = '_'.join(folder_name.split('_')[:-2])
            destination_folder = os.path.join(destination_path, new_folder_name)

            shutil.copytree(source_folder, destination_folder)

            # Rename .html file to 'index.html' if exists
            html_files = [f for f in os.listdir(destination_folder) if f.endswith('.html')]
            if len(html_files) == 1:
                os.rename(os.path.join(destination_folder, html_files[0]), 
                          os.path.join(destination_folder, 'index.html'))
            elif len(html_files) != 1:
                print(f"Folder '{new_folder_name}' does not contain exactly one .html file.")

    print("Folders with 'accept.txt' copied, renamed, and .html file processed successfully.")

# Define the base 'data' folder path
base_data_path = 'data'

# Define the source and destination subfolders
source_subfolder = '2_Extracted'
destination_subfolder = '3_Accepted'

# Usage
copy_rename_folders_and_html(base_data_path, source_subfolder, destination_subfolder)
