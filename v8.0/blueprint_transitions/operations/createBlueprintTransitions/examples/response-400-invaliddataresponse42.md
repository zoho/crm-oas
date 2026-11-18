Error response with **INVALID_DATA**: invalid data type in **id**

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.transitions[*].during_inputs[*].field.id"
      },
      "status": "error"
    }
  ]
}
```
