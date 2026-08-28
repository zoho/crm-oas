# Examples: deleteRecordPhoto

**DELETE /{module}/{record}/photo**

## Response examples

### Status `200` — `application/json` — SuccessResponse

Delete record photo success

```json
{
  "code": "SUCCESS",
  "message": "Photo deleted successfully",
  "status": "success",
  "details": {}
}
```

### Status `400` — `application/json` — InvalidUrlPattern

Delete record photo with invalid URL pattern

```json
{
  "code": "INVALID_URL_PATTERN",
  "message": "Please check if the URL trying to access is a correct one",
  "status": "error",
  "details": {}
}
```
