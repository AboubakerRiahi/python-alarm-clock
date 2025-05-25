import datetime
import time
import os
from playsound import playsound  # pip install playsound


# sound_file="Alarm.mp3"
def alarm_clock(alarm_time, sound_file):
    """
    Fonction pour déclencher une alarme à l'heure spécifiée.
    :param alarm_time: Heure de l'alarme au format HH:MM (24h).
    :param sound_file: Nom du fichier audio à jouer.
    """
    print(f"⏰ Alarme réglée pour {alarm_time}...")

    # Vérifie que le fichier audio existe
    if not os.path.exists(sound_file):
        print(f"❌ ....Le fichier audio '{sound_file}' est introuvable.")
        return

    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == alarm_time:
            print("🔔 C'est l'heure !")
            playsound(sound_file)
            break
        time.sleep(1)


def main():
    """
    Fonction principale pour saisir l'heure et démarrer l'alarme.
    """
    heure = input("🕒 Entre l'heure de l'alarme (HH:MM, format 24h) : ")

    try:
        # Vérifie que le format est correct
        datetime.datetime.strptime(heure, "%H:%M")
        alarm_clock(heure, "Alarm.mp3")
    except ValueError:
        print("❌ Format invalide. Utilise HH:MM (ex : 08:30).")


print(r"""
       ___                                  
       /\_ \                                 
   __  \//\ \      __     _ __    ___ ___    
 /'__`\  \ \ \   /'__`\  /\`'__\/' __` __`\  
/\ \L\.\_ \_\ \_/\ \L\.\_\ \ \/ /\ \/\ \/\ \ 
\ \__/.\_\/\____\ \__/.\_\\ \_\ \ \_\ \_\ \_\
 \/__/\/_/\/____/\/__/\/_/ \/_/  \/_/\/_/\/_/

""")

if __name__ == "__main__":
    main()




