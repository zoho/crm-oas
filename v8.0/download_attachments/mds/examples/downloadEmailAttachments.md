# Examples: downloadEmailAttachments

**GET /{module}/{recordId}/Emails/actions/download_attachments**

## Response examples

### Status `400` — `application/json` — InvalidData

INVALID_DATA error when the record ID is incorrect. 

```json
{
  "status": "error",
  "code": "INVALID_DATA",
  "message": "Invalid record ID provided."
}
```

### Status `401` — `application/json` — AuthFail

INVALID_TOKEN error for an invalid OAuth access token

```json
{
  "status": "error",
  "code": "INVALID_TOKEN",
  "message": "Invalid token."
}
```
