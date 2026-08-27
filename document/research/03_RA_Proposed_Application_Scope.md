# Proposed Application — Scope and Feature List

## Introduction

**Purpose.** This document outlines the scope of the proposed application as a list of proposed features, grouped by category. Each feature is briefly explained.

**Scope.** This document lists proposed features only, as input to requirement analysis. It does not analyze feasibility, does not evaluate alternatives, does not map features to specific technologies or vendors, and does not commit to final requirements. Unlike other documents in this research series, it describes the project's own proposed application rather than external market findings; no external sources are cited.

---

## 1. UI Features

- **Web-based application.** Accessed through a browser; no dedicated desktop client required.
- **Drag-and-drop plan/work-process builder.** User creates production plans and work processes visually, without writing code or configuration files.
- **No-code data configuration.** User configures data types and data sources through the UI, without needing knowledge of the underlying communication technology or protocol.
- **Live data view.** UI reflects incoming data as it updates, rather than only on manual refresh.
- **Manual data input.** User can enter data directly through the UI, as an alternative to automated collection.

## 2. Infrastructure

- **On-premise deployment.** Application is deployed on a server located within the factory, not on external/public cloud infrastructure.
- **Machine connectivity layer.** Provides the communication means to connect to factory machines and collect data from them.
- **Multiple data-source channels.** Ingests data from varied sources: worker check-in/login devices (e.g. over Wi-Fi), production-line cameras capturing images of produced parts (possible deferred milestone), machine sensors, and file uploads.
- **Multi-format data support.** Accepts data in multiple formats: CSV, Excel, JSON, and possibly video/image.
- **Local data storage.** Collected and normalized data is stored on the local, secured server rather than an external service.
- **Offline operation.** Application and its data pipeline function without a connection to the outside internet.

## 3. Business Logic

- **Data normalization pipeline.** Incoming data, regardless of source or format, is normalized into a consistent form before storage.
- **Reporting.** Generates reports from stored data.
- **Prediction.** Produces predictive outputs (e.g. forecasts) from stored data.
- **Model selection.** More than one machine-learning model type is available depending on the data type involved; the user can select a model, or the application can select the best-performing one automatically.

## 4. Security Logics

- **Secured local server.** Server and stored data reside within the factory's own secured environment.
- **Secure connections.** Communication between machines, users, and the server is secured.
- **Fully offline, no external reachability.** The application does not require, and does not allow, an outbound connection to the public internet.

## 5. AI Features

- **Multiple model types.** Different machine-learning model types are applied depending on the type of data being analyzed (e.g. tabular, time-series, image).
- **Model selection.** User can choose a specific model, or let the application select the best-fitting model.
- **Prediction capability.** Trained models produce predictions from stored data.
- **Offline inference.** AI models run entirely on the local server, independent of any internet connection.
