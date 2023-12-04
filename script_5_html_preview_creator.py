import os

def generate_html_preview_with_names_and_style(base_data_path, accepted_folder, output_html, css_file):
    """
    Generates an HTML file with previews, names, and external CSS for each subfolder in the accepted folder.
    """
    accepted_path = os.path.join(base_data_path, accepted_folder)
    html_snippets = []

    for folder in os.listdir(accepted_path):
        folder_path = os.path.join(accepted_path, folder)
        if os.path.isdir(folder_path):
            name_parts = folder.split('_')
            name = ' '.join(name_parts[::-1])
            html_snippet = f"""
            <div class="website-preview">
                <div class="creator-name">{name}</div>
                <a href="{os.path.join(accepted_folder, folder)}/index.html">
                    <img src="{os.path.join(accepted_folder, folder)}/preview.png" alt="Website Preview">
                </a>
            </div>
            """
            html_snippets.append(html_snippet)

    full_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="{css_file}">
        <title>Website Previews</title>
    </head>
    <body>
        <h1>Informatiklabor 2023 - Übung 10</h1>
        <h2>Alle Abgaben mit accept.txt</h2>
        <div class="grid-container">
        {''.join(html_snippets)}
        </div>
    </body>
    </html>
    """

    # Write the HTML content to a file with UTF-8 encoding
    with open(os.path.join(base_data_path, output_html), 'w', encoding='utf-8') as file:
        file.write(full_html)

    print(f"HTML file '{output_html}' generated successfully.")


def create_css_file(base_data_path, css_file):
    """
    Creates a CSS file with specific styles in the given directory.
    """
    css_content = """
    body {
        font-family: Arial, sans-serif;
        background-color: #1a1a1a; /* Dark background */
        color: #f5f5f5; /* Light text color */
        margin: 0;
        padding: 20px;
    }

    h1 {
        text-align: center;
        margin-bottom: 30px;
    }

    .grid-container {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 10px;
        padding: 10px;
    }

    .website-preview {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        overflow: hidden;
        background-color: #333333; /* Slightly lighter background for each preview */
        padding: 15px;
        border-radius: 8px;
    }

    .website-preview img {
        width: 100%;
        height: auto;
        border-radius: 5px;
    }

    .creator-name {
        margin-bottom: 10px;
        font-weight: bold;
        color: #e5e5e5; /* Bright text color for creator name */
    }
    """

    css_path = os.path.join(base_data_path, css_file)
    with open(css_path, 'w', encoding='utf-8') as file:
        file.write(css_content.strip())

    print(f"CSS file '{css_file}' created successfully.")


# Define the base 'data' folder path
base_data_path = 'data'

# Define the accepted subfolder and output HTML file name
accepted_folder = '3_Accepted'
output_html = 'website_previews.html'
css_file = 'style.css'

generate_html_preview_with_names_and_style(base_data_path, accepted_folder, output_html, css_file)

create_css_file(base_data_path, css_file)


