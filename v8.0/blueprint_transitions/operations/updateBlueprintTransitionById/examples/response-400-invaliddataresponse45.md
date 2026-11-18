**INVALID_DATA** error when the **message** field contains invalid data

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "message",
        "maximum_length": 1000,
        "json_path": "$.transitions[*].during_inputs[*].message"
      },
      "status": "error"
    }
  ]
}
```
