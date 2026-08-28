# Examples: getAttachments

**GET /{moduleApiName}/{recordId}/Attachments**

## Response examples

### Status `200` — `application/json` — MultipleAttachments

Multiple attachments including file and link types

```json
{
  "data": [
    {
      "Owner": {
        "name": "John CRM",
        "id": "2876819000000511001",
        "email": "test@zohocorp.com"
      },
      "Modified_Time": "2025-12-11T11:34:53+05:30",
      "File_Name": "Q4_Report.pdf",
      "$field_states": null,
      "Created_Time": "2025-12-11T11:34:53+05:30",
      "Size": "1048576",
      "Parent_Id": {
        "name": "John Doe",
        "id": "2876819000001234567"
      },
      "$editable": true,
      "$file_id": "file123",
      "$type": "File",
      "$se_module": "Leads",
      "Modified_By": {
        "name": "John CRM",
        "id": "2876819000000511001",
        "email": "test@zohocorp.com"
      },
      "$state": "save",
      "id": "2876819000001935002",
      "Created_By": {
        "name": "John CRM",
        "id": "2876819000000511001",
        "email": "test@zohocorp.com"
      }
    },
    {
      "Owner": {
        "name": "Admin User",
        "id": "2876819000000511002",
        "email": "admin@zohocorp.com"
      },
      "Modified_Time": "2025-12-10T09:20:15+05:30",
      "File_Name": "Google",
      "$field_states": null,
      "Created_Time": "2025-12-10T09:20:15+05:30",
      "Size": "0",
      "Parent_Id": {
        "name": "Jane Smith",
        "id": "2876819000001234568"
      },
      "$editable": true,
      "$file_id": null,
      "$type": "Link URL",
      "$se_module": "Contacts",
      "Modified_By": {
        "name": "Admin User",
        "id": "2876819000000511002",
        "email": "admin@zohocorp.com"
      },
      "$state": "save",
      "id": "2876819000001935003",
      "Created_By": {
        "name": "Admin User",
        "id": "2876819000000511002",
        "email": "admin@zohocorp.com"
      },
      "$link_url": "https://www.google.com"
    }
  ],
  "info": {
    "per_page": 200,
    "next_page_token": null,
    "count": 2,
    "page": 1,
    "previous_page_token": null,
    "page_token_expiry": null,
    "more_records": false
  }
}
```

### Status `200` — `application/json` — EmptyList

No attachments found

```json
{
  "data": [],
  "info": {
    "per_page": 200,
    "next_page_token": null,
    "count": 0,
    "page": 1,
    "previous_page_token": null,
    "page_token_expiry": null,
    "more_records": false
  }
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
