import csv

csvfile = open('result.csv', 'r')

csvreader = csv.reader(csvfile, delimiter='\n')


ssids = {}
macs = {}

for row in csvreader:

    row = row[0].split(";")
    mac = row[1]
    ssid = row[3]

    if mac not in macs.keys():
        macs[mac] = []

    if(ssid not in macs[mac]):
        macs[mac].append(ssid)

    if ssid not in ssids.keys():
        ssids[ssid] = []

    if(mac not in ssids[ssid]):
        ssids[ssid].append(mac)


print("\n********************")
print("MAC")
print("********************")

for mac in macs.keys():
    print(mac,':',macs[mac])


print("\n********************")
print("SSID")
print("********************")
for ssid in ssids.keys():
    print(ssid,':',ssids[ssid])

print("\n\n")