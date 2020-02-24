from django.shortcuts import render

# Create your views here.
def index(req):
    import json
    import requests
    if req.method=="POST":
        zipcode=req.POST['zipcode']
        url="https://api.openweathermap.org/data/2.5/weather?zip=" + zipcode + ",IN&units=metric&appid=0560deabe871665b30f19fdc26ae1019"
        api_req = requests.get(url)
        try:
            api=json.loads(api_req.content)
        except Exception as e:
            api="Error"
        icon=api['weather'][0]['icon']
        icon_url='http://openweathermap.org/img/w/{}.png'.format(icon)
        return render(req,'index.html',{'api':api,'icon_url':icon_url})
    else:
        return render(req,'index.html')
         
def about(req):
    return render(req,'about.html')
