import threading
import time
import library

def start_job_and_poll(job_id: str, video_url: str, file_path: str) -> None:
    # print "starting job"
    print("starting job")

    # start the job in a separate thread
    thread = threading.Thread(target=library.start_job, args=(job_id, video_url, file_path))
    thread.start()

    # while waiting, check the job status every 10 seconds
    while thread.is_alive():
        job_status = (library.get_job_status(job_id) or {}).get("job_status")
        print(f"job status: {job_status}")

        if job_status == "complete":
            break

        time.sleep(10)

    # print "job finished"
    print("job finished")

    # retrieve the file data
    file_data = library.get_file(job_id)

    # print the file location
    print(f"file location: {file_path}")

    # return the file data
    return file_data



data = start_job_and_poll("test_job", "https://www.youtube.com/watch?v=s-MsZo02dos", "/tmp/file.mp4")
print(f"File Data: {data}")
