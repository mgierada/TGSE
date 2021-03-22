import requests
import json
import os


class SGUTrans:
    def __init__(self) -> None:
        self.api_key = os.environ['asemblyai_api_key']
        self.url = 'https://api.assemblyai.com/v2/transcript'
        self.headers = {
            "authorization": self.api_key
        }
        self.current_dir = os.getcwd()
        self.response_dir_name = 'responses'
        self.transcript_dir_name = 'transcripts'
        self.response_fname = 'response.json'
        self.transcript_fname = 'transcript.txt'
        self.response_dir = os.path.join(
            self.current_dir, self.response_dir_name)
        self.transcript_dir = os.path.join(
            self.current_dir, self.transcript_dir_name)

    def submit(
            self,
            audio_url: str) -> None:
        '''Submit audio_url for converstion to speech (json format)

        Parameters
        ----------
        audio_url : str
            an url to audio file
            e.g.
            >>> audio_url = 'https://media.libsyn.com/media/skepticsguide/
                            skepticast2021-03-06.mp3'

        '''
        self.headers['content-type'] = 'application/json'

        json_submit = {
            "audio_url": audio_url
        }

        response = requests.post(
            self.url, json=json_submit, headers=self.headers)
        print(response.json())

        id = response.json()['id']
        response_path = os.path.join(
            self.response_dir, id + '_' + self.response_fname)
        with open(response_path, 'w') as f:
            json.dump(response.json(), f, indent=4)

        # res = json.dumps(response.json(), indent=4)
        # print(res)

    def get(
            self,
            id: str) -> None:
        ''' Get a GET request for submitted audio

        Parameters
        ----------
        id : str
            id of the submitted audio_url

        '''
        endpoint = self.url + '/' + str(id)
        response = requests.get(endpoint, headers=self.headers)

        os.makedirs(self.response_dir, exist_ok=True)

        response_path = os.path.join(
            self.response_dir, id + '_' + self.response_fname)

        with open(response_path, 'w') as f:
            json.dump(response.json(), f, indent=4)

    def get_status(
            self,
            id: str) -> None:
        ''' Get status of conversion to speach.

        The status goes from "queued" to "processing" to "completed" or
        sometimes "error"

        Parameters
        ----------
        id : str
            id of the submitted audio_url

        '''
        response_path = os.path.join(
            self.response_dir, id + '_' + self.response_fname)

        with open(response_path, 'r') as f:
            data = json.load(f)
        print(data['status'])

    def get_transcript(
            self,
            id: str) -> None:
        ''' Get transcript and store it in ./transcripts dir.

        The status goes from "queued" to "processing" to "completed" or
        sometimes "error"

        Parameters
        ----------
        id : str
            id of the submitted audio_url

        '''
        response_path = os.path.join(
            self.response_dir, id + '_' + self.response_fname)
        transcript_path = os.path.join(
            self.transcript_dir, id + '_' + self.transcript_fname)
        os.makedirs(self.transcript_dir, exist_ok=True)

        with open(response_path, 'r') as f:
            data = json.load(f)
            text = data['text']
        with open(transcript_path, 'w') as ff:
            ff.write(text)

    def read_all_podcasts_data_json(self, json_fname='all_podcasts_data.json'):
        path_to_json = os.path.join(os.getcwd(), 'source', json_fname)
        with open(path_to_json, 'r') as f:
            all_podcasts = json.load(f)

        links_to_mp3 = [episode['link_to_mp3']
                        for episode in all_podcasts.values()]

        return links_to_mp3
