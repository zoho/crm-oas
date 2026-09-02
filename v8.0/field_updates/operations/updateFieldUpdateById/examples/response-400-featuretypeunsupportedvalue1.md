Error response with code INVALID_DATA: Invalid data type (Field: field)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "field",
        "expected_data_type": "jsonobject",
        "json_path": "$.field_updates[*].dependent_fields[*].field"
      },
      "status": "error"
    }
  ]
}
```
