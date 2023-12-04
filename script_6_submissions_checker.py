import os
from bs4 import BeautifulSoup

def analyze_html(file_path, folder_path):
    """Analyzes the HTML file for specified requirements and CSS.

    Args:
    file_path (str): The path to the HTML file.
    folder_path (str): The path to the folder containing the HTML file.

    Returns:
    dict: A dictionary with the status of each requirement and CSS checks.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Requirements checks
    requirements = {
        "Headings": len(soup.find_all(['h1', 'h2'])) >= 2,
        "Images": len(soup.find_all('img')) >= 1,
        "Text Blocks": len(soup.find_all(['p', 'div'])) >= 2,
        "List": len(soup.find_all(['ol', 'ul'])) >= 1,
        "Hyperlink": len(soup.find_all('a', href=True)) >= 1,
        "Table": len(soup.find_all('table')) >= 1
    }

    # CSS checks
    css_checks = {
        "Embedded CSS": bool(soup.find('style')),
        "External CSS": False,
        "CSS Link Valid": True
    }

    # Check for external CSS
    for link in soup.find_all('link', {'rel': 'stylesheet'}):
        css_href = link.get('href')
        if css_href:
            css_path = os.path.join(folder_path, css_href)
            css_checks["External CSS"] = True
            css_checks["CSS Link Valid"] = css_checks["CSS Link Valid"] and os.path.exists(css_path)

    return {**requirements, **css_checks}

def choose_html_file(folder_path, html_files):
    """Asks the user to choose an HTML file from the list.

    Args:
    folder_path (str): The path to the folder.
    html_files (list): List of HTML files in the folder.

    Returns:
    str: The path to the chosen HTML file.
    """
    print(f"Multiple HTML files found in {folder_path}. Please choose one:")
    for i, file in enumerate(html_files):
        print(f"{i + 1}: {file}")

    while True:
        choice = input("Enter the number of the file you want to use: ")
        if choice.isdigit() and 1 <= int(choice) <= len(html_files):
            return os.path.join(folder_path, html_files[int(choice) - 1])
        else:
            print("Invalid choice. Please try again.")

def find_html_file(folder_path):
    """Finds the appropriate HTML file within the folder.

    Args:
    folder_path (str): The path to the folder containing HTML files.

    Returns:
    str: The path to the chosen HTML file, or None if no HTML file is found.
    """
    html_files = [file for file in os.listdir(folder_path) if file.endswith('.html')]
    
    if len(html_files) == 1:
        return os.path.join(folder_path, html_files[0])
    elif len(html_files) > 1:
        return choose_html_file(folder_path, html_files)
    else:
        return None

def print_results(folder, results, col_widths):
    """Prints the results in a table format, more neatly.

    Args:
    folder (str): The folder name.
    results (dict): The analysis results for the HTML file.
    col_widths (list): List of column widths.
    """
    folder_display = (folder[:19] + '..') if len(folder) > 19 else folder
    # Format and print the results values
    values = [str(val).center(col_widths[i+1]) for i, val in enumerate(results.values())]
    print(f"{folder_display:<20} | {' | '.join(values)}")
def process_folders(main_folder):
    """Processes folders within the given main folder.

    Args:
    main_folder (str): The path to the main folder.
    """
    headers = ['Folder', 'Headings', 'Images', 'Text Blocks', 'List', 'Hyperlink', 'Table', 'Emb CSS', 'Ext CSS', 'CSS Valid']
    col_widths = [21, 8, 8, 12, 6, 10, 6, 8, 8, 10]  # Adjusted column widths

    header_row = ' | '.join(header.center(col_widths[i]) for i, header in enumerate(headers))
    print(header_row)
    print("-" * (sum(col_widths) + 3 * (len(headers) - 1)))

    for folder in os.listdir(main_folder):
        folder_display = (folder[:19] + '..') if len(folder) > 19 else folder
        try:
            folder_path = os.path.join(main_folder, folder)
            if os.path.isdir(folder_path):
                html_file_path = find_html_file(folder_path)
                if html_file_path:
                    results = analyze_html(html_file_path, folder_path)
                    print_results(folder, results, col_widths)
                else:
                    #no_file_msg = ['No HTML file' if i == 1 else '' for i in range(len(headers))]
                    #print(f"{folder:<20} | {' | '.join(msg.center(col_widths[i]) for i, msg in enumerate(no_file_msg))}")
                    print(f"{folder_display:<20} | No HTML file")
        except Exception as e:
            #error_msg = ['Error' if i == 1 else '' for i in range(len(headers))]
            #print(f"{folder:<20} | {' | '.join(msg.center(col_widths[i]) for i, msg in enumerate(error_msg))}")
            print(f"{folder_display:<20} | Error")

# Example usage
data_folder = "data"
extracted_folder = "2_Extracted"

main_folder = os.path.join(data_folder, extracted_folder)
process_folders(main_folder)
