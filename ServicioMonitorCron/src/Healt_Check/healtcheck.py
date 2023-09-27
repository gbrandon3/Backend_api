import time
import requests
import os
from EnviarCorreo.send_email import EnviarNotificacion
from Redis_Cache.redis_cache import RedisCache

class HealthCheck:
    def healthcheck(self, user, emails):
        enviarNotificacion = EnviarNotificacion()
        redisCache = RedisCache()
        try:
            session = requests.Session()
            content = session.get(os.environ.get('URL_PRUEBA_TEC', '') + "healthcheck")
            if content.status_code != 200:
                print("Fallo Servicio...")
                redisCache.setKey("url_prueba_tecnica", os.environ.get('URL_PRUEBA_TEC_BK', ''))
                enviarNotificacion.send_email_notification(user, emails)
                time.sleep(int(os.environ.get('TIME_WAIT', 60)))
            else:
                redisCache.setKey("url_prueba_tecnica", os.environ.get('URL_PRUEBA_TEC', ''))
                print("Servicio Ok...")
                time.sleep(int(os.environ.get('TIME_JOB', 1)))
        except Exception:
            print("Fallo Servicio...")
            redisCache.setKey("url_prueba_tecnica", os.environ.get('URL_PRUEBA_TEC_BK', ''))
            enviarNotificacion.send_email_notification(user, emails)
            time.sleep(int(os.environ.get('TIME_WAIT', 60)))