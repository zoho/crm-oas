INVALID_DATA error when description is not of type text

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "description",
        "expected_data_type": "text",
        "json_path": "$.approval_process[*].description"
      },
      "status": "error"
    }
  ]
}
```
