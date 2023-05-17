#import encrytioncode
#GetInp = encrytioncode.Encode()
import test_link_FStoPY
import firebase_admin
from firebase_admin import credentials, firestore
from test_link_FStoPY import Encode

'''
db.collection("QRCODE_DETAILS").add({
    'name_of_the_drug': 'Cofsils',
    'Batch_No':'M630072',
    'Expire_date' : 'JANUARY 2026',
    'Manufacture_details' : 'm.l, 25A/2/2016, mFD. BY CIPLA HEALTH LTD,PLOT NO: 6-A, SECTOR-D, MANDIDEEP,RAISEN, MADHYA PRADESH – 046.',
    'Encryption_verification_code' : 100100,
    'Unique_identification_number' : 311312,
    'Toll_free_number' : 18001201431
    })'''


def VC(get_input):
    global dictVal
    dictVal = {}
    try:
        app = firebase_admin.get_app()
    except ValueError as e:
        cred = credentials.Certificate(r"C:\Users\KAILASH\Desktop\SR Project\py\qrcodedetails-2cbf2-firebase-adminsdk-6f6u2-c1db97cbc3.json")
        firebase_admin.initialize_app(cred)
        
    db = firestore.client()
    lst = []
    docs = db.collection('QRCODE_DETAILS').get()
    for doc in docs:
        ObtoDic = doc.to_dict()
        lst.append(ObtoDic['Encryption_verification_code'])
    
    if(test_link_FStoPY.Encode(lst,get_input)):
        for i in Encode(lst, get_input):
            pass
        fetchdb = db.collection('QRCODE_DETAILS').where('Encryption_verification_code','==',get_input).get()
        for i in fetchdb:
            user_display_dict = i.to_dict()
            print()
            for j in user_display_dict.keys():
                if(j == 'Encryption_verification_code'):
                    pass
                else:
                    dictVal[j] = user_display_dict[j]
                    

def all_details():
    return dictVal