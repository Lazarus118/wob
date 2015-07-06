from app import db
from datetime import datetime

#*************************************************************************************#
# //User database class 
#*************************************************************************************#
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), index=True, unique=True)
	password = db.Column(db.String(64), index=True)
	email = db.Column(db.String(64), index=True, unique=True)
	comment = db.relationship('Comments', backref='author', lazy='dynamic')

	
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
	def __init__(self, comment):
		self.comment = comment	
		
#*************************************************************************************#
# //Comments database class 
#*************************************************************************************#		
class Comments(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	comments = db.Column(db.String(64), index=True, unique=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	
	def __init__(self, comments):
		self.comments = comments

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
	#uploaded_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	company = db.Column(db.String(64), index=True)
	price = db.Column(db.String(12), index=True)
	amount = db.Column(db.String(100), index=True)

	def __init__(self, photo_description, photo_filename, company, price, amount):	
		self.photo_description = photo_description
		self.photo_filename = photo_filename
		self.company = company
		self.price = price
		self.amount = amount
		#self.uploaded_at = uploaded_at
	
	
	
	
