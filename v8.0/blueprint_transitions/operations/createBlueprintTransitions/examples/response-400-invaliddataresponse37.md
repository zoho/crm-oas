**INVALID_DATA** error: invalid data in the **sequence** field

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "sequence",
        "maximum_length": 1,
        "json_path": "$.transitions[*].during_inputs[*].sequence"
      },
      "status": "error"
    }
  ]
}
```
