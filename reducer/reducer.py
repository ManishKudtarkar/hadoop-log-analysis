
#!/usr/bin/env python3
import sys

current_ip = None
current_count = 0

# Reducer: sums values for each IP
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    ip, count = line.split("\t", 1)
    count = int(count)

    if current_ip == ip:
        current_count += count
    else:
        if current_ip:
            print(f"{current_ip}\t{current_count}")
        current_ip = ip
        current_count = count

# Output last IP
if current_ip:
    print(f"{current_ip}\t{current_count}")
