# Examples: updateAppointmentById

**PUT /Appointments__s/{appointmentId}**

## Request examples

### `application/json` — SamplePutRequest

PUT request body with a data array for a single appointment record update

```json
{
  "data": [
    {
      "Appointment_Name": "service06 - ll",
      "Appointment_For": {
        "module": {
          "api_name": "Contacts",
          "id": "111115000000002654"
        },
        "name": "ll",
        "id": "111115000000120725"
      },
      "Service_Name": {
        "name": "service06",
        "id": "111115000000127506"
      },
      "Appointment_Start_Time": "2026-01-16T18:00:00+05:30",
      "Location": "Business Address",
      "Address": null,
      "Owner": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "Additional_Information": null,
      "Remind_At": [
        {
          "unit": 1,
          "period": "hours"
        }
      ],
      "Created_By": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "Modified_By": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "Created_Time": "2026-01-16T16:50:29+05:30",
      "Modified_Time": "2026-01-19T16:12:24+05:30",
      "Tag": [],
      "Status": "Overdue",
      "Last_Activity_Time": "2026-01-19T16:12:24+05:30",
      "Rescheduled_From": null,
      "Reschedule_Reason": null,
      "Reschedule_Note": null,
      "Rescheduled_By": null,
      "Rescheduled_Time": null,
      "Cancelled_By": null,
      "Cancellation_Reason": null,
      "Cancellation_Note": null,
      "Job_Sheet_Created__s": false,
      "Cancelled_Time": null,
      "Job_Sheet_Name__s": null,
      "Job_Sheet_Description__s": null,
      "Date_1": null,
      "Reschedule_Count": 0,
      "Appointment_End_Time": "2026-01-16T18:30:00+05:30",
      "Duration": 30,
      "Rescheduled_To": null
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — Success200

Successful update of a single appointment record.

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "Modified_Time": "2026-01-19T18:42:32+05:30",
        "Modified_By": {
          "name": "madesh04",
          "id": "111115000000058229"
        },
        "Created_Time": "2026-01-16T13:07:30+05:30",
        "id": "111115000000147181",
        "Created_By": {
          "name": "madesh04",
          "id": "111115000000058229"
        }
      },
      "message": "record updated",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse1

**MANDATORY_NOT_FOUND** error when required **Appointment_For** field is absent.

```json
{
  "data": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "Appointment_For",
        "json_path": "$.data[2].Appointment_For"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldUnchangedResponse1

DEPENDENT_FIELD_UNCHANGED error when reschedule time matches existing Appointment_Start_Time.

```json
{
  "data": [
    {
      "code": "DEPENDENT_FIELD_UNCHANGED",
      "details": {
        "dependee": {
          "api_name": "Appointment_Start_Time",
          "json_path": "$.data[0].Appointment_Start_Time"
        },
        "api_name": "Rescheduled_From",
        "json_path": "$.data[0].Rescheduled_From"
      },
      "message": "Reschedule_From and Appointment_Start_Time cannot be same",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse1

DEPENDENT_FIELD_MISSING error when Appointment_Start_Time is absent during reschedule.

```json
{
  "data": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "Reschedule_Reason",
          "json_path": "$.data[0].Reschedule_Reason"
        },
        "api_name": "Rescheduled_From",
        "json_path": "$.data[0].Rescheduled_From"
      },
      "message": "Rescheduled_From cannot be empty",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NotAllowedResponse1

**NOT_ALLOWED** error when the service is unavailable at the given **Appointment_Start_Time**.

```json
{
  "data": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "Appointment_Start_Time",
        "json_path": "$.data[0].Appointment_Start_Time"
      },
      "message": "Service is not available on the given time",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NotAllowedResponse2

**NOT_ALLOWED** error when **Appointment_Start_Time** falls outside configured business hours.

```json
{
  "data": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "Appointment_Start_Time",
        "json_path": "$.data[0].Appointment_Start_Time"
      },
      "message": "Appointment time does not falls under business hours",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse1

**DEPENDENT_MISMATCH** error when appointment **Owner** is not a **Service_Name** member.

```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Services.Members",
          "json_path": "$.data[0].Services.Members"
        },
        "api_name": "id",
        "json_path": "$.data[0].Owner.id"
      },
      "message": "Appointment Owner is not a part of Service Members",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse1

**INVALID_DATA** error  when the  **Appointment_For.module** value is not a valid JSON object.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "jsonobject",
        "api_name": "module",
        "json_path": "$.data[0].Appointment_For.module"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse2

**INVALID_DATA** error is thrown when  **api_name** in **Appointment_For.module** not found in multi-module lookup.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "api_name",
        "json_path": "$.data[0].Appointment_For.module.api_name"
      },
      "message": "the given module name is not exist in multimodulelookup",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse2

DEPENDENT_FIELD_MISSING error when Status is not Cancelled but cancellation fields are set.

```json
{
  "data": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "Cancellation_Reason",
          "json_path": "$.data[0].Cancellation_Reason"
        },
        "api_name": "Status",
        "json_path": "$.data[0].Status"
      },
      "message": "To Update the fields of Cancellation Information Section, value of Status should be Cancelled",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NotAllowedResponse3

