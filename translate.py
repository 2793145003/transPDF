import json
import time
import requests

def translate(txt):
    url = "http://translate.google.cn/translate_a/single?client=gtx&dt=t&dj=1&ie=UTF-8&sl=EN&tl=zh_CN"
    params={
        'q': txt
    }
    result = requests.get(url, params)
    trans = ""
    for s in json.loads(result.text)["sentences"]:
        trans += s["trans"]
    time.sleep(0.5)
    return trans