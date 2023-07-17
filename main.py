"""
This is the main Python script for generating a PDF file using pdfkit
"""

# Imports
import sys

# import pdfkit
import pdfkit

# Global variables

# Class declarations

# Function declarations

def main():
    options = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    }
    
    pdfkit.from_file('contract.html', 'contract.pdf', options=options, css='style.css')

# Main body
if __name__ == '__main__':
    main()