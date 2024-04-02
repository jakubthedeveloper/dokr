#!/usr/bin/env python3

# Install:
# sudo pip3 install docker

import docker
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--all", action='store_const', const=True)
args = parser.parse_args()

client = docker.from_env()

containers = client.containers.list()

i = 0
choiceList = []
for c in containers:  
  if args.all or 'php' in c.name or 'systemd' in c.name or 'db' in c.name:
    print(i, c.name)
    choiceList.append(c.name)
    i = i + 1

print("\n")
print("Enter container number: ")

choice = input()

try:
  choice = int(choice)
except ValueError as ve:
  print("Not a number.")
  exit()

if choice < 0 or choice >= i:
  print("Wrong choice")
  exit()

cmdStr = "docker exec -it " + choiceList[choice] + " bash"
subprocess.run(cmdStr, shell=True)
exit()


