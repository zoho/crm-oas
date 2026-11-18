INVALID_DATA error when rules is not a JSON array

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "rules",
        "expected_data_type": "jsonarray",
        "json_path": "$.approval_process[*].rules"
      },
      "status": "error"
    }
  ]
}
```
