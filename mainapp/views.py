from datetime import datetime

from django.shortcuts import render, redirect
from django.views import View
from .forms import ApplicationForm
from .models import Region, Degree, Family, Position, ComputerScience, Application
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from twilio.rest import Client


key = {
  "type": "service_account",
  "project_id": "applicationsform",
  "private_key_id": "b3e47dfe799f2d7403b07862ca575939e0441c8b",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDBTcqkew31aUl3\n5PCX9sIW3+d2DXH2xyZ5gTjOTShL+o8in+iq/56dBxBBZZzgHufY8dxNqd5i0tX6\nxT+Zgycti6y7dmHKTMWQc+jQ2RNw9dYhiUK7rC82sUmLz7xVcpsAQynrq4H1ovsE\nU6uqWa7N1oUQGbKC2TIQvU6bCcUKiiU11lI6H1fkRpL/FJTRLROY19CvBg/Qqpkp\nERWet2shnvaPP4kOoSiSmHjyhIpPN5qHRfk+Zk9cdxDSxytXxm6ilG4u+VBj6jlp\nZToilsm7OgPOQTG3jNOVaPmduzxBy2dLISAccxGZInaJCeANGOgIEEHktCdYau6e\nPjBrWVghAgMBAAECggEAAhwvexr3LKRvYqyptHvDSjnVezEFLnSlrRJF19948iNh\nDp3nDbIB13FgfwyoT4kzoYDT+9EMr9CtxbGdH4R4yzZI6dIoAFJVBPeoi418rD3/\njjKP+1NGcxCXK4lWYyrMgFs7VbdzxFLfVJopN8NudUOQBK+TIEe74SzmP8Q1vDpM\njMP3lYnJNBtm4liQ7giv0HXKde2X0ymAQJ7klFV2z8fA5M/f6nMn2+4N+k3fCQmW\ny5ajN5XvTpHU8G4VOb7qpGY5flvgoVHF7nymLslW5nL1qRaM7mHYXDKCYY+FlBsD\n75t/Wdhzpb3BaOA8r6ezEuIboH/keIvTP2s61IZccQKBgQDx/886rSWvoDzLmR20\n683C32uMTAVu/2Dkd9hE43ggcyBDuFEKI5goYREtRoggA2AI990tekYUnNR8eZfa\nqh8ywuiA7Vl88lrODyS46T2btrXu6GgcQ2o8CUC7xbExz+HKzDK7U9gpkzBhbJxF\nuaAdPrSgDOgCoC7VwhXBSNOyRQKBgQDMfMRWNPT0YZgPV9jukUYI0S6IMOKoa3kB\n3vlDOzIkhRG+u3XtzfPrsb0BQWc3g/Fkn5JyXnHIxj3FtVthoTiX8NL4SKX8GHTZ\nZzZ11Pc+RIxYJ6/agWI8o/bwT3MyTHwGevumEwkES5Shu0sMhCS5i3U22HhrRbDm\nGi4SCmgaLQKBgHZeYcaZmq1k+1e69UThciu3jKt7I80/LO2TkT1g5gk5RrbZGQqU\njoBxui0jKsI95GN+mbj87fp3G5gnAZf7TndNztwBPJxZDwFrdtLbgz7/B85r70Cj\n2Pq0q+0srZdnz1Gav9XRFRKA5FFDBs00FpU3brI6neFq6H22CV4ZeTLhAoGBAMZD\nOkGzOsUvUrWdoRE9/T9TQeB+NWTCPyMXQ2pyHJ3X/2qEa0TUaOle/TgYZ7El1oiP\nRvhopb3ap83nluBD5pE6x/I+zeBs/e5D6kO45reS0tguMoyS4eKVvzkkbzaXfbDy\n0McmsZleho+A/rT18n2Lv2wb2jV37ppLS9vmByVJAoGBAJj/pRbzK50r1WpK1d/E\n7m6wThi2Rs0Dt/Kz/JdOE6363Yu6IaFSY34u4uI0IB2h+8j/pVWAIURpBxXW0xWi\nacRaqkIkGQz4wovpRVhikS7orf1bHfn39oxH85xMLt1i0CT/jCTwmCOiyrFcgiC4\ncm4K1A4hXF6e2bWMvBjG4m8q\n-----END PRIVATE KEY-----\n",
  "client_email": "applicationsform@applicationsform.iam.gserviceaccount.com",
  "client_id": "116769189539274419042",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/applicationsform%40applicationsform.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_dict(keyfile_dict=key)

file = gspread.authorize(creds)

workbook = file.open("ApplicationForm")
arizalar_sheet = workbook.worksheet("Arizalar")
elon_lavozimlari_sheet = workbook.worksheet("elon_lavozimlari")


def get_data():
    elon_lavozimlari_sheet_data = elon_lavozimlari_sheet.get_values()[1:]
    Position.objects.filter(deleted=False).update(deleted=True)
    for position in elon_lavozimlari_sheet_data:
        if not Position.objects.filter(name=position[0]).exists():
            Position.objects.create(
                name=position[0]
            )
        elif Position.objects.filter(name=position[0]).exists():
            Position.objects.filter(name=position[0]).update(deleted=False)
    data = {
        "regions": Region.objects.all(),
        "degrees": Degree.objects.all(),
        "family": Family.objects.all(),
        "positions": Position.objects.filter(deleted=False),
        "computer_science": ComputerScience.objects.all(),
    }
    return data


class ApplicationView(View):
    def get(self, request):
        data = get_data()
        return render(request, 'index2.html', data)

    def post(self, request):
        forma = ApplicationForm(request.POST, request.FILES)
        # # forma = ApplicationForm()
        #
        # if forma.is_valid():
        #     if Application.objects.filter(
        #             first_name=forma.cleaned_data.get('first_name'),
        #             last_name=forma.cleaned_data.get('last_name'),
        #             phone_number=forma.cleaned_data.get('phone_number'),
        #     ).exists():
        #         data = {"message": "Siz avval ro'yxatdan o'tgansiz !"}
        #         return redirect("/false/")
        #     else:
        #         # forma.save()
        #         application = Application.objects.all().last()
        #         data = arizalar_sheet.get_values()
        #         sanoq = len(data) + 1
        #         arizalar_sheet.update(f"A{sanoq}:M{sanoq}", [
        #             [
        #                 sanoq - 1,
        #                 f"{application.last_name} {application.first_name}",
        #                 f"{application.phone_number}",
        #                 f"{application.city}" if application.city else "-",
        #                 f"{application.date_of_birth}" if application.date_of_birth else "-",
        #                 f"{application.appeal if application.appeal is not None else '-'}",
        #                 f"{application.position}",
        #                 f"{application.degree}",
        #                 f"{application.address}" if application.address else "-",
        #                 f"{application.language_ru}",
        #                 f"{application.computer_science}",
        #                 f"https://applicationform.pythonanywhere.com{application.photo.url}" if application.photo else "-",
        #                 f"{str(application.date_time)[:19]}"
        #             ]
        #         ])
        #
        #         return redirect("/done/")
        # else:
        #     data = {"message": f"Ma'lumotlaringiz to'liq emas !{forma.errors}"}
        # data2 = get_data()
        # data.update(data2)
        # return render(request, "index2.html", data)

        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone_number = request.POST.get("phone_number")
        city = request.POST.get("city")
        date_of_birth = request.POST.get("date_of_birth")
        appeal = request.POST.get("appeal")
        position = request.POST.get("position")
        degree = request.POST.get("degree")
        address = request.POST.get("address")
        language_ru = request.POST.get("language_ru")
        computer_science = request.POST.get("computer_science")
        photo = request.POST.get("photo")

        # if last_name and first_name and phone_number:
        if forma.is_valid():
            forma.save()
            application = Application.objects.all().last()
            data = arizalar_sheet.get_values()
            sanoq = len(data) + 1
            arizalar_sheet.update(f"A{sanoq}:M{sanoq}", [
                [
                    sanoq - 1,
                    f"{last_name} {first_name}",
                    f"{phone_number}",
                    f"{city}" if city else "-",
                    f"{date_of_birth}" if date_of_birth else "-",
                    f"{appeal if appeal else '-'}",
                    f"{position}",
                    f"{degree}",
                    f"{address}" if address else "-",
                    f"{language_ru}",
                    f"{computer_science}",
                    f"https://applicationform.pythonanywhere.com{application.photo.url}" if application.photo else "-",
                    f"{str(datetime.today())[:19]}"
                ]
            ])

            return redirect("/done/")
        else:
            data = {"message": f"Ma'lumotlaringiz to'liq emas !{str(request.POST.get('photo'))}"}
        data2 = get_data()
        data.update(data2)
        return render(request, "index2.html", data)


def success_view(request):
    return render(request, "success.html")


def main_page_view(request):
    return render(request, "index.html")

def false_page_view(request):
    return render(request, "false_page.html")
