INVALID_DATA error for a pipeline value exceeding the maximum length

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "pipeline",
        "maximum_length": 1,
        "json_path": "$.blueprints[*].pipeline"
      },
      "status": "error"
    }
  ]
}
```
