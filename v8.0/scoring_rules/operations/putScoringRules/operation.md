# PUT /settings/automation/scoring_rules
**Operation:** `putScoringRules` — Scoring Rules
> Updates one or more scoring rules. Returns 200 (all success) or 207 (partial success).

**Schemas:**
`BetweenFilterCriterionRequest`:
  > Represents a filter criterion for the between and not_between comparators. The value must be an array of exactly two elements — [lower_bound, upper_bound]. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for date or datetime fields, and SimpleFilterCriterionValueNumber for integer, currency, or double fields. Resolve the data_type from the field's FieldSchema. For formula fields, use formula.return_type as the effective data_type; for rollup_summary fields, use rollup_summary.return_type.
  - `field` (object) **REQ** — Represents the target field definition to which the range filter criterion is applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['between', 'not_between']] — Represents the range comparison operator applied to the criterion, indicating whether the field value falls within or outside the specified bounds.
Possible values:
between - Matches records where the field value falls within the specified range.
not_between - Matches records where the field value falls outside the specified range.
  - `value` (array of object) [minItems=2, maxItems=2] **REQ** — Contains the two boundary values — [lower_bound, upper_bound] — against which the field is evaluated for the between or not_between comparator.
    oneOf:
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
`EqualFilterCriterionRequest`:
  > Represents a filter criterion for the equal comparator. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime fields; SimpleFilterCriterionValueNumber for integer, currency, or double fields; SimpleFilterCriterionValueBoolean for Boolean fields; SimpleFilterCriterionValueObjectRequest for lookup, ownerlookup, or userlookup fields; and SimpleFilterCriterionValueObjectPredefined for predefined user or role object placeholders. Accepts scalar or array values. Resolve the data_type from the field's FieldSchema.
  - `field` (object) **REQ** — Represents the target field definition to which the equal filter criterion is applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['equal']] — Represents the equal comparison operator applied to the criterion.
Possible values:
equal - Matches records where the field value equals the specified filter value.
  - `value` (object) **REQ** — Represents the filter value used in the equal comparator. Accepts a scalar or an array of values, depending on the field's data_type.
    anyOf:
        type: array of object [minItems=1, maxItems=500]
          oneOf:
            - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
            - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
              anyOf:
                - `SimpleFilterCriterionValueObjectRequest` — Represents a lookup object filter criterion value for request bodies, applicable when the field's data_type is lookup, ownerlookup, or userlookup. The ID property is required.
                - `SimpleFilterCriterionValueObjectPredefined` — Represents a predefined placeholder object filter criterion value for lookup fields, applicable with equal or not_equal comparators when the field's data_type is ownerlookup or userlookup. Two forms are supported: (1) the currently logged-in user, represented by passing only the name property with the predefined value ${CURRENTUSER} and no ID property; and (2) the logged-in user's role, represented by passing the ID property with the predefined value ${CURRENTUSERROLE} and an optional display label in the name property. For specific real users or roles that are not predefined, use SimpleFilterCriterionValueObjectRequest, which requires the ID property.
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
      - `SimpleFilterCriterionValueBoolean` (boolean) — Represents a Boolean filter criterion value. Applicable only when the field has a Boolean data type (checkbox field).
      - `SimpleFilterCriterionValueObjectRequest` — Represents a lookup object filter criterion value for request bodies, applicable when the field's data_type is lookup, ownerlookup, or userlookup. The ID property is required.
      - `SimpleFilterCriterionValueObjectPredefined` — Represents a predefined placeholder object filter criterion value for lookup fields, applicable with equal or not_equal comparators when the field's data_type is ownerlookup or userlookup. Two forms are supported: (1) the currently logged-in user, represented by passing only the name property with the predefined value ${CURRENTUSER} and no ID property; and (2) the logged-in user's role, represented by passing the ID property with the predefined value ${CURRENTUSERROLE} and an optional display label in the name property. For specific real users or roles that are not predefined, use SimpleFilterCriterionValueObjectRequest, which requires the ID property.
      - `SimpleFilterCriterionValueGeneralPredefined` (string) [enum=['${EMPTY}', '${NOTEMPTY}']] — Represents a predefined placeholder value applicable to any field data_type with the equal comparator.
Possible values:
${EMPTY} - Matches records where the field has no value.
${NOTEMPTY} - Matches records where the field has any non-empty value.
      - `SimpleFilterCriterionValueDateTimePredefined` (string) [enum=[22 values]] — Represents a predefined placeholder value applicable only when the field's data_type is date or datetime, with the equal comparator.
      - `SimpleFilterCriterionValueNDaysPredefined` (string) [maxLen=255, pattern=^\$\{(LAST_N_|NEXT_N_)(DAYS|WEEKS|MONTHS|YEARS):([0-9]+)\}$] — Represents a predefined N-period range placeholder value applicable only when the field's data_type is date or datetime, with the equal comparator. Follows the pattern ${NEXT_N_<PERIOD>:<n>} or ${LAST_N_<PERIOD>:<n>}, where PERIOD is DAYS, WEEKS, MONTHS, or YEARS and n is a positive integer. The current period is always excluded from the range.
      - `SimpleFilterCriterionValueAgeDuePredefined` (string) [maxLen=255, pattern=^\$\{(AGEINDAYS|DUEINDAYS)\}\+[0-9]+$] — Represents a predefined age or due-in-days placeholder value applicable only when the field's data_type is date or datetime. Follows the pattern ${AGEINDAYS}+<n> for records where the date field was exactly n days in the past, or ${DUEINDAYS}+<n> for records where the date field is exactly n days in the future. Supported comparators are equal, not_equal, less_than, greater_than, less_equal, and greater_equal.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
`EqualityFilterCriterionRequest`:
  oneOf:
    - `EqualFilterCriterionRequest` — Represents a filter criterion for the equal comparator. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime fields; SimpleFilterCriterionValueNumber for integer, currency, or double fields; SimpleFilterCriterionValueBoolean for Boolean fields; SimpleFilterCriterionValueObjectRequest for lookup, ownerlookup, or userlookup fields; and SimpleFilterCriterionValueObjectPredefined for predefined user or role object placeholders. Accepts scalar or array values. Resolve the data_type from the field's FieldSchema.
    - `NotEqualFilterCriterionRequest` — Represents a filter criterion for the not_equal comparator. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime fields; SimpleFilterCriterionValueNumber for integer, currency, or double fields; SimpleFilterCriterionValueBoolean for Boolean fields; SimpleFilterCriterionValueObjectRequest for lookup, ownerlookup, or userlookup fields; and SimpleFilterCriterionValueObjectPredefined for predefined user or role object placeholders.
`FilterFieldBase`:
  > Represents the base field reference used in filter operations, containing minimal required properties. The field's data_type is not part of this object; resolve it from the corresponding FieldSchema. For formula fields, use formula.return_type as the effective data_type; for rollup_summary fields, use rollup_summary.return_type.
  - `id` (string/int64) — Represents the unique ID of the field used for filter operations.
  - `api_name` (string) **REQ** — Represents the API name of the field used for filter application. Supports relationship notation, for example, Deals__r.Stage.
  additionalProperties: any
`GroupedFilterCriterionRequest`:
  > Represents a grouped filter criterion containing multiple filter conditions evaluated with a logical operator. Supports recursive nesting for complex filtering logic.
  - `group` (array of object) [minItems=2, maxItems=25] **REQ** — Contains an array of filter conditions grouped together and evaluated with the specified logical operator.
    oneOf:
      - `SimpleFilterCriterionRequest` — Represents a simple field-based filter criterion that dispatches to the appropriate comparator-specific schema. The equal and not_equal comparators support scalar or array values; text comparators support scalar or array strings; ordering comparators require a scalar; between and not_between comparators require a two-element array; in and not_in comparators require an array of primitives; and include_all, include_any, exclude_all, and exclude_any comparators require an array of lookup objects and apply only when the field's data_type is multiuserlookup or multiselectlookup.
      - `GroupedFilterCriterionRequest` — Represents a grouped filter criterion containing multiple filter conditions evaluated with a logical operator. Supports recursive nesting for complex filtering logic.
  - `group_operator` (string) **REQ** [enum=['AND', 'OR', 'and', 'or']] — Represents the logical operator applied between the filter conditions in the group.
Possible values:
AND - All conditions in the group must be satisfied.
OR - At least one condition in the group must be satisfied.
and - Equivalent to AND; all conditions in the group must be satisfied.
or - Equivalent to OR; at least one condition in the group must be satisfied.
`MultiSelectLookupFilterCriterionRequest`:
  > Represents a filter criterion for the include_all, include_any, exclude_all, and exclude_any comparators. Applicable only when the field's data_type is multiuserlookup or multiselectlookup. The value must be an array of SimpleFilterCriterionValueObjectRequest lookup objects.
  - `field` (object) **REQ** — Represents the target field definition to which the multi-select lookup filter criterion is applied. The field must have a data_type of multiuserlookup or multiselectlookup.
  - `comparator` (string) **REQ** [enum=['include_all', 'include_any', 'exclude_all', 'exclude_any']] — Represents the multi-select lookup comparison operator applied to the criterion. Applicable only when the field's data_type is multiuserlookup or multiselectlookup.
Possible values:
include_all - Matches records that include all specified lookup values.
include_any - Matches records that include at least one of the specified lookup values.
exclude_all - Matches records that exclude all specified lookup values.
exclude_any - Matches records that exclude at least one of the specified lookup values.
  - `value` (array of object `SimpleFilterCriterionValueObjectRequest`) [minItems=1, maxItems=5] **REQ** — Contains an array of lookup object references used in the multi-select comparison.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
`NotEqualFilterCriterionRequest`:
  > Represents a filter criterion for the not_equal comparator. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime fields; SimpleFilterCriterionValueNumber for integer, currency, or double fields; SimpleFilterCriterionValueBoolean for Boolean fields; SimpleFilterCriterionValueObjectRequest for lookup, ownerlookup, or userlookup fields; and SimpleFilterCriterionValueObjectPredefined for predefined user or role object placeholders.
  - `field` (object) **REQ** — Represents the target field definition to which the not-equal filter criterion is applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['not_equal']] — Represents the not-equal comparison operator applied to the criterion.
Possible values:
not_equal - Matches records where the field value does not equal the specified filter value.
  - `value` (object) **REQ** — Represents the filter value used in the not_equal comparator. Accepts a scalar or an array of values, depending on the field's data_type.
    anyOf:
        type: array of object [minItems=1, maxItems=500]
          oneOf:
            - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
            - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
              anyOf:
                - `SimpleFilterCriterionValueObjectRequest` — Represents a lookup object filter criterion value for request bodies, applicable when the field's data_type is lookup, ownerlookup, or userlookup. The ID property is required.
                - `SimpleFilterCriterionValueObjectPredefined` — Represents a predefined placeholder object filter criterion value for lookup fields, applicable with equal or not_equal comparators when the field's data_type is ownerlookup or userlookup. Two forms are supported: (1) the currently logged-in user, represented by passing only the name property with the predefined value ${CURRENTUSER} and no ID property; and (2) the logged-in user's role, represented by passing the ID property with the predefined value ${CURRENTUSERROLE} and an optional display label in the name property. For specific real users or roles that are not predefined, use SimpleFilterCriterionValueObjectRequest, which requires the ID property.
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
      - `SimpleFilterCriterionValueBoolean` (boolean) — Represents a Boolean filter criterion value. Applicable only when the field has a Boolean data type (checkbox field).
      - `SimpleFilterCriterionValueObjectRequest` — Represents a lookup object filter criterion value for request bodies, applicable when the field's data_type is lookup, ownerlookup, or userlookup. The ID property is required.
      - `SimpleFilterCriterionValueObjectPredefined` — Represents a predefined placeholder object filter criterion value for lookup fields, applicable with equal or not_equal comparators when the field's data_type is ownerlookup or userlookup. Two forms are supported: (1) the currently logged-in user, represented by passing only the name property with the predefined value ${CURRENTUSER} and no ID property; and (2) the logged-in user's role, represented by passing the ID property with the predefined value ${CURRENTUSERROLE} and an optional display label in the name property. For specific real users or roles that are not predefined, use SimpleFilterCriterionValueObjectRequest, which requires the ID property.
      - `SimpleFilterCriterionValueAgeDuePredefined` (string) [maxLen=255, pattern=^\$\{(AGEINDAYS|DUEINDAYS)\}\+[0-9]+$] — Represents a predefined age or due-in-days placeholder value applicable only when the field's data_type is date or datetime. Follows the pattern ${AGEINDAYS}+<n> for records where the date field was exactly n days in the past, or ${DUEINDAYS}+<n> for records where the date field is exactly n days in the future. Supported comparators are equal, not_equal, less_than, greater_than, less_equal, and greater_equal.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
`OrderingFilterCriterionRequest`:
  > Represents a filter criterion for the less_than, less_equal, greater_than, and greater_equal comparators. The value must be a scalar; arrays and objects are not supported. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for date or datetime fields, and SimpleFilterCriterionValueNumber for integer, currency, or double fields.
  - `field` (object) **REQ** — Represents the target field definition to which the ordering filter criterion is applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['less_than', 'less_equal', 'greater_than', 'greater_equal']] — Represents the ordering comparison operator applied to the criterion.
Possible values:
less_than - Matches records where the field value is less than the specified filter value.
less_equal - Matches records where the field value is less than or equal to the specified filter value.
greater_than - Matches records where the field value is greater than the specified filter value.
greater_equal - Matches records where the field value is greater than or equal to the specified filter value.
  - `value` (object) **REQ** — Represents the scalar filter value used in the ordering comparator. Arrays and objects are not supported for ordering comparators.
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
`ScoringRuleResponseDetails`:
  > Represents the per-item operation result for a Scoring Rule action, including status, code, and message.
  - `code` (string) [maxLen=255] — Represents the result code for this per-item Scoring Rule operation.
  - `details` (object `SuccessResponseDetails`) — Represents the details returned in a successful Scoring Rule operation, including the affected rule ID and any unsaved custom fields.
  - `message` (string) [maxLen=255] — Response message for the scoring rule operation
  - `status` (string) [maxLen=255] — Response status for the scoring rule operation
`SetFilterCriterionRequest`:
  > Represents a filter criterion for the in and not_in comparators. The value must be an array of primitive values. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for text-based types, and SimpleFilterCriterionValueNumber for integer, currency, or double fields.
  - `field` (object) **REQ** — Represents the target field definition to which the set filter criterion is applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['in', 'not_in']] — Represents the set membership comparison operator applied to the criterion.
Possible values:
in - Matches records where the field value is in the specified set of values.
not_in - Matches records where the field value is not in the specified set of values.
  - `value` (array of object) [minItems=1, maxItems=500] **REQ** — Contains an array of primitive filter values used in the set comparison.
    oneOf:
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
`SimpleFilterCriterionRequest`:
  oneOf:
    - `EqualityFilterCriterionRequest` — Represents an equality filter criterion that dispatches to either the EqualFilterCriterionRequest or NotEqualFilterCriterionRequest schema based on the comparator value.
    - `TextFilterCriterionRequest` — Represents a filter criterion for the like, not_like, starts_with, ends_with, contains, and not_contains comparators. The value must be a string scalar or array; use SimpleFilterCriterionValueString for text-based field types. Object and Boolean values are not supported. Resolve the data_type from the field's FieldSchema.
    - `OrderingFilterCriterionRequest` — Represents a filter criterion for the less_than, less_equal, greater_than, and greater_equal comparators. The value must be a scalar; arrays and objects are not supported. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for date or datetime fields, and SimpleFilterCriterionValueNumber for integer, currency, or double fields.
    - `BetweenFilterCriterionRequest` — Represents a filter criterion for the between and not_between comparators. The value must be an array of exactly two elements — [lower_bound, upper_bound]. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for date or datetime fields, and SimpleFilterCriterionValueNumber for integer, currency, or double fields. Resolve the data_type from the field's FieldSchema. For formula fields, use formula.return_type as the effective data_type; for rollup_summary fields, use rollup_summary.return_type.
    - `SetFilterCriterionRequest` — Represents a filter criterion for the in and not_in comparators. The value must be an array of primitive values. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for text-based types, and SimpleFilterCriterionValueNumber for integer, currency, or double fields.
    - `MultiSelectLookupFilterCriterionRequest` — Represents a filter criterion for the include_all, include_any, exclude_all, and exclude_any comparators. Applicable only when the field's data_type is multiuserlookup or multiselectlookup. The value must be an array of SimpleFilterCriterionValueObjectRequest lookup objects.
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
`SimpleFilterCriterionValueObjectRequest`:
  > Represents the base minified record structure of a lookup module, containing the record's unique identifier and display name.
  - `id` (object) **REQ**
  - `name` (string) [maxLen=255] — Represents the display name of the lookup module record.
  additionalProperties: any
`SuccessResponseDetails`:
  > Represents the details returned in a successful Scoring Rule operation, including the affected rule ID and any unsaved custom fields.
  - `unsaved_custom_fields` (array of object `UnsavedCustomFieldDetails`) [maxItems=6] — Represents an array of custom fields that could not be saved during the operation.
  - `id` (string) [maxLen=25] — Represents the unique ID of the Scoring Rule affected by the operation.
  additionalProperties: any
`TextFilterCriterionRequest`:
  > Represents a filter criterion for the like, not_like, starts_with, ends_with, contains, and not_contains comparators. The value must be a string scalar or array; use SimpleFilterCriterionValueString for text-based field types. Object and Boolean values are not supported. Resolve the data_type from the field's FieldSchema.
  - `field` (object) **REQ** — Represents the target field definition to which the text filter criterion is applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['like', 'not_like', 'starts_with', 'ends_with', 'contains', 'not_contains']] — Represents the text comparison operator applied to the criterion.
Possible values:
like - Matches records where the field value contains the specified pattern.
not_like - Matches records where the field value does not contain the specified pattern.
starts_with - Matches records where the field value begins with the specified string.
ends_with - Matches records where the field value ends with the specified string.
contains - Matches records where the field value contains the specified string.
not_contains - Matches records where the field value does not contain the specified string.
  - `value` (object) **REQ** — Represents the string filter value used in the text comparator. Accepts a scalar string or an array of string values.
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
`UnsavedCustomFieldDetails`:
  > Represents the details of a custom field that could not be saved during the operation.
  - `field_label` (string) [maxLen=100] — Represents the display name of the custom field that could not be saved.

**Request Body** — application/json `UpdateScoringRulesRequestBody`
> Accepts a JSON request body containing an array of Scoring Rule updates.
  > Request body for updating multiple scoring rules.
  - `scoring_rules` (array of object `ScoringRulePUT`) [minItems=1, maxItems=25] **REQ** — Array of scoring rule update objects (Required)
    schema: `ScoringRulePUT`
    - `custom_fields` (array of object `CustomFieldConfigurationPUT`) [maxItems=6, nullable] — Represents the custom fields can be configured for scoring rule. These fields will hold the referred scores.
      schema: `CustomFieldConfigurationPUT`
      - `id` (string) [maxLen=25] — Custom field id
      - `field_label` (string) [maxLen=100] — Name of the custom field
      - `api_name` (string) [maxLen=100] — Api name of the custom field
      - `reference_field` (object `ReferencedScoreField`) — It will hold the referenced score field info.
        schema: `ReferencedScoreField`
        - `api_name` (string) [enum=[6 values]] — Specifies the API name of the referenced score field. Required when creating a Scoring Rule.
        - `id` (string) [maxLen=25] — Represents the unique ID of the referenced score field.
        additionalProperties: any
      - `_delete` (null) — Set to null to delete the custom field
    - `description` (string) [maxLen=500, nullable] — Rule configuration info can be added here.
    - `active` (boolean) — It defined the status (active or inactive) of the rule.
    - `field_rules` (array of object `FieldScoreConfigurationRequest`) [maxItems=50] — Specifies an array of touch point score configurations, available for Leads and Contacts modules.
      schema: `FieldScoreConfigurationRequest`
      - `score` (integer/int32) — Specifies the score points to add when the criteria condition is met.
      - `id` (string) [maxLen=255] — Field rule ID
      - `criteria` (object `FilterCriterionRequest`) — Represents the top-level filter criterion for data selection, supporting both simple field-based filters and complex grouped filters with logical operators.
        oneOf:
          - `SimpleFilterCriterionRequest` — Represents a simple field-based filter criterion that dispatches to the appropriate comparator-specific schema. The equal and not_equal comparators support scalar or array values; text comparators support scalar or array strings; ordering comparators require a scalar; between and not_between comparators require a two-element array; in and not_in comparators require an array of primitives; and include_all, include_any, exclude_all, and exclude_any comparators require an array of lookup objects and apply only when the field's data_type is multiuserlookup or multiselectlookup.
          - `GroupedFilterCriterionRequest` — Represents a grouped filter criterion containing multiple filter conditions evaluated with a logical operator. Supports recursive nesting for complex filtering logic.
    - `name` (string) [maxLen=25] — Scoring rule name. Must be unique within the organization. It cannot contain special characters: ` ~ # % ^ & * ( ) + = " ; < > [ ] { } | \
    - `signal_rules` (array of object `TouchPointScoreConfiguration`) [maxItems=250, nullable] — Represents the touch points based score configurations and is applicable only for Leads and Contacts modules
      schema: `TouchPointScoreConfiguration`
      - `score` (integer/int32) — Points that should be added for the signal (Required for CREATE)
      - `id` (string) [maxLen=25] — Signal rule primary key
      - `_delete` (null) — used to delete the signal rule
      - `signal` (object `SignalInformation`) — Touch point signal info (Required for CREATE)
        schema: `SignalInformation`
        - `namespace` (string) [maxLen=255] — Signal namespace
        - `id` (string) [maxLen=25] — Signal id
    - `id` (string) [maxLen=255] — Represents the Scoring rule id
    additionalProperties: any

**Responses:**

- **200**: Rules updated successfully — Schema: `ScoringRulesPutSuccessResponse` [application/json]
    schema: `ScoringRulesPutSuccessResponse`
    - `scoring_rules` (array of object `ScoringRuleResponseDetails`) [maxItems=20] — Update results for all requested scoring rules.

- **207**: Few rule object has errors, others are updated successfully. — Schema: `PutScoringRulesPartialSuccessResponse` [application/json]
    > Represents the multi-status response body for the bulk update Scoring Rules operation when some items succeed and others fail.
    schema: `PutScoringRulesPartialSuccessResponse`
    - `scoring_rules` (array of object `ScoringRuleResponseDetails`) [maxItems=300] — Represents an array of per-item operation statuses for the multi-status Scoring Rule operation.

- **400**: Returns an error response when the request contains invalid or missing data.
**Resolution:** Verify that all field values are valid and required fields are present. [application/json]
    > Represents the wrapped error response containing per-item error objects for the update Scoring Rules operation.
    - `scoring_rules` (array of object `GeneralErrorResponse`) [maxItems=25] **REQ** — Represents an array of per-item error objects in the update Scoring Rules error response.
      schema: `GeneralErrorResponse`
      - `code` (string) [maxLen=255] — Represents the error code for this error response.
      - `details` (object) — Represents additional details about the validation error.
        - `api_name` (string) [maxLen=255] — Represents the API name of the field that caused the error.
        - `json_path` (string) [maxLen=1000] — Represents the JSON path of the field that caused the error.
        additionalProperties: any
      - `message` (string) [maxLen=1000] — Represents the error message describing the issue.
      - `status` (string) [enum=['error']] — Represents the status of the error response. The value is always **error**.
      additionalProperties: any

**Scopes:** ZohoCRM.settings.scoring_rules.UPDATE
