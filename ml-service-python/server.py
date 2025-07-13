import grpc
from concurrent import futures
from app import server as medical_server
import generated.medical_pb2_grpc as pb2_grpc


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_MedicalAnalyzerServicer_to_server(
        medical_server.MedicalAnalyzer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
