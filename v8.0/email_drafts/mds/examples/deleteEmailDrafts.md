# Examples: deleteEmailDrafts

**DELETE /{module}/{record}/__email_drafts/{draft}**

## Response examples

### Status `200` — `application/json` — Success

Successful deletion

```json
{
  "__email_drafts": [
    {
      "code": "SUCCESS",
      "message": "Draft deleted Successfully",
      "status": "success",
      "details": {
        "id": "4f8efdcbaf23fd33c939217d4e14222d6d1cb21e4a45914fb9ba0c31c3c47330"
      }
    }
  ]
}
```

### Status `400` — `application/json` — InvalidModule

Invalid module name

```json
{
  "code": "INVALID_MODULE",
  "message": "the module name given seems to be invalid",
  "status": "error",
  "details": {
    "resource_path_index": 0
  }
}
```

### Status `400` — `application/json` — InvalidRelatedID

Invalid record ID

```json
{
  "code": "INVALID_DATA",
  "message": "the related id given seems to be invalid",
  "status": "error",
  "details": {
    "resource_path_index": 1
  }
}
```

### Status `400` — `application/json` — InvalidDraftId

Invalid draft ID

```json
{
  "code": "INVALID_DATA",
  "message": "Invalid draft Id",
  "status": "error",
  "details": {
    "resource_path_index": 3
  }
}
```

### Status `400` — `application/json` — DraftNotDeleted

Draft could not be deleted

```json
{
  "code": "INVALID_DATA",
  "message": "draft not deleted",
  "status": "error",
  "details": {
    "id": "473895000000583029"
  }
}
```

### Status `403` — `application/json` — NoPermission

No permission to access resource

```json
{
  "code": "NO_PERMISSION",
  "message": "Please contact your admin",
  "status": "error",
  "details": {}
}
```
