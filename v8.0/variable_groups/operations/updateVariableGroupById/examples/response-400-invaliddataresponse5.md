Error response for invalid request data

```json
{
  "variable_groups": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.variable_groups[*].api_name"
      },
      "status": "error"
    }
  ]
}
```
