import os
import smtplib
from email.message import EmailMessage

class EnviarNotificacion:
    def send_email_notification(self, user, emails):
        body = """
            <!DOCTYPE html>
                <head>
                    <body>
                        <h1>Error en el servicio de pruebas técnicas</h1>

                        <p>Hola <b>{}</b>, </p>
                        <p>El servicio de  pruebas técnicas ha dejado de funcionar, se activo el plan de contingencia, mientras se soliciona el inconveniente.
                        </p>
                        </br>
                        <p> <b>
                            Esto es un correo automatico de notificación, no contestar.
                            </b>
                        </p>
                    </body>
                </head>
            """.format(user)
        
        # Objeto emailMessage
        message = EmailMessage()

        # Propiedades del mensaje
        email_subject = "Error en el servicio de Pruebas Técnicas"
        sender_email_address = os.environ.get('SENDER_EMAIL_ADDRESS','')
        passwordEmail = os.environ.get('PASSWORD_EMAIL', '')
        receiver_email_address = emails

        # Encabezados del mensaje
        message['Subject'] = email_subject
        message['From'] = sender_email_address
        message['To'] = receiver_email_address

        # Contenido del mensaje
        message.set_content(body,subtype='html')

        # Servdior smtp y puerto
        email_smtp = os.environ.get('EMAIL_SMTP', '')
        server = smtplib.SMTP(email_smtp, os.environ.get('PRUERTO_SMTP',''))

        # Identificar este cliente al servidor SMTP
        server.ehlo()

        # Conexión SMTP segura
        server.starttls()

        # Loguearse en la cuenta de google
        server.login(sender_email_address, passwordEmail)

        # Enviar email
        server.send_message(message)

        # Detener la conexión al servidor
        server.quit()