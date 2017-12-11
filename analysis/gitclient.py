from secret import req, get_secret, get_id
import requests
import json

TOK_ENDPOINT = 'https://github.com/login/oauth/access_token'
USER_ENDPOINT = 'https://api.github.com/user'
REPOS_ENDPOINT = 'https://api.github.com/user/repos'
COMMITS_ENDPOINT = 'https://api.github.com/repos'

#get access token
def get_token(session_code):
	payload = {'client_id':get_id(), 'client_secret':get_secret(),'code':session_code}
	result = requests.post('https://github.com/login/oauth/access_token',data=payload)
	token = result.text
	token = token.split('&')[0].split('=')[1]
	return token

#get user data
def get_user(access_token):
	payload = {'access_token':access_token}
	u_data = requests.get(USER_ENDPOINT,params=payload)
	return json.loads(u_data.text)

#get all repos
def get_repos(access_token):
	payload = {'access_token':access_token,'sort':'created'}
	repos = requests.get(REPOS_ENDPOINT,params=payload)
	return json.loads(repos.text)

#get all commits to all repos
def get_all_commits(access_token, u_name):
	commits = []
	payload = {'access_token':access_token}
	for repo in json.loads(get_repos(access_token)):
		name = repo['name']
		result = json.loads(requests.get(COMMITS_ENDPOINT + '/' + u_name + '/' + name + '/commits'
										 ,params=payload).text);
		commits += result
	return commits

#get the commits data for a single repo
def get_commits(access_token, repo, owner):
	 payload = {'access_token':access_token}
	 result = json.loads(requests.get(COMMITS_ENDPOINT + '/' + owner + '/' + repo + '/commits'
		 								,params=payload).text);
	 return result
	
#get commits per repo
def get_cpa(access_token, owner):
	return 1

def leach(access_token, u_name):
	return True
