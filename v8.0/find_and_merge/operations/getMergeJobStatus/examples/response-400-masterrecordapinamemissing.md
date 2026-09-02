Example of API name missing from master_record_fields entry. 

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
