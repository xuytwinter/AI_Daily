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
| **2026-08-14** | [AI日报：MiniMax发布Music3音乐模型；百度GenFlow官宣中文名“…](daily/2026-08-14/zh.md) | [AI Daily: MiniMax Launches Music3 Music …](daily/2026-08-14/en.md) | [AI日報：MiniMax發佈Music3音樂模型；百度GenFlow官宣中文名“…](daily/2026-08-14/tw.md) | [AI日報：MiniMaxがMusic3音楽モデルをリリース；百度GenFlowが…](daily/2026-08-14/ja.md) |
| **2026-08-13** | [AI日报：DeepSeek V4 Pro正式版亮相；小红书或推进“AI导购”功能…](daily/2026-08-13/zh.md) | [AI Daily: DeepSeek V4 Pro Final Version …](daily/2026-08-13/en.md) | [AI日報：DeepSeek V4 Pro正式版亮相；小紅書或推進“AI導購”功能…](daily/2026-08-13/tw.md) | [AI日報：DeepSeek V4 Proの正式版が登場；小紅書がAI販売ガイド機…](daily/2026-08-13/ja.md) |
| **2026-08-12** | [AI日报：SpaceXAI 推出Grok Bot；OpenAI发布Linux版C…](daily/2026-08-12/zh.md) | [AI Daily: SpaceXAI Launches Grok Bot; Op…](daily/2026-08-12/en.md) | [AI日報：SpaceXAI 推出Grok Bot；OpenAI發佈Linux版C…](daily/2026-08-12/tw.md) | [AI日報：SpaceXAIがGrok Botを発表；OpenAIがLinux版C…](daily/2026-08-12/ja.md) |
| **2026-08-11** | [AI日报：豆包接入抖音来客酒店交易；千问上线AI硬件开放平台；腾讯开源全新浏览器…](daily/2026-08-11/zh.md) | [AI Daily: DouBao Integrates with Douyin …](daily/2026-08-11/en.md) | [AI日報：豆包接入抖音來客酒店交易；千問上線AI硬件開放平臺；騰訊開源全新瀏覽器…](daily/2026-08-11/tw.md) | [AI日報：ドウボウが抖音来客のホテル取引に統合；千問がAIハードウェアオープンプ…](daily/2026-08-11/ja.md) |
| **2026-08-10** | [AI日报：xAI Imagine Image2.0上线；豆包推荐酒店也开始收费；…](daily/2026-08-10/zh.md) | [AI Daily: xAI Imagine Image2.0 Launches;…](daily/2026-08-10/en.md) | [AI日報：xAI Imagine Image2.0上線；豆包推薦酒店也開始收費；…](daily/2026-08-10/tw.md) | [AI日報：xAI Imagine Image2.0がリリース；ドウバオがホテルの…](daily/2026-08-10/ja.md) |
| **2026-08-08** | [AI日报：OpenAI取消ChatGPT文本聊天限制；小米智能摄像机4 Max …](daily/2026-08-08/zh.md) | [AI Daily: OpenAI Removes ChatGPT Text Ch…](daily/2026-08-08/en.md) | [AI日報：OpenAI取消ChatGPT文本聊天限制；小米智能攝像機4 Max …](daily/2026-08-08/tw.md) | [AI日報：OpenAIがChatGPTのテキストチャット制限を解除；小米スマート…](daily/2026-08-08/ja.md) |
| **2026-08-07** | [AI日报：OpenAI取消ChatGPT文本聊天限制；小米智能摄像机4 Max …](daily/2026-08-07/zh.md) | [AI Daily: OpenAI Removes ChatGPT Text Ch…](daily/2026-08-07/en.md) | [AI日報：OpenAI取消ChatGPT文本聊天限制；小米智能攝像機4 Max …](daily/2026-08-07/tw.md) | [AI日報：OpenAIがChatGPTのテキストチャット制限を解除；小米スマート…](daily/2026-08-07/ja.md) |
| **2026-08-06** | [AI日报：DeepSeek将上调API价格；美图上线AI平台MeituHub；小…](daily/2026-08-06/zh.md) | [AI Daily: DeepSeek to Increase API Price…](daily/2026-08-06/en.md) | [AI日報：DeepSeek將上調API價格；美圖上線AI平臺MeituHub；小…](daily/2026-08-06/tw.md) | [AI日報：DeepSeekがAPI価格を引き上げる；メイトゥがAIプラットフォー…](daily/2026-08-06/ja.md) |
| **2026-08-05** | [AI日报：京东开源视频实时编辑模型；Qwen-Image-3.0上线；腾讯混元发…](daily/2026-08-05/zh.md) | [AI Daily: JD.com Opens Source Real-Time …](daily/2026-08-05/en.md) | [AI日報：京東開源視頻實時編輯模型；Qwen-Image-3.0上線；騰訊混元發…](daily/2026-08-05/tw.md) | [AI日報：京东がビデオリアルタイム編集モデルをオープンソース化；Qwen-Ima…](daily/2026-08-05/ja.md) |
| **2026-08-04** | [AI日报：商汤甩出8B小钢炮 U1.5-Lite-Preview；MiniMax…](daily/2026-08-04/zh.md) | [AI Daily: SenseTime Unveils 8B Mini Gun …](daily/2026-08-04/en.md) | [AI日報：商湯甩出8B小鋼炮 U1.5-Lite-Preview；MiniMax…](daily/2026-08-04/tw.md) | [AI日報：商湯が8Bの軽量モデルU1.5-Lite-Previewを発表；Min…](daily/2026-08-04/ja.md) |
| **2026-08-03** | [AI日报：Qwen3.8-Max上线；DeepSeek V4-Flash API…](daily/2026-08-03/zh.md) | [AI Daily: Qwen3.8-Max Launches; DeepSeek…](daily/2026-08-03/en.md) | [AI日報：Qwen3.8-Max上線；DeepSeek V4-Flash API…](daily/2026-08-03/tw.md) | [AI日報：Qwen3.8-Maxがリリース；DeepSeek V4-Flash …](daily/2026-08-03/ja.md) |
| **2026-08-01** | [AI日报：MiniMax发布全模态模型H3；Seedance 2.5发布，30秒…](daily/2026-08-01/zh.md) | [AI Daily: MiniMax Launches Full-modal Mo…](daily/2026-08-01/en.md) | [AI日報：MiniMax發佈全模態模型H3；Seedance 2.5發佈，30秒…](daily/2026-08-01/tw.md) | [AI日報：MiniMaxが全モードモデルH3を発表；Seedance 2.5が3…](daily/2026-08-01/ja.md) |
| **2026-07-31** | [AI日报：MiniMax发布全模态模型H3；Seedance 2.5发布，30秒…](daily/2026-07-31/zh.md) | [AI Daily: MiniMax Launches Full-modal Mo…](daily/2026-07-31/en.md) | [AI日報：MiniMax發佈全模態模型H3；Seedance 2.5發佈，30秒…](daily/2026-07-31/tw.md) | [AI日報：MiniMaxが全モードモデルH3を発表；Seedance 2.5が3…](daily/2026-07-31/ja.md) |
| **2026-07-30** | [AI日报：火山引擎上线豆包搜索开放服务；WorkBuddy上线人机双写；Open…](daily/2026-07-30/zh.md) | [AI Daily: Volc Engine Launches Doubao Se…](daily/2026-07-30/en.md) | [AI日報：火山引擎上線豆包搜索開放服務；WorkBuddy上線人機雙寫；Open…](daily/2026-07-30/tw.md) | [AI日報：ボルカノエンジンがドウバオ検索オープンサービスをリリース；WorkBu…](daily/2026-07-30/ja.md) |
| **2026-07-29** | [AI日报：Fish Audio发布S2.1Pro实时对话语音模型；Grok4.6…](daily/2026-07-29/zh.md) | [AI Daily: Fish Audio launches the S2.1Pr…](daily/2026-07-29/en.md) | [AI日報：Fish Audio發佈S2.1Pro實時對話語音模型；Grok4.6…](daily/2026-07-29/tw.md) | [AI日報：Fish AudioがS2.1Proリアルタイム対話音声モデルを発表；…](daily/2026-07-29/ja.md) |
| **2026-07-28** | [AI日报：Kimi K3登顶全球最大开源模型；小度AI手表Fit开售；我国启动大…](daily/2026-07-28/zh.md) | [AI Daily: Kimi K3 Tops the World's Large…](daily/2026-07-28/en.md) | [AI日報：Kimi K3登頂全球最大開源模型；小度AI手錶Fit開售；我國啓動大…](daily/2026-07-28/tw.md) | [AI日報：Kimi K3が世界最大のオープンソースモデルをトップに；小度のAI腕…](daily/2026-07-28/ja.md) |
| **2026-07-27** | [AI日报：千问办公悄然开启内测；Suno上线高级音轨分离功能；Midjourne…](daily/2026-07-27/zh.md) | [AI Daily: Qwen Office Begins Internal Te…](daily/2026-07-27/en.md) | [AI日報：千問辦公悄然開啓內測；Suno上線高級音軌分離功能；Midjourne…](daily/2026-07-27/tw.md) | [AI日報：千問オフィスが静かに内線を開始；Sunoが上級音軌分離機能をリリース；…](daily/2026-07-27/ja.md) |
| **2026-07-25** | [AI日报：黑森林实验室放出Flux3；Claude Opus现已支持语音模式；快…](daily/2026-07-25/zh.md) | [AI Daily: Black Forest Lab Releases Flux…](daily/2026-07-25/en.md) | [AI日報：黑森林實驗室放出Flux3；Claude Opus現已支持語音模式；快…](daily/2026-07-25/tw.md) | [AI日報：ブラックフォレストラボがFlux3をリリース；Claude Opusは…](daily/2026-07-25/ja.md) |
| **2026-07-24** | [AI日报：黑森林实验室放出Flux3；Claude Opus现已支持语音模式；快…](daily/2026-07-24/zh.md) | [AI Daily: Black Forest Lab Releases Flux…](daily/2026-07-24/en.md) | [AI日報：黑森林實驗室放出Flux3；Claude Opus現已支持語音模式；快…](daily/2026-07-24/tw.md) | [AI日報：ブラックフォレストラボがFlux3をリリース；Claude Opusは…](daily/2026-07-24/ja.md) |
| **2026-07-23** | [AI日报：腾讯云推出 CodeBuddy NPC；北京抛出智能体新政十策；三星眼…](daily/2026-07-23/zh.md) | [AI Daily: Tencent Cloud Launches CodeBud…](daily/2026-07-23/en.md) | [AI日報：騰訊雲推出 CodeBuddy NPC；北京拋出智能體新政十策；三星眼…](daily/2026-07-23/tw.md) | [AI日報：テンセントクラウドがCodeBuddy NPCをリリース；北京がスマー…](daily/2026-07-23/ja.md) |
| **2026-07-22** | [AI日报：谷歌发布 Gemini 3.6 Flash；小红书大模型IMO满分夺金…](daily/2026-07-22/zh.md) | [AI Daily: Google Launches Gemini 3.6 Fla…](daily/2026-07-22/en.md) | [AI日報：谷歌發佈 Gemini 3.6 Flash；小紅書大模型IMO滿分奪金…](daily/2026-07-22/tw.md) | [AI日報：グーグルがGemini 3.6 Flashを発表；小紅書の大規模モデル…](daily/2026-07-22/ja.md) |
| **2026-07-21** | [AI日报：腾讯混元发布科研智能体Hyra-1.0；阿里发布Qwen-Image-…](daily/2026-07-21/zh.md) | [AI Daily: Tencent Huan Yuan Launches Res…](daily/2026-07-21/en.md) | [AI日報：騰訊混元發佈科研智能體Hyra-1.0；阿里發佈Qwen-Image-…](daily/2026-07-21/tw.md) | [AI日報：テンセント・フンユアンが研究用スマートエージェントHyra-1.0を発…](daily/2026-07-21/ja.md) |
| **2026-07-20** | [AI日报：千问3.8模型将发布；字节发布Seed Audio 1.0；面壁智能开…](daily/2026-07-20/zh.md) | [AI Daily: Qwen 3.8 Model to Be Released;…](daily/2026-07-20/en.md) | [AI日報：千問3.8模型將發佈；字節發佈Seed Audio 1.0；面壁智能開…](daily/2026-07-20/tw.md) | [AI日報：千問3.8モデルがリリース予定；バイチューブがSeed Audio 1…](daily/2026-07-20/ja.md) |
| **2026-07-18** | [AI日报：开源模型Kimi K3登场；Google Vids引入Gemini O…](daily/2026-07-18/zh.md) | [AI Daily: Open Source Model Kimi K3 Make…](daily/2026-07-18/en.md) | [AI日報：開源模型Kimi K3登場；Google Vids引入Gemini O…](daily/2026-07-18/tw.md) | [AIニュース：オープンソースモデルKimi K3登場；Google VidsにG…](daily/2026-07-18/ja.md) |
| **2026-07-17** | [AI日报：开源模型Kimi K3登场；Google Vids引入Gemini O…](daily/2026-07-17/zh.md) | [AI Daily: Open Source Model Kimi K3 Make…](daily/2026-07-17/en.md) | [AI日報：開源模型Kimi K3登場；Google Vids引入Gemini O…](daily/2026-07-17/tw.md) | [AIニュース：オープンソースモデルKimi K3登場；Google VidsにG…](daily/2026-07-17/ja.md) |
| **2026-07-16** | [AI日报：MiniMax Code 2.0桌面端发布；Kimi K3模型预热视频…](daily/2026-07-16/zh.md) | [AI Daily: MiniMax Code 2.0 Desktop Versi…](daily/2026-07-16/en.md) | [AI日報：MiniMax Code 2.0桌面端發佈；Kimi K3模型預熱視頻…](daily/2026-07-16/tw.md) | [AI日報：MiniMax Code 2.0デスクトップ版リリース；Kimi K3…](daily/2026-07-16/ja.md) |
| **2026-07-15** | [AI日报：豆包千问同日下线智能体功能；GPT-5.6Sol被曝自主删除用户数据库…](daily/2026-07-15/zh.md) | [AI Daily: DouBao and QianWen Discontinue…](daily/2026-07-15/en.md) | [AI日報：豆包千問同日下線智能體功能；GPT-5.6Sol被曝自主刪除用戶數據庫…](daily/2026-07-15/tw.md) | [AI日報：ドウボー・ワンウェンが同日にスマートエージェント機能を終了；GPT-5…](daily/2026-07-15/ja.md) |
| **2026-07-14** | [AI日报：混元发布HyOCR-1.5；PixVerse完成4.39亿美元融资；商…](daily/2026-07-14/zh.md) | [AI Daily: Hengyuan Releases HyOCR-1.5; P…](daily/2026-07-14/en.md) | [AI日報：混元發佈HyOCR-1.5；PixVerse完成4.39億美元融資；商…](daily/2026-07-14/tw.md) | [AI日報：フンユアンがHyOCR-1.5をリリース；PixVerseが4億390…](daily/2026-07-14/ja.md) |
| **2026-07-13** | [AI日报：抖音电商将豆包纳入抖店结算序列;Claude Fable5访问权限延长…](daily/2026-07-13/zh.md) | [AI Daily: Douyin E-commerce Integrates D…](daily/2026-07-13/en.md) | [AI日報：抖音電商將豆包納入抖店結算序列;Claude Fable5訪問權限延長…](daily/2026-07-13/tw.md) | [AIニュース：抖音电商は豆包をドットストアの決済フローに組み込み；Claude …](daily/2026-07-13/ja.md) |
| **2026-07-10** | [AI日报：SpaceXAI推出“Opus级”大模型Grok4.5;阶跃星辰首款A…](daily/2026-07-10/zh.md) | [AI Daily: SpaceXAI Launches Opus-Level L…](daily/2026-07-10/en.md) | [AI日報：SpaceXAI推出“Opus級”大模型Grok4.5;階躍星辰首款A…](daily/2026-07-10/tw.md) | [AI日報：SpaceXAIがOpus級の大規模モデルGrok4.5を発表；段階の…](daily/2026-07-10/ja.md) |
<!-- END_INDEX -->

## License & 数据来源

内容版权归原作者 / [aibase.com](https://news.aibase.com/) 所有，本仓库仅作个人学习与归档用途。
