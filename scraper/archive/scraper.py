import os
import requests
from bs4 import BeautifulSoup

# URL of the webpage containing the images
url = "https://www.vogue.com/fashion-shows/fall-2023-menswear/saint-laurent/slideshow/collection"

# Send a request to the webpage and get the HTML content
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all img tags on the webpage
imgs = soup.find_all('img')

# Create the directory to save the images
if not os.path.exists('images'):
    os.makedirs('images')

# Download each image and save it to the images directory
for i, img in enumerate(imgs):
    # Get the URL of the image
    img_url = img['src']
    
    # Check if the URL is a relative URL
    if img_url.startswith('/'):
        img_url = f"https://www.vogue.com{img_url}"
    
    # Send a request to the image URL and get the content
    response = requests.get(img_url)
    
    # Save the image to a file
    filename = f"image{i+1}.jpeg"
    filepath = os.path.join('images', filename)
    with open(filepath, 'wb') as f:
        f.write(response.content)
        print(f"Saved image {filename}")
