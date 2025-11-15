import subprocess
import csv
import re

params = [1, 10, 20, 50, 100, 1000]
runs = 3
url = "http://tinyinsta-benchmark.ew.r.appspot.com/api/timeline?user=user1&limit=20"

with open("conc/conc.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["PARAM", "AVG_LAT_MS", "RUN", "FAILED"])

    for concurrent in params:
        amount = concurrent
        for r in range(1, runs + 1):
            print(f"Running test: {concurrent} concurrent, run {r}...")

            result = subprocess.run(
                ["hey", "-n", str(amount), "-c", str(concurrent), url],
                capture_output=True,
                text=True
            )
            output = result.stdout

            # Extraire latence moyenne
            match_lat = re.search(r"Average:\s+([\d\.]+)\s+secs", output)
            avg_lat = float(match_lat.group(1)) * 1000 if match_lat else None  # convert to ms

            # Extraire erreurs
            match_fail = re.search(r"Non-2xx responses:\s+(\d+)", output)
            failed = int(match_fail.group(1)) if match_fail else 0

            writer.writerow([concurrent, avg_lat, r, failed])
            print(f"Done: AVG_LAT={avg_lat} ms, FAILED={failed}")
