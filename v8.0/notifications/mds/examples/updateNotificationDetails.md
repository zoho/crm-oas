# Examples: updateNotificationDetails

**PUT /actions/watch**

## Request examples

### `application/json` — Sample

Replace all details of a notification channel

```json
{'watch': [{'channel_id': '1000000068001', 'notify_url': 'https://www.example.com/callback', 'channel_expiry': TimeStamp(2025, 11, 25, 12, 0, tzinfo=datetime.timezone(datetime.timedelta(0), 'Z')), 'events': ['Leads.create', 'Contacts.edit', 'Deals.delete'], 'notification_condition': [{'type': 'field_selection'}], 'notify_on_related_action': True, 'token': 'TOKEN_FOR_VERIFICATION_OF_1000000068001'}]}
```

## Response examples

### Status `200` — `application/json` — Sample

Successful notification channel full replacement response

```json
{'watch': [{'code': 'SUCCESS', 'details': {'events': [{'channel_expiry': TimeStamp(2023, 8, 11, 2, 4, 14, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=46800), '-11:00')), 'resource_uri': 'https://www.zohoapis.com/crm/v8/Contacts', 'resource_id': '554023000000000129', 'resource_name': 'Contacts', 'channel_id': '10000'}, {'channel_expiry': TimeStamp(2023, 8, 11, 2, 4, 14, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=46800), '-11:00')), 'resource_uri': 'https://www.zohoapis.com/crm/v8/Deals', 'resource_id': '554023000000000131', 'resource_name': 'Deals', 'channel_id': '10000'}]}, 'message': 'Successfully subscribed for actions-watch of the given module', 'status': 'success'}]}
```

### Status `207` — `application/json` — MultiStatusResponse

```json
{'watch': [{'code': 'SUCCESS', 'details': {'events': [{'channel_expiry': TimeStamp(2025, 12, 18, 20, 33, 55), 'resource_uri': 'https://www.zohoapis.com/crm/v2/Leads', 'resource_id': '4794080000000000125', 'resource_name': 'Leads', 'channel_id': '175720435875'}]}, 'message': 'Successfully subscribed for actions-watch of the given module', 'status': 'success'}, {'code': 'MANDATORY_NOT_FOUND', 'details': {'api_name': 'channel_id', 'json_path': '$.watch[1].channel_id'}, 'message': 'required field not found', 'status': 'error'}]}
```

### Status `400` — `application/json` — MandatoryNotFound

Required field notify_url missing from the request

```json
{
  "code": "MANDATORY_NOT_FOUND",
  "message": "required field not found",
  "details": {
    "api_name": "notify_url"
  },
  "status": "error"
}
```

### Status `400` — `application/json` — ModuleNotSupported

Unsupported module referenced in the events field

