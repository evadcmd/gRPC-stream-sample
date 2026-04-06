# gRPC demo

https://grpc.io/  
simple gRPC demo code using port: 50050

including:

- single request -> single response
- single request -> stream response
- stream request -> single response
- stream request -> stream response

## run demo-gRPC-server and demo-gRPC-client in containers

(in project folder)

```bash
$ docker-compose up -d --build
```

```bash
$ python grpc_sample/client.py
```

### demo-gRPC-client -> demo-gRPC-server

```bash
$ docker-compose exec server /bin/bash
```

```bash
$ python client.py
```

## stop containers && delete images

```bash
$ docker-compose down
```
