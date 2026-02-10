from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mail import Mail, Message

app = Flask(__name__)
CORS(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'caxtonetechnologieske@gmail.com'
app.config['MAIL_PASSWORD'] = 'itdh gorw ixcm pkdv'

mail = Mail(app)

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
    recipient = 'pycodersofkirinyaga@gmail.com'
    sender = app.config['MAIL_USERNAME']

    if purpose == 'yes/no':
        if inputs.get('response') == 'yes':
            msg = Message(subject='Success Notification', sender=sender, recipients=[recipient])
            msg.html = f"""
            {email_head}
            <div style="font-family: 'Poppins', Arial, sans-serif; max-width: 600px; margin: auto; padding: 40px; border: 1px solid #e1e1e1; border-radius: 20px; text-align: center; background-color: #ffffff;">
                <div style="font-size: 50px; color: #ff1493; margin-bottom: 20px;">✦</div>
                <h1 style="font-family: 'Playfair Display', serif; color: #2d3436; font-size: 32px; margin-bottom: 10px;">She Said Yes</h1>
                <p style="color: #636e72; font-size: 16px; line-height: 1.6;">Aggie has accepted to come back. The journey that began on March 13th is moving forward.</p>
                <div style="margin-top: 30px; border-top: 1px solid #f1f1f1; padding-top: 20px; font-size: 12px; color: #b2bec3; text-transform: uppercase; letter-spacing: 2px;">Automated Status Update</div>
            </div>
            """
            mail.send(msg)
        else:
            msg = Message(subject='Status Update', sender=sender, recipients=[recipient])
            msg.html = f"""
            {email_head}
            <div style="font-family: 'Poppins', Arial, sans-serif; max-width: 600px; margin: auto; padding: 40px; border: 1px solid #e1e1e1; border-radius: 20px; text-align: center; background-color: #f9f9f9;">
                <div style="font-size: 50px; color: #6c5ce7; margin-bottom: 20px;">✧</div>
                <h1 style="font-family: 'Playfair Display', serif; color: #2d3436; font-size: 32px; margin-bottom: 10px;">Not Ready</h1>
                <p style="color: #636e72; font-size: 16px; line-height: 1.6;">Aggie clicked "Not ready". She saw the message about April 13th but requested more time.</p>
                <div style="margin-top: 30px; border-top: 1px solid #f1f1f1; padding-top: 20px; font-size: 12px; color: #b2bec3;">LOGGED VIA PYCODERS BACKEND</div>
            </div>
            """
            mail.send(msg)
        return jsonify({'Message': 'Success'})

    elif purpose == 'number':
        phone = inputs.get('number')
        msg = Message(subject='Contact Info Received', sender=sender, recipients=[recipient])
        msg.html = f"""
        {email_head}
        <div style="font-family: 'Poppins', Arial, sans-serif; max-width: 600px; margin: auto; padding: 40px; border: 1px solid #32cd32; border-radius: 20px; text-align: center; background-color: #ffffff;">
            <div style="font-size: 50px; color: #32cd32; margin-bottom: 20px;">◈</div>
            <h1 style="font-family: 'Playfair Display', serif; color: #2d3436; font-size: 28px; margin-bottom: 10px;">Connection Established</h1>
            <p style="color: #636e72; font-size: 16px; margin-bottom: 30px;">Aggie shared her contact details with you.</p>
            <div style="display: inline-block; background: #f0fff0; padding: 20px 40px; border: 2px dashed #32cd32; border-radius: 10px;">
                <a href="tel:{phone}" style="text-decoration: none; font-size: 24px; font-weight: 600; color: #155724; letter-spacing: 3px; font-family: monospace;">{phone}</a>
                <div style="margin-top: 10px; font-size: 11px; color: #2e8b57; font-weight: 600;">CLICK TO CALL / LONG PRESS TO COPY</div>
            </div>
            <p style="margin-top: 40px; font-size: 13px; color: #b2bec3; font-style: italic;">"Welcome home, Aggie wangu."</p>
        </div>
        """
        mail.send(msg)
        return jsonify({'Message': 'Success'})

    return jsonify({'error': 'invalid'}), 400
@app.route('/')
    return 'Hello, it is working!!!'

if __name__ == '__main__':
   app.run(debug=True)



