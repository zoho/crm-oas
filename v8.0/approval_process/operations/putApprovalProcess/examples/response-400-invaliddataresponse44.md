INVALID_DATA error for invalid data type in the criteria field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "criteria",
        "expected_data_type": "jsonobject",
        "json_path": "$.approval_process[*].rules[*].criteria"
      },
      "status": "error"
    }
  ]
}
```
