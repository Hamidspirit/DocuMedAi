import grpc
import medical_pb2
import medical_pb2_grpc
from pathlib import Path
import sys


def run(file_path: str):
    # Infer file type
    ext = Path(file_path).suffix.lower()
    file_type = "pdf" if ext == ".pdf" else "image"

    # Read file content
    with open(file_path, "rb") as f:
        file_bytes = f.read()

    # Connect to gRPC server
    channel = grpc.insecure_channel("localhost:50051")
    stub = medical_pb2_grpc.OCRServiceStub(channel)

    request = medical_pb2.OCRRequest(
        file_bytes=file_bytes,
        file_type=file_type
    )

    try:
        response = stub.ExtractText(request)
        print("=== Extracted Text ===")
        print(response.text)
    except grpc.RpcError as e:
        print(f"gRPC failed: {e.code()} - {e.details()}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ocr_client.py path_to_file")
    else:
        run(sys.argv[1])
