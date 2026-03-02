import subprocess
import threading
import random
import time
import winsound
import pyautogui
import ctypes
import msvcrt
import os

parar = False

def iniciar_cmd():
    return subprocess.Popen(
        "cmd",
        stdin=subprocess.PIPE,
        text=True
    )

def configurar_cmd(proc):
    proc.stdin.write("color A\n")
    proc.stdin.write("title Kernel Panic\n")
    proc.stdin.write("mode con: cols=120 lines=30\n")
    proc.stdin.write("cls\n")
    proc.stdin.flush()

def comandos_fake(proc):
    comandos = [
        "echo Iniciando protocolo 7...",
        "echo Bypassando firewall...",
        "echo Extraindo credenciais...",
        "echo Acesso root concedido...",
        "echo Sistema comprometido."
    ]

    while not parar:
        proc.stdin.write(random.choice(comandos) + "\n")
        proc.stdin.flush()
        time.sleep(0.5)

def som():
    while not parar:
        winsound.Beep(random.randint(600, 1500), 150)

def mouse_caos():
    while not parar:
        x, y = pyautogui.position()
        pyautogui.moveTo(
            x + random.randint(-15, 15),
            y + random.randint(-15, 15)
        )
        time.sleep(0.05)

def abrir_calc():
    system32 = os.path.join(os.environ["WINDIR"], "System32")
    calc = os.path.join(system32, "calc.exe")
    while not parar:
        subprocess.Popen(calc)
        time.sleep(1)

def mensagem():
    ctypes.windll.user32.MessageBoxW(
        0,
        "Falha crítica detectada no Kernel32.",
        "Windows Fatal Error",
        0x10
    )

def ouvir_tecla():
    global parar
    print("Pressione J para encerrar o caos.")
    while True:
        if msvcrt.kbhit():
            if msvcrt.getch().lower() == b'j':
                parar = True
                print("Encerrando...")
                break

if __name__ == "__main__":
    cmd_proc = iniciar_cmd()
    configurar_cmd(cmd_proc)

    threading.Thread(target=comandos_fake, args=(cmd_proc,)).start()
    threading.Thread(target=som).start()
    threading.Thread(target=mouse_caos).start()
    threading.Thread(target=abrir_calc).start()
    threading.Thread(target=mensagem).start()

    ouvir_tecla()

    cmd_proc.stdin.write("echo Sistema restaurado.\n")
    cmd_proc.stdin.flush()
