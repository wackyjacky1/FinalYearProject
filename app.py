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
        res = webhook_beginner_advanced(data)
    elif req.get("result").get("action") == "Page3":
        data = req
        res = webhookForDegree(data)
    elif req.get("result").get("action") == "Page4":
        data = req
        res = webhookForMaster(data)
    elif req.get("result").get("action") == "beginner":
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
    elif req.get("result").get("action") == "GIAC-info":
        data = req
        res = webhook_giac_summary(data)
    elif req.get("result").get("action") == "GIAC-cat":
        data = req
        res = webhook_giac_cat(data)
    elif req.get("result").get("action") == "GIAC-cyber-defense":
        data = req
        res = webhook_giac_cyber_defense(data)
    elif req.get("result").get("action") == "GIAC-gsec":
        data = req
        res = webhook_giac_gsec(data)
    elif req.get("result").get("action") == "GIAC-gcia":
        data = req
        res = webhook_giac_gcia(data)
    elif req.get("result").get("action") == "GIAC-gisf":
        data = req
        res = webhook_giac_gisf(data)
    elif req.get("result").get("action") == "GIAC-gced":
        data = req
        res = webhook_giac_gced(data)
    elif req.get("result").get("action") == "GIAC-gcwn":
        data = req
        res = webhook_giac_gcwn(data)
    elif req.get("result").get("action") == "GIAC-gmon":
        data = req
        res = webhook_giac_gmon(data)
    elif req.get("result").get("action") == "GIAC-pen-tester":
        data = req
        res = webhook_giac_pen_tester(data)
    elif req.get("result").get("action") == "GIAC-gcih":
        data = req
        res = webhook_giac_gcih(data)
    elif req.get("result").get("action") == "GIAC-gpen":
        data = req
        res = webhook_giac_gpen(data)
    elif req.get("result").get("action") == "GIAC-gwapt":
        data = req
        res = webhook_giac_gwapt(data)
    elif req.get("result").get("action") == "GIAC-gxpn":
        data = req
        res = webhook_giac_gxpn(data)
    elif req.get("result").get("action") == "GIAC-gawn":
        data = req
        res = webhook_giac_gawn(data)
    elif req.get("result").get("action") == "GIAC-gmob":
        data = req
        res = webhook_giac_gmob(data)
    elif req.get("result").get("action") == "GIAC-Incident-response":
        data = req
        res = webhook_giac_incident_response(data)
    elif req.get("result").get("action") == "GIAC-management":
        data = req
        res = webhook_giac_management(data)
    elif req.get("result").get("action") == "GIAC-mgt512":
        data = req
        res = webhook_giac_mgt512(data)
    elif req.get("result").get("action") == "GIAC-aud507":
        data = req
        res = webhook_giac_aud507(data)
    elif req.get("result").get("action") == "GIAC-mg414":
        data = req
        res = webhook_giac_mg414(data)
    elif req.get("result").get("action") == "GIAC-leg523":
        data = req
        res = webhook_giac_leg523(data)
    elif req.get("result").get("action") == "GIAC-mgt525":
        data = req
        res = webhook_giac_mgt525(data)
    elif req.get("result").get("action") == "GIAC-mgt414":
        data = req
        res = webhook_giac_mgt414(data)
    elif req.get("result").get("action") == "GIAC-gcfa":
        data = req
        res = webhook_giac_gcfa(data)
    elif req.get("result").get("action") == "GIAC-gcfe":
        data = req
        res = webhook_giac_gcfe(data)
    elif req.get("result").get("action") == "GIAC-grem":
        data = req
        res = webhook_giac_grem(data)
    elif req.get("result").get("action") == "GIAC-gnfa":
        data = req
        res = webhook_giac_gnfa(data)
    elif req.get("result").get("action") == "GIAC-gasf":
        data = req
        res = webhook_giac_gasf(data)
    elif req.get("result").get("action") == "GIAC-gcti":
        data = req
        res = webhook_giac_gcti(data)
    elif req.get("result").get("action") == "GIAC-gslc":
        data = req
        res = webhook_giac_gslc(data)
    elif req.get("result").get("action") == "GIAC-gsna":
        data = req
        res = webhook_giac_gsna(data)
    elif req.get("result").get("action") == "GIAC-gisp":
        data = req
        res = webhook_giac_gisp(data)
    elif req.get("result").get("action") == "GIAC-gleg":
        data = req
        res = webhook_giac_gleg(data)
    elif req.get("result").get("action") == "GIAC-gcpm":
        data = req
        res = webhook_giac_gcpm(data)
    elif req.get("result").get("action") == "GIAC-gstrt":
        data = req
        res = webhook_giac_gstrt(data)
    elif req.get("result").get("action") == "GIAC-industrial-defense":
        data = req
        res = webhook_giac_industrial_defense(data)
    elif req.get("result").get("action") == "GIAC-gicsp":
        data = req
        res = webhook_giac_gicsp(data)
    elif req.get("result").get("action") == "GIAC-grid":
        data = req
        res = webhook_giac_grid(data)
    elif req.get("result").get("action") == "GIAC-gcip":
        data = req
        res = webhook_giac_gcip(data)
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

