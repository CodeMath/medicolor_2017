from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    if request.method == "POST":
        name = request.POST.get("name")
        num = request.POST.get("num")
        context = {
            "name":name,
            "num":num
        }
        return render(request, 'web/output.html', context)
    return render(request, 'web/index.html', context)