

class APIError(Exception):
    def __init__(self,HTTPCode,error,**kwargs):
        self.error = error
        self.HTTPCode = HTTPCode
        self.API = kwargs.get('API')
    def __str__(self):
        msg = f'Server responded: {self.HTTPCode} with Error: {self.error}'
        if self.API: msg = f'{self.API} API {msg}' #prepend API host if defined
        return msg

class AuthError(Exception):
    def __init__(self,message):
        self.msg = message
    def __str__(self):
        return self.msg
