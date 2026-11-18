INVALID_DATA error when the **owners** field contains invalid data

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "owners",
        "maximum_length": 5,
        "json_path": "$.transitions[*].owners"
      },
      "status": "error"
    }
  ]
}
```
