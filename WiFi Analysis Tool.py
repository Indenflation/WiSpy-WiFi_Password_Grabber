import subprocess
import webbrowser


# Hostname And Date
hostname = subprocess.getoutput('hostname')
date = subprocess.getoutput('date /t')




# Wifi Passwords
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]



# IPv4
IPv4 = subprocess.getoutput('ipconfig | findstr /i "IPv4"')

# IPv6
IPv6 = subprocess.getoutput('ipconfig | findstr /i "IPv6"')

# Defult Gateway
gateway = subprocess.getoutput('ipconfig | findstr /i "Gateway"')








# ------------------Writing To Text File







# Opening .txt 
text_file = open("output.txt", "w")

# Write Basic Info 
text_file.write("\n xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \n")
text_file.write(hostname)
text_file.write('\n')
text_file.write(date)
text_file.write("\n xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \n")

# Write WiFi Passwords To .txt
text_file.write("\n\n\n\n             Profile Name & Password \n")
text_file.write("\n xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \n")

for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        text_file.write("{:<30} - {:<}   \n".format(i, results[0]))
    except IndexError:
        text_file.write("{:<30}|  {:<}".format(i, ""))

text_file.write("\n xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \n\n\n")





#Write IP's To .txt
text_file.write("\n\n\n                Current Addresses \n")
text_file.write("\n xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \n")
text_file.write("IPv4 \n")
text_file.write(IPv4)
text_file.write("\n IPv6 \n")
text_file.write(IPv6)
text_file.write("\n Gateway \n")
text_file.write(gateway)
text_file.write("\n xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \n")

# Close The File
text_file.close()



