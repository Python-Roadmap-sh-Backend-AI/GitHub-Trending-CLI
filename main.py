import argparse
import requests
import sys
from datetime import datetime, timedelta

BASE_URL = "https://api.github.com/search/repositories"


def get_data_from_duration(duration):
    today = datetime.now()
    durations = {
        "day": today - timedelta(days=1),
        "week": today - timedelta(days=7),
        "month": today - timedelta(days=30),
        "year": today - timedelta(days=365),
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
        "per_page": limit,
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("items", [])[:limit]

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from GitHub API: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"Value error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


def display_repositories(repositories):
    if not repositories:
        print("No repositories found.")
        return

    print("\n" + "=" * 40 + "\nTop Repositories:\n" + "=" * 40)
    for repo in repositories:
        name = repo.get("name")
        description = repo.get("description") or "No description provided."
        language = repo.get("language") or "Not specified"
        stars = repo.get("stargazers_count", 0)
        url = repo.get("html_url")
        print(
            f"Name: {name}\n"
            f"Description: {description}\n"
            f"Language: {language}\n"
            f"Stars: {stars}\n"
            f"URL: {url}\n"
            f"{'-' * 40}"
        )


def main():
    parser = argparse.ArgumentParser(
        description="Fetch top GitHub repositories based on creation date."
    )
    parser.add_argument(
        "--duration",
        choices=["day", "week", "month", "year"],
        default="week",
        help="Duration to filter repositories (day, week, month, year).",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=20,
        help="Number of repositories to fetch (default: 20).",
    )

    args = parser.parse_args()
    if args.limit <= 0:
        print("Error: limit must be greater than 0")
        sys.exit(1)

    repositories = fetch_repositories(args.duration, args.limit)
    display_repositories(repositories)


if __name__ == "__main__":
    main()