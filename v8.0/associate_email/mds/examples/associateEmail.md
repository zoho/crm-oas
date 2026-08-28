# Examples: associateEmail

**POST /{module}/{recordId}/actions/associate_email**

## Request examples

### `application/json` — Standard

```json
{
  "data": [
    {
      "from": {
        "user_name": "John Doe",
        "email": "john.doe@example.com"
      },
      "to": [
        {
          "user_name": "Client",
          "email": "client@business.com"
        }
      ],
      "subject": "Project Update",
      "content": "Update content",
      "original_message_id": "msg_123",
      "sent": true,
      "date_time": "2025-10-10T14:00:00Z"
    }
  ]
}
```

## Response examples

### Status `201` — `application/json` — Success

```json
{
  "Emails": [
    {
      "code": "SUCCESS",
      "details": {
        "message_id": "msg_123"
      },
      "message": "Email associated successfully.",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — MaximumLength

```json
{
  "code": "INVALID_DATA",
  "message": "invalid data",
  "status": "error",
  "details": {
    "maximum_length": 1,
    "api_name": "Emails",
    "json_path": "$.Emails"
  }
}
```

### Status `400` — `application/json` — InvalidData

```json
{
  "code": "INVALID_DATA",
  "message": "the related id given seems to be invalid",
  "status": "error",
  "details": {}
}
```

### Status `400` — `application/json` — MandatoryNotFound

```json
{
  "Emails": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "from",
        "json_path": "$.Emails[0].from"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidValue

```json
{
  "code": "INVALID_DATA",
  "message": "invalid data",
  "status": "error",
  "details": {
    "api_name": "from",
    "json_path": "$.Emails[0].from"
  }
}
```

### Status `404` — `application/json` — InvalidModule

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
