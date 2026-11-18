INVALID_DATA error for an invalid ID field

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "regex": "[0-9]+",
        "json_path": "$.blueprints[*].transitions[*].module.id"
      },
      "status": "error"
    }
  ]
}
```
