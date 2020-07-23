from django.http import HttpResponse
def disp(request):
    with open('mysite/one.txt','r') as f:
        data = f.read()
        return HttpResponse("<h1>"+data+"</h1>")
