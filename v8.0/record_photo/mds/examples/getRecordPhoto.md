# Examples: getRecordPhoto

**GET /{module}/{record}/photo**

## Response examples

### Status `400` — `application/json` — InvalidUrlPattern

Get record photo with invalid URL pattern

```json
{
  "code": "INVALID_URL_PATTERN",
  "message": "Please check if the URL trying to access is a correct one",
  "status": "error",
  "details": {}
}
```
