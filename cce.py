#----------------- Certified Computer Examiner (CCE) -----------------------------
def webhook_cce_info(req):
    
    speech = "The purpose of CCE certification is to certify computer forensic examiners solely " \
    		 "based on their knowledge and practical examination skills and abilities as they relate " \
    		 "to the practice of digital forensics. Because of its high forensic and ethical standards, " \
    		 "the CCE has evolved into one of the most desired certifications in the digital forensics industry. " \
             "\n\nMore information about CCE certification can be obtained by entering one of the disciples below:" \
             "\n1. CCE Training " \
             "\n2. CCE Requirements " \
             "\n3. CCE software " \
             "\n4. CCE fees " \
             "\n5. CCE aplication " \
             "\n\nOr visit their website at: https://www.isfce.com/certification.htm"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

def webhook_cce_training(req):
    
    speech = "The ISFCE has Authorized Training Centers (ATCs) around the world to train specifically for CCE certification. " \
             "It is reccommended that you enroll within one of these courses before " \
             "attempting the CCE certification testing." \
             "\n\nFor more info on these ATCs bootcamp visit the website at: http://www.cce-bootcamp.com/" \
             "\n\nMore information about CCE certification can be obtained by entering one of the disciples below:" \
             "\n1. CCE Requirements " \
             "\n2. CCE software " \
             "\n3. CCE fees " \
             "\n4. CCE aplication " \
             "\n\nOr visit their website at: https://www.isfce.com/certification.htm"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

def webhook_cce_requirements(req):
    
    speech = "CCE Requirements:" \
             "\nComplete training at a CCE Bootcamp Authorized Training Center" \
             "\n--------------OR----------------" \
             "\nMinimum of 18 months of professional experience conducting digital forensic examinations" \
             "\n--------------OR----------------" \
             "\nHave documented self study in the field of digital forensics" \
             "\n\nMore information about CCE certification can be obtained by entering one of the disciples below:" \
             "\n1. CCE Training " \
             "\n2. CCE software " \
             "\n3. CCE fees " \
             "\n4. CCE aplication " \
             "\n\nOr visit their website at: https://www.isfce.com/certification.htm"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

def webhook_cce_software(req):
    
    speech = "To view the list of software tools used to complete CCE certification " \
             "visit the CCE webiste at : https://www.isfce.com/software.htm" \
             "\n\nMore information about CCE certification can be obtained by entering one of the disciples below:" \
             "\n1. CCE Training " \
             "\n2. CCE Requirements " \
             "\n3. CCE fees " \
             "\n4. CCE aplication " \
             "\n\nOr visit their website at: https://www.isfce.com/certification.htm"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

def webhook_cce_fees(req):
    
    speech = "CCE Fees - $395.00 USD" \
             "\n\nCCE Recertification (2 years) - $75.00 USD" \
             "\n\nRetake the CCE Exam - $175.00 USD" \
             "\n\nVisit the CCE website for more info on their fees at: https://www.isfce.com/fee.htm " \
             "\n\nMore information about CCE certification can be obtained by entering one of the disciples below:" \
             "\n1. CCE Training " \
             "\n2. CCE Requirements " \
             "\n3. CCE software " \
             "\n4. CCE aplication " \
             "\n\nOr visit their website at: https://www.isfce.com/certification.htm"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }

def webhook_cce_application(req):
    
    speech = "To apply for CCE certification, click this link: https://www.isfce.com/app.html" \
             "\n\nMore information about CCE certification can be obtained by entering one of the disciples below:" \
             "\n1. CCE Training " \
             "\n2. CCE Requirements " \
             "\n3. CCE software " \
             "\n4. CCE fees " \
             "\n\nOr visit their website at: https://www.isfce.com/certification.htm"

    print("Response")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FProject"
    }
