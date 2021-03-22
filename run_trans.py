from transcribe import SGUTrans

sgutrans = SGUTrans()
links = sgutrans.read_all_podcasts_data_json()[:2]
print(links)
# SGUTrans().get_status('ic074h0f7-39f8-4550-b347-d645dcb3b2a6')
# # SGUTrans().submit('https://media.libsyn.com/media/skepticsguide/skepticast2021-02-27.mp3')

# SGUTrans().get('ic074h0f7-39f8-4550-b347-d645dcb3b2a6')
# SGUTrans().get_status('ic074h0f7-39f8-4550-b347-d645dcb3b2a6')
# SGUTrans().get_transcript('ic074h0f7-39f8-4550-b347-d645dcb3b2a6')

# # SGUTrans().get('icb47y7t9-2aa0-485e-b8b7-73f0930f7562')
# # SGUTrans().get_status('icb47y7t9-2aa0-485e-b8b7-73f0930f7562')
# # SGUTrans().get_transcript('icb47y7t9-2aa0-485e-b8b7-73f0930f7562')
