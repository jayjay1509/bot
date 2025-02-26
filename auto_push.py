import random
import time
import datetime
import os

# Plage horaire souhaitée (par exemple, entre 9h et 17h)
start_hour = 9
end_hour = 17

# Générer une heure aléatoire entre 9h et 17h
random_hour = random.randint(start_hour, end_hour)
random_minute = random.randint(0, 59)
random_second = random.randint(0, 59)

# Calculer l'heure actuelle et l'heure cible
now = datetime.datetime.now()
target_time = now.replace(hour=random_hour, minute=random_minute, second=random_second, microsecond=0)

# Si l'heure cible est déjà passée aujourd'hui, attendre jusqu'à demain
if target_time < now:
    target_time += datetime.timedelta(days=1)

# Calculer le temps restant avant l'heure cible
time_to_wait = (target_time - now).total_seconds()

# Attendre jusqu'à l'heure cible
print(f"Attente jusqu'à {target_time.strftime('%H:%M:%S')}...")
time.sleep(time_to_wait)

# Une fois l'heure cible atteinte, exécuter le code de modification du fichier et du commit
file_path = "raport.txt"

# Simuler un changement (par exemple, ajouter la date et l'heure du commit)
with open(file_path, "a") as file:
    commit_time = datetime.datetime.now()
    file.write(f"\nDernier commit effectué à {commit_time.strftime('%Y-%m-%d %H:%M:%S')}\n")

# Commandes Git pour commit et push
os.system("git add .")
os.system('git commit -m "Auto commit du jour 🚀"')

print(f"Fichier mis à jour et commit effectué à {commit_time.strftime('%Y-%m-%d %H:%M:%S')}")
