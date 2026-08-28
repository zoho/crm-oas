# Examples: uploadOrganizationPhoto

**POST /org/photo**

## Response examples

### Status `200` — `application/json` — SuccessResponse

Success response for status code 200

```json
{
  "status": "success",
  "code": "SUCCESS",
  "message": "Organization photo uploaded successfully",
  "details": {}
}
```

### Status `400` — `application/json` — BadRequestError

INVALID_DATA error: request data is invalid

```json
{
  "status": "error",
  "code": "INVALID_DATA",
  "message": "Invalid data provided",
  "details": {}
}
```

### Status `403` — `application/json` — NoPermissionError

NO_PERMISSION error: insufficient permissions to upload organization photo

```json
{
  "status": "error",
  "code": "NO_PERMISSION",
  "message": "Permission denied to upload organization photo",
  "details": {
    "permissions": [
      "org.photo.upload"
    ]
  }
}
```

### Status `413` — `application/json` — FileSizeExceedsError

FILE_SIZE_EXCEEDS error: uploaded file exceeds the maximum allowed size

```json
{
  "status": "error",
  "code": "FILE_SIZE_EXCEEDS",
  "message": "File size exceeds the maximum allowed limit",
  "details": {
    "size": 5242880
  }
}
```

### Status `415` — `application/json` — FileResolutionExceedsError

FILE_RESOLUTION_EXCEEDS error: image resolution exceeds the allowed limit

```json
{
  "status": "error",
  "code": "FILE_RESOLUTION_EXCEEDS",
  "message": "File resolution exceeds the maximum allowed limit",
  "details": {
    "resolution": 10000000
  }
}
```

### Status `415` — `application/json` — InvalidDataError

INVALID_DATA error: uploaded file is not a supported image format

```json
{
  "status": "error",
  "code": "INVALID_DATA",
  "message": "Invalid file format. Only image files are allowed",
  "details": {}
}
```
