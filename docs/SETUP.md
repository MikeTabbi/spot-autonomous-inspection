# Setup Guide

## Prerequisites

- Ubuntu 22.04 LTS (or macOS for development)
- Python 3.10+
- Access to Boston Dynamics Spot robot
- Spot SDK credentials

## Installation

### 1. Clone Repository
```bash
git clone https://github.com/MikeTabbi/spot-autonomous-inspection.git
cd spot-autonomous-inspection
```

### 2. Install Dependencies
```bash
# Install Spot SDK
pip3 install bosdyn-client bosdyn-api bosdyn-mission

# Install Computer Vision libraries
pip3 install opencv-python ultralytics torch torchvision

# Install web framework (for dashboard)
pip3 install fastapi uvicorn
```

### 3. Configure Spot Connection
```bash
# Create config file (coming soon)
cp config.example.yaml config.yaml

# Edit with your Spot credentials
nano config.yaml
```

## Quick Start

Documentation will be added as development progresses.

## Troubleshooting

Common issues and solutions will be documented here as they arise.

---

**Last Updated:** December 2025