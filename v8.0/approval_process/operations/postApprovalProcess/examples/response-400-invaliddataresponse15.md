INVALID_DATA error for an invalid data type on the name field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.approval_process[*].name"
      },
      "status": "error"
    }
  ]
}
```
