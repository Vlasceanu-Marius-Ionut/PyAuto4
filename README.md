IP Classification Script

This Python script reads a list of IP addresses from a text file (ips.txt) and separates them into private and public IPs.
Features
Reads IPs from a file.
Detects if an IP is private (192.*, 10.*, 172.*) or public.
Stores private and public IPs in separate lists.
Prints each IP with its type in the console.
Shows complete lists of private and public IPs at the end.

How It Works
The script reads all IPs from ips.txt.

For each IP:
Checks if it starts with the private prefixes.
Adds it to the corresponding list (private or public).
Prints the IP and its type in the console.

After processing all IPs, it prints the full lists of private and public IPs.
