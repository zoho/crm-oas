DEPENDENT_FIELD_MISSING error: Dependent field is missing (submission_redirect_url)

```json
{
  "unsubscribe_links": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "message": "Dependent field is missing",
      "details": {
        "dependee": {
          "api_name": "submission_action_type",
          "json_path": "$.unsubscribe_links[*].submission_action_type"
        },
        "api_name": "submission_redirect_url",
        "json_path": "$.unsubscribe_links[*].unsubscribe_links.submission_redirect_url"
      },
      "status": "error"
    }
  ]
}
```
