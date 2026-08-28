# Examples: fetchFullDataForSingleRecord

**GET /{moduleApiName}/{id}/actions/fetch_full_data**

## Parameter examples

### `moduleApiName` (path) — Leads

Leads module

```json
"Leads"
```

### `moduleApiName` (path) — Contacts

Contacts module

```json
"Contacts"
```

### `fields` (query) — SingleField

A single rich text field API name

```json
"RichTextField1"
```

### `fields` (query) — MultipleFields

A comma-separated list of multiple rich text field API names

```json
"RichTextField1,RichTextField2,RichTextField3"
```

### `id` (path) — LeadId

Typical lead record ID

```json
"3652397000000624001"
```

### `id` (path) — ContactId

Typical contact record ID

```json
"3652397000000624002"
```

## Response examples

### Status `200` — `application/json` — SingleRecord

```json
{
  "data": [
    {
      "id": "1043386000018763408",
      "Rich_Text_1": "<b>Bold Content</b>",
      "Rich_Text_2": "<i>Italic Content</i>"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidModule

Invalid Module

```json
{
  "code": "INVALID_MODULE",
  "details": {
    "resource_path_index": 0
  },
  "message": "the module name given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidRequest

Invalid Request

```json
{
  "code": "INVALID_REQUEST",
  "details": {},
  "message": "unable to process your request. please verify whether you have entered proper method name, parameter and parameter values.",
  "status": "error"
}
```

### Status `401` — `application/json` — AuthenticationFailure

Authentication Failure

```json
{
  "code": "AUTHENTICATION_FAILURE",
  "details": {},
  "message": "Authentication failed",
  "status": "error"
}
```

### Status `401` — `application/json` — OAuthScopeMismatch

OAuth Scope Mismatch

```json
{
  "code": "OAUTH_SCOPE_MISMATCH",
  "details": {},
  "message": "invalid oauth scope to access this URL",
  "status": "error"
}
```

### Status `500` — `application/json` — ErrorExample

```json
{
  "code": "INTERNAL_ERROR",
  "message": "Internal Server Error",
  "details": {},
  "status": "error"
}
```
