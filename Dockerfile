FROM python:3.8-slim as server
ENV APPDIR /opt/app/
WORKDIR ${APPDIR}
COPY grpc_example/grpc_src/ ${APPDIR}/grpc_src/
COPY grpc_example/server.py ${APPDIR}
COPY Pipfile* ${APPDIR}
RUN pip install pipenv
RUN pipenv install --system --deploy
ENTRYPOINT ["python", "server.py"]

FROM python:3.8-slim as client
ENV APPDIR /opt/app/
WORKDIR ${APPDIR}
COPY grpc_example/grpc_src/ ${APPDIR}/grpc_src/
COPY grpc_example/client.py ${APPDIR}
COPY Pipfile* ${APPDIR}
RUN pip install pipenv
RUN pipenv install --system --deploy

