chmod +x Makefile

# TubeTune
TubeTune é uma aplicação simples para transferir áudio de vídeos ou playlists do YouTube no formato MP3. A interface gráfica é feita em Tkinter, e o processo de download é gerido pela biblioteca yt-dlp.

## Captura de Tela
![Tela principal do TUbeTune](docs/tubetune_tela_principal.png)


## Funcionalidade
- Transferir áudio de vídeos individuais do YouTube.
- Transferir áudio de playlists completas.
- Escolha da pasta de destino para salvar os arquivos de áudio.
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
Clone o repositório:
```bash
git clone https://github.com/ruilagarto-dev/TubeTune.git
cd TubeTune
```

Instale as dependências e crie o ambiente virtual:
```bash
make install
```

Execute:
```bash
make run
```


## Uso
1. Insira o link do vídeo ou da playlist do YouTube no campo **"Insira o link do YouTube"**.
2. Selecione a pasta de destino onde os arquivos MP3 serão salvos.
3. Clique em **"Baixar Música"** para baixar um vídeo único ou em **"Baixar Playlist"** para baixar todos os vídeos da playlist.
4. Aguarde a conclusão. Mensagens informativas aparecerão durante o processo.


## Estrutura do Projeto
- **src/main.py** — ponto de entrada da aplicação.
- **modules/view.py** — interface gráfica com Tkinter.
- **modules/controller.py** — lógica de controle e validação.
- **modules/model.py** — gerenciamento do download usando yt-dlp.
- **Makefile** — comandos para instalar, limpar, sincronizar dependências e rodar.

