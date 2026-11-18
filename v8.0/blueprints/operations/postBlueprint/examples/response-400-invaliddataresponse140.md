INVALID_DATA error for invalid data in the resources field

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "resources",
        "maximum_length": 1,
        "json_path": "$.blueprints[*].transitions[*].owners[*].resources"
      },
      "status": "error"
    }
  ]
}
```
