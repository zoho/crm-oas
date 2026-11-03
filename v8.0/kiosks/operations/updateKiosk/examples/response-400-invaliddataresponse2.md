INVALID_DATA error — invalid data in the status field

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
