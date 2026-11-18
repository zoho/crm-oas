INVALID_DATA error for a transition_type value exceeding the maximum length

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "transition_type",
        "maximum_length": 25,
        "json_path": "$.blueprints[*].transitions[*].transition_type"
      },
      "status": "error"
    }
  ]
}
```
