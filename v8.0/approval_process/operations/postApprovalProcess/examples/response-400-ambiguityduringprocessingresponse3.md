Error response with code AMBIGUITY_DURING_PROCESSING: ambiguity while processing the request

```json
{
  "approval_process": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "level",
            "json_path": "$.approval_process[0].rules[0].approver_stages[0].approver.level"
          },
          {
            "api_name": "level_up_to",
            "json_path": "$.approval_process[0].rules[0].approver_stages[0].approver.level_up_to"
          }
        ]
      },
      "message": "Ambiguity while processing the request",
      "status": "error"
    }
  ]
}
```
