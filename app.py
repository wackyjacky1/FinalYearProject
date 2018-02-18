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

# Handles different webhooks
def processRequest(req):
    print("Request:")
    print(json.dumps(req, indent=4))

    if req.get("result").get("action") == "Page":
        data = req
        res = makeWebhookForLinks(data)
    elif req.get("result").get("action") == "Page2":
        data = req
        res = makeWebhookForAllCertificates(data)
    elif req.get("result").get("action") == "Page3":
        data = req
        res = webhookForDegree(data)
    elif req.get("result").get("action") == "Page4":
        data = req
        res = webhookForMaster(data)
    elif req.get("result").get("action") == "Page5":
        data = req
        res = webhook_for_beginner(data)
    elif req.get("result").get("action") == "GenericCert-SANS-SUMMARY":
        data = req
        res = webhook_for_sans_summary(data)
    elif req.get("result").get("action") == "GenericCert-SANS-LIST":
        data = req
        res = webhook_for_sans_course_list(data)
    elif req.get("result").get("action") == "GenericCert-SANS-FOR500":
        data = req
        res = webhook_for_sans_for500(data)
    elif req.get("result").get("action") == "GenericCert-SANS-FOR508":
        data = req
        res = webhook_for_sans_for508(data)
    elif req.get("result").get("action") == "GenericCert-SANS-FOR518":
        data = req
        res = webhook_for_sans_for518(data)
    elif req.get("result").get("action") == "GenericCert-SANS-FOR526":
        data = req
        res = webhook_for_sans_for526(data)
    elif req.get("result").get("action") == "GenericCert-SANS-FOR572":
        data = req
        res = webhook_for_sans_for572(data)
    elif req.get("result").get("action") == "GenericCert-SANS-FOR578":
        data = req
        res = webhook_for_sans_for578(data)
    elif req.get("result").get("action") == "GenericCert-SANS-FOR585":
        data = req
        res = webhook_for_sans_for585(data)
    elif req.get("result").get("action") == "GenericCert-SANS-FOR610":
        data = req
        res = webhook_for_sans_for610(data)
    else:
        return {}
    return res

# Webhook for the links to the certification pages
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

# Webhook for naming all the certifications know to the bot
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

