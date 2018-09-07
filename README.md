#r0k-u

Fiddling around with the Roku api, wanted to create some automation. Utilizing 
[jcarbaugh/python-roku](https://github.com/jcarbaugh/python-roku) library as well as making some requests to Roku's API.  

At the moment, the script is automation a force off, where it turns off the Roku every time its on... for those pesky
children of the night. As well an extremely basic way to put both youtube a video urls to be streamed on the Roku.


***Please excuse my OOP, still a novice in implementing it, any notes/commits in making it more 'Pythonic' would be 
greatly appreciated***

###Getting Started:
> - Just run main.py

### Prerequisites:

jcarbough's module does have a device discovery method, but at the current moment I have failed to get it to work for me
properly so You have to manually insert the device's IP manually for now.

0. Device Target IP
1. [jcarbaugh/python-roku](https://github.com/jcarbaugh/python-roku)
2. BeautifulSoup
3. requests
4. pyfiglet

```sh
pip install python-roku
pip install beautifulsoup4
pip install requests
pip install pyfiglet
```
or equivalent in for your environment set-up

### TODO:
> * Add more functionality.
>  + App functionality
> - Clean up code.