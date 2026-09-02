# PUT /settings/fiscal_year
**Operation:** `updateFiscalYear` — Update Fiscal Year Settings
> Updates the fiscal year configuration for the organization. Only administrators can update fiscal year settings.

**Schemas:**
`SurplusWeekNested`:
  oneOf:
      type: null — Clears any existing surplus week configuration for the custom fiscal year.
    - `SurplusWeekValue` — Represents the surplus week configuration values, including the quarter, period, and year in which the surplus week is placed.
`SurplusWeekValue`:
  > Represents the surplus week configuration values, including the quarter, period, and year in which the surplus week is placed.
  - `period` (integer/int32) **REQ** — Specify the fiscal period within the quarter that contains the surplus week.
  - `year` (integer/int32) **REQ** — Specify the year in which the surplus week is configured. You can configure this only for the current year and the following year.
  - `quarter` (integer/int32) **REQ** — Specify the fiscal quarter that contains the surplus week.

**Request Body** — application/json `PutfiscalyearRequest`
> The request body must contain a `fiscal_year` object with the settings to update. Specify a valid `start_month`, `display_based_on`, or both. fiscal_year JSON Object, mandatory To update the fiscal year settings you must specify a valid start_month or display_based_on value or both inside this JSON object. start_month string, optional Represents the start month of the year and the allowed values are valid month names (eg: January, February) display_based_on string, optional This value represents whether the name of the fiscal year is based on starting month or ending month of the fiscal period. For example, assume your fiscal year start in April 2023 and ends in March 2024. If you choose to name the year based on the start month (April) the fiscal year will be 2023; If you choose to name the year based on the end month (April) the fiscal year will be 2024
  > Represents the request body for updating the fiscal year settings of the Zoho CRM organization.
  - `fiscal_year` (object `FiscalYearNested`) **REQ** — Root key of the API (Required)
    oneOf:
      - `DisplayBasedOnFiscalYearUpdate` — Represents a request to update only the fiscal year display option for an existing standard or custom fiscal year.
        - `display_based_on` (string) **REQ** [maxLen=20, enum=['start_month', 'end_month']] — Specify whether the fiscal year label is based on the start month or the end month of the fiscal period. Possible values: `start_month`, `end_month`.
      - `StandardFiscalYearUpdate` — Represents the request payload to update standard fiscal year settings. When `display_based_on` is set to `end_month`, the `start_month` cannot be `JANUARY`.
        - `start_month` (string) **REQ** [maxLen=20, enum=[12 values]] — Specify the start month of the fiscal year. Possible values: `JANUARY`, `FEBRUARY`, `MARCH`, `APRIL`, `MAY`, `JUNE`, `JULY`, `AUGUST`, `SEPTEMBER`, `OCTOBER`, `NOVEMBER`, `DECEMBER`.
        - `display_based_on` (string) [maxLen=20, enum=['start_month', 'end_month']] — Specify whether the fiscal year label is based on the start month or the end month of the fiscal period. When set to `end_month`, the `start_month` cannot be `JANUARY`. Possible values: `start_month`, `end_month`.
      - `SwitchToStandardFiscalYearUpdate` — Represents the request payload to switch the organization from a custom fiscal year to a standard fiscal year.
        - `calendar_type` (string) **REQ** [maxLen=10, enum=['gregorian']] — Specify the calendar type used to switch to a standard fiscal year. Possible values: `gregorian`.
        - `start_month` (string) [maxLen=20, enum=[12 values]] — Specify the start month of the fiscal year. Possible values: `JANUARY`, `FEBRUARY`, `MARCH`, `APRIL`, `MAY`, `JUNE`, `JULY`, `AUGUST`, `SEPTEMBER`, `OCTOBER`, `NOVEMBER`, `DECEMBER`.
        - `display_based_on` (string) [maxLen=20, enum=['start_month', 'end_month']] — Specify whether the fiscal year label is based on the start month or the end month of the fiscal period. When set to `end_month`, the `start_month` cannot be `JANUARY`. Possible values: `start_month`, `end_month`.
      - `SwitchToCustomFiscalYearUpdate` — Represents the request payload to switch the organization from a standard fiscal year to a custom fiscal year. When `start_month` is provided alongside `start_date`, its value must match the month component of `start_date`.
        - `calendar_type` (string) **REQ** [maxLen=10, enum=['custom']] — Specify the calendar type used to switch to a custom fiscal year. Possible values: `custom`.
        - `display_based_on` (string) [maxLen=20, enum=['start_month', 'end_month']] — Specify whether the custom fiscal year label is based on the start month or the end month of the fiscal period. When set to `end_month`, the `start_date` cannot fall in January or February. Possible values: `start_month`, `end_month`.
        - `surplus_week` (object `SurplusWeekNested`) — Specify the surplus week configuration for the custom fiscal year. Send `null` to clear the configured surplus week.
        - `interval_display_option` (string) **REQ** [maxLen=7, enum=['year', 'quarter']] — Specify the display format for the custom fiscal year intervals. Possible values: `year`, `quarter`.
        - `structure` (string) **REQ** [maxLen=10, enum=['4-4-5', '4-5-4', '5-4-4', '3-3-3-4', '3-3-4-3', '3-4-3-3', '4-3-3-3']] — Specify the week distribution structure for the custom fiscal year. Possible values: `4-4-5`, `4-5-4`, `5-4-4`, `3-3-3-4`, `3-3-4-3`, `3-4-3-3`, `4-3-3-3`.
        - `start_date` (string/date) **REQ** [maxLen=10] — Specify the start date of the custom fiscal year. This field can be configured only for the current year.
        - `start_month` (string) [maxLen=20, enum=[12 values]] — Specify the start month of the fiscal year. This field is optional. When provided, its value must match the month component of the configured start_date.
      - `CustomFiscalYearPartialUpdate` — Represents the request payload to update selected settings of an existing custom fiscal year. When `start_month` is provided alongside `start_date`, its value must match the month component of `start_date`.
        - `display_based_on` (string) [maxLen=20, enum=['start_month', 'end_month']] — Specify whether the custom fiscal year label is based on the start month or the end month of the fiscal period. When set to `end_month`, the `start_date` cannot fall in January or February. Possible values: `start_month`, `end_month`.
        - `surplus_week` (object) — Specify the surplus week configuration for the custom fiscal year. Send `null` to clear the configured surplus week.
        - `interval_display_option` (string) [maxLen=7, enum=['year', 'quarter']] — Specify the display format for the custom fiscal year intervals. Possible values: `year`, `quarter`.
        - `structure` (string) [maxLen=10, enum=['4-4-5', '4-5-4', '5-4-4', '3-3-3-4', '3-3-4-3', '3-4-3-3', '4-3-3-3']] — Specify the week distribution structure for the custom fiscal year. Possible values: `4-4-5`, `4-5-4`, `5-4-4`, `3-3-3-4`, `3-3-4-3`, `3-4-3-3`, `4-3-3-3`.
        - `start_date` (string/date) [maxLen=10] — Specify the start date of the custom fiscal year. This field can be configured only for the current year.
        - `start_month` (string) [maxLen=20, enum=[12 values]] — Specify the start month of the fiscal year. This field is optional. When provided, its value must match the month component of the configured start_date.
        anyOf:

