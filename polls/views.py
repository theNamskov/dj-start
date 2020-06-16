from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")

def more_info(request):
	return HttpResponse("<h1>Over here we are starting with django and we gonna build a polls app. Stay tuned...</h1>")
