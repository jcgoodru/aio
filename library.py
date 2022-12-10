import db
import dl
import glob


def start_job(job_id: str, video_url: str, file_path: str) -> None:
    # update the job status to "in_progress"
    db.put_job_status(job_id, "in_progress")

    # download the remote file
    dl.download_youtube_video(video_url, file_path)

    # save the local file to the database
    db.put_file(job_id, glob.glob(f"{file_path}*")[0])

    # update the job status to "complete"
    db.put_job_status(job_id, "complete")


def get_job_status(job_id: str) -> dict:
    return db.get_job_status(job_id)


def get_file(job_id: str) -> dict:
    return db.get_file(job_id)

