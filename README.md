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
| **2026-07-09** | [AI日报：SpaceXAI推出“Opus级”大模型Grok4.5;阶跃星辰首款A…](daily/2026-07-09/zh.md) | [AI Daily: SpaceXAI Launches Opus-Level L…](daily/2026-07-09/en.md) | [AI日報：SpaceXAI推出“Opus級”大模型Grok4.5;階躍星辰首款A…](daily/2026-07-09/tw.md) | [AI日報：SpaceXAIがOpus級の大規模モデルGrok4.5を発表；段階の…](daily/2026-07-09/ja.md) |
| **2026-07-08** | [AI日报：Claude Cowork登陆网页和手机端；美国放行GPT-5.6；M…](daily/2026-07-08/zh.md) | [AI Daily: Claude Cowork Launches on Web …](daily/2026-07-08/en.md) | [AI日報：Claude Cowork登陸網頁和手機端；美國放行GPT-5.6；M…](daily/2026-07-08/tw.md) | [AI日報：Claude Coworkがウェブとモバイル端末に登場；米国がGPT-…](daily/2026-07-08/ja.md) |
| **2026-07-07** | [AI日报：Claude Code更新v2.1.202版本；支付宝AI开放平台开启…](daily/2026-07-07/zh.md) | [AI Daily: Claude Code Updates to Version…](daily/2026-07-07/en.md) | [AI日報：Claude Code更新v2.1.202版本；支付寶AI開放平臺開啓…](daily/2026-07-07/tw.md) | [AI日報：Claude Codeがバージョン2.1.202にアップデート；支付宝…](daily/2026-07-07/ja.md) |
| **2026-07-06** | [AI日报：豆包、千问下线AI拟人化功能；腾讯混元Hy3发布；Gemini3.5 …](daily/2026-07-06/zh.md) | [AI Daily: DouBao and Qianwen Discontinue…](daily/2026-07-06/en.md) | [AI日報：豆包、千問下線AI擬人化功能；騰訊混元Hy3發佈；Gemini3.5 …](daily/2026-07-06/tw.md) | [AI日報：ドウボー、チンウェンがAIキャラクター化機能を終了；テンセント・混元H…](daily/2026-07-06/ja.md) |
| **2026-07-04** | [AI日报：阿里巴巴内部“反向禁用”Claude；微软纯网页版Aion系统曝光；C…](daily/2026-07-04/zh.md) | [AI Daily: Alibaba Internally Reverses Di…](daily/2026-07-04/en.md) | [AI日報：阿里巴巴內部“反向禁用”Claude；微軟純網頁版Aion系統曝光；C…](daily/2026-07-04/tw.md) | [AI日報：アリババが社内からClaudeを逆に無効化；マイクロソフトの純粋なウェ…](daily/2026-07-04/ja.md) |
| **2026-07-03** | [AI日报：阿里巴巴内部“反向禁用”Claude；微软纯网页版Aion系统曝光；C…](daily/2026-07-03/zh.md) | [AI Daily: Alibaba Internally Reverses Di…](daily/2026-07-03/en.md) | [AI日報：阿里巴巴內部“反向禁用”Claude；微軟純網頁版Aion系統曝光；C…](daily/2026-07-03/tw.md) | [AI日報：アリババが社内からClaudeを逆に無効化；マイクロソフトの純粋なウェ…](daily/2026-07-03/ja.md) |
| **2026-07-02** | [AI日报：可灵AI将完成30亿美元融资；支付宝AI生活助理“阿宝”正式公测；Ki…](daily/2026-07-02/zh.md) | [AI Daily: Kler AI Completes $3 Billion F…](daily/2026-07-02/en.md) | [AI日報：可靈AI將完成30億美元融資；支付寶AI生活助理“阿寶”正式公測；Ki…](daily/2026-07-02/tw.md) | [AI日報：クレアAIが30億ドルの資金調達を完了；支付宝のAIライフアシスタント…](daily/2026-07-02/ja.md) |
| **2026-07-01** | [AI日报：谷歌推新图片模型Nano Banana 2 Lite；Claude S…](daily/2026-07-01/zh.md) | [AI Daily: Google Launches New Image Mode…](daily/2026-07-01/en.md) | [AI日報：谷歌推新圖片模型Nano Banana 2 Lite；Claude S…](daily/2026-07-01/tw.md) | [AIニュース：グーグルが新画像モデル「Nano Banana 2 Lite」を発…](daily/2026-07-01/ja.md) |
| **2026-06-30** | [AI日报：美团发布LongCat-2.0；小红书 RedKnot 推理引擎开源；…](daily/2026-06-30/zh.md) | [AI Daily: Meituan Releases LongCat-2.0; …](daily/2026-06-30/en.md) | [AI日報：美團發佈LongCat-2.0；小紅書 RedKnot 推理引擎開源；…](daily/2026-06-30/tw.md) | [AI日報：美团がLongCat-2.0を発表；小紅書のRedKnot推論エンジン…](daily/2026-06-30/ja.md) |
| **2026-06-29** | — | [AI Daily: DouBao Tests Social Features; …](daily/2026-06-29/en.md) | [AI日報：豆包內測社交功能；高德內測“袋馬”入局AI編程；新浪VibeThink…](daily/2026-06-29/tw.md) | [AI日報：ドウバオがソーシャル機能のテストを開始；高徳が袋馬（マース）をAIプロ…](daily/2026-06-29/ja.md) |
| **2026-06-27** | [AI日报：苹果Xcode 26.6正式发布；美团“小店有AI”行动落地北京；Op…](daily/2026-06-27/zh.md) | [AI Daily: Apple Xcode 26.6 Released Offi…](daily/2026-06-27/en.md) | [AI日報：蘋果Xcode 26.6正式發佈；美團“小店有AI”行動落地北京；Op…](daily/2026-06-27/tw.md) | [AI日報：アップルXcode 26.6が正式リリース；メイドゥー・ショップにAI…](daily/2026-06-27/ja.md) |
| **2026-06-26** | [AI日报：苹果Xcode 26.6正式发布；美团“小店有AI”行动落地北京；Op…](daily/2026-06-26/zh.md) | [AI Daily: Apple Xcode 26.6 Released Offi…](daily/2026-06-26/en.md) | [AI日報：蘋果Xcode 26.6正式發佈；美團“小店有AI”行動落地北京；Op…](daily/2026-06-26/tw.md) | [AI日報：アップルXcode 26.6が正式リリース；メイドゥー・ショップにAI…](daily/2026-06-26/ja.md) |
| **2026-06-25** | [AI日报：iOS 27支持自由切换ChatGPT；百度文心网站全面扩容；Goog…](daily/2026-06-25/zh.md) | [AI Daily: iOS 27 Supports Free Switching…](daily/2026-06-25/en.md) | [AI日報：iOS 27支持自由切換ChatGPT；百度文心網站全面擴容；Goog…](daily/2026-06-25/tw.md) | [AI日報：iOS 27がChatGPTの自由な切り替えをサポート；バイドゥー文心…](daily/2026-06-25/ja.md) |
| **2026-06-24** | [AI日报：豆包音频生成模型1.0发布；企业微信内测AI Agent大圆；Curs…](daily/2026-06-24/zh.md) | [AI Daily: DouBao Audio Generation Model …](daily/2026-06-24/en.md) | [AI日報：豆包音頻生成模型1.0發佈；企業微信內測AI Agent大圓；Curs…](daily/2026-06-24/tw.md) | [AI日報：ドウバオ音声生成モデル1.0公開；企業WeChatでAIエージェントの…](daily/2026-06-24/ja.md) |
<!-- END_INDEX -->

## License & 数据来源

内容版权归原作者 / [aibase.com](https://news.aibase.com/) 所有，本仓库仅作个人学习与归档用途。
