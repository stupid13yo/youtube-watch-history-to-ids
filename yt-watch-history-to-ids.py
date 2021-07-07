import json

WATCH_HISTORY_FILE = 'watch-history.json'
WATCH_IDS_FILE = 'watch-history-ids.txt'

with open(WATCH_HISTORY_FILE) as f:
    history = json.load(f)

videoIds = set()

for item in history:
    videoId = item['titleUrl'].split('=')[-1]
    videoIds.add(videoId)

with open(WATCH_IDS_FILE, 'a+') as f:
    f.write('\n'.join(videoIds) + '\n')
