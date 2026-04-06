FROM python:3.13-slim AS server
ENV APPDIR=/opt/grpc_example/
WORKDIR ${APPDIR}

# install uv
RUN pip install --no-cache-dir uv
# copy dependency files first (for docker layer cache)
COPY pyproject.toml uv.lock* ${APPDIR}
# install dependencies
RUN uv sync --frozen --no-dev

COPY grpc_example/ ${APPDIR}
ENTRYPOINT ["/opt/grpc_example/.venv/bin/python", "server.py"]

FROM envoyproxy/envoy:v1.37.1 AS proxy
COPY envoy.yaml /etc/envoy/envoy.yaml
CMD /usr/local/bin/envoy -c /etc/envoy/envoy.yaml