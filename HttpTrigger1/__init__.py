import logging
import requests 
import json
import time
import http.client, urllib.request, urllib.parse, urllib.error, base64
from github import Github
from pprint import pprint
import os

import azure.functions as func



GITHUB_TOKEN="9f41be5df3f57a1dc80bd37b42129abe704de5b5"

def githubPush(name):
    token = GITHUB_TOKEN
    g = Github(token)
    repo = g.get_repo("adityaoberai/GarudaHacks-Project")
    file_path = 'submission.java'
    message = 'submission'
    branch = 'master'
    def push(path, message, branch, update=False):
        author = InputGitAuthor(
        "eKuG",
        "ekanshgupta.eku@gmail.com"
    )
    source = repo.get_branch("master")

    push(file_path, "Converted Image to Text", "master", update=True)

def CodeCapture2(image_url, name):

    subscription_key = '3f5be862da834a4b8cda49032b5cd676'
    headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '{subscription_key}',
}

    params = urllib.parse.urlencode({
    # Request parameters
    'language': '{en}',
})
    body = {'url': image_url}
    # try:
    conn = http.client.HTTPSConnection('centralindia.api.cognitive.microsoft.com')
    response = conn.request("POST", "/vision/v3.0/read/analyze?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    logging.info('Image processing +++++++++++++++++++++++++++++')
    with open('submission.java', 'wb') as mycode:
        mycode.write(data)
    conn.close()
    # except Exception as e:
    #     logging.info('[Errno {0}] {1}'.format(e.errno, e.strerror))

    githubPush(name)

def CodeCapture(name):
    if(name == 'cpp'):
        image_url = "https://github.com/adityaoberai/GarudaHacks-Project/blob/master/cpp.jpeg"
        CodeCapture2(image_url, name)
        logging.info('Image Sent')
    if(name == 'java'):
        image_url = "https://raw.githubusercontent.com/adityaoberai/GarudaHacks-Project/master/java.jpeg"
        CodeCapture2(image_url,name)
        logging.info('Image Sent')
    if(name == 'python'):
        image_url = "https://github.com/adityaoberai/GarudaHacks-Project/blob/master/python.jpeg"
        CodeCapture2(image_url, name)
        logging.info('Image Sent')
    if(name == 'txt'):
        image_url = "https://github.com/adityaoberai/GarudaHacks-Project/blob/master/txt.jpeg"
        CodeCapture2(image_url, name)
        logging.info('Image Sent')
    else:
        logging.info('Http request either not made or is incorrect')


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(CodeCapture(name))
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )
