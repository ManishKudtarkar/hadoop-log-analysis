
#!/usr/bin/env python3
import sys

# Mapper: reads log lines and emits (IP, 1)
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    # Extract IP address (first field in log)
    parts = line.split()
    ip = parts[0]

    # Output key-value pair
    print(f"{ip}\t1")
