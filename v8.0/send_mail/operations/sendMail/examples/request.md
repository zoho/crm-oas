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
