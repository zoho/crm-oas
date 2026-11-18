Error response with code **INVALID_DATA**: invalid data type in **field**

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "field",
        "expected_data_type": "jsonobject",
        "json_path": "$.transitions[*].criteria.group[*].group[*].field"
      },
      "status": "error"
    }
  ]
}
```
