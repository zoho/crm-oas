Example of API name being not mentioned in master_record_fields array.

```json
{
  "merge": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "api_name",
        "json_path": "$.merge[0].master_record_fields[0].api_name"
      },
      "message": "API name not mentioned for the master record",
      "status": "error"
    }
  ]
}
```
