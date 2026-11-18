INVALID_DATA error when the rule name has an invalid data type

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.approval_process[*].rules[*].name"
      },
      "status": "error"
    }
  ]
}
```
