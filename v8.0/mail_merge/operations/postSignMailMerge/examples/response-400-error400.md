Example of missing required field error response.

```json
{
  "sign_mail_merge": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "mail_merge_template",
        "json_path": "$.sign_mail_merge[0].mail_merge_template"
      },
      "message": "Required field is missing",
      "status": "error"
    }
  ]
}
```
