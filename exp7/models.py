from exp7 import db

# Stores POS options for different languages.
class Lang_opt(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	options = db.Column(db.String(120), unique=True, nullable=False)

# Stores sentences of Hindi Language
class Hindi(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	sentence = db.Column(db.String(64), unique=True, nullable=False)
	answers = db.Column(db.String(120), nullable=False)

# Stores sentences of English Language
class English(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	sentence = db.Column(db.String(64), unique=True)
	answers = db.Column(db.String(120), nullable=False)