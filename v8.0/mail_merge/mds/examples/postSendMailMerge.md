# Examples: postSendMailMerge

**POST /{moduleApiName}/{recordId}/actions/send_mail_merge**

## Request examples

### `application/json` — SamplePostRequest

Send mail merge request body

```json
{
  "send_mail_merge": [
    {
      "mail_merge_template": {
        "name": "mailmergename"
      },
      "from_address": {
        "type": "email",
        "value": "p.boyle@gmail.com"
      },
      "to_address": [
        {
          "type": "email",
          "value": "smith@abc.com"
        },
        {
          "type": "email",
          "value": "john@abc.com"
        }
      ],
      "subject": "Hi there",
      "cc_email": [
        {
          "type": "email",
          "value": "brie.c@gmail.com"
        }
      ],
      "bcc_email": [
        {
          "type": "email",
          "value": "ceo.zylker@gmail.com"
        }
      ],
      "type": "attachment",
      "attachment_name": "testdocument",
      "message": "Big Deal"
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — Success200

Successful send mail merge response

```json
{
  "send_mail_merge": [
    {
      "code": "SUCCESS",
      "details": {
        "report_link": "https://writer.zoho.com/writer/v1/mailmerge/job/4791a19ea20e60e4a17c03f3b5feb149ef2caa18572d9587f26e041e5c47d868dca099732f2d7c6c51fed0693f066194"
      },
      "message": "send mail merge action initiated successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — Error400

Example of a missing required field error response.

```json
{
  "send_mail_merge": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "mail_merge_template",
        "json_path": "$.send_mail_merge[0].mail_merge_template"
      },
      "message": "Required field is missing",
      "status": "error"
    }
  ]
}
```
