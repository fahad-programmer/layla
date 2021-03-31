import requests
from bs4 import BeautifulSoup

def download_files(url):
    local_filename = url.split('/')[-1]
    print(local_filename)
    with requests.get(url, stream=True) as r:
        print("Downloading...")
        with open("D:/static/"+local_filename, 'wb') as f:
            print("Writing data to file")
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    f.close()
    print("Download complete")
    print("File saved as "+ local_filename)

while 1:
    print("Welcome to the image downloader")
    image_url = input(str("Image url : "))
    download_files(image_url)
    print("")