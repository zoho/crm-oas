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
