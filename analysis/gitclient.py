from secret import req, get_secret, get_id
import requests
import json

TOK_ENDPOINT = 'https://github.com/login/oauth/access_token'
USER_ENDPOINT = 'https://api.github.com/user'
REPOS_ENDPOINT = 'https://api.github.com/user/repos'
COMMITS_ENDPOINT = 'https://api.github.com/repos'
def get_token(session_code):
	payload = {'client_id':get_id(), 'client_secret':get_secret(),'code':session_code}
	result = requests.post('https://github.com/login/oauth/access_token',data=payload)
	token = result.text
	token = token.split('&')[0].split('=')[1]
	return token

def get_user(access_token):
	payload = {'access_token':access_token}
	u_data = requests.get(USER_ENDPOINT,params=payload)
	return json.loads(u_data.text)

def get_repos(access_token):
	payload = {'access_token':access_token,'sort':'created'}
	repos = requests.get(REPOS_ENDPOINT,params=payload)
	return repos.text

def get_all_commits(access_token, u_name):
	commits = []
	payload = {'access_token':access_token}
	for repo in json.loads(get_repos(access_token)):
		name = repo['name']
		result = json.loads(requests.get(COMMITS_ENDPOINT + '/' + u_name + '/' + name + '/commits'
										 ,params=payload).text);
		commits += result
	return commits

def get_commits(access_token, repo, owner):
	 payload = {'access_token':access_token}
	 result = json.loads(requests.get(COMMITS_ENDPOINT + '/' + owner + '/' + repo + '/commits'
		 								,params=payload).text);
	 return result
	
