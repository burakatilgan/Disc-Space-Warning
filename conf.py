import socket

import psutil

path = psutil.disk_usage("/")
disk_name = socket.gethostname()
local_ip = socket.gethostbyname(disk_name)
# variables
gb = 1073741824
remaining_space_percentage = 100 - path.percent
remaining_space_percentage = str(round(remaining_space_percentage, 2))
remaining_space = path.used / gb
remaining_space = str(round(remaining_space, 2))

under_percentage = 5

# mail conf
# sender
sender_mail = "sender@gmail.com"
sender_password = "example-password"
# receiver
receiver_mail = "receiver@gmail.com"
# mail info
subject = 'Space Usage'
message_low_disk_space = " Disc Name: " + disk_name + "\n IP Address: " + local_ip + "\n Remaining Space: " + remaining_space + " GB\n Remaining Percentage: %"+ remaining_space_percentage
message_normal_disk_space = "Kalan kullanım alanı yeterli."

