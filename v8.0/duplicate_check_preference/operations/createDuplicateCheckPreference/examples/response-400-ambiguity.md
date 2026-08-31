Ambiguity during field mapping

```json
{
  "code": "AMBIGUITY_DURING_PROCESSING",
  "details": {
    "ambiguity_due_to": [
      {
        "api_name": "id",
        "json_path": "$.duplicate_check_preference[0].type_configurations.field_mappings[0].mapped_field.id"
      },
      {
        "api_name": "api_name",
        "json_path": "$.duplicate_check_preference[0].type_configurations.field_mappings[0].mapped_field.api_name"
      }
    ]
  },
  "message": "two different crm fields are found",
  "status": "error"
}
```