**Responses:**

- **200**: Returns the status and details of the updated fiscal year settings. — Schema: `UpdateFiscalYearResponse` [application/json]
    > Represents the response body for a successful fiscal year settings update.
    schema: `UpdateFiscalYearResponse`
    - `fiscal_year` (object `FiscalYearNested1`) **REQ** — Represents the response body for a successful fiscal year settings update, including the status code, message, and updated record details.
      schema: `FiscalYearNested1`
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the status code of the operation. Possible values: `SUCCESS`.
      - `details` (object `DetailsNested`) **REQ** — Represents the details of the updated fiscal year configuration, including its unique identifier.
        schema: `DetailsNested`
        - `id` (string/int64) **REQ** [maxLen=255] — Represents the unique identifier of the updated fiscal year configuration.
      - `message` (string) **REQ** [maxLen=255] — Represents the status message of the operation.
      - `status` (string) **REQ** [enum=['success']] — Represents the status of the response. Possible values: `success`.

- **400**: The fiscal year settings update request failed due to invalid field values or an unsupported configuration. [application/json]
    > Represents a wrapped fiscal year error response containing the validation error details.
    - `fiscal_year` (object) **REQ**
      oneOf:
        - `FiscalInvalidStartDateError` — Represents the error returned when the start_date field value is invalid.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code. Possible values: `INVALID_DATA`.
          - `details` (object) **REQ** — Represents the error details with information about the field that caused the validation failure.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the validation failure.
            - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the validation failure.
          - `message` (string) **REQ** [enum=['Please give a valid start_date']] — Represents the error message. Possible values: `Please give a valid start_date`.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: `error`.
        - `FiscalInvalidCalendarTypeError` — Represents the error returned when the calendar_type value is invalid — either because it contains non-alphabetic characters (returns expected_data_type) or because it is not one of the supported values (returns supported_values).
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code. Possible values: `INVALID_DATA`.
          - `details` (object) **REQ** — Represents the error details. Contains either `expected_data_type` when the value has non-alphabetic characters, or `supported_values` when the value is not one of the allowed calendar types.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the validation failure.
            - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the validation failure.
            - `supported_values` (array of string) [maxItems=25] — Represents the list of supported calendar type values. Present when the value is alphabetic but not a recognized calendar type.
              items: [maxLen=255]
            - `expected_data_type` (string) [enum=['text']] — Represents the expected data type for the field. Present when the value contains non-alphabetic characters. Possible values: `text`.
          - `message` (string) **REQ** [enum=['Please give a valid calendar type']] — Represents the error message. Possible values: `Please give a valid calendar type`.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: `error`.
        - `FiscalInvalidStructureError` — Represents the error returned when the structure field value is not one of the supported patterns.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code. Possible values: `INVALID_DATA`.
          - `details` (object) **REQ** — Represents the error details with information about the field that caused the validation failure.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the validation failure.
            - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the validation failure.
            - `supported_values` (array of string) [maxItems=25] **REQ** — Represents the list of supported values for the invalid field.
              items: [maxLen=255]
          - `message` (string) **REQ** [enum=['Please give a valid structure']] — Represents the error message. Possible values: `Please give a valid structure`.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: `error`.
        - `FiscalInvalidStartDateMonthError` — Represents the error returned when the start_date value does not match the month component of the configured start_month.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code. Possible values: `INVALID_DATA`.
          - `details` (object) **REQ** — Represents the error details with information about the field that caused the validation failure.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the validation failure.
            - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the validation failure.
          - `message` (string) **REQ** [enum=['start_date does not match with start_month']] — Represents the error message. Possible values: `start_date does not match with start_month`.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: `error`.
        - `FiscalInvalidMonthError` — Represents the error returned when the start_month value is not a valid month name.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code. Possible values: `INVALID_DATA`.
          - `details` (object) **REQ** — Represents the error details with information about the field that caused the validation failure.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the validation failure.
            - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the validation failure.
            - `supported_values` (array of string) [maxItems=25] **REQ** — Represents the list of supported values for the invalid field.
              items: [maxLen=255]
          - `message` (string) **REQ** [enum=['Please give a valid month']] — Represents the error message. Possible values: `Please give a valid month`.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: `error`.
        - `FiscalInvalidDisplayBasedOnError` — Represents the error returned when the display_based_on field value is invalid.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code. Possible values: `INVALID_DATA`.
          - `details` (object) **REQ** — Represents the error details with information about the field that caused the validation failure.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the validation failure.
            - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the validation failure.
            - `supported_values` (array of string) [maxItems=25] **REQ** — Represents the list of supported values for the invalid field.
              items: [maxLen=255]
          - `message` (string) **REQ** [enum=['Please give a valid display based on']] — Represents the error message. Possible values: `Please give a valid display based on`.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: `error`.
        - `FiscalInvalidIntervalDisplayOptionError` — Represents the error returned when the interval_display_option field value is invalid.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code. Possible values: `INVALID_DATA`.
          - `details` (object) **REQ** — Represents the error details with information about the field that caused the validation failure.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the validation failure.
            - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the validation failure.
            - `supported_values` (array of string) [maxItems=25] **REQ** — Represents the list of supported values for the invalid field.
              items: [maxLen=255]
          - `message` (string) **REQ** [enum=['Please give a valid number_by display option']] — Represents the error message. Possible values: `Please give a valid number_by display option`.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: `error`.
        - `FiscalInvalidEndMonthConfigError` — Represents the error returned when end_month is configured as the display option for a custom calendar type with a start date in January or February.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code. Possible values: `INVALID_DATA`.
          - `details` (object) **REQ** — Represents the error details with information about the field that caused the validation failure.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the validation failure.
            - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the validation failure.
          - `message` (string) **REQ** [enum=[1 values]] — Represents the error message. Possible values: `Cannot configure end month as display based option for January and February for custom calendar type`.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: `error`.
        - `FiscalInvalidStartYearError` — Represents the error returned when the start_date is set to a year other than the current year for a custom fiscal year.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code. Possible values: `INVALID_DATA`.
          - `details` (object) **REQ** — Represents the error details with information about the field that caused the validation failure.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the validation failure.
            - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the validation failure.
          - `message` (string) **REQ** [enum=['custom fiscal year can be configured only with current year']] — Represents the error message. Possible values: `custom fiscal year can be configured only with current year`.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: `error`.
        - `FiscalInvalidSurpluYearError` — Represents the error returned when the surplus week is configured for a year outside the current year or the following year.
          - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code. Possible values: `NOT_ALLOWED`.
          - `details` (object) **REQ** — Represents the error details with information about the field that caused the validation failure.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the validation failure.
            - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the validation failure.
            - `supported_values` (array of integer/int32) [maxItems=25] **REQ** — Represents the list of supported values for the invalid field.
          - `message` (string) **REQ** [enum=['Surplus week can be updated only for current year and next year']] — Represents the error message. Possible values: `Surplus week can be updated only for current year and next year`.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: `error`.
        - `FiscalCompletedSurplusError` — Represents the error returned when attempting to update the surplus week for a fiscal year that has already been completed.
          - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code. Possible values: `NOT_ALLOWED`.
          - `details` (object) **REQ** — Represents the error details with information about the field that caused the validation failure.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the validation failure.
            - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the validation failure.
          - `message` (string) **REQ** [enum=['Cannot edit surplus week for completed fiscal year']] — Represents the error message. Possible values: `Cannot edit surplus week for completed fiscal year`.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: `error`.
        - `AmbiguityError` — Represents the error returned when conflicting fields are sent in the same request — specifically when calendar_type is set to gregorian while also providing fields that are only valid for a custom calendar, such as structure, start_date, interval_display_option, or surplus_week.
          - `code` (string) **REQ** [enum=['AMBIGUITY_DURING_PROCESSING']] — Represents the error code. Possible values: `AMBIGUITY_DURING_PROCESSING`.
          - `details` (object) **REQ** — Represents the error details containing the fields that caused the ambiguity.
            - `ambiguity_due_to` (array of object) [maxItems=2] **REQ** — Represents the list of fields that caused the ambiguity during processing.
              - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the ambiguity.
              - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the ambiguity.
          - `message` (string) **REQ** [enum=['Ambiguity while processing']] — Represents the error message. Possible values: `Ambiguity while processing`.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: `error`.
        - `FiscalSurplusWeekYearMissingError` — Represents the error returned when the year field is missing from the surplus_week object.
          - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Represents the error code. Possible values: `DEPENDENT_FIELD_MISSING`.
          - `details` (object) **REQ** — Represents the error details identifying the missing year field and the surplus_week object it belongs to.
            - `dependee` (object) **REQ** — Represents the parent surplus_week field that requires the year to be present.
              - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the parent field.
              - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the parent field.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the missing year field.
            - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the missing year field.
          - `message` (string) **REQ** [enum=['Provide valid year for surplus week']] — Represents the error message. Possible values: `Provide valid year for surplus week`.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: `error`.
        - `FiscalSurplusWeekQuarterMissingError` — Represents the error returned when the quarter field is missing from the surplus_week object.
          - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Represents the error code. Possible values: `DEPENDENT_FIELD_MISSING`.
          - `details` (object) **REQ** — Represents the error details identifying the missing quarter field and the surplus_week object it belongs to.
            - `dependee` (object) **REQ** — Represents the parent surplus_week field that requires the quarter to be present.
              - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the parent field.
              - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the parent field.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the missing quarter field.
            - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the missing quarter field.
          - `message` (string) **REQ** [enum=['Provide valid quarter for surplus week']] — Represents the error message. Possible values: `Provide valid quarter for surplus week`.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: `error`.
        - `FiscalSurplusWeekPeriodMissingError` — Represents the error returned when the period field is missing from the surplus_week object.
          - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Represents the error code. Possible values: `DEPENDENT_FIELD_MISSING`.
          - `details` (object) **REQ** — Represents the error details identifying the missing period field and the surplus_week object it belongs to.
            - `dependee` (object) **REQ** — Represents the parent surplus_week field that requires the period to be present.
              - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the parent field.
              - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the parent field.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the missing period field.
            - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the missing period field.
          - `message` (string) **REQ** [enum=['Provide valid period for surplus week']] — Represents the error message. Possible values: `Provide valid period for surplus week`.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: `error`.
        - `DependentFieldMissingError` — Represents the error returned when a required dependent field is missing from the request.
          - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Represents the error code. Possible values: `DEPENDENT_FIELD_MISSING`.
          - `details` (object) **REQ** — Represents the error details identifying the missing field and the field it depends on.
            - `dependee` (object) **REQ** — Represents the dependent field that is required to be present in the request.
              - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the required dependent field.
              - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the required dependent field.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that requires a dependent field.
            - `json_path` (string) **REQ** [maxLen=1024] — Represents the JSON path of the field that requires a dependent field.
          - `message` (string) **REQ** [enum=['Dependent field missing']] — Represents the error message. Possible values: `Dependent field missing`.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: `error`.
        - `FiscalStructureNotAllowedForGregorianError` — Represents the error returned when structure is provided in the request while the calendar type is gregorian.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code. Possible values: `INVALID_DATA`.
          - `details` (object) **REQ** — Represents the error details with information about the field that caused the validation failure.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the validation failure.
            - `json_path` (string) **REQ** [maxLen=1024] — Represents the JSON path of the field that caused the validation failure.
          - `message` (string) **REQ** [enum=['cannot configure structure for gregorian calendar']] — Represents the error message. Possible values: `cannot configure structure for gregorian calendar`.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: `error`.
        - `FiscalIntervalDisplayOptionNotAllowedForGregorianError` — Represents the error returned when interval_display_option is provided in the request while the calendar type is gregorian.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code. Possible values: `INVALID_DATA`.
          - `details` (object) **REQ** — Represents the error details with information about the field that caused the validation failure.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the validation failure.
            - `json_path` (string) **REQ** [maxLen=1024] — Represents the JSON path of the field that caused the validation failure.
          - `message` (string) **REQ** [enum=['cannot configure interval_display_option for gregorian calendar']] — Represents the error message. Possible values: `cannot configure interval_display_option for gregorian calendar`.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: `error`.
        - `FiscalSurplusWeekNotAllowedForGregorianError` — Represents the error returned when surplus_week is provided in the request while the calendar type is gregorian.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code. Possible values: `INVALID_DATA`.
          - `details` (object) **REQ** — Represents the error details with information about the field that caused the validation failure.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the validation failure.
            - `json_path` (string) **REQ** [maxLen=1024] — Represents the JSON path of the field that caused the validation failure.
          - `message` (string) **REQ** [enum=['cannot configure surplus week for gregorian calendar']] — Represents the error message. Possible values: `cannot configure surplus week for gregorian calendar`.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: `error`.
        - `FiscalStartDateNotAllowedForGregorianError` — Represents the error returned when start_date is provided in the request while the calendar type is gregorian.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code. Possible values: `INVALID_DATA`.
          - `details` (object) **REQ** — Represents the error details with information about the field that caused the validation failure.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the validation failure.
            - `json_path` (string) **REQ** [maxLen=1024] — Represents the JSON path of the field that caused the validation failure.
          - `message` (string) **REQ** [enum=['cannot configure start_date for gregorian calendar']] — Represents the error message. Possible values: `cannot configure start_date for gregorian calendar`.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: `error`.
        - `FiscalInvalidStartMonthForConfiguredDateError` — Represents the error returned when the start_month value does not match the month of the existing start_date configured for the custom fiscal year.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code. Possible values: `INVALID_DATA`.
          - `details` (object) **REQ** — Represents the error details with information about the field that caused the validation failure.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the validation failure.
            - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the validation failure.
          - `message` (string) **REQ** [enum=['Invalid start_month for the start_date configured']] — Represents the error message. Possible values: `Invalid start_month for the start_date configured`.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: `error`.
        - `FiscalDeleteCompletedSurplusError` — Represents the error returned when attempting to delete the surplus week for a fiscal year that has already been completed.
          - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code. Possible values: `NOT_ALLOWED`.
          - `details` (object) **REQ** — Represents the error details with information about the field that caused the validation failure.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the validation failure.
            - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the validation failure.
          - `message` (string) **REQ** [enum=['Cannot delete surplus week for completed fiscal year']] — Represents the error message. Possible values: `Cannot delete surplus week for completed fiscal year`.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: `error`.
        - `FiscalInvalidSurplusWeekQuarterValueError` — Represents the error returned when the quarter value in the surplus_week object is not in the allowed range of 1 to 4.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code. Possible values: `INVALID_DATA`.
          - `details` (object) **REQ** — Represents the error details with the JSON path and the list of supported quarter values.
            - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the validation failure.
            - `supported_values` (array of integer/int32) [maxItems=4] **REQ** — Represents the list of supported values for the quarter field.
          - `message` (string) **REQ** [enum=['Provide valid quarter for surplus week']] — Represents the error message. Possible values: `Provide valid quarter for surplus week`.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: `error`.
        - `FiscalInvalidSurplusWeekPeriodValueError` — Represents the error returned when the period value in the surplus_week object exceeds the maximum allowed period for the configured quarter.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code. Possible values: `INVALID_DATA`.
          - `details` (object) **REQ** — Represents the error details with the JSON path and the list of supported period values for the configured quarter.
            - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the validation failure.
            - `supported_values` (array of integer/int32) [maxItems=4] **REQ** — Represents the list of supported period values for the configured quarter.
          - `message` (string) **REQ** [enum=['Provide valid period for surplus week']] — Represents the error message. Possible values: `Provide valid period for surplus week`.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: `error`.
        - `FiscalInvalidDataError` — Represents the error returned when the request body does not contain any valid fiscal year field to update.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code. Possible values: `INVALID_DATA`.
          - `details` (object) **REQ** — Represents an empty details object returned with the error.
          - `message` (string) **REQ** [enum=['Please give a valid data']] — Represents the error message. Possible values: `Please give a valid data`.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: `error`.

