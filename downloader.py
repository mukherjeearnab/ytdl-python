from youtube_dl import YoutubeDL

def download(dl_link):
    link = ''
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }
    with YoutubeDL(ydl_opts) as ydl:
        r = ydl.extract_info(dl_link, download=False)
        # return r
        return {'title': r['title'], 'url': r['url'], 'filename': r['title'] + '.mp3'}
