Error response with code **INVALID_DATA**: invalid data type in **kiosk**

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "kiosk",
        "expected_data_type": "jsonobject",
        "json_path": "$.transitions[*].during_inputs[*].kiosk"
      },
      "status": "error"
    }
  ]
}
```
