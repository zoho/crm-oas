INVALID_DATA error for an invalid data type on the api_name property

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.approval_process[*].module.api_name"
      },
      "status": "error"
    }
  ]
}
```
