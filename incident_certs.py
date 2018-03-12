#----------------------------------------- GIAC Incident response courses --------------------------------------
def webhook_giac_incident_response(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    giac_list = {'GIAC Incident response': 'https://www.giac.org/certifications/digital-forensics'}

    speech = "Below is a list of the GIAC Incident response courses: " \
             "\n1. GCFA: Certified Forensic Analyst " \
             "\n2. GCFE: Certified Forensic Examiner " \
             "\n3. GASF: Advanced smartphone Forensics" \
             "\n\nFor more info on a certification, type and enter the code name of the certification that you are interested in" \
             " i.e. type 'GCFA' for GIAC's Certified Forensic Analyst certification" \
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

    speech = "Certified Forensic Analyst (GCFA) certification gives individuals in depth knowledge on: " \
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

# webhook for FOR508: Advanced Digital Forensics, Incident Response, and Threat Hunting
def webhook_giac_for508(req):

    speech = "FOR508: Advanced Digital Forensics, Incident Response, and Threat Hunting Training prepares individuals for GCFA certification. " \
             "The training course can be completed in 6 days" \
             "\n\n1. For course syllabus information enter 'FOR508 syllabus'" \
             "\n\n2. For laptop requirements to participate in the training course enter 'FOR508 laptop'" \
             "\n\n3. For info on who should attend this course enter 'FOR508 attend'" \
             "\n\n4. To register for FOR508 enter 'FOR508 register'" \

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# webhook for FOR508 syllabus
def webhook_giac_for508_syllabus(req):
    
    speech = "---FOR508 Syllabus---" \
             "\nDay 1: Advanced Incident Response & Threat Hunting" \
             "\nDay 2: Memory Forensics" \
             "\nDay 3: Intrusion Forensics" \
             "\nDay 4: Timeline Analysis" \
             "\nDay 5: Incident Response & Hunting Across the Enterprise" \
             "\nDay 6: The APT Incident Response Challenge" \
             "\n\n1. For laptop requirements to participate in the training course enter 'FOR508 laptop'" \
             "\n\n2. For info on who should attend this course enter 'FOR508 attend'" \
             "\n\n3. To register for FOR508 enter 'FOR508 register'" \
             "\n\nOr visit their website at: https://www.sans.org/course/advanced-incident-response-threat-hunting-training#__utma=183869984.18323172.1519689563.1519733474.1519733474.4"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }


# webhook for Certified Forensic Examiner (GCFE)
def webhook_giac_gcfe(req):

    speech = "Certified Forensic Examiner (GCFE) certification gives individuals in depth knowledge on: " \
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

# webhook for FOR500: Windows Forensic Analysis
def webhook_giac_for500(req):

    speech = "FOR500: Windows Forensic Analysis Training prepares individuals for GCFE certification. " \
             "The training course can be completed in 6 days" \
             "\n\n1. For course syllabus information enter 'FOR500 syllabus'" \
             "\n\n2. For laptop requirements to participate in the training course enter 'FOR500 laptop'" \
             "\n\n3. For info on who should attend this course enter 'FOR500 attend'" \
             "\n\n4. To register for FOR500 enter 'FOR500 register'" \

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# webhook for FOR500 syllabus
def webhook_giac_for500_syllabus(req):
    
    speech = "---FOR500 Syllabus---" \
             "\nDay 1: Windows Digital Forensics" \
             "\nDay 2: Core Windows Forensics" \
             "\nDay 3: Core Windows Forensics" \
             "\nDay 4: Core Windows Forensics" \
             "\nDay 5: Core Windows Forensics" \
             "\nDay 6: Core Windows Forensics" \
             "\n\n1. For laptop requirements to participate in the training course enter 'FOR500 laptop'" \
             "\n\n2. For info on who should attend this course enter 'FOR500 attend'" \
             "\n\n3. To register for FOR500 enter 'FOR500 register'" \
             "\n\nOr visit their website at:https://www.sans.org/course/windows-forensic-analysis#__utma=183869984.18323172.1519689563.1519733474.1519733474.4"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# webhook for Advanced Smartphone Forensics (GASF)
def webhook_giac_gasf(req):

    speech = "Advanced Smartphone Forensics (GASF) certification gives individuals in depth knowledge on: " \
             "\n1. Mobile forensics" \
             "\n2. Device file system analysis" \
             "\n3. Smartphone application behavior" \
             "\n4. Artifact analysis and the identification and analysis of smart device malware." \
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

# webhook for FOR585: Advanced Smartphone Forensics
def webhook_giac_for585(req):

    speech = "FOR585: Advanced Smartphone Forensics Training prepares individuals for GASF certification. " \
             "The training course can be completed in 6 days" \
             "\n\n1. For course syllabus information enter 'FOR585 syllabus'" \
             "\n\n2. For laptop requirements to participate in the training course enter 'FOR585 laptop'" \
             "\n\n3. For info on who should attend this course enter 'FOR585 attend'" \
             "\n\n4. To register for FOR585 enter 'FOR585 register'" \

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# webhook for FOR585 syllabus
def webhook_giac_for585_syllabus(req):
    
    speech = "---FOR585 Syllabus---" \
             "\nDay 1: Malware Forensics, Smartphone Overview, and SQLite Introduction" \
             "\nDay 2: Android Forensics" \
             "\nDay 3: Android Backups and iOS Device Forensics" \
             "\nDay 4: iOS Backups, Windows, and BlackBerry 10 Forensics" \
             "\nDay 5: Third-Party Application and Knock-Off Forensics" \
             "\nDay 6: Smartphone Forensic Capstone Exercise" \
             "\n\n1. For laptop requirements to participate in the training course enter 'FOR585 laptop'" \
             "\n\n2. For info on who should attend this course enter 'FOR585 attend'" \
             "\n\n3. To register for FOR585 enter 'FOR585 register'" \
             "\n\nOr visit their website at: https://www.sans.org/course/advanced-smartphone-mobile-device-forensics#__utma=183869984.18323172.1519689563.1519733474.1519744377.5"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }