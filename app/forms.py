from wtforms import form, fields, validators

class LoginForm(form.Form):
	username = fields.TextField('username', validators=[validators.DataRequired()])
	password = fields.PasswordField('password', validators=[validators.DataRequired()])
		
class CommentForm(form.Form):
	comments = fields.TextField('comments')
	
class LikeForm(form.Form):
	liked = fields.TextField('liked')
	
class adminForm(form.Form):
	photo_description = fields.TextField('photo_description')
	price = fields.TextField('price')
	amount = fields.TextField('amount')
	size = fields.TextField('size')
	
class signupForm(form.Form):
	username = fields.TextField('username', validators=[validators.DataRequired()])
	password = fields.TextField('password', validators=[validators.DataRequired()])
	email = fields.TextField('email', validators=[validators.DataRequired()])
	number = fields.TextField('number', validators=[validators.DataRequired()])
	user_option = fields.TextField('user_option', validators=[validators.DataRequired()])
	#user = fields.TextField('user', validators=[validators.DataRequired()])
	#retailer = fields.TextField('retailer', validators=[validators.DataRequired()])
	