- **401**: The request failed because the OAuth access token is missing, invalid, or does not include the required scope. [application/json]
    > Contains one of the possible authentication error responses returned when the fiscal year settings cannot be updated.
    oneOf:
      - `OAuthScopeMismatchError` — Represents the error returned when the OAuth access token does not include the required scope to access this endpoint.
        - `code` (string) **REQ** [enum=['OAUTH_SCOPE_MISMATCH']] — Represents the error code. Possible values: `OAUTH_SCOPE_MISMATCH`.
        - `details` (object) **REQ** — Represents an empty details object returned with the error.
        - `message` (string) **REQ** [enum=['invalid oauth scope to access this URL']] — Represents the error message. Possible values: `invalid oauth scope to access this URL`.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: `error`.
      - `AuthenticationFailureError` — Represents the error returned when the OAuth access token is missing or invalid.
        - `code` (string) **REQ** [enum=['AUTHENTICATION_FAILURE']] — Represents the error code. Possible values: `AUTHENTICATION_FAILURE`.
        - `details` (object) **REQ** — Represents an empty details object returned with the error.
        - `message` (string) **REQ** [enum=['Authentication failed']] — Represents the error message. Possible values: `Authentication failed`.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: `error`.

- **403**: The request failed because the authenticated user does not have administrator privileges to update the fiscal year settings [application/json]
    > Contains the forbidden error response returned when the fiscal year settings cannot be updated due to insufficient permissions.
    schema: `FiscalNoPermissionError`
    - `fiscal_year` (object) **REQ** — Represents the wrapped error response returned when the user does not have permission to update the fiscal year settings.
      - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code. Possible values: `NO_PERMISSION`.
      - `details` (object) **REQ** — Represents an empty details object returned with the error.
      - `message` (string) **REQ** [enum=['Only Admin Users can modify the fiscal year settings']] — Represents the error message. Possible values: `Only Admin Users can modify the fiscal year settings`.
      - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: `error`.

**Scopes:** ZohoCRM.settings.fiscal_year.UPDATE
