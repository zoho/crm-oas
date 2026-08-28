# Examples: linkEmailToRecord

**POST /Contacts/{contactId}/Emails/{messageId}/actions/link_record**

## Request examples

### `application/json` — SampleRequestBody

Link Email to Record - Request Body

```json
{
  "Emails": [
    {
      "owner": {
        "id": "4876876000000362001"
      },
      "linked_record": {
        "module": {
          "api_name": "Deals",
          "id": "4876876000000000131"
        },
        "name": "Acme Renewal Deal",
        "id": "4876876000000514024"
      }
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — SampleResponse

Link Email to Record - Response

```json
{
  "Emails": [
    {
      "status": "success",
      "code": "SUCCESS",
      "message": "Email linked to the record successfully",
      "details": {
        "message_id": "f129cbd6953db55b4464b4dfc6f5cd3ebc57ab5c83a16c6d08843a24d4f4cfbc04e4b089882b920f306be5735ce55782"
      }
    }
  ]
}
```
