import time
from plyer import notification

def notificar():
    notification.notify(
        title='Hora de Beber Água!',
        message='Lembre-se de beber 200ml de água!',
        app_name='Lembrete de Hidratação',
        timeout=10
    )

if __name__ == '__main__':
    while True:
        notificar()
        time.sleep(3600)
