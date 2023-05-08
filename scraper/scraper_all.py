# import requests
# from bs4 import BeautifulSoup
# import os

# # URL of the webpage to scrape
# url = "https://www.vogue.com/fashion-shows/fall-2023-menswear/saint-laurent/slideshow/collection"

# # Use a header in 
# headers = {'User-agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36'}

# # Send a GET request to the URL
# response = requests.get(url, headers=headers)

# # Create a BeautifulSoup object from the HTML content
# soup = BeautifulSoup(response.content, 'html.parser')

# # Find all the image tags on the page
# img_tags = soup.find_all('img')

# # Create a directory to store the downloaded images
# output_dir = '/Users/aliasci/rr/runwayreconnaissance/images'
# if not os.path.exists(output_dir):
#     os.makedirs(output_dir)

# # Iterate over the range of image numbers (1-47)
# for i in range(1, 48):
#     # Get the URL of the image to download
#     img_url = f"https://www.vogue.com/fashion-shows/fall-2023-menswear/saint-laurent/slideshow/collection#{i}"
#     # Send a GET request to the image URL
#     response = requests.get(img_url)
#     # Save the image to the output directory
#     with open(f"{output_dir}/image_{i}.jpg", "wb") as f:
#         f.write(response.content)
#         print(f"Image {i} downloaded")
#         print(response.status_code)

# <img alt="" class="ResponsiveImageContainer-dkDswF jdxiQR responsive-image__image" src="https://assets.vogue.com/photos/63c7533b3a32434f4bef5ab4/master/w_2560%2Cc_limit/00001-saint-laurent-fall-2023-menswear-credit-brand.jpg">
# <img alt="" class="ResponsiveImageContainer-dkDswF jdxiQR responsive-image__image" src="https://assets.vogue.com/photos/63c753317022d35c31c7667b/master/w_2560%2Cc_limit/00002-saint-laurent-fall-2023-menswear-credit-brand.jpg">

# THIS CODE WORKS BUT ONLY DOWNLOADS 1 IMG
import requests
from bs4 import BeautifulSoup
import os

# url = 'https://www.vogue.com/fashion-shows/fall-2023-menswear/saint-laurent/slideshow/collection#'
url = 'https://www.vogue.com/fashion-shows/fall-2023-menswear/saint-laurent#review'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

image_urls = []

# find all img tags with class "responsive-image__image"
for img in soup.find_all('img', class_='responsive-image__image'):
    src = img.get('src')
    # check if the image source contains "vogue.com/photos/" and ends with ".jpg"
    if "https://assets.vogue.com/photos/" in src and src.endswith(".jpg"):
        image_urls.append(src)

# create folder to save images
if not os.path.exists('images'):
    os.makedirs('images')

# download and save images
for i, url in enumerate(image_urls):
    response = requests.get(url)
    filename = f"{i+1:02d}.jpg"
    filepath = os.path.join('images', filename)
    with open(filepath, 'wb') as f:
        f.write(response.content)
        print(f"Saved {filename}")
