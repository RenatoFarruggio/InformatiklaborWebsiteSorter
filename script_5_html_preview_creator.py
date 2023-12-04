import os

def generate_html_preview(base_data_path, accepted_folder, output_html):
    """
    Generates an HTML file with previews for each subfolder in the accepted folder.
    """
    accepted_path = os.path.join(base_data_path, accepted_folder)
    html_snippets = []

    for folder in os.listdir(accepted_path):
        folder_path = os.path.join(accepted_path, folder)
        if os.path.isdir(folder_path):
            # Assuming each folder has 'index.html' and 'preview.png'
            html_snippet = f"""
            <div class="website-preview">
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
        <title>Website Previews</title>
        <style>
        .grid-container {{
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 10px;
        }}
        .website-preview {{
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
        }}
        .website-preview img {{
            width: 100%;
            height: auto;
        }}
        </style>
    </head>
    <body>
        <div class="grid-container">
        {''.join(html_snippets)}
        </div>
    </body>
    </html>
    """

    # Write the HTML content to a file
    with open(os.path.join(base_data_path, output_html), 'w') as file:
        file.write(full_html)

    print(f"HTML file '{output_html}' generated successfully.")

# Define the base 'data' folder path
base_data_path = 'data'

# Define the accepted subfolder and output HTML file name
accepted_folder = '3_Accepted'
output_html = 'website_previews.html'

# Usage
generate_html_preview(base_data_path, accepted_folder, output_html)
