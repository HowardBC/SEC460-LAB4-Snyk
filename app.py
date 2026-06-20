"""Minimal application used for the SEC460 LAB4 SCA exercise."""

import urllib3


def fetch_status(url: str) -> int:
    """Return the HTTP status code for a simple GET request."""
    client = urllib3.PoolManager()
    response = client.request("GET", url, timeout=5.0)
    return response.status


if __name__ == "__main__":
    print(fetch_status("https://example.com"))
