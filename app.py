import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

RESEND_API_KEY = "re_your_api_key_here"
RECIPIENT = "pycodersofkirinyaga@gmail.com"
SENDER = "onboarding@resend.dev"

email_head = """
<head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com" rel="stylesheet">
</head>
"""

def send_api_email(subject, html_content):
    url = "https://api.resend.com"
    headers = {
        "Authorization": f"Bearer {RESEND_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "from": SENDER,
        "to": RECIPIENT,
        "subject": subject,
        "html": html_content
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.status_code

@app.route('/send_message', methods=['POST'])
def send():
    inputs = request.get_json()
    purpose = inputs.get('purpose')
    subject = ""
    html_body = ""

    if purpose == 'yes/no':
        if inputs.get('response') == 'yes':
            subject = 'Success Notification'
            html_body = f"""{email_head}<div style="font-family: 'Poppins', Arial, sans-serif; text-align: center; padding: 40px;"><h1>She Said Yes</h1><p>Aggie has accepted.</p></div>"""
        else:
            subject = 'Status Update'
            html_body = f"""{email_head}<div style="font-family: 'Poppins', Arial, sans-serif; text-align: center; padding: 40px;"><h1>Not Ready</h1><p>Aggie requested more time.</p></div>"""

    elif purpose == 'number':
        phone = inputs.get('number')
        subject = 'Contact Info Received'
        html_body = f"""{email_head}<div style="text-align: center; padding: 40px;"><h1>Connection Established</h1><p>Number: {phone}</p></div>"""

    if subject and html_body:
        status = send_api_email(subject, html_body)
        if status in [200, 201]:
            return jsonify({'Message': 'Success'}), 200
        else:
            return jsonify({'error': 'Email provider rejected request'}), 500

    return jsonify({'error': 'invalid'}), 400

@app.route('/')
def Test():
    return 'Working via REST API'

if __name__ == '__main__':
   app.run(debug=True)
