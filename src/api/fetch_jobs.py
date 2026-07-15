import requests
from src.utils.config import API_URL, HEADERS


def fetch_jobs():
    """
    Fetch job data from the RemoteOK API.
    Returns a Python list.
    """

    response = requests.get(API_URL, headers=HEADERS)

    response.raise_for_status()

    return response.json()


if __name__ == "__main__":
    jobs = fetch_jobs()

    print(f"Fetched {len(jobs)-1} jobs successfully.")