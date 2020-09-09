import sys
import json
import requests
from customErrors import APIError, AuthError

"""
    Desc:

    Functions:

    Optional args:

    Errors:

        FileNotFoundError
            The auth filepath defined does not exist




"""
class RegisteredBoats:
    def __init__(self,authFile="keys.json"):
        self.auth = self._loadKeys(authFile)

    def lookup(self,id):
        #confirm string
        if type(id) is not str:
            raise ValueError('Boat identifier must be a string. Received: '+str(type(id)))

        #determine boat id type
        id = id.upper()
        if id.startswith('TX'):
            return self._lookupTX(id)

        #fallback
        raise ValueError('Unsupported boat identifier: '+id)

    def _lookupTX(self,id):
        id = id[2:].replace(' ','')
        url = 'https://data.texas.gov/resource/v2f5-4wth.json'

        try:
            API_ID = self.auth['tx']['id']
            API_Secret = self.auth['tx']['secret']
        except KeyError:
            AuthError('The auth file does not have the required keys for tx (id, secret)')

        r = requests.get(
            url,
            {'tx_number': id},
            auth=(
                self.auth['tx']['id'],
                self.auth['tx']['secret']
            )
        )
        #confirm server returned json, raise error otherwise
        data = None
        try:
            data = r.json()
        except JSONDecodeError:
            raise APIError(r.status_code,r.text,API='TX')

        #confirm server responded as expected
        if r.status_code != 200 or type(data) is not list:
            raise APIError(
                r.status_code,
                data.get('message',r.text),
                API='TX'
            )
        return data



    def _loadKeys(self,authFile):
        with open(authFile) as f:
            try:
                return json.loads(f.read())
            except JSONDecodeError:
                raise AuthError("The auth file does not contian valid JSON")



RB = RegisteredBoats()
print(RB.lookup(sys.argv[1]))
