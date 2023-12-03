import os
import shutil
import zipfile

# Base path for the 'data' folder
base_data_path = 'data'

# Paths for the zip file and the directory to extract to, relative to the base data path
zip_file_path = os.path.join(base_data_path, 'Uebung 10.zip')
extract_to_path = os.path.join(base_data_path, 'Original')

def extract_zip(zip_path, extract_to):
    """Extracts the given zip file into the specified directory."""
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def user_confirmation(prompt):
    """Asks user for confirmation with a y/n prompt."""
    while True:
        choice = input(prompt).lower()
        if choice in ['y', 'n']:
            return choice == 'y'
        print("Please respond with 'y' or 'n'.")

def main():
    # Check if the target directory exists
    if os.path.exists(extract_to_path):
        # Ask user for confirmation to replace
        if user_confirmation(f"The folder '{extract_to_path}' already exists. Replace it? (y/n): "):
            shutil.rmtree(extract_to_path)  # Remove the existing directory
            print(f"Deleted the existing '{extract_to_path}' folder.")
        else:
            print("Extraction aborted.")
            return

    # Create the directory and extract the zip file
    os.makedirs(extract_to_path, exist_ok=True)
    extract_zip(zip_file_path, extract_to_path)
    print(f"Extracted '{zip_file_path}' into '{extract_to_path}'.")

if __name__ == "__main__":
    main()
