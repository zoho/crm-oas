# Examples: deleteOrgPhoto

**DELETE /org/photo**

## Response examples

### Status `200` — `application/json` — SuccessResponse

Success response for status 200

```json
{
  "status": "success",
  "code": "SUCCESS",
  "message": "Organization photo deleted successfully",
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

NO_PERMISSION error: insufficient permissions to delete organization photo

```json
{
  "status": "error",
  "code": "NO_PERMISSION",
  "message": "Permission denied to delete organization photo",
  "details": {
    "permissions": [
      "org.photo.delete"
    ]
  }
}
```
