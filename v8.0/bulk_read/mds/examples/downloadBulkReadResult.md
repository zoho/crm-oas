# Examples: downloadBulkReadResult

**GET /read/{jobId}/result**

## Response examples

### Status `404` — `application/json` — Example1

Job result not found error

```json
{
  "code": "RESOURCE_NOT_FOUND",
  "details": {
    "resource": "string"
  },
  "message": "string",
  "status": "error"
}
```
