INVALID_DATA error when a rule criteria is not a jsonobject

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
