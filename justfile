send:
    uv run python src/client.py

generate:
    uv run python -m grpc_tools.protoc --proto_path=. \
        --python_out=src \
        --grpc_python_out=src \
        --mypy_grpc_out=src \
        --mypy_out=src \
        schema/service.proto