# Webhook for users looking for Degree were computer forensic software certificates are covered
def webhookForDegree(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    degree = \
        {'Degree':
            'http://www.nuigalway.ie/courses/undergraduate-courses/computer-science-and-information-technology.html'}

    speech = "Computer Science and IT in NUI Galway cover computer forensics in Year 4. " \
             "For more info visit their website at: \n " + str(degree[name])

    print("Response")
    print(speech)
    return{
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# Webhook for Masters with computer forensics requested by user
def webhookForMaster(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    masters = \
        {'Masters':
             'http://www.ucd.ie/cci/education/prospective_students/msc_difc.html'}

    speech = "UCD have a masters programme for students with a background in computer science, " \
             "information technology, or a related discipline. " \
             "It covers all aspects of digital investigations from legislation and crime scene processing " \
             "to digital forensics, reverse engineering, and forensic reporting.  " \
             "Visit their website at: \n " + str(masters[name])

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# Webhook for General courses recommended by the system
def webhook_for_beginner(req):
    speech = "Generic/Beginner Computer forensic courses include: " \
             "\n1. SANS - For quick info type 'SANS SUMMARY'"  \
             "\n2. GCFE - For quick info type 'GCFE SUMMARY'" \
             "\n3. GCFA - For quick info type 'GCFA SUMMARY'"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# Webhook for SANS SUMMARY
def webhook_for_sans_summary(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    sans_link = {'SANS SUMMARY': 'https://digital-forensics.sans.org/about'}

    speech = "SANS provides computer forensics training via live classroom training events and online. " \
             "There are six computer forensics courses that prepare you in the disciplines of " \
             "forensics investigations, incident response, memory forensics, network forensics, " \
             "mobile device forensics, and reverse-engineering malware." \
             "\n\nHere is a link to there website:" + str(sans_link[name]) + \
             "\n\nFor a list of the courses SANS provides type 'SANS LIST'"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# webhook for SANS list of courses
def webhook_for_sans_course_list(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    sans_list = {'SANS LIST': 'https://digital-forensics.sans.org/training'}

    speech = "SANS course list on website:" + str(sans_list[name]) + \
             "\n\n 1. FOR500 - Windows Forensic Analysis" \
             "\n 2. FOR508 - Advanced Incident Response and Threat Hunting" \
             "\n 3. FOR518 - Mac Forensic Analysis" \
             "\n 4. FOR526 - In-Depth Memory Forensics" \
             "\n 5. FOR572 - Advanced Network Forensics and Analysis" \
             "\n 6. FOR578 - Cyber Threat Intelligence" \
             "\n 7. FOR585 - Advanced Smartphone Forensics" \
             "\n 8. FOR610 - Reverse engineering Malware" \
             "\n\n For more info on any of these courses type the course code i.e. 'FOR500'"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

def webhook_for_sans_for500(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    for500_link = {'FOR500': 'https://www.sans.org/course/windows-forensic-analysis'}

    speech = "FOR500: Windows Forensic Analysis will teach you to:\n\n" \
             "1. Conduct in-depth forensic analysis of Windows operating systems and media exploitation focusing " \
             "on Windows 7, Windows 8/8.1, Windows 10, and Windows Server 2008/2012/2016 \n" \
             "2. Identify artifact and evidence locations to answer critical questions, including application " \
             "execution, file access, data theft, external device usage, cloud services, geolocation, file download, " \
             "anti-forensics, and detailed system usage\n" \
             "3. Focus your capabilities on analysis instead of on how to use a particular tool\n" \
             "4. Extract critical answers and build an in-house forensic capability via a variety of free, " \
             "open-source, and commercial tools provided within the SANS Windows SIFT Workstation\n\n" \
             "For more information on " + name + " visit the website at: " + str(for500_link[name])

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

def webhook_for_sans_for508(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    for508_link = {'FOR508': 'https://www.sans.org/course/advanced-incident-response-threat-hunting-training#'
                             '__utma=71453702.1578707992.1516911150.1516911150.1517231750.2'}

    speech = "FOR508: Advanced Incident Response and Threat Hunting Course will help you to:\n\n" \
             "1. Detect how and when a breach occurred \n" \
             "2. Identify compromised and affected systems \n" \
             "3. Determine what attackers took or changed \n" \
             "4. Contain and remediate incidents \n" \
             "5. Develop key sources of threat intelligence \n" \
             "6. Hunt down additional breaches using knowledge of the adversary \n\n" \
             "For more information on " + name + " visit the website at: " + str(for508_link[name])

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

def webhook_for_sans_for518(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    for518_link = {'FOR518': 'https://www.sans.org/course/mac-forensic-analysis'}

    speech = "FOR518: Mac Forensic Analysis will teach you:\n\n" \
             "1. Mac and iOS Fundamentals: How to analyze and parse the Hierarchical File System \n" \
             "2. User Activity: How to understand and profile users through their data files \n" \
             "3. Advanced Analysis and Correlation \n" \
             "4. Apple Technologies \n\n" \
             "For more information on " + name + " visit the website at: " + str(for518_link[name])

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

def webhook_for_sans_for526(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    for526_link = {'FOR526': 'https://www.sans.org/course/memory-forensics-in-depth'}

    speech = "FOR526: An In-Depth Memory Forensics Training Course will teach you: \n\n" \
             "1. The critical skills necessary for digital forensics examiners and incident responders " \
             "to successfully perform live system memory triage and analyze captured memory images.\n\n" \
             "For more information on " + name + " visit the website at: " + str(for526_link[name])

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

def webhook_for_sans_for572(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    for572_link = {'FOR572': 'https://www.sans.org/course/advanced-network-forensics-analysis#__'
                             'utma=71453702.1578707992.1516911150.1517244707.1517316692.6'}

    speech = "FOR572: Advanced Network Forensics and Analysis Course Topics: \n\n" \
             "1. Foundational network forensics tools: tcpdump and Wireshark refresher \n" \
             "2. Packet capture applications and data \n"\
             "3. Network protocol analysis \n" \
             "4. Commercial network forensic tools \n" \
             "5. Automated tools and libraries \n" \
             "6. NetFlow \n" \
             "7. Wireless networking \n" \
             "8. Log data to supplement network examinations \n\n" \
             "For more information on " + name + " visit the website at: " + str(for572_link[name])

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

def webhook_for_sans_for578(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    for578_link = {'FOR578': 'https://www.sans.org/course/cyber-threat-intelligence#__'
                             'utma=71453702.1578707992.1516911150.1517244707.1517316692.6'}

    speech = "FOR578: A brief overview of Cyber Threat Intelligence: \n\n" \
             "1. Develop analysis skills to better comprehend complex scenarios \n" \
             "2. Identify and create intelligence requirements through practices such as threat modeling \n"\
             "3. Understand and develop skills in tactical, operational, and strategic-level threat intelligence \n" \
             "4. Generate threat intelligence to detect, respond to, and defeat focused and targeted threats \n" \
             "5. Automated tools and libraries \n" \
             "6. Validate information received externally to minimize the costs of bad intelligence \n\n" \
             "For more information on " + name + " visit the website at: " + str(for578_link[name])

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

def webhook_for_sans_for585(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    for585_link = {'FOR585': 'https://www.sans.org/course/cyber-threat-intelligence#__'
                             'utma=71453702.1578707992.1516911150.1517244707.1517316692.6'}

    speech = "FOR585: A brief overview of Advanced Smartphone Forensics: \n\n" \
             "1. Learn where key evidence is located on a smartphone \n" \
             "2. How the data got onto the smartphone \n"\
             "3. How to recover deleted mobile device data that forensic tools miss \n" \
             "4. How to decode evidence stored in third-party applications \n" \
             "5. How to detect, decompile, and analyze mobile malware and spyware \n" \
             "6. How to handle locked or encrypted devices, applications, and containers \n\n" \
             "For more information on " + name + " visit the website at: " + str(for585_link[name])

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

def webhook_for_sans_for610(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    for610_link = {'FOR610': 'https://www.sans.org/course/cyber-threat-intelligence#__'
                             'utma=71453702.1578707992.1516911150.1517244707.1517316692.6'}

    speech = "FOR610: A brief overview of Reverse engineering Malware: \n\n" \
             "1. Learn to  analyzing the code and behavior of malicious programs \n" \
             "2. Examine how malware interacts with the Windows enviroment \n"\
             "3. Uncover and analyze malicious JavaScript and other components of web pages \n" \
             "4. Control relevant aspects of the malicious program's behavior through network traffic interception \n" \
             "5. Use a disassembler and a debugger to examine the inner workings of malicious Windows executables \n" \
             "6. L injection, API hooking, and anti-analysis measures \n" \
             "Assess the threat associated with malicious documents, such as PDF and Microsoft Office files \n\n" \
             "For more information on " + name + " visit the website at: " + str(for610_link[name])

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

if __name__ == '__main__' :
    port = int(os.getenv('PORT', 80))
    print ("Starting app on port %d" %(port))
    app.run(debug=True, port=port, host='0.0.0.0')
