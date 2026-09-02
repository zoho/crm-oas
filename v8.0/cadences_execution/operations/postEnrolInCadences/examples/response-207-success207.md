Multi-status response with partial enrollment success

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "534412000002201155",
        "cadences": [
          {
            "name": "Cadence 1",
            "id": "1234567890456789"
          },
          {
            "name": "Cadence 2",
            "id": "1234567890456789"
          }
        ]
      },
      "message": "records manually enrolled",
      "status": "success"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "ids",
        "json_path": "$.ids[1]"
      },
      "message": "given id seems to be invalid",
      "status": "error"
    }
  ]
}
```
