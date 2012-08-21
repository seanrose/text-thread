import os
import requests
import simplejson as json



from flask import Flask, request
app = Flask(__name__)

@app.route('/twilio', methods=['GET'])
def convert_text_to_comment():
	"""
	Twilio will post any texts it receives
	to this endpoint. We will do the following:

	-Get the text message from Twilio
	-Convert it into a Box comment object
	-Send the comment to Box 
	"""

	#Get the text message sent by Twilio
	message = request.args.get('Body')

	#Set up the comment to send to box
	box_comment = {'message' : message}
	
	#build the request to send to box
	url = "https://api.box.com/2.0/files/%s/comments" % os.environ['BOX_FILE']
	headers = {'Authorization' : 'BoxAuth api_key=%s&auth_token=%s' % (os.environ['BOX_API_KEY'], os.environ['BOX_AUTH_TOKEN'])}

	#send the request
	r = requests.post(url, data=json.dumps(box_comment), headers=headers)
	return r.text
    
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)