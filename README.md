# Informatiklabor Exercise Processing Scripts

## Description
This repository contains a series of Python scripts designed to automate the processing of exercise submissions for an Informatiklabor course. The scripts handle various tasks including extracting submissions, processing and organizing data, generating previews, and creating a webpage to display these submissions.

## Scripts Overview and Assumptions

### Script 1: `script_1_extract_exercises_zip.py`
**Assumptions:**
- A zip file named `Uebung 10.zip` exists in the `data` folder.
- Python environment is set up with necessary permissions to read from and write to the file system.

Extracts submissions from a zip file and organizes them in a specified directory.

### Script 2: `script_2_extract.py`
**Assumptions:**
- The `1_Original` folder exists and contains folders with or without zip files.
- The `2_Extracted` folder may or may not exist. If it does, the script will ask for permission to overwrite.

Processes extracted files, handling additional zip files within submissions and reorganizing content.

### Script 3: `script_3_handle_submissions_with_accept.py`
**Assumptions:**
- The `2_Extracted` folder exists with subfolders, each potentially containing an `accept.txt` file.
- The `3_Accepted` folder may or may not exist. If it does, the script will ask for permission to overwrite.

Filters and prepares submissions for display, copying only those with an 'accept.txt' file and standardizing file names.

### Script 4: `script_4_screenshot_taker.py`
**Assumptions:**
- The `3_Accepted` folder exists with subfolders, each containing an `index.html` file.
- Selenium WebDriver and necessary browser drivers are correctly installed and configured.

Automates the taking of screenshots for each submission using Selenium, saving them for preview purposes.

### Script 5: `script_5_html_preview_creator.py`
**Assumptions:**
- The `3_Accepted` folder exists with the necessary subfolders, each containing `index.html` and `preview.png`.
- The system can handle file encoding (UTF-8) correctly.

Generates an HTML page to showcase the submissions, each with a screenshot and link to the submission.

### Script 6: `script_6_submissions_checker.py`
**Assumptions:**
- The `2_Extracted` folder exists and contains multiple subfolders, each with an HTML file.
- Python environment is set up with BeautifulSoup library installed for HTML parsing.

Analyzes HTML files in each subfolder for specific requirements such as headings, images, text blocks, lists, hyperlinks, tables, and CSS usage. Reports the findings for each submission.

## Installation

To run these scripts, you need to have Python installed on your system along with several dependencies. To install these dependencies, navigate to the repository's root directory and run:

```bash
pip install -r requirements.txt
```

## Usage

Each script can be run individually as per the requirements of the exercise processing stage. Ensure that the `data` directory is structured as expected by each script.

## License

[GNU General Public License v3.0](LICENSE)
