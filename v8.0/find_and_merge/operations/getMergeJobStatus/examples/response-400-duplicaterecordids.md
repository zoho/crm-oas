Example of duplicate record IDs in merge request. 

```json
{
  "merge": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.merge[0].data[0].id"
      },
      "message": "Valid record ids need to be given for merging",
      "status": "error"
    }
  ]
}
```
