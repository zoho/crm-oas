Error response with code AMBIGUITY_DURING_PROCESSING: The field api name seems to be invalid

```json
{
  "field_updates": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "id",
            "json_path": "$.field_updates[0].field.id"
          },
          {
            "api_name": "api_name",
            "json_path": "$.field_updates[0].field.api_name"
          }
        ]
      },
      "message": "The field api name seems to be invalid",
      "status": "error"
    }
  ]
}
```
