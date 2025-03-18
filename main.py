import requests
from bs4 import BeautifulSoup
import os

# Fetch the HTML content
url = "https://www.britannica.com/place/Victor-Emmanuel-II-Monument"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# -------------------------------------------------------------------------------------------------------------------------------


# Finding specific image:

# finding specific image
specific_image = soup.find('img', {'alt' : "Victor Emmanuel II Monument"})
img_url = specific_image['src']

# saving image
img_data = requests.get(img_url).content
with open('image.jpg', 'wb') as img_file:
    img_file.write(img_data)


# -------------------------------------------------------------------------------------------------------------------------------


# finding all images:

# Gather Images
# images = soup.find_all('img')
# img_urls = [img['src'] for img in images if 'src' in img.attrs]

# # download images and create folder to house images
# os.makedirs('images', exist_ok=True)

# # save images
# for i, img_url in enumerate(img_urls):
#     img_data = requests.get(img_url).content
#     with open(f'images/image_{i+1}.jpg', 'wb') as img_file:
#         img_file.write(img_data)