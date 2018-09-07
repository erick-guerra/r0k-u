import re
import requests
import urllib.parse
from RokuAPI import RokuAPI

class VideoStream(RokuAPI):
    stream_url = "http://{}:8060/input/15985?t=v&u="
    yt_url = "http://{}:8060/launch/837?contentID={}"
    yt_re_id = "(?<==).*"

    def push_video(self, vid_url):
        if "youtube" in vid_url:
            p = re.compile(self.yt_re_id)
            m = p.search(vid_url)
            requests.post(self.yt_url.format(self.ro_ip, m.group()))
            print("This is youtube video id: {}".format(m.group()))
        else:
            vid_url_enc = urllib.parse.quote_plus(vid_url)
            requests.post(url=self.stream_url.format(self.ro_ip) + vid_url_enc)
            print(self.stream_url.format(self.ro_ip) + vid_url_enc)
