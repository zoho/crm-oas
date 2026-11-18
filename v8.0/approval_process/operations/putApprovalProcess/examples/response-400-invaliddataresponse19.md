INVALID_DATA error: approval process name exceeds maximum length

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 200,
        "json_path": "$.approval_process[*].name"
      },
      "status": "error"
    }
  ]
}
```
