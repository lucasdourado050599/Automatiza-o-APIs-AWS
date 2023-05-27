import requests
import json
from datetime import date, timedelta, datetime
from aws_requests_auth.aws_auth import AWSRequestsAuth

###Pega DATA atual###
data_started = date.today() - timedelta(days=1)
data_ended = date.today() - timedelta(days=0)

###Consulta API AWS####
print("Iniciando Script....")
print("Consultando API AWS")

url = "https://ce.us-east-1.amazonaws.com"
headers = {
        'X-Amz-Target': 'AWSInsightsIndexService.GetCostAndUsage',
        'Content-Type': 'application/x-amz-json-1.1',        
        }

body = {  
              
    "TimePeriod": {
    "Start":f"{data_started}",
    "End":f"{data_ended}"
  },
  "Granularity": "DAILY",
  "GroupBy":[
    {
      "Type":"DIMENSION",
      "Key":"LINKED_ACCOUNT"
    },
    {
      "Type":"DIMENSION",
      "Key":"SERVICE"
    }
  ],
   "Metrics":["BlendedCost", "UnblendedCost", "UsageQuantity"]
}

###Autenticação AWS###
auth = AWSRequestsAuth(aws_access_key='access_key',
                       aws_secret_access_key='secret_access_key',
                       aws_host='ce.us-east-1.amazonaws.com',
                       aws_region='us-east-1',
                       aws_service='ce')

response = requests.post(url=url,headers=headers,json=body,auth=auth)


if response.status_code >= 200 and response.status_code <= 299:
        # Sucesso
        print('Suceso, status code:', response.status_code)
        print('Retorno API:', response.json())
       
else:
        # Erros
        print('Status code', response.status_code)
        print('Reason', response.reason)
        
###Fim Consulta AWS ###
