import grpc
from concurrent import futures
import medical_pb2
import medical_pb2_grpc
import pytesseract
from pdf2image import convert_from_bytes
from PIL import Image
import io


class OCRService(medical_pb2_grpc.OCRServiceServicer):
    def ExtractText(self, request, context):
        file_bytes = request.file_bytes
        file_type = request.file_type.lower()

        try:
            if file_type == "pdf":
                images = convert_from_bytes(file_bytes)
                text = ""
                for img in images:
                    text += pytesseract.image_to_string(img) + "\n"
            elif file_type == "image":
                image = Image.open(io.BytesIO(file_bytes))
                text = pytesseract.image_to_string(image)
            else:
                context.set_details("Unsupported file type.")
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                return medical_pb2.OCRResponse()

            return medical_pb2.OCRResponse(text=text)
        except Exception as e:
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return medical_pb2.OCRResponse()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    medical_pb2_grpc.add_OCRServiceServicer_to_server(OCRService(), server)
    server.add_insecure_port('[::]:50051')
    print("OCR server is running on port 50051...")
    server.start()
    server.wait_for_termination()
