from django.shortcuts import redirect
from django.conf import settings as django_settings
from django.core.files.base import ContentFile
import requests

def generateUserName():
    response = requests.get('https://api.api-ninjas.com/v1/randomuser', headers={'X-Api-Key': 'LceLcBA8r2YMy0aBsaw2Uw==8tGk7QJr0FZefb9L'})
    if response.status_code == 200:
        return response.json()['username']

def generateUserAvatar(username):
    r = requests.get(f"https://robohash.org/{username}.png")
    return ContentFile(r.content)
        
def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('home')
		else:
			return view_func(request, *args, **kwargs)
	return wrapper_func