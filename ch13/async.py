import asyncio
import time
import aiohttp
from aiohttp import ClientSession
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# List of URLs to fetch
URLS = [
    'https://www.python.org',
    'https://www.github.com',
    'https://www.stackoverflow.com',
    'https://www.reddit.com',
    'https://www.wikipedia.org',
    'https://www.nodejs.org',
    'https://www.rust-lang.org',
    'https://golang.org',  # Fixed URL for Go
    'https://www.mozilla.org',
    'https://www.postgresql.org'
]


async def fetch_url(url: str, session: ClientSession) -> tuple:
    """Fetch content from a URL and return the URL and response status"""
    try:
        start_time = time.time()
        async with session.get(url) as response:
            # Just get the first chunk of content
            content = await response.read()
            content_sample = content[:1024]  # Just take the first 1024 bytes for analysis
            elapsed = time.time() - start_time
            logger.info(f"Fetched {url} with status {response.status} in {elapsed:.2f} seconds")
            return url, response.status, elapsed
    except Exception as e:
        logger.error(f"Error fetching {url}: {str(e)}")
        return url, f"Error: {str(e)}", None


async def fetch_all_urls(urls: list) -> list:
    """Concurrently fetch all URLs"""
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(fetch_url(url, session))

        # Execute all tasks concurrently and gather results
        results = await asyncio.gather(*tasks)
        return results


async def process_with_semaphore(urls: list, limit: int = 5) -> list:
    """Fetch URLs with a limit on concurrent connections using semaphore"""
    semaphore = asyncio.Semaphore(limit)
    async with aiohttp.ClientSession() as session:
        tasks = []

        async def fetch_with_semaphore(url):
            async with semaphore:  # Only allow `limit` concurrent requests
                return await fetch_url(url, session)

        for url in urls:
            tasks.append(fetch_with_semaphore(url))

        results = await asyncio.gather(*tasks)
        return results


async def main():
    logger.info(f"Starting to fetch {len(URLS)} URLs")

    # Method 1: Fetch all URLs without limiting concurrency
    start_time = time.time()
    logger.info("Method 1: Fetching without limits")
    results = await fetch_all_urls(URLS)
    elapsed = time.time() - start_time
    logger.info(f"Completed all unrestricted fetches in {elapsed:.2f} seconds")

    # Method 2: Fetch with a concurrency limit using semaphore
    logger.info("\nMethod 2: Fetching with semaphore (max 3 concurrent connections)")
    start_time = time.time()
    results_limited = await process_with_semaphore(URLS, limit=3)
    elapsed = time.time() - start_time
    logger.info(f"Completed all semaphore-controlled fetches in {elapsed:.2f} seconds")

    # Compare and print results summary
    logger.info("\nResults Summary:")

    # Create a table-like output of results
    logger.info("-" * 80)
    logger.info(f"{'URL':<35} | {'Status':<10} | {'Time (s)':<10}")
    logger.info("-" * 80)

    for url, status, elapsed_time in results:
        status_str = str(status)
        time_str = f"{elapsed_time:.2f}" if elapsed_time else "N/A"
        logger.info(f"{url[:35]:<35} | {status_str:<10} | {time_str:<10}")


if __name__ == "__main__":
    asyncio.run(main())