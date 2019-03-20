### Solution:

1. I have choosen ansible as my config management tool for setting up ec2 instance/ec2 auto scaling group.

command to execute the playbook: 

   ansible-playbook -i hosts -ask-vault-pass provision-web-server.yml

2. I have created an ansible role aws_ec2_webserver which does the following:
   
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

