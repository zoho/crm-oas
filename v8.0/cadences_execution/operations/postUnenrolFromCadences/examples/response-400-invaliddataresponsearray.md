Error response - multiple invalid record IDs

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "ids",
        "json_path": "$.ids[0]"
      },
      "message": "given id seems to be invalid",
      "status": "error"
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
