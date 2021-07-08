import msal
import jwt
import json 
import requests 
from datetime import datetime

class Mytoken:
    """ Application Registration is required and proper scope access need to be given. 
        :param tenantid      AD Tenant ID 
        :param clientid      App Reg Clinet ID
        :param clientsecret  App Reg Secret
        """
    def __init__(self,tenantid,clientid,clientsecret):
        self._tenantid = tenantid
        self._clientid = clientid
        self._clientsecret = clientsecret
        self._graphuri = 'https://graph.microsoft.com'
        self._scope = ['https://graph.microsoft.com/.default']
        

    def msgraph_auth(self):
        authority = 'https://login.microsoftonline.com/' + self._tenantid
        app = msal.ConfidentialClientApplication(self._clientid, authority=authority, client_credential = self._clientsecret)
        try:
            accesstoken = app.acquire_token_silent(self._scope, account=None)
            # Acquire an access token for given account, without user interaction. https://msal-python.readthedocs.io/en/latest/#msal.PublicClientApplication.acquire_token_silent
            if not accesstoken:
                try:
                    accesstoken = app.acquire_token_for_client(scopes=self._scope)
                    if accesstoken['access_token']:
                        print('New Token Received!')
                        requestheaders = {'Authorization': 'Bearer ' + accesstoken['access_token']}
                        print(requestheaders)
                    else:
                        print('Error aquiring authorization token. Check your tenantID, clientid and clientsecret.')
                        print(accesstoken['error'])
                except:
                    pass 
            else:
                print('Token retreived from MSAL Cache....')

            decodedaccesstoken = jwt.decode(accesstoken['access_token'], verify=False)
            accesstokenformatted = json.dumps(decodedaccesstoken, indent=3)
            print('Decoded Access Token')
            print(accesstokenformatted)

            # Token Expiry
            tokenexpiry = datetime.fromtimestamp(int(decodedaccesstoken['exp']))
            print('Token Expires at: ' + str(tokenexpiry))
            return
        except Exception as err:
            print(err)

a = Mytoken(tenantid='xxx', clientid='xxxxx', clientsecret='xxxxx')
Mytoken.msgraph_auth(a)

