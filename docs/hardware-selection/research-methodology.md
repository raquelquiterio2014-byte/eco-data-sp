# Research Methodology

## Objective
The V5.2 Hardware Selection Study converts the generic instrumentation categories introduced in V5.1 into an evidence-backed commercial candidate shortlist.

The study is intentionally a **pre-selection study**, not procurement engineering.

## Source policy
Only official manufacturer pages, manuals, datasheets, product-information systems and manufacturer-hosted technical documents are used as evidence for the shortlist.

Third-party marketplaces, distributor specifications, blogs, forums and AI-generated specifications are not accepted as authoritative evidence.

## Inclusion criteria
A candidate is included when it satisfies all of the following:

1. **Measurement compatibility** — it measures at least one physical variable required by Eco Data SP.
2. **Industrial applicability** — manufacturer documentation positions the instrument for industrial, commercial, utility or water-network measurement.
3. **Documented measurement characteristics** — the manufacturer publishes relevant range, accuracy/class or configuration information.
4. **Digital integration path** — the product family provides an industrial communication mechanism such as Modbus RTU/TCP, industrial Ethernet, pulse output or an IoT/gateway path.
5. **Traceability** — manufacturer, family/model and official evidence can be stored with the software candidate record.
6. **Architecture relevance** — the instrument helps evaluate a design decision already present in Eco Data SP.

## Exclusion criteria
A product is not promoted to the shortlist when:
- its technical claims cannot be verified from an official manufacturer source;
- it measures a variable outside the current V5.2 scope;
- its integration path cannot yet be explained at architecture level;
- only price or marketplace information is available;
- it would require inventing installation parameters that are not known.

## Evaluation fields
Each candidate is recorded using:
- Domain
- Manufacturer
- Model/family
- Instrument type
- Measured variables
- Measurement range
- Accuracy or accuracy class
- Communication / output
- Intended application
- Possible Eco Data SP integration path
- Official source
- Evidence note
- Candidate status

## No-price rule
Price is deliberately excluded. V5.2 studies technical suitability and integration evidence, not procurement economics.

## Selection logic
The study does not calculate a single numerical winner. At this stage, a weighted score would imply certainty about deployment requirements that do not yet exist.

The workflow is therefore:

**Requirements → Official Manufacturer Research → Candidate Shortlist → Technical Comparison → Integration Analysis → Deployment-Specific Engineering → Final Selection**

## Evidence date
Research consolidated for Eco Data SP V5.2 in October 2026. Manufacturer documentation may change; specifications must be re-verified before any real deployment.
