import msal
import jwt
import json 
import requests 
import pandas as pd 
from datetime import datetime

accessToken = None 
requestHeaders = None 
tokenExpiry = None 
queryResults = None 
graphURI = 'https://graph.microsoft.com'

def msgraph_auth():
    global accessToken
    global requestHeaders
    global tokenExpiry
    tenantID = 'ceb41c7f-15aa-47b2-b4ec-19b9aec82c1a'
    authority = 'https://login.microsoftonline.com/' + tenantID
    clientID = '696b01f7-6499-44f9-bdd5-91e94cf343a2'
    clientSecret = 'Q7mYoFv-7lvC1C0XD3n_~Yg_Y_PwAtODHJ'
    scope = ['https://graph.microsoft.com/.default']

    app = msal.ConfidentialClientApplication(clientID, authority=authority, client_credential = clientSecret)

    try:
        accessToken = app.acquire_token_silent(scope, account=None)
        if not accessToken:
            try:
                accessToken = app.acquire_token_for_client(scopes=scope)
                if accessToken['access_token']:
                    print('New access token retreived....')
                    #print(accessToken['access_token'])
                    requestHeaders = {'Authorization': 'Bearer ' + accessToken['access_token']}
                else:
                    print('Error aquiring authorization token. Check your tenantID, clientID and clientSecret.')
            except:
                pass 
        else:
            print('Token retreived from MSAL Cache....')
        decodedAccessToken = jwt.decode(accessToken['access_token'], verify=False, algorithms=['RS256'])
        accessTokenFormatted = json.dumps(decodedAccessToken, indent=2)
        print('Decoded Access Token')
        print(accessTokenFormatted)

        # Token Expiry
        tokenExpiry = datetime.fromtimestamp(int(decodedAccessToken['exp']))
        print('Token Expires at: ' + str(tokenExpiry))
        return
    except Exception as err:
        print(err)

def msgraph_request(resource,requestHeaders):
    # Request
    results = requests.get(resource, headers=requestHeaders).json()
    return results


# Auth
msgraph_auth()

# Query
queryResults = msgraph_request(graphURI +'/v1.0/users',requestHeaders)


# Results to Dataframe
try:
    df = pd.read_json(json.dumps(queryResults['value']))
    # set ID column as index
    df = df.set_index('id')
    #print(df)
    print(str(df['displayName'] + " " + df['userPrincipalName']))

except:
    print(json.dumps(queryResults, indent=2))