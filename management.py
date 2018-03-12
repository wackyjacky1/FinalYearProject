#-------------------------------------------------- GIAC Management, Audit, Legal ---------------------------------------
def webhook_giac_management(req):
    result = req.get("result")
    parameters = result.get("parameters")

    name = parameters.get("Certification-Names")
    giac_list = {'GIAC management': 'https://www.giac.org/certifications/management'}

    speech = "Below is a list of the GIAC Management, Audit, Legal certificates: " \
             "\n1. GSLC: Security Leadership" \
             "\n2. GSNA: Systems and Network Auditor" \
             "\n3. GISP: Information Security Professional" \
             "\n4. GLEG: Law of Data Security & Investigations" \
             "\n\nFor more info on a certification, type and enter the code name of the certification that you are interested in" \
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
   
    speech = "Security Leadership (GSLC) certification gives individuals in depth knowledge on: " \
             "\n1. Risks of 802.11 wireless networks and how to secure them" \
             "\n2. Access control and password management" \
             "\n3. Building a security awareness program" \
             "\n4. Cryptography applications, VPNs and IPSec." \
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
    
    speech = "MGT512: Security Leadership Essentials Training prepares individuals for GSLC certification. " \
             "The training course can be completed in 5 days" \
             "\n\n1. For course syllabus information enter 'MGT512 syllabus'" \
             "\n\n2. For laptop requirements to participate in the training course enter 'MGT512 laptop'" \
             "\n\n3. For info on who should attend this course enter 'MGT512 attend'" \
             "\n\n4. To register for MGT512 enter 'MGT512 register'"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# webhook for MGT512 syllabus
def webhook_giac_mgt512_syllabus(req):
    
    speech = "MGT512 Syllabus:" \
             "\nDay 1: Managing the Enterprise, Planning, Network, and Physical Plant" \
             "\nDay 2: IP Concepts, Attacks Against the Enterprise and Defense-in-Depth" \
             "\nDay 3: Secure Communications" \
             "\nDay 4: The Value of Information" \
             "\nDay 5: Management Practicum" \
             "\n\n1. For laptop requirements to participate in the training course enter 'MGT512 laptop'" \
             "\n\n2. For info on who should attend this course enter 'MGT512 attend'" \
             "\n\n3. To register for MGT512 enter 'MGT512 register'" \
             "\n\nOr visit their website at: https://www.sans.org/course/security-leadership-essentials-managers-knowledge-compression#__utma=183869984.18323172.1519689563.1519733474.1519744377.5"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# webhook for Systems and Network Auditor (GSNA)
def webhook_giac_gsna(req):

    speech = "Systems and Network Auditor (GSNA) certification gives individuals in depth knowledge on: " \
             "\n1. Basic knowledge of risk analysis techniques and be able to conduct a technical audit of essential information systems." \
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

# AUD507: Auditing & Monitoring Networks, Perimeters & Systems
def webhook_giac_aud507(req):
    
    speech = "AUD507: Auditing & Monitoring Networks, Perimeters & Systems Training prepares individuals for GSNA certification. " \
             "The training course can be completed in 5 days" \
             "\n\n1. For course syllabus information enter 'AUD507 syllabus'" \
             "\n\n2. For laptop requirements to participate in the training course enter 'AUD507 laptop'" \
             "\n\n3. For info on who should attend this course enter 'AUD507 attend'" \
             "\n\n4. To register for AUD507 enter 'AUD507 register'"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# Auditing & Monitoring Networks, Perimeters & Systems (AUD507) syllabus
def webhook_giac_aud507_syllabus(req):
    
    speech = "---AUD507 Syllabus---" \
             "\nDay 1: Effective Auditing, Risk Assessment, Reporting" \
             "\nDay 2: Effective Network & Perimeter Auditing / Monitoring" \
             "\nDay 3: Web Application Auditing" \
             "\nDay 4: Advanced Windows Auditing & Monitoring" \
             "\nDay 5: Advanced UNIX Auditing & Monitoring" \
             "\nDay 6: Audit the Flag: A NetWars Experience" \
             "\n\n1. For laptop requirements to participate in the training course enter 'AUD507 laptop'" \
             "\n\n2. For info on who should attend this course enter 'AUD507 attend'" \
             "\n\n3. To register for AUD507 enter 'AUD507 register'" \
             "\n\nOr visit their website at: https://www.sans.org/course/auditing-networks-perimeters-systems#__utma=183869984.1578707992.1516911150.1519227651.1519229972.14"
    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# webhook for Information Security Professional (GISP)
def webhook_giac_gisp(req):

    speech = "Information Security Professional (GISP) certification gives individuals in depth knowledge on: " \
             "\n1. understanding of technical security, information security and system security. " \
             "\n\nInfo at: https://www.giac.org/certification/information-security-professional-gisp" \
             "\n\nTo obtain GISP certification, the below training must be completed: " \
             "\n\nMGT414: SANS Training Program for GISP Certification" \
             "\n\nFor info on MG414 training type the course code 'MG414'"
    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# GIAC - SANS Training Program for CISSP Certification (MG414)
def webhook_giac_mgt414(req):
   
    speech = "MGT414: SANS Training Program for CISSP Certification Training prepares individuals for GISP certification. " \
             "The training course can be completed in 6 days" \
             "\n\n1. For course syllabus information enter 'MG414 syllabus'" \
             "\n\n2. For laptop requirements to participate in the training course enter 'MG414 laptop'" \
             "\n\n3. For info on who should attend this course enter 'MG414 attend'" \
             "\n\n4. To register for MG414 enter 'MG414 register'"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

def webhook_giac_mgt414_syllabus(req):
    
    speech = "---MGT414 Syllabus---" \
             "\nDay 1: Security and Risk Management" \
             "\nDay 2: Security Engineering" \
             "\nDay 3: Security Engineering " \
             "\nDay 4: Identity and Access Management" \
             "\nDay 5: Security Assessment and Testing" \
             "\nDay 6: Software Development Security" \
             "\n\n1. For laptop requirements to participate in the training course enter 'MGT414 laptop'" \
             "\n\n2. For info on who should attend this course enter 'MGT414 attend'" \
             "\n\n3. To register for MGT414 enter 'MGT414 register'" \
             "\n\nOr visit their website at: https://www.sans.org/course/sans-plus-s-training-program-cissp-certification-exam#__utma=183869984.18323172.1519689563.1519744377.1520265721.6"
    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

    # webhook for Law of Data Security & Investigations (GLEG)
def webhook_giac_gleg(req):

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
 
    speech = "LEG523: Law of Data Security and Investigations Training prepares individuals for GLEG certification. " \
             "The training course can be completed in 6 days" \
             "\n\n1. For course syllabus information enter 'LEG523 syllabus'" \
             "\n\n2. For laptop requirements to participate in the training course enter 'LEG523 laptop'" \
             "\n\n3. For info on who should attend this course enter 'LEG523 attend'" \
             "\n\n4. To register for LEG523 enter 'LEG523 register'"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

def webhook_giac_leg523_syllabus(req):
    
    speech = "---LEG523 Syllabus---" \
             "\nDay 1: Fundamentals of IT Security Law and Policy" \
             "\nDay 2: E-Records, E-Discovery and Business Law" \
             "\nDay 3: Contracting for Data Security " \
             "\nDay 4: How to Conduct Investigations" \
             "\nDay 5: Cyber Defense" \
             "\n\n1. For laptop requirements to participate in the training course enter 'LEG523 laptop'" \
             "\n\n2. For info on who should attend this course enter 'LEG523 attend'" \
             "\n\n3. To register for LEG523 enter 'LEG523 register'" \
             "\n\nOr visit their website at: https://www.sans.org/course/law-data-security-investigations#__utma=183869984.18323172.1519689563.1520265721.1520265735.7"
    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }