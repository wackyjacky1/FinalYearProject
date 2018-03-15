#----------------- EnCase certification-----------------------------
def webhook_encase_info(req):
    
    speech = "The purpose of EnCase certification is proof that individuals possess a deep " \
             "understanding of the EnCase software. The guidance certification program focuses " \
             "on teaching individuals how to recover evidence from seized harddrives." \
             "\n\nThere are currently three certifications offered by EnCase:" \
             "\n1. EnCase Certified Examiner (EnCE)" \
             "\n2. Certified Forensic Security Responder (CFSR)" \
             "\n3. EnCase Certified eDiscovery Practitioner (EnCEP)" \
             "\n\nFor more info on any of these certificates, enter the cert code i.e. EnCE, CFSR or EnCEP"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

#----------------------------EnCE-------------------------------------------
def webhook_encase_ence(req):
    
    speech = "The EnCase Certified Examiner(EnCE) program certifies both public and private sector " \
             "professionals in the use of Guidance Software's EnCase computer forensic software. " \
             "Recognized by both the law enforcement and corporate communities as a symbol of a skilled computer examiner." \
             "\n\n1. Enter 'ence get started' for training and experience requirements to apply for certification." \
             "\n\n2. Enter 'ence apply' to apply for EnCE certification. " \
             "\n\n3. Enter 'ence renew' to renew your EnCE certification"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

def webhook_encase_ence_start(req):
    
    speech = "EnCase Certified Examiner(EnCE) get started: " \
             "\n\nhttps://www.guidancesoftware.com/docs/default-source/training/ence-get-started.pdf?sfvrsn=12"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

def webhook_encase_ence_apply(req):
    
    speech = "EnCase Certified Examiner(EnCE) apply: " \
             "\n\nhttps://www.guidancesoftware.com/docs/default-source/training/ence-application.pdf?sfvrsn=2"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

def webhook_encase_ence_renew(req):
    
    speech = "EnCase Certified Examiner(EnCE) renew: " \
             "\n\nhttps://www.guidancesoftware.com/docs/default-source/training/ence-renewal-form.pdf?sfvrsn=2"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }


#----------------------------CFSR-------------------------------------------

def webhook_encase_cfsr(req):
    
    speech = "The Certified Forensic Security Responder(CFSR) will equip you with the breadth and depth of " \
             "knowledge that you need to become a highly sought-after cyber security forensics expert. " \
             "\n\n1. Enter 'cfsr get started' for training and experience requirements to apply for certification." \
             "\n\n2. Enter 'cfsr apply' to apply for CFSR certification. " \
             "\n\n3. Enter 'cfsr renew' to renew your CFSR certification"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

def webhook_encase_cfsr_start(req):
    
    speech = "CFSR Certification Program get started: " \
             "\n\nhttps://www.guidancesoftware.com/docs/default-source/training/cfsr-get-started.pdf?sfvrsn=60918cad_16"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

def webhook_encase_cfsr_apply(req):
    
    speech = "CFSR Certification Program apply: " \
             "\n\nhttps://www.guidancesoftware.com/docs/default-source/training/cfsr-application.pdf?sfvrsn=2"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

def webhook_encase_cfsr_renew(req):
    
    speech = "CFSR Certification Program renew: " \
             "\n\nhttps://www.guidancesoftware.com/docs/default-source/training/cfsr-renewal.pdf?sfvrsn=2"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }


#----------------------------EnCEP-------------------------------------------

def webhook_encase_encep(req):
    
    speech = "EnCase Certified eDiscovery Practitioner(EnCEP) program is the leading e-discovery solution for the " \
             "search, collection, preservation, and processing of electronically stored information(ESI). " \
             "Recognized by both the law enforcement and corporate communities as a symbol of a skilled computer examiner. " \
             "\n\n1. Enter 'encep get started' for training and experience requirements to apply for certification." \
             "\n\n2. Enter 'encep apply' to apply for EnCEP certification. " \
             "\n\n3. Enter 'encep renew' to renew your EnCEP certification"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

def webhook_encase_encep_start(req):
    
    speech = "EnCEP eDiscovery Practitioner Certification Program get started: " \
             "\n\nhttps://www.guidancesoftware.com/docs/default-source/training/encep-get-started.pdf?sfvrsn=6fvrsn=6"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

def webhook_encase_encep_apply(req):
    
    speech = "EnCEP eDiscovery Practitioner Certification Program apply: " \
             "\n\nhttps://www.guidancesoftware.com/docs/default-source/training/encep-application.pdf?sfvrsn=2"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

def webhook_encase_encep_renew(req):
    
    speech = "EnCEP eDiscovery Practitioner Certification Program renew: " \
             "\n\nhttps://www.guidancesoftware.com/docs/default-source/training/encep-renewal-form.pdf?sfvrsn=2"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }