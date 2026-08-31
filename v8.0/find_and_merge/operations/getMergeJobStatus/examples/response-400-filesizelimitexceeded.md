Example of total file size across merge participants exceeds limit. 

```json
{
  "merge": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "MAXIMUM_SIZE": "30 MB",
        "limit_due_to": [
          {
            "api_name": "File_Upload_30MB",
            "json_path": "$.merge[0].data[0]._fields[0].api_name"
          },
          {
            "api_name": "File_Upload_30MB",
            "json_path": "$.merge[0].data[1]._fields[1].api_name"
          },
          {
            "api_name": "File_Upload_30MB",
            "json_path": "$.merge[0].master_record_fields[1].api_name"
          }
        ]
      },
      "message": "Attachment size limit exceeded",
      "status": "error"
    }
  ]
}
```
