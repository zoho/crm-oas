# Examples: unlinkEmailsFromDeal

**DELETE /Contacts/{contactId}/Emails/actions/link_record**

## Response examples

### Status `200` — `application/json` — SampleResponse

Unlink Emails from Deals - Response

```json
{
  "Emails": [
    {
      "status": "success",
      "code": "SUCCESS",
      "message": "Email unlinked from the record successfully",
      "details": {
        "message_id": "f129cbd6953db55b4464b4dfc6f5cd3ebc57ab5c83a16c6d08843a24d4f4cfbc04e4b089882b920f306be5735ce55782"
      }
    }
  ]
}
```

### Status `400` — `application/json` — SampleErrorResponse

Unlink Emails from Records - Error Response

```json
{
  "Emails": [
    [
      {
        "status": "error",
        "code": "MANDATORY_NOT_FOUND",
        "message": "message_id is mandatory",
        "details": {
          "api_name": "message_id",
          "json_path": "message_ids[0]"
        }
      }
    ]
  ]
}
```
