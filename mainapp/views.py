from django.shortcuts import render, redirect
from django.views import View
from .forms import ApplicationForm
from .models import Region, Degree, Family, Position, ComputerScience


def get_data():
    data = {
        "regions": Region.objects.all(),
        "degrees": Degree.objects.all(),
        "family": Family.objects.all(),
        "positions": Position.objects.all(),
        "computer_science": ComputerScience.objects.all(),
    }
    return data


class ApplicationView(View):
    def get(self, request):
        data = get_data()
        return render(request, 'index.html', data)

    def post(self, request):
        forma = ApplicationForm(request.POST, request.FILES)
        if forma.is_valid():
            forma.save()
            return redirect("/done/")
        data = {"message": "Ma'lumotlaringiz to'liq emas !"}
        data2 = get_data()
        data.update(data2)
        return render(request, "index.html", data)


def success_view(request):
    return render(request, "success.html")
