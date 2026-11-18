Shows the error response for an Approval Process create request in which one of the required fields is not provided. The response returns the EXPECTED_FIELD_MISSING code and states that one of the required fields is missing.

```json
{
  "approval_process": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "message": "One of the required fields is missing",
      "details": {
        "expected_fields": [
          {
            "api_name": "api_name",
            "json_path": "$.approval_process[*].module.api_name"
          },
          {
            "api_name": "id",
            "json_path": "$.approval_process[*].module.approval_process.module.id"
          }
        ]
      },
      "status": "error"
    }
  ]
}
```
