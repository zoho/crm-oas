No ID or api_name supplied for related_field in association_details

```json
{
  "layouts": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "id",
            "json_path": "$.layouts[0].sections[0].fields[0].association_details.related_field.id"
          },
          {
            "api_name": "api_name",
            "json_path": "$.layouts[0].sections[0].fields[0].association_details.related_field.api_name"
          }
        ]
      },
      "message": "One of the required fields is missing",
      "status": "error"
    }
  ]
}
```
