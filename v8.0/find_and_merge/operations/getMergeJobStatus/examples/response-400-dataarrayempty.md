Example of data array empty or missing from request. 

```json
{
  "merge": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "data",
        "json_path": "$.merge[0].data",
        "minimum_length": 1
      },
      "message": " Atleast one child record id is required to be merged.",
      "status": "error"
    }
  ]
}
```
