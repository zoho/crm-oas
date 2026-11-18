INVALID_DATA error for an invalid value in the description field

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "description",
        "maximum_length": 1000,
        "json_path": "$.blueprints[*].transitions[*].description"
      },
      "status": "error"
    }
  ]
}
```
