from app import db
from datetime import datetime

Image_comments = db.Table('Image_comments',
    db.Column('image_id', db.Integer, db.ForeignKey('image.id')),
    db.Column('comments_id', db.Integer, db.ForeignKey('comments.id'))
)

#*************************************************************************************#
# //User database class 
#*************************************************************************************#
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), index=True, unique=True)
	password = db.Column(db.String(64), index=True)
	email = db.Column(db.String(64), index=True)
	number = db.Column(db.String(64), index=True)
	individual = db.Column(db.String(10), index=True)
	retailer = db.Column(db.String(10), index=True)
	
	#*********************************************************************#
	# // Database relational link for Comments
	#*********************************************************************#
	comments = db.relationship('Comments', backref='user', lazy='dynamic') 
	
	#*********************************************************************#
	# // Database relational link for Image
	#*********************************************************************#
	images = db.relationship('Image', backref='user', lazy='dynamic')
	
	
	def is_authenticated(self):
		return True
	def is_active(self):
		return True
	def is_anonymous(self):
		return False
	def get_auth_token(self):
		return unicode(hashlib.sha1(self.username + self.password).hexdigest())
	def get_id(self):
		return unicode(self.id)
	def __repr__(self):
		return '<User %r>' % (self.username)
	
	def __init__(self, email, number, individual, retailer):
		self.email = email
		self.number = number
		self.individual = individual
		self.retailer = retailer	
	
	
#*************************************************************************************#
# //Comments database class 
#*************************************************************************************#		
class Comments(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	comments = db.Column(db.String(64), index=True, unique=True)
	image_comments = db.relationship('Image', secondary=Image_comments, backref=db.backref('comments', lazy='dynamic'))
	
	#*******************************************************#
	# // ForeignKey link to User
	#*******************************************************#
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	
	
	
	def __init__(self, comments, user_id):
		self.comments = comments
		self.user_id = user_id

#*************************************************************************************#
# //Number of Likes database class 
#*************************************************************************************#
class Like(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	liked = db.Column(db.String(1000), index=True, unique=False)
	
	
	def __init__(self, liked):
		self.liked = liked 
		
#*************************************************************************************#
# //Images database class 
#*************************************************************************************#
class Image(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	photo_description = db.Column(db.Unicode(64))
	photo_filename = db.Column(db.Unicode(128))
	uploaded_at = db.Column(db.String(12), index=True)
	price = db.Column(db.String(12), index=True)
	amount = db.Column(db.String(100), index=True)
	size = db.Column(db.String(50), index=True)
	
	#*******************************************************#
	# // ForeignKey link to User
	#*******************************************************#
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	

	def __init__(self, photo_description, photo_filename, price, amount, size, uploaded_at, user_id):	
		self.photo_description = photo_description
		self.photo_filename = photo_filename
		self.price = price
		self.amount = amount
		self.size = size 
		self.uploaded_at = uploaded_at
		self.user_id = user_id
	
	
	
	
	
