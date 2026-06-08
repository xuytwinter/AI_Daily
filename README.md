# AI_Daily

> 每日自动抓取 [AIBase 新闻](https://news.aibase.com/) 的多语言（简体中文 / English / 繁體中文 / 日本語）AI 日报，归档为 Markdown。

## 工作机制

- **数据源**：`https://news.aibase.com/{zh,'',tw,ja}/daily`
- **定时**：GitHub Actions 每日 **UTC 06:00（北京时间 14:00）** 自动运行（cron 实际触发可能延迟 5–15 分钟）。
- **策略**：扫描列表页最近 7 天的条目，自动补抓本地缺失的语言版本；同一篇日报四种语言共享同一个 ID。
- **存储**：`daily/YYYY-MM-DD/{zh,en,tw,ja}.md`，每篇文件含 YAML front-matter（id、source、fetched_at 等）。
- **手动触发**：在 Actions 页面点 *Run workflow*，可指定 `days` 回看窗口或 `force` 覆盖重抓。

## 本地运行

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 抓近 7 天所有语言
python scripts/fetch_daily.py

# 仅抓中文，回看 14 天，强制覆盖
python scripts/fetch_daily.py --langs zh --days 14 --force

# 刷新 README 索引
python scripts/update_readme.py
```

## 目录结构

```
.
├── daily/                  # 抓取的 Markdown 内容（按日期 + 语言）
├── scripts/
│   ├── fetch_daily.py      # 主抓取脚本
│   ├── parsers.py          # 列表页 / 详情页解析
│   └── update_readme.py    # 生成下方索引表
├── .github/workflows/daily.yml
├── requirements.txt
└── README.md
```

## 最近更新 / Recent

<!-- BEGIN_INDEX -->
| 日期 Date | 简体中文 | English | 繁體中文 | 日本語 |
| --- | --- | --- | --- | --- |
| **2026-06-08** | [AI日报：微信开放平台发布AI生态接入指引；月之暗面再融资20亿美元；ChatG…](daily/2026-06-08/zh.md) | [AI Daily: WeChat Open Platform Releases …](daily/2026-06-08/en.md) | [AI日報：微信開放平臺發佈AI生態接入指引；月之暗面再融資20億美元；ChatG…](daily/2026-06-08/tw.md) | [AI日報：微信オープンプラットフォームがAIエコシステム接続指針を発表；Moon…](daily/2026-06-08/ja.md) |
| **2026-06-06** | [AI日报：阿里上线首个官方大模型NBA Chat； Ideogram4.0开源发…](daily/2026-06-06/zh.md) | [AI Daily: Alibaba Launches Its First Off…](daily/2026-06-06/en.md) | [AI日報：阿里上線首個官方大模型NBA Chat； Ideogram4.0開源發…](daily/2026-06-06/tw.md) | [AI日報：アリババが初の公式大規模モデルNBA Chatをリリース；Ideogr…](daily/2026-06-06/ja.md) |
| **2026-06-05** | [AI日报：快手App上线AI购物助手；Kimi Work开启内测；微信互联多厂商…](daily/2026-06-05/zh.md) | [AI Daily: Kuaishou App Launches AI Shopp…](daily/2026-06-05/en.md) | [AI日報：快手App上線AI購物助手；Kimi Work開啓內測；微信互聯多廠商…](daily/2026-06-05/tw.md) | [AI日報：快手アプリにAIショッピングアシスタントが登場；Kimi Workのテ…](daily/2026-06-05/ja.md) |
| **2026-06-04** | [AI日报：千问全面开放第三方Agent与Skill；字节开源统一框架 Berni…](daily/2026-06-04/zh.md) | [AI Daily: Qwen Fully Opens Third-Party A…](daily/2026-06-04/en.md) | [AI日報：千問全面開放第三方Agent與Skill；字節開源統一框架 Berni…](daily/2026-06-04/tw.md) | [AI日報：千問が第三者のエージェントおよびスキルを全面的に開放；バイトダンスが統…](daily/2026-06-04/ja.md) |
| **2026-06-03** | [AI日报：扣子3.0正式上线；豆包预计6月下旬上线付费版本；Krea 2 LoR…](daily/2026-06-03/zh.md) | [AI Daily: Koutu 3.0 Officially Released;…](daily/2026-06-03/en.md) | [AI日報：釦子3.0正式上線；豆包預計6月下旬上線付費版本；Krea 2 LoR…](daily/2026-06-03/tw.md) | [AI日報：クーリー3.0が正式リリース；トウバオは6月下旬に有料版をリリース予定…](daily/2026-06-03/ja.md) |
| **2026-06-02** | [AI日报：MiniMax发布M3 大模型；英伟达物理大模型Cosmos3发布；小…](daily/2026-06-02/zh.md) | [AI Daily: MiniMax Launches M3 Large Mode…](daily/2026-06-02/en.md) | [AI日報：MiniMax發佈M3 大模型；英偉達物理大模型Cosmos3發佈；小…](daily/2026-06-02/tw.md) | [AI日報：MiniMaxがM3大モデルを発表；NVIDIAの物理的大モデルCos…](daily/2026-06-02/ja.md) |
<!-- END_INDEX -->

## License & 数据来源

内容版权归原作者 / [aibase.com](https://news.aibase.com/) 所有，本仓库仅作个人学习与归档用途。
