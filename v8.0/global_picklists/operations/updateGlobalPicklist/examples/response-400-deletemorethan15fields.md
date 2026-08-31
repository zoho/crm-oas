Cannot delete when associated with >15 fields

```json
{
  "global_picklists": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "type",
        "json_path": "$.global_picklists[0].pick_list_values[0]._delete"
      },
      "message": "option can't be deleted as global set is associated to more than 15 fields",
      "status": "error"
    }
  ]
}
```
