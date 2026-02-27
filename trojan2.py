import subprocess

def abrir_app():
    app_path = r"C:\Windows\System32\calc.exe"
    
    try:
        subprocess.Popen(app_path)
        print(f"{app_path} aberto com sucesso.")
        
    except FileNotFoundError:
        print("Aplicativo não encontrado. Verifique o caminho.")

import msvcrt

if __name__ == "__main__":
    print("Pressione 'J' para parar.")
    for _ in range(100):
        abrir_app()
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key.lower() == b'j':
                print("Tecla J detectada. Encerrando.")
                break