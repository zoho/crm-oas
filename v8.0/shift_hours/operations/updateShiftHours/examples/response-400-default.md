An example of error response.

```json
{
  "shift_hours": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.shift_hours[0].name"
      },
      "message": "Shift Name should not contain special characters:#, %, ^",
      "status": "error"
    }
  ]
}
```
