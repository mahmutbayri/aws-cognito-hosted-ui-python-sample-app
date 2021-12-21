import os
import re
import boto3

def getAccessTokenFromCookie(cookies):
    cookie = None
    pattern = 'CognitoIdentityServiceProvider.' + os.getenv('CLIENT_ID') + '.+.accessToken'

    for value in cookies:
        if re.search(pattern, value):
            cookie = cookies[value]

    return cookie

def getUser(accessToken):
    if accessToken is None:
        return None
    return getClient().get_user(AccessToken=accessToken)

def getClient():
    return boto3.client(
        'cognito-idp',
        region_name=os.getenv('REGION')
    )

def getenv(value):
  return os.getenv(value)
