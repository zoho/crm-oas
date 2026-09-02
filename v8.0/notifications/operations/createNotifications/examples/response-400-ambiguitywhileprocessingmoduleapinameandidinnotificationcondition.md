Ambiguity between api_name and module ID in the notification condition

```json
{
  "code": "AMBIGUITY_DURING_PROCESSING",
  "message": "AMBIGUITY_DURING_PROCESSING",
  "details": {
    "ambiguity_due_to": [
      {
        "api_name": "api_name",
        "json_path": "$.watch[0].notification_condition[0].module.api_name"
      },
      {
        "api_name": "id",
        "json_path": "$.watch[0].notification_condition[0].module.id"
      }
    ]
  },
  "status": "error"
}
```
