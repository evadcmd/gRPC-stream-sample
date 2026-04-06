send:
    uv run python grpc_example/client.py

generate:
    uv run python -m grpc_tools.protoc -I ./proto --python_out=grpc_example/grpc_src --grpc_python_out=grpc_example/grpc_src proto/example.proto