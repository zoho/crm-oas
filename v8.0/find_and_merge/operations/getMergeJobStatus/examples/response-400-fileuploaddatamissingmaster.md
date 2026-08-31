Example of _data array missing for master record file upload field. 

```json
{
  "merge": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "api_name": "id",
        "json_path": "$.merge[0].master_record_fields[0]._data",
        "dependee": {
          "api_name": "api_name",
          "json_path": "$.merge[0].master_record_fields[0].api_name"
        }
      },
      "message": "_data array is not mentioned for the master record",
      "status": "error"
    }
  ]
}
```
