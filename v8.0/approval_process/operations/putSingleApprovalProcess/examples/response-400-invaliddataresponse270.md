Field-mapping id of a rejection action exceeds 25 characters

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 25,
        "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.actions[*].details.field_mappings[*].field.id"
      },
      "status": "error"
    }
  ]
}
```
