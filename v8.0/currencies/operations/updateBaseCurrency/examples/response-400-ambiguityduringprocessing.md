Both id and rid refer to different currencies

```json
{
  "base_currency": {
    "code": "AMBIGUITY_DURING_PROCESSING",
    "message": "Ambiguity while processing the request",
    "status": "error",
    "details": {
      "ambiguity_due_to": [
        {
          "api_name": "id",
          "json_path": "$.base_currency.id"
        },
        {
          "api_name": "rid",
          "json_path": "$.base_currency.rid"
        }
      ]
    }
  }
}
```
