# Drug-verification-and-disease-breakdown-analysis

In this project, we have created an alternative solution for drug authentication and made an analysis of disease breakdown. The techniques and procedures followed to verify the drug, as well as an analysis of disease breakdown, are explained further:

<b>Current drug verification techniques used in India:</b>

Presently, there is no standard method for verifying whether a drug is genuine or not. Only the erasable ink ( T 200 (black) ink series ) is used for printing the expiration date and batch number. There is a huge danger that the printed details can be erased and reprinted for the benefit of business people. At last, the consumer is the one who is affected. To overcome this, we have introduced the verification of drugs using dynamic QR codes.

<b>For this project, we have used the Cofsil drug to verify its authenticity. The drug strip that is used for this project is displayed below:</b>

<img src="https://github.com/kailash3113/Drug-verification-and-disease-breakdown-analysis/blob/main/assets/WhatsApp%20Image%202023-05-09%20at%205.37.05%20PM.jpeg" width=300, height=300>

<b>We have created a dynamic QR code for tracking the scanning activities of the user. The QR code contains all the information about the drug, like the</b>

* Medical drug description

* Ingredients used in the drug, uses

* How to use (the procedure for using the drug or equipment)

* Safety information, YouTube

* Like how to use

* Expiration date

* Batch number

* Verification website link

* Toll-free number

* Verification code

* Manufacture details

* Email

* How to use the verification code

The above-mentioned details are written inside the pdf, and further authentication of the medical will be done once after entering the verification website that is given inside the pdf. The sample pdf format is given below:

<img src="https://github.com/kailash3113/Drug-verification-and-disease-breakdown-analysis/blob/main/assets/1.png" height=700 width=700>

<img src="https://github.com/kailash3113/Drug-verification-and-disease-breakdown-analysis/blob/main/assets/2.png" height=700 width=700>


This dynamic QR code will be printed on the drug strip, When the user wants to verify the drug, the QR code has to be scanned. After scanning the QR code, a PDF will be automatically downloaded, and all the information mentioned above will be shown. A drug strip after applying the QR code looks like this:

<img src="https://github.com/kailash3113/Drug-verification-and-disease-breakdown-analysis/blob/main/assets/WhatsApp%20Image%202023-05-09%20at%205.38.08%20PM.jpeg" height=300 weidth=300 >

The Dynamic QR code is developed using a third party website called <b>hovercode.com</b>:

<img src='https://github.com/kailash3113/Drug-verification-and-disease-breakdown-analysis/blob/main/assets/qr.png' height=300 width=400>

The architecture diagram and process flow of the project as follows:

![Google Fire Store](https://github.com/kailash3113/Drug-verification-and-disease-breakdown-analysis/blob/main/assets/Google%20Fire%20Store.png)

Screenshot of web app and result of obtained:

![wapp](https://github.com/kailash3113/Drug-verification-and-disease-breakdown-analysis/blob/main/assets/wapp.png)

The web app is developed using Flask server for backend and for front end development we have used HTML, CSS, JS. For data storing and retrival we have uesd google firestore - GFB. The website is locally hosted on 5000 port.

The result of the web app, once after entering the correct verification code:

![S](https://github.com/kailash3113/Drug-verification-and-disease-breakdown-analysis/blob/main/assets/S.png)

The result of hte web app if the verification code is incorrect:

![Screenshot 2023-05-19 120658](https://github.com/kailash3113/Drug-verification-and-disease-breakdown-analysis/blob/main/assets/Screenshot%202023-05-19%20120658.png)

The google drive link of the working model of web app is given below:

https://drive.google.com/file/d/1rYQ3mJgJttsr5yvIz6U8oMMpWDRs-3a6/view?usp=sharing

