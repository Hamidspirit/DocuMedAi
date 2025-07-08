# Backend-Dotnet

This is still in the works and it can be updated

## 🔐 1. Authentication & User Management

(Using ASP.NET Identity or JWT authentication)


| Method | Endpoint             | Description                              |
| ------ | -------------------- | ---------------------------------------- |
| POST   | `/api/auth/register` | Register a new user                      |
| POST   | `/api/auth/login`    | Login and receive JWT                    |
| GET    | `/api/user/profile`  | Get current user's profile               |
| PUT    | `/api/user/profile`  | Update profile information               |
| POST   | `/api/auth/logout`   | Logout (optional for token invalidation) |

## 📄 2. Medical Document Upload & Management


| Method | Endpoint                | Description                                |
| ------ | ----------------------- | ------------------------------------------ |
| POST   | `/api/documents/upload` | Upload a medical document (PDF/Image)      |
| GET    | `/api/documents`        | List all uploaded documents (for the user) |
| GET    | `/api/documents/{id}`   | Get details of a specific document         |
| DELETE | `/api/documents/{id}`   | Delete a document                          |

Accept multipart/form-data for file uploads. Store files in cloud/local storage and metadata in DB.

## 🧠 3. AI Analysis


| Method | Endpoint                            | Description                                      |
| ------ | ----------------------------------- | ------------------------------------------------ |
| POST   | `/api/analyze/{documentId}`         | Run OCR + NLP + AI on the uploaded document      |
| GET    | `/api/analyze/{documentId}/result`  | Get analysis result                              |
| GET    | `/api/analyze/{documentId}/summary` | Get AI-generated summary or diagnosis (optional) |

> These endpoints will connect to the Python-based AI service, maybe via HTTP or gRPC.

## 📥 4. Exporting / Downloading Results


| Method | Endpoint                       | Description                               |
| ------ | ------------------------------ | ----------------------------------------- |
| GET    | `/api/export/{documentId}`     | Download full analysis report (PDF, JSON) |
| GET    | `/api/export/{documentId}/raw` | Get raw OCR/NLP JSON data                 |

