# Day 3 Python Assignment
# Write a Network Ping Script using Python
# DESCRIPTION:
#       ping uses the ICMP protocol's mandatory ECHO_REQUEST datagram to elicit
#       an ICMP ECHO_RESPONSE from a host or gateway. ECHO_REQUEST datagrams
#       (“pings”) have an IP and ICMP header, followed by a struct timeval and
#       then an arbitrary number of “pad” bytes used to fill out the packet.

import subprocess
import platform

banner = """
╭━╮╱╭╮╭╮╱╱╱╱╱╱╭━┳╮╱╱╱╱╱╭━━╮╱╱╱╭╮╱╭╮
┃╋┣┳┫╰┫╰┳━┳━┳╮┃╋┣╋━┳┳━╮┃━━╋━┳┳╋╋━┫╰╮
┃╭┫┃┃╭┫┃┃╋┃┃┃┃┃╭┫┃┃┃┃╋┃┣━━┃━┫╭┫┃╋┃╭┫
╰╯┣╮┣━┻┻┻━┻┻━╯╰╯╰┻┻━╋╮┃╰━━┻━┻╯╰┫╭┻━╯
╱╱╰━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━╯╱╱╱╱╱╱╱╱╰╯by Nazu
  """
print(banner)
def ping(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping",param,"5",host]
    return subprocess.call(command)
host = str(input("Enter a Domain Example youtube.com: "))
print(ping(host))