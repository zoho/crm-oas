INVALID_DATA error for an invalid pipeline name value

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 100,
        "json_path": "$.blueprints[*].pipeline.name"
      },
      "status": "error"
    }
  ]
}
```
