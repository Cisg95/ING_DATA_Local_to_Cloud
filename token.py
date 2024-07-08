import json
import http.client
import urllib.parse

def authenticate(hostname, client_id, client_secret, username, password):
    """Authenticate via username/password. Returns json token object.
     
    Args:
    string hostname - hostname like "myaccount.sharefile.com"
    string client_id - OAuth2 client_id key
    string client_secret - OAuth2 client_secret key
    string username - my@user.name
    string password - my password """
 
    uri_path = '/oauth/token'
     
    headers = {'Content-Type':'application/x-www-form-urlencoded'}
    params = urllib.parse.urlencode({
        'grant_type': 'password',
        'client_id': client_id,
        'client_secret': client_secret,
        'username': username,
        'password': password
    })
     
    conn = http.client.HTTPSConnection(hostname)
    conn.request('POST', uri_path, params, headers)
    response = conn.getresponse()
     
    print(response.status, response.reason)
    token = None
    if response.status == 200:
        token = json.loads(response.read())
        print('Received token info', token)
     
    conn.close()
    return token
