# Foundation Features
> Advanced features and implementation details for foundation features.

| Feature Group | Feature Name | Short Description | Detailed Description | Why This Feature is Needed | Implementation Phase |
|--------------|--------------|------------|----------------|---------------------------|---------------------|
| 3D Scene & 3D Tiles | 3D Mode Toggle | Chuyển 2D↔3D mượt | Chuyển 2D↔3D mượt | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| 3D Scene & 3D Tiles | 3D Tileset Loader | Tải tileset 3D Tiles theo ID/URL | Tải tileset 3D Tiles theo ID/URL | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| 3D Scene & 3D Tiles | 3D Feature Picking | Click đối tượng 3D để nhận diện/thông tin | Click đối tượng 3D để nhận diện/thông tin | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| 3D Scene & 3D Tiles | 3D Tiles Cache Control | Quản lý cache tile (kích thước, eviction). | Quản lý cache tile (kích thước, eviction). | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Core | Deep link boostrap | Khởi tạo trạng thái Viewer từ URL (camera, layers, tools,. | Khởi tạo trạng thái Viewer từ URL (camera, layers, tools,...) | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Core | Config remote fetch | Lấy cấu hình viewer từ dịch vụ cấu hình (remote config) | Lấy cấu hình viewer từ dịch vụ cấu hình (remote config) | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Core | Startup State Presets | Áp dụng trạng thái khởi động mặc định: camera, layer, UI | Áp dụng trạng thái khởi động mặc định: camera, layer, UI | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Core | State Persistence | Lưu trạng thái gần nhất (chế độ xem vệ tinh, light mode,. | Lưu trạng thái gần nhất (chế độ xem vệ tinh, light mode,...) hoặc đang thao tác -> URL Hash | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Core | Feature flags | Bật/tắt tính năng bằng cờ cấu hình | Bật/tắt tính năng bằng cờ cấu hình | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | 3D Tileset Loader | Tính năng 3d tileset loader | Tính năng 3d tileset loader | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | LOD Selection | Tính năng lod selection | Tính năng lod selection | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Frustum Culling | Tính năng frustum culling | Tính năng frustum culling | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Occlusion Culling Basic | Tính năng occlusion culling basic | Tính năng occlusion culling basic | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tile Cache (Memory) | Tính năng tile cache (memory) | Tính năng tile cache (memory) | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tile Cache (Disk) | Tính năng tile cache (disk) | Tính năng tile cache (disk) | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Request Concurrency Limit | Tính năng request concurrency limit | Tính năng request concurrency limit | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Request Priority Queue | Tính năng request priority queue | Tính năng request priority queue | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Progressive Refinement | Tính năng progressive refinement | Tính năng progressive refinement | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tile Loading Indicator | Tính năng tile loading indicator | Tính năng tile loading indicator | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tileset Bounds Visualization | Tính năng tileset bounds visualization | Tính năng tileset bounds visualization | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tile Error Handling | Tính năng tile error handling | Tính năng tile error handling | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tile Retry with Backoff | Tính năng tile retry with backoff | Tính năng tile retry with backoff | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Gzip/Brotli Support | Tính năng gzip/brotli support | Tính năng gzip/brotli support | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Draco/meshopt Decode | Tính năng draco/meshopt decode | Tính năng draco/meshopt decode | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | KTX2/Basis Texture | Tính năng ktx2/basis texture | Tính năng ktx2/basis texture | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tile Content Type Support | Tính năng tile content type support | Tính năng tile content type support | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Point Cloud Rendering Basic | Tính năng point cloud rendering basic | Tính năng point cloud rendering basic | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Instanced Models Basic | Tính năng instanced models basic | Tính năng instanced models basic | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tile Material Pipeline | Tính năng tile material pipeline | Tính năng tile material pipeline | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Lighting per Tileset | Tính năng lighting per tileset | Tính năng lighting per tileset | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tileset Clipping Planes | Tính năng tileset clipping planes | Tính năng tileset clipping planes | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tileset Transforms | Tính năng tileset transforms | Tính năng tileset transforms | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tileset Height Correction | Tính năng tileset height correction | Tính năng tileset height correction | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tileset Shadow Receiver/ കാസter | Tính năng tileset shadow receiver/ കാസter | Tính năng tileset shadow receiver/ കാസter | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tileset Picking Enable | Tính năng tileset picking enable | Tính năng tileset picking enable | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tileset Feature Metadata Support | Tính năng tileset feature metadata support | Tính năng tileset feature metadata support | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tileset Style by Metadata | Tính năng tileset style by metadata | Tính năng tileset style by metadata | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tileset Temporal Loading Guard | Tính năng tileset temporal loading guard | Tính năng tileset temporal loading guard | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tile Unload Policy | Tính năng tile unload policy | Tính năng tile unload policy | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Memory Budget Manager | Tính năng memory budget manager | Tính năng memory budget manager | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tile Request Cancellation | Tính năng tile request cancellation | Tính năng tile request cancellation | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | HTTP/2 Friendly Batching | Tính năng http/2 friendly batching | Tính năng http/2 friendly batching | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | CDN Cache Key Strategy | Tính năng cdn cache key strategy | Tính năng cdn cache key strategy | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Signed URL Support | Tính năng signed url support | Tính năng signed url support | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tileset Multi-Origin Support | Tính năng tileset multi-origin support | Tính năng tileset multi-origin support | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tileset Prewarming | Tính năng tileset prewarming | Tính năng tileset prewarming | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tileset Streaming Metrics | Tính năng tileset streaming metrics | Tính năng tileset streaming metrics | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tileset Fallback LOD | Tính năng tileset fallback lod | Tính năng tileset fallback lod | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tileset Versioned Manifest | Tính năng tileset versioned manifest | Tính năng tileset versioned manifest | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Multi-Tileset Orchestrator | Tính năng multi-tileset orchestrator | Tính năng multi-tileset orchestrator | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tileset Dependency Graph | Tính năng tileset dependency graph | Tính năng tileset dependency graph | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tileset Region-of-Interest | Tính năng tileset region-of-interest | Tính năng tileset region-of-interest | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tileset Throttling on Tab Hidden | Tính năng tileset throttling on tab hidden | Tính năng tileset throttling on tab hidden | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Background Decode Worker | Tính năng background decode worker | Tính năng background decode worker | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | GPU Instancing Optimization | Tính năng gpu instancing optimization | Tính năng gpu instancing optimization | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tile Hotspot Detection | Tính năng tile hotspot detection | Tính năng tile hotspot detection | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tile Integrity Check | Tính năng tile integrity check | Tính năng tile integrity check | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tile Progressive Texture | Tính năng tile progressive texture | Tính năng tile progressive texture | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Multi-Resolution Terrain Tiles | Tính năng multi-resolution terrain tiles | Tính năng multi-resolution terrain tiles | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | App Init Config | Tính năng app init config | Tính năng app init config | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Environment Profiles | Tính năng environment profiles | Tính năng environment profiles | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Responsive Layout Engine | Tính năng responsive layout engine | Tính năng responsive layout engine | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | App State Store | Tính năng app state store | Tính năng app state store | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Deep Link Router | Tính năng deep link router | Tính năng deep link router | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Session Persistence | Tính năng session persistence | Tính năng session persistence | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Feature Flags | Tính năng feature flags | Tính năng feature flags | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Theme System | Tính năng theme system | Tính năng theme system | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Keyboard Shortcuts Core | Tính năng keyboard shortcuts core | Tính năng keyboard shortcuts core | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Help & Onboarding | Tính năng help & onboarding | Tính năng help & onboarding | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Error Boundary UI | Tính năng error boundary ui | Tính năng error boundary ui | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Loading Skeleton | Tính năng loading skeleton | Tính năng loading skeleton | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Network Retry Policy | Tính năng network retry policy | Tính năng network retry policy | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Offline Detection | Tính năng offline detection | Tính năng offline detection | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Telemetry Consent | Tính năng telemetry consent | Tính năng telemetry consent | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Basic Audit Trail (Client) | Tính năng basic audit trail (client) | Tính năng basic audit trail (client) | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Resource Preload | Tính năng resource preload | Tính năng resource preload | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | CDN Asset Support | Tính năng cdn asset support | Tính năng cdn asset support | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Multi-Tab Safety | Tính năng multi-tab safety | Tính năng multi-tab safety | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Localization Bootstrap | Tính năng localization bootstrap | Tính năng localization bootstrap | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Date/Time Utilities | Tính năng date/time utilities | Tính năng date/time utilities | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Permission Gate UI | Tính năng permission gate ui | Tính năng permission gate ui | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Rate Limit Friendly UI | Tính năng rate limit friendly ui | Tính năng rate limit friendly ui | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Client Cache Control | Tính năng client cache control | Tính năng client cache control | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Config Validation | Tính năng config validation | Tính năng config validation | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Dependency Health Check | Tính năng dependency health check | Tính năng dependency health check | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Security Headers Readiness | Tính năng bảo mật và kiểm soát truy cập | Tính năng bảo mật và kiểm soát truy cập | Tăng cường bảo mật và tuân thủ quy định | Phase 1 |
| Foundation - App Shell | CORS Preflight Optimizer | Tính năng cors preflight optimizer | Tính năng cors preflight optimizer | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Version Badge & Build Info | Tính năng version badge & build info | Tính năng version badge & build info | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Changelog Notifier | Tính năng changelog notifier | Tính năng changelog notifier | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | API Key Input Modes | Tính năng api key input modes | Tính năng api key input modes | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Token Refresh Hook | Tính năng token refresh hook | Tính năng token refresh hook | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Secure Storage Wrapper | Tính năng secure storage wrapper | Tính năng secure storage wrapper | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Content Sanitization | Tính năng content sanitization | Tính năng content sanitization | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Crash Recovery Mode | Tính năng crash recovery mode | Tính năng crash recovery mode | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Config Override UI UI | Tính năng config override ui ui | Tính năng config override ui ui | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Startup Performance Budget | Tính năng startup performance budget | Tính năng startup performance budget | Cải thiện hiệu suất và trải nghiệm người dùng | Phase 1 |
| Foundation - App Shell | Accessibility Baseline | Tính năng accessibility baseline | Tính năng accessibility baseline | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Cookie/Storage Policy Banner | Tính năng cookie/storage policy banner | Tính năng cookie/storage policy banner | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Multi-Project Switcher | Tính năng multi-project switcher | Tính năng multi-project switcher | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Interaction & Identify | Click Select Basics | Tính năng click select basics | Tính năng click select basics | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Interaction & Identify | Hover Highlight | Tính năng hover highlight | Tính năng hover highlight | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Interaction & Identify | Properties Panel | Tính năng properties panel | Tính năng properties panel | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Interaction & Identify | Attribute Formatting | Tính năng attribute formatting | Tính năng attribute formatting | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Interaction & Identify | Copy Attribute | Tính năng copy attribute | Tính năng copy attribute | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Interaction & Identify | Feature Locate Button | Tính năng feature locate button | Tính năng feature locate button | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Interaction & Identify | Multi-Select Mode | Tính năng multi-select mode | Tính năng multi-select mode | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Interaction & Identify | Selection Set Save | Tính năng selection set save | Tính năng selection set save | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Interaction & Identify | Identify Across Layers | Quản lý và điều khiển identify across layers | Quản lý và điều khiển identify across layers | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Interaction & Identify | Pixel/World Tolerance Control | Tính năng pixel/world tolerance control | Tính năng pixel/world tolerance control | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Orbit | Điều khiển camera cho camera orbit | Điều khiển camera cho camera orbit | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Pan | Điều khiển camera cho camera pan | Điều khiển camera cho camera pan | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Zoom | Điều khiển camera cho camera zoom | Điều khiển camera cho camera zoom | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Fly-To Position | Tính năng fly-to position | Tính năng fly-to position | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Home View | Tính năng home view | Tính năng home view | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Compass Widget | Tính năng compass widget | Tính năng compass widget | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Pitch Controls | Tính năng pitch controls | Tính năng pitch controls | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Inertia | Điều khiển camera cho camera inertia | Điều khiển camera cho camera inertia | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Collision | Điều khiển camera cho camera collision | Điều khiển camera cho camera collision | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Globe/Plane Mode | Tính năng globe/plane mode | Tính năng globe/plane mode | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Coordinate Display | Tính năng coordinate display | Tính năng coordinate display | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Scale Bar | Tính năng scale bar | Tính năng scale bar | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Minimap (Optional) | Tính năng minimap (optional) | Tính năng minimap (optional) | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | North Lock Option | Tính năng north lock option | Tính năng north lock option | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Bookmarks | Điều khiển camera cho camera bookmarks | Điều khiển camera cho camera bookmarks | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Transition Presets | Điều khiển camera cho camera transition presets | Điều khiển camera cho camera transition presets | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Path Recording | Điều khiển camera cho camera path recording | Điều khiển camera cho camera path recording | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Path Playback | Điều khiển camera cho camera path playback | Điều khiển camera cho camera path playback | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Sync Multi-Views | Điều khiển camera cho camera sync multi-views | Điều khiển camera cho camera sync multi-views | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Split Screen Compare | Tính năng split screen compare | Tính năng split screen compare | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Field of View Control | Tính năng field of view control | Tính năng field of view control | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Near/Far Plane Tuning | Tính năng near/far plane tuning | Tính năng near/far plane tuning | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Auto-Exposure (Basic) | Tính năng auto-exposure (basic) | Tính năng auto-exposure (basic) | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Frame Rate Cap | Tính năng frame rate cap | Tính năng frame rate cap | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Constraints by Area | Điều khiển camera cho camera constraints by area | Điều khiển camera cho camera constraints by area | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Terrain Exaggeration | Tính năng terrain exaggeration | Tính năng terrain exaggeration | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Terrain Toggle | Tính năng terrain toggle | Tính năng terrain toggle | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Height Reference Modes | Tính năng height reference modes | Tính năng height reference modes | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Sun & Time-of-Day Basic | Tính năng sun & time-of-day basic | Tính năng sun & time-of-day basic | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Shadow Toggle | Tính năng shadow toggle | Tính năng shadow toggle | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Fog Control | Tính năng fog control | Tính năng fog control | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Atmosphere Toggle | Tính năng atmosphere toggle | Tính năng atmosphere toggle | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Ground Transparency | Tính năng ground transparency | Tính năng ground transparency | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Reset Orientation | Điều khiển camera cho camera reset orientation | Điều khiển camera cho camera reset orientation | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Jump to Coordinates | Tính năng jump to coordinates | Tính năng jump to coordinates | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Speed Control | Điều khiển camera cho camera speed control | Điều khiển camera cho camera speed control | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Touch Gesture Support | Tính năng touch gesture support | Tính năng touch gesture support | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Double-Click FlyTo | Tính năng double-click flyto | Tính năng double-click flyto | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Focus on Selection | Điều khiển camera cho camera focus on selection | Điều khiển camera cho camera focus on selection | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Auto-LOD Targeting | Tính năng auto-lod targeting | Tính năng auto-lod targeting | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Shake Guard | Điều khiển camera cho camera shake guard | Điều khiển camera cho camera shake guard | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | High Precision Mode | Tính năng high precision mode | Tính năng high precision mode | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Device Pixel Ratio Control | Tính năng device pixel ratio control | Tính năng device pixel ratio control | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Screenshot Viewport Safe Area | Tính năng screenshot viewport safe area | Tính năng screenshot viewport safe area | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Presets by Role | Điều khiển camera cho camera presets by role | Điều khiển camera cho camera presets by role | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Kiosk Auto-Rotate | Tính năng kiosk auto-rotate | Tính năng kiosk auto-rotate | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Multi-Monitor Support | Tính năng multi-monitor support | Tính năng multi-monitor support | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | VRAM Budget Indicator | Tính năng vram budget indicator | Tính năng vram budget indicator | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Roll Lock | Điều khiển camera cho camera roll lock | Điều khiển camera cho camera roll lock | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Smooth Stop | Điều khiển camera cho camera smooth stop | Điều khiển camera cho camera smooth stop | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Adaptive Input Sensitivity | Tính năng adaptive input sensitivity | Tính năng adaptive input sensitivity | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Teleport Mode | Điều khiển camera cho camera teleport mode | Điều khiển camera cho camera teleport mode | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Follow Object | Điều khiển camera cho camera follow object | Điều khiển camera cho camera follow object | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera LookAt Lock | Điều khiển camera cho camera lookat lock | Điều khiển camera cho camera lookat lock | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Safe Height Floor | Điều khiển camera cho camera safe height floor | Điều khiển camera cho camera safe height floor | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Navigation History | Điều khiển camera cho camera navigation history | Điều khiển camera cho camera navigation history | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Jump List | Điều khiển camera cho camera jump list | Điều khiển camera cho camera jump list | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Metrics Overlay | Điều khiển camera cho camera metrics overlay | Điều khiển camera cho camera metrics overlay | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera API Surface | Điều khiển camera cho camera api surface | Điều khiển camera cho camera api surface | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Events | Điều khiển camera cho camera events | Điều khiển camera cho camera events | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | View Frustum Debug | Tính năng view frustum debug | Tính năng view frustum debug | Hỗ trợ troubleshooting và phân tích vấn đề | Phase 1 |
| Foundation - Scene & Camera | Ground Clamp Sampling Mode | Tính năng ground clamp sampling mode | Tính năng ground clamp sampling mode | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Transition Interruptability | Tính năng transition interruptability | Tính năng transition interruptability | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Auto-Focus on Search | Điều khiển camera cho camera auto-focus on search | Điều khiển camera cho camera auto-focus on search | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Precision Cursor Height | Tính năng precision cursor height | Tính năng precision cursor height | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Scene Screenshot Thumbnail | Tính năng scene screenshot thumbnail | Tính năng scene screenshot thumbnail | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Cinematic DOF (Basic) | Tính năng cinematic dof (basic) | Tính năng cinematic dof (basic) | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Anti-Aliasing Toggle | Tính năng anti-aliasing toggle | Tính năng anti-aliasing toggle | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Anisotropic Filtering Level | Tính năng anisotropic filtering level | Tính năng anisotropic filtering level | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Screenshot at Resolution | Tính năng screenshot at resolution | Tính năng screenshot at resolution | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Tutorial Mode | Điều khiển camera cho camera tutorial mode | Điều khiển camera cho camera tutorial mode | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Center-on-Map Click | Tính năng center-on-map click | Tính năng center-on-map click | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Auto-Leveling | Tính năng auto-leveling | Tính năng auto-leveling | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Safe Mode Rendering | Tính năng safe mode rendering | Tính năng safe mode rendering | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Boundary Snap | Điều khiển camera cho camera boundary snap | Điều khiển camera cho camera boundary snap | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Telemetry for Navigation | Tính năng telemetry for navigation | Tính năng telemetry for navigation | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Viewport Ruler | Tính năng viewport ruler | Tính năng viewport ruler | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Night Mode Preset | Tính năng night mode preset | Tính năng night mode preset | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | High Contrast Scene Mode | Tính năng high contrast scene mode | Tính năng high contrast scene mode | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Snapshot API | Điều khiển camera cho camera snapshot api | Điều khiển camera cho camera snapshot api | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Observability & Integrations | Webhook Triggers (Optional) | Kích hoạt webhook cho hành động quan trọng (optional). | Kích hoạt webhook cho hành động quan trọng (optional). | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Performance & Reliability | Adaptive Quality | Tự điều chỉnh chất lượng theo FPS/năng lực thiết bị. | Tự điều chỉnh chất lượng theo FPS/năng lực thiết bị. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Performance & Reliability | Tile Request Concurrency Control | Giới hạn số request song song tránh nghẽn. | Giới hạn số request song song tránh nghẽn. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Performance & Reliability | Progressive Loading | Tải thô trước, tinh dần để người dùng thấy nhanh. | Tải thô trước, tinh dần để người dùng thấy nhanh. | Nâng cao trải nghiệm và khả năng sử dụng cho người dùng | Phase 2 |
| Performance & Reliability | Cache Management UI | Xem/xóa cache để xử lý lỗi hiển thị. | Xem/xóa cache để xử lý lỗi hiển thị. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Performance & Reliability | Network Resilience Mode | Chế độ tiết kiệm băng thông khi mạng yếu. | Chế độ tiết kiệm băng thông khi mạng yếu. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Performance & Reliability | Error Boundary U | Màn hình lỗi thân thiện, có nút khôi phục. | Màn hình lỗi thân thiện, có nút khôi phục. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Performance & Reliability | Offline Detection | Phát hiện offline và tạm dừng request hợp lý. | Phát hiện offline và tạm dừng request hợp lý. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Performance & Reliability | Resource Budgeting | Giới hạn RAM, tự evict tile ít dùng. | Giới hạn RAM, tự evict tile ít dùng. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Performance & Reliability | Warm Start | Preload tile quanh điểm xuất phát để mở nhanh. | Preload tile quanh điểm xuất phát để mở nhanh. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Routing & Navigation | Outdoor Routing | Tìm đường ngoài trời giữa A→B | Tìm đường ngoài trời giữa A→B | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Routing & Navigation | Route Profiles | Hồ sơ tuyến: car/bike/walk/accessibility. | Hồ sơ tuyến: car/bike/walk/accessibility. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Routing & Navigation | Avoid Options | Tùy chọn tránh: thu phí/cao tốc/cầu thang/khu hạn chế. | Tùy chọn tránh: thu phí/cao tốc/cầu thang/khu hạn chế. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Routing & Navigation | Multi-Stop Routing | Thêm điểm dừng (via points), tối ưu thứ tự (optional). | Thêm điểm dừng (via points), tối ưu thứ tự (optional). | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Routing & Navigation | Turn-by-Turn Steps | Danh sách hướng dẫn từng bước. | Danh sách hướng dẫn từng bước. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Security & Privacy (OAuth2 Opaque Tokens) | OAuth2 Login (Auth Code + PKCE) | Đăng nhập an toàn theo OAuth2 với PKCE. | Đăng nhập an toàn theo OAuth2 với PKCE. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Security & Privacy (OAuth2 Opaque Tokens) | Opaque Access Token Storage | Lưu access token dạng opaque an toàn, không “parse token”. | Lưu access token dạng opaque an toàn, không “parse token”. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Security & Privacy (OAuth2 Opaque Tokens) | Token Revocation on Logout | Logout thì revoke token theo RFC 7009 (nếu bật). | Logout thì revoke token theo RFC 7009 (nếu bật). | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Security & Privacy (OAuth2 Opaque Tokens) | Cross-Tenant Isolation Guards | Ngăn request trộn tenant (đảm bảo isolation). | Ngăn request trộn tenant (đảm bảo isolation). | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Security & Privacy (OAuth2 Opaque Tokens) | PII Redaction in Logs | Loại PII khỏi log/telemetry phía client. | Loại PII khỏi log/telemetry phía client. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Terrain & Elevation | Elevation Query | Truy vấn độ cao tại điểm người dùng click | Truy vấn độ cao tại điểm người dùng click | Nâng cao trải nghiệm và khả năng sử dụng cho người dùng | Phase 2 |
| Terrain & Elevation | Height Profile Tool | Biểu đồ cao độ theo tuyến (profile) | Biểu đồ cao độ theo tuyến (profile) | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Uncategory | Hiển thị bản đồ hình cầu | Tính năng hiển thị bản đồ hình cầu | Tính năng hiển thị bản đồ hình cầu | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Uncategory | Bật, tắt lớp dữ liệu | Bật/ tắt lớp tình trạng kẹt xe, địa điểm (POI) | Bật/ tắt lớp tình trạng kẹt xe, địa điểm (POI) | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Uncategory | Custom map button | Nút phóng to, thu nhỏ | Nút phóng to, thu nhỏ | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Uncategory | Xoay trục Bắc bản đồ | Tính năng xoay trục bắc bản đồ | Tính năng xoay trục bắc bản đồ | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Uncategory | Vị trí của tôi | Tính năng vị trí của tôi | Tính năng vị trí của tôi | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Uncategory | Sao chép vị trí | Tính năng sao chép vị trí | Tính năng sao chép vị trí | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Uncategory | None | Chia sẻ địa điểm | Chia sẻ địa điểm | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Pan / Zoom / Rotate / Tilt | Điều khiển camera 3D | Điều khiển camera 3D | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Reset / Home view | Về góc nhìn mặc định | Về góc nhìn mặc định | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Fly-to (animate) | Bay đến vị trí/đối tượng | Bay đến vị trí/đối tượng | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Bookmark viewpoints | Lưu góc nhìn | Lưu góc nhìn | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Camera settings | Tùy chỉnh camera | Tùy chỉnh camera | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Lighting (Sun) | Ánh sáng theo thời gian | Ánh sáng theo thời gian | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Shadows | Đổ bóng | Tính năng shadows | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Terrain/DEM (tuỳ) | Địa hình 3D | Địa hình 3D | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Globe/Flat mode (tuỳ) | Địa cầu/phẳng | Địa cầu/phẳng | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Layer list & visibility | Bật/tắt lớp dữ liệu | Bật/tắt lớp dữ liệu | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Opacity | Độ trong suốt | Độ trong suốt | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Layer ordering / priority | Ưu tiên hiển thị | Ưu tiên hiển thị | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | 3D Tiles / Model layer | Lớp mô hình 3D | Lớp mô hình 3D | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Vector / POI layers | Lớp 2D/POI trên 3D | Lớp 2D/POI trên 3D | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Filter by attribute | Lọc theo thuộc tính | Lọc theo thuộc tính | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Time filter (tuỳ) | Lọc theo thời gian | Lọc theo thời gian | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Pick / Select object | Chọn đối tượng | Chọn đối tượng | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Hover highlight | Tô sáng khi hover | Tô sáng khi hover | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Tooltip / Popup | Thông tin nhanh | Thông tin nhanh | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Details panel | Bảng chi tiết | Bảng chi tiết | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Multi-select (tuỳ) | Chọn nhiều đối tượng | Chọn nhiều đối tượng | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Search (place/POI/address) | Tìm kiếm | Tính năng tìm kiếm và tra cứu nâng cao | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Autocomplete | Gợi ý khi gõ | Gợi ý khi gõ | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Locate me / GPS (tuỳ) | Định vị người dùng | Định vị người dùng | Nâng cao trải nghiệm và khả năng sử dụng cho người dùng | Phase 2 |
| Use Cases - tmp | Route | Vẽ tuyến đường | Vẽ tuyến đường | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Route preview | Xem trước tuyến | Xem trước tuyến | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Turn-by-turn steps (tuỳ) | Hướng dẫn từng bước | Hướng dẫn từng bước | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Measure distance | Đo khoảng cách | Đo khoảng cách | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Measure area | Đo diện tích | Đo diện tích | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Measure height | Đo chiều cao | Đo chiều cao | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Draw/Annotate (tuỳ) | Vẽ & ghi chú | Vẽ & ghi chú | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Clipping plane/box | Cắt để nhìn bên trong | Cắt để nhìn bên trong | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Indoor/Outdoor switch | Chuyển cảnh indoor/outdoor | Chuyển cảnh indoor/outdoor | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Style / Theme switch | Đổi style | Tính năng style / theme switch | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Label control | Điều khiển nhãn | Điều khiển nhãn | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Color by attribute | Tô màu theo thuộc tính | Tô màu theo thuộc tính | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Heatmap/Choropleth (tuỳ) | Bản đồ nhiệt/choropleth | Bản đồ nhiệt/choropleth | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Share link | Chia sẻ trạng thái | Chia sẻ trạng thái | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Screenshot | Chụp ảnh | Tính năng screenshot | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Export data (tuỳ) | Xuất dữ liệu | Xuất dữ liệu | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | LOD/Streaming | Tải theo mức chi tiết | Tải theo mức chi tiết | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Cache | Cache tiles/models | Cache tiles/models | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | FPS/Debug panel | Bảng debug | Bảng debug | Hỗ trợ debug và troubleshooting hiệu quả | Phase 2 |
| Use Cases - tmp | API key / token | Xác thực truy cập | Xác thực truy cập | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | RBAC / Access control | Phân quyền dữ liệu | Phân quyền dữ liệu | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Event API | Sự kiện tương tác | Sự kiện tương tác | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Custom layers | Nhúng lớp tuỳ chỉnh | Nhúng lớp tuỳ chỉnh | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp | Plugin system (tuỳ) | Hệ plugin | Tính năng plugin system (tuỳ) | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp2 | Trải nghiệm bản đồ & Camera | Pan / Zoom / Rotate / Tilt | Pan / Zoom / Rotate / Tilt | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp2 | Trực quan hóa & Style | Tính năng trực quan hóa & style | Tính năng trực quan hóa & style | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp2 | Tìm kiếm & Định vị | Search address | Search address | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp2 | Dẫn đường | Route | Tính năng dẫn đường | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp2 | Đo đạc & vẽ | Measure distance | Measure distance | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp2 | Nền/khung cảnh 3D | Lighting (Sun) | Lighting (Sun) | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp2 | Dữ liệu & Layer | Layer list & visibility | Layer list & visibility | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp2 | Tương tác & Thông tin | Pick / Select object | Pick / Select object | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp2 | Cắt lớp & Indoor | Clipping plane/box | Clipping plane/box | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp2 | Chia sẻ & Xuất bản | Share link | Share link | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp2 | Hiệu năng & Debug | LOD/Streaming | LOD/Streaming | Hỗ trợ troubleshooting và phân tích vấn đề | Phase 2 |
| Use Cases - tmp2 | Bảo mật & Phân quyền | API key / token | API key / token | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp2 | Tích hợp & Mở rộng | Event API | Tính năng tích hợp & mở rộng | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | CORE MAP & VISUALIZATION | NỀN TẢNG BẢN ĐỒ | NỀN TẢNG BẢN ĐỒ | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Hiển thị bản đồ cơ bản | Tính năng hiển thị bản đồ cơ bản | Tính năng hiển thị bản đồ cơ bản | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Xem chi tiết | Người dùng có thể xem chi tiết một địa điểm | Người dùng có thể xem chi tiết một địa điểm | Nâng cao trải nghiệm và khả năng sử dụng cho người dùng | Phase 2 |
| Use Cases - tmp3 | Quay bản đồ | Người dùng có thể quay bản đồ sang trái | Người dùng có thể quay bản đồ sang trái | Nâng cao trải nghiệm và khả năng sử dụng cho người dùng | Phase 2 |
| Use Cases - tmp3 | Nghiêng bản đồ | Người dùng có thể nghiêng bản đồ lên trên | Người dùng có thể nghiêng bản đồ lên trên | Nâng cao trải nghiệm và khả năng sử dụng cho người dùng | Phase 2 |
| Use Cases - tmp3 | Phóng to thu nhỏ bản đồ | Người dùng có thể phóng to bản đồ | Người dùng có thể phóng to bản đồ | Nâng cao trải nghiệm và khả năng sử dụng cho người dùng | Phase 2 |
| Use Cases - tmp3 | Đổi layout hiển thị | Cho phép đổi bản đồ sang tối | Cho phép đổi bản đồ sang tối | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Xem vị trí | Người dùng có thể click chuột trái vào bản đồ để xem thông tin một vị trí bất kỳ | Người dùng có thể click chuột trái vào bản đồ để xem thông tin một vị trí bất kỳ trên bản đồ | Nâng cao trải nghiệm và khả năng sử dụng cho người dùng | Phase 2 |
| Use Cases - tmp3 | Sao chép kinh độ vĩ độ | Người dùng có thể click chuột phải trên bản đồ và sao chép kinh độ, vĩ độ của vị | Người dùng có thể click chuột phải trên bản đồ và sao chép kinh độ, vĩ độ của vị trí đó | Nâng cao trải nghiệm và khả năng sử dụng cho người dùng | Phase 2 |
| Use Cases - tmp3 | Người dùng có thể xem tọa độ vn2000/WGS84 | Người dùng có thể xem tọa độ VN2000, WGS 84 | Người dùng có thể xem tọa độ VN2000, WGS 84 | Nâng cao trải nghiệm và khả năng sử dụng cho người dùng | Phase 2 |
| Use Cases - tmp3 | Basemap & đa nguồn, Thao tác vị trí & tọa độ | Tính năng basemap & đa nguồn, thao tác vị trí & tọa độ | Tính năng basemap & đa nguồn, thao tác vị trí & tọa độ | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Hiển thị bản đồ đa nguồn | hỗ trợ basemaps (OSM, satelit, bản đồ chính phủ), tiles raster/ vector (XYZ, Til | hỗ trợ basemaps (OSM, satelit, bản đồ chính phủ), tiles raster/ vector (XYZ, TileJSON), WMS/WMTS, TM | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Định vị GPS “Vị trí của tôi” | Cho phép định vị gps của tôi | Cho phép định vị gps của tôi | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Measurement tools | đo khoảng cách, diện tích, tọa độ. | đo khoảng cách, diện tích, tọa độ. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Drawing & annotation | vẽ vùng, đường, điểm; lưu annotation vào hệ thống (kèm meta: user, time). | vẽ vùng, đường, điểm; lưu annotation vào hệ thống (kèm meta: user, time). | Nâng cao trải nghiệm và khả năng sử dụng cho người dùng | Phase 2 |
| Use Cases - tmp3 | Hiển thị Lớp địa giới | tỉnh / huyện / xã / phường | tỉnh / huyện / xã / phường | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Lưu địa điểm | Người dùng có thể lưu địa điểm để dễ dàng xem lại sau đó | Người dùng có thể lưu địa điểm để dễ dàng xem lại sau đó | Nâng cao trải nghiệm và khả năng sử dụng cho người dùng | Phase 2 |
| Use Cases - tmp3 | Chia sẻ địa điểm | Người dùng có thể chia sẻ địa điểm bằng sao chép link | Người dùng có thể chia sẻ địa điểm bằng sao chép link | Nâng cao trải nghiệm và khả năng sử dụng cho người dùng | Phase 2 |
| Use Cases - tmp3 | Đề xuất chỉnh sửa | Người dùng có thể đề xuất chỉnh sửa một địa điểm | Người dùng có thể đề xuất chỉnh sửa một địa điểm | Nâng cao trải nghiệm và khả năng sử dụng cho người dùng | Phase 2 |
| Use Cases - tmp3 | Cài đặt hiển thị bản đồ | Người dùng có thể cái đặt hiển thị bản đồ theo thời tiết: tự động, nắng, mưa, tu | Người dùng có thể cái đặt hiển thị bản đồ theo thời tiết: tự động, nắng, mưa, tuyết | Nâng cao trải nghiệm và khả năng sử dụng cho người dùng | Phase 2 |
| Use Cases - tmp3 | Lựa chọn ngôn ngữ | Người dùng có thể lựa chọn ngôn ngữ sử dụng là tiếng Việt hoặc tiếng Anh | Người dùng có thể lựa chọn ngôn ngữ sử dụng là tiếng Việt hoặc tiếng Anh | Nâng cao trải nghiệm và khả năng sử dụng cho người dùng | Phase 2 |
| Use Cases - tmp3 | Phân quyền dữ liệu theo lớp bản đồ | Camera, GPS, lực lượng → chỉ user được phép mới thấy | Camera, GPS, lực lượng → chỉ user được phép mới thấy | Nâng cao trải nghiệm và khả năng sử dụng cho người dùng | Phase 2 |
| Use Cases - tmp3 | Bản đồ ẩn danh | Thao tác bản đồ ẩn danh | Thao tác bản đồ ẩn danh | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Watermark & chống chụp màn hình | Ghi dấu user, thời gian trên bản đồ, Phát hiện export trái phép | Ghi dấu user, thời gian trên bản đồ, Phát hiện export trái phép | Nâng cao trải nghiệm và khả năng sử dụng cho người dùng | Phase 2 |
| Use Cases - tmp3 | Bảng điều khiển | Tổng hợp: số vụ việc, lực lượng đang hoạt động, điểm nóng… | Tổng hợp: số vụ việc, lực lượng đang hoạt động, điểm nóng… | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Playbook xử lý sự cố trên bản đồ | Mẫu kịch bản: Cháy lớn, Tai nạn liên hoàn. | Mẫu kịch bản: Cháy lớn, Tai nạn liên hoàn. Map tự động bật: lực lượng gần nhất | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Người dùng có thể nhúng link vào web | Cho phép nhúng link embed | Cho phép nhúng link embed | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Hiển thị bản đồ các điểm cháy | Cho phép bật lớp dữ liệu đám cháy | Cho phép bật lớp dữ liệu đám cháy | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Hiển thị các vị trí cứu nạn cứu hộ | Cho phép thêm địa điểm khi offline và đồng bộ khi online | Cho phép thêm địa điểm khi offline và đồng bộ khi online | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Tính năng đăng nhập, đăng xuất | Cho phép đăng nhập bằng tài khoản | Cho phép đăng nhập bằng tài khoản | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Cho phép thao tác model 3D | Cho phép xem thông tin, đo chiều cao, chỉ đường trên nền 3D | Cho phép xem thông tin, đo chiều cao, chỉ đường trên nền 3D | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | DATA & LAYER MANAGEMENT | QUẢN LÝ DỮ LIỆU & LỚP | QUẢN LÝ DỮ LIỆU & LỚP | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Cấu hình hiển thị đối tượng 3D theo thời gian | Người dùng có thể chọn mốc thời gian | Người dùng có thể chọn mốc thời gian | Nâng cao trải nghiệm và khả năng sử dụng cho người dùng | Phase 2 |
| Use Cases - tmp3 | Báo cáo lỗi | Người dùng có thể gửi báo cáo lỗi đến hệ thống | Người dùng có thể gửi báo cáo lỗi đến hệ thống | Nâng cao trải nghiệm và khả năng sử dụng cho người dùng | Phase 2 |
| Use Cases - tmp3 | Layer time slider / temporal playback | em dữ liệu theo thời gian (ví dụ: tracks xe, trafic theo thời gian). | em dữ liệu theo thời gian (ví dụ: tracks xe, trafic theo thời gian). | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Feature info & pop-ups | hiển thị thông tin chi tiết, liên kết tới hồ sơ (case ID). | hiển thị thông tin chi tiết, liên kết tới hồ sơ (case ID). | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Tìm kiếm theo bán kính, theo thuộc tính | tìm kiếm, lọc theo thuộc tính, spatial query (within, intersect), saved queries. | tìm kiếm, lọc theo thuộc tính, spatial query (within, intersect), saved queries. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Heatmaps | Mật độ kẹt xe, an ninh giao thông | Mật độ kẹt xe, an ninh giao thông | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Hiển thị tuyến đường cấm | Đường cấm khi có dự kiện, đường cấm xe xăng dầu | Đường cấm khi có dự kiện, đường cấm xe xăng dầu | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Hiển thị vùng cấm bay của drone | Hiển thị vùng cấm bay | Hiển thị vùng cấm bay | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Hiển thị các tuyến đường ngập | Hiển thị tuyến đường ngập do mưa hoặc triểu cường, bảo lũ | Hiển thị tuyến đường ngập do mưa hoặc triểu cường, bảo lũ | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Thêm mới địa điểm | Người dùng có thể thêm mới một địa điểm trên map | Người dùng có thể thêm mới một địa điểm trên map | Nâng cao trải nghiệm và khả năng sử dụng cho người dùng | Phase 2 |
| Use Cases - tmp3 | Thêm đối tượng 3D | Người dùng có thể thêm mới một đối tượng 3D | Người dùng có thể thêm mới một đối tượng 3D | Nâng cao trải nghiệm và khả năng sử dụng cho người dùng | Phase 2 |
| Use Cases - tmp3 | Chỉnh sửa tuyến đường | Người dùng có thể chính sửa tuyến đường trực tiếp trên map | Người dùng có thể chính sửa tuyến đường trực tiếp trên map | Nâng cao trải nghiệm và khả năng sử dụng cho người dùng | Phase 2 |
| Use Cases - tmp3 | Xem dữ liệu theo mốc thời gian | Cho phép xem dữ liệu theo chiều thời gian | Cho phép xem dữ liệu theo chiều thời gian | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Hiển thị đèn giao thông toàn quốc | Tính năng hiển thị đèn giao thông toàn quốc | Tính năng hiển thị đèn giao thông toàn quốc | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Hiển thị tuyến đường ngập | Tính năng hiển thị tuyến đường ngập | Tính năng hiển thị tuyến đường ngập | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | SEARCH & SPATIAL QUERY | (TÌM KIẾM & PHÂN TÍCH KHÔNG GIAN) | (TÌM KIẾM & PHÂN TÍCH KHÔNG GIAN) | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Cấu hình địa điểm của tôi | Người dùng có thể thiết lập địa điểm là nhà riêng | Người dùng có thể thiết lập địa điểm là nhà riêng | Nâng cao trải nghiệm và khả năng sử dụng cho người dùng | Phase 2 |
| Use Cases - tmp3 | Tìm kiếm theo địa chỉ | Cho phép tìm kiếm theo địa chỉ | Cho phép tìm kiếm theo địa chỉ | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Tìm kiếm theo tọa độ | vn2000/WGS 84 | vn2000/WGS 84 | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Tìm kiếm theo đơn vị hành chính | Theo đơn vị hành chính | Theo đơn vị hành chính | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Search around | Tính năng tìm kiếm và tra cứu nâng cao | Tính năng tìm kiếm và tra cứu nâng cao | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Tìm kiếm trên bản đồ | Người dùng có thể tìm kiếm thông tin bất kỳ trên bản đồ: địa điểm, địa chỉ, khu | Người dùng có thể tìm kiếm thông tin bất kỳ trên bản đồ: địa điểm, địa chỉ, khu vực, số nhà, thửa đấ | Nâng cao trải nghiệm và khả năng sử dụng cho người dùng | Phase 2 |
| Use Cases - tmp3 | Chức năng cho phép người dùng gửi thông tin về sự cố giao thông lớn | Cho phép đưa thông tin về sự cố giao thông trên bản đồ | Cho phép đưa thông tin về sự cố giao thông trên bản đồ | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Chức năng cho phép người dùng chia sẽ thông tin sự cố giao thông | cho phép chia sẽ thông tin giao thông tại nơi xảy ra sự cố | cho phép chia sẽ thông tin giao thông tại nơi xảy ra sự cố | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Tìm kiếm nâng cao QR Code scanner | QR Code scanner | QR Code scanner | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Tìm kiếm nâng cao Photo location | Photo location | Photo location | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Tìm kiếm nâng cao Voice search | Voice search | Voice search | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Tìm kiếm nâng cao Autocomplete | Autocomplete | Autocomplete | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Search history | Search history | Search history | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Spatial query theo điều kiện | Cho phép tìm kiếm danh sách con đường có camera | Cho phép tìm kiếm danh sách con đường có camera | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | NAVIGATION & ROUTING | DẪN ĐƯỜNG – LỘ TRÌNH | DẪN ĐƯỜNG – LỘ TRÌNH | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Chỉ đường | Người dùng có thể chỉ đường từ một điểm xuất phát đến một điểm đến trên bản đồ: | Người dùng có thể chỉ đường từ một điểm xuất phát đến một điểm đến trên bản đồ: dành cho xe cứu thươ | Nâng cao trải nghiệm và khả năng sử dụng cho người dùng | Phase 2 |
| Use Cases - tmp3 | Chức năng AI chỉ đường né kẹt xe | tự động tối ưu lộ trình giờ cao điểm | tự động tối ưu lộ trình giờ cao điểm | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Hiển thị tuyến đường dành riêng cho bộ công an | xe cứu thương, xe chữ cháy, xe tuần tra | xe cứu thương, xe chữ cháy, xe tuần tra | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | AI chỉ đường dựa trên kẹt xe và đèn giao thông | tính toàn lưu lượng xe và đèn giao thông để chỉ đường với thời gian ngắn nhất | tính toàn lưu lượng xe và đèn giao thông để chỉ đường với thời gian ngắn nhất | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Dẫn đường trong nhà (indoor map) | cho phép chỉ đường nội khu, trong tòa nhà | cho phép chỉ đường nội khu, trong tòa nhà | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Bản đồ offline mã hoá | Cho phép chỉ đường khi offline, phục vụ cứu nạn tỏng rừng sâu | Cho phép chỉ đường khi offline, phục vụ cứu nạn tỏng rừng sâu | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Dẫn đường nghiệp vụ Xe cứu thương, Xe chữa cháy | Tính năng dẫn đường nghiệp vụ xe cứu thương, xe chữa cháy | Tính năng dẫn đường nghiệp vụ xe cứu thương, xe chữa cháy | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | AI Routing | Né kẹt xe theo thời gian thực | Né kẹt xe theo thời gian thực | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | REAL-TIME MONITORING | GIÁM SÁT THỜI GIAN THỰC | GIÁM SÁT THỜI GIAN THỰC | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Real-time feeds | ingest feed từ GPS/AVL, CCTV meta, cảm biến IoT, alert stream. | ingest feed từ GPS/AVL, CCTV meta, cảm biến IoT, alert stream. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Automatic Vehicle Location (AVL) | hiển thị vị trí xe, trạng thái (on-duty, off-duty), breadcrumb trails. | hiển thị vị trí xe, trạng thái (on-duty, off-duty), breadcrumb trails. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Thêm api/ link nhúng camera hiển thị | Hiển thị hình ảnh camera giao thông trực tuyến | Hiển thị hình ảnh camera giao thông trực tuyến | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Hiển thị Bản đồ camera giao thông | Hiển thị trực tiếp camera giao thông | Hiển thị trực tiếp camera giao thông | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Gắn camera vào bản đồ 2D / 3D | Gắn link camera vào gtel maps | Gắn link camera vào gtel maps | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Hiển thị hệ thống đèn giao thông toàn quốc | Thông tin đèn giao thông toàn quốc | Thông tin đèn giao thông toàn quốc | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | IoT sensors | Mưa, bão, lũ | Mưa, bão, lũ | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | COMMAND & DISPATCH | CHỈ HUY – ĐIỀU PHỐI | CHỈ HUY – ĐIỀU PHỐI | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Integrated CAD/113/114/115 systems | phối hợp gọi cứu hộ, dispatch trực tiếp từ bản đồ. | phối hợp gọi cứu hộ, dispatch trực tiếp từ bản đồ. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Giao nhiệm vụ trực tiếp trên bản đồ | Hiển thị các địa điểm cần cứu hộ cứu nạn và địa điểm cần cấp cứu | Hiển thị các địa điểm cần cứu hộ cứu nạn và địa điểm cần cấp cứu | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Geofencing & Alerts: | tạo vùng cảnh báo kẹt xe, push alert khi có vi phạm/entry/exit. | tạo vùng cảnh báo kẹt xe, push alert khi có vi phạm/entry/exit. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | AI gợi ý phân bổ lực lượng CSGT | Hiển thị khu vực cần CSGT giám sát và điều tiết giao thông | Hiển thị khu vực cần CSGT giám sát và điều tiết giao thông | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Ước tính ETA tiếp cận | Tính năng ước tính eta tiếp cận | Tính năng ước tính eta tiếp cận | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Dispatch trực tiếp từ bản đồ | Tính năng dispatch trực tiếp từ bản đồ | Tính năng dispatch trực tiếp từ bản đồ | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Cảnh báo sự cố lớn | Hiển thị cảnh báo sự cố lớn | Hiển thị cảnh báo sự cố lớn | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | AI & ADVANCED ANALYTICS | Tính năng ai & advanced analytics | Tính năng ai & advanced analytics | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | AI dự báo kẹt xe theo thời gian | Dự báo kẹt xe theo tuần tháng năm, ngày , giờ. | Dự báo kẹt xe theo tuần tháng năm, ngày , giờ. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | AI phân tích tuyển đường theo camera trên bản đồ | Theo dõi lộ trình xe theo camera, Phân tích mối liên hệ không gian | Theo dõi lộ trình xe theo camera, Phân tích mối liên hệ không gian | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Hiển thị thành phố 3D | Hiển thị đối tương 3D trên bản đồ | Hiển thị đối tương 3D trên bản đồ | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | AR hiển thị thông tin lên camera | Hiển thị thông tin camera AR | Hiển thị thông tin camera AR | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Mô phỏng tình huống an ninh/ Mô phỏng tình huống cháy | Hiển thị trực quan hình ảnh cháy, an ninh trên bản đồ | Hiển thị trực quan hình ảnh cháy, an ninh trên bản đồ | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Digital twins / 3D city models | mô phỏng kịch bản cho giám sát và chỉ huy | mô phỏng kịch bản cho giám sát và chỉ huy | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp3 | Theo dõi lực lượng thời gian thực (GPS) | Theo dõi GPS theo thời gian thực | Theo dõi GPS theo thời gian thực | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp4 | Data loading & access APIs | Tiling Service | Tiling Service | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp4 | Tiling & rendering APIs | Vector Tiles API | Vector Tiles API | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp4 | Map design | Styles API | Styles API | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp4 | Navigation APIs | Directions API | Directions API | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp4 | Search APIs | Geocoding API | Geocoding API | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp5 | Nhóm tính năng lớp dữ liệu bản đồ - Layer Maps | Quản lý và điều khiển nhóm tính năng lớp dữ liệu bản đồ - layer maps | Quản lý và điều khiển nhóm tính năng lớp dữ liệu bản đồ - layer maps | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp5 | Nhóm công cụ tương tác bản đồ - Map Tools | Tính năng nhóm công cụ tương tác bản đồ - map tools | Tính năng nhóm công cụ tương tác bản đồ - map tools | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp5 | Nhóm tính năng tiện ích - Convenient Tools | Tính năng nhóm tính năng tiện ích - convenient tools | Tính năng nhóm tính năng tiện ích - convenient tools | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp5 | Nhóm tính năng tìm kiếm - Search | Tính năng tìm kiếm và tra cứu nâng cao | Tính năng tìm kiếm và tra cứu nâng cao | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp5 | Nhóm tính năng điều hướng - Direction | Tính năng nhóm tính năng điều hướng - direction | Tính năng nhóm tính năng điều hướng - direction | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp5 | Nhóm tính năng phân tích không gian | Tính năng nhóm tính năng phân tích không gian | Tính năng nhóm tính năng phân tích không gian | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp5 | Nhóm tính năng tạo vùng tiếp cận - Isochrone | Tính năng nhóm tính năng tạo vùng tiếp cận - isochrone | Tính năng nhóm tính năng tạo vùng tiếp cận - isochrone | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp5 | Nhóm tính năng tạo vùng phát hiện - Geofence | Tính năng nhóm tính năng tạo vùng phát hiện - geofence | Tính năng nhóm tính năng tạo vùng phát hiện - geofence | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp5 | DASHBOARD - ĐIỀU KHIỂN | Tính năng dashboard - điều khiển | Tính năng dashboard - điều khiển | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp5 | Nhóm tính năng thống kê người dùng | Tính năng nhóm tính năng thống kê người dùng | Tính năng nhóm tính năng thống kê người dùng | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp5 | Nhóm tính năng thống kê dữ liệu bản đồ | Tính năng nhóm tính năng thống kê dữ liệu bản đồ | Tính năng nhóm tính năng thống kê dữ liệu bản đồ | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp5 | Nhóm tính năng thống kê lớp dữ liệu bản đồ | Tính năng nhóm tính năng thống kê lớp dữ liệu bản đồ | Tính năng nhóm tính năng thống kê lớp dữ liệu bản đồ | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp5 | LANDING PAGE - TRANG ĐÍCH | Tính năng landing page - trang đích | Tính năng landing page - trang đích | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp5 | NOTIFICATION - THÔNG BÁO | Tính năng notification - thông báo | Tính năng notification - thông báo | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp5 | AUTHENTICATION - XÁC THỰC | Tính năng authentication - xác thực | Tính năng authentication - xác thực | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp5 | USER MANAGEMENT - QUẢN LÝ NGƯỜI DÙNG | Tính năng user management - quản lý người dùng | Tính năng user management - quản lý người dùng | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp5 | PERMISSION GROUP MANAGEMENT - QUẢN LÝ NHÓM QUYỀN | Tính năng permission group management - quản lý nhóm quyền | Tính năng permission group management - quản lý nhóm quyền | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp5 | SETTING - THIẾT LẬP | Tính năng setting - thiết lập | Tính năng setting - thiết lập | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp5 | APPEARANCE - TƯƠNG THÍCH | Tính năng appearance - tương thích | Tính năng appearance - tương thích | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp6 | Bản đồ nền | Thêm bản đồ nền mới bằng URL. | Thêm bản đồ nền mới bằng URL. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp6 | Tương tác bản đồ | Phóng to/thu nhỏ bản đồ. | Phóng to/thu nhỏ bản đồ. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp6 | Tiện ích | Chia sẻ vị trí hiện tại hoặc vị trí được chọn cho người khác. | Chia sẻ vị trí hiện tại hoặc vị trí được chọn cho người khác. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp6 | Tìm kiếm | Chuyển đổi địa chỉ dạng văn bản (địa chỉ, tên địa điểm) thành thông tin vị trí. | Chuyển đổi địa chỉ dạng văn bản (địa chỉ, tên địa điểm) thành thông tin vị trí. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp6 | Điều hướng | Tìm tuyến đường tránh: đường thu phí, phà, cao tốc, khu cấm, chiều cao/trọng tải | Tìm tuyến đường tránh: đường thu phí, phà, cao tốc, khu cấm, chiều cao/trọng tải xe.... | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp6 | Các trang giới thiệu | Giới thiệu tổng quan về nền tảng bản đồ. | Giới thiệu tổng quan về nền tảng bản đồ. | Cải thiện hiệu suất và trải nghiệm người dùng | Phase 2 |
| Use Cases - tmp6 | Xác thực người dùng | Đăng nhập bằng tài khoản thông thường (username/email & mật khẩu). | Đăng nhập bằng tài khoản thông thường (username/email & mật khẩu). | Nâng cao trải nghiệm và khả năng sử dụng cho người dùng | Phase 2 |
| Use Cases - tmp6 | Quản lý người dùng | Thay đổi mật khẩu đăng nhập. | Thay đổi mật khẩu đăng nhập. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp6 | Quản lý quyền | Quản lý danh sách nhóm quyền. | Quản lý danh sách nhóm quyền. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp6 | Thiết lập | Thay đổi logo hiển thị cho nền tảng. | Thay đổi logo hiển thị cho nền tảng. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp6 | Cấu hình giao diện | Hỗ trợ giao diện và trải nghiệm người dùng trên thiết bị di động. | Hỗ trợ giao diện và trải nghiệm người dùng trên thiết bị di động. | Nâng cao trải nghiệm và khả năng sử dụng cho người dùng | Phase 2 |
| Use Cases - tmp7 | Maps Viewer | Tính năng maps viewer | Tính năng maps viewer | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp7 | Maps Accounts | Đăng nhập thường | Đăng nhập thường | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp7 | Maps MyAccount | Cập nhật thông tin cá nhân (avatar, tên người dùng, số điện thoại, địa chỉ,. | Cập nhật thông tin cá nhân (avatar, tên người dùng, số điện thoại, địa chỉ,... ) | Nâng cao trải nghiệm và khả năng sử dụng cho người dùng | Phase 2 |
| Use Cases - tmp7 | Điều hướng & Camera | Chuyển chế độ 2D / 3D | Chuyển chế độ 2D / 3D | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp7 | Tìm kiếm, tra cứu, identify | Thanh tìm kiếm tổng (Global Search) | Thanh tìm kiếm tổng (Global Search) | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp7 | Đo vẽ & chú thích | Tính năng đo vẽ & chú thích | Tính năng đo vẽ & chú thích | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Use Cases - tmp7 | Chỉ đường & Di chuyển | Tính năng chỉ đường & di chuyển | Tính năng chỉ đường & di chuyển | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
