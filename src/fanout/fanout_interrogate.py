import aiohttp
import asyncio
import time
import csv
import os

# Paramètres
concurrent = 50
runs = 3
base_url = "http://tinyinsta-benchmark.ew.r.appspot.com/api/timeline"

# Crée le dossier si nécessaire
os.makedirs("fanout", exist_ok=True)

async def fetch(session, url):
    start = time.monotonic()
    try:
        async with session.get(url) as resp:
            await resp.text()
            return (time.monotonic() - start) * 1000, 0
    except:
        return None, 1

async def run_test(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        return await asyncio.gather(*tasks)

with open("fanout/fanout.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["RUN", "AVG_TIME", "FAILED"])

    for r in range(1, runs + 1):
        print(f"Running test: 50 concurrent users, run {r}...")

        # Chaque utilisateur distinct interroge sa timeline
        urls = [f"{base_url}?user=user{i}&limit=20" for i in range(concurrent)]

        results = asyncio.run(run_test(urls))

        latencies = [lat for lat, fail in results if lat is not None]
        failures = sum(fail for lat, fail in results)
        avg_lat = sum(latencies) / len(latencies) if latencies else None

        print(f"Done: AVG_LAT={avg_lat} ms, FAILED={failures}")
        writer.writerow([r, avg_lat, failures])
