FROM python:3.13-slim AS builder
ENV APPDIR=/opt/grpc_example/
WORKDIR ${APPDIR}

RUN pip install --no-cache-dir uv
COPY pyproject.toml uv.lock* ${APPDIR}
RUN uv sync --frozen --no-dev

FROM python:3.13-slim AS server
ENV APPDIR=/opt/grpc_example/
WORKDIR ${APPDIR}

COPY src ${APPDIR}
COPY --from=builder ${APPDIR}/.venv/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
ENTRYPOINT ["python", "server.py"]

FROM envoyproxy/envoy:v1.37.1 AS proxy
COPY envoy.yaml /etc/envoy/envoy.yaml
CMD ["/usr/local/bin/envoy", "-c", "/etc/envoy/envoy.yaml"]
