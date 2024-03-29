from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {"insert_content" : "Lads we need to add shits here"}
    return render(request,'website.html',context=my_dict)