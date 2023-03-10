# Dokr

This simple script allows to access docker container by entering the container number from the list.

```
$ sudo dokr

1 my_great_container
2 php_hello_world
3 java_test_app
4 my_website

Enter container number:

```

# Installation

Install required python 3 packages.

```
pip3 install docker
```
You may need to install it with `sudo` if you access your docker containers with `sudo`.

Install the application

```
sudo cp dokr.py /usr/local/bin/dokr
sudo chmod a+x /usr/local/bin/dokr
```

# Run
```
dokr
```
You may need to run it with `sudo` if you access your docker containers with `sudo`.

# Filter containers

If you want to filter the containers list, just edit the script `/usr/local/bin/dokr`.

```
  if True:
  #if 'php' in c.name or 'systemd' in c.name:
``` 

Remove or comment the line `if True:` na uncomment the other one. Replace `php` and `systemd` with a strings you want to use to filter the container names. You can add more conditions.

# Buy me a coffee

It's hard to develop without a mug of coffee, help me have the black liquid always available ☕.

https://www.buymeacoffee.com/JakubDeveloper