# Webhook for beginner or advanced forensics course
def webhook_beginner_advanced(req):
    speech = "Are you looking for a beginners course of a more advanced course?"

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
    speech = "Generic/Beginner Computer forensic bodies include: " \
             "\n\n1.  GIAC - For more info type 'GIAC info'"  \
             "\n\n2.  SANS - For more info type 'SANS info'" \
             

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

#-------------------------------------------------- GIAC -------------------------------------------------------------#

# GIAC SUMMARY
def webhook_giac_summary(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    giac_link = {'GIAC info': 'https://www.giac.org/certification/certified-forensic-examiner-gcfe'}

    speech = "GIAC is for professionals working or interested in information " \
             "security, legal and law enforcement industries with a need to understand computer forensic analysis. " \
             "The certification focuses on skills required to collect and analyze data from Windows computer " \
             "systems." \
             "\n\nGIAC offers a variety of certifications. " \
             "For a list of the certification categories GIAC offers type 'GIAC cat'" \
             "\n\nOr visit their website at: " + str(giac_link[name])

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# GIAC categories of courses
def webhook_giac_cat(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    giac_list = {'GIAC cat': 'https://www.giac.org/certifications/categories'}

    speech = "GIAC offer a range of computer forensic certifications in each category (Below 1-5)." \
             "\n\n1. Cyber Defense" \
             "\n2. Penetration Testing" \
             "\n3. Incident Response and Forensics" \
             "\n4. Management, Audit, Legal" \
             "\n5. Industrial Control Systems" \
             "\n\nType and enter the category name that you are interested in" \
             " to view the list of certifications in that category " \
             "i.e. 'Penetration Testing'" \
             "\n\nOr if you prefer, visit the GIAC certification categories on their website at: " + str(giac_list[name])


    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

#---------------------------- GIAC cyber defense courses --------------------------------------
def webhook_giac_cyber_defense(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    giac_list = {'GIAC Cyber Defense': 'https://www.giac.org/certifications/categories'}

    speech = "Below is a list of the GIAC Cyber Defense certifications: " \
             "\n\n 1. GSEC: Security Essentials" \
             "\n 2. GCIA: Certified Intrustion Analyst" \
             "\n 3. GISF: Information Security Fundamentals" \
             "\n 4. GCED: Certified Enterprise Defender" \
             "\n 5. GCWN: Certified Windows Security Administrator" \
             "\n 6. GMON: Continuos Monitoring Certification" \
             "\n\nFor more information on any of the certifications, enter the certification code" \
             " i.e. type 'GSEC' for more info on GIAC's Security Essentials cert." \
             "\n\nOr if you prefer, here is a link to the GIAC Cyber Defense certs: " + str(giac_list[name]) 

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# webhook for GSEC Security Essentials certification
def webhook_giac_gsec(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    giac_list = {'GSEC ': 'https://www.giac.org/certification/security-essentials-gsec'}

    speech = "After receiving Security Essentials (GSEC) certification users should: " \
             "\n1. be able to prevent attacks and detect network adversaries" \
             "\n2. have in-depth knowlegde of Networks, Defense and Secure communications" \
             "\n3. have foundational linux skills" \
             "\nInfo at:  https://www.giac.org/certification/security-essentials-gsec" \
             "\n\nHowever in order to obtain Security Essentials (GSEC) certification one " \
             "must complete appropriate training: " \
             "\n\nSEC401: Security Essentials Bootcamp Style Training" \
             "\n\nFor more info on SEC401 Training type and enter the course code 'SEC401'" 

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# webhook for gcia
def webhook_giac_gcia(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    giac_list = {'GCIA ': 'https://www.giac.org/certification/certified-intrusion-analyst-gcia'}

    speech = "After receiving Certified Intrusion Analyst  (GCIA) certification users should: " \
             "\n1. be able to understand fundamentals of Traffic Analysis" \
             "\n2. understand open source IDS: Snort and Bro" \
             "\n3. have in depth knowledge of Network Traffic Forensics and Monitoring" \
             "\nInfo at:  https://www.giac.org/certification/certified-intrusion-analyst-gcia" \
             "\n\nHowever in order to obtain Intrusion Analyst  (GCIA) certification one " \
             "must complete appropriate training: " \
             "\n\nSEC503: Intrusion Detection In-Depth Training" \
             "\n\nFor more info on SEC503 Training type and enter the course code 'SEC503'" 

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# webhook for gisf
def webhook_giac_gisf(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    gisf_list = {'GISF ': 'https://www.giac.org/certification/information-security-fundamentals-gisf'}

    speech = "After receiving Information Security Fundamentals (GISF) certification users should have in depth knowledge on: " \
             "\n1. Information Security Foundations" \
             "\n2. Cryptography" \
             "\n3. Network Protection Strategies and Host Protection" \
             "\nInfo at:  https://www.giac.org/certification/information-security-fundamentals-gisf" \
             "\n\nHowever in order to obtain Information Security Fundamentals (GISF) certification one " \
             "must complete appropriate training: " \
             "\n\nSEC301: Intro to Information Security" \
             "\n\nFor more info on SEC301 Training type and enter the course code 'SEC301'"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# webhook for gced
def webhook_giac_gced(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    gisf_list = {'GCED ': 'https://www.giac.org/certification/certified-enterprise-defender-gced'}

    speech = "After receiving Certified Enterprise Defender (GCED) certification users should have in depth knowledge on: " \
             "\n1. Defensive Network Infrastructure and Packet Analysis" \
             "\n2. Pen Testing and Vulnerability Analysis and Mitigation" \
             "\n3. Incident Response, Malware and Data Loss Prevention" \
             "\nInfo at:  https://www.giac.org/certification/certified-enterprise-defender-gced" \
             "\n\nHowever in order to obtain Certified Enterprise Defender (GCED) certification one " \
             "must complete appropriate training: " \
             "\n\nSEC501: Advanced Security Essentials - Enterprise Defender" \
             "\n\nFor more info on SEC501 Training type and enter the course code 'SEC501'"
    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# webhook for gcwn
def webhook_giac_gcwn(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    gisf_list = {'GCWN ': 'https://www.giac.org/certification/certified-windows-security-administrator-gcwn'}

    speech = "After receiving Certified Windows Security Administrator (GCWN) certification users should have in depth knowledge on: " \
             "\n1. Windows OS and Application Hardening" \
             "\n2. PowerShell Scripting and Managing Cryptography" \
             "\n3. Server Hardening, IPSec, Dynamic Access Control and DNS" \
             "\nInfo at:  https://www.giac.org/certification/certified-windows-security-administrator-gcwn" \
             "\n\nHowever in order to obtain Certified Windows Security Administrator (GCWN) certification one " \
             "must complete appropriate training: " \
             "\n\nSEC505: Securing Windows and PowerShell Automation" \
             "\n\nFor more info on SEC505 Training type and enter the course code 'SEC505'"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# webhook for gmon
def webhook_giac_gmon(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    gisf_list = {'GMON ': 'https://www.giac.org/certification/continuous-monitoring-certification-gmon'}

    speech = "After receiving Continuous Monitoring Certification (GMON) certification users should have in depth knowledge on: " \
             "\n1. Security Architecture and Security Operations Centers (SOCs)" \
             "\n2. Network Security Architecture and Monitoring" \
             "\n3. Endpoint Security Architecture, Automation and Continuous Monitoring" \
             "\nInfo at:  https://www.giac.org/certification/continuous-monitoring-certification-gmon" \
             "\n\nHowever in order to obtain Continuous Monitoring Certification (GMON) certification one " \
             "must complete appropriate training: " \
             "\n\nSEC511: Continuous Monitoring and Security Operations" \
             "\n\nFor more info on SEC511 Training type and enter the course code 'SEC511'"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

#--------------------------------------------- GIAC Penetration testing ----------------------------------------#
# webhook for giac pen tester courses
def webhook_giac_pen_tester(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    giac_list = {'GIAC Penetration Tester': 'https://www.giac.org/certifications/pen-testing'}

    speech = "Below is a list of the GIAC Penetration Testing Courses available: " \
             "\n\n1. GCIH: Certified Incident Handler" \
             "\n2. GPEN: Penetration Tester" \
             "\n3. GWAPT: Web Application Penetration Tester" \
             "\n4. GXPN: Exploit Researcher and Advanced Penetration Tester" \
             "\n5. GAWN: Assessing and Auditing Wireless Networks" \
             "\n6. GMOB: Mobile Device Security Analyst" \
             "\n\nFor more information on any of the courses, enter the course code" \
             " i.e. type 'GCIH' for more info on GIAC's Certified Incident Handler Course" \
             "\n\nOr if you would prefer, here is a link to the GIAC Penetration Testing Courses: " + str(giac_list[name]) 

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# webhook for Certified Incident Handler (GCIH)
def webhook_giac_gcih(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    gisf_list = {'GCIH ': 'https://www.giac.org/certification/certified-incident-handler-gcih'}

    speech = "After receiving Certified Incident Handler (GCIH) certification users should have in depth knowledge on: " \
             "\n1. the steps of the incident handling process" \
             "\n2. detecting malicious applications and network activity" \
             "\n3. common attack techniques that compromise hosts" \
             "\n4. detecting and analyzing system and network vulnerabilities" \
             "\nInfo at: https://www.giac.org/certification/certified-incident-handler-gcih" \
             "\n\nto obtain Certified Incident Handler (GCIH) certification, the below training must be completed: " \
             "\n\nSEC504: Hacker Tools, Techniques, Exploits Training" \
             "\n\nFor info on SEC504 training type the course code 'SEC504'"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# webhook for Penetration Tester (GPEN)
def webhook_giac_gpen(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    gisf_list = {'GPEN ': 'https://www.giac.org/certification/penetration-tester-gpen'}

    speech = "After receiving Penetration Tester (GPEN) certification users should have in depth knowledge on: " \
             "\n1. ethical hacking methodologies" \
             "\n2. conducting a penetration test" \
             "\nInfo at: https: https://www.giac.org/certification/penetration-tester-gpen" \
             "\n\nTo obtain Penetration Tester (GPEN) certification, the below training must be completed: " \
             "\n\nSEC560: Network Penetration Testing and Ethical Hacking" \
             "\n\nFor info on SEC560 training type the course code 'SEC560'"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# webhook for Web Application Penetration Tester (GWAPT)
def webhook_giac_gwapt(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    gisf_list = {'GWAPT ': 'https://www.giac.org/certification/web-application-penetration-tester-gwapt'}

    speech = "After receiving Web Application Penetration Tester (GWAPT) certification users should have in depth knowledge on: " \
             "\n1. est and defend web applications and the vulnerabilities associated with them." \
             "\n\nInfo at: https://www.giac.org/certification/web-application-penetration-tester-gwapt" \
             "\n\nTo obtain Web Application Penetration Tester (GWAPT) certification, the below training must be completed: " \
             "\n\nSEC542: Web App Penetration Testing and Ethical Hacking" \
             "\n\nFor info on SEC542 training type the course code 'SEC542'"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# webhook for Exploit Researcher and Advanced Penetration Tester (GXPN)
def webhook_giac_gxpn(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    gisf_list = {'GXPN ': 'https://www.giac.org/certification/exploit-researcher-advanced-penetration-tester-gxpn'}

    speech = "After receiving Exploit Researcher and Advanced Penetration Tester (GXPN) certification users should have in depth knowledge on: " \
             "\n1.conducting advanced penetration testing and ethical hacking." \
             "\n2.modelling the abilities of an advanced attacker to find significant security flaws in systems." \
             "\n\nInfo at: https://www.giac.org/certification/exploit-researcher-advanced-penetration-tester-gxpn" \
             "\n\nTo obtain GXPN certification, the below training must be completed: " \
             "\n\nSEC660: Advanced Penetration Testing, Exploit Writing, and Ethical Hacking" \
             "\n\nFor info on SEC660 training type the course code 'SEC660'"
    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# webhook for Assessing and Auditing Wireless Networks (GAWN)
def webhook_giac_gawn(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    gisf_list = {'GAWN ': 'https://www.giac.org/certification/assessing-auditing-wireless-networks-gawn'}

    speech = "After receiving Assessing and Auditing Wireless Networks (GAWN) certification users should have in depth knowledge on: " \
             "\n1.security mechanisms for wireless networks." \
             "\n2.tools and techniques used to evaluate and exploit weaknesses." \
             "\n3.techniques used to analyze wireless networks." \
             "\n\nInfo at: https://www.giac.org/certification/assessing-auditing-wireless-networks-gawn" \
             "\n\nTo obtain GAWN certification, the below training must be completed: " \
             "\n\nSEC617: Wireless Penetration Testing and Ethical Hacking" \
             "\n\nFor info on SEC617 training type the course code 'SEC617'"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# webhook for Mobile Device Security Analyst (GMOB)
def webhook_giac_gmob(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    gisf_list = {'GMOB ': 'https://www.giac.org/certification/mobile-device-security-analyst-gmob'}

    speech = "After receiving Mobile Device Security Analyst (GMOB) certification users should have in depth knowledge on: " \
             "\n1.protect systems and networks." \
             "\n2.properly securing the mobile devices accessing vital information." \
             "\n\nInfo at: https://www.giac.org/certification/mobile-device-security-analyst-gmob" \
             "\n\nTo obtain GMOB certification, the below training must be completed: " \
             "\n\nSEC575: Mobile Device Security and Ethical Hacking" \
             "\n\nFor info on SEC575 training type the course code 'SEC575'"
    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

#----------------------------------------- GIAC Incident response courses --------------------------------------
def webhook_giac_incident_response(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    giac_list = {'GIAC Incident response': 'https://www.giac.org/certifications/digital-forensics'}

    speech = "Below is a list of the GIAC Incident response courses: " \
             "\n1. GCFA: Certified Forensic Analyst " \
             "\n2. GCFE: Certified Forensic Examiner " \
             "\n3. GREM: Reverse Engineering Malware " \
             "\n4. GNFA: Network Forensic Analyst " \
             "\n5. GASF: Advanced smartphone Forensics" \
             "\n6. GCTI: Cyber Threat Intelligence" \
             "\n\nFor more info on a course, type and enter the code name of the course that you are interested in" \
             " i.e. type 'GCFA' for GIAC's Certified Forensic Analyst Course" \
             "\n\nOr if you prefer, here is a link to the GIAC Incident response courses: " + str(giac_list[name]) 

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# webhook for Certified Forensic Analyst (GCFA)
def webhook_giac_gcfa(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    gisf_list = {'GCFA ': 'https://www.giac.org/certification/certified-forensic-analyst-gcfa'}

    speech = "After receiving Certified Forensic Analyst (GCFA) certification users should have in depth knowledge on: " \
             "\n1. Collecting and analyzing data from Windows computer systems." \
             "\n2. Handling advanced incident handling scenarios." \
             "\n\nInfo at: https://www.giac.org/certification/certified-forensic-analyst-gcfa" \
             "\n\nTo obtain GCFA certification, the below training must be completed: " \
             "\n\nFOR508: Advanced Digital Forensics, Incident Response, and Threat Hunting" \
             "\n\nFor info on FOR508 training type the course code 'FOR508'"
    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# webhook for Certified Forensic Examiner (GCFE)
def webhook_giac_gcfe(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    gisf_list = {'GCFE ': 'https://www.giac.org/certification/certified-forensic-analyst-gcfe'}

    speech = "After receiving Certified Forensic Examiner (GCFE) certification users should have in depth knowledge on: " \
             "\n1. Conducting deep-dive incident investigations including forensic analysis and reporting, " \
             "evidence acquisition, browser forensics and tracing user and application activities on Windows systems.." \
             "\n\nInfo at: https://www.giac.org/certification/certified-forensic-analyst-gcfe" \
             "\n\nTo obtain GCFE certification, the below training must be completed: " \
             "\n\nFOR500: Windows Forensic Analysis" \
             "\n\nFor info on FOR500 training type the course code 'FOR500'"
    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# webhook for Reverse Engineering Malware (GREM)
def webhook_giac_grem(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    gisf_list = {'GREM ': 'https://www.giac.org/certification/reverse-engineering-malware-grem'}

    speech = "After receiving Reverse Engineering Malware (GREM) certification users should have in depth knowledge on: " \
             "\n1. analyzing and reverse-engineer malicious software that targets common platforms." \
             "\n\nInfo at: https://www.giac.org/certification/reverse-engineering-malware-grem" \
             "\n\nTo obtain GREM certification, the below training must be completed: " \
             "\n\nFOR610: Reverse-Engineering Malware: Malware Analysis Tools and Techniques" \
             "\n\nFor info on FOR610 training type the course code 'FOR610'"
    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# webhook for Network Forensic Analyst (GNFA)
def webhook_giac_gnfa(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    gisf_list = {'GNFA ': 'https://www.giac.org/certification/network-forensic-analyst-gnfa'}

    speech = "After receiving Network Forensic Analyst (GNFA) certification users should have in depth knowledge on: " \
             "\n1. the fundamentals of network forensics" \
             "\n2. conditions for common network protocols" \
             "\n3. the process and tools used to examine device and system logs" \
             "\n4. wireless communication and encrypted protocols." \
             "\n\nInfo at: https://www.giac.org/certification/network-forensic-analyst-gnfa" \
             "\n\nTo obtain GNFA certification, the below training must be completed: " \
             "\n\nFOR572: Advanced Network Forensics: Threat Hunting, Analysis, and Incident Response" \
             "\n\nFor info on FOR572 training type the course code 'FOR572'"
    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# webhook for Advanced Smartphone Forensics (GASF)
def webhook_giac_gasf(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    gisf_list = {'GASF ': 'https://www.giac.org/certification/advanced-smartphone-forensics-gasf'}

    speech = "After receiving Advanced Smartphone Forensics (GASF) certification users should have in depth knowledge on: " \
             "\n1. mobile forensics" \
             "\n2. device file system analysis" \
             "\n3. smartphone application behavior" \
             "\n4. artifact analysis and the identification and analysis of smart device malware." \
             "\n\nInfo at: https://www.giac.org/certification/advanced-smartphone-forensics-gasf" \
             "\n\nTo obtain GASF certification, the below training must be completed: " \
             "\n\nFOR585: Advanced Smartphone Forensics" \
             "\n\nFor info on FOR585 training type the course code 'FOR585'"
    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# webhook for Cyber Threat Intelligence (GCTI)
def webhook_giac_gcti(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    gisf_list = {'GCTI ': 'https://www.giac.org/certification/advanced-smartphone-forensics-gasf'}

    speech = "After receiving Cyber Threat Intelligence (GCTI) certification users should have in depth knowledge on: " \
             "\n1. Strategic, Operational, and Tactical Cyber Threat Intelligence" \
             "\n2. Open Source Intelligence and Campaigns" \
             "\n3. Intelligence Applications and Kill Chain" \
             "\n4. artifact analysis and the identification and analysis of smart device malware." \
             "\n\nInfo at: https://www.giac.org/certification/advanced-smartphone-forensics-gasf" \
             "\n\nTo obtain GCTI certification, the below training must be completed: " \
             "\n\nFOR578: Cyber Threat Intelligence" \
             "\n\nFor info on FOR578 training type the course code 'FOR578'"
    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }
#---------------------------------- GIAC Management, Audit, Legal ---------------------------------------
def webhook_giac_management(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    giac_list = {'GIAC management': 'https://www.giac.org/certifications/management'}

    speech = "Here is a list of the GIAC Management, Audit, Legal certificate: " \
             "\n1. GSLC: Security Leadership" \
             "\n2. GSNA: Systems and Network Auditor" \
             "\n3. GISP: Information Security Professional" \
             "\n4. GLEG: Law of Data Security & Investigations" \
             "\n5. GCPM: Certified Project Manager" \
             "\n6. GSTRT: Strategic Planning, Policy, and Leadership" \
             "\n\nFor more info on a course, type and enter the code name of the course that you are interested in" \
             " i.e. type 'GSLC' for GIAC's Security Leadership certificate" \
             "\n\nHere is a link to the GIAC Management, Audit, Legal certificate website: " + str(giac_list[name]) 

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# webhook for Security Leadership (GSLC)
def webhook_giac_gslc(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    gisf_list = {'GSLC ': 'https://www.giac.org/certification/security-leadership-gslc'}

    speech = "After receiving Security Leadership (GSLC) certification users should have in depth knowledge on: " \
             "\n1. risks of 802.11 wireless networks and how to secure them" \
             "\n2. access control and password management" \
             "\n3. building a security awareness program" \
             "\n4. cryptography applications, VPNs and IPSec." \
             "\n\nInfo at: https://www.giac.org/certification/security-leadership-gslc" \
             "\n\nTo obtain GSLC certification, the below training must be completed: " \
             "\n\nMGT512: SANS Security Leadership Essentials For Managers with Knowledge Compression" \
             "\n\nFor info on MGT512 training type the course code 'MGT512'"
    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# GIAC - SANS Security Leadership Essentials (MGT512)
def webhook_giac_mgt512(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    gisf_list = {'MGT512 ': 'https://www.sans.org/course/security-strategic-planning-policy-leadership#__utma=183869984.1578707992.1516911150.1519227651.1519229972.14'}

    speech = "Info on MGT512"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# webhook for Systems and Network Auditor (GSNA)
def webhook_giac_gsna(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    gisf_list = {'GSNA ': 'https://www.giac.org/certification/systems-and-network-auditor-gsna'}

    speech = "After receiving Systems and Network Auditor (GSNA) certification users should have: " \
             "\n1. basic knowledge of risk analysis techniques and be able to conduct a technical audit of essential information systems." \
             "\n\nInfo at: https:https://www.giac.org/certification/systems-and-network-auditor-gsna" \
             "\n\nTo obtain GSNA certification, the below training must be completed: " \
             "\n\nAUD507: Auditing & Monitoring Networks, Perimeters & Systems" \
             "\n\nFor info on AUD507 training type the course code 'AUD507'"
    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# GIAC - Auditing & Monitoring Networks, Perimeters & Systems (AUD507)
def webhook_giac_aud507(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    gisf_list = {'AUD507 ': 'https://www.sans.org/course/auditing-networks-perimeters-systems#__utma=183869984.1578707992.1516911150.1519227651.1519229972.14'}
    speech = "Info on AUD507"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# webhook for Information Security Professional (GISP)
def webhook_giac_gisp(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    gisf_list = {'GISP ': 'https://www.giac.org/certification/information-security-professional-gisp'}

    speech = "After receiving Information Security Professional (GISP) certification users should have: " \
             "\n1. an understanding of technical information security; System, Security " \
             "\n\nInfo at: https://www.giac.org/certification/information-security-professional-gisp" \
             "\n\nTo obtain GISP certification, the below training must be completed: " \
             "\n\nMGT414: SANS Training Program for CISSP Certification" \
             "\n\nFor info on MG414 training type the course code 'MG414'"
    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# GIAC - SANS Training Program for CISSP Certification (MG414)
def webhook_giac_mg414(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    gisf_list = {'MG414 ': 'https://www.sans.org/course/auditing-networks-perimeters-systems#__utma=183869984.1578707992.1516911150.1519227651.1519229972.14'}
    speech = "Info on MG414"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

    # webhook for Law of Data Security & Investigations (GLEG)
def webhook_giac_gleg(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    gisf_list = {'GLEG ': 'https://www.giac.org/certification/law-data-security-investigations-gleg'}

    speech = "GLEG certification holders have the knowledge, skills," \
             "and abilities to manage security relationship to business law, contracts," \
             "fraud, crime, IT security, IT liability and IT policy with a focus on electronically stored and transmitted records " \
             "\n\nInfo at: https://www.giac.org/certification/law-data-security-investigations-gleg" \
             "\n\nTo obtain GLEG certification, the below training must be completed: " \
             "\n\nLEG523: Law of Data Security and Investigations" \
             "\n\nFor info on LEG523 training type the course code 'LEG523'"
    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# GIAC - Law of Data Security and Investigations (LEG523)
def webhook_giac_leg523(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    gisf_list = {'LEG523 ': 'https://www.sans.org/course/law-data-security-investigations#__utma=183869984.1578707992.1516911150.1519227651.1519229972.14'}
    speech = "Info on LEG5234"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# webhook for Certified Project Manager (GCPM)
def webhook_giac_gcpm(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    gisf_list = {'GCPM ': 'https://www.giac.org/certification/certified-project-manager-gcpm'}

    speech = "GCPM certification holders have knowledge, skills, " \
             "and abilities critical to making projects successful, including effective communication, " \
             "time, cost, quality, procurement and risk management of IT projects " \
             "and application development" \
             "\n\nInfo at: https://www.giac.org/certification/certified-project-manager-gcpm" \
             "\n\nTo obtain GCPM certification, the below training must be completed: " \
             "\n\nMGT525: IT Project Management, Effective Communication, and PMP Exam Prep" \
             "\n\nFor info on MGT525 training type the course code 'MGT525'"
    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# GIAC - IT Project Management, Effective Communication, and PMP Exam Prep (MGT525)
def webhook_giac_mgt525(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    gisf_list = {'MGT525 ': 'https://www.sans.org/course/project-management-effective-communication-pmp-exam-prep#__utma=183869984.1578707992.1516911150.1519139371.1519227651.13'}
    speech = "Info on MGT525"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

    # webhook for Strategic Planning, Policy, and Leadership (GSTRT)
def webhook_giac_gstrt(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    gisf_list = {'GSTRT ': 'https://www.giac.org/certification/strategic-planning-policy-leadership-gstrt'}

    speech = "GSTRT certification is for CISOs, Information Security Officers, Security Directors and Managers " \
             "developing or maintaining cyber security programs and technical cyber " \
             "security professionals wanting to learn proven business analysis, strategic planning, and management tools" \
             "\n\nInfo at: https://www.giac.org/certification/strategic-planning-policy-leadership-gstrt" \
             "\n\nTo obtain GSTRT certification, the below training must be completed: " \
             "\n\nMGT514: Security Strategic Planning, Policy, and Leadership" \
             "\n\nFor info on MGT514 training type the course code 'MGT514'"
    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# GIAC - SANS Training Program for CISSP Certification (MGT414)
def webhook_giac_mgt414(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    gisf_list = {'MGT414 ': 'https://www.sans.org/course/sans-plus-s-training-program-cissp-certification-exam#__utma=183869984.1578707992.1516911150.1519227651.1519229972.14'}
    speech = "Info on MGT414"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

#---------------------------- GIAC industrial defense certifications --------------------------------------
def webhook_giac_industrial_defense(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    giac_list = {'GIAC industrial defense': 'https://www.giac.org/certifications/ics'}

    speech = "Below is a list of the GIAC industrial defense certifications: " \
             "\n\n1. GICSP: Global Industrial Cyber Security" \
             "\n2. GRID: Response and Industrial Defense" \
             "\n3. GCIP: Critical Infrastructure Protection" \
             "\n\nFor more information on any of the certifications, enter the certification code" \
             " i.e. type 'GCISP' for more info on GIAC's Global Industrial Cyber Security Professional cert." \
             "\n\nOr if you prefer, here is a link to the GIAC industrial defense certifications: https://www.giac.org/certifications/ics"  

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

 # webhook for Global Industrial Cyber Security Professional (GICSP)
def webhook_giac_gicsp(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    gisf_list = {'GICSP ': 'https://www.giac.org/certification/global-industrial-cyber-security-professional-gicsp'}

    speech = "After receiving Global Industrial Cyber Security Professional (GICSP) certification users should have in depth knowledge in: " \
             "\n1. Hardening Linux/Unix " \
             "\n2. Application Security in Depth" \
             "\n3. Digital Forensics in the Linux/Unix Environment" \
             "\n\nInfo at: https://www.giac.org/certification/global-industrial-cyber-security-professional-gicsp" \
             "\n\nTo obtain GICSP certification, the below training must be completed: " \
             "\n\nICS410: ICS/SCADA Security Essentials" \
             "\n\nFor info on ICS410 training type the course code 'ICS410'"
    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# webhook for Response and Industrial Defense (GRID)
def webhook_giac_grid(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    gisf_list = {'GRID ': 'https://www.giac.org/certification/response-industrial-defense-grid'}

    speech = "After receiving Response and Industrial Defense (GRID) certification users should have in depth knowledge in: " \
             "\n1. Overview and application of Active Defense and Threat Intelligence " \
             "\n2. Industrial Control Systems (ICS/SCADA) Digital Forensics, Incident Response, and Threat Analysis" \
             "\n3. Monitoring and Detection ICS/SCADA networks and systems" \
             "\n\nInfo at: https://www.giac.org/certification/response-industrial-defense-grid" \
             "\n\nTo obtain GRID certification, the below training must be completed: " \
             "\n\nICS515: ICS Active Defense and Incident Response" \
             "\n\nFor info on ICS515 training type the course code 'ICS515'"
    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# webhook for Critical Infrastructure Protection (GCIP)
def webhook_giac_gcip(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    gisf_list = {'GCIP ': 'https://www.giac.org/certification/critical-infrastructure-protection-gcip'}

    speech = "After receiving Critical Infrastructure Protection (GCIP) certification users should have in depth knowledge in: " \
             "\n1. BES Cyber System identification and strategies for lowering their impact rating " \
             "\n2. Nuances of NERC defined terms and CIP standards applicability" \
             "\n3. Strategic implementation approaches for supporting technologies" \
             "\n\nInfo at: https://www.giac.org/certification/critical-infrastructure-protection-gcip" \
             "\n\nTo obtain GCIP certification, the below training must be completed: " \
             "\n\nICS456: Essentials for NERC Critical Infrastructure Protection" \
             "\n\nFor info on ICS456 training type the course code 'ICS456'"
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
