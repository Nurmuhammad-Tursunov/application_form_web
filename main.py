import gspread
from oauth2client.service_account import ServiceAccountCredentials


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

sanoq = arizalar_sheet.get_values()
print(f"{len(sanoq)=}")