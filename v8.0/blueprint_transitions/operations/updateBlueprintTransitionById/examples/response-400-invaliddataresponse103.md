INVALID_DATA error for invalid data in the title field

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "title",
        "maximum_length": 10,
        "json_path": "$.transitions[*].during_inputs[*].title"
      },
      "status": "error"
    }
  ]
}
```
