Example of stage being mentioned when child and master record have different pipelines.

```json
{
  "merge": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "api_name",
        "json_path": "$.merge[0].data[0]._fields[0].api_name"
      },
      "message": "Stage field will be automatically populated based on chosen Pipeline",
      "status": "error"
    }
  ]
}
```
