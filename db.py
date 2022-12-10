import firebase_admin
from firebase_admin import firestore
from firebase_admin import storage

# Tracks initialization.
_DATABASE_INSTANCE = None
_BUCKET_INSTANCE = None

STORAGE_BUCKET = 'aio-project-jon-misc'


def _get_database_client():
    global _DATABASE_INSTANCE
    if not _DATABASE_INSTANCE:
        initialize()
        _DATABASE_INSTANCE = firestore.client()
    return _DATABASE_INSTANCE


def _get_storage_client():
    global _BUCKET_INSTANCE
    if not _BUCKET_INSTANCE:
        initialize()
        _BUCKET_INSTANCE = storage.bucket(STORAGE_BUCKET)
    return _BUCKET_INSTANCE


def initialize():
    if not firebase_admin._apps:
        firebase_admin.initialize_app()


def get_job_status(job_id: str) -> dict:
    # get the database connection
    db = _get_database_client()

    # get the document from the "job_status" collection
    doc = db.collection("job_status").document(job_id).get()

    # return the document as a dictionary
    return doc.to_dict()


def put_job_status(job_id: str, job_status: str) -> None:
    # get the database connection
    db = _get_database_client()

    # create a document in the "job_status" collection
    db.collection("job_status").document(job_id).set({"job_status": job_status})


def get_file(job_id: str) -> bytes:
    bucket = _get_storage_client()
    # get the file from the "files" bucket
    file = bucket.get_blob(job_id)

    # return the file content as bytes
    return file.download_as_bytes()


def put_file(job_id: str, file_path: str) -> None:
    bucket = _get_storage_client()
    # upload the file to the "files" bucket
    bucket.blob(job_id).upload_from_filename(file_path)

