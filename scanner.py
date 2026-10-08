import socket

print("=================================")
print("     VULNERABILITY SCANNER")
print("=================================")

target = "127.0.0.1"

ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 3306, 8080]

report = []

report.append("VULNERABILITY SCANNER REPORT")
report.append("============================")
report.append("Target: " + target)
report.append("")

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((target, port))

    if result == 0:
        message = "Port " + str(port) + " is OPEN"
        print(message)
        report.append(message)
    else:
        message = "Port " + str(port) + " is CLOSED"
        print(message)
        report.append(message)

    sock.close()

report.append("")
report.append("Scan completed.")

with open("report.txt", "w") as file:
    for line in report:
        file.write(line + "\n")

print()
print("Scan completed.")
print("Report saved as report.txt")