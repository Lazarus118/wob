#!venv/bin/python
from app import app
app.run(debug = True)

#app.run()
#Bind to PORT if defined, otherwise default to 5000. 

port = int(os.environ.get('PORT', 4000))
app.run(host='0.0.0.0', port=port)
