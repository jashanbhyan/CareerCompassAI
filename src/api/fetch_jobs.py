import requests
import pandas as pd
import os

print("Fetching data from RemoteOK API...")

url = "https://remoteok.com/api"

headers = {
    "User-Agent": "CareerCompassAI"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("API Connected Successfully!")

    data = response.json()

    # The first element contains metadata, so skip it
    jobs = data[1:]

    # Convert JSON to DataFrame
    df = pd.DataFrame(jobs)

    # Create data/raw folder if it doesn't exist
    os.makedirs("data/raw", exist_ok=True)

    # Save CSV
    df.to_csv("data/raw/jobs.csv", index=False)

    print(f"Total Jobs Collected: {len(df)}")
    print("Dataset saved to data/raw/jobs.csv")

    # Display first 5 rows
    print("\nFirst 5 Records:")
    print(df.head())

else:
    print("Failed to connect.")
    print("Status Code:", response.status_code)