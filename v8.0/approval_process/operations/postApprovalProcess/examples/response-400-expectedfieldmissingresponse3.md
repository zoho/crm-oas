Represents the error returned when the Approval Process create request is missing a required field in its configuration. The response contains the EXPECTED_FIELD_MISSING code along with the message that one of the required fields is missing.

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
            "json_path": "$.approval_process[*].rules[*].criteria.field.api_name"
          },
          {
            "api_name": "id",
            "json_path": "$.approval_process[*].rules[*].criteria.field.approval_process.rules.criteria.field.id"
          }
        ]
      },
      "status": "error"
    }
  ]
}
```
