# Examples: getAttachmentById

**GET /{moduleApiName}/{recordId}/Attachments/{id}**

## Response examples

### Status `400` — `application/json` — LinkAttachmentError

Link attachment cannot be downloaded

```json
{
  "code": "DOWNLOAD_NOT_ALLOWED",
  "details": {},
  "message": "As it is a linked attachment, you can not download it",
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
  "status": "error",
  "code": "INVALID_MODULE",
  "message": "the module name given seems to be invalid",
  "details": {
    "resource_path_index": 0
  }
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
