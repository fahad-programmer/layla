from emails import Email

smtp_config = {
    'sender': 'unexpectedprogrammer@gmail.com',
    'host': 'smtp.gmail.com',
    'port': 587,
    'password': 'fahadmalik123'
}
# first_attachment = {
#     'filename': 'example.png', 
#     'content': open('example.png', 'rb').read()
# }
# other_attachment = {
#     'filename': 'example.csv', 
#     'content': open('example.csv', 'rb').read()
# }
my_email = Email( 
    smtp_config, 
    subject='How are you?',
    body='Long time no see, we should get together!',
)

my_email.send('nawaz1616@gmail.com')