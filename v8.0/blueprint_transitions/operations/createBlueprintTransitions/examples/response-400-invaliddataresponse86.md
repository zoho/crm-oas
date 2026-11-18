Error response with code **INVALID_DATA**: invalid data type in field **id**

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.transitions[*].during_inputs[*].related_list.id"
      },
      "status": "error"
    }
  ]
}
```
