import threading
import re

class TubeTuneController:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.view.set_controller(self)

    def is_valid_youtube_url(self, url):
        patterns = [
            r'^https?://(www\.)?youtube\.com/watch\?v=',
            r'^https?://youtu\.be/',
            r'^https?://(www\.)?youtube\.com/playlist\?list='
        ]
        return any(re.search(pattern, url) for pattern in patterns)

    def download_music(self):
        url = self.view.get_link()
        path = self.view.get_destination()
        
        if not url:
            self.view.show_message("Error", "Por favor, insira um link válido.")
            return
            
        if not self.is_valid_youtube_url(url):
            self.view.show_message("Error", "Por favor, insira um link do YouTube válido.")
            return
            
        if not path:
            self.view.show_message("Error", "Por favor, selecione uma pasta destino.")
            return

        def download_task():
            try:
                self.model.download_single_music(url, path)
                self.view.show_message("Info", "Download da música concluído com sucesso!")
                self.view.clearFields()
            except Exception as e:
                print(f"Erro ao baixar música: {str(e)}")
                self.view.show_message("Error", f"Erro ao baixar música: {str(e)}")

        threading.Thread(target=download_task, daemon=True).start()

    def download_playlist(self):
        url = self.view.get_link()
        path = self.view.get_destination()
        
        if not url:
            self.view.show_message("Error", "Por favor, insira um link válido.")
            return
            
        if not self.is_valid_youtube_url(url):
            self.view.show_message("Error", "Por favor, insira um link do YouTube válido.")
            return
            
        if not path:
            self.view.show_message("Error", "Por favor, selecione uma pasta destino.")
            return

        def download_task():
            try:
                self.model.download_playlist(url, path)
                self.view.show_message("Info", "Download da playlist concluído com sucesso!")
                self.view.clearFields()
            except Exception as e:
                self.view.show_message("Error", f"Erro ao baixar playlist: {str(e)}")

        threading.Thread(target=download_task, daemon=True).start()
