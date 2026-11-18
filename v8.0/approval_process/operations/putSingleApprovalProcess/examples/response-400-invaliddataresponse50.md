Wrong data type for the criteria field API name

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.approval_process[*].rules[*].criteria.field.api_name"
      },
      "status": "error"
    }
  ]
}
```
