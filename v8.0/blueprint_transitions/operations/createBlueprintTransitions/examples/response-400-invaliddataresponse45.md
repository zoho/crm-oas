Error response with code **INVALID_DATA**: **message** exceeds the maximum length of 1000

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
