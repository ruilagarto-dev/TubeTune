VENV_NAME = myvenv
PYTHON = $(VENV_NAME)/bin/python
PIP = $(VENV_NAME)/bin/pip

install:
	@echo "Instalando FFmpeg no sistema..."
	@if ! command -v ffmpeg > /dev/null 2>&1; then \
		sudo apt update && sudo apt install -y ffmpeg; \
	else \
		echo "FFmpeg já instalado."; \
	fi
	@echo "Criando ambiente virtual..."
	test -d $(VENV_NAME) || python3 -m venv $(VENV_NAME)
	@echo "Atualizando pip..."
	$(PIP) install --upgrade pip
	@if [ -f "requeriments.txt" ]; then \
		echo "Instalando dependências do requeriments.txt..."; \
		$(PIP) install -r requeriments.txt; \
	else \
		echo "AVISO: requeriments.txt não encontrado, instalando dependências básicas..."; \
		$(PIP) install yt-dlp pydub; \
	fi

clean:
	@echo "Limpando ambiente..."
	@rm -rf $(VENV_NAME)
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type f -name "*.py[co]" -delete
	@rm -rf .pytest_cache .mypy_cache .coverage dist build *.egg-info

sync:
	@echo "Gerando requeriments.txt..."
	$(PIP) freeze > requeriments.txt

pip:
	$(PIP) list

run:
	@echo "Iniciando aplicação..."
	$(PYTHON) src/main.py

.PHONY: install clean sync pip run

