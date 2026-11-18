INVALID_DATA error: Invalid data (Field: ID)

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "regex": "[0-9]+",
        "json_path": "$.blueprints[*].criteria.field.id"
      },
      "status": "error"
    }
  ]
}
```
