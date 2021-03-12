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
        self.current_dir = os.getcwd()
        self.response_dir_name = 'responses'
        self.transcript_dir_name = 'transcripts'
        self.response_fname = 'response.json'
        self.response_dir = os.path.join(
            self.current_dir, self.response_dir_name)

    def submit(self, audio_url):
        self.headers['content-type'] = 'application/json'

        json = {
            "audio_url": audio_url
        }

        response = requests.post(self.url, json=json, headers=self.headers)
        print(response.json())
        res = json.dumps(response.json(), indent=4)
        print(res)

    def get(self, id):
        endpoint = self.url + str(id)
        response = requests.get(endpoint, headers=self.headers)

        os.makedirs(self.response_dir, exist_ok=True)

        response_path = os.path.join(
            self.response_dir, id + '_' + self.response_fname)

        with open(response_path, 'w') as f:
            json.dump(response.json(), f, indent=4)

    def get_status(self):
        with open(self.response_fname, 'r') as f:
            data = json.load(f)
        print(data['status'])

    def get_transcript(self):
        with open(self.response_fname, 'r') as f:
            data = json.load(f)
            text = data['text']
        with open('transcript.txt', 'w') as ff:
            ff.write(text)


SGUTrans().get('icb47y7t9-2aa0-485e-b8b7-73f0930f7562')
# SGUTrans().get_status()
# SGUTrans().get_transcript()

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
