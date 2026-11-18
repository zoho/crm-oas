INVALID_DATA error for an invalid data type on the field property

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
