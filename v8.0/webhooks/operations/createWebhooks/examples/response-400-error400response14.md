Error response when format value exceeds the maximum allowed length

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "format",
      "maximum_length": 4,
      "json_path": "$.webhooks[*].body.format"
    },
    "status": "error"
  }
}
```
