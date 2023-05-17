import ecdsa
from ecdsa import SigningKey


def Encode(lst,getinput):
    private_key = SigningKey.generate() # uses NIST192p
    signature = private_key.sign(getinput.encode('ascii'))
    flag = False
    for i in lst:
        try:
            public_key = private_key.verifying_key         
            yield f"Verified : {public_key.verify(signature,i.encode('ascii'))}"
            flag = True
            break
         
        except:
            pass
         
    if(flag==False):
        yield "The code is incorrect, please check the code...!!!"
        return False

    else:
        yield "The code is verified and the drug is genuine...!!!"
        return True

