INVALID_DATA error for invalid data in the ID field

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
