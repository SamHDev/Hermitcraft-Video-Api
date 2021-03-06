# Hermitcraft Video API
This is a python wrapper for the Hermitcraft.com api, that supports retrieving data for hermits and their videos.

The Site was created by hypnotised, and the api is used within the site to get the latest videos and see when hermits are live. This uses those api endpoints allowing us to get the data that the site uses.

# Getting started

Go ahead and import the library.
```py
import hermitcraftvideos
```

Next, we get a hermit from the api. Let's use Xisumavoid for this example.
```py
hermit = hermitcraftvideos.getHermit("xisumavoid")
```
Make sure that you use the right name. It needs to be the EXACT channel name in the youtube URL in lower case. ``Example: Mumbo --> https://www.youtube.com/user/ThatMumboJumbo --> thatmumbojumbo``

How we have our hermit from the api, we can find out data.

Such as a profile picture
```py
print(hermit.picture) #https://yt3.ggpht.com/-x5tq4dTokyM/AAAAAAAAAAI/AAAAAAAAAAA/x4s30KOqUVA/s88-c-k-no/photo.jpg
```

Or we can find out a twitter:
```py
print("@{} - {}".format(hermit.twitter.name,hermit.twitter.url)) #@xisumavoid - https://twitter.com/xisumavoid
```

Or better, if they are live on youtube, twitch or mixer(beam)
```py
print(hermit.youtube.live) #False
print(hermit.twitch.live) #True
print(hermit.mixer.live) #False
```

We can also get videos!
```py
videos = hermit.getVideos()
```

You can get simple data from the video
```py
video = videos[0]
print(video.title) #Hermitcraft VI 712 Already Its The End!
```

And Some handy data
```py
print("video is {} mins long".format(video.duration_time)) #video is 22:49 mins long
print("uploaded {}".format(video.uploaded_time)) #uploaded 7 hours ago 
```

Oooooh. Statistics
```py
print(video.views) #44430
print(video.likes) # 2785
```

Oooooooooooooooooooooooooooooooooooooh. Updated Statistics
```py
video.update()
print(video.views) #44440
print(video.likes) # 2790
```

And That's Mostly it. You can also get a jumble of videos with
```
hermitcraftvideos.getLatestVideos()
```

# API Reference

Soon!
