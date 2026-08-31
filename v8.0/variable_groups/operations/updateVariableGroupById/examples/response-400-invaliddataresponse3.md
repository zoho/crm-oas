Error response for invalid variable group ID

```json
{
  "variable_groups": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.variable_groups[*].name"
      },
      "status": "error"
    }
  ]
}
```
