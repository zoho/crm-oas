Multiple validation errors in a single record

```json
{
  "data": [
    {
      "code": "MULTIPLE_OR_MULTI_ERRORS",
      "details": {
        "errors": [
          {
            "code": "DUPLICATE_DATA",
            "details": {
              "api_name": "Email",
              "duplicate_record": {
                "Owner": {
                  "name": "Prajesh Kumar S",
                  "id": "4881139000000307001",
                  "zuid": "736078909"
                },
                "module": {
                  "api_name": "Leads",
                  "id": "4881139000000002175"
                },
                "id": "4881139000000428295"
              },
              "json_path": "$.data[0].Email",
              "more_records": true
            },
            "message": "duplicate data",
            "status": "error"
          },
          {
            "code": "DUPLICATE_DATA",
            "details": {
              "api_name": "Mobile",
              "duplicate_record": {
                "Owner": {
                  "name": "Prajesh Kumar S",
                  "id": "4881139000000307001",
                  "zuid": "736078909"
                },
                "module": {
                  "api_name": "Leads",
                  "id": "4881139000000002175"
                },
                "id": "4881139000002432007"
              },
              "json_path": "$.data[0].Mobile",
              "more_records": true
            },
            "message": "duplicate data",
            "status": "error"
          }
        ]
      },
      "message": "Multiple errors in the request",
      "status": "error"
    }
  ]
}
```
