# Examples: getDownloadInlineImages

**GET /{module}/{recordId}/Emails/actions/download_inline_images**

## Response examples

### Status `400` — `application/json` — ErrorExample

INVALID_DATA error for an invalid record ID.

```json
{
  "status": "error",
  "code": "INVALID_DATA",
  "message": "The provided record ID is invalid",
  "details": {
    "resource_path_index": 1
  }
}
```
