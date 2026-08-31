Moving >50 values to used when >15 fields

```json
{
  "global_picklists": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "limit_due_to": [
          {
            "api_name": "type",
            "json_path": "$.global_picklists[0].pick_list_values[50].type"
          }
        ],
        "limit": 50
      },
      "message": "Moving more than 50 values to the used section in a single save is not allowed when they are associated with more than 15 fields.",
      "status": "error"
    }
  ]
}
```
