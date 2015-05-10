from pymongo import MongoClient
import datetime 
class User:
	def __init__(self, userId,email,articleIds,commentIds,userName,userDesc):
		self.userId = userId  
		self.email =  email
		self.articleIds =  articleIds
 		self.commentIds  = commentIds
		self.userName =   userName
		self.userDesc =  userDesc

class Article:
	def __init__(self, articleId,authorId,visibility,dateOfPublication,articleHeading,para_ids,para_ids_sequence,commentIds):
		self.articleId = articleId  
		self.authorId =  authorId
		self.visibility =  visibility
		self.dateOfPublication  = dateOfPublication
		self.articleHeading  =  articleHeading
		self.para_ids =   para_ids
		self.para_ids_sequence =  para_ids_sequence
		self.commentIds  =  commentIds

class Paragraph:
	def __init__(self, paraId,commentIds,articleId,content):
		self.paraId = paraId 
		self.commentIds =  commentIds
		self.articleId =  articleId
		self.content  = content

class Comment:
	def __init__(self, commentid,articleId,paraId,authorId,visibility ,content):
		self.commentid = commentid 
		self.articleId =  articleId
		self.paraId  = paraId
		self.authorId =  authorId
		self.visibility  =  visibility
		self.content =  content



def LoadAllUsers():
	us  =  users.find()
	for e in us:
		print e["username"] 
		print "\n"
		print "\n"

def LoadAllArticles():
	arts =  articles.find()
	for e in arts:
		print e["articleHeading"] 
		print "Author  ->  "  + (users.find({"user_id" : e["author_id"]})[0])["username"]  
		print "\n"
		print "\n"

def LoadArticle(id):
	art  =  articles.find({"article_id":id})
	for e in art:
		print e["articleHeading"]
		paraseq =  e["para_ids_sequence"]
		for g in paraseq:
			print "New Para"
			print ((paragraphs.find({"para_id":g}))[0])["content"]
			commentids = ((paragraphs.find({"para_id":g}))[0])["comment_ids"]
			if(len(commentids)>0):
				for comm in commentids:
					print "New Comment"
					print ((comments.find({"comment_id":comm}))[0])["content"]
		acomm  =  e["comment_ids"]
		if(len(acomm)>0):
			for f  in acomm:
				print "New Article Comment"
				#print f
				print ((comments.find({"comment_id":f}))[0])["content"]

def insert_new_user(userDetails):
	us  =   {"user_id":userDetails.userId,
		  "email":  userDetails.email,
		  "articleIds" :userDetails.articleIds,
		  "CommentIds" : userDetails.commentIds,
		  "username" : userDetails.userName,
		  "userdesc" : userDetails.userDesc,
		}
	users.insert(us)    

def insert_new_article(articleDetails):
	article  =   {"article_id": articleDetails.articleId,
		  "author_id" :articleDetails.authorId,
		  "visibility" : articleDetails.visibility,
		  "dateOfPublication" : articleDetails.dateOfPublication,
		  "articleHeading"  : articleDetails.articleHeading,
		  "para_ids" : articleDetails.para_ids,
		  "para_ids_sequence" : articleDetails.para_ids_sequence,
		  "comment_ids" : articleDetails.commentIds
		}
	articles.insert(article)    


def insert_new_paragraph(paragraphDetails):
	paragraph =  {"para_id":paragraphDetails.paraId,
				  "comment_ids":paragraphDetails.commentIds,
				  "article_id": paragraphDetails.articleId,
				  "content":paragraphDetails.content

	}
	paragraphs.insert(paragraph)

def insert_new_comment(commentDetails):
	comment  = {"comment_id":commentDetails.commentid,
				"article_id":commentDetails.articleId,
				"para_id" : commentDetails.paraId,
				"visibility": commentDetails.visibility,
				"author_id":commentDetails.authorId,
				"content" : commentDetails.content
	}
	comments.insert(comment)


client = MongoClient()

#databse
db = client['Medium']

#Collections
users =  db.users
articles =  db.articles
comments =  db.comments
paragraphs = db.paragraphs

#create new user 
#newUser  = User(1,"sahil@gmail.com",[1,2],[3],"sahil","cool")
#newUser  = User(3,"sachin@gmail.com",[5],[2],"scahin","geeks")
#newUser  = User(2,"rahul@gmail.com",[3],[4],"rahul","crazy")
#insert_new_user(newUser)
#users.drop()
#print users
#print users.find_one()


#create new article 
#newArticle  = Article(5,3,0,datetime.datetime.utcnow(),"This is fourth article",[7],[7])
#insert_new_article(newArticle)
#articles.drop()

newArticle  = Article(5,3,0,datetime.datetime.utcnow(),"This is fourth article",[7],[7],[1])
#insert_new_article(newArticle)
newArticle  = Article(3,2,0,datetime.datetime.utcnow(),"This is third article",[6],[6],[2])
#insert_new_article(newArticle)
newArticle  = Article(2,1,0,datetime.datetime.utcnow(),"This is second article",[4,5],[4,5],[3])
#insert_new_article(newArticle)
newArticle  = Article(1,1,0,datetime.datetime.utcnow(),"This is first article",[1,2,3],[2,3,1],[3])
#insert_new_article(newArticle)
#print articles
#print articles.find_one()



#create new paragraphs
#paragraphs.drop()
newPara = Paragraph(4,[1],2,"Testing 7")
#insert_new_paragraph(newPara)

newPara = Paragraph(5,[],2,"Testing 6")
#insert_new_paragraph(newPara)

newPara = Paragraph(6,[2],3,"Testing 5")
#insert_new_paragraph(newPara)

newPara = Paragraph(7,[1],4,"Testing 4")
#insert_new_paragraph(newPara)

newPara = Paragraph(3,[3],1,"Testing 3")
#insert_new_paragraph(newPara)

newPara = Paragraph(2,[2],1,"Testing 2")
#insert_new_paragraph(newPara)

newPara = Paragraph(1,[],1,"Testing 1")
#insert_new_paragraph(newPara)




#print paragraphs
#print paragraphs.find_one()

#create new comment
newComment = Comment(3,1,-1,0 ,1,"This is a cool paragraph")
#insert_new_comment(newComment)
#print comments

print "List of all Users"
LoadAllUsers()
print "List of all Articles"
LoadAllArticles()

LoadArticle(2)