# About
## Quick overview
KMD Policy Tool is our solution for [Orlen 3A task](https://hackathon.orlen.pl/zad3a.html) at [Hackyeah 2019](https://hackyeah.pl/).

## Task
> The solution should collect data about automation server and workstation configuration, compare the collected configuration with the predefined model configuration and on this basis prepare a report. Data collection (i.a. audit policies, users, network interfaces, disk space, OS patches, AV, installed applications, launched websites) should be initiated manually and the results should be available in a legible form, e.g. in tabular form. The model configuration should be entered into the solution manually and stored in it under unique names. The solution must enable comparison of the collected configuration with the predefined model configuration and generate the report in a clear form. If the part relating to the model configuration is not provided, the report should contain the appropriate information.**(...)**

## Technologies
- Python - easy to develop and multiplatform language. You can find it in server.
- Powershell - built into Windows (since XP SP2), miminal interference on workstations with Windows OS.
- Docker - set of *platform-as-a-service* products that use OS-level virtualization to deliver software in packages called containers. What does it mean for our app? Server components are isolated (more secure) and you need only one command to run entire server.
- RavenDB - no-sql database engine. By using no-sql we are able to create dynamic structures for policies and computer reports.
- React - javascript framework which we use to build user interface.

# Setup
## requirements
- software:
    - docker
    - docker-compose
- hardware:
    - You have to have anythink better than Samsung R540, ~~unless you want to have 10 min input lag~~.
    - *Linux is highly recommended for docker*


## Run
- Server:
    - Go to the main repository folder (where `docker-compose.yml` is located)
    - Run command `docker-compose up`
- Machines:
    - Run script `main.ps1` on machine, that you want to check.

And thats it! Api, database and web should running.


## Example Rules:
```json
[
	{
		"name": "Firewall - domain - disabled",
		"namespace": "firewall",
		"object": "['Profile'] == 'Domain'",
		"requirement": {
			"key": "Enabled",
			"value": 0
		}
	}, 
	{
		"name": "Firewall - private - enabled",
		"namespace": "firewall",
		"object": "['Profile'] == 'Private'",
		"requirement": {
			"key": "Enabled",
			"value": 1
		}
	}
 ]
 ```