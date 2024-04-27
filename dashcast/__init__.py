import os
import subprocess

VIDEO_EXTENSIONS = ['.mp4', '.avi', '.mkv', '.flv', '.mov']

def install_ffmpeg():
    # Vérifie si ffmpeg est installé
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("ffmpeg est déjà installé.")
    except FileNotFoundError:
        # ffmpeg n'est pas installé, l'installer
        print("ffmpeg n'est pas installé, installation en cours...")
        try:
            subprocess.run(["sudo", "apt", "update"])
            subprocess.run(["sudo", "apt", "install", "ffmpeg", "-y"])
            print("ffmpeg a été installé avec succès.")
        except Exception as e:
            try:
                subprocess.run(["choco", "install", "ffmpeg", "-y"])
                print("ffmpeg a été installé avec succès.")
            except Exception as e:
                raise Exception(f"Une erreur s'est produite lors de l'installation de ffmpeg: {e}\n\nVeuillez installer ffmpeg manuellement.")

def encode_to_av1(input_path: str | list[str], output_path: str | list[str]) -> None:
    def encode(input_file_path: str, output_file_path: str):
        install_ffmpeg()
        # Vérifiez si le fichier d'entrée existe
        if not os.path.isfile(input_file_path):
            raise ValueError(f"Le fichier {input_file_path} n'existe pas.")

        # Utilisez FFmpeg pour encoder la vidéo en AV1
        command = f"ffmpeg -i {input_file_path} -c:v libaom-av1 -strict -2 {output_file_path}"
        
        try:
            # Exécutez la commande
            subprocess.run(command, shell=True, check=True)
            print(f"La vidéo a été encodée avec succès en AV1 et enregistrée sous {output_file_path}.")
        except subprocess.CalledProcessError as e:
            print(f"Une erreur s'est produite lors de l'encodage de la vidéo : {str(e)}")

    if isinstance(input_path, str):
        input_path = [input_path]
    if isinstance(output_path, str):
        output_path = [output_path]
    
    # Vérifiez si les chemins d'entrée et de sortie sont correctes
    if len(output_path) != 1:
        if len(input_path) != len(output_path):
            raise ValueError("Le nombre de chemins d'entrée et de sortie doit être le même.")
        if any(os.path.isdir(input_file_path) and os.path.isfile(output_file_path) for input_file_path, output_file_path in zip(input_path, output_path)):
            raise TypeError("Un dossier ne peux pas être convertis en vidéo.")

    for input_file_path, output_file_path in zip(input_path, output_path):
        if os.path.isdir(input_file_path):
            for filename in os.listdir(input_file_path):
                if any(filename.endswith(ext) for ext in VIDEO_EXTENSIONS):
                    filepath = os.path.join(input_file_path, filename)
                    new_filepath = os.path.join(output_file_path, f'{os.path.splitext(filename)[0]}_av1{os.path.splitext(filename)[1]}')
                    encode(filepath, new_filepath)
        else:
            encode(input_file_path, output_file_path)

# Testez la fonction avec un fichier vidéo exemple
# encode_to_av1("exemple.mp4", "exemple_av1.mp4")
