Field-of-Lookup mapping limit reached for lookup

```json
{
  "layouts": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "limit": 5,
        "limit_due_to": [
          {
            "api_name": "id",
            "json_path": "$.layouts[0].sections[0].fields[0].association_details.lookup_field.id"
          }
        ]
      },
      "message": "Field of Lookup mapping limit is reached for the lookup",
      "status": "error"
    }
  ]
}
```
