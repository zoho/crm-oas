EXPECTED_FIELD_MISSING error for missing captcha configuration fields

```json
{
  "webforms": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "site_key",
            "json_path": "$.webforms[0].form_fields[2].site_key"
          },
          {
            "api_name": "secret_key",
            "json_path": "$.webforms[0].form_fields[2].secret_key"
          },
          {
            "api_name": "recaptcha_label",
            "json_path": "$.webforms[0].form_fields[2].recaptcha_label"
          }
        ]
      },
      "message": "One of the expected field missing",
      "status": "error"
    }
  ]
}
```
