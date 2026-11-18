Error response when the **layout** field contains invalid data

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "layout",
        "maximum_length": 1,
        "json_path": "$.transitions[*].during_inputs[*].related_list.layout"
      },
      "status": "error"
    }
  ]
}
```
