from twilio.rest import Client


client = Client("AC5ae6814d7179967d4180648505607d9b", "5c7e866617032a235636f54ccbff4a19")
msg = f"Ariza qoldirildi\n\n" \
      f"F.I.Sh - N.T\n" \
      f"Tel. - 123456789\n\n\n" \
      f"Havola - https://applicationform.pythonanywhere.com/admin/"
client.messages.create(
    body=msg,
    from_="+15097745886",
    to=f"+998880729933"
)