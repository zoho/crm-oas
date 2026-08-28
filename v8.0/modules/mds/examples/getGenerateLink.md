# Examples: getGenerateLink

**GET /settings/module/{moduleid}/actions/generate_link**

## Parameter examples

### `moduleid` (path) — Leads

Leads module API name

```json
"Leads"
```

### `moduleid` (path) — CustomModule

Custom module API name

```json
"Custom_Module_1"
```

## Response examples

### Status `200` — `application/json` — Success200

Successful generation of web-tab link for a module

```json
{
  "generate_link": {
    "name": "WebTab1",
    "id": "111111000000066002",
    "web_link": "https://www.wikipedia.org/"
  }
}
```

### Status `400` — `application/json` — InvalidModuleName

Invalid module name provided in path parameter

```json
{
  "code": "INVALID_DATA",
  "details": {
    "param_name": "module"
  },
  "message": "the module name given seems to be invalid",
  "status": "error"
}
```
