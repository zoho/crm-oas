An example of partial success response with one valid and one invalid entry.

```json
{
  "share": [
    {
      "code": "SUCCESS",
      "details": {},
      "message": "record will be shared successfully",
      "status": "success"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "shared_with",
        "json_path": "$.share[1].shared_with"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```
