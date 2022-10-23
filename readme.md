# create a env
Conda create -n <env_name> python=3.7
conda env list - to check all the envs
conda activate <env_name>
pip list - to check all the packages that are installed in the env
pip freeze > requirements.txt -- will save all the packages in the file

To install the packages in requirements file to a new enviornment - pip install -r requirements.txt
This is done after activating the needed environment in command prompt where we need to install these packages of specific version
