DEPENDENT_FIELD_MISSING error: required field not found (submission_action_type)

```json
{
  "unsubscribe_links": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "submission_redirect_url",
          "json_path": "$.unsubscribe_links[0].submission_redirect_url"
        },
        "api_name": "submission_action_type",
        "json_path": "$.unsubscribe_links[0].submission_action_type"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```
