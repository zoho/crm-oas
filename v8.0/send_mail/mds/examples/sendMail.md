# Examples: sendMail

**POST /{moduleName}/{id}/actions/send_mail**

## Request examples

### `application/json` — FullRequest

Comprehensive send mail request with all recipient fields

```json
{
  "data": [
    {
      "from": {
        "user_name": "Sales",
        "email": "sales@company.com"
      },
      "to": [
        {
          "user_name": "Lead",
          "email": "lead@client.com"
        }
      ],
      "cc": [
        {
          "email": "manager@company.com"
        }
      ],
      "bcc": [
        {
          "email": "admin@company.com"
        }
      ],
      "reply_to": {
        "email": "support@company.com"
      },
      "subject": "Product Update",
      "content": "<h1>Hello</h1>",
      "mail_format": "html",
      "org_email": true
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — Success

Successful email send response

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "status": "success",
      "message": "Mail sent successfully",
      "details": {
        "message_id": "2cceafa...867"
      }
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryMissing

Missing required field error

```json
{
  "data": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `403` — `application/json` — NoPermission

Permission denied error

```json
{
  "code": "NO_PERMISSION",
  "message": "permission denied",
  "status": "error"
}
```
