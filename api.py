import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script

data = {'input1': {'columnAttributes': [{'name': 'winery', 'type': 'String', 'isFeature': True, 'elementType': {'typeName': 'str', 'isNullable': False}}, 
                                        {'name': 'wine', 'type': 'String', 'isFeature': True, 'elementType': {'typeName': 'str', 'isNullable': False}\nData: b'{}'\nTraceback (most recent call last):\n  File \"/azureml-envs/azureml_1cb18400c65045b04f876961ed2a6d0a/lib/python3.8/site-packages/azureml/designer/serving/dagengine/processor.py\", line 18, in run\n    webservice_input, global_parameters = self.pre_process(raw_data)\n  File \"/azureml-envs/azureml_1cb18400c65045b04f876961ed2a6d0a/lib/python3.8/site-packages/azureml/designer/serving/dagengine/processor.py\", line 46, in pre_process\n    all_inputs = json_data['Inputs']\nKeyError: 'Inputs'\n", "details": ""}}

body = str.encode(json.dumps(data))

url = 'http://977f160c-117a-4a0b-a6ea-f0d843821893.eastus2.azurecontainer.io/score'
# Replace this with the primary/secondary key, AMLToken, or Microsoft Entra ID token for the endpoint
api_key = 'apJb6ZuVTApkqYKV3tfGNdgaUoq4mJb8'
if not api_key:
    raise Exception("A key should be provided to invoke the endpoint")


headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))