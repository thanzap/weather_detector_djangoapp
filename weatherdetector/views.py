from django.shortcuts import render
import json
import urllib.request

# Create your views here.

def index(request):
    if request.method == 'POST':
        city=request.POST['city']
        res=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+ '&appid=5cc545813f580cfa9facb2454547768f').read()
        json_data=json.loads(res)
        data= {
            'country_code':str(json_data['sys']['country']),
            'coordinate': str(json_data['coord']['lon'])+' '+str(json_data['coord']['lat']),
            'temp': float(json_data['main']['temp']),
            'pressure': str(json_data['main']['pressure']),
            'humidity' : str(json_data["main"]["humidity"])
        }
        data["temp"]=round(data["temp"]- 273.10)
    else:
        data="The location doesn't exist"
    return render (request,'index.html',{'data':data})