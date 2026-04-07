from concurrent.futures import ThreadPoolExecutor

import grpc

from schema.service_pb2 import Param, Res
from schema.service_pb2_grpc import FuncServicer, add_FuncServicer_to_server


class Func(FuncServicer):
    def Simple(self, request, context):
        s = request.x + request.y + request.z
        return Res(value=s)

    def StreamReq(self, request_iterator, context):
        s = 0
        for param in request_iterator:
            s = param.x + param.y + param.z
        return Res(value=s)

    def StreamResp(self, request, context):
        for i in range(10):
            yield Res(value=i)

    def BiStream(self, request_iterator, context):
        for i, param in enumerate(request_iterator):
            s = param.x + param.y + param.z
            if i & 0b1:
                yield Res(value=s)


def serve():
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    add_FuncServicer_to_server(Func(), server)
    server.add_insecure_port("[::]:50050")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
