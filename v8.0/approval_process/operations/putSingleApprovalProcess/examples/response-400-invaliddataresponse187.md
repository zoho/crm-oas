Error response with code INVALID_DATA: Invalid data type (Field: record_modification)

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "record_modification",
        "expected_data_type": "jsonobject",
        "json_path": "$.approval_process[*].rules[*].process_admin_configuration.record_modification"
      },
      "status": "error"
    }
  ]
}
```
