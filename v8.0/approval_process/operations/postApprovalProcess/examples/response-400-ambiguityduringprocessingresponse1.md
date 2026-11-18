Invalid field API name in the request

```json
{
  "approval_process": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "id",
            "json_path": "$.approval_process[0].rules[0].approver_stages[1].approver.based_on_field.id"
          },
          {
            "api_name": "api_name",
            "json_path": "$.approval_process[0].rules[0].approver_stages[1].approver.based_on_field.api_name"
          }
        ]
      },
      "message": "The field api name seems to be invalid",
      "status": "error"
    }
  ]
}
```
