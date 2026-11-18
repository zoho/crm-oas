INVALID_DATA error for a module ID with an invalid format

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "regex": "[0-9]+",
        "json_path": "$.blueprints[*].states[*].module.id"
      },
      "status": "error"
    }
  ]
}
```
