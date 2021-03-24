from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'MyApp/base.html')

def index(request):
    context_dict = {'text':'hello world','number':100}
    return render(request, 'MyApp/index.html',context_dict)

def other(request):
    return render(request, 'MyApp/other.html')

def relative(request):
    return render(request, 'MyApp/relative_url_template.html')