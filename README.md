# Crypto-Introduction
An interactive Web Application to introduce Caesar and Vigenère ciphers 

## Run Locally 
To run this Application locally: 
* Download Python 2.7 [Python 2.7](https://www.python.org/downloads/)
* Download [Web2Py](http://www.web2py.com/init/default/download)
* Open Web2Py - You are required to give a password - Click on **start server**
* Open Web2Py Web Interface (typically accessible via 127.0.0.1:8000)  
* On the right-hand-side, look for the heading - **Upload and install packed application** 
* Under **Application Name**, give an appropriate name
* Now, you need to give the source code. Under **Get from URL**, add _https://github.com/arjuntherajeev/Crypto-Introduction.git_
* Click on **Install**
* After installation, the Application will be visible under **Installed Applications**
* Open it! 

## Extending the Application 
Extending, modifying or fixing bugs is strongly encouraged!

## Main Areas of Code 
This is a Web2Py Web Application written in Python 2.7. 
Web2Py is an MVC (Model-View-Controller) Framework with lots of rich features.
This Application **DOES NOT** make use of a data store. Hence, a _model_ is not used.

The Controller (found at `Crypto-Introduction/controllers/default.py`) contains the definitions of functions which correspond to various actions in the Application.
The View (found at `Crypto-Introduction/views/default/index.html`) contains the HTML required to render the main Web Page of the Application. 

## Fixing Errors
In the above section (__Run Locally__), you _may_ face an Error saying that `GitPython` module is missing. 
To fix: 
* Open a CLI (CMD in Windows)
* Get the `GitPython` package using `pip` - `pip install GitPython`
* If `pip` is **Not Found** - use the complete path; for example - `C:\Python27\Scripts\pip.exe install GitPython`
