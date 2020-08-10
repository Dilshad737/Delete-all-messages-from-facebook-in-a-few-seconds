# Delete all messages from facebook in a few seconds 2019/2020


## Python 3 Installation

- Download the [latest version](https://www.python.org/downloads/)

## Installing packages using pip and virtual environments

### Windows

```sh
$ py -m pip --version
$ pip 9.0.1 from c:\python36\lib\site-packages (Python 3.6.1)
```

- Installing virtualenv

```sh
$ py -m pip install --user virtualenv
```

- Creating a virtual environment

```sh
$ py -m venv env
```

- Activating a virtual environment

```sh
$ .\env\Scripts\activate
```
### Linux and macOS

```sh
$ python3 -m pip install --user --upgrade pip
$ python3 -m pip --version
```

- Installing virtualenv

```sh
$ python3 -m pip install --user virtualenv
```

- Creating a virtual environment

```sh
$ python3 -m venv env
```

- Activating a virtual environment

```sh
$ source env/bin/activate
```

## Selenium

- Install

```sh
$ pip install selenium
```

- Selenium WebDriver


| **Browser** |                                       **Link**                                      |
|:-----------:|:-----------------------------------------------------------------------------------:|
|   Chrome:   |    [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)   |
|    Edge:    | [EdgeDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) |
|   Firefox:  |           [FirefoxDriver](https://github.com/mozilla/geckodriver/releases)          |
|    Safari   |     [SafariDriver](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)    |


- Setup path

```sh
$ mkdir -p $HOME/bin
$ mv chromedriver $HOME/bin
$ echo "export PATH=$PATH:$HOME/bin" >> $HOME/.bash_profile
```

**Note**: _macOS Catalina error_
```
“chromedriver” cannot be opened because the developer cannot be verified.

macOS cannot verify that this app is free from malware.

Safari downloaded this file today at xx:yy from chromedriver.storage.googleapis.com.
```

The problem is solved by the command below:
```sh
$ sudo spctl --master-disable
```


- Excample

```py
import time
from selenium import webdriver

driver = webdriver.Chrome('/path/to/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()
```

**Note**: _macOS Catalina error_
```
“chromedriver” cannot be opened because the developer cannot be verified.

macOS cannot verify that this app is free from malware.

Safari downloaded this file today at xx:yy from chromedriver.storage.googleapis.com.
```

The problem is solved by the command below:
```sh
$ sudo spctl --master-disable
```

## Start deleting messages from FACEBOOK

```sh
$ python3 delete_all_messages_from_facebook.py
```


