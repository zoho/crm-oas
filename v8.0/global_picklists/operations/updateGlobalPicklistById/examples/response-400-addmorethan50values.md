Adding >50 values when >15 fields

```json
{
  "global_picklists": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "limit_due_to": {
          "api_name": "type",
          "json_path": "$.global_picklists[0].pick_list_values[50]"
        },
        "limit": 50
      },
      "message": "Adding more than 50 values in a single save is not allowed when they are associated with more than 15 fields.",
      "status": "error"
    }
  ]
}
```
