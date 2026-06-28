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

    

if __name__ == "__main__":
    main()