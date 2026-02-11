import time
import os
import resend
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

resend.api_key = "re_JRQNW7js_QDBNMVpPicGxU9qP37pYj468"
VERIFIED_SENDER = "onboarding@resend.dev"

email_head = """
<head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com" rel="stylesheet">
</head>
"""

@app.route('/send_message', methods=['POST'])
def send():
    inputs = request.get_json()
    purpose = inputs.get('purpose')
    recipient = 'tolecaxtone2@gmail.com'

    subject = ""
    html_content = ""

    if purpose == 'yes/no':
        if inputs.get('response') == 'yes':
            subject = 'Success Notification'
            html_content = f"""
            {email_head}
            <div style="font-family: 'Poppins', sans-serif; max-width: 600px; margin: auto; padding: 40px; border-radius: 20px; text-align: center; background-color: #ffffff; border: 1px solid #eee;">
                <div style="font-size: 50px; color: #ff1493; margin-bottom: 20px;">✦</div>
                <h1 style="font-family: 'Playfair Display', serif; color: #2d3436; font-size: 32px; margin-bottom: 10px;">She Said Yes</h1>
                <p style="color: #636e72; font-size: 16px; line-height: 1.6;">Aggie has accepted to come back. The journey that began on March 13th is moving forward.</p>
            </div>
            """
        else:
            subject = 'Status Update'
            html_content = f"""
            {email_head}
            <div style="font-family: 'Poppins', sans-serif; max-width: 600px; margin: auto; padding: 40px; border-radius: 20px; text-align: center; background-color: #f9f9f9; border: 1px solid #eee;">
                <div style="font-size: 50px; color: #6c5ce7; margin-bottom: 20px;">✧</div>
                <h1 style="font-family: 'Playfair Display', serif; color: #2d3436; font-size: 32px; margin-bottom: 10px;">Not Ready</h1>
                <p style="color: #636e72; font-size: 16px; line-height: 1.6;">Aggie clicked "Not ready". She saw the message about April 13th but requested more time.</p>
            </div>
            """

    elif purpose == 'number':
        phone = inputs.get('number')
        subject = 'Contact Info Received'
        html_content = f"""
        {email_head}
        <div style="font-family: 'Poppins', sans-serif; max-width: 600px; margin: auto; padding: 40px; border: 1px solid #32cd32; border-radius: 20px; text-align: center;">
            <h1 style="font-family: 'Playfair Display', serif; color: #2d3436; font-size: 28px; margin-bottom: 10px;">Connection Established</h1>
            <div style="display: inline-block; background: #f0fff0; padding: 20px 40px; border: 2px dashed #32cd32; border-radius: 10px;">
                <a href="tel:{phone}" style="text-decoration: none; font-size: 24px; font-weight: 600; color: #155724;">{phone}</a>
            </div>
            <p style="margin-top: 40px; font-size: 13px; color: #b2bec3; font-style: italic;">"Welcome home, Aggie wangu."</p>
        </div>
        """

    if subject and html_content:
        start_time = time.time()
        try:
            resend.Emails.send({
                "from": VERIFIED_SENDER,
                "to": recipient,
                "subject": subject,
                "html": html_content
            })
            duration = time.time() - start_time
            print(f"Resend send time: {duration:.2f}s")
            return jsonify({'Message': 'Success', 'time_taken': round(duration, 2)})
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    return jsonify({'error': 'invalid'}), 400

if __name__ == '__main__':
    app.run(debug=True)
