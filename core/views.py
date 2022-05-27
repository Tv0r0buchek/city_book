from django.shortcuts import render

def main(request):
    cities = ["Москва","Санкт-Петербург", "Астрахань", "Лондон"]
    print(request.path)
    path = request.path
    path = path.replace("/","")
    if path =="":
        path = "index"
    path = path + ".html"
    return render(request,path,{'cities_for_html': cities})


