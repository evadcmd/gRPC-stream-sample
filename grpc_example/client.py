import os
import logging

import grpc

from grpc_src.example_pb2 import Param
from grpc_src.example_pb2_grpc import FuncStub

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s %(levelname)s] %(message)s',
    datefmt='%Y%m%d %H:%M:%S'
)

URL = f'{"server" if os.environ.get("IN_CONTAINER", False) else "localhost"}:50050'

params = [
    Param(x=1, y=3, z=5),
    Param(x=2, y=4, z=6),
    Param(x=-1, y=-3, z=-5),
    Param(x=-2, y=-4, z=-6),
]

def test_simple():
    with grpc.insecure_channel(URL) as channel:
        stub = FuncStub(channel)
        res = stub.Simple(Param(x=1, y=3, z=5))
        logging.info(f'[simple] resp:{res.value}')

def test_stream_resp():
    with grpc.insecure_channel(URL) as channel:
        stub = FuncStub(channel)
        for res in stub.StreamResp(Param(x=1, y=3, z=5)):
            logging.info(f'[stream-resp] resp:{res.value}')

def test_stream_req():
    with grpc.insecure_channel(URL) as channel:
        stub = FuncStub(channel)
        res = stub.StreamReq(iter(params))
        logging.info(f'[stream-req] resp:{res.value}')

def test_bistream():
    with grpc.insecure_channel(URL) as channel:
        stub = FuncStub(channel)
        for res in stub.BiStream(iter(params)):
            logging.info(f'[bistream] resp:{res.value}')


if __name__ == '__main__':
    test_simple()
    test_stream_req()
    test_stream_resp()
    test_bistream()
