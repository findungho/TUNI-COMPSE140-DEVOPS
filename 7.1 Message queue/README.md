### Exercise 7.1 Message queue


### How to build
1. Clone the project
`git clone -b messaging https://github.com/findungho/TUNI-COMPSE140-DEVOPS.git`
2. Navigate for exercise folder
`cd TUNI-COMPSE140-DEVOPS/7.1\ Message\ queue/`
3. Run docker-compose
`docker-compose up -d`


### How to test
1. A text file will appear in the project root folder
`data.txt`
2. Do the curl command to localhost
`curl localhost:8080`
3. Stop and remove all containers & images
`docker-compose down --rmi all`