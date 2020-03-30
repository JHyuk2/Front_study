from django.shortcuts import render
import urllib.request
import json

# Create your views here.

def index(request):
    return render(request, 'index.html')

def gallery(request):
    photo = request.GET.get('photo')
    client_id = 'kGY602VEVpAceBa61YCqSaSZqJogJ8M3HRxiZ39VpC4'
    unsplash_url = "https://api.unsplash.com/search/photos/?&query="
    json_url = unsplash_url + str(photo) + "&client_id=" + client_id 
    json_data = urllib.request.urlopen(json_url).read().decode('utf-8')
    images = json.loads(json_data)['results']
    context = {
        'images': images,   
    }
    return render(request, 'gallery.html', context)