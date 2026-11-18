INVALID_DATA error for a transition name exceeding the maximum length

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 50,
        "json_path": "$.blueprints[*].transitions[*].name"
      },
      "status": "error"
    }
  ]
}
```
