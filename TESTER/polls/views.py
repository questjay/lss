from django.shortcuts import render
from django.http import HttpResponse
from proxy_server.decorators import expose_service
from proxy_server.helpers import generate_service_url
from proxy_server.backend_services import invoke_backend_service_as_proxy
import proxy_server


#@expose_service(['GET'])
def index(request):
    #user = auth.authenticate(username='questjayjay@gmail.com', password='JayQuest', request=request)
    return  render(request, "mynaija.html")#invoke_backend_service_as_proxy('GET', generate_service_url('/get_user', params={ 'questjayjay@gmail.com' }, encrypted=True), request=request)
    ...
    

def twitter(request):
    return render(request, "twitter.html",{'tho':'yiy'})
# Create your views here.
