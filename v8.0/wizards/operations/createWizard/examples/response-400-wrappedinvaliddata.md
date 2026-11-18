Wrapped invalid data error — e.g., boolean field received a string

```json
{
  "wizards": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "active",
        "json_path": "$.wizards[0].active",
        "expected_data_type": "boolean"
      },
      "message": "Data type mismatch",
      "status": "error"
    }
  ]
}
```
