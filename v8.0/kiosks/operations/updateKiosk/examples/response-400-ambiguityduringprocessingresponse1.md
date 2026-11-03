AMBIGUITY_DURING_PROCESSING error — mismatched module ID and API name

```json
{
  "kiosks": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "id",
            "json_path": "$.kiosks[0].current_record_module.id"
          },
          {
            "api_name": "api_name",
            "json_path": "$.kiosks[0].current_record_module.api_name"
          }
        ]
      },
      "message": "Ambiguity while processing the request",
      "status": "error"
    }
  ]
}
```
