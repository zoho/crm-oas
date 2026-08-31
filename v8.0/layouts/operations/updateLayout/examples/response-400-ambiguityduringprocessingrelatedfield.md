Ambiguity detected when both ID and api_name identify different related_fields

```json
{
  "layouts": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
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
      "message": "ambiguity while processing the related_field",
      "status": "error"
    }
  ]
}
```
