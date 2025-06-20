import getpass
import os
import subprocess
import shutil

class ManipulaRepositorios:

    def __init__(self, username):  # <-- precisa estar assim
        self.username = username
        self.api_base_url = 'https://api.github.com'
        self.access_token = getpass.getpass("Digite o Token: ")
        self.headers = {
            'Authorization': "Bearer " + self.access_token,
            'X-GitHub-Api-Version': '2022-11-28'
        }
    def commit_repo(self, caminho_repo_local):
        try:
            subprocess.run(["git", "-C", caminho_repo_local, "add", "."], check=True)
            subprocess.run(["git", "-C", caminho_repo_local, "commit", "-m", "Atualizando repositório inteiro"], check=True)
            subprocess.run(["git", "-C", caminho_repo_local, "push"], check=True)
            print("Commit e push realizados com sucesso.")
        except subprocess.CalledProcessError as e:
            print(f"Erro durante o git: {e}")
