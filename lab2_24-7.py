def create_youtube_video(title,description) :
	comments ={};

	dic1 = {"title" : title , "description" : description , "likes": 0, "dislikes":0 ,"comments":{}}
	return dic1
def like (dic1):
	if "likes" in dic1:
		dic1["likes"]=dic1["likes"]+1
	return dic1 

def dislike (dic1):
	if "dislikes" in dic1:
		dic1["dislikes"]+=1
	return dic1 

def add_comment(dic1,username,comment_text):
	dic1["comments"][username]=comment_text
	return dic1 
first= create_youtube_video("hii","idk what the description is")
like(first)
dislike(first)
add_comment(first, "larinee","hi")


for i in range(495):
	like(first)
	
print(first)

