INVALID_DATA error when the criteria field is not a jsonobject

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "field",
        "expected_data_type": "jsonobject",
        "json_path": "$.approval_process[*].rules[*].criteria.field"
      },
      "status": "error"
    }
  ]
}
```
