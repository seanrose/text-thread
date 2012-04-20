import os

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

#Endpoint that handles Twilio callbacks
@app.route('/twilio', , methods=['GET', 'POST'])
def convert_text_to_comment():
	return 'Hello Twilio!'

#Endpoint that handles Box authentication
@app.route('/box', methods=['GET', 'POST'])
def box():
	return 'Hello Box!'
    

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)