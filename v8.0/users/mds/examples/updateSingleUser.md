# Examples: updateSingleUser

**PUT /users/{user}**

## Request examples

### `application/json` — UserAdded

Update Single User Request

```json
{
  "users": [
    {
      "first_name": "rfdc2",
      "email": "user@example.com",
      "role": {
        "name": "CEO",
        "id": "2922942000000015966"
      },
      "profile": {
        "name": "Administrator",
        "id": "2922942000000015972"
      }
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — UserUpdatedSuccessfully

Single User Updated Successfully

```json
{
  "users": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111113000000071587"
      },
      "message": "User updated",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InValidUserIdResponse

Invalid User ID in Update Request

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 1
  },
  "message": "the id given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — DeletedUserUpdate

Updating a Deleted User

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "resource_path_index": 1
  },
  "message": "the id given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — ActivatingSupportUser

Activating a Support User

```json
{
  "users": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "id",
        "json_path": "$.users[0].id"
      },
      "message": "Support user cannot be activated",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ActivatingSystemUser

Activating a System User

```json
{
  "users": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "id",
        "json_path": "$.users[0].id"
      },
      "message": "System user cannot be activated",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — UpdatingCreatedByOrModifiedByField

Updating Read-Only Created By or Modified By Field

```json
{
  "users": [
    {
      "code": "NOT_SUPPORTED",
      "details": {
        "api_name": "created_by",
        "json_path": "$.users[0].created_by"
      },
      "message": "Created by & Modified by fields cannot be updated by api",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DeactivatingSupportUser

Deactivating a Support User

```json
{
  "users": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "id",
        "json_path": "$.users[0].id"
      },
      "message": "Support user cannot be deactivated",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DeactivatingSystemUser

Deactivating a System User

```json
{
  "users": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "id",
        "json_path": "$.users[0].id"
      },
      "message": "System user cannot be deactivated",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — UpdatingSupportUserDetails

Updating Support User Details

```json
{
  "users": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "id",
        "json_path": "$.users[0].id"
      },
      "message": "Cannot update the user details of support user",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — UpdatingDigitalUserStatus

Example request

```json
{
  "users": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "type__s",
        "json_path": "$.users[0].type__s"
      },
      "message": "Digital Employee cannot be Deleted / Deactivated / Activated",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — AssigningSystemProfileToUser

Assigning System Profile to User

```json
{
  "users": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "profile",
        "json_path": "$.users[0].profile"
      },
      "message": "System Profile cannot be assigned to other users",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — UpdatingDeletedUser

Updating a Deleted User

