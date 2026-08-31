Invalid data error when Duration is outside the permitted 5-min to 24-hr range.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "Duration",
        "json_path": "$.data[0].Duration"
      },
      "message": "Duration value should not be greater than 24hrs or less than 5mins",
      "status": "error"
    }
  ]
}
```
