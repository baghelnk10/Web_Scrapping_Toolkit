############################################################################
# Developer: N.K. Baghel (U. Louisville)                                   #
# Created on: 5-Jan-2024                                                   #
# Modified on: 5-Jan-2023                                                  #
# Usage: Scrapping from git file                                           #
# Documentation: Use this code to prints the raw content of a gitlab file  #                             
#                protected behind api.                                     #                           
# See git log for contributors and copyright holders.                      #
# This file is licensed under LGPL-3.0, see LICENSE.md.                    #
############################################################################



import requests

# Define the GitLab project namespace, project name, and file path
project_path = "belle2/data-production/mc"                             # For example
file_path = "MC10/release-01-00-01/DB00000294/4S/signal/3470020000.py" #For Example
encoded_project_namespace = requests.utils.quote(project_path, safe='')   # output same as below
#encoded_project_namespace = "belle2%2Fdata-production%2Fmc"
encoded_path = requests.utils.quote(file_path, safe='')  # output same as below
#encoded_path= "MC10%2Frelease-01-00-01%2FDB00000294%2F4S%2Fsignal%2F3470020000.py" 

# Specify the branch or reference (e.g., "master")
reference = "master"

# Build the GitLab API URL for the raw file
url = f"https://gitlab.desy.de/api/v4/projects/{encoded_project_namespace}/repository/files/{encoded_path}/raw?ref={reference}"

# Replace 'access_token' with your GitLab access token
access_token = "uLp5B4brvzGttaw5x5xR"

# Set up headers with the access token for authentication
headers = {
    "PRIVATE-TOKEN": access_token
}

# Make an HTTP GET request to the GitLab API to fetch the raw content
response = requests.get(url, headers=headers)

# Check if the request was successful (HTTP status code 200)
if response.status_code == 200:
    # Extract the raw content from the response
    raw_content = response.text
    print(raw_content)
else:
    # Print an error message if the request fails
    print(f"Failed to fetch raw content. Status code: {response.status_code}")


