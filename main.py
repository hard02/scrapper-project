import requests
from bs4 import BeautifulSoup


def automate_voter_list_download(dist):
    # Launch the website and navigate to the desired page
    base_url = "https://ceoelection.maharashtra.gov.in/searchlist/"  # Replace with the actual website URL
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the district dropdown form field
    district_dropdown = soup.find("select", {"id": "ctl00_Content_DistrictList"})  # Update the attribute value here

    if district_dropdown is None:
        raise ValueError("District dropdown not found")

    # Find the district option and its value
    district_option = district_dropdown.find("option", string=dist)

    if district_option is None:
        raise ValueError("District option not found")

    district_value = district_option["value"]

    # Submit the form to select the district
    form_data = {
        "ctl00_Content_DistrictList": district_value,  # Update the field name here
        # Include any other form fields if required
    }
    response = requests.post(base_url, data=form_data)

    # Perform further actions to download the PDFs
    # ...
    # Implement the specific steps required to navigate, select constituencies, and download PDFs automatically
    # ...

    # Use the response variable for subsequent actions if needed
    # ...


district = input("Enter the district: ")
automate_voter_list_download(district)
