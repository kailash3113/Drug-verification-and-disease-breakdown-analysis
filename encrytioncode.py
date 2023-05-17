import ecdsa
from ecdsa import SigningKey


def Encode(Vcode):
    getinput = Vcode.encode('ascii')
    private_key = SigningKey.generate() # uses NIST192p
    signature = private_key.sign(getinput)
    flag = False
    lst = ['1','12','123']
    for i in lst:
        try:
            public_key = private_key.verifying_key         
            print("Verified:", public_key.verify(signature,i.encode('ascii')))
            flag = True
            break
         
        except:
            pass
         
    if(flag==False):
        print("The code is incorrect")

    else:
        print("The code is verified")

