# Examples: fetchFullDataForMultipleRecords

**GET /{moduleApiName}/actions/fetch_full_data**

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

### `ids` (query) — SingleId

A single record ID

```json
"3652397000000624001"
```

### `ids` (query) — MultipleIds

A comma-separated list of multiple record IDs

```json
"3652397000000624001,3652397000000624002,3652397000000624003"
```

## Response examples

### Status `200` — `application/json` — MultipleRecords

```json
{
  "data": [
    {
      "id": "1043386000018763408",
      "Rich_Text_1": "<b>Bold Content</b>",
      "Rich_Text_2": "<i>Italic Content</i>"
    },
    {
      "id": "1043386000018763409",
      "Rich_Text_1": "<p><b>Specifications:</b> Tonnage: 300</p>",
      "Rich_Text_2": "<p><b>Controller:</b> V22 Control</p>"
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

### Status `400` — `application/json` — RequiredParamMissing

Required Parameter Missing

```json
{
  "code": "REQUIRED_PARAM_MISSING",
  "details": {
    "param_name": "fields"
  },
  "message": "One of the expected parameter is missing",
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
