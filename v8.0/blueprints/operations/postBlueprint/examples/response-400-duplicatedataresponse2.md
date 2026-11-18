DUPLICATE_DATA error for a duplicate picklist value in a Blueprint state

```json
{
  "blueprints": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.blueprints[0].state[2].pick_list_value.id"
      },
      "message": "There is already a state with the same pick list value used in the blueprint",
      "status": "error"
    }
  ]
}
```
