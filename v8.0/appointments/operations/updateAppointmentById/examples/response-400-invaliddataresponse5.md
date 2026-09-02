**INVALID_DATA** error when **unit** field in **Remind_At** receives a non-integer value.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "integer",
        "api_name": "unit",
        "json_path": "$.data[0].Remind_At[0].unit"
      },
      "message": "INVALID_DATA",
      "status": "error"
    }
  ]
}
```
