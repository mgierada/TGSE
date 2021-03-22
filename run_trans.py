from transcribe import SGUTrans

sgutrans = SGUTrans()
# sgutrans.submit_all_transcripts(812, 814)
sgutrans.downlad_all_transcripts()


# to_be_removed
# links = sgutrans.read_all_podcasts_data_json()
# print(len(links))
# print(links)
# for link in links:
#     sgutrans.submit(link)


# ids = sgutrans.get_all_ids_submitted()
# for id in ids:
#     print('Getting translation for {}'.format(id))
#     sgutrans.get(id)
#     print('Done!')
# print('All transcripts downloaded successfully')

# qxgvpsa0e-42cb-4076-af44-ca5312f4445d
# qxz654b4s-9703-4b7b-b58f-e101b87475b8
# SGUTrans().get('qxgvpsa0e-42cb-4076-af44-ca5312f4445d')
# # SGUTrans().submit('https://media.libsyn.com/media/skepticsguide/skepticast2021-02-27.mp3')

# SGUTrans().get('ic074h0f7-39f8-4550-b347-d645dcb3b2a6')
# SGUTrans().get_status('ic074h0f7-39f8-4550-b347-d645dcb3b2a6')
# SGUTrans().get_transcript('ic074h0f7-39f8-4550-b347-d645dcb3b2a6')

# # SGUTrans().get('icb47y7t9-2aa0-485e-b8b7-73f0930f7562')
# # SGUTrans().get_status('icb47y7t9-2aa0-485e-b8b7-73f0930f7562')
# # SGUTrans().get_transcript('icb47y7t9-2aa0-485e-b8b7-73f0930f7562')
