#!/usr/bin/env python3

# Install:
# sudo pip3 install docker

import docker
import subprocess
import argparse
from colorama import Fore, Back, Style

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--all", action='store_const', const=True)
args = parser.parse_args()

client = docker.from_env()

containers = client.containers.list()
containers.sort(key=lambda x: x.name, reverse=False)

i = 0
choiceList = []

for c in containers:  
  if args.all or 'php' in c.name or 'systemd' in c.name or 'db' in c.name or 'nginx' in c.name:
    print(i, c.name)
    choiceList.append(c.name)
    i = i + 1

print("\n")

print(Style.DIM + "If the container you are looking for is not on the list, run the command with -a.")

print(Style.NORMAL + Fore.GREEN + "Enter container number: ")

try:
  choice = input()
except KeyboardInterrupt:
  print(Fore.RESET + "\nGoodbye")
  exit()

print(Fore.RESET)

try:
  choice = int(choice)
except ValueError as ve:
  print(Fore.RED + "Not a number." + Fore.RESET)
  exit()

if choice < 0 or choice >= i:
  print(Fore.RED + "Wrong choice" + Fore.RESET)
  exit()

cmdStr = "docker exec -it " + choiceList[choice] + " bash"
subprocess.run(cmdStr, shell=True)
exit()
