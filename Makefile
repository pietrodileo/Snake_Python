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

# Target per fare il push delle modifiche al repository remoto
push:
	@echo "Pushing changes to remote repository"
	git push --set-upstream origin master

# Target per eliminare il virtual environment
clean:
	@echo "Removing the Virtual Environment"
	rmdir /s /q $(VENV_NAME) __pycache__

# Target for displaying the remote repository URLs
remote:
	@echo "Displaying remote repository URLs"
	git remote -v

# Target for displaying the commit log
log:
	@echo "Displaying commit log"
	git log

# Target for creating a new branch
new-branch:
	@echo "Creating new branch"
	git branch $(name)

# Target for checking out a branch
checkout:
	@echo "Checking out branch"
	git checkout $(name)

# Target for pushing a branch to the remote repository
push-branch:
	@echo "Pushing branch to remote repository"
	git push -u $(remote) $(name)

# To use these targets, you need to specify the name of the branch and the name of the remote repository 
# as variables when you run the make command
# make checkout name=new-feature
# make push-branch name=new-feature remote=origin