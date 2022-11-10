from urllib.request import urlopen, Request
import os


url = 'https://test.com/loremipsum/123/456/video0.ts'       # The url of one of the .ts files
url = '/'.join(url.split("/")[:-1])
video_id = url.split('/')[5]

if not os.path.exists('Downloads'):
    os.makedirs('Downloads')

num = 0
try:
    while True:
        file = f'{url}/video{num}.ts'               # Change according to .ts filenames
        print(file)
        req = Request(url=file, headers={'User-Agent': 'Mozilla/5.0'})

        webpage = urlopen(req).read()
        save_path = os.path.join('Downloads', f'video_{video_id}.ts')
        open(save_path, 'ab').write(webpage)
        num += 1

except Exception as e:
    print(e)
