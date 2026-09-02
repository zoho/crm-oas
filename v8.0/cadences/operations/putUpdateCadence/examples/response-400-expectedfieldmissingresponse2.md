Second expected field missing error

```json
{
  "cadences": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "api_name",
            "json_path": "$.cadences[0].follow_ups[1].action.details.field_mappings[0].field.api_name"
          },
          {
            "api_name": "id",
            "json_path": "$.cadences[0].follow_ups[1].action.details.field_mappings[0].field.id"
          }
        ]
      },
      "message": "Specify atleast one field",
      "status": "error"
    }
  ]
}
```
