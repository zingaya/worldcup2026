# World Cup 2026 Countdown Project

This is a personal project, with the idea to do some tests, combine some of my knowledge, and learn a little more. And also, to provide some proof of my diverse skills.

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

There is no goal in this project, just combine those items and make them work thogether.\
I did not test all scenarios, and many conditions to catch errors are missing.

In the other hand, I am also somewhat limited due to my home server capacity, and my free time available to deploy a whole new subnet with a separate firewall and router, to automate IP tables, portforwaring rules, load balancer, and even use a DNS.

## How it works, what it does

There are 2 Azure Pipelines. One will use this repository, and the other will use a repository ([zabbix-azure-pipeline](https://github.com/zingaya/zabbix-azure-pipeline)) where its goal is to send data to Zabbix after the first one finishes.

This pipeline has all the jobs in order to:
- Create a new LXC in Proxmox; taking into account the next available VMid
- Install prerequisites in the LXC; python, pip, git
- Clone this repository in the LXC
- Install the python script as a service in the LXC
- Swap LXC hostnames, the production and the staging
- Remove the old LXC; finally setting up the static IP to the new LXC, minimizing any downtime
- In case of error; it will undo the creation of the new LXC.

The project in ADO, uses a variable group. To avoid using any IP, key, or any private data that will could exposed in this public repository.\
Additionally, as I do not own an Azure Subscription I am not able to create an Azure Key Vault. But **do not hesitate to use the Azure Key Vault** in order to secure any key like the Personal Access Token (PAT).

Anyway, this is just a test, in a test environment.

There are 2 agent pools created. One pool will use this pipeline, and its agent is installed in the Proxmox Server.\
The other pool, that uses the pipeline for Zabbix, where the agent is installed in the Zabbix Server.

## About the files

**worldcup2026countdown.py**

This is a simple Python script that calculates the remaining time until the World Cup 2026 and returns the result in a JSON format.\
The JSON data will be used later in Zabbix.

**worldcup2026countdown.service**

As the LXC is based on Debian 10, where uses Systemd, it is need to copy this file under /etc/systemd/system/ to enable the script to run as a service.

**azure-pipelines.yml**

The YAML file for the Azure Pipeline, that contains all the jobs.
