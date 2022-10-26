### Exercise 6.1 Ansible

### How to build
1. Clone the project
2. Navigate for exercise folder
`TUNI-COMPSE140-DEVOPS/6.1\ Ansible/`
3. Build Docker image
`docker build -t ansible .`


### How to test
1. Run first docker container from previous build image (name it as ansible1 and port 2022)
`docker run -d -p 2022:22 --name ansible1 ansible`
2. Add first container port to the hosts file (./inv/hosts)
`ansible1 ansible_host=127.0.0.1 ansible_user=ssldung ansible_port=2022 ansible_ssh_private_key_file=./.ssh/id_rsa`
3. Run the playbook
`ansible-playbook DevOps_6.1_ansible.yml`
4. Run second container from previous build image (name it as ansible2 and port 2222)
`docker run -d -p 2222:22 --name ansible2 ansible`
5. Add first container port to the hosts file (./inv/hosts)
`ansible2 ansible_host=127.0.0.1 ansible_user=ssldung ansible_port=2222 ansible_ssh_private_key_file=./.ssh/id_rsa`
Other configurations keep the same.
6. Run the playbook again
`ansible-playbook DevOps_6.1_ansible.yml`