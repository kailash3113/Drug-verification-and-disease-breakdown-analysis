from flask import Flask, render_template,request
from PyToFirebase import VC,all_details
from test_link_FStoPY import Encode

VC('1n?3KBIKDzC')
print(all_details())

app = Flask(__name__,static_url_path='/static/images/')
 
@app.route('/',methods = ['GET','POST'])
def front_end():
    if request.method == 'POST':
        VerificationCode = request.form.get("vr_code")
        VC(VerificationCode)
        result = all_details()
        if(result == {}):
            return render_template('result.html')
        else:
            return render_template('test.html',result = result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port = 5000, debug=True)