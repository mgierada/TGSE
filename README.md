![GitHub repo size](https://img.shields.io/github/repo-size/mgierada/sgu_transcript_generator)
[![Python package](https://github.com/mgierada/sgu_transcript_generator/actions/workflows/python-package.yml/badge.svg)](https://github.com/mgierada/sgu_transcipt_generator/actions/workflows/python-package.yml

![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/mgierada/sgu_transcript_generator
?label=version)
![GitHub last commit](https://img.shields.io/github/last-commit/mgierada/sgu_transcript_generator?label=last%20modified)
![GitHub](https://img.shields.io/badge/License-GPLv3-orange)
![GitHub top language](https://img.shields.io/github/languages/top/mgierada/sgu_transcript_generator?color=brightgreen)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/mgierada/sgu_transcript_generator.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/mgierada/sgu_transcript_generator/context:python)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/mgierada/sgu_transcript_generator.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/mgierada/sgu_transcript_generator/alerts/)

# SGU Transcripts & Search Engine (**SGU-TSE**)

A Django based search engine and transcripts generator for the Skeptics Guide to the Universe (SGU) podcast.

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

# Wish List

- [ ] better design
- [ ] set up an event listiner to check for new episodes, get detials, submit for transcription, get transcript and populate DB in automated fashion
- [ ] use timestaps to navigate to the exact moment in the audio file matching the query
- [ ] better transcripts quality
- [ ] improved search-engine by implementing a method to search for an almost exact match
- [ ] refactoring
- [ ] documentation

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
