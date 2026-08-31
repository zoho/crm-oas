Expected field missing error

```json
{
  "status": "error",
  "code": "EXPECTED_FIELD_MISSING",
  "message": "Specify at least one field.",
  "details": {
    "expected_fields": [
      {
        "api_name": "id",
        "json_path": "$.duplicate_check_preference[0].type_configurations.field_mappings[0].mapped_field.id"
      },
      {
        "api_name": "api_name",
        "json_path": "$.duplicate_check_preference[0].type_configurations.field_mappings[0].mapped_field.api_name"
      }
    ]
  }
}
```
