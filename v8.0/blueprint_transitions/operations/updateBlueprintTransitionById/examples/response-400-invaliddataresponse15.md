INVALID_DATA error for invalid data in the description field

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "description",
        "maximum_length": 1000,
        "json_path": "$.transitions[*].description"
      },
      "status": "error"
    }
  ]
}
```
