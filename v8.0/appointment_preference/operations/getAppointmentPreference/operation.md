# GET /settings/appointment_preferences
**Operation:** `getAppointmentPreference` — Get Appointment Preferences
> Fetches the existing configuration for appointment preferences, including rules for deal creation, job sheet visibility, and mark as complete configurations.

**Parameters:**
- `include` (query, string, optional) [enum=['deal_record_configuration']]: Specify this key to fetch deal record configuration when **when_appointment_completed:create_deal**.
Possible values: **deal_record_configuration**.


**Responses:**

- **200**: Contains the details of the requested resource.  [application/json]
    > Returns the appointment preferences configured for the Zoho CRM organization.
    - `appointment_preferences` (object) **REQ** — Represents the complete set of appointment preferences configured in the CRM organization. 
      - `show_job_sheet` (boolean) **REQ** — Represents whether filling out the job sheet is mandatory for marking an appointment as 'completed'.
Possible values:
**true** - Job sheet is mandatory for appointment completion.
**false** - Job sheet is not mandatory for appointment completion.

      - `when_duration_exceeds` (string) [enum=['mark_as_complete', 'ask_appointment_provider_to_complete']] — Represents who has to mark the appointment as 'Completed' when the service duration gets over.
Possible values:
**mark_as_complete** - The appointment is automatically marked as 'completed'.
**ask_appointment_provider_to_complete** - User has to manually mark the appointment as 'completed'.

      - `when_appointment_completed` (string) **REQ** [enum=['do_not_create_deal', 'create_deal']] — Represents whether a deal has to be created when an appointment is completed.
Possible values:
**create_deal** - Deal is created when any appointment is marked 'Completed'.
**do_not_create_deal** - Deal is not created when any appointment is marked 'Completed'.

      - `allow_booking_outside_service_availability` (boolean) **REQ** — Denotes if you can create appointments outside service availability.
Possible values:
**true** - You can create appointments outside service availability.
**false** - You can not create appointments outside service availability.

      - `allow_booking_outside_businesshours` (boolean) **REQ** — Denotes if you can create appointments outside business hours.
Possible values:
**true** - You can create appointments outside business hours.
**false** - You can not create appointments outside business hours.

      - `sharing_enabled` (boolean) — Indicates whether sharing of the associated record in appointments with the appointment owner is enabled.
      - `sharing_details` (object) — Details about the sharing configuration for appointment-associated records. When sharing is enabled, the record associated in the appointment field is shared with the appointment owner with the configured permission level.
        - `sharing_computation_status` (boolean) — Indicates whether the sharing computation is currently in progress or completed.
        - `permission` (string) [enum=['read_only', 'read_write', 'full_access']] — The permission level granted to the appointment owner for the associated record.
      - `deal_record_configuration` (object) **REQ** — Contains the field mappings and layout details for record configuration in Deals from the Appointments module.
        - `layout` (object) **REQ** — Represents the Deals module layout used when creating deal records after an appointment is completed. 
          - `name` (string) **REQ** [maxLen=255] — Represents the display name of the Deals module layout as shown in the Zoho CRM interface. 
          - `id` (string) [maxLen=64] — Represents the unique identifier of the Deals module layout.
        - `field_mappings` (array of object) [maxItems=100] **REQ** — Contains the field mappings that define how appointment and service data populates deal fields when Zoho CRM creates a deal automatically after the appointment completion.
          - `type` (string) **REQ** [enum=['static', 'merge_field']] — Indicates the type of field mapping applied to populate the deal field. 
Possible values:
**static** - A fixed value applies to the deal field regardless of appointment data.
**merge_field** - The field value maps from the appointment or service module data.

          - `value` (object) **REQ** — Represents the value assigned to the Deals module field during deal creation. 
            oneOf:
                type: string [maxLen=1000] — Represents a merge-field expression that maps data from the Appointments or Services module to the deal field.
                additionalProperties: any
          - `field` (object) **REQ** — Represents the Deals module field to which the appointment data is mapped. 
            - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the Deals module field. 
            - `id` (string) **REQ** [maxLen=20] — Represents the unique identifier of the Deals module field. 
        - `id` (string) **REQ** [maxLen=20] — Represents the unique identifier of the deal record configuration. 

**Scopes:** ZohoCRM.settings.modules.READ
