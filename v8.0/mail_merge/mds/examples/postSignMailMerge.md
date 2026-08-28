# Examples: postSignMailMerge

**POST /{moduleApiName}/{recordId}/actions/sign_mail_merge**

## Request examples

### `application/json` — SamplePostRequest

Sign mail merge request body

```json
{
  "sign_mail_merge": [
    {
      "mail_merge_template": {
        "name": "mailmergename"
      },
      "file_name": "testdocument",
      "sign_in_order": true,
      "signers": [
        {
          "recipient_name": "Sam",
          "action_type": "sign",
          "recipient": {
            "type": "email",
            "value": "smith@gmail.com"
          }
        },
        {
          "recipient_name": "John",
          "action_type": "approve",
          "recipient": {
            "type": "email",
            "value": "john@gmail.com"
          }
        },
        {
          "recipient_name": "John",
          "action_type": "approve",
          "recipient": {
            "type": "merge_field",
            "value": "${!Leads.Last_Name}"
          }
        }
      ]
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — Success200

Successful sign mail merge response

```json
{
  "sign_mail_merge": [
    {
      "code": "SUCCESS",
      "details": {
        "sign_resource_id": "112953000000044001",
        "report_link": "https://writer.zoho.com/writer/v1/mailmerge/job/e1aee66cb489b8e89f8df4c8e36847ff2c1ec12b0b945e6f41314d5ca9a0870f710d651349ecdc916fbff687b9db8b3e"
      },
      "message": "send mail merge action initiated successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — Error400

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
