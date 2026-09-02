Error response with code INVALID_DATA: Invalid data type (Field: api_name)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.field_updates[*].dependent_fields[*].field.api_name"
      },
      "status": "error"
    }
  ]
}
```
