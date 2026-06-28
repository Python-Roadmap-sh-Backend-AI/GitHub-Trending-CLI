import argparse
from ast import main
import requests
import sys
from datetime import datetime, timedelta

BASE_URL = "https://api.github.com/search/repositories"

def get_data_from_duration(duration):
    today = datetime.now()
    durations = {
        "day":today - timedelta(days=1),
        "week": today - timedelta(days=7),
        "month": today - timedelta(days=30),
        "year": today - timedelta(days=365)
    }

    return durations.get(duration)

def fetch_repositories(duration, limit):
    start_date = get_data_from_duration(duration)
    if not start_date:
        raise ValueError(
            f"Invalid duration: {duration}. Valid options are: day, week, month, year."
        )
    query_data = start_date.strftime("%Y-%m-%d")

    params = {
        "q": f"created:>{query_data}",
        "sort": "stars",
        "order": "desc",
        "per_page": limit
    }

    try:
        reponse = requests.get(
            BASE_URL,
            params=params
            timeout=10

            response.raise_for_status()
            data = response.json()
            return data.get("items", [])[:limit]

        )
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from GitHub API: {e}")
        sys.exit(1)
    
    except ValueError as ve:
        print(f"Value error: {ve}")
        sys.exit(1)
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
     
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from GitHub API: {e}")
        sys.exit(1)

    

if __name__ == "__main__":
    main()