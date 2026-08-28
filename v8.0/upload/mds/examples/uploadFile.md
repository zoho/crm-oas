# Examples: uploadFile

**POST /upload**

## Request examples

### `multipart/form-data` — Sample

Sample file upload request

```json
{
  "file": {
    "filename": "example.zip",
    "contentType": "application/octet-stream",
    "data": "<binary>"
  }
}
```

## Response examples

### Status `200` — `application/json` — Success

Response of a successful file upload.

```json
{
  "status": "success",
  "code": "FILE_UPLOAD_SUCCESS",
  "message": "file uploaded.",
  "details": {
    "file_id": "abc123xyz",
    "created_time": "2024-06-01T12:34:56Z"
  }
}
```

### Status `400` — `application/json` — InvalidOrgHeader

Invalid **X-CRM-ORG** header

```json
{
  "status": "error",
  "code": "INVALID_DATA",
  "message": "Invalid data - x-crm-org",
  "details": {}
}
```

### Status `400` — `application/json` — FeatureNotSupported

Feature not supported response

```json
{
  "status": "error",
  "code": "NOT_SUPPORTED_FEATURE",
  "message": "Feature is not supported",
  "details": {}
}
```

### Status `400` — `application/json` — FeatureHeaderMissing

Missing feature header

```json
{
  "status": "error",
  "code": "MANDATORY_NOT_FOUND",
  "message": "Required key feature is not available",
  "details": {}
}
```

### Status `400` — `application/json` — OrgHeaderMissing

Missing **X-CRM-ORG** header

```json
{
  "status": "error",
  "code": "MANDATORY_NOT_FOUND",
  "message": "Required key x-crm-org is not available",
  "details": {}
}
```

### Status `400` — `application/json` — InvalidFileFormat

Unsupported file format

```json
{
  "status": "error",
  "code": "INVALID_FILE_FORMAT",
  "message": "invalid file format. only zip format is supported",
  "details": {}
}
```

### Status `400` — `application/json` — ImportFileTooLarge

Import file exceeds size limit

```json
{
  "status": "error",
  "code": "INVALID_DATA",
  "message": "Import file size should be less than 25 mb.",
  "details": {}
}
```
