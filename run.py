#!venv/bin/python
import os
from app import app

if __name__ == '__main__':
	 port = int(os.environ.get('PORT', 3000))
	 #app.run(host='0.0.0.0', port=port, debug = True)
	 app.run(host='0.0.0.0', port=port)
	 



