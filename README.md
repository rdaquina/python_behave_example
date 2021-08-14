# Install & Setup Environment

**_Pre-requisite:_** Git for Windows
    - 1: Download and Install Git for Windows `https://git-scm.com/download/win`
    - 2: Press Windows key, type `git`, right-click GitBash app, click `Run as Administrator`
    - 3: ** App lauches **

**_1:_** Clone the project
    - `git clone git@github.com:rdaquina/python_behave_example.git`

**_2:_** VS Code for Windows
    - 2.1: Download and Install the latest version of VS Code `https://code.visualstudio.com/download`
    - 2.2: Press Windows Key + R, type `cmd`, press Enter
    - 2.3: Type `code`, press Enter
    - 2.4: ** App lauches **

**_3:_** Download and Install Python
    - 3.1: Download and Install the latest version of Python `https://www.python.org/downloads/`
    - 3.2: Press Windows Key + R, type `cmd`, press Enter
    - 3.3: Type `python -V`, press Enter
    - 3.4: Python version should appear in the cmd prompt
    

**_4:_** Install and Update PIP
    - From vscode terminal, execute `python -m pip install --upgrade pip`

**_5:_** Install Behave and all dependencies listed on pip_installs.txt
    - From vscode terminal, execute `pip instal -r pip_installs.txt`

**_Install appropriate webdrivers_**
Download links for your webdrivers:
    | Browser  | Link                                                                   |
    | -------- | ---------------------------------------------------------------------- |
    | Chrome:  | https://chromedriver.chromium.org/downloads                            |
    | Firefox: | https://github.com/mozilla/geckodriver/releases                        |
    | Edge:    | https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/  |

**_Test execution from vscode terminal_**
    - `behave features/login.feature`

## Allure Reports 
    ** Pre-requisite **
    Install Allure
        - `Set-ExecutionPolicy RemoteSigned -scope CurrentUser`
        - `iwr -useb get.scoop.sh | iex`
        - `scoop install allure`
    
    ** Generate Report **
    Execute test and generate report files (.json) on `reports/` directory
        `behave -f allur_behave.formatter:AllureFormatter -o reports/ feature/login.feature`

    Generate Allure report
        `allure serve reports/`