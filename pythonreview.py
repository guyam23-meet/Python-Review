def create_youtube_video(title,description,hashtag):
	vid_dict = {"title":title,"description":description,"likes":0,"dislikes":0,"comments":{},"hastags":hashtag}
	return vid_dict
def likes(video):
	if "likes" in video:
		video["likes"]+=1
	return video

def dislikes(video):
	if "dislikes" in video:
		video["dislikes"]+=1
	return video

def add_comment(youtubevideo,username,comment_text):
	youtubevideo["comments"][username]=comment_text
	return youtubevideo

def similarity_to_video(vid1,vid2):
	if vid1["hashtags"].len()>vid2["hasgtags"].len():
		sml = vid2["hashtags"]
		big = vid1["hashtags"]
	else:
		sml = vid1["hashtags"]
		big = vid2["hashtags"]
	count=0
	for i in range(sml.len()):
		if sml[i] in big:
			count++
	return string(count/sml.len()*100)+"%"

IPrankedMyGF = create_youtube_video("OMG guys i pranked my girlfriend at 3am???","so yesterday at 3am me and the boys took my GF threw her in the pull drownd her and hid her body. best prank ever!")

for i in range(495):
	likes(IPrankedMyGF)

print(IPrankedMyGF["likes"])

add_comment(IPrankedMyGF,"guyam23-meet","bro nice vid bro do your dad next")

dislikes(IPrankedMyGF)

print(IPrankedMyGF)