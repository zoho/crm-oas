INVALID_DATA error for a pipeline ID in an invalid numeric format

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "regex": "[0-9]+",
        "json_path": "$.blueprints[*].pipeline.id"
      },
      "status": "error"
    }
  ]
}
```
