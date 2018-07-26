import hermitcraftvideos as hermitcraft

#Lets get Xsumiavoid as an example. Make sure to use the exact channel name.
x = hermitcraft.getHermit("xisumavoid")

#We can get his name (xisumavoid)
print(x.name)

#Or his shortened display name (Xisuma)
print(x.displayname)

#And his Profile Picture (https://yt3.ggpht.com/-x5tq4dTokyM/AAAAAAAAAAI/AAAAAAAAAAA/x4s30KOqUVA/s88-c-k-no/photo.jpg)
print(x.picture)

#We can get his youtube details too!
print("Name: {}".format(x.youtube.name))
print("Url: {}".format(x.youtube.url))
#We can see if he is live on youtube (He is on Twitch)
print("Live YT: {}".format(x.youtube.live))

#We can see if he is live on Twitch
print("Live Twitch: {}".format(x.twitch.live))

#We can get his latest videos
videos = x.getVideos()
#We can get the latest one
video = videos[0]
print("Title: {}".format(video.title))
#We can get stats!
print("Views: {}".format(video.views))
print("Likes: {}".format(video.likes))
#And other info!
print(video.duration_time + " mins long")
print("uploaded" + video.uploaded_time)