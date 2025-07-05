This is a small application which, given an excel spreadsheet containing IP addresses along with their corresponding subnet masks, produces a summary report with information on the given IP addresses such as their CIDR notation, their corresponding network address, the broadcast address of their corresponding network, and the number of usable host addresses within their network's address space. Included is also a Dockerfile which allows for the containerization of the application using Docker containers.

---

The Python script uses the following modules:
- pandas
- ipaddress
- matplotlib

---

### To run the application locally, run the following terminal command from within the barq-devops-subnet-task directory:
```
python subnet_analyzer.py
```

### To build a docker image for this application, run the following terminal command from within the barq-devops-subnet-task directory:
```
docker build -t <image tag> .
```

### To run a docker container based on the image, run the following terminal command:
```
docker run <image tag>
```