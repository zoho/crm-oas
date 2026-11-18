INVALID_DATA error: invalid data in the ID field (connections)

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "regex": "[0-9]+",
        "json_path": "$.blueprints[*].owners[*].resources[*].id"
      },
      "status": "error"
    }
  ]
}
```
