import time
import pychromecast




from gtts import gTTS
def makeMp3(text):
    mp3_path = "greeting.mp3"
    tts = gTTS(text=text, lang='ja')
    tts.save(mp3_path)
    return mp3_path

def castMp3(mp3_url):
    mc = cast.media_controller
    mc.play_media(mp3_url, 'audio/mp3')
    mc.block_until_active()
    mc.pause()
    time.sleep(2)
    mc.play()

def castMp3FromText(text):
    mp3_path = makeMp3(text)
    url  = "http://192.168.50.234:8000/"
    mp3_url = f"{url}{mp3_path}"
    castMp3(mp3_url)

def main(text):
    castMp3FromText(text)

import sys
# main
if __name__ == '__main__':
    # コマンドライン引数を取得
    args = sys.argv
    text = args[1]

    # List chromecasts on the network, but don't connect
    services, browser = pychromecast.discovery.discover_chromecasts()
    # Shut down discovery
    pychromecast.discovery.stop_discovery(browser)
    # Discover and connect to chromecasts named Living Room
    chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=["折尾"])
    # [cc.friendly_name for cc in chromecasts]
    cast = chromecasts[0]
    # Start worker thread and wait for cast device to be ready
    cast.wait()

    main(text)

    # Shut down discovery
    pychromecast.discovery.stop_discovery(browser)
