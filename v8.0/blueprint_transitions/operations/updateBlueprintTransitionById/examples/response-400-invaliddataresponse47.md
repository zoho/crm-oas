**INVALID_DATA** error when the **validation_filter** field contains invalid data

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "validation_filter",
        "maximum_length": 1,
        "json_path": "$.transitions[*].during_inputs[*].validation_filter"
      },
      "status": "error"
    }
  ]
}
```
