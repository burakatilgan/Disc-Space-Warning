import smtplib
import conf

# Print disk usage statistics
print("Disk usage statistics")
print(conf.subject)
print("Disk usage percentage: %", conf.path.percent)
print("Disk usage:  ", conf.path.used, "gb")
print("Disk Name:   ", conf.disk_name)
print("Disk IP:     ", conf.local_ip)

if 100 - conf.path.percent < conf.under_percentage:
    print("Remaining disc space %", conf.remaining_space_percentage)
    print(conf.message_low_disk_space)
    to = conf.receiver_mail
    user = conf.sender_mail
    pwd = conf.sender_password
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(user, pwd)
    header = 'To:' + to + '\n' + 'From: ' + user + '\n' + 'Subject:'+ conf.subject
    print(header)
    msg = header + '\n\n' + conf.message_low_disk_space + '\n\n'
    smtpserver.sendmail(user, to, msg)
    print('done!')
    smtpserver.quit()
