# -*- coding: utf-8 -*-
"""
This script downloads the data sets for examples in data subfolder of examples folder.

Created on Fri Aug 12 10:19:50 2024

@author: U.S. Securities and Exchange Commission.
"""

import requests
import zipfile
from io import BytesIO

def download_and_unzip(url, extract_to='.'):
    """
    Downloads a ZIP file from a URL and extracts its contents
    
    Parameters
    ----------
    url : str
        URL pointing to the ZIP file.
    extract_to : str, optional
        Directory path where the contents will be extracted. The default is 'data'.

    Returns
    -------
    None.

    """
    # Define headers with a User-Agent
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 (Contact: your-email@example.com)'
    }
    
    # Send a GET request to the URL
    print(f"Downloading ZIP file from {url} ...")
    response = requests.get(url, headers=headers)
    
    # Raise an exception if the download fails
    response.raise_for_status()
    
    # Create a ZipFile object from the bytes of the ZIP file
    zip_file = zipfile.ZipFile(BytesIO(response.content))
    
    # Extract the contents of the Zip file
    print(f"Extracting the contents to {extract_to}...")
    zip_file.extractall(path=extract_to)
    zip_file.close()
    print("Extraction complete.")
    
    
download_and_unzip("https://www.sec.gov/files/dera/data/financial-statement-data-sets/2022q1.zip", extract_to="examples/data/2022q1")
download_and_unzip("https://www.sec.gov/files/dera/data/financial-statement-data-sets/2022q2.zip", extract_to="examples/data/2022q2")
download_and_unzip("https://www.sec.gov/files/dera/data/financial-statement-data-sets/2022q3.zip", extract_to="examples/data/2022q3")
download_and_unzip("https://www.sec.gov/files/dera/data/financial-statement-data-sets/2022q4.zip", extract_to="examples/data/2022q4")
download_and_unzip("https://www.sec.gov/files/dera/data/financial-statement-notes-data-sets/2024_02_notes.zip", extract_to="examples/data/2024_02_notes")
