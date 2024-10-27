import threading

def cpu_stress():
    while True:
        pass  # Loop infinito per stressare la CPU

# Numero di thread che vuoi creare per stressare la CPU
num_threads = 10000
threads = []

for _ in range(num_threads):
    thread = threading.Thread(target=cpu_stress)
    thread.start()
    threads.append(thread)

# I thread continueranno a girare indefinitamente.
# Per terminare il programma, interrompere manualmente.
