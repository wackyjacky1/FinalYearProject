#!/usr/bin/env python
import urllib
import json
import os

import cce
import defense_certs
import management
import incident_certs
import pentest_certs
import cd_certs

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
    elif req.get("result").get("action") == "degree":
        data = req
        res = webhookForDegree(data)
    elif req.get("result").get("action") == "masters":
        data = req
        res = webhookForMaster(data)
    elif req.get("result").get("action") == "beginner":
        data = req
        res = webhook_for_beginner(data)
    elif req.get("result").get("action") == "experienced":
        data = req
        res = webhook_for_experienced(data)
    elif req.get("result").get("action") == "GIAC-info":
        data = req
        res = webhook_giac_summary(data)
    elif req.get("result").get("action") == "GIAC-cat":
        data = req
        res = webhook_giac_cat(data)
    elif req.get("result").get("action") == "cce-info":
        data = req
        res = cce.webhook_cce_info(data)

    # Statements for CCE certification
    elif req.get("result").get("action") == "cce-training":
        data = req
        res = cce.webhook_cce_training(data)
    elif req.get("result").get("action") == "cce-requirements":
        data = req
        res = cce.webhook_cce_requirements(data)
    elif req.get("result").get("action") == "cce-software":
        data = req
        res = cce.webhook_cce_software(data)
    elif req.get("result").get("action") == "cce-fees":
        data = req
        res = cce.webhook_cce_fees(data)
    elif req.get("result").get("action") == "cce-application":
        data = req
        res = cce.webhook_cce_application(data)
    elif req.get("result").get("action") == "cce-testing":
        data = req
        res = cce.webhook_cce_testing(data)

    # Statements for Cyber Defense certifications and training courses need to obtain certification
    elif req.get("result").get("action") == "GIAC-cyber-defense":
        data = req
        res = cd_certs.webhook_giac_cyber_defense(data)
    elif req.get("result").get("action") == "GIAC-gsec":
        data = req
        res = cd_certs.webhook_giac_gsec(data)
    elif req.get("result").get("action") == "GIAC-sec401":
        data = req
        res = cd_certs.webhook_giac_sec401(data)
    elif req.get("result").get("action") == "GIAC-sec401-syllabus":
        data = req
        res = cd_certs.webhook_giac_sec401_syllabus(data)
    elif req.get("result").get("action") == "GIAC-laptop":
        data = req
        res = cd_certs.webhook_giac_laptop(data)
    elif req.get("result").get("action") == "GIAC-attend":
        data = req
        res = cd_certs.webhook_giac_attend(data)
    elif req.get("result").get("action") == "GIAC-register":
        data = req
        res = cd_certs.webhook_giac_register(data)
    elif req.get("result").get("action") == "GIAC-gcia":
        data = req
        res = cd_certs.webhook_giac_gcia(data)
    elif req.get("result").get("action") == "GIAC-sec503-syllabus":
        data = req
        res = cd_certs.webhook_giac_sec503_syllabus(data)
    elif req.get("result").get("action") == "GIAC-gisf":
        data = req
        res = cd_certs.webhook_giac_gisf(data)
    elif req.get("result").get("action") == "GIAC-sec301":
        data = req
        res = cd_certs.webhook_giac_sec301(data)
    elif req.get("result").get("action") == "GIAC-sec301-syllabus":
        data = req
        res = cd_certs.webhook_giac_sec301_syllabus(data)
    elif req.get("result").get("action") == "GIAC-gced":
        data = req
        res = cd_certs.webhook_giac_gced(data)
    elif req.get("result").get("action") == "GIAC-sec501":
        data = req
        res = cd_certs.webhook_giac_sec501(data)
    elif req.get("result").get("action") == "GIAC-sec501-syllabus":
        data = req
        res = cd_certs.webhook_giac_sec501_syllabus(data)
    elif req.get("result").get("action") == "GIAC-gcwn":
        data = req
        res = cd_certs.webhook_giac_gcwn(data)
    elif req.get("result").get("action") == "GIAC-sec505":
        data = req
        res = cd_certs.webhook_giac_sec505(data)
    elif req.get("result").get("action") == "GIAC-sec505-syllabus":
        data = req
        res = cd_certs.webhook_giac_sec505_syllabus(data)
    elif req.get("result").get("action") == "GIAC-gmon":
        data = req
        res = cd_certs.webhook_giac_gmon(data)
    elif req.get("result").get("action") == "GIAC-sec511":
        data = req
        res = cd_certs.webhook_giac_sec511(data)
    elif req.get("result").get("action") == "GIAC-sec511-syllabus":
        data = req
        res = cd_certs.webhook_giac_sec511_syllabus(data)
    
    # Statements for Penetration Tester certifications and training courses need to obtain certification
    elif req.get("result").get("action") == "GIAC-pen-tester":
        data = req
        res = pentest_certs.webhook_giac_pen_tester(data)
    elif req.get("result").get("action") == "GIAC-gcih":
        data = req
        res = pentest_certs.webhook_giac_gcih(data)
    elif req.get("result").get("action") == "GIAC-sec504":
        data = req
        res = pentest_certs.webhook_giac_sec504(data)
    elif req.get("result").get("action") == "GIAC-sec504-syllabus":
        data = req
        res = pentest_certs.webhook_giac_sec504_syllabus(data)
    elif req.get("result").get("action") == "GIAC-gpen":
        data = req
        res = pentest_certs.webhook_giac_gpen(data)
    elif req.get("result").get("action") == "GIAC-sec560":
        data = req
        res = pentest_certs.webhook_giac_sec560(data)
    elif req.get("result").get("action") == "GIAC-sec560-syllabus":
        data = req
        res = pentest_certs.webhook_giac_sec560_syllabus(data)
    elif req.get("result").get("action") == "GIAC-gwapt":
        data = req
        res = pentest_certs.webhook_giac_gwapt(data)
    elif req.get("result").get("action") == "GIAC-sec542":
        data = req
        res = pentest_certs.webhook_giac_sec542(data)
    elif req.get("result").get("action") == "GIAC-sec542-syllabus":
        data = req
        res = pentest_certs.webhook_giac_sec542_syllabus(data)
    elif req.get("result").get("action") == "GIAC-gxpn":
        data = req
        res = pentest_certs.webhook_giac_gxpn(data)
    elif req.get("result").get("action") == "GIAC-sec660":
        data = req
        res = pentest_certs.webhook_giac_sec660(data)
    elif req.get("result").get("action") == "GIAC-sec660-syllabus":
        data = req
        res = pentest_certs.webhook_giac_sec660_syllabus(data)
    elif req.get("result").get("action") == "GIAC-gawn":
        data = req
        res = pentest_certs.webhook_giac_gawn(data)
    elif req.get("result").get("action") == "GIAC-sec617":
        data = req
        res = pentest_certs.webhook_giac_sec617(data)
    elif req.get("result").get("action") == "GIAC-sec617-syllabus":
        data = req
        res = pentest_certs.webhook_giac_sec617_syllabus(data)


    # Statements for Incident response certifications and training courses need to obtain certification
    elif req.get("result").get("action") == "GIAC-Incident-response":
        data = req
        res = incident_certs.webhook_giac_incident_response(data)
    elif req.get("result").get("action") == "GIAC-gcfa":
        data = req
        res = incident_certs.webhook_giac_gcfa(data)
    elif req.get("result").get("action") == "GIAC-for508":
        data = req
        res = incident_certs.webhook_giac_for508(data)
    elif req.get("result").get("action") == "GIAC-for508-syllabus":
        data = req
        res = incident_certs.webhook_giac_for508_syllabus(data)
    elif req.get("result").get("action") == "GIAC-gcfe":
        data = req
        res = incident_certs.webhook_giac_gcfe(data)
    elif req.get("result").get("action") == "GIAC-for500":
        data = req
        res = incident_certs.webhook_giac_for500(data)
    elif req.get("result").get("action") == "GIAC-for500-syllabus":
        data = req
        res = incident_certs.webhook_giac_for500_syllabus(data)
    elif req.get("result").get("action") == "GIAC-gasf":
        data = req
        res = incident_certs.webhook_giac_gasf(data)
    elif req.get("result").get("action") == "GIAC-for585":
        data = req
        res = incident_certs.webhook_giac_for585(data)
    elif req.get("result").get("action") == "GIAC-for585-syllabus":
        data = req
        res = incident_certs.webhook_giac_for585_syllabus(data)

    # Statements for Management certifications and training courses need to obtain certification
    elif req.get("result").get("action") == "GIAC-management":
        data = req
        res = management.webhook_giac_management(data)
    elif req.get("result").get("action") == "GIAC-gslc":
        data = req
        res = management.webhook_giac_gslc(data)
    elif req.get("result").get("action") == "GIAC-mgt512":
        data = req
        res = management.webhook_giac_mgt512(data)
    elif req.get("result").get("action") == "GIAC-mgt512-syllabus":
        data = req
        res = management.webhook_giac_mgt512_syllabus(data)
    elif req.get("result").get("action") == "GIAC-gsna":
        data = req
        res = management.webhook_giac_gsna(data)
    elif req.get("result").get("action") == "GIAC-aud507":
        data = req
        res = management.webhook_giac_aud507(data)
    elif req.get("result").get("action") == "GIAC-aud507-syllabus":
        data = req
        res = management.webhook_giac_aud507_syllabus(data)
    elif req.get("result").get("action") == "GIAC-gisp":
        data = req
        res = management.webhook_giac_gisp(data)
    elif req.get("result").get("action") == "GIAC-mgt414":
        data = req
        res = management.webhook_giac_mgt414(data)
    elif req.get("result").get("action") == "GIAC-mgt414-syllabus":
        data = req
        res = management.webhook_giac_mgt414_syllabus(data)
    elif req.get("result").get("action") == "GIAC-gleg":
        data = req
        res = management.webhook_giac_gleg(data)
    elif req.get("result").get("action") == "GIAC-leg523":
        data = req
        res = management.webhook_giac_leg523(data)
    elif req.get("result").get("action") == "GIAC-leg523-syllabus":
        data = req
        res = management.webhook_giac_leg523_syllabus(data)

   
    elif req.get("result").get("action") == "GIAC-mg414":
        data = req
        res = webhook_giac_mg414(data)
    elif req.get("result").get("action") == "GIAC-leg523":
        data = req
        res = webhook_giac_leg523(data)
    elif req.get("result").get("action") == "GIAC-mgt525":
        data = req
        res = webhook_giac_mgt525(data)
    
    elif req.get("result").get("action") == "GIAC-gcti":
        data = req
        res = webhook_giac_gcti(data)
    

    # Statements for Industrial defense certifications and training courses need to obtain certification
    elif req.get("result").get("action") == "GIAC-industrial-defense":
        data = req
        res = defense_certs.webhook_giac_industrial_defense(data)
    elif req.get("result").get("action") == "GIAC-gicsp":
        data = req
        res = defense_certs.webhook_giac_ics410(data)
    elif req.get("result").get("action") == "GIAC-ICS410":
        data = req
        res = defense_certs.webhook_giac_ics410_syllabus(data)
    elif req.get("result").get("action") == "GIAC-ICS410-syllabus":
        data = req
        res = defense_certs.webhook_giac_gicsp(data)
    elif req.get("result").get("action") == "GIAC-grid":
        data = req
        res = defense_certs.webhook_giac_grid(data)
    elif req.get("result").get("action") == "GIAC-ICS515":
        data = req
        res = defense_certs.webhook_giac_ics515(data)
    elif req.get("result").get("action") == "GIAC-ICS515-syllabus":
        data = req
        res = defense_certs.webhook_giac_ics515_syllabus(data)
    elif req.get("result").get("action") == "GIAC-gcip":
        data = req
        res = defense_certs.webhook_giac_gcip(data)
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
    speech = "For individuals who are new to computer forensics, perhaps have a look at completing a degree or masters " \
             "in Computer Forensics. For more info enter 'degree' or 'masters'" \
             "\n\nAnother options for beginners is to get GIAC certification.  GIAC certifictaion is considered one of the "  \
             "highest certifications possible with regard to computer forensics that a beginner can obtain." \
             "\nFor more info on GIAC certifications type 'giac info'" \
             

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# Webhook for experienced computer forensic examiners looking for certification
def webhook_for_experienced(req):

    speech = "More advanced computer forensic analysts should look at obtaining Certified Computer Examiner (CCE) certification. " \
             "For more info on CCE certification enter 'CCE info'."
             
    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }


# ------------------------------------ GIAC SUMMARY -------------------------------------------
def webhook_giac_summary(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    giac_link = {'GIAC info': 'https://www.giac.org/certification/certified-forensic-examiner-gcfe'}

    speech = "GIAC is for professionals working or interested in information " \
             "security, legal and law enforcement industries with a need to understand computer forensic analysis. " \
             "The certification focuses on skills required to collect and analyze data from Windows computer " \
             "systems." \
             "\n\nNo entry requirements are necessary to apply for any GIAC certifications. " \
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
             "\n3. Incident Response" \
             "\n4. Management/Audit/Legal" \
             "\n5. Industrial Defence" \
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


if __name__ == '__main__' :
    port = int(os.getenv('PORT', 443))
    print ("Starting app on port %d" %(port))
    app.run(debug=True, port=port, host='0.0.0.0')
