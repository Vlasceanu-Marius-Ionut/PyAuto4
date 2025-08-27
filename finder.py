private_prefixes = ["192.", "10.", "172."]
private = []
public = []

with open("ips.txt") as f:
    ips = f.read().splitlines()

for ip in ips:
    if ip.startswith(tuple(private_prefixes)):
        private.append(ip)
    else:
        public.append(ip)

print("\nAll Private IPs:", private)
print("\nAll Public IPs:", public)
