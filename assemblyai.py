import requests
import json
import os


class SGUTrans:
    def __init__(self):
        self.api_key = os.environ['asemblyai_api_key']
        self.url = 'https://api.assemblyai.com/v2/transcript/'
        self.headers = {
            "authorization": self.api_key
        }

    def get_status(self, id):
        endpoint = self.url + str(id)
        response = requests.get(endpoint, headers=self.headers)

        res = json.dumps(response.json(), indent=3)

        status = response.json()['status']

        print(res)
        print(status)


SGUTrans().get_status('icb47y7t9-2aa0-485e-b8b7-73f0930f7562')

# endpoint = "https://api.assemblyai.com/v2/transcript"

# json = {
#     "audio_url": "https://s3-us-west-2.amazonaws.com/blog.assemblyai.com/audio/8-7-2018-post/7510.mp3"
# }

# headers = {
#     "authorization": "9879d0404bcf45698658f0a51cd77317",
#     "content-type": "application/json"
# }

# response = requests.post(endpoint, json=json, headers=headers)

# print(response.json())


# endpoint = "https://api.assemblyai.com/v2/transcript/icb6net15-727c-4b20-b18b-f76a7ac4f003"

# headers = {
#     "authorization": "9879d0404bcf45698658f0a51cd77317",
# }

# response = requests.get(endpoint, headers=headers)

# print(response.json())

# endpoint = "https://api.assemblyai.com/v2/transcript"

# json = {
#     "audio_url": "https://media.libsyn.com/media/skepticsguide/skepticast2021-03-06.mp3"
# }

# headers = {
#     "authorization": "9879d0404bcf45698658f0a51cd77317",
#     "content-type": "application/json"
# }

# response = requests.post(endpoint, json=json, headers=headers)

# response_json = response.json()
# # response_json = json.dumps(response.json(), indent=1)
# print(response_json)
# endpoint = 'https://api.assemblyai.com/v2/transcript/icb47y7t9-2aa0-485e-b8b7-73f0930f7562'
# headers = {
#     "authorization": "9879d0404bcf45698658f0a51cd77317",
# }

# response = requests.get(endpoint, headers=headers)

# res = json.dumps(response.json(), indent=3)

# status = response.json()['status']

# print(res)
# print(status)
