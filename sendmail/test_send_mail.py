import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to_email):
    # SMTPサーバー情報
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_user = 'your_email@gmail.com'  # 送信元のGmailアドレス
    smtp_password = 'your_app_password'  # アプリパスワード
    # メールの内容
    subject = 'Notification'
    body = 'This is a test notification.'

    # MIMEオブジェクトの作成
    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # SMTPサーバーに接続
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # TLS暗号化を開始
        server.login(smtp_user, smtp_password)  # SMTPサーバーにログイン
        text = msg.as_string()
        server.sendmail(smtp_user, to_email, text)  # メールを送信
        server.quit()  # サーバーを切断
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# メールを送信
send_email('your@gmail.com')
