Example of one particular field is mentioned more than once.

```json
{
  "merge": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "api_name",
        "json_path": "$.merge[0].data[0]._fields[0].api_name"
      },
      "message": "When one field is mentioned more than once",
      "status": "error"
    }
  ]
}
```
