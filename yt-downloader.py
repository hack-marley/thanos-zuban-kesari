from pytube import YouTube

def download_youtube_video(url, path):
    try:
        yt = YouTube(url)
        highest_quality = yt.streams.get_highest_resolution()

        print(f"Downloading: {yt.title} to {path}")
        highest_quality.download(filename=path)
        print("Download completed!!")
    except Exception as e:
        print(e)

# Define the URL of the video and the directory path you want to download it into
url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'  # Replace with your YouTube video URL
path = '/Users/kothari/Documents/trial/vid.mp4'  # Replace with the desired directory path

download_youtube_video(url, path)