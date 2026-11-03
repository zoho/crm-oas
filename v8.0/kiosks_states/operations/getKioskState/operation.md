# GET /settings/kiosks/{kioskId}/states/{stateId}
**Operation:** `getKioskState` — Get a specific kiosk state by ID
> To retrieve the complete configuration of one specific state within a kiosk in Zoho CRM, including its transitions, associated fields, and configured properties. Use the include_inner_details query parameter to expand nested type information. The response structure varies based on the state type: screen, decision, action, or get_records.

To obtain the state ID required for this request, use the [Get Kiosk States API](kiosks_states.yaml#$.paths./settings/kiosks/{kioskId}/states.get)

To obtain the Kiosk ID required for this request, use the [Get Kiosks API](kiosks.yaml#$.paths./settings/kiosks.get)


**Parameters:**
- `include_inner_details` (query, string, optional) [enum=['details.type']]: Specify to include additional inner details in the GET response for the kiosk state.
- `include` (query, string, optional) [enum=['configured_properties']]: Specify additional properties to be included in the response for each Kiosk state. By default, the response returns only the basic metadata of each state which includes each state's id, name, and associated_fields.

**Possible values:**

**configured_properties** - Includes the configured_properties key in the response for each state, which holds the list of merge fields and other dynamic references that have been configured within that state. When a state has no such configured properties, the value is returned as null.

- `kioskId` (path, string, required) [maxLen=255]: Specify the unique identifier of the Kiosk.
- `stateId` (path, string, required) [maxLen=255]: Specify the unique identifier of the kiosk state.

**Schemas:**
`BetweenFilterCriterionResponse`:
  > Represents the response for a filter criterion using the between and not_between comparators. The value is an array of exactly two elements — [lower_bound, upper_bound]. The value type is determined by the field's data_type: SimpleFilterCriterionValueString for date or datetime fields, and SimpleFilterCriterionValueNumber for integer, currency, or double fields.
  - `field` (object) **REQ** — Represents the target field definition to which the range filter criterion was applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['between', 'not_between']] — Represents the range comparison operator returned for the criterion, indicating whether the field value falls within or outside the specified bounds.
Possible values:
between - Matches records where the field value falls within the specified range.
not_between - Matches records where the field value falls outside the specified range.
  - `value` (array of object) [minItems=2, maxItems=2] **REQ** — Contains the two boundary values — [lower_bound, upper_bound] — against which the field was evaluated for the between or not_between comparator.
    oneOf:
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
  - `$disrupted` (boolean) — Indicates whether the between filter criterion is in a disrupted state, typically due to an invalid or unresolvable field or value reference.
`EqualFilterCriterionResponse`:
  > Represents the response for a filter criterion using the equal comparator. The value type is determined by the field's data_type: SimpleFilterCriterionValueString for text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime; SimpleFilterCriterionValueNumber for integer, currency, or double; SimpleFilterCriterionValueBoolean for Boolean; SimpleFilterCriterionValueObjectResponse for lookup, ownerlookup, or userlookup; and SimpleFilterCriterionValueObjectPredefined for predefined user or role object placeholders.
  - `field` (object) **REQ** — Represents the target field definition to which the equal filter criterion was applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['equal']] — Represents the equal comparison operator returned for the criterion.
Possible values:
equal - Matches records where the field value equals the specified filter value.
  - `value` (object) **REQ** — Represents the filter value returned for the equal comparator. Contains a scalar or an array of values, depending on the field's data_type.
    anyOf:
        type: array of object [minItems=1, maxItems=500]
          oneOf:
            - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
            - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
              anyOf:
                - `SimpleFilterCriterionValueObjectResponse` — Represents a lookup object filter criterion value for response bodies, applicable when the field's data_type is lookup, ownerlookup, or userlookup. Both the ID and name properties are included.
                - `SimpleFilterCriterionValueObjectPredefined` — Represents a predefined placeholder object filter criterion value for lookup fields, applicable with equal or not_equal comparators when the field's data_type is ownerlookup or userlookup. Two forms are supported: (1) the currently logged-in user, represented by passing only the name property with the predefined value ${CURRENTUSER} and no ID property; and (2) the logged-in user's role, represented by passing the ID property with the predefined value ${CURRENTUSERROLE} and an optional display label in the name property. For specific real users or roles that are not predefined, use SimpleFilterCriterionValueObjectRequest, which requires the ID property.
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
      - `SimpleFilterCriterionValueBoolean` (boolean) — Represents a Boolean filter criterion value. Applicable only when the field has a Boolean data type (checkbox field).
      - `SimpleFilterCriterionValueObjectResponse` — Represents a lookup object filter criterion value for response bodies, applicable when the field's data_type is lookup, ownerlookup, or userlookup. Both the ID and name properties are included.
      - `SimpleFilterCriterionValueObjectPredefined` — Represents a predefined placeholder object filter criterion value for lookup fields, applicable with equal or not_equal comparators when the field's data_type is ownerlookup or userlookup. Two forms are supported: (1) the currently logged-in user, represented by passing only the name property with the predefined value ${CURRENTUSER} and no ID property; and (2) the logged-in user's role, represented by passing the ID property with the predefined value ${CURRENTUSERROLE} and an optional display label in the name property. For specific real users or roles that are not predefined, use SimpleFilterCriterionValueObjectRequest, which requires the ID property.
      - `SimpleFilterCriterionValueGeneralPredefined` (string) [enum=['${EMPTY}', '${NOTEMPTY}']] — Represents a predefined placeholder value applicable to any field data_type with the equal comparator.
Possible values:
${EMPTY} - Matches records where the field has no value.
${NOTEMPTY} - Matches records where the field has any non-empty value.
      - `SimpleFilterCriterionValueDateTimePredefined` (string) [enum=[22 values]] — Represents a predefined placeholder value applicable only when the field's data_type is date or datetime, with the equal comparator.
      - `SimpleFilterCriterionValueNDaysPredefined` (string) [maxLen=255, pattern=^\$\{(LAST_N_|NEXT_N_)(DAYS|WEEKS|MONTHS|YEARS):([0-9]+)\}$] — Represents a predefined N-period range placeholder value applicable only when the field's data_type is date or datetime, with the equal comparator. Follows the pattern ${NEXT_N_<PERIOD>:<n>} or ${LAST_N_<PERIOD>:<n>}, where PERIOD is DAYS, WEEKS, MONTHS, or YEARS and n is a positive integer. The current period is always excluded from the range.
      - `SimpleFilterCriterionValueAgeDuePredefined` (string) [maxLen=255, pattern=^\$\{(AGEINDAYS|DUEINDAYS)\}\+[0-9]+$] — Represents a predefined age or due-in-days placeholder value applicable only when the field's data_type is date or datetime. Follows the pattern ${AGEINDAYS}+<n> for records where the date field was exactly n days in the past, or ${DUEINDAYS}+<n> for records where the date field is exactly n days in the future. Supported comparators are equal, not_equal, less_than, greater_than, less_equal, and greater_equal.
  - `type` (string) [enum=['merge_field', 'value', 'pre_defined', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
  - `$disrupted` (boolean) — Indicates whether the equal filter criterion is in a disrupted state, typically due to an invalid or unresolvable field or value reference.
`EqualityFilterCriterionResponse`:
  oneOf:
    - `EqualFilterCriterionResponse` — Represents the response for a filter criterion using the equal comparator. The value type is determined by the field's data_type: SimpleFilterCriterionValueString for text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime; SimpleFilterCriterionValueNumber for integer, currency, or double; SimpleFilterCriterionValueBoolean for Boolean; SimpleFilterCriterionValueObjectResponse for lookup, ownerlookup, or userlookup; and SimpleFilterCriterionValueObjectPredefined for predefined user or role object placeholders.
    - `NotEqualFilterCriterionResponse` — Represents the response for a filter criterion using the not_equal comparator. The value type is determined by the field's data_type: SimpleFilterCriterionValueString for text-based types; SimpleFilterCriterionValueNumber for numeric types; SimpleFilterCriterionValueBoolean for Boolean; SimpleFilterCriterionValueObjectResponse for lookup types; and SimpleFilterCriterionValueObjectPredefined for predefined user or role placeholders.
`FilterCriterionResponse`:
  oneOf:
    - `SimpleFilterCriterionResponse` — Represents the response for a simple field-based filter criterion, dispatching to the appropriate comparator-specific response schema.
    - `GroupedFilterCriterionResponse` — Represents the grouped filter criterion returned in the response, containing multiple filter conditions evaluated with a logical operator. Supports recursive nesting for complex filtering logic.
`FilterFieldBase`:
  > Represents the base field reference used in filter operations, containing minimal required properties. The field's data_type is not part of this object; resolve it from the corresponding FieldSchema. For formula fields, use formula.return_type as the effective data_type; for rollup_summary fields, use rollup_summary.return_type.
  - `id` (string/int64) — Represents the unique ID of the field used for filter operations.
  - `api_name` (string) **REQ** — Represents the API name of the field used for filter application. Supports relationship notation, for example, Deals__r.Stage.
  additionalProperties: any
`GETAssociatedField`:
  > Represents a field associated with a kiosk state, including its API name and unique identifier.
  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field associated with the kiosk state.
  - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the field associated with the kiosk state.
  - `type` (string) [maxLen=255] — Field: type. Present only for screen state associated fields.
`GETConfiguredPropertyDetails`:
  > Represents the details of a configured property associated with a kiosk state. Contains the name of the configured property.
  - `name` (string) **REQ** [maxLen=255] — Represents the name of the configured property detail.
  - `component_name` (string) [maxLen=255] — Field: component_name. Associated component reference.
`GETFromTransition`:
  > Specifies the transition through which the current state is reached. This object contains the transition's name and ID. This field is null for the start state.
  - `name` (string) **REQ** [maxLen=255] — Represents the display name of the transition that leads into this kiosk state.
  - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the transition that leads into this kiosk state.
`GETModule`:
  > Represents a CRM module reference returned in a GET response, including the module's API name and unique identifier.
  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the CRM module.
  - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the CRM module.
`GETScreenSelectedField`:
  > Represents a field selected from a get_record or data hub component to display on the screen. Contains the field's API name and unique identifier.
  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field selected from the get_record component to display on the screen.
  - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the field selected from the get_record component.
`GETTransition`:
  > Represents an outgoing transition from a kiosk state returned in a GET response. Contains the transition ID and display name.
  - `name` (string) **REQ** [maxLen=255] — Represents the display name of the outgoing transition.
  - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the outgoing transition.
`GroupedFilterCriterionResponse`:
  > Represents the grouped filter criterion returned in the response, containing multiple filter conditions evaluated with a logical operator. Supports recursive nesting for complex filtering logic.
  - `group` (array of object) [minItems=2, maxItems=25] **REQ** — Contains an array of filter conditions grouped together and evaluated with the specified logical operator.
    oneOf:
      - `SimpleFilterCriterionResponse` — Represents the response for a simple field-based filter criterion, dispatching to the appropriate comparator-specific response schema.
      - `GroupedFilterCriterionResponse` — Represents the grouped filter criterion returned in the response, containing multiple filter conditions evaluated with a logical operator. Supports recursive nesting for complex filtering logic.
  - `group_operator` (string) **REQ** [enum=['AND', 'OR', 'and', 'or']] — Represents the logical operator applied between the filter conditions in the group.
Possible values:
AND - All conditions in the group must be satisfied.
OR - At least one condition in the group must be satisfied.
and - Equivalent to AND; all conditions in the group must be satisfied.
or - Equivalent to OR; at least one condition in the group must be satisfied.
  - `$disrupted` (boolean) — Indicates whether the grouped filter criterion is in a disrupted state, typically due to an invalid or unresolvable condition within the group.
`MultiSelectLookupFilterCriterionResponse`:
  > Represents the response for a filter criterion using the include_all, include_any, exclude_all, and exclude_any comparators. Applicable only when the field's data_type is multiuserlookup or multiselectlookup.
  - `field` (object) **REQ** — Represents the target field definition to which the multi-select lookup filter criterion was applied. The field has a data_type of multiuserlookup or multiselectlookup.
  - `comparator` (string) **REQ** [enum=['include_all', 'include_any', 'exclude_all', 'exclude_any']] — Represents the multi-select lookup comparison operator returned for the criterion. Applicable only when the field's data_type is multiuserlookup or multiselectlookup.
Possible values:
include_all - Matches records that include all specified lookup values.
include_any - Matches records that include at least one of the specified lookup values.
exclude_all - Matches records that exclude all specified lookup values.
exclude_any - Matches records that exclude at least one of the specified lookup values.
  - `value` (array of object `SimpleFilterCriterionValueObjectResponse`) [minItems=1, maxItems=500] **REQ** — Contains an array of lookup object references returned for the multi-select comparison.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
  - `$disrupted` (boolean) — Indicates whether the multi-select lookup filter criterion is in a disrupted state, typically due to an invalid or unresolvable field or value reference.
`NotEqualFilterCriterionResponse`:
  > Represents the response for a filter criterion using the not_equal comparator. The value type is determined by the field's data_type: SimpleFilterCriterionValueString for text-based types; SimpleFilterCriterionValueNumber for numeric types; SimpleFilterCriterionValueBoolean for Boolean; SimpleFilterCriterionValueObjectResponse for lookup types; and SimpleFilterCriterionValueObjectPredefined for predefined user or role placeholders.
  - `field` (object) **REQ** — Represents the target field definition to which the not-equal filter criterion was applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['not_equal']] — Represents the not-equal comparison operator returned for the criterion.
Possible values:
not_equal - Matches records where the field value does not equal the specified filter value.
  - `value` (object) **REQ** — Represents the filter value returned for the not_equal comparator. Contains a scalar or an array of values, depending on the field's data_type.
    anyOf:
        type: array of object [minItems=1, maxItems=500]
          oneOf:
            - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
            - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
              anyOf:
                - `SimpleFilterCriterionValueObjectResponse` — Represents a lookup object filter criterion value for response bodies, applicable when the field's data_type is lookup, ownerlookup, or userlookup. Both the ID and name properties are included.
                - `SimpleFilterCriterionValueObjectPredefined` — Represents a predefined placeholder object filter criterion value for lookup fields, applicable with equal or not_equal comparators when the field's data_type is ownerlookup or userlookup. Two forms are supported: (1) the currently logged-in user, represented by passing only the name property with the predefined value ${CURRENTUSER} and no ID property; and (2) the logged-in user's role, represented by passing the ID property with the predefined value ${CURRENTUSERROLE} and an optional display label in the name property. For specific real users or roles that are not predefined, use SimpleFilterCriterionValueObjectRequest, which requires the ID property.
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
      - `SimpleFilterCriterionValueBoolean` (boolean) — Represents a Boolean filter criterion value. Applicable only when the field has a Boolean data type (checkbox field).
      - `SimpleFilterCriterionValueObjectResponse` — Represents a lookup object filter criterion value for response bodies, applicable when the field's data_type is lookup, ownerlookup, or userlookup. Both the ID and name properties are included.
      - `SimpleFilterCriterionValueObjectPredefined` — Represents a predefined placeholder object filter criterion value for lookup fields, applicable with equal or not_equal comparators when the field's data_type is ownerlookup or userlookup. Two forms are supported: (1) the currently logged-in user, represented by passing only the name property with the predefined value ${CURRENTUSER} and no ID property; and (2) the logged-in user's role, represented by passing the ID property with the predefined value ${CURRENTUSERROLE} and an optional display label in the name property. For specific real users or roles that are not predefined, use SimpleFilterCriterionValueObjectRequest, which requires the ID property.
      - `SimpleFilterCriterionValueAgeDuePredefined` (string) [maxLen=255, pattern=^\$\{(AGEINDAYS|DUEINDAYS)\}\+[0-9]+$] — Represents a predefined age or due-in-days placeholder value applicable only when the field's data_type is date or datetime. Follows the pattern ${AGEINDAYS}+<n> for records where the date field was exactly n days in the past, or ${DUEINDAYS}+<n> for records where the date field is exactly n days in the future. Supported comparators are equal, not_equal, less_than, greater_than, less_equal, and greater_equal.
  - `type` (string) [enum=['merge_field', 'value', 'pre_defined', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
  - `$disrupted` (boolean) — Indicates whether the not-equal filter criterion is in a disrupted state, typically due to an invalid or unresolvable field or value reference.
`OrderingFilterCriterionResponse`:
  > Represents the response for a filter criterion using the less_than, less_equal, greater_than, and greater_equal comparators. The value is a scalar; arrays and objects are not valid.
  - `field` (object) **REQ** — Represents the target field definition to which the ordering filter criterion was applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['less_than', 'less_equal', 'greater_than', 'greater_equal']] — Represents the ordering comparison operator returned for the criterion.
Possible values:
less_than - Matches records where the field value is less than the specified filter value.
less_equal - Matches records where the field value is less than or equal to the specified filter value.
greater_than - Matches records where the field value is greater than the specified filter value.
greater_equal - Matches records where the field value is greater than or equal to the specified filter value.
  - `value` (object) **REQ** — Represents the scalar filter value returned for the ordering comparator.
    anyOf:
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
      - `SimpleFilterCriterionValueAgeDuePredefined` (string) [maxLen=255, pattern=^\$\{(AGEINDAYS|DUEINDAYS)\}\+[0-9]+$] — Represents a predefined age or due-in-days placeholder value applicable only when the field's data_type is date or datetime. Follows the pattern ${AGEINDAYS}+<n> for records where the date field was exactly n days in the past, or ${DUEINDAYS}+<n> for records where the date field is exactly n days in the future. Supported comparators are equal, not_equal, less_than, greater_than, less_equal, and greater_equal.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
  - `$disrupted` (boolean) — Indicates whether the ordering filter criterion is in a disrupted state, typically due to an invalid or unresolvable field or value reference.
`SetFilterCriterionResponse`:
  > Represents the response for a filter criterion using the in and not_in comparators. The value is an array of primitive values.
  - `field` (object) **REQ** — Represents the target field definition to which the set filter criterion was applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['in', 'not_in']] — Represents the set membership comparison operator returned for the criterion.
Possible values:
in - Matches records where the field value is in the specified set of values.
not_in - Matches records where the field value is not in the specified set of values.
  - `value` (array of object) [minItems=1, maxItems=500] **REQ** — Contains an array of primitive filter values returned for the set comparison.
    oneOf:
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
  - `$disrupted` (boolean) — Indicates whether the set filter criterion is in a disrupted state, typically due to an invalid or unresolvable field or value reference.
`SimpleFilterCriterionResponse`:
  oneOf:
    - `EqualityFilterCriterionResponse` — Represents the response for an equality filter criterion that dispatches to either the EqualFilterCriterionResponse or NotEqualFilterCriterionResponse schema based on the comparator value.
    - `TextFilterCriterionResponse` — Represents the response for a filter criterion using the like, not_like, starts_with, ends_with, contains, and not_contains comparators. The value is a string scalar or array; SimpleFilterCriterionValueString applies to text-based field types.
    - `OrderingFilterCriterionResponse` — Represents the response for a filter criterion using the less_than, less_equal, greater_than, and greater_equal comparators. The value is a scalar; arrays and objects are not valid.
    - `BetweenFilterCriterionResponse` — Represents the response for a filter criterion using the between and not_between comparators. The value is an array of exactly two elements — [lower_bound, upper_bound]. The value type is determined by the field's data_type: SimpleFilterCriterionValueString for date or datetime fields, and SimpleFilterCriterionValueNumber for integer, currency, or double fields.
    - `SetFilterCriterionResponse` — Represents the response for a filter criterion using the in and not_in comparators. The value is an array of primitive values.
    - `MultiSelectLookupFilterCriterionResponse` — Represents the response for a filter criterion using the include_all, include_any, exclude_all, and exclude_any comparators. Applicable only when the field's data_type is multiuserlookup or multiselectlookup.
`SimpleFilterCriterionValueObjectBase`:
  > Represents the base minified record structure of a lookup module, containing the record's unique identifier and display name.
  - `id` (string/int64) — Represents the unique ID of the lookup module record.
  - `name` (string) [maxLen=255] — Represents the display name of the lookup module record.
  additionalProperties: any
`SimpleFilterCriterionValueObjectPredefined`:
  oneOf:
      - `name` (string) **REQ** [enum=['${CURRENTUSER}']] — Represents the predefined placeholder for the currently logged-in user.
Possible values:
${CURRENTUSER} - Represents the currently logged-in user.
      - `id` (string) **REQ** [enum=['${CURRENTUSERROLE}']] — Represents the predefined placeholder for the logged-in user's role record ID.
Possible values:
${CURRENTUSERROLE} - Represents the role of the currently logged-in user.
      - `name` (string) [maxLen=255] — Represents an optional display label for the predefined role, such as Logged in User Role.
      additionalProperties: any
`SimpleFilterCriterionValueObjectResponse`:
  > Represents the base minified record structure of a lookup module, containing the record's unique identifier and display name.
  - `id` (object) **REQ**
  - `name` (object) **REQ**
  additionalProperties: any
`TextFilterCriterionResponse`:
  > Represents the response for a filter criterion using the like, not_like, starts_with, ends_with, contains, and not_contains comparators. The value is a string scalar or array; SimpleFilterCriterionValueString applies to text-based field types.
  - `field` (object) **REQ** — Represents the target field definition to which the text filter criterion was applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['like', 'not_like', 'starts_with', 'ends_with', 'contains', 'not_contains']] — Represents the text comparison operator returned for the criterion.
Possible values:
like - Matches records where the field value contains the specified pattern.
not_like - Matches records where the field value does not contain the specified pattern.
starts_with - Matches records where the field value begins with the specified string.
ends_with - Matches records where the field value ends with the specified string.
contains - Matches records where the field value contains the specified string.
not_contains - Matches records where the field value does not contain the specified string.
  - `value` (object) **REQ** — Represents the string filter value returned for the text comparator. Contains a scalar string or an array of string values.
    oneOf:
        type: array of object [minItems=1, maxItems=500]
          oneOf:
            - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
  - `$disrupted` (boolean) — Indicates whether the text filter criterion is in a disrupted state, typically due to an invalid or unresolvable field or value reference.

**Responses:**

- **200**: Returns the details of the specified kiosk state in Zoho CRM. The response contains a single-item states array whose structure varies by state type: screen, decision, action, or get_records. — Schema: `GetStateResponse` [application/json]
    > Represents the response for retrieving a specific kiosk state. The state details structure varies by type and can be a screen, decision, action, or get_records state.
    schema: `GetStateResponse`
    - `states` (array of object) [maxItems=1] **REQ** — Represents the list of states returned for the kiosk.
      oneOf:
        - `GETScreenState` — Represents a single screen state returned by the get-by-ID endpoint, including its configuration, associated fields, transitions, and configured properties.
          - `associated_fields` (array of object `GETAssociatedField`) [maxItems=2] **REQ** — Represents the list of fields associated with the screen state.
          - `configured_properties` (array of object `GETScreenConfiguredProperty`) [maxItems=2, nullable] **REQ** — Represents the configured properties associated with the screen state.
            schema: `GETScreenConfiguredProperty`
            - `details` (object `GETConfiguredPropertyDetails`) **REQ** — Represents the details of a configured property associated with a kiosk state. Contains the name of the configured property.
            - `type` (string) **REQ** [maxLen=255, enum=['_merge_field', 'recipients']] — Represents the type of the configured property associated with the screen state.
          - `from_transition` (object `GETFromTransition`) **REQ** — Specifies the transition through which the current state is reached. This object contains the transition's name and ID. This field is null for the start state.
          - `name` (string) **REQ** [maxLen=255] — Represents the display name of the kiosk screen state.
          - `details` (object `GETScreenStateDetails`) **REQ** — Represents the details object for a screen state returned in a GET response. Contains the screen configuration including elements, buttons, and layout properties.
            schema: `GETScreenStateDetails`
            - `screen_details` (object `GETScreenConfiguration`) **REQ** — Represents the screen configuration returned in a GET response for a screen state. Contains the UI elements, buttons, width, title, and button alignment.
              schema: `GETScreenConfiguration`
              - `buttons` (array of object `GETScreenButton`) [maxItems=1] **REQ** — Represents the list of action buttons configured on the screen.
                schema: `GETScreenButton`
                - `prop_name` (string) **REQ** [maxLen=255] — Represents the style type of the button, which determines its visual appearance and behavior.
                - `name` (string) **REQ** [maxLen=255] — Represents the display label of the screen button shown to the user.
                - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the screen button.
              - `elements` (array of object) [maxItems=30] **REQ** — Represents the list of UI components rendered on the screen, ordered from top to bottom.
                oneOf:
                  - `GETScreenTextElement` — Represents a text element returned in a GET response for a screen state. Contains the element type and text content.
                    - `type` (string) **REQ** [maxLen=255] — Represents the type of the screen element. Always 'text' for text elements.
                    - `value` (string) **REQ** [maxLen=255] — Represents the text content displayed in the text element on the screen.
                  - `GETScreenGetRecordElement` — Represents a get_record element wrapper returned in a GET response for a screen state. Contains the element type, UI type, and get_record configuration.
                    - `get_record` (object `GETScreenGetRecord`) **REQ** — Represents a get_record component returned in a GET response for a screen state. Contains the component ID, name, selected fields, module reference, open_record flag, and selection details.
                      schema: `GETScreenGetRecord`
                      - `selection_details` (object `GETScreenSelectionDetails`) **REQ** — Represents the selection configuration for a get_record or data hub component on the screen. Contains the selection type, result type, limit, and range.
                        schema: `GETScreenSelectionDetails`
                        - `selection_type` (string) **REQ** [maxLen=255] — Represents the selection method used to retrieve records in the get_record component.
                        - `result_type` (string) **REQ** [maxLen=255] — Represents the result type of the get_record retrieval, indicating whether the query returns a single record or a list of records.
                        - `limit` (integer/int32) **REQ** — Represents the maximum number of records to retrieve from the get_record component.
                        - `range` (integer/int32) **REQ** — Represents the record range for the get_record retrieval.
                      - `open_record` (boolean) **REQ** — Indicates whether clicking a record in the get_record component opens its detail view.\nPossible values:\ntrue - Clicking a record opens its detail view.\nfalse - Records are displayed without opening the detail view.
                      - `module` (object `GETModule`) **REQ** — Represents a CRM module reference returned in a GET response, including the module's API name and unique identifier.
                      - `name` (string) **REQ** [maxLen=255] — Represents the display name of the get_record component shown on the screen.
                      - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the get_record component displayed on the screen.
                      - `selected_fields` (array of object `GETScreenSelectedField`) [maxItems=2] **REQ** — Represents the list of fields retrieved from the get_record component and displayed on the screen.
                    - `ui_type` (integer/int32) **REQ** — Represents the numeric identifier of the UI widget type used to render the get_record element.
                    - `type` (string) **REQ** [maxLen=255] — Represents the type of the screen element. Always 'get_records' for get_record elements.
                    - `value` (null) **REQ** — Represents the element value. Null for get_record elements.
                  - `GETScreenFieldElement` — Represents a basic field element wrapper returned in a GET response for a screen state. Contains the element type and field configuration.
                    - `field` (object `GETScreenBasicField`) **REQ** — Represents a basic form field returned in a GET response for a screen state. Contains field metadata including API name, data type, UI type, display label, read-only flag, and required flag.
                      schema: `GETScreenBasicField`
                      - `allow_multiple_upload` (null) **REQ** — Indicates whether multiple file uploads are allowed. Null for field types that do not support file upload.
                      - `field_label` (string) **REQ** [maxLen=255] — Represents the display label of the screen field shown to the user.
                      - `length` (integer/int32) **REQ** [nullable] — Represents the maximum number of characters or digits allowed for the field. Null for field types that do not enforce a length constraint.
                      - `tooltip` (null) **REQ** — Represents the tooltip configuration for the field. Null when no tooltip is configured.
                      - `_merge_field` (null) **REQ** — Represents a dynamic data binding expression that populates the field from an external source. Three formats are supported: record field, CRM module field, and kiosk screen field. Null when no merge field is configured.
                      - `number_separator` (boolean) **REQ** — Indicates whether a thousands separator is displayed for numeric values.\nPossible values:\ntrue - A thousands separator is displayed.\ nfalse - No thousands separator is displayed.
                      - `required` (boolean) **REQ** — Indicates whether a value is required before the screen can proceed.\nPossible values:\ntrue - A value must be provided.\nfalse - The field may be left empty.
                      - `ui_type` (integer/int32) **REQ** — Represents the numeric identifier of the UI widget type used to render the field.
                      - `read_only` (boolean) **REQ** — Indicates whether the field is read-only.\nPossible values:\ ntrue - The field is displayed but cannot be edited by the user.\nfalse - The user can input or modify the value.
                      - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the screen field.
                      - `data_type` (string) **REQ** [maxLen=255] — Represents the data type of the screen field, such as text, textarea, phone, email, currency, or picklist.
                      - `currency` (null) **REQ** — Represents the currency configuration of the field. Null for non-currency fields.
                      - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the screen field.
                      - `_pick_list_type` (null) **REQ** — Represents the picklist source type. Null for non-picklist fields.
                      - `decimal_place` (null) **REQ** — Represents the number of decimal places for numeric fields. Null for non-numeric fields.
                      - `pick_list_values` (null) **REQ** — Represents the list of picklist option values. Null for non-picklist fields.
                    - `type` (string) **REQ** [maxLen=255] — Represents the type of the screen element. Always 'field' for basic field elements.
                    - `value` (null) **REQ** — Represents the element value. Null for field-type elements.
                  - `GETScreenCurrencyFieldElement` — Represents a currency field element wrapper returned in a GET response for a screen state. Contains the element type and field configuration.
                    - `field` (object `GETScreenCurrencyField`) **REQ** — Represents a currency form field returned in a GET response for a screen state. Contains currency-specific metadata including decimal places, precision, and rounding option.
                      schema: `GETScreenCurrencyField`
                      - `allow_multiple_upload` (null) **REQ** — Indicates whether multiple file uploads are allowed. Null for currency fields.
                      - `field_label` (string) **REQ** [maxLen=255] — Represents the display label of the currency field shown to the user.
                      - `length` (integer/int32) **REQ** — Represents the maximum number of digits allowed for the currency field.
                      - `tooltip` (null) **REQ** — Represents the tooltip configuration for the currency field. Null when no tooltip is configured.
                      - `_merge_field` (null) **REQ** — Represents a dynamic data binding expression that populates the field from an external source. Three formats are supported: record field, CRM module field, and kiosk screen field. Null when no merge field is configured.
                      - `number_separator` (boolean) **REQ** — Indicates whether a thousands separator is displayed for the currency field value.\nPossible values:\ntrue - A thousands separator is displayed.\nfalse - No thousands separator is displayed.
                      - `required` (boolean) **REQ** — Indicates whether a value is required in the currency field before the screen can proceed.\nPossible values:\ntrue - A value must be provided.\nfalse - The field may be left empty.
                      - `ui_type` (integer/int32) **REQ** — Represents the numeric identifier of the UI widget type used to render the currency field.
                      - `read_only` (boolean) **REQ** — Indicates whether the currency field is read-only.\nPossible values:\ntrue - The field is displayed but cannot be edited.\nfalse - The user can modify the value.
                      - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the currency screen field.
                      - `data_type` (string) **REQ** [maxLen=255] — Represents the data type of the field. Always 'currency' for this schema.
                      - `currency` (object `GETScreenCurrency`) **REQ** — Field: currency
                        schema: `GETScreenCurrency`
                        - `rounding_option` (string) **REQ** [maxLen=255] — Represents the rounding method applied to the currency field value.
                        - `precision` (integer/int32) **REQ** — Represents the number of digits after the decimal point for the currency field value.
                      - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the currency screen field.
                      - `_pick_list_type` (null) **REQ** — Represents the picklist source type. Null for currency fields.
                      - `decimal_place` (integer/int32) **REQ** — Represents the number of decimal places configured for the currency field.
                      - `pick_list_values` (null) **REQ** — Represents the list of picklist option values. Null for currency fields.
                    - `type` (string) **REQ** [maxLen=255] — Represents the type of the screen element. Always 'field' for currency field elements.
                    - `value` (null) **REQ** — Represents the element value. Null for field-type elements.
                  - `GETScreenPicklistFieldElement` — Represents a picklist field element wrapper returned in a GET response for a screen state. Contains the element type and field configuration.
                    - `field` (object `GETScreenPicklistField`) **REQ** — Represents a picklist form field returned in a GET response for a screen state. Contains the field metadata including the picklist values and source type.
                      schema: `GETScreenPicklistField`
                      - `allow_multiple_upload` (null) **REQ** — Indicates whether multiple file uploads are allowed. Null for picklist fields.
                      - `field_label` (string) **REQ** [maxLen=255] — Represents the display label of the picklist field shown to the user.
                      - `length` (integer/int32) **REQ** — Represents the maximum number of options allowed for the picklist field.
                      - `tooltip` (null) **REQ** — Represents the tooltip configuration for the picklist field. Null when no tooltip is configured.
                      - `_merge_field` (null) **REQ** — Represents a dynamic data binding expression that populates the field from an external source. Three formats are supported: record field, CRM module field, and kiosk screen field. Null when no merge field is configured.
                      - `number_separator` (boolean) **REQ** — Indicates whether a thousands separator is displayed. Not applicable for picklist fields.
                      - `required` (boolean) **REQ** — Indicates whether a selection is required before the screen can proceed.\nPossible values:\ntrue - A selection must be made.\nfalse - The field may be left empty.
                      - `ui_type` (integer/int32) **REQ** — Represents the numeric identifier of the UI widget type used to render the picklist field.
                      - `read_only` (boolean) **REQ** — Indicates whether the picklist field is read-only.\nPossible values:\ntrue - The field is displayed but cannot be edited.\nfalse - The user can select a value.
                      - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the picklist screen field.
                      - `data_type` (string) **REQ** [maxLen=255] — Represents the data type of the screen field, such as picklist or multiselectpicklist.
                      - `currency` (null) **REQ** — Represents the currency configuration of the field. Null for picklist fields.
                      - `_pick_list_type` (string) **REQ** [maxLen=255, nullable] — Represents the source of picklist values.\nPossible values:\ nlocal - Values are defined inline within the screen field.\nglobal_set - Values are sourced from a shared global picklist.
                      - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the picklist screen field.
                      - `decimal_place` (null) **REQ** — Represents the number of decimal places for the field. Null for picklist fields.
                      - `pick_list_values` (array of object `GETScreenPickListValue`) [maxItems=3] **REQ** — Represents the list of picklist options available for selection.
                        schema: `GETScreenPickListValue`
                        - `display_value` (string) **REQ** [maxLen=255] — Represents the text displayed to the user for this picklist option.
                        - `sequence_number` (integer/int32) **REQ** — Represents the display order of the picklist option within the list.
                        - `actual_value` (string) **REQ** [maxLen=255] — Represents the value stored internally when this picklist option is selected.
                        - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the picklist option.
                    - `type` (string) **REQ** [maxLen=255] — Represents the type of the screen element. Always 'field' for picklist field elements.
                    - `value` (null) **REQ** — Represents the element value. Null for picklist field elements.
                  - `GETScreenDataHubElement` — Represents a data hub element wrapper returned in a GET response for a screen state. Contains the element type and data hub configuration.
                    - `data_hub` (object `GETScreenDataHub`) **REQ** — Represents a data hub component returned in a GET response for a screen state. Contains the component ID, name, selected fields, module reference, and selection details.
                      schema: `GETScreenDataHub`
                      - `selection_details` (object `GETDataHubSelectionDetails`) **REQ** — Represents the selection details for a data hub component, including the selection type, result type, limit, and range.
                        schema: `GETDataHubSelectionDetails`
                        - `selection_type` (string) **REQ** [maxLen=255, nullable] — Represents the selection method used for the data hub query.
                        - `result_type` (string) **REQ** [maxLen=255] — Represents the result type of the data hub query, indicating whether the query returns a single record or a list of records.
                        - `limit` (integer/int32) **REQ** — Represents the maximum number of records to retrieve in the data hub query.
                        - `range` (integer/int32) **REQ** [nullable] — Represents the record range for the data hub query result.
                      - `module` (object `GETModule`) **REQ** — Represents a CRM module reference returned in a GET response, including the module's API name and unique identifier.
                      - `name` (string) **REQ** [maxLen=255] — Represents the display name of the data hub component.
                      - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the data hub component.
                      - `selected_fields` (array of object `GETScreenSelectedField`) [maxItems=10] **REQ** — Represents the list of fields selected from the data hub query to display on the screen.
                    - `type` (string) **REQ** [maxLen=255] — Represents the type of the screen element. Always 'data_hubs' for data hub elements.
                    - `value` (null) **REQ** — Represents the element value. Null for data hub elements.
              - `width` (string) **REQ** [maxLen=255, enum=['670px', '1000px']] — Represents the visual width of the screen container.
              - `title` (string) **REQ** [maxLen=255] — Represents the display title shown at the top of the screen.
              - `button_align` (string) **REQ** [maxLen=255, enum=['right_to_left', 'left_to_right', 'center']] — Represents the alignment direction of action buttons within the screen footer.
          - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the kiosk screen state.
          - `type` (string) **REQ** [maxLen=255, enum=['screen']] — Represents the type of the kiosk state. Always 'screen' for this schema.
          - `transitions` (array of object `GETTransition`) [maxItems=1] **REQ** — Represents the list of outgoing transitions configured for the screen state.
        - `GETDecisionState` — Represents a single decision state returned by the get-by-ID endpoint, including its configuration, associated fields, transitions, and configured properties.
          - `associated_fields` (array of object `GETDecisionAssociatedField`) [maxItems=30] **REQ** — Represents the list of fields associated with the decision state, including the paths that reference each field.
            schema: `GETDecisionAssociatedField`
            - `path_details` (array of object `GETDecisionPathRef`) [maxItems=11] — Represents the list of decision paths that reference this associated field.
              schema: `GETDecisionPathRef`
              - `name` (string) **REQ** [maxLen=255] — Represents the display name of the decision path referenced by the associated field.
              - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the decision path referenced by the associated field.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field associated with the decision state.
            - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the field associated with the decision state.
          - `configured_properties` (array of object `GETDecisionConfiguredProperty`) [maxItems=30] **REQ** — Represents the list of configured properties associated with the decision state.
            schema: `GETDecisionConfiguredProperty`
            - `details` (object `GETConfiguredPropertyDetails`) **REQ** — Represents the details of a configured property associated with a kiosk state. Contains the name of the configured property.
            - `type` (string) **REQ** [maxLen=255, enum=['_merge_field', 'recipients']] — Represents the type of the configured property associated with the decision state.
          - `from_transition` (object `GETFromTransition`) **REQ** — Specifies the transition through which the current state is reached. This object contains the transition's name and ID. This field is null for the start state.
          - `name` (string) **REQ** [maxLen=255] — Represents the display name of the kiosk decision state.
          - `details` (object `GETDecisionStateDetails`) **REQ** — Represents the details object for a decision state returned in a GET response. Contains the path definitions configured for the decision.
            schema: `GETDecisionStateDetails`
            - `path_details` (array of object) [maxItems=6] **REQ** — Represents the list of decision paths configured for the decision state.
              oneOf:
                - `GETDecisionPathDetails` — Represents a decision path returned in a GET response, including the path ID, name, default flag, and filter conditions.
                  - `default` (boolean) **REQ** — Indicates whether this path is the default fallback path. Possible values:
true - This path is the default fallback and is taken if no other conditions are satisfied.
false - This path requires filter conditions to be met.

                  - `name` (string) **REQ** [maxLen=255] — Represents the display name of the decision path.
                  - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the decision path.
                  - `filter_conditions` (object `GETDecisionFilterConditions`) **REQ** — Field: filter_conditions
                    schema: `GETDecisionFilterConditions`
                    - `criteria_groupings` (array of object) [maxItems=5] **REQ** — Represents the list of conditions evaluated as part of the decision state.
                      oneOf:
                        - `GETDecisionCriteriaGrouping` — Represents a single condition grouping returned in a GET response for a decision state. Contains the sequence number, data source type, evaluation value, and criteria details.
                          - `sequence_number` (integer/int32) **REQ** — Represents the position index of the condition within the criteria groupings list, referenced by the logical pattern expression.
                          - `resource` (null) **REQ** — Represents the resource used as the data source when evaluating the condition. This is null when the condition type does not reference an external record.
                          - `criteria` (object `FilterCriterionResponse`) **REQ** — Criteria for this grouping in the GET response. Automatically resolves to either a simple field-value comparison or a nested grouped condition. Defined in Criterion.json.
                          - `type` (string) **REQ** [maxLen=255] — Represents the data source type used for condition evaluation. Indicates whether the condition evaluates a field from the current record, a get_record result, a kiosk screen field, a data hub, a created record, or a loop record.
                          - `value` (string) **REQ** [maxLen=255, nullable] — Represents whether the evaluated field must contain data.\ nPossible values:\n${NOTEMPTY} - The field must have a value.\n${EMPTY} - The field must be empty.
                        - `GETDecisionCriteriaGroupingNested` — Represents a nested condition grouping returned in a GET response for a decision state. Contains the sequence number, data source type, evaluation value, resource reference, and criteria details.
                          - `sequence_number` (integer/int32) **REQ** — Represents the position index of the condition within the criteria groupings list, referenced by the logical pattern expression.
                          - `resource` (object) **REQ** — Represents the resource used as the data source when evaluating the condition.
                            - `name` (string) **REQ** [maxLen=255] — Represents the display name of the resource referenced by the decision condition.
                            - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the resource referenced by the decision condition.
                          - `criteria` (object `FilterCriterionResponse`) — Criteria for this grouping in the GET response. Automatically resolves to either a simple field-value comparison or a nested grouped condition. Defined in Criterion.json.
                          - `type` (string) **REQ** [maxLen=255] — Represents the data source type used for condition evaluation.
                          - `value` (string) **REQ** [maxLen=255] — Represents whether the evaluated field must contain data.\ nPossible values:\n${NOTEMPTY} - The field must have a value.\n${EMPTY} - The field must be empty.
                    - `pattern` (string) **REQ** [maxLen=255] — Represents the logical expression that combines criteria groupings. Sequence numbers in the pattern reference the corresponding groupings, combined using logical operators such as and and or.
          - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the kiosk decision state.
          - `type` (string) **REQ** [maxLen=255, enum=['decision']] — Represents the type of the kiosk state. Always 'decision' for this schema.
          - `transitions` (array of object `GETDecisionTransition`) [maxItems=30] **REQ** — Represents the list of outgoing transitions configured for the decision state.
            schema: `GETDecisionTransition`
            - `default` (boolean) **REQ** — Indicates whether this transition corresponds to the default fallback decision path.
Possible values:
true - This is the default fallback transition.
false - This transition requires filter conditions to be met.

            - `name` (string) **REQ** [maxLen=255] — Represents the display name of the decision transition.
            - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the decision transition.
        - `GETActionStateDetail` — Represents a single action state returned by the get-by-ID endpoint, including the action configuration, associated fields, transitions, and configured properties.
          - `associated_fields` (array of object `GETAssociatedField`) [maxItems=25, nullable] **REQ** — Represents the list of fields associated with the action state.
          - `configured_properties` (object) [nullable] — Represents additional configured properties returned for the action state.
          - `from_transition` (object `GETTransition`) — Transition that leads into this action state.
          - `name` (string) **REQ** [maxLen=255] — Represents the name of the kiosk action state.
          - `details` (object) **REQ** — Represents the detailed action configuration for the kiosk action state.
          - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the kiosk action state.
          - `type` (string) **REQ** [maxLen=255, enum=['action']] — Represents the type of the kiosk state.
          - `transitions` (array of object `GETTransition`) [maxItems=25] **REQ** — Represents the list of outgoing transitions configured for the kiosk action state.
        - `GETGetRecordState` — Represents a single get_records state returned by the get-by-ID endpoint. Contains the state configuration, associated fields, transitions, and the linked get_record component details.
          - `associated_fields` (array of object `GETAssociatedField`) [maxItems=25, nullable] **REQ** — Represents the list of fields associated with the get_records state.
          - `configured_properties` (object) [nullable] — Represents additional configured properties returned for the get_records state. This is typically null for get_records states.
          - `from_transition` (object `GETFromTransition`) **REQ** — Transition that leads into this get_records state.
          - `name` (string) **REQ** [maxLen=255] — Represents the display name of the kiosk get_records state.
          - `details` (object `GETGetRecordStateDetails`) **REQ** — Configuration details containing the get_record reference.
            schema: `GETGetRecordStateDetails`
            - `get_record` (object) **REQ** — Represents the get_record component associated with the get_records state.
              - `name` (string) **REQ** [maxLen=255] — Represents the display name of the get_record component.
              - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the get_record component.
          - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the kiosk get_records state.
          - `type` (string) **REQ** [enum=['get_records']] — Represents the type of the kiosk state. Always 'get_records' for this schema.
          - `transitions` (array of object `GETTransition`) [maxItems=25, nullable] **REQ** — Represents the list of outgoing transitions from the get_records state.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request could not be processed due to invalid or missing data in the path parameters.
