#!/usr/bin/env python3

# Install:
# sudo pip3 install docker

import docker
import subprocess

client = docker.from_env()

containers = client.containers.list()
containers.sort(key=lambda c: c.name)

i = 0
choiceList = []
for c in containers:  
  if True:
  #if 'php' in c.name or 'systemd' in c.name:
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



