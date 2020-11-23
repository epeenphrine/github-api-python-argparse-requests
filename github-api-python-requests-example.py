#%%
##create repo
import requests
import json
from config import access_token, user
import os


def create_repo(repo_name):
    query_url = "https://api.github.com/user/repos"
    data = {'name':f'{repo_name}'}
    remote_url = f"https://github.com/{user}/{data['name']}.git"
    res = requests.post(query_url, auth=(user, access_token), data=json.dumps(data))
    print(res.content)

#%% 
##delete repo
import requests 
import json
from config import access_token
def delete_repo(repo_name):
    query_url = f"https://api.github.com/repos/{user}/{repo_name}"
    print(query_url)
    res = requests.delete(query_url, auth=(user,access_token))
    print(res.content)

#%%
## get list of repo 
import requests
from config import access_token
def list_repo(search):
    url = f'https://api.github.com/users/{user}/repos'

    res = requests.get(url).json()
    print(f"searching for : {search} in {len(res)} repos")
    #print(res)
    for item in res:
        if search.lower() in item['name'].lower():
            print(item['name'])

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--create-repo", help="create a new repo",
                    type=create_repo,
                    action="store")
parser.add_argument("--delete-repo", help="delete a repo",
                    type=delete_repo,
                    action="store")
parser.add_argument("--list-repo", help="filter repos",
                    type=list_repo,
                    action="store")
args = parser.parse_args()