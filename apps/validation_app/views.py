from django.shortcuts import render
from .models import User

# Create your views here.
def index(request):
    print("Running index method, calling out to User.")
    user = User.objects.login("speros@codingdojo.com","Speros")
    # DO NOT PASS THE WHOLE REQUEST OBJECT TO THE MODEL!!!
    print (type(user))
    if 'error' in user:
        pass
    if 'theuser' in user:
        pass
    return HttpResponse("Done running userManager method. Check your terminal console.")
