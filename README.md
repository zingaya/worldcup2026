# World Cup 2026 Countdown Project

This is a personal project, with the idea to do some tests, combine some of my knowledge, and learn more. Also, to provide some proof of my diverse skills.\
With this idea in mind, I created this project that uses:

- Python
- YAML
- Azure Pipelines
- Zabbix
- Linux
- Containerization (LXC with Proxmox)
- Bash
- Azure API
- Github repositories

There is no goal in this project, just combine those and make them work thogether.\
I did not test all scenarios, and many conditions to catch errors are missing.

In the other hand, I am also somewhat limited due to my home server capacity, and time to deploy a whole new subnet with a separate firewall and router, to further create some script to automate IP tables for portforwaring rules or even use a DNS.

## How it works, what it does

There are 2 Azure Pipelines. One will use this repository, and the other will use a repository ([zabbix-azure-pipeline](https://github.com/zingaya/zabbix-azure-pipeline)) where its goal is to send data to Zabbix after the first one finishes.

The pipeline has all the jobs in order to:
- Create a new LXC in Proxmox; taking into account the next available VMid
- Install prerequisites in the LXC; python, pip, git
- Clone this repository in the LXC
- Install the python script as a service in the LXC
- Swap LXC hostname, between the production and the staging; finally setting up a static IP
- Remove the old LXC
- In case of error; case of any bash script fails, it will undo the creation of the new LXC.

The project uses a variable group. To avoid using any IP, or key, or any private data exposed in this public repository.\
Besides, as I don not own an Azure Subscription I am not able to create an Azure Key Vault. **Do not hesitate to use the Azure Key Vault** in order to secure any key like the Personal Access Token (PAT).

Anyway, this is just a test, in a test environment.

## About the files

**worldcup2026countdown.py**

This is a simple Python script that calculates the remaining time until the World Cup 2026 and returns the result in a JSON format.\
The JSON data will be used later in Zabbix.

**worldcup2026countdown.service**

As the LXC is based on Debian 10, where uses Systemd, it is need to copy this file under /etc/systemd/system/ to enable the script to run as a service.

**azure-pipelines.yml**

The YAML file for the Azure Pipeline, that contains all the jobs.
