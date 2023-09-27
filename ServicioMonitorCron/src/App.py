import os
from Healt_Check.healtcheck import HealthCheck

healthCheck = HealthCheck()

user = os.environ.get('USER_NOTIFICATION', '')
emails = os.environ.get('EMAILS_NOTIFICATION', '')

while True:
    print("Escaneando servicio...")
    healthCheck.healthcheck(user, emails)
    

