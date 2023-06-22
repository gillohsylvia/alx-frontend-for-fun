#!/usr/bin/python3

"""
markdown2html.py: Converts a Markdown file to HTML.

Usage: markdown2html.py <markdown_file> <output_file>
"""

import sys
import os
import markdown2

def convert_markdown_to_html(markdown_file, output_file):
    """
    Converts the given Markdown file to HTML and writes the output to the specified file.

    Args:
        markdown_file (str): Path to the Markdown file.
        output_file (str): Path to the output HTML file.
    """

    # Check if the Markdown file exists
    if not os.path.isfile(markdown_file):
        sys.stderr.write("Missing {}\n".format(markdown_file))
        sys.exit(1)

    # Read the Markdown content
    with open(markdown_file, 'r') as f:
        markdown_content = f.read()

    # Convert Markdown to HTML
    html_content = markdown2.markdown(markdown_content)

    # Write the HTML content to the output file
    with open(output_file, 'w') as f:
        f.write(html_content)

if __name__ == '__main__':
    # Check the number of arguments
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py <markdown_file> <output_file>\n")
        sys.exit(1)

    # Get the filenames from the command line arguments
    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    # Convert Markdown to HTML
    convert_markdown_to_html(markdown_file, output_file)

    # Exit successfully
    sys.exit(0)

