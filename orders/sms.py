import requests
import json

URL = 'https://www.160by2.com/api/v1/sendCampaign'

def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
    
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo, 
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)
