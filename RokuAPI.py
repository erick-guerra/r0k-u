import requests
import keyboard
from time import sleep
from roku import Roku
from bs4 import BeautifulSoup

#TODO: Add app management functionality


class RokuAPI(object):

    def __init__(self, ro_ip):
        self.ro_ip = ro_ip
        self.roku = Roku(self.ro_ip)

    def device_info(self):
        info_url = "http://{}:8060/query/device-info".format(self.ro_ip)
        req = requests.get(info_url)
        return req.content

    def my_device(self):
        content = self.device_info()
        soup = BeautifulSoup(content, "xml")
        mn = soup.find('model-number').string
        fdn = soup.find('friendly-device-name').string
        nn = soup.find('network-name').string
        wmac = soup.find('wifi-mac').string
        sv = soup.find('software-version').string
        sb = soup.find('software-build').string
        print("Device name: {}, Model: {}, Soft-version {}, Soft-Build {}\n"
              "Connected to {} [{}]".format(fdn, mn, sv, sb, nn, wmac))


    def get_info(self):
        content = self.device_info()
        soup = BeautifulSoup(content, "xml")
        for info in soup.find_all():
            print("{}:\n{}".format(info.name, info.string))

    def device_pw_state(self):
        content = self.device_info()
        soup = BeautifulSoup(content, "xml")
        state = soup.find('power-mode').string
        return state

class RokuRemote(RokuAPI):
    def remote(self):
        while True:
            if keyboard.is_pressed('q'):
                break
            elif keyboard.is_pressed('8'):
                self.roku.up()
                sleep(.3)
            elif keyboard.is_pressed('2'):
                self.roku.up()
                sleep(.3)
            elif keyboard.is_pressed('4'):
                self.roku.left()
                sleep(.3)
            elif keyboard.is_pressed('6'):
                self.roku.right()
                sleep(.3)
            elif keyboard.is_pressed('5'):
                self.roku.select()
                sleep(.3)

    def DenyRemote(self):
        state = self.device_pw_state()
        while True:
            sleep(10)
            if state == "PowerOn":
                self.roku._post('/keypress/Power')
            elif keyboard.is_pressed('q'):
                break
            else:
                pass

