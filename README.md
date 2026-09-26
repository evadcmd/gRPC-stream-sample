# gRPC Stream Sample

A minimal Python [gRPC](https://grpc.io/) demo showing the four RPC call patterns, fronted by an
[Envoy](https://www.envoyproxy.io/) proxy that translates [gRPC-Web](https://github.com/grpc/grpc-web) to
plain gRPC.

## What's included

The `Func` service (defined in [`schema/service.proto`](schema/service.proto)) implements all four gRPC
patterns:

| RPC | Pattern |
| --- | --- |
| `Simple` | unary request -> unary response |
| `StreamResp` | unary request -> streaming response |
| `StreamReq` | streaming request -> unary response |
| `BiStream` | streaming request -> streaming response |

Both `Param` (`x`, `y`, `z`, all `int32`) and `Res` (`value: int32`) are simple integer messages, so each
handler just sums or streams `x + y + z` to keep the demo focused on the streaming mechanics rather than
business logic — see [`src/server.py`](src/server.py).

## Architecture

```
client.py --(grpc-web/gRPC)--> envoy proxy (:8070) --(gRPC)--> server.py (:50050)
```

- **server** — a Python `grpc` server (`src/server.py`) implementing `Func`, listening on `:50050`.
- **proxy** — an Envoy instance (config in [`envoy.yaml`](envoy.yaml)) that terminates gRPC-Web/CORS on
  `:8070` and forwards to the `server` container over plain gRPC. Envoy's admin UI is exposed on `:9901`.
- **client** — `src/client.py`, a script that calls all four RPCs against the proxy (or directly against a
  container running the server, when `IN_CONTAINER` is set).

Both images are built from the same multi-stage [`Dockerfile`](Dockerfile) (`server` and `proxy` targets),
and wired together by [`docker-compose.yml`](docker-compose.yml).

## Requirements

- [uv](https://docs.astral.sh/uv/) and [just](https://github.com/casey/just)
- Docker / Docker Compose

```bash
brew install uv just
```

## Running the demo

From the project root:

```bash
docker-compose up -d --build
```

This starts `grpc-demo-server` (port `50050`) and `grpc-envoy-proxy` (ports `8070` and `9901`).

Run the client against the proxy:

```bash
just send
```

You can also exec into the server container and run the client from there:

```bash
docker-compose exec server /bin/bash
python client.py
```

Stop everything and remove the built images:

```bash
docker-compose down
```

## Regenerating the protobuf/gRPC code

If you change [`schema/service.proto`](schema/service.proto), regenerate the Python stubs (including
mypy types) with:

```bash
just generate
```

This runs `grpc_tools.protoc` and writes the generated `*_pb2*.py(i)` files into `src/schema/`.

## Project structure

```
schema/service.proto      # RPC + message definitions
src/server.py              # Func service implementation
src/client.py               # exercises all four RPC patterns
src/schema/                 # generated protobuf/gRPC/mypy stubs
envoy.yaml                  # Envoy gRPC-Web proxy config
docker-compose.yml          # server + proxy containers
Dockerfile                   # multi-stage build: builder / server / proxy
justfile                     # `just send`, `just generate`
```