INVALID_DATA error: invalid data type for the **message** field

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "message",
        "expected_data_type": "text",
        "json_path": "$.transitions[*].during_inputs[*].message"
      },
      "status": "error"
    }
  ]
}
```
