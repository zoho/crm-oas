Invalid data type error for the criteria field api_name expected as text

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
