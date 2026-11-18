Error response with code **INVALID_DATA**: invalid data type for the **name** field

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.transitions[*].during_inputs[*].related_list.name"
      },
      "status": "error"
    }
  ]
}
```
