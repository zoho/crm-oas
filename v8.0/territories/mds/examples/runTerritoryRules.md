# Examples: runTerritoryRules

**POST /settings/territories/actions/run_rules**

## Request examples

### `application/json` — RunRulesExample

Criteria-based territory rule execution for a module

```json
{
  "run_rules": {
    "based_on": "criteria",
    "criteria": {
      "comparator": "equal",
      "field": {
        "api_name": "Account_Name"
      },
      "value": "test"
    },
    "module": {
      "id": "11111000736439"
    }
  }
}
```

## Response examples

### Status `202` — `application/json` — TerritoryRulesScheduled

Scheduled response for territory rules execution

```json
{
  "run_rules": {
    "code": "SCHEDULED",
    "details": {
      "job_id": "111111678900087967"
    },
    "message": "Territory rules scheduled successfully.Once done, completion email will be sent.",
    "status": "success"
  }
}
```

### Status `400` — `application/json` — InvalidDataOnTerritoryOption

Invalid territory ID in the territories array

```json
{
  "run_rules": {
    "code": "INVALID_DATA",
    "details": {
      "api_name": "id",
      "json_path": "$.run_rules.territories[0].id"
    },
    "message": "the given value is invalid",
    "status": "error"
  }
}
```

### Status `400` — `application/json` — MandatoryNotFound

Missing mandatory field in the territory run rules request

```json
{
  "run_rules": {
    "code": "MANDATORY_NOT_FOUND",
    "details": {
      "api_name": "module",
      "json_path": "$.run_rules.module"
    },
    "message": "required field not found",
    "status": "error"
  }
}
```

### Status `400` — `application/json` — DependentFieldMissing

Dependent field missing when custom_view is provided without based_on

```json
{
  "run_rules": {
    "code": "DEPENDENT_FIELD_MISSING",
    "details": {
      "dependee": {
        "api_name": "based_on",
        "json_path": "$.run_rules.based_on"
      },
      "api_name": "id",
      "json_path": "$.run_rules.custom_view"
    },
    "message": "Dependent Field missing",
    "status": "error"
  }
}
```

### Status `400` — `application/json` — InvalidDataForIncludeChild

Invalid data type for the include_child field

```json
{
  "run_rules": {
    "code": "INVALID_DATA",
    "details": {
      "expected_data_type": "boolean",
      "api_name": "include_child",
      "json_path": "$.run_rules.include_child"
    },
    "message": "invalid data",
    "status": "error"
  }
}
```

### Status `400` — `application/json` — AlreadyScheduled

Territory rules execution already scheduled

```json
{
  "code": "ALREADY_SCHEDULED",
  "message": "Previously scheduled Run Rules Action was not yet Completed. Please try again once it's completed",
  "status": "error",
  "details": {
    "job_id": "4476574676432"
  }
}
```

### Status `400` — `application/json` — AmbiguityDuringProcessing

Ambiguity error when both module.id and module.api_name are provided

```json
{
  "run_rules": {
    "code": "AMBIGUITY_DURING_PROCESSING",
    "details": {
      "ambiguity_due_to": [
        {
          "api_name": "api_name",
          "json_path": "$.run_rules.module.api_name"
        },
        {
          "api_name": "id",
          "json_path": "$.run_rules.module.id"
        }
      ]
    },
    "message": "Ambiguity while processing the request",
    "status": "error"
  }
}
```

### Status `400` — `application/json` — ExpectedFieldMissing

Expected field missing — module identifier not provided

```json
{
  "run_rules": {
    "code": "EXPECTED_FIELD_MISSING",
    "details": {
      "expected_fields": [
        {
          "api_name": "api_name",
          "json_path": "$.run_rules.module.api_name"
        },
        {
          "api_name": "id",
          "json_path": "$.run_rules.module.id"
        }
      ]
    },
    "message": "one of the expected field is missing",
    "status": "error"
  }
}
```

### Status `400` — `application/json` — LeadRuleNotEnabled

Territory lead rule not enabled for the organization

```json
{
  "run_rules": {
    "code": "FEATURE_NOT_ENABLED",
    "details": {},
    "message": "Territory Lead Rule Disabled",
    "status": "error"
  }
}
```

### Status `400` — `application/json` — DealRuleNotEnabled

Territory deal rule not enabled for the organization

```json
{
  "run_rules": {
    "code": "FEATURE_NOT_ENABLED",
    "details": {},
    "message": "Territory Deal Rule Disabled",
    "status": "error"
  }
}
```

### Status `400` — `application/json` — InvalidBasedOnValue

Invalid value provided for the based_on field

```json
{
  "run_rules": {
    "code": "INVALID_DATA",
    "details": {
      "api_name": "based_on",
      "json_path": "$.run_rules.based_on"
    },
    "message": "the given filter value is invalid",
    "status": "error"
  }
}
```

### Status `400` — `application/json` — InvalidCustomViewId

Invalid Custom View ID in the request

```json
{
  "run_rules": {
    "code": "INVALID_DATA",
    "details": {
      "api_name": "id",
      "json_path": "$.run_rules.custom_view.id"
    },
    "message": "the given value is invalid",
    "status": "error"
  }
}
```

### Status `400` — `application/json` — InvalidModuleApiName

Invalid module API name — only Leads, Accounts, and Deals are supported

```json
{
  "run_rules": {
    "code": "INVALID_DATA",
    "details": {
      "api_name": "api_name",
      "json_path": "$.run_rules.module.api_name"
    },
    "message": "invalid data",
    "status": "error"
  }
}
```

### Status `400` — `application/json` — InvalidModuleId

Invalid module ID in the request

```json
{
  "run_rules": {
    "code": "INVALID_DATA",
    "details": {
      "api_name": "id",
      "json_path": "$.run_rules.module.id"
    },
    "message": "invalid data",
    "status": "error"
  }
}
```

### Status `400` — `application/json` — TerritoryNotYetEnabled

Territory management not yet enabled for the organization

```json
{
  "code": "FEATURE_NOT_ENABLED",
  "details": {},
  "message": "Territory Management is not enabled",
  "status": "error"
}
```

### Status `400` — `application/json` — TerritoryDisabled

Territory management disabled for the organization

```json
{
  "code": "FEATURE_NOT_ENABLED",
  "details": {},
  "message": "Territory Management is disabled",
  "status": "error"
}
```

### Status `401` — `application/json` — AuthenticationFailure

Authentication failure due to an invalid or missing OAuth token

```json
{
  "code": "AUTHENTICATION_FAILURE",
  "details": {},
  "message": "Authentication failed",
  "status": "error"
}
```

### Status `403` — `application/json` — PermissionDenied

Permission denied to run territory assignment rules

```json
{
  "run_rules": {
    "code": "NO_PERMISSION",
    "details": {},
    "message": "You don't have permission to run rules based on criteria filter.",
    "status": "error"
  }
}
```

### Status `403` — `application/json` — RunRulesModuleNoPermission

Permission denied for the specified module in territory rule execution

```json
{
  "run_rules": {
    "code": "NO_PERMISSION",
    "details": {},
    "message": "You don't have permission for the module.",
    "status": "error"
  }
}
```
