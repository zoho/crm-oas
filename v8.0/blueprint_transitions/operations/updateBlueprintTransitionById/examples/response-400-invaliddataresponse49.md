**INVALID_DATA** error when the **validation_message** field contains invalid data

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "validation_message",
        "maximum_length": 39,
        "json_path": "$.transitions[*].during_inputs[*].validation_filter.validation_message"
      },
      "status": "error"
    }
  ]
}
```
