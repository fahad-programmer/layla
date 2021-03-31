from google_images_search import GoogleImagesSearch


def my_progressbar(url, progress):
    print(f"{url}  {progress}%")

gis = GoogleImagesSearch('AIzaSyCv-IIGcdyrQVRNEXvuNLtRxlBULLAmgQQ', '2a12700713ad1971c', progressbar_fn=my_progressbar)

_search_params = {
    'q': 'atif aslam',
    'num': 10,
}


gis.search(search_params=_search_params, path_to_dir='C:\\Users\\unexp\\Pictures\\Layla\\')