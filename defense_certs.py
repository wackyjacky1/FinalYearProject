#------------------------------------------------- GIAC industrial defense certifications --------------------------------------
def webhook_giac_industrial_defense(req):

    speech = "Below is a list of the GIAC Industrial Defense certifications: " \
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

def webhook_giac_gicsp(req):

    speech = "Global Industrial Cyber Security Professional (GICSP) certification gives individuals in depth knowledge on: " \
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

# GIAC - ICS410: ICS/SCADA Security Essentials
def webhook_giac_ics410(req):
    
    speech = "ICS410: ICS/SCADA Security Essentials Training prepares individuals for GICSP certification. " \
             "The training course can be completed in 5 days" \
             "\n\n1. For course syllabus information enter 'ICS410 syllabus'" \
             "\n\n2. For laptop requirements to participate in the training course enter 'ICS410 laptop'" \
             "\n\n3. For info on who should attend this course enter 'ICS410 attend'" \
             "\n\n4. To register for ICS410 enter 'ICS410 register'"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# webhook for ICS410 syllabus
def webhook_giac_ics410_syllabus(req):
    
    speech = "---ICS410 Syllabus---" \
             "\nDay 1: ICS Overview" \
             "\nDay 2: ICS Attack Surface" \
             "\nDay 3: Defending ICS Servers and Workstations" \
             "\nDay 4: Defending ICS Networks and Devices" \
             "\nDay 5: ICS Security Governance" \
             "\n\n1. For laptop requirements to participate in the training course enter 'ICS410 laptop'" \
             "\n\n2. For info on who should attend this course enter 'ICS410 attend'" \
             "\n\n3. To register for ICS410 enter 'ICS410 register'" \
             "\n\nOr visit their website at: https://www.sans.org/course/ics-scada-cyber-security-essentials#__utma=183869984.18323172.1519689563.1520346899.1520432188.11"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# webhook for Response and Industrial Defense (GRID)
def webhook_giac_grid(req):

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

# ICS515: ICS Active Defense and Incident Response
def webhook_giac_ics515(req):
    
    speech = "ICS515: ICS Active Defense and Incident Response Training prepares individuals for GRID certification. " \
             "The training course can be completed in 5 days" \
             "\n\n1. For course syllabus information enter 'ICS515 syllabus'" \
             "\n\n2. For laptop requirements to participate in the training course enter 'ICS515 laptop'" \
             "\n\n3. For info on who should attend this course enter 'ICS515 attend'" \
             "\n\n4. To register for ICS515 enter 'ICS515 register'"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# webhook for ICS515 syllabus
def webhook_giac_ics515_syllabus(req):
    
    speech = "ICS515 Syllabus:" \
             "\nDay 1: Threat Intelligence" \
             "\nDay 2: Network Security Monitoring" \
             "\nDay 3: Incident Response" \
             "\nDay 4: Threat and Environment Manipulation" \
             "\nDay 5: Active Defense and Incident Response" \
             "\n\n1. For laptop requirements to participate in the training course enter 'ICS515 laptop'" \
             "\n\n2. For info on who should attend this course enter 'ICS515 attend'" \
             "\n\n3. To register for ICS515 enter 'ICS515 register'" \
             "\n\nOr visit their website at: https://www.sans.org/course/industrial-control-system-active-defense-and-incident-response#__utma=183869984.18323172.1519689563.1520346899.1520432188.11"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

# webhook for Critical Infrastructure Protection (GCIP)
def webhook_giac_gcip(req):

    speech = "Critical Infrastructure Protection (GCIP) certification gives individuals in depth knowledge on: " \
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