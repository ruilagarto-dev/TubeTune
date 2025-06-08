chmod +x Makefile

# TubeTune

TubeTune é uma aplicação simples para transferir aúdio de vídeos ou playlist do YOutube no formato MP3. A interface gráfica é feita em tkinter, e o processo de download é gerido pela biblioteca yt-dlp.

## Preview
![Tela principal do TUbeTune](docs/tubetune_tela_principal.png)

## Video Demonstração
[![Video de demostração]()]()



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


## Estrutura do Projeto

- **src/main.py** — ponto de entrada da aplicação.
- **modules/view.py** — interface gráfica com Tkinter.
- **modules/controller.py** — lógica de controle e validação.
- **modules/model.py** — gerenciamento do download usando yt-dlp.
- **Makefile** — comandos para instalar, limpar, sincronizar dependências e rodar.


## Licença

Este projeto é open-source. Sinta-se à vontade para modificar e distribuir.
