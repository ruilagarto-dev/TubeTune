# TubeTune
<P align = "Center">
    <img src= "docs/Tubetune.png" alt= "logotipo" width = "200">
</p>


TubeTune é uma aplicação simples para transferir áudio de vídeos ou playlists do YouTube em formato MP3. A interface gráfica é feita em Tkinter, e o processo de download é gerido pela biblioteca yt-dlp.

```bash
⚠️ **Atenção:** Esta aplicação é **suportada apenas no Linux Ubuntu**. Não foi validade noutros sistemas operativas.
```

## Captura de Tela
<P align = "Center">
    <img src= "docs/tubetune_tela_principal.png" alt= "docs/tubetune_tela_principal.png" width = "400">
</p>



## Funcionalidade
- Transferir áudio de vídeos individuais do YouTube.
- Transferir áudio de playlists completas.
- Escolha da pasta de destino para guardar os ficheiros de áudio.
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

### Pré-requisitos
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
2. Selecione a pasta de destino onde os ficheiros MP3 serão guardados.
3. Clique em **"Descarregar Música"** para descarregar um vídeo único ou em **"Descarregar Playlist"** para descarregar todos os vídeos da playlist.
4. Aguarde a conclusão. Mensagens informativas serão exibidas durante o processo.


## Estrutura do Projeto
- **src/main.py** — ponto de entrada da aplicação.
- **modules/view.py** — interface gráfica com Tkinter.
- **modules/controller.py** — lógica de controle e validação.
- **modules/model.py** — gerenciamento do download usando yt-dlp.
- **Makefile** — comandos para instalar, limpar, sincronizar dependências e rodar.

