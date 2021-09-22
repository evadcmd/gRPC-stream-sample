FROM python:3.9 AS server
ENV APPDIR /opt/grpc_example/
WORKDIR ${APPDIR}
# install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
	cd /usr/local/bin && \
	ln -s /opt/poetry/bin/poetry && \
	poetry config virtualenvs.create false
# Copy using poetry.lock* in case it doesn't exist yet
COPY pyproject.toml poetry.lock* ${APPDIR}
RUN poetry install --no-dev --no-root
COPY grpc_example/ ${APPDIR}
ENTRYPOINT ["python", "server.py"]

FROM envoyproxy/envoy:v1.17.1 AS proxy
COPY envoy.yaml /etc/envoy/envoy.yaml
CMD /usr/local/bin/envoy -c /etc/envoy/envoy.yaml