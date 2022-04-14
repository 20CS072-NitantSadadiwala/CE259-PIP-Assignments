from django.core.mail import EmailMessage

msg = EmailMessage('Subject of the Email', 'Body of the email', 'from@email.com', ['to@email.com'])
msg.content_subtype = "html"  
msg.attach_file('pdfs/Instructions.pdf')
msg.send()