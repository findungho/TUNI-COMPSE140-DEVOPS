### Exercise 5.1 Docker Compose

### How to run
1. Git clone repo
`git clone git@github.com:findungho/TUNI-COMPSE140-DEVOPS.git`
2. Navigate for exercise folder
`cd TUNI-COMPSE140-DEVOPS/5.1\ Docker\ Compose`
3. Run docker-compose command to build
`docker-compose up –build`
5. Test:
`curl localhost:8001`

- The result will look like this:
    ```
    Hello came from 172.20.0.1:55220 to 172.20.0.3:8001
    Hello came from 172.20.0.3:45870 to 172.20.0.2:8002
    ```
6. Stop and remove all containers/images:
`docker-compose down --rmi all`