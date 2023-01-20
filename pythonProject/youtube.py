from pytube import YouTube

url="https://www.youtube.com/watch?v=2Vv-BfVoq4g"
yt=YouTube(url)

video=yt.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first()

video.download('E:/youtube video download')
print('SUCESSFULLY DOWNLOAD')