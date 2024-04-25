#!/usr/bin/python3
"""
This is a script to convert a Markdown file to HTML.

Usage:
    ./markdown2html.py README.md README.html

Arguments:
    input_file: First argument is the name of the Markdown file
    output_file: Second argument is the output file name

"""

import argparse
import pathlib
import re
import sys 

def conv_md_to_html(input_file, output_file):
    '''
    Converts markdown file to HTML file
    '''
    with open(input_file, encoding='utf-8') as f:
        md_cont = f.readlines()

    html_cont = []
    for line in md_cont:
        # Check if the line is a heading
        match = re.match(r'(#){1,6} (.*)', line)
        if match:
            # Get the level of the heading
            h_level = len(match.group(1))
            # Get the content of the heading
            h_content = match.group(2)
            # Append the HTML equivalent of the heading
            html_cont.append(f'<h{h_level}>{h_content}</h{h_level}>\n')
        else:
            html_cont.append(line)

    # Write the HTML content to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(html_cont)


if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Convert markdown to HTML')
    parser.add_argument('input_file', help='path to input markdown file')
    parser.add_argument('output_file', help='path to output HTML file')
    args = parser.parse_args()

    # Check if the input file exists
    input_path = pathlib.Path(args.input_file)
    if not input_path.is_file():
        print(f'Missing {input_path}', file=sys.stderr)
        sys.exit(1)

    # Convert the markdown file to HTML
    conv_md_to_html(args.input_file, args.output_file)
