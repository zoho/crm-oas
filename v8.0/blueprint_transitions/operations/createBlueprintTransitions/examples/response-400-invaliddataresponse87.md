Error response with code **INVALID_DATA**: invalid data in the **id** field

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 25,
        "json_path": "$.transitions[*].during_inputs[*].related_list.id"
      },
      "status": "error"
    }
  ]
}
```