**NOT_ALLOWED** error when completing an appointment without a job sheet.

```json
{
  "data": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "Status",
        "json_path": "$.data[0].Status"
      },
      "message": "Appointment cannot be marked as completed without creating the jobsheet",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse2

**DEPENDENT_MISMATCH** error when **Status** set to Completed before appointment ends.

```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Appointment_Start_Time",
          "json_path": "$.data[0].Appointment_Start_Time"
        },
        "api_name": "Status",
        "json_path": "$.data[0].Status"
      },
      "message": "Appointment cannot be marked as completed before the appointment ends",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse3

**DEPENDENT_MISMATCH** error when **Job_Sheet_Name__s** set on a non-completed appointment.

```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Status",
          "json_path": "$.data[0].Status"
        },
        "api_name": "Job_Sheet_Name__s",
        "json_path": "$.data[0].Job_Sheet_Name__s"
      },
      "message": "Job Sheet can be created only for completed appointment",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse4

**DEPENDENT_MISMATCH** error when **Status** set to Overdue before appointment ends.

```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Appointment_Start_Time",
          "json_path": "$.data[0].Appointment_Start_Time"
        },
        "api_name": "Status",
        "json_path": "$.data[0].Status"
      },
      "message": "Appointment cannot be marked as overdue before the appointment ends",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse5

**DEPENDENT_MISMATCH** error when **Status** set to Scheduled with a past **Appointment_Start_Time**

```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Appointment_Start_Time",
          "json_path": "$.data[0].Appointment_Start_Time"
        },
        "api_name": "Status",
        "json_path": "$.data[0].Status"
      },
      "message": "Appointment cannot be scheduled for past dates",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse2

**MANDATORY_NOT_FOUND** error when the **unit** key is missing from a **Remind_At** object.

```json
{
  "data": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "unit",
        "json_path": "$.data[0].Remind_At[0].unit"
      },
      "message": "mandatory key missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse3

**INVALID_DATA** error is thrown when the  **appointmentId** path parameter does not match a valid appointment record.

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

### Status `400` — `application/json` — InvalidDataResponse4

**INVALID_DATA** error  when the **Status** field value fails validation.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "Status",
        "json_path": "$.data[0].Status"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse5

**INVALID_DATA** error when **unit** field in **Remind_At** receives a non-integer value.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "integer",
        "api_name": "unit",
        "json_path": "$.data[0].Remind_At[0].unit"
      },
      "message": "INVALID_DATA",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — RecordLockedResponse1

**RECORD_LOCKED** error when the appointment record is locked and cannot be modified.

```json
{
  "data": [
    {
      "code": "RECORD_LOCKED",
      "details": {
        "api_name": "id",
        "action": "record_locking",
        "json_path": "$.data[0].id"
      },
      "message": "Sorry, you cannot perform this operation as the record is locked.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataMaxLengthResponse1

**INVALID_DATA** error when maximum length exceeded for the **data** field.

```json
{
  "code": "INVALID_DATA",
  "details": {
    "maximum_length": 1,
    "api_name": "data",
    "json_path": "$.data"
  },
  "message": "invalid data",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermissionCompleteResponse1

**NO_PERMISSION** error when the caller lacks permission to complete the appointment.

```json
{
  "data": [
    {
      "code": "NO_PERMISSION",
      "details": {
        "permissions": [
          "Crm_Implied_Mark_As_Complete_Appointments"
        ]
      },
      "message": "permission denied",
      "status": "error"
    }
  ]
}
```

### Status `403` — `application/json` — NoPermissionRescheduleResponse1

**NO_PERMISSION** error when the caller lacks permission to reschedule the appointment.

```json
{
  "data": [
    {
      "code": "NO_PERMISSION",
      "details": {
        "permissions": [
          "Crm_Implied_Reschedule_Appointments"
        ]
      },
      "message": "permission denied",
      "status": "error"
    }
  ]
}
```

### Status `403` — `application/json` — NoPermissionCancelResponse1

**NO_PERMISSION** error when the caller lacks permission to cancel the appointment.

```json
{
  "data": [
    {
      "code": "NO_PERMISSION",
      "details": {
        "permissions": [
          "Crm_Implied_Cancel_Appointments"
        ]
      },
      "message": "permission denied",
      "status": "error"
    }
  ]
}
```

### Status `403` — `application/json` — NoPermissionFlatResponse1

**NO_PERMISSION** error when the appointment record is not accessible to the caller.

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "resource_path_index": 1
  },
  "message": "record not accessible",
  "status": "error"
}
```
