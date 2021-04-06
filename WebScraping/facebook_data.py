#pip install facebook-py-sdk

from facebook_sdk.exceptions import FacebookResponseException
from facebook_sdk.facebook import Facebook

facebook = Facebook(
    app_id='266461301634567',
    app_secret='124c2cc15b0a417bc1c32757288f6bd6',
    default_graph_version='v10.0',
)

facebook.set_default_access_token(access_token='EAADyWFs69gcBAKZBcxqcBmwaIgVWC4Y2THTfQfKZA3QnydAE45zS8GFPHxhsX6IzYe1amo3GkZAdCGh50tqd1rQiz5KScQYGMkdwZBmnl38FIBnCiNOUiVp3PSaIBCZAYm7SndVCIYaEwlrzbnYxV4I3tMkNneq2xbuOwT4SNzcKy10Q7Lz8PkdcgY99OsaEM1mkOakUebVUShr49IofDJmjZCB4OM4DX8ZBr9PQzkxjgZDZD')

try:
    response = facebook.get(endpoint='/me?fields=id,name,birthday,email,location')
except FacebookResponseException as e:
    print(e.message)
else:
    print('User id: %(name)s' % {'name': response.json_body.get('id')})
    print('User name: %(name)s' % {'name': response.json_body.get('name')})
    print('BirthDay: %(name)s' % {'name': response.json_body.get('birthday')})
    print('email: %(name)s' % {'name': response.json_body.get('email')})
    print('location: %(name)s' % {'name': response.json_body.get('location')})