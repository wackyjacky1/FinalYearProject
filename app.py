#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

# Handles different intents
def processRequest(req):
    print("Request:")
    print(json.dumps(req, indent=4))

    if req.get("result").get("action") == "Page":
        data = req
        res = makeWebhookForLinks(data)
    elif req.get("result").get("action") == "Page2":
        data = req
        res = makeWebhookForAllCertificates(data)
    else:
        return {}
    return res

# intent for the links to the certification pages
def makeWebhookForLinks(req):
    result = req.get("result")
    parameters = result.get("parameters")

    # If a users asks specifically about a certification they can visit the page
    name = parameters.get("Certification-Names")
    cert = {'EnCase Certification': 'https://www.guidancesoftware.com/training/certifications#EnCE',
            'CFCE Certification': 'https://www.iacis.com/2016/02/23/cfce/',
            'ISFCE Certification': 'http://www.isfce.com/index.html'}

    speech = "For more information on " + name + " go to " + str(cert[name])

    print("Response:")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# intent for naming all the certifications know to the bot
def makeWebhookForAllCertificates(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    cert = {'Certifications': 'EnCase Certification, CFCE Certification, ISFCE Certification'}

    speech = "Here is a list of Forensic Software certificates/courses: \n" + str(cert[name])

    print("Response")
    print(speech)
    return{
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

if __name__ == '__main__' :
    port = int(os.getenv('PORT', 80))
    print ("Starting app on port %d" %(port))
    app.run(debug=True, port=port, host='0.0.0.0')
