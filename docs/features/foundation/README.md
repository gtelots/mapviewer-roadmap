# Foundation Features

> Infrastructure and low-level platform features

## Overview

Foundation features provide **infrastructure** for other features. These are technical, low-level features that enable higher-level functionality.

**Total**: 6 feature groups, ~270 features

---

## Feature Groups

| Feature Group | Features | Description |
|---------------|----------|-------------|
| [3D Tiles Streaming](3d-tiles-streaming.md) | 50 | 3D tile streaming infrastructure |
| [App Shell](app-shell.md) | 80 | Application shell & lifecycle |
| [Interaction & Identify](interaction-identify.md) | 20 | Feature interaction system |
| [Scene & Camera](scene-camera.md) | 80 | Scene & camera control system |

---

## Characteristics

- **Technical** - Implementation-focused features
- **Infrastructure** - Enables other features to work
- **Reusable** - Used by multiple feature groups
- **Low-level** - Close to rendering/engine layer

---

## Implementation Priority

**Phase 1** - Foundation features should be implemented early as dependencies.

**Note**: Some foundation features may be split across multiple files due to extraction from the original foundation-features.md file.

---

**Category**: Foundation  
**Priority**: High  
**Status**: Required infrastructure
