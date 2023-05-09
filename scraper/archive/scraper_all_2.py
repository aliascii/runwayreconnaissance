import os
import requests
from bs4 import BeautifulSoup


# URL of the webpage with the images
url = 'https://www.vogue.com/fashion-shows/fall-2023-menswear/saint-laurent/slideshow/collection'

# Output folder for the downloaded images
output_folder = '/Users/aliasci/rr/runwayreconnaissance/images'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Send a GET request to the webpage and parse the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the <img> tags on the webpage
img_tags = soup.find_all('img')

# Loop through each <img> tag and download the corresponding image
for i, img_tag in enumerate(img_tags):
    # Get the source URL of the image
    img_url = img_tag.get('src')

    # Skip images with empty URLs
    if not img_url:
        continue

    # Download the image to the output folder
    output_path = os.path.join(output_folder, f'{i+1}.jpg')
    response = requests.get(img_url)
    with open(output_path, 'wb') as f:
        f.write(response.content)
