import pyfiglet
from RokuAPI import RokuRemote
from VideoHandler import VideoStream

options = """
Please enter number of selection:
1. Push a url video to roku
2. Get device info
3. Deny remote
0. Quit

#More to be done
"""
banner = "ROK-U"
author = "      bash.sec"
banner_fig = pyfiglet.figlet_format(banner, font="cyberlarge")
author_fig = pyfiglet.figlet_format(author, font="cybermedium")


class Main(object):
    def __init__(self, ro_ip):
        self.ro_ip = ro_ip
        self.RokuAPI = RokuRemote(self.ro_ip)
        self.Video = VideoStream(self.ro_ip)
    def connect(self):
        #roku = RokuAPI(self.ro_ip)
        self.RokuAPI.device_info()

    def video(self, vid_url):
        self.Video.push_video(vid_url)

ro_ip = input("Please enter roku device IP address: \n")

status = False

while status == False:
    inst = Main(ro_ip)
    print("{}\n{}".format(banner_fig, author_fig))
    inst.connect()
    inst.RokuAPI.my_device()
    print(options)
    selection = int(input(""))
    if selection == 1:
        vid_url = input("Please enter vid url:\n")
        inst.video(vid_url)

    elif selection == 2:
        inst.RokuAPI.get_info()

    elif selection == 3:
        inst.RokuAPI.DenyRemote()

    elif selection == 0:
        status = True
