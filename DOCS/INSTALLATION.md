# Thank you for choosing Hunter-Toolkit!

<br>

### INSTALLATION/USAGE: 

---

<img src="https://github.com/Keyj33k/Hunter-Toolkit/blob/main/imgs/installation.gif?raw=true"/>

---

Clone the repository:
``` 
git clone https://github.com/Keyj33k/Hunter-Toolkit.git
```

---

### Automated Installation (Debian-/based)

- Change path to the Hunter-Toolkit directory:
    
    ```
    cd Hunter-Toolkit
    ```

- Run the installer:

    ```
    bash installer
    ```
    
### Automated Installation (Termux)

- Change path to the Hunter-Toolkit directory:
    
    ```
    cd Hunter-Toolkit
    ```

- Run the installer:

    ```
    bash installer-termux
    ```

### Manually Installation (Debian-/based)

1) Make sure you have CURL installed:<br>
    -> We need curl to get the http header from the server.<br>
    -> If curl is not installed, use the following commands:
    ``` 
    sudo apt-get update && sudo apt-get full-upgrade -y
    ``` 
    ``` 
    sudo apt-get install -y curl
    ```

2) Make sure you have PYTHON3 installed<br>
    -> We need python3 to run this toolkit<br>
    -> If python3 is not installed, use the following commands:
    ``` 
    sudo apt-get update && sudo apt-get full-upgrade -y
    ``` 
    ``` 
    sudo apt-get install python3 python3-pip
    ``` 
   
3) Now you need to install the needed python modules/requirements
    - Change path to the Hunter-Toolkit directory:
    
    ```
    cd Hunter-Toolkit/req/
    ```

    - Install the requirements:   

    ``` 
    pip install -r requirements.txt
    ```
    
### Manually Installation (Termux)

1) Make sure you have CURL installed:<br>
    -> We need curl to get the http header from the server.<br>
    -> If curl is not installed, use the following commands:
    ``` 
    pkg update -y && pkg install curl -y
    ```

2) Make sure you have PYTHON3 installed<br>
    -> We need python3 to run this toolkit<br>
    -> If python3 is not installed, use the following commands:
    ``` 
    pkg update -y && pkg install python3 -y
    ``` 
   
3) Now you need to install the needed python modules/requirements
    - Change path to the Hunter-Toolkit directory:
    
    ```
    cd Hunter-Toolkit/req/
    ```

    - Install the requirements:   

    ``` 
    pip install -r requirements.txt
    ```

### If the steps above are done, then you are ready for running the Hunter-Toolkit

- Use this command:
    
    ```
    python3 gate.py
    ``` 
  
## Update the pentesting assistant (Debian-/based):

- Change path to the Hunter-Toolkit directory and type:

    ```
    cd Hunter-Toolkit
    ```
    
- Run the updater

    ```
    bash updater
    ```
    
## Update the pentesting assistant (Termux):

- Change path to the Hunter-Toolkit directory and type:

    ```
    cd Hunter-Toolkit
    ```
    
- Run the updater

    ```
    bash updater-termux
    ```

NOTE: Use Ctrl+C to return to the menu or exit the Hunter-Toolkit.

### DISCLAIMER: 

---

    The following isn't some silly blah blah or anything. It's a serious warning.
    Always remember that port scanning etc. can be illegal if you don't have any
    permissions to do that. You can end up in jail for being a blackhat.
    Make the internet a safer place.

    -> This tool is for ethical purposes only.
    -> I'm not responsible for your actions.
    -> Don't hack anyone without permissions.
    -> With great force follows great responsibility.



