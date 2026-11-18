**INVALID_DATA** error when the **validation_message** field has an invalid data type

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "validation_message",
        "expected_data_type": "text",
        "json_path": "$.transitions[*].during_inputs[*].validation_filter.validation_message"
      },
      "status": "error"
    }
  ]
}
```
