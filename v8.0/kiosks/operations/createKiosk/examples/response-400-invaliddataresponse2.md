INVALID_DATA error when status is set to a value outside the allowed set

```json
{
  "kiosks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "text",
        "regex": "draft",
        "api_name": "status",
        "json_path": "$.kiosks[0].status"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```
