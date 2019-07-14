import urllib.request

url = "[anything].mp4"
name = "One piece episode 1.mp4"

try:
    print("Downloading video...")
    urllib.request.urlretrieve(url, name)
    print("Download complete!")

except Exception as e:
    print(e)