```json
{
  "code": "INVALID_DATA",
  "message": "invalid data",
  "details": {
    "api_name": "events"
  },
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidFieldInFields

Invalid field reference in the fields parameter

```json
{
  "code": "INVALID_DATA",
  "message": "invalid data",
  "details": {
    "api_name": "fields",
    "json_path": "$.watch[0].fields[1]"
  },
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidNotificationConditionDataType

Invalid data type for the notification_condition field

```json
{
  "code": "INVALID_DATA",
  "message": "invalid data",
  "details": {
    "api_name": "notification_condition",
    "json_path": "$.watch[0].notification_condition"
  },
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataTypeForUnderscoreDelete

Invalid data type for the _delete field

```json
{
  "code": "INVALID_DATA",
  "message": "invalid data",
  "details": {
    "api_name": "_delete",
    "expected_data_type": "boolean",
    "json_path": "$.watch[0]._delete"
  },
  "status": "error"
}
```

### Status `400` — `application/json` — RequestFieldModuleNotAvailableInNotificationCondition

Specified module is not available in the notification condition

```json
{
  "code": "INVALID_DATA",
  "message": "required field not found",
  "details": {
    "api_name": "module",
    "json_path": "$.watch[0].notification_condition[0].module"
  },
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataTypeForModuleInNotificationCondition

Invalid data type for the module field in the notification condition

```json
{
  "code": "INVALID_DATA",
  "message": "invalid data",
  "details": {
    "api_name": "module",
    "expected_data_type": "jsonobject",
    "json_path": "$.watch[0].notification_condition[0].module"
  },
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataTypeForApiNameInModuleOfNotificationCondition

Invalid data type for api_name in the notification condition module

```json
{
  "code": "INVALID_DATA",
  "message": "invalid data",
  "details": {
    "api_name": "api_name",
    "expected_data_type": "string",
    "json_path": "$.watch[0].notification_condition[0].module.api_name"
  },
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataTypeForIdInModuleOfNotificationCondition

Invalid data type for the module ID field in the notification condition

```json
{
  "code": "INVALID_DATA",
  "message": "invalid data",
  "details": {
    "api_name": "id",
    "expected_data_type": "string",
    "json_path": "$.watch[0].notification_condition[0].module.api_name"
  },
  "status": "error"
}
```

### Status `400` — `application/json` — BothApiNameAndIdIsMissingInModuleOfNotificationCondition

Both api_name and module ID missing from the notification condition

```json
{
  "code": "EXPECTED_FIELD_MISSING",
  "message": "Specify atleast one field",
  "details": {
    "expected_fields": [
      {
        "api_name": "api_name",
        "json_path": "$.watch[0].notification_condition[0].module.api_name"
      },
      {
        "api_name": "id",
        "json_path": "$.watch[0].notification_condition[0].module.id"
      }
    ]
  },
  "status": "error"
}
```

### Status `400` — `application/json` — AmbiguityWhileProcessingModuleApiNameAndIdInNotificationCondition

Ambiguity between api_name and module ID in the notification condition

```json
{
  "code": "AMBIGUITY_DURING_PROCESSING",
  "message": "AMBIGUITY_DURING_PROCESSING",
  "details": {
    "ambiguity_due_to": [
      {
        "api_name": "api_name",
        "json_path": "$.watch[0].notification_condition[0].module.api_name"
      },
      {
        "api_name": "id",
        "json_path": "$.watch[0].notification_condition[0].module.id"
      }
    ]
  },
  "status": "error"
}
```

### Status `400` — `application/json` — DependentFieldMissingInModuleOfNotificationCondition

Dependent field field_selection missing from the notification condition

```json
{
  "code": "DEPENDENT_FIELD_MISSING",
  "message": "DEPENDENT_FIELD_MISSING",
  "details": {
    "api_name": "field_selection",
    "json_path": "$.watch[0].notification_condition[0].field_selection",
    "dependee": {
      "api_name": "type",
      "json_path": "$.watch[0].notification_condition[0].type"
    }
  },
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataTypeForFieldSelection

Invalid data type for the field_selection field

```json
{
  "code": "INVALID_DATA",
  "message": "invalid data",
  "details": {
    "api_name": "field_selection",
    "json_path": "$.watch[0].notification_condition[0].field_selection",
    "expected_data_type": "jsonobject"
  },
  "status": "error"
}
```

### Status `400` — `application/json` — MandatoryGroupOperatorNotFound

Required group_operator field missing from the field_selection

```json
{
  "code": "MANDATORY_NOT_FOUND",
  "message": "required field not found",
  "details": {
    "api_name": "group_operator",
    "json_path": "$.watch[0].notification_condition[0].field_selection.group_operator"
  },
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataTypeForGroupOperator

Invalid data type for the group_operator field

```json
{
  "code": "INVALID_DATA",
  "message": "invalid data",
  "details": {
    "api_name": "group_operator",
    "json_path": "$.watch[0].notification_condition[0].field_selection.group_operator",
    "expected_data_type": "text"
  },
  "status": "error"
}
```

### Status `400` — `application/json` — UnsupportedValueForGroupOperator

Unsupported value for the group_operator field

```json
{
  "code": "INVALID_DATA",
  "message": "invalid data",
  "details": {
    "api_name": "group_operator",
    "json_path": "$.watch[0].notification_condition[0].field_selection.group_operator",
    "supported_values": [
      "or",
      "and"
    ]
  },
  "status": "error"
}
```

### Status `400` — `application/json` — MandatoryFieldOrGroupNotFound

Required field or group array missing from the notification condition

```json
{
  "code": "MANDATORY_NOT_FOUND",
  "message": "required field not found",
  "details": {
    "api_name": "field",
    "json_path": "$.watch[0].notification_condition.field_selection.field"
  },
  "status": "error"
}
```

### Status `400` — `application/json` — NotificationCriteriaLimitExceeded

Field reference limit exceeded in the field_selection

```json
{
  "code": "INVALID_DATA",
  "message": "invalid data",
  "details": {
    "api_name": "field_selection",
    "json_path": "$.watch[0].notification_condition.field_selection",
    "maximum_length": 10
  },
  "status": "error"
}
```

### Status `400` — `application/json` — MandatoryTypeNotFound

Required type field missing from the notification condition

```json
{
  "code": "MANDATORY_NOT_FOUND",
  "message": "required field not found",
  "details": {
    "api_name": "type",
    "json_path": "$.watch[0].notification_condition[0].type"
  },
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataTypeForType

Invalid data type for the type field

```json
{
  "code": "INVALID_DATA",
  "message": "invalid data",
  "details": {
    "api_name": "type",
    "json_path": "$.watch[0].notification_condition[0].type",
    "expected_data_type": "text"
  },
  "status": "error"
}
```

### Status `400` — `application/json` — UnsupportedValueForType

Unsupported value for the type field

```json
{
  "code": "INVALID_DATA",
  "message": "invalid data",
  "details": {
    "api_name": "type",
    "json_path": "$.watch[0].notification_condition[0].type",
    "supported_values": [
      "field_selection"
    ]
  },
  "status": "error"
}
```

### Status `401` — `application/json` — OauthScopeMismatch

Missing required OAuth scope

```json
{
  "code": "OAUTH_SCOPE_MISMATCH",
  "message": "Unauthorized",
  "status": "error"
}
```

### Status `429` — `application/json` — RateLimitExceeded

API rate limit exceeded

```json
{
  "code": "RATE_LIMIT_EXCEEDED",
  "message": "Too many requests. Please try again later.",
  "status": "error"
}
```

### Status `500` — `application/json` — Sample

Unexpected internal server error

```json
{
  "code": "INTERNAL_ERROR",
  "message": "An unexpected error occurred.",
  "status": "error"
}
```
