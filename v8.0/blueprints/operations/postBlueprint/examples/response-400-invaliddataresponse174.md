INVALID_DATA error for a non-text validation filter validation_message

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "validation_message",
        "expected_data_type": "text",
        "json_path": "$.blueprints[*].transitions[*].during_inputs[*].validation_filter.validation_message"
      },
      "status": "error"
    }
  ]
}
```
