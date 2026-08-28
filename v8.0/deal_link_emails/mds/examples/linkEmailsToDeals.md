# Examples: linkEmailsToDeals

**POST /Contacts/{contactId}/Emails/actions/link_record**

## Request examples

### `application/json` — SampleRequestBody

Link Emails to Deals

```json
{
  "Emails": [
    {
      "message_id": "f129cbd6953db55b4464b4dfc6f5cd3ebc57ab5c83a16c6d08843a24d4f4cfbc04e4b089882b920f306be5735ce55782",
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
    },
    {
      "message_id": "f129cbd6953db55b4464b4dfc6f5cd3ebc57ab5c83a16c6d08843a24d4f4cfbc04e4b089882b920f306be5735ce55782",
      "owner": {
        "id": "4876876000000362001"
      },
      "linked_record": {
        "module": {
          "api_name": "Deals",
          "id": "4876876000000000131"
        },
        "id": "4876876000000002676"
      }
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — SampleResponse

Link Emails to Deals - Response

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
    },
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

### Status `400` — `application/json` — SampleErrorResponse

Link Emails to Deals - Error Response

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
          "json_path": "Emails[0].message_id"
        }
      }
    ],
    [
      {
        "status": "error",
        "code": "INVALID_DATA",
        "message": "invalid data",
        "details": {
          "api_name": "linked_record.id",
          "json_path": "Emails[1].linked_record.id"
        }
      }
    ]
  ]
}
```

### Status `404` — `application/json` — SampleNotFoundResponse

Link Emails to Deals - Not Found Response

```json
{
  "status": "error",
  "code": "INVALID_URL_PATTERN",
  "message": "Please check if the URL trying to access is a correct one",
  "details": {}
}
```
