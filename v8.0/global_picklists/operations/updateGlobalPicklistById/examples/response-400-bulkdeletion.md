Bulk deletion not allowed

```json
{
  "global_picklists": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "limit_due_to": {
          "api_name": "_delete",
          "json_path": "$.global_picklists[0].pick_list_values[1]._delete"
        },
        "limit": 1
      },
      "message": "More than one picklist value cannot be deleted",
      "status": "error"
    }
  ]
}
```
