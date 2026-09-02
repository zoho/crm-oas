Example of API name missing from configuration. 

```json
{
  "merge": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "api_name",
        "json_path": "$.merge[0].data[0]._fields[0].api_name"
      },
      "message": "API name of the field is not mentioned",
      "status": "error"
    }
  ]
}
```
