![Python package](https://github.com/mgierada/sgu_transcript_generator/actions/workflows/python-package.yml/badge.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/mgierada/sgu_transcript_generator?label=last%20modified)
![GitHub repo size](https://img.shields.io/github/repo-size/mgierada/sgu_transcript_generator)
![GitHub](https://img.shields.io/badge/License-GPLv3-orange)
![GitHub top language](https://img.shields.io/github/languages/top/mgierada/sgu_transcript_generator?color=brightgreen)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/mgierada/sgu_transcript_generator.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/mgierada/sgu_transcript_generator/context:python)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/mgierada/sgu_transcript_generator.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/mgierada/sgu_transcript_generator/alerts/)

# Transcripts & Search Engine (**TSE**)

A Django based search engine and transcripts generator currently applied to the Skeptics Guide to the Universe (SGU) podcast.

# Functionality

## Submit for transcription

![SubmitTranscripts](./media/submit_eps.gif)

## Get transcripts

![GetTranscripts](./media/download_eps.gif)

## Search

![Functionality](./media/functionality.gif)

<!-- ffmpeg -i screen_rec.mov -s 800x600 -pix_fmt rgb24 -r 10 -f gif - | gifsicle --optimize=3 --delay=1 > out.gif -->

# Like that project?

Consider becoming a patreon by clicking https://www.patreon.com/maciejgierada

# Contributions

Contributions are highly welcome! There is still a lot of work to be done!

# How to run local

SGU-TSA backend is Django based, so to run locally do:

```bash
# navigate to path where you will keep the project
cd path_to_install
# clone the repo (if you are planning to contribute, fork the repo and clone it)
git clone https://github.com/mgierada/sgu_transcript_generator.git
# enter the repo's root directory
cd sgu_transcript_generator
# create a virtual environment
python3 -m venv sgu-tse_venv
# activate the environment
source sgu-tse_venv/bin/activate
# upgrade pip
python3 -m pip install --upgrade pip
# install sgu-tse
python3 -m pip install -r requirements.txt
# run local server
python3 manage.py runserver
# open browser at http://127.0.0.1:8000/
```

# REST API

It is not my main goal to have a nice REST API at this moment, however, there are a couple of enpoints you can access. More will come later:

| endpoint                         |            feature             | method |
| -------------------------------- | :----------------------------: | -----: |
| `episodes/`                      |  get details of all episodes   |  `GET` |
| `episodes/<int:episode_number>/` | get details of a given episode |  `GET` |

# Wish List

- [ ] better design
- [ ] set up an event listiner to check for new episodes, get detials, submit for transcription, get transcript and populate DB in automated fashion
- [x] use timestaps to navigate to the exact moment in the audio file matching the query
- [x] better transcripts quality
- [ ] improved search-engine by implementing a method to search for an almost exact match
- [x] refactoring
- [x] documentation

# Tech Stack

- Python
- HTML/CSS
- JavaScript
- Django
- PostgreSQL
- Selenium
- Assemblyai
- Haystack
- Heroku
- CI/CD pipelines
