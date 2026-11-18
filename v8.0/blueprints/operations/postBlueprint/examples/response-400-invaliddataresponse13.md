INVALID_DATA error for an invalid ID field

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 25,
        "json_path": "$.blueprints[*].owners[*].resources[*].id"
      },
      "status": "error"
    }
  ]
}
```
