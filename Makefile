# Variabili
PYTHON = python3
MAIN_FILE = main.py
VENV_NAME = VirtualEnvironment
# command (cmd) "keep" (/k) mantiene attivo il vEnv all'interno del prompt dei comandi e mantiene la finestra attiva per eseguire altri comandi
VENV_ACTIVATE = .\$(VENV_NAME)\Scripts\activate
REQUIREMENTS = requirements.txt

# Target predefinito
all: run

# Target per eseguire il gioco
run:
	@echo "Run Mode"
	$(PYTHON) $(MAIN_FILE)

# Target per creare il virtual environment e installare le dipendenze
install: venv
	@echo "Installing dependencies"
	cmd /k "$(VENV_ACTIVATE) && pip install -r $(REQUIREMENTS)"

# Target per creare il virtual environment
venv:
	@echo "Building a Virtual Environment"
	if not exist $(VENV_NAME) (python -m venv $(VENV_NAME))

# Target per fare il pull dal repository remoto
pull:
	@echo "Pulling changes from remote repository"
	git pull

# Target per fare il commit delle modifiche locali
commit:
	@echo "Committing changes to local repository"
	git add .
	git commit -m "Aggiornamento del codice - $(date)"
# To enter a custom commit message, simply execute the 'git commit' command without the '-m' option

# Target per eliminare il virtual environment
clean:
	@echo "Removing the Virtual Environment"
	rmdir /s /q $(VENV_NAME) __pycache__