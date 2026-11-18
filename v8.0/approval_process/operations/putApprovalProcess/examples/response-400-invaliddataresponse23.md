INVALID_DATA: approval process description exceeds its maximum length

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "description",
        "maximum_length": 3000,
        "json_path": "$.approval_process[*].description"
      },
      "status": "error"
    }
  ]
}
```
