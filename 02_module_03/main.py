import csv
host_1 = ["workstation.local", "192.168.25.46"]
host_2 = ["webserver.cloud", "10.2.5.6"]
hosts = [host_1, host_2]
with open("hosts.csv", "w") as hosts_csv:
	writer = csv.writer(hosts_csv)
	writer.writerows(hosts)
    