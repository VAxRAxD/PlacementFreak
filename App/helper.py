from django.shortcuts import redirect
from django.http import HttpResponseForbidden
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

def superuser_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseForbidden("You are not authorized to access this page.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view