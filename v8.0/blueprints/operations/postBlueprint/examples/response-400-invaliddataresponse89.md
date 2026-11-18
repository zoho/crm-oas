INVALID_DATA error for a module ID in an invalid format

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "regex": "[0-9]+",
        "json_path": "$.blueprints[*].module.id"
      },
      "status": "error"
    }
  ]
}
```
