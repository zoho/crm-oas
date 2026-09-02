Example of configuring Reporting To for child and Account for master (or vice versa).

```json
{
  "merge": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "api_name",
        "json_path": "$.merge[0].data[0]._fields[0].api_name"
      },
      "message": "Reporting to and account should belong to the same record",
      "status": "error"
    }
  ]
}
```
