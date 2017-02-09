import praw
from urllib.request import urlopen
from io import BytesIO
from PIL import Image
from datetime import datetime

user_agent = ("Wallpaper Script by /u/sukibae 1.1")
r = praw.Reddit(client_id = "nMeXsi0VEEaW_A", user_agent = user_agent, client_secret = "E6PLfbBEs_CyKqlFYgxe046fop8")

for post in r.subreddit("earthporn").hot(limit = 5):
    response = urlopen(post.url)
    data = response.read()
    print(post.title)
    try:
        image = Image.open(BytesIO(data))
        image.verify()
        fname= "Images/" + str(datetime.now()) + ".jpg"
        Image.open(BytesIO(data)).save(fname)
    except:
        # Encountered issue downloading image. Image is probably somewhere in the page
        # or might not be a filetype supported by PIL
        pass