```json
{
  "users": [
    {
      "code": "CANNOT_UPDATE_DELETED_USER",
      "details": {},
      "message": "Deleted user cannot be updated",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — CrmPlusUserEmailUpdate

Email Update for CRM Plus User

```json
{
  "users": [
    {
      "code": "EMAIL_UPDATE_NOT_ALOWED",
      "details": {
        "api_name": "email"
      },
      "message": "Crm Plus account is not allowed to edit the email while updating the user info",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ReinvitingConfirmedUser

Re-inviting an Already Confirmed User

```json
{
  "users": [
    {
      "code": "INVALID_REQUEST",
      "details": {
        "api_name": "reinvite"
      },
      "message": "Reinvite is not allowed for a confirmed user",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — UpdatingEmailForAConfirmedUser

Updating Email for a Confirmed User

```json
{
  "users": [
    {
      "code": "EMAIL_UPDATE_NOT_ALOWED",
      "details": {
        "api_name": "email"
      },
      "message": "Cannot update email of a confirmed CRM User",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — UserAlreadyExistsInCRMplus

User Already Exists in CRM Plus

```json
{
  "users": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "email",
        "id": "0987654321"
      },
      "message": "User with same email id is already in CRM Plus",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DeactivatingAlreadyDeactivatedUser

Deactivating an Already Deactivated User

```json
{
  "users": [
    {
      "code": "ID_ALREADY_DEACTIVATED",
      "details": {
        "api_name": "id",
        "id": "$.users[0].id"
      },
      "message": "User is already deactivated",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DigitalUserStatusUpdate

Digital Employee User Status Change

```json
{
  "users": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "id": "0987654321"
      },
      "message": "You are not allowed to perform this operation.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — LoggedInUserStatusUpdate

Deactivating the Currently Logged-In User

```json
{
  "users": [
    {
      "code": "FEATURE_NOT_AVAILABLE",
      "details": {},
      "message": "Share among Subordinates Feature is not available",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — UserUpdatingWithNotEligibleReportingTo

Reporting To User Not Eligible

```json
{
  "users": [
    {
      "code": "CONFLICTING_DATA_FOUND",
      "details": {
        "api_name": "Reporting_To",
        "json_path": "$.users[0].Reporting_To"
      },
      "message": "the user must be updated with new eligible reporting manager because of changing user role",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — UserUpdatingWithNotEligibleSubordinates

Role Change Creates Invalid Subordinate Relationships

```json
{
  "users": [
    {
      "code": "CONFLICTING_DATA_FOUND",
      "details": {
        "api_name": "Reporting_To",
        "json_path": "$.users[0].Reporting_To"
      },
      "message": "the user must be updated with new eligible reporting manager and the subordinates  who are going to report to a user in a role below them, because of new role change are need to transfer to new eligible reporting manager",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — UpdatingSameUserIdAsReportingTo

Setting Self as Reporting To Manager

```json
{
  "users": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "ReportingTo Id should not be the same as userId"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — UpdatingUserWithReportingToWithNotSupportedRoles

Reporting To Not Supported for User Role

```json
{
  "users": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "Reporting_To"
      },
      "message": "Reporting manager should be from parent roles or from the same role to which the current user belongs",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ShareAmongFeatureNotEnabled

Share Among Feature Not Enabled

```json
{
  "users": [
    {
      "code": "INVALID_REQUEST",
      "details": {},
      "message": "You can't perform this action over logged in user",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DeactivatingPrimaryUser

Deactivating the Primary User

```json
{
  "users": [
    {
      "code": "INVALID_REQUEST",
      "details": {
        "id": "0987654321",
        "json_path": "$.users[0].id"
      },
      "message": "Primary Contact cannot be deactivated",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — AlreadyActiveUserActivation

Activating an Already Active User

```json
{
  "users": [
    {
      "code": "ID_ALREADY_ACTIVE",
      "details": {
        "id": "0987654321",
        "json_path": "$.users[0].id"
      },
      "message": "User is already active",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InsufficientPrevilidgesToUpdateUser

Insufficient Authorization to Update User

```json
{
  "users": [
    {
      "code": "AUTHORIZATION_FAILED",
      "details": {},
      "message": "Either trial is expired or user does not have sufficient previlege to perform this action",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — LicenseLimitExceededWhileActivatingUser

License Limit Exceeded While Activating User

```json
{
  "users": [
    {
      "code": "LICENSE_LIMIT_EXCEEDED",
      "details": {},
      "message": "License Limit is Exceeded",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MoreThanOneUserUpdationAttempt

More Than One User in Single User Update Request

```json
{
  "code": "INVALID_DATA",
  "details": {
    "maximum_length": 1,
    "api_name": "users",
    "json_path": "$.users"
  },
  "message": "invalid data",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataErrorResponse

Invalid Data in Update Request

```json
{
  "users": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "time_zone",
        "json_path": "$.users[0].time_zone"
      },
      "message": "Give a proper time zone value",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataInResponse2

Invalid Data - Alternate Scenario

```json
{
  "users": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "Valid userid should be given"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidProfieIdOrRoleIdOrLocale

Invalid Profile ID, Role ID, or Locale

```json
{
  "users": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "profile",
        "json_path": "$.users[0].profile"
      },
      "message": "INVALID_DATA",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NumberAndDecimalSeparatorMismatch

Number and Decimal Separator Cannot Be the Same

```json
{
  "users": [
    {
      "code": "MAPPING_MISMATCH",
      "details": {
        "mapped_field": {
          "api_name": "number_separator",
          "json_path": "$.users[0].number_separator"
        },
        "api_name": "decimal_separator",
        "json_path": "$.users[0].decimal_separator"
      },
      "message": "the number separator and decimal separator values should not be same",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidNumberSeparator

Invalid Number Separator

```json
{
  "users": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "number_separator",
        "json_path": "$.users[0].number_separator"
      },
      "message": "Invalid data. Valid values are Comma/Period/Space (Not case-sensitive)",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDecimalSeparator

Invalid Decimal Separator

```json
{
  "users": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "decimal_separator",
        "json_path": "$.users[0].decimal_separator"
      },
      "message": "Invalid data. Valid values are Comma/Period (Not case-sensitive)",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidNameFormat

Invalid Name Format

```json
{
  "users": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "name_format__s",
        "json_path": "$.users[0].name_format__s"
      },
      "message": "Valid name format should be given",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidSortPreference

Invalid Sort Order Preference

```json
{
  "users": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "sort_order_preference__s",
        "json_path": "$.users[0].sort_order_preference__s"
      },
      "message": "Valid sort order preference should be given",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NotUpdatingFortheSameUser

Not Allowed to Update Another User

```json
{
  "users": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "name_format__s"
      },
      "message": "Cannot update the name_format__s of another User",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidLanguageCode

Invalid Language Code

```json
{
  "users": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "language",
        "json_path": "$.users[0].language"
      },
      "message": "Give a proper language code",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — SpecialCharacterInField

Special Character in Field Value

```json
{
  "users": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "first_name",
        "json_path": "$.users[0].first_name"
      },
      "message": "Special Characters Found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — PatternMismatchInField

Pattern Mismatch in Field Value

```json
{
  "users": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "time_format",
        "json_path": "$.users[0].time_format"
      },
      "message": "Pattern not matched",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — UpdatingReportingToFieldWithoutEnablingReportingToFeature

Setting Reporting To Without Enabling the Feature

```json
{
  "users": [
    {
      "code": "FEATURE_NOT_ENABLED",
      "details": {},
      "message": "ReportingTo Feature is not enabled",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Updatingtypesfields

Updating Read-Only Type Field

```json
{
  "users": [
    {
      "code": "NOT_SUPPORTED",
      "details": {
        "api_name": "type__s",
        "json_path": "$.users[0].type__s"
      },
      "message": "type__s is cannot be updated by api",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — CreatingSupportOrSystemUser

Changing User to Support or System Type

```json
{
  "users": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "profile"
      },
      "message": "Support user cannot be added",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — UserLimitExceeded

User Limit Exceeded

```json
{
  "users": [
    {
      "code": "LICENSE_LIMIT_EXCEEDED",
      "details": {},
      "message": "You are trying to activate more mail addon which exceeds your license limit. If you want to activate mail addon for additional users, please upgrade your license",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicateEmailId

Duplicate Email Address in User Update

```json
{
  "users": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "email",
        "json_path": "$.users[0].email"
      },
      "message": "Email already exists",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InSufficientPrivilegesToUpdateUser

Insufficient Privileges to Update User

```json
{
  "users": [
    {
      "code": "AUTHORIZATION_FAILED",
      "details": {},
      "message": "Either trial is expired or user does not have sufficiet previlege to perform this action",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — UpdatingNonSubordinateUser

Updating a Non-Subordinate User

```json
{
  "users": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "id",
        "json_path": "$.users[0].id"
      },
      "message": "Non subordinate users cannot be updated",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — UpdatingClosedOrDeletedUser

Updating User in Closed or Deleted Organization

```json
{
  "users": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "id",
        "json_path": "$.users[0].id"
      },
      "message": "You can't perform this action over a closed/deleted user",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidReportingManager

Invalid Reporting Manager

```json
{
  "users": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.users[0].Reporting_To.id"
      },
      "message": "the reporting manager must be superior in reporting hierarchy",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidCurrenntShiftId

Invalid Current Shift ID

```json
{
  "users": [
    {
      "code": "INVALID_REQUEST",
      "details": {
        "api_name": "$current_shift",
        "json_path": "$.users[0].$current_shift.id"
      },
      "message": "Invalid current shift id",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidNextShiftId

Invalid Next Shift ID

```json
{
  "users": [
    {
      "code": "INVALID_REQUEST",
      "details": {
        "api_name": "$next_shift",
        "json_path": "$.users[0].$next_shift.id"
      },
      "message": "Invalid next shift id",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — SameCurrentAndNextShiftId

Current and Next Shift Cannot Be the Same

```json
{
  "users": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "$next_shift.id",
        "json_path": "$.users[0].$next_shift.id"
      },
      "message": "current shift and next shift should not be same",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ShiftEffectiveFromDateMissing

Missing Shift Effective From Date

```json
{
  "users": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "$next_shift",
          "json_path": "$.users[0].$next_shift"
        },
        "api_name": "$shift_effective_from",
        "json_path": "$.users[0].$shift_effective_from"
      },
      "message": "Dependent Field value should not be null",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidShiftEffectiveFromDate

Invalid Shift Effective From Date

```json
{
  "users": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "$shift_effective_from",
        "json_path": "$.users[0].$shift_effective_from"
      },
      "message": "current shift and next shift should not be same",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NextShiftWithDateWithMoretimePeriod

Shift Effective From Date Exceeds Maximum Period

```json
{
  "users": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "Maximum time period is six months to move shift",
        "api_name": "$shift_effective_from",
        "json_path": "$.users[0].$shift_effective_from"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `403` — `application/json` — NoPermissionToCreateUser

No Permission to Update User

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_Users"
    ]
  },
  "message": "permission denied",
  "status": "error"
}
```
