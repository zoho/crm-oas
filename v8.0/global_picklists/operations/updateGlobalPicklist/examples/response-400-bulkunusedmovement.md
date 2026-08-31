Bulk unused movement not allowed

```json
{
  "global_picklists": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "limit_due_to": [
          {
            "api_name": "type",
            "json_path": "$.global_picklists[0].pick_list_values[1].type"
          }
        ],
        "limit": 1
      },
      "message": "More than one picklist value cannot be moved to unused type",
      "status": "error"
    }
  ]
}
```
