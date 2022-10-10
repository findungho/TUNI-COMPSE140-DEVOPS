### Exercise 5.1 Docker Compose

### How to run
1. Git clone repo
2. Navigate for exercise folder
3. Run docker-compose command to build
`docker-compose up –build`
5. Test:
`curl localhost:8001`
6. The result will be like this:
```
Hello came from 172.20.0.1:55220 to 172.20.0.3:8001
Hello came from 172.20.0.3:45870 to 172.20.0.2:8002
```