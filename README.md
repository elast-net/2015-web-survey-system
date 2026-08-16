# Custom Web Survey & Data Processing System

**2015–2017 · Python, HTML5, CSS3, JavaScript, XML, XSLT, Bash, Apache**

Custom production web application for a highly specialized questionnaire workflow, developed end-to-end from frontend and backend to data processing, administration and deployment automation.

> **Source code:** Not publicly available. This repository documents the architecture and selected implementation details of the original system.

## Overview

The system combined an interactive web questionnaire with custom data processing and reporting.

Key requirements included:

* dynamic interaction without full-page reloads,
* JSON/AJAX communication with a Python backend,
* operation without JavaScript,
* XML and RSS generation,
* live administration statistics,
* automated frontend optimization,
* separation of source and production assets.

```text id="2x8c5m"
                     ┌──────────────┐
                     │    Browser   │
                     └──────┬───────┘
                            │
                 AJAX/JSON  │  HTTP POST
                            │
                            ▼
                    ┌──────────────┐
                    │ Python / CGI │
                    └──────┬───────┘
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
     Data processing   XML / RSS        Logging &
       & storage       generation       statistics
```

## Dual Request Model

The application supported both an interactive AJAX mode and a conventional server-rendered fallback.

```text id="y4x2zq"
JavaScript enabled
       │
       ▼
   AJAX / JSON
       │
       ▼
Partial page update


JavaScript disabled
       │
       ▼
    HTTP POST
       │
       ▼
Full HTML response
```

The same backend processing was used in both paths.

A simplified version of the AJAX response:

```python id="zq7m1p"
if ajax_enabled:
    data = {
        'js': '<script>' + javascript + '</script>',
        'html': html
    }

    print 'Content-Type: application/json\n'
    print json.dumps(data)
```

This allowed the frontend to update selected parts of the questionnaire while retaining a functional non-JavaScript path.

## Source / Production Asset Separation

Frontend source files were processed into optimized production versions. At runtime, the application preferred the generated version and automatically fell back to the source file when necessary.

```python id="m8k3rt"
for filename in source_files:
    optimized = optimized_dir + filename
    source = source_dir + filename

    files[filename] = (
        optimized if os.path.isfile(optimized) else source
    )
```

This created a simple separation between:

```text id="b6n4vx"
Readable source
      │
      ▼
 automated processing
      │
      ▼
Optimized production assets
```

The original processing pipeline packaged frontend files, sent them to an external minification service, received the processed archive and deployed the resulting files.

## Data Processing

Survey submissions were normalized and converted into structured XML data.

Selected data was additionally published through RSS.

The application separated data generation from presentation, allowing the same processed data to be consumed by administration and reporting tools.

A lightweight intermediate representation was used for selected XML structures to reduce repeated processing.

## Administration & Monitoring

The system included dedicated administration and reporting tools.

Runtime statistics recorded information such as:

* request type,
* execution time,
* client information,
* requested URI,
* referrer,
* user agent.

Execution time was measured directly within the application:

```python id="v2r6hs"
start = int(round(time.time() * 1000))

# application processing

end = int(round(time.time() * 1000))
elapsed = end - start
```

The resulting records were stored for later analysis.

## Other Implementation Details

The application also included:

* responsive layout using CSS media queries,
* CSS/JavaScript/HTML minification,
* optimized static asset delivery,
* legacy browser compatibility,
* simplified presentation without CSS,
* Bash-based supporting automation,
* modular Python components,
* XSLT-based reporting tools.

## Project Structure

```text id="p7t3kw"
survey/
├── incl/       # reusable application modules
├── src/        # source HTML, CSS and JavaScript
├── obf/        # generated / optimized assets
├── rss/        # RSS-related data
├── out/        # processed data / storage
├── log/        # application and statistics logs
└── adm/        # administration and reporting
```

## Codebase

Approximate source statistics from the original implementation:

| Component  |        LOC |
| ---------- | ---------: |
| Python     |     ~1,200 |
| HTML       |       ~400 |
| CSS        |       ~350 |
| XSLT       |       ~200 |
| JavaScript |       ~150 |
| **Total**  | **~2,300** |

## Historical Context

Originally developed in **2015** and maintained until **2017**.

The implementation reflects the web environment of that period, including Python 2, CGI and legacy browser compatibility requirements.

The project is presented as an example of **end-to-end system design, data processing, automation and integration**, rather than as a modern web-development stack.

## What the Project Demonstrates

* End-to-end production system development
* Python backend development
* AJAX / JSON integration
* Data processing and XML generation
* RSS publishing
* Automated asset processing
* Logging and runtime monitoring
* Source/production environment separation
* Administration and reporting
* Practical engineering under compatibility and deployment constraints

**Status:** Historical production project · source code not publicly available
