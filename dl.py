import argparse
import youtube_dl

def download_youtube_video(video_url: str, download_path: str) -> None:
    ydl_opts = {
        "outtmpl": download_path
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

if __name__ == "__main__":
    # create an argument parser
    parser = argparse.ArgumentParser()

    # add an argument for the YouTube video URL
    parser.add_argument("video_url", help="the URL of the YouTube video to download")

    # add an argument for the download path
    parser.add_argument("download_path", help="the path where the video should be saved")

    # parse the arguments
    args = parser.parse_args()

    # call the download_youtube_video() function with the parsed arguments
    download_youtube_video(args.video_url, args.download_path)

