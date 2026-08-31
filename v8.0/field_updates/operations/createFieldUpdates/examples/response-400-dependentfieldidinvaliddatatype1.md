Error response with code INVALID_DATA: Invalid data type (Field: id)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.field_updates[*].dependent_fields[*].field.id"
      },
      "status": "error"
    }
  ]
}
```
