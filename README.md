chmod +x Makefile

# TubeTune

TubeTune é uma aplicação simples para transferir aúdio de vídeos ou playlist do YOutube no formato MP3. A interface gráfica é feita em tkinter, e o processo de download é gerido pela biblioteca yt-dlp.


## Funcionalidade
- Transferir áudio de videos individuias do YouTube.
- Transferir áudio de playlist completas.
- Escolha da pasta destino para salvar os arquivos de áudio.
- Validação básica de URLs do YouTube.
- Interface gráfica simples e intuitiva.
- Download em segundo plano utilizando threads para evitar travamentos.

## Tecnologias e Bibliotecas

- Python 3
- Tkinter
- yt-dlp
- FFmpeg
- pydub


## Instalar

### Pré-requesitos
- python 3 instalado
- FFmpeg instalado no sistema

### Passos para instalar e executar

Clonar o repositorio:

```bash
git clone <>
cd <>
```

Instalar as dependências e criar ambiente virtual:
```bash
make install
```

Executar:
```bash
make run
```


## Uso


1. Insira o link do vídeo ou da playlist do YouTube no campo **"Insira o link do YouTube"**.

2. Selecione a pasta destino onde os arquivos MP3 serão salvos.

3. Clique em **"Baixar Música"** para baixar o vídeo único ou em **"Baixar Playlist"** para baixar todos os vídeos da playlist.

4. Aguarde a conclusão. Mensagens informativas aparecerão durante o processo.
