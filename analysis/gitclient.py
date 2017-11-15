from secret import req, get_secret, get_id
import requests
import json

TOK_ENDPOINT = 'https://github.com/login/oauth/access_token'
USER_ENDPOINT = 'https://api.github.com/user'
def get_token(session_code):
	payload = {'client_id':get_id(), 'client_secret':get_secret(),'code':session_code}
	result = requests.post('https://github.com/login/oauth/access_token',data=payload)

	token = result.text
	token = token.split('&')[0].split('=')[1]
	return token

def get_user(access_token):
	payload = {'access_token':access_token}
	u_data = requests.get('https://api.github.com/user',params=payload)
	return json.loads(u_data.text)

