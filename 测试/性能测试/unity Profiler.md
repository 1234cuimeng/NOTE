## 性能分析器模块（Profiler Modules）

### CPU使用率性能分析器（CPU Usage Profiler）
CPU Usage Profiler 模块包含一个图表，其中显示应用程序中的时间花费情况。通过该图表可以概要了解应用程序花费时间的所有重要方面（例如渲染、脚本和动画）

- `Rendering` 应用程序花费多少时间来渲染图形。
- `Scripts`	应用程序花费多少时间来运行脚本。
- `Physics`	应用程序在物理引擎上花费多少时间。
- `Animation` 应用程序花费多少时间来动画化应用程序中带蒙皮的网格渲染器 (Skinned Mesh Renderers)、游戏对象和其他组件。这还包括针对 Animation 组件和 Animator 组件所用的系统进行计算所花费的时间。
- `GarbageCollector`	应用程序花费多少时间来运行垃圾回收器。
- `VSync` 应用程序每帧花费多少时间来等待 targetFrameRate 或下一个要同步的 VBlank。此时间基于 QualitySettings.vSyncCount 值、目标帧率或者 VSync 设置（即运行应用程序的平台的默认或强制最大值）。有关 VSync 的更多信息，请参阅本文档中的渲染和 VSync 样本部分。
- `Global Illumination`	应用程序在光照中花费多少时间。
- `UI` 应用程序花费多少时间来显示其 UI。
- `Others` 应用程序在不属于任何其他类别的代码中花费多少时间。此事件包括整个 EditorLoop 或者是 Editor 中对运行模式进行性能分析时的性能分析开销等方面。kjm v v  