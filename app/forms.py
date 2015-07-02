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
	company = fields.TextField('company')
	price = fields.TextField('price')
	amount = fields.TextField('amount')
	
class signupForm(form.Form):
	username = fields.TextField('username', validators=[validators.DataRequired()])
	password = fields.TextField('password', validators=[validators.DataRequired()])
	email = fields.TextField('email', validators=[validators.DataRequired()])