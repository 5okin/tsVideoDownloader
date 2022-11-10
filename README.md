# tsVideoDownloader

A simple script that downloads .ts video files, merging them into a single (.ts) file.

## Running it
Specify the url of of the .ts files, any file will do.
```python
url = 'https://test.com/loremipsum/123/456/video0.ts' 
```
You might also need to change the way the video_id is captured. This is used to automatically name the saved files. Alternatively you can change this to a simple string.
```python
video_id = url.split('/')[5]
```
In my specific use case the files were named Video0.ts, Video1.ts, ..., etc. If the file names do not follow this patern you have to change.
```python
file = f'{url}/video{num}.ts' 
```
## License

MIT
