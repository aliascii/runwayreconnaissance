#FIRST CODE WORKS BUT DOWNLOADS 47 TIMES THE SAME IMAGE
import requests
from bs4 import BeautifulSoup
import os

base_url = 'https://www.vogue.com/fashion-shows/fall-2023-menswear/saint-laurent/slideshow/collection#{}'

if not os.path.exists('vogue_images'):
    os.makedirs('vogue_images')

image_urls = []

for i in range(1, 47):  # there are 47 pages in this slideshow
    url = base_url.format(i)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # find all img tags with class "responsive-image__image"
    for img in soup.find_all('img', class_='responsive-image__image'):
        src = img.get('src')
        # check if the image source contains "vogue.com/photos/" and ends with ".jpg"
        if "vogue.com/photos/" in src and src.endswith(".jpg"):
            image_urls.append(src)

for i, img_url in enumerate(image_urls):
    img_response = requests.get(img_url)
    img_name = f"vogue_images/{i+1:02d}.jpg"
    with open(img_name, 'wb') as f:
        f.write(img_response.content)
        print(f"Image {i+1} saved as {img_name}")

#SELENIUM CODE
# import time
# import requests
# from selenium import webdriver

# # set up the webdriver
# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--incognito')
# options.add_argument('--headless')
# driver = webdriver.Chrome(options=options)

# # navigate to the first slide
# url = 'https://www.vogue.com/fashion-shows/fall-2023-menswear/saint-laurent/slideshow/collection#1'
# driver.get(url)

# # find the image and download it
# img = driver.find_element_by_class_name('slide-image')
# src = img.get_attribute('src')
# response = requests.get(src)
# with open('1.jpg', 'wb') as f:
#     f.write(response.content)

# # iterate over the rest of the slides and download the images
# for i in range(2, 4):
#     # click the "Next" button
#     next_button = driver.find_element_by_class_name('slide-next')
#     next_button.click()
#     # wait for the image to load
#     time.sleep(2)
#     # find the image and download it
#     img = driver.find_element_by_class_name('slide-image')
#     src = img.get_attribute('src')
#     response = requests.get(src)
#     with open(f'{i}.jpg', 'wb') as f:
#         f.write(response.content)

# # close the webdriver
# driver.quit()