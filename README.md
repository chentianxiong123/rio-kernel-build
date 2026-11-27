# RIO-UL00 提权研究归档

本仓库记录华为 G7 Plus (RIO-UL00) 的提权可行性研究。已归档（只读）。

**结论：未成功。** 完整过程见 [华为提权尝试-失败总结.md](华为提权尝试-失败总结.md)。

## 内容

- `华为提权尝试-失败总结.md` — 全过程总结：CVE 排查、exploit 编译、源码反推、CI 编译、9008/EDL 尝试、犯的错误、最终结论。
- `androotzf/` — [androotzf](https://github.com/idhyt/androotzf) 源码（GPL-3.0），含 CVE-2017-8890 / Dirty COW / CVE-2015-1805 等 aarch64 exploit。`exploit/CVE-2017-8890/1003/` 是本次尝试用的方案（内部方案号 `n=103`）。
- `.github/workflows/build.yml` — GitHub Actions 内核编译 workflow（尝试从源码生成 System.map，未成功）。
- `scripts/fix_py2.py` — 编译过程中修 Python 2 脚本的辅助脚本。

## 关键事实

- CVE-2017-8890 在本机内核源码中确认未修，但缺精确符号地址（SELinux enforcing、`/proc/kallsyms` 全 0）。
- 设备 boot 是 test-keys 签名的第三方 boot，官方 OTA 内核未必匹配。
- RIO-UL00 封了所有软件进 9008 的入口（`adb reboot edl`、`fastboot oem edl` 等），柚坛工具箱底层也是同样的命令，无法强制进 EDL。
- 用户决定收手，未对手机做任何永久性修改。
