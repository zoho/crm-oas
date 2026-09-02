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
