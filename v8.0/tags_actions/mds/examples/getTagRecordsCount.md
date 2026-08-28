# Examples: getTagRecordsCount

**GET /settings/tags/{id}/actions/records_count**

## Parameter examples

### `module` (query) — Example

```json
"Leads"
```

## Response examples

### Status `200` — `application/json` — Success200

Success response for status 200

```json
{
  "configured_areas": {
    "workflow_tagActionRecords": {
      "Orchestration": {
        "3060320000000666022": {
          "RemoveTags": [
            {
              "name": "newtd, newraf, test, new, new2, three, 34ytwerfdgjhfwgerfs, asf, daf, das, dw, fr, e, gfe, ht, oy, kjtd, hfsdgfas, d, ds",
              "rules": [
                {
                  "subtype_name": "rewq",
                  "subtype": "transition",
                  "module": "Leads",
                  "name": "qwert - V1",
                  "execution_type": "instant",
                  "id": "3060320000002372133",
                  "source": 1,
                  "subtype_id": "3060320000002183036",
                  "status": "Active"
                }
              ],
              "id": "3060320000002372782"
            }
          ],
          "AddTags": [
            {
              "name": "34ytwerfdgjhfwgerfs, newtd, newraf, new2, three, asf, daf, das, f, dw, fr, e, gfe, ht, jryi, oy, new, kjtd, hfsdgfas, d",
              "rules": [
                {
                  "subtype_name": "test",
                  "subtype": "state",
                  "module": "Leads",
                  "name": "qwert - V1",
                  "execution_type": "instant",
                  "id": "3060320000002372133",
                  "source": 1,
                  "subtype_id": "3060320000002372686",
                  "status": "Active"
                }
              ],
              "id": "3060320000002372688"
            }
          ]
        }
      },
      "Blueprint": {
        "3060320000000666022": {
          "RemoveTags": [
            {
              "name": "newtd, newraf, test, new, new2, three, asf, daf, f, das, dw, fr, e, gfe, ht, jryi, 34ytwerfdgjhfwgerfs, oy, hfsdgfas, d",
              "rules": [
                {
                  "subtype_name": "qwertyu",
                  "subtype": "transition",
                  "module": "Leads",
                  "name": "new",
                  "execution_type": "instant",
                  "id": "3060320000001828051",
                  "source": 1,
                  "subtype_id": "3060320000001828038"
                }
              ],
              "id": "3060320000002372109"
            }
          ],
          "AddTags": [
            {
              "name": "blue, newtd, newraf, test, 34ytwerfdgjhfwgerfs, new2, three, asf, daf, das, f, dw, fr, e, gfe, ht, jryi, oy, kjtd, hfsdgfas",
              "rules": [
                {
                  "subtype_name": "qwertyu",
                  "subtype": "transition",
                  "module": "Leads",
                  "name": "new",
                  "execution_type": "instant",
                  "id": "3060320000001828051",
                  "source": 1,
                  "subtype_id": "3060320000001828038"
                }
              ],
              "id": "3060320000001828044"
            }
          ]
        }
      },
      "Workflow": {
        "3060320000000666022": {
          "RemoveTags": [
            {
              "name": "newraf, test, new, new2, three, 34ytwerfdgjhfwgerfs, newtd, daf, das, f, dw, fr, e, gfe, ht, jryi, asf, oy, kjtd, hfsdgfas",
              "rules": [
                {
                  "subtype": "rule_condition",
                  "module": "Leads",
                  "name": "qwerty",
                  "execution_type": "instant",
                  "id": "3060320000002072019",
                  "source": 1,
                  "subtype_id": "3060320000002072020"
                }
              ],
              "id": "3060320000002372082"
            },
            {
              "name": "newtd, newraf, test, new, new2, three, asf, daf, das, 34ytwerfdgjhfwgerfs, fr, e, gfe, dw, ht, jryi, oy, kjtd, hfsdgfas, d",
              "rules": [
                {
                  "subtype": "rule_condition",
                  "module": "Leads",
                  "name": "qwerty",
                  "execution_type": "schedule",
                  "id": "3060320000002072019",
                  "source": 1,
                  "subtype_id": "3060320000002072020"
                }
              ],
              "id": "3060320000002372091"
            }
          ],
          "AddTags": [
            {
              "name": "newtd, newraf, test, new, new2, three, asf, daf, das, f, dw, fr, e, gfe, 34ytwerfdgjhfwgerfs, ht, jryi, kjtd, hfsdgfas, d",
              "rules": [
                {
                  "subtype": "rule_condition",
                  "module": "Leads",
                  "name": "qwerty",
                  "execution_type": "instant",
                  "id": "3060320000002072019",
                  "source": 1,
                  "subtype_id": "3060320000002072020"
                }
              ],
              "id": "3060320000002372081"
            },
            {
              "name": "34ytwerfdgjhfwgerfs, test, new, new2, three, newraf, asf, daf, das, f, dw, fr, e, gfe, ht, jryi, oy, kjtd, hfsdgfas, d",
              "rules": [
                {
                  "subtype": "rule_condition",
                  "module": "Leads",
                  "name": "qwerty",
                  "execution_type": "schedule",
                  "id": "3060320000002072019",
                  "source": 1,
                  "subtype_id": "3060320000002072020"
                }
              ],
              "id": "3060320000002072235"
            },
            {
              "name": "newraf, 34ytwerfdgjhfwgerfs, test",
              "rules": [
                {
                  "subtype": "rule_condition",
                  "module": "Leads",
                  "name": "New Rule",
                  "execution_type": "instant",
                  "id": "3060320000000666866",
                  "source": 1,
                  "subtype_id": "3060320000000666867"
                }
              ],
              "id": "3060320000000666870"
            }
          ]
        }
      }
    },
    "custom_view": {
      "cvnames": [],
      "inaccessible_custom_view_present": false,
      "cvmodules": [],
      "cvids": []
    }
  },
  "count": "18"
}
```

### Status `400` — `application/json` — RequiredParamMissingResponse1

Error response with code REQUIRED_PARAM_MISSING: One of the expected param is missing

```json
{
  "code": "REQUIRED_PARAM_MISSING",
  "details": {
    "param_name": "module"
  },
  "message": "One of the expected param is missing",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidModuleResponse1

Error response with code INVALID_MODULE: the module name given seems to be invalid

```json
{
  "code": "INVALID_MODULE",
  "details": {},
  "message": "the module name given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidModuleResponse2

Error response with code INVALID_MODULE: the given module is not supported for this api

```json
{
  "code": "INVALID_MODULE",
  "details": {},
  "message": "the given module is not supported for this api",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidRequestMethodResponse1

Error response with code INVALID_REQUEST_METHOD: The http request method type is not a valid one

```json
{
  "code": "INVALID_REQUEST_METHOD",
  "details": {},
  "message": "The http request method type is not a valid one",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermissionResponse1

Error response with code NO_PERMISSION: permission denied

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Edit_Leads",
      "Crm_Implied_Tags_Leads"
    ]
  },
  "message": "permission denied",
  "status": "error"
}
```

### Status `404` — `application/json` — TagIdNotFoundResponse1

Error response with code INVALID_DATA: invalid tag id

```json
{
  "code": "INVALID_DATA",
  "details": {
    "api_name": "id"
  },
  "message": "tags not found",
  "status": "error"
}
```
