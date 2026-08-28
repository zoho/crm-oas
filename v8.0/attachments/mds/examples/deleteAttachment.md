# Examples: deleteAttachment

**DELETE /{moduleApiName}/{recordId}/Attachments/{id}**

## Response examples

### Status `200` — `application/json` — SuccessfulDeletion

Successful attachment deletion

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "2876819000001935002"
      },
      "message": "record deleted",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidData

Invalid record ID

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 3
  },
  "message": "record not deleted",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidAttachmentId

Invalid attachment ID

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 3
  },
  "message": "record not deleted",
  "status": "error"
}
```

### Status `400` — `application/json` — AlreadyDeleted

Attachment already deleted

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 3
  },
  "message": "record not deleted",
  "status": "error"
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
