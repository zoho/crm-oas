INVALID_DATA error for an oversized validation filter validation_message

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "validation_message",
        "maximum_length": 100,
        "json_path": "$.blueprints[*].transitions[*].during_inputs[*].validation_filter.validation_message"
      },
      "status": "error"
    }
  ]
}
```
