# Examples: getEmailSharingDetail

**GET /{moduleApiName}/{id}/__emails_sharing_details**

## Parameter examples

### `moduleApiName` (path) — Example

```json
"Leads"
```

### `id` (path) — Example

```json
"412463000000867017"
```

## Response examples

### Status `200` — `application/json` — EmailsSharingDetailsResponseExample

Successful response with email sharing details for a record

```json
{
  "__emails_sharing_details": [
    {
      "available_types": [
        "emails_sent_from_crm",
        "all_contacts_emails",
        "all_imap_shared_users",
        "all_emails"
      ],
      "shared_from_users": [
        {
          "id": "412463000001213019",
          "name": "Will Grandon",
          "_type": "pop"
        },
        {
          "id": "412463000000867017",
          "name": "boyle",
          "_type": "imap"
        }
      ]
    }
  ]
}
```

### Status `400` — `application/json` — InvalidModuleExample

400 error response for an unrecognized module API name

```json
{
  "code": "INVALID_MODULE",
  "message": "The module API name is invalid.",
  "details": {
    "resource_path_index": 3
  },
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataExample

400 error response for invalid request data

```json
{
  "code": "INVALID_DATA",
  "message": "The given data is invalid.",
  "details": {
    "resource_path_index": 3
  },
  "status": "error"
}
```
