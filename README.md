# tools

## development note

```
# create env
conda create -n <env_name> python=3.8

# activate the environment
conda activate <env_name> 

# extract the package list to requirements.txt
pip freeze > requirements.txt

# install the required library
pip install -r requirements.txt

# deactivate the environment
conda deactivate

# delete env
conda env remove -n <env_name> 

pyinstaller --name application-offline --onefile main.py
```
