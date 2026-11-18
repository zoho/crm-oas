Error response with code INVALID_DATA: You can provide up to 30 characters (Field: title)

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "details": {
        "maximum_length": 30,
        "json_path": "$.transitions[0].during_inputs[0].title",
        "api_name": "title"
      },
      "message": "You can provide upto 30 characters.",
      "status": "error"
    }
  ]
}
```
