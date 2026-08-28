# Examples: uploadAttachment

**POST /{moduleApiName}/{recordId}/Attachments**

## Request examples

### `multipart/form-data` — BasicUpload

Upload with title

```json
{
  "attachmentUrl": "https://example.com/document.pdf",
  "title": "Q4 Financial Report"
}
```

### `multipart/form-data` — MinimalUpload

Upload without title

```json
{
  "attachmentUrl": "https://example.com/document.pdf"
}
```

### `multipart/form-data` — MaxLengthUrl

Maximum length URL

```json
{
  "attachmentUrl": "https://example.com/very/long/path/that/could/reach/maximum/allowed/length/of/2000/characters/...",
  "title": "Document with long URL"
}
```

## Response examples

### Status `200` — `application/json` — SuccessfulUpload

Successful attachment upload

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "Modified_Time": "2025-12-22T13:14:47+05:30",
        "Modified_By": {
          "name": "John Doe",
          "id": "2876819000000511001"
        },
        "Created_Time": "2025-12-22T13:14:47+05:30",
        "id": "2876819000002738705",
        "Created_By": {
          "name": "John Doe",
          "id": "2876819000000511001"
        }
      },
      "message": "attachment uploaded successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidUrl

Invalid URL format

```json
{
  "status": "error",
  "code": "INVALID_URL_PATTERN",
  "message": "the given attachment URL is incorrect",
  "details": {}
}
```

### Status `400` — `application/json` — MandatoryNotFound

Required field missing

```json
{
  "status": "error",
  "code": "MANDATORY_NOT_FOUND",
  "message": "required field not found",
  "details": {}
}
```

### Status `400` — `application/json` — InvalidData

Invalid data format

```json
{
  "status": "error",
  "code": "INVALID_DATA",
  "message": "invalid data provided",
  "details": {}
}
```

### Status `400` — `application/json` — RequiredParamMissing

Required parameter missing

```json
{
  "code": "REQUIRED_PARAM_MISSING",
  "details": {
    "param_name": "fields"
  },
  "message": "One of the expected parameter is missing",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidRecordId

Invalid record ID

```json
{
  "status": "error",
  "code": "INVALID_DATA",
  "message": "the related id given seems to be invalid",
  "details": {
    "resource_path_index": 1
  }
}
```

### Status `400` — `application/json` — InvalidModule

Invalid module name

```json
{
  "code": "INVALID_MODULE",
  "details": {
    "resource_path_index": 0
  },
  "message": "the module name given seems to be invalid",
  "status": "error"
}
```

### Status `401` — `application/json` — InvalidToken

Invalid or expired access token

```json
{
  "status": "error",
  "code": "INVALID_TOKEN",
  "message": "invalid oauth token",
  "details": {}
}
```

### Status `403` — `application/json` — InsufficientScope

Insufficient OAuth scope

```json
{
  "status": "error",
  "code": "OAUTH_SCOPE_MISMATCH",
  "message": "required oauth scope is missing",
  "details": {}
}
```

### Status `404` — `application/json` — RecordNotFound

Record not found

```json
{
  "status": "error",
  "code": "INVALID_MODULE",
  "message": "the module name given seems to be invalid",
  "details": {}
}
```

### Status `404` — `application/json` — AttachmentNotFound

Attachment not found

```json
{
  "status": "error",
  "code": "INVALID_DATA",
  "message": "the id given seems to be invalid",
  "details": {}
}
```

### Status `413` — `application/json` — FileSizeExceeded

File size exceeds allowed limit

```json
{
  "status": "error",
  "code": "FILE_SIZE_MORE_THAN_ALLOWED_SIZE",
  "message": "Please check if the size of the file is in the correct range",
  "details": {}
}
```

### Status `429` — `application/json` — RateLimitExceeded

API rate limit exceeded

```json
{
  "status": "error",
  "code": "RATE_LIMIT_EXCEEDED",
  "message": "API rate limit exceeded. Please retry after some time",
  "details": {}
}
```

### Status `500` — `application/json` — ServerError

Internal server error

```json
{
  "status": "error",
  "code": "INTERNAL_ERROR",
  "message": "Internal Server Error",
  "details": {}
}
```

### Status `503` — `application/json` — Maintenance

Service under maintenance

```json
{
  "status": "error",
  "code": "SERVICE_UNAVAILABLE",
  "message": "Service temporarily unavailable. Please try again later",
  "details": {}
}
```
