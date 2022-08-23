# CoDrone-Edu
Tutorial on how to set up any CoDrone-Edu Products
# Step 1: VS Code and GitHub Setup 
## -- Software Installation
Download Visual Studio Code from "https://code.visualstudio.com/download" and Git from "https://git-scm.com/downloads". 
## -- GitHub Integration with VS Code 
Go to Extensions and look for $\textbf{GitHub Pull Requests and Issues}$, install that. You will see a GitHub icon pop up on the left of VS Code, click on it and sign in to your GitHub account. 
## -- Cloning the CoDrone-Edu repository 
Directly clone the repository using "https://github.com/JefferyZhou-98/CoDrone-Edu.git" and select a location of the cloned repo on your pc. Now you will have access to all the files from this repo and make changes or edits to them. 

# Step 2: Python Installation
## -- Downloading Python
Download and install Python 3.7.8 x64 exe version from "https://www.python.org/downloads/release/python-378"
## -- Python Version Environment
Go to your download folder and you will see $\textbf{python-3.7.8-amd64}$. Rename the file so that it says $\textbf{python-3.7.8}$.
## -- Python Interpreter Path Selection 
Open the simple_takeoff.py code and you will see a default Python version in the bottom right corner of the screen which may or maynot already be $\textbf{3.7.8}$. If not, click on it and select $\textbf{Enter Interpreter Path}$ where you will paste in the path of the previously downloaded Python 3.7.8 exe file. 
## -- Pip Install Packages
Go to the command line of the VS Code and copy in the following:
```
pip install codrone_edu
pip install numpy
pip install sympy
pip install matplotlib
pip install pandas
pip install seaborn
```
# Step 3: Run simple_takeoff.py
