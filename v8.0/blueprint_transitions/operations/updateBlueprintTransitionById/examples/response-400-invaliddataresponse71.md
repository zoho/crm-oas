**INVALID_DATA** error response: invalid data in the **criteria** field

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "criteria",
        "maximum_length": 1,
        "json_path": "$.transitions[*].during_inputs[*].configured_fields[*].criteria"
      },
      "status": "error"
    }
  ]
}
```