**Resolution:** Verify that the kiosk ID and state ID in the request path refer to existing resources and that all required fields are provided with the correct data types. — Schema: `KioskStateErrorResponse` [application/json]
    > Represents the generic error response for kiosk state operations. Contains an error code, error message, and contextual details about the validation failure.
    schema: `KioskStateErrorResponse`
    - `code` (string) **REQ** [enum=[8 values]] — Represents the error category code indicating the type of validation failure.
    - `details` (object) **REQ** — Represents contextual details about the error. The structure varies by error type and may include the affected field path, expected data type, or resource path.
      - `api_name` (string) [maxLen=255] — Represents the API name of the field that caused the error.
      - `json_path` (string) [maxLen=1000] — Represents the JSON path pointing to the problematic field in the request body.
      - `expected_data_type` (string) [maxLen=255] — Represents the expected data type when a type mismatch occurs in the request.
      - `maximum_length` (integer/int32) — Represents the maximum allowed length when a field value exceeds the configured limit.
      - `resource_path_index` (integer/int32) — Represents the index in the resource path that is invalid.
      - `permissions` (array of string) [maxItems=100] — Represents the list of required OAuth scopes when access is denied.
        items: [maxLen=255]
      additionalProperties: any
    - `message` (string) **REQ** [maxLen=500] — Represents the error message describing what went wrong.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Always 'error' for error responses.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.kiosks.READ
