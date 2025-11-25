import aiohttp
import asyncio
import time
import csv

params = [1, 10, 20, 50, 100, 1000]
runs = 3
base_url = "http://tinyinsta-benchmark.ew.r.appspot.com/api/timeline?limit=20"

async def fetch(session, url):
    start = time.monotonic()
    try:
        async with session.get(url) as resp:
            await resp.text()
            return (time.monotonic() - start) * 1000, 0
    except:
        return None, 1

async def run_test(concurrent):
    urls = [f"{base_url}&user=user{i}" for i in range(concurrent)]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        return await asyncio.gather(*tasks)

with open("conc/conc.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["PARAM", "AVG_TIME", "RUN", "FAILED"])

    for concurrent in params:
        for r in range(1, runs + 1):
            print(f"Running test: {concurrent} concurrent users, run {r}...")
            results = asyncio.run(run_test(concurrent))

            latencies = [lat for lat, fail in results if lat is not None]
            failures = sum(fail for lat, fail in results)

            avg_lat = sum(latencies) / len(latencies) if latencies else None

            print(f"Done: AVG_LAT={avg_lat} ms, FAILED={failures}")
            writer.writerow([concurrent, avg_lat, r, failures])
