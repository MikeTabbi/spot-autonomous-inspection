# System Architecture

## Overview

The Spot Autonomous Inspection System consists of four main components working together to enable fully autonomous facility inspection.

## High-Level Architecture
```
┌─────────────────────────────────────┐
│    Mission Control Dashboard        │
│         (React.js)                  │
└──────────────┬──────────────────────┘
               │ REST API / WebSocket
┌──────────────┴──────────────────────┐
│     Autonomous Agent (Python)       │
│  ┌────────────────────────────┐    │
│  │  Navigation Controller      │    │
│  │  • GraphNav SLAM           │    │
│  │  • Path Planning           │    │
│  └────────────────────────────┘    │
│  ┌────────────────────────────┐    │
│  │  AI Vision System          │    │
│  │  • YOLOv8 Detection        │    │
│  │  • Anomaly Recognition     │    │
│  └────────────────────────────┘    │
│  ┌────────────────────────────┐    │
│  │  Decision Engine           │    │
│  │  • State Machine           │    │
│  │  • Priority Management     │    │
│  └────────────────────────────┘    │
└──────────────┬──────────────────────┘
               │ Spot SDK
┌──────────────┴──────────────────────┐
│    Boston Dynamics Spot Robot       │
└─────────────────────────────────────┘
```

## Component Details

### 1. Navigation Controller
- Utilizes Spot's GraphNav for localization and mapping
- Waypoint-based autonomous navigation
- Dynamic obstacle avoidance

### 2. AI Vision System
- Real-time object detection using YOLOv8
- Processes camera feeds at 10-15 FPS
- Detects: fire extinguishers, gauges, spills, obstructions, damage

### 3. Decision Engine
- Finite state machine: PATROLLING → INVESTIGATING → REPORTING
- Autonomous priority-based task management
- Battery monitoring and safety protocols

### 4. Mission Control Dashboard
- Web-based interface for mission planning
- Real-time telemetry and video streaming
- Inspection report viewing and export

## Data Flow

1. User initiates mission via dashboard
2. Navigation controller executes waypoint sequence
3. Vision system continuously processes camera feeds
4. Detection results feed into decision engine
5. Decision engine adjusts robot behavior autonomously
6. Findings logged and compiled into report
7. Report displayed in dashboard upon mission completion

## Technology Stack

- **Robot Control:** Spot SDK (Python)
- **AI/ML:** YOLOv8, PyTorch, OpenCV
- **Backend:** FastAPI, Python 3.10+
- **Frontend:** React.js, WebSocket
- **Data Storage:** JSON logs, SQLite (planned)

---

**Note:** This architecture will evolve as development progresses.

**Last Updated:** December 2025