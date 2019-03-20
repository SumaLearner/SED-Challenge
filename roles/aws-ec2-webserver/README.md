Role Name
=========

ansible role aws_ec2_webserver creates aws ec2 instances and installs, configured apache to host a static web page 
   
	1. tasks/main.yml 
		- creates security group with ingress to allow connect on tcp port 22, 80, 443 and egres rules 
		- uses ec2 or ec2_asg module to launch ec2 instance or ec2 auto scaling group (to address scalability)
		- Add the newly created host to inventory so that we can contact it
		- Wait for SSH connection
		- execute tasks in webserver.yml
	2. tasks/webserver.yml
		- On the newly created ec2 istance install httpd
		- configure apache as below
		- copy the httpd.conf containing <virtualhost> config for https redirection
		- copy the index file to document root
		- copy self signed certficates under /etc/ssl
		- start and enable httpd 
	3. files/httpd.conf
	   files/mysite.crt
	   files/mysite.key
	   files/index.html

	4. vars/main.yml
	   vars/aws_keys.yml #### vaulted aws keys
Requirements
------------

The role uses the EC2 module, hence the VM on which this role is executed requires boto package to be intalled .

Role Variables
--------------
vars/main.yml: Config vars for ec2 instance launch 

instance_type: t2.micro
security_group:
image: ami-0b500ef59d8335eee
keypair: default
region: us-east-2

vars/aws_keys.yml #### vaulted aws keys

Dependencies
------------

NA

Example Playbook
----------------


example of how to use your:

---
- hosts: local
  connection: local #this makes sure it is local connection and doesnt need ssh 
  gather_facts: False 

- roles:
     - aws-ec2-webserver



command to execute the playbook: 

   ansible-playbook -i hosts -ask-vault-pass provision-web-server.yml
   
License
-------

BSD

Author Information
------------------

Suma Nataraj
