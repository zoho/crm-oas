Error response with code INVALID_DATA: Invalid data type (Field: name)

```json
{
  "workflow_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.workflow_rules[*].name"
      },
      "status": "error"
    }
  ]
}
```
