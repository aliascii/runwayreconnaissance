import requests
from bs4 import BeautifulSoup
import os

# URL of the webpage to scrape
url = "https://www.vogue.com/fashion-shows/fall-2023-menswear/saint-laurent/slideshow/collection"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object from the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the image tags on the page
img_tags = soup.find_all('img')

# Create a directory to store the downloaded images
output_dir = '/Users/aliasci/rr/runwayreconnaissance/images'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Iterate over the range of image numbers (1-47)
for i in range(1, 48):
    # Get the URL of the image to download
    img_url = f"https://www.vogue.com/fashion-shows/fall-2023-menswear/saint-laurent/slideshow/collection#{i}"
    # Send a GET request to the image URL
    response = requests.get(img_url)
    # Save the image to the output directory
    with open(f"{output_dir}/image_{i}.jpg", "wb") as f:
        f.write(response.content)
        print(f"Image {i} downloaded")
