import os
import shutil
from zipfile import ZipFile

def extract_files_and_process_zips(base_data_path, source_subfolder, destination_subfolder):
    """
    Moves all files from the source folder within the base data folder to a new destination subfolder,
    extracts zip files within each subfolder, and performs additional cleanup and reorganization steps.
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
    for item_name in os.listdir(source_path):
        source_item = os.path.join(source_path, item_name)
        destination_item = os.path.join(destination_path, item_name)

        if os.path.isfile(source_item):
            shutil.copy(source_item, destination_item)
        elif os.path.isdir(source_item):
            shutil.copytree(source_item, destination_item)


    # Iterate through each folder in the base path
    for folder in os.listdir(destination_path):
        folder_path = os.path.join(destination_path, folder)

        # If there is no zip file, but only a html file, then there is nothing to unzip in this folder
        if len(os.listdir(folder_path)) == 1 and os.listdir(folder_path)[0].endswith(".html"):
            print(f"Folder {folder} only contains one html file and nothing else.")
            continue
            
        # Check that there is only one file in the folder
        if len(os.listdir(folder_path)) != 1:
            print(f"Folder '{folder}' does not contain exactly one file.")
            continue
            

        # Find the zip file in the folder
        zip_files = [f for f in os.listdir(folder_path) if f.endswith('.zip')]

        # Check if there is exactly one zip file
        if len(zip_files) != 1:
            print(f"Folder '{folder}' does not contain exactly one zip file.")
            continue



        # Extract the zip file
        zip_file_path = os.path.join(folder_path, zip_files[0])
        with ZipFile(zip_file_path, 'r') as zip_ref:
            extract_to = os.path.join(destination_path, folder)
            os.makedirs(extract_to, exist_ok=True)
            zip_ref.extractall(extract_to)
            
            # Delete "__MACOSX" folder if it exists
            macosx_path = os.path.join(extract_to, '__MACOSX')
            if os.path.exists(macosx_path):
                shutil.rmtree(macosx_path)

            # Check and reorganize the contents
            if not any(file.endswith('.html') for file in os.listdir(extract_to)):
                if len(os.listdir(extract_to)) == 2:
                    single_name = os.listdir(extract_to)[0]
                    single_path = os.path.join(extract_to, single_name)

                    if os.path.isdir(single_path):
                        for item in os.listdir(single_path):
                            shutil.move(os.path.join(single_path, item), extract_to)
                        os.rmdir(single_path)

        os.remove(zip_file_path)


    print("Extraction and cleanup complete.")
    
    
# Define the base 'data' folder path
base_data_path = 'data'

# Define the source and destination subfolders
source_subfolder = '1_Original'
destination_subfolder = '2_Extracted'

# Usage
extract_files_and_process_zips(base_data_path, source_subfolder, destination_subfolder)
