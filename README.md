# Wallbg
WallBG is a Script designed to Scrape wallpapers from <a href="https://www.wallpaperflare.com">www.wallpaperflare.com</a>, for your computer desktop.

## Install :
```
git clone https://github.com/NotoriousArnav/wallbg.git
cp wallbg/scrape_bg.py $(echo $PATH|awk -F ':' '{print $2}')
```

## Running :
```
### 1st way
echo -n "myquery !! /path/to/the/folder !! 1 !! 2" | scrape_bg.py

### 2nd way
scrape_bg.py #Now put your query,folder,verbose_bool,and halt in mins after it
```
