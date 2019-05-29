import json

import requests


def send_messag_example():
    resp = requests.post("http://sms-api.luosimao.com/v1/send.json",
                         auth=("api", "6980fad72b3ec043ef216e067fce9bb7"),
                         data={
                             "mobile": "18580008582",
                             "message": "王思聪，短信轰炸，自主研发 !【铁壳测试】"
                         }, timeout=3, verify=False)
    result = json.loads(resp.content)
    print(result)


if __name__ == '__main__':
    send_messag_example()



