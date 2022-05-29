#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import time

"""
This script uses BeautifulSoup and Requests to scrape www.wallpaperflare.com to scrape wallpapers.
The three Functions are used to search, download and save the results.
"""

def search_bg(query="spongebob", verbose=False):
     """
	NOTE : Verbose is turned off By default, but you can Turn it on by ```verbose=True``` in arguments
		Function to Get Search results from Wallpaperflare.com
		The Output is in a list type, containing links to all the wallpaper pages
    """
     try:
        r = requests.get("https://www.wallpaperflare.com/search?wallpaper="+'+'.join(query.split(" ")))
        soup = BeautifulSoup(r.content, 'html.parser')
        ul_gallery = soup.find('ul', {'id':'gallery'})
        li_list = ul_gallery.find_all('li', {"itemtype":"http://schema.org/ImageObject"})
        a_list = [x.find('a').get('href') for x in li_list]
        return a_list
     except Exception as e:
        if verbose: print(e)
        if isinstance(e, requests.exceptions.ConnectionError): print("Please Check your Internet Connection")
        print("Connectivity issue with the server")
        return

def bytes_bg(link, verbose=False):
    """
	NOTE : Verbose is turned off By default, but you can Turn it on by ```verbose=True``` in arguments
	This function downloads the picture from {link}/download page.
	This downloads Orignal Resolution picture and returns an Byte-Array.
    """
    try:
        r = requests.get(f'{link}/download').content #Get the Page
        soup =  BeautifulSoup(r, 'html.parser') # Parse it
        img = soup.find('img', {'id':'show_img'}).get('src') # Find the Image link
        img_bytes = requests.get(img).content # Download the Image in RAM
    except Exception as e:
        if verbose: print(e)
        print("Connectivity Issue with the Server")
        return Exception(e)
    return img_bytes #Give the Image

def saveBytesTofile(bytes_, path_filename, verbose=False):
    """
	NOTE : Verbose is turned off By default, but you can Turn it on by ```verbose=True``` in arguments
	This saves the Bytes downloaded to the file Specified.
    """
    try:
        with open(path_filename, 'wb') as f:
            f.write(bytes_)
        print(f"\rFile written at {path_filename}                                          ", end="")
    except Exception as e:
        if verbose: print(e)
        print("Error Could not write the file")
        return

if __name__ == "__main__":
    query, folderpath, verbose, halt= input("query !! folderpath  !! verbose !! halt in minutes: ").split('!!')
    print(f"\r Query:{query},Folder: {folderpath}, Verbose: {bool(verbose)}", end="")
    while True:
        try:
            bglist = search_bg(query=query, verbose=bool(verbose))
            for x in bglist:
                filename = x.split('/')[-1]+'.jpg'
                img_bytes = bytes_bg(x, verbose=bool(verbose))
                saveBytesTofile(img_bytes, f"{folderpath}/{filename}")
        except KeyboardInterrupt:
            print("Signal recieved: Exiting")
            break
        except TypeError as e:
            print("Could not Fetch Query from the Server")
            break
        time.sleep(int(halt)*60)
