import subprocess
import csv
import re

params = [1, 10, 20, 50, 100, 1000]
runs = 3
url = "http://tinyinsta-benchmark.ew.r.appspot.com/api/timeline?user=user1&limit=20"

with open("conc.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["PARAM", "AVG_TIME", "RUN", "FAILED"])
    
    for concurrent in params:
        amount = concurrent   # total requests
        for r in range(1, runs + 1):
            print(f"Running test: {concurrent} concurrent, run {r}...")
            result = subprocess.run(
                ["ab", "-n", str(amount), "-c", str(concurrent), url],
                capture_output=True,
                text=True
            )
            output = result.stdout
            
            # Extraire le temps moyen (ms)
            match_time = re.search(r"Time per request:\s+([\d\.]+)\s+\[ms\]", output)
            avg_time = float(match_time.group(1)) if match_time else None
            
            # Extraire le nombre d'échecs
            match_failed = re.search(r"Failed requests:\s+(\d+)", output)
            failed = int(match_failed.group(1)) if match_failed else None
            
            writer.writerow([concurrent, avg_time, r, failed])
            print(f"Done: AVG_TIME={avg_time} ms, FAILED={failed}")
