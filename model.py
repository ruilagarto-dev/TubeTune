import yt_dlp
import os
import subprocess

class YTDownloadManager:
    def __init__(self):
        self.ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': '%(title)s.%(ext)s',
            'quiet': True,
            'no_warnings': True,
            'extractaudio': True,
            'audioformat': 'mp3',
            'noplaylist': True,
            'writethumbnail': False,
            'writeinfojson': False,
            'writesubtitles': False,
            'writeautomaticsub': False,
            'ignoreerrors': False,
            'nooverwrites': True
        }

    def download_single_music(self, url, path):
        try:
            # Configura o caminho de saída
            self.ydl_opts['outtmpl'] = os.path.join(path, '%(title)s.%(ext)s')
            
            # Força o download do áudio
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=True)
                
                # Verifica se o arquivo foi criado
                filename = ydl.prepare_filename(info_dict)
                mp3_file = os.path.splitext(filename)[0] + '.mp3'
                
                if os.path.exists(mp3_file):
                    return True
                
            # Se não funcionou com yt-dlp, tenta com subprocess
            return self._download_with_subprocess(url, path)
            
        except Exception as e:
            raise Exception(f"Falha no download: {str(e)}")

    def download_playlist(self, url, path):
        try:
            self.ydl_opts['outtmpl'] = os.path.join(path, '%(title)s.%(ext)s')
            self.ydl_opts['noplaylist'] = False
            
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                ydl.download([url])
                return True
        except Exception as e:
            raise Exception(f"Falha no download da playlist: {str(e)}")

    def _download_with_subprocess(self, url, path):
        """Método alternativo usando subprocess"""
        try:
            command = [
                'yt-dlp',
                '-x',
                '--audio-format', 'mp3',
                '--no-playlist',
                '-o', os.path.join(path, '%(title)s.%(ext)s'),
                url
            ]
            result = subprocess.run(command, capture_output=True, text=True)
            
            if result.returncode == 0:
                return True
            else:
                raise Exception(result.stderr)
        except Exception as e:
            raise Exception(f"Erro no subprocess: {str(e)}")


