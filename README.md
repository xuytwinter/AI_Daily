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
| **2026-06-23** | [AI日报：火山引擎发布豆包Seedance2.5等模型；生数Vidu Q3上线华…](daily/2026-06-23/zh.md) | [AI Daily: Volcano Engine launches Doubao…](daily/2026-06-23/en.md) | [AI日報：火山引擎發佈豆包Seedance2.5等模型；生數Vidu Q3上線華…](daily/2026-06-23/tw.md) | [AI日報：ボルカノエンジンがドウバオSeedance2.5などモデルを公開；シャ…](daily/2026-06-23/ja.md) |
| **2026-06-22** | [AI日报：阿里发布HappyHorse 1.1；字节豆包灰测网约车服务；三星12…](daily/2026-06-22/zh.md) | [AI Daily: Alibaba Launches HappyHorse 1.…](daily/2026-06-22/en.md) | [AI日報：阿里發佈HappyHorse 1.1；字節豆包灰測網約車服務；三星12…](daily/2026-06-22/tw.md) | [AI日報：アリババがHappyHorse 1.1を発表；字節跳動のドウボーがタク…](daily/2026-06-22/ja.md) |
| **2026-06-19** | [AI日报：通义开源首个统一科学大模型LOGOS、AI情感陪伴App妙时宣布停运；…](daily/2026-06-19/zh.md) | [AI Daily: Tongyi Opensources Its First U…](daily/2026-06-19/en.md) | [AI日報：通義開源首個統一科學大模型LOGOS、AI情感陪伴App妙時宣佈停運；…](daily/2026-06-19/tw.md) | [AI日報：通義が初めての統一科学大モデルLOGOSをオープンソース化、AI感情パ…](daily/2026-06-19/ja.md) |
| **2026-06-18** | [AI日报：通义开源首个统一科学大模型LOGOS、AI情感陪伴App妙时宣布停运；…](daily/2026-06-18/zh.md) | [AI Daily: Tongyi Opensources Its First U…](daily/2026-06-18/en.md) | [AI日報：通義開源首個統一科學大模型LOGOS、AI情感陪伴App妙時宣佈停運；…](daily/2026-06-18/tw.md) | [AI日報：通義が初めての統一科学大モデルLOGOSをオープンソース化、AI感情パ…](daily/2026-06-18/ja.md) |
| **2026-06-17** | [AI日报：微信支付推出“AI专属卡“；小米龙虾MiMo Claw正式版发布;智谱…](daily/2026-06-17/zh.md) | [AI Daily: WeChat Pay Launches AI Dedicat…](daily/2026-06-17/en.md) | [AI日報：微信支付推出“AI專屬卡“；小米龍蝦MiMo Claw正式版發佈;智譜…](daily/2026-06-17/tw.md) | [AI日報：微信支払いがAI専用カードを発表；小米のロブタMiMo Claw正式版…](daily/2026-06-17/ja.md) |
| **2026-06-16** | [AI日报：字节发布Seedance 2.0 Mini；Kimi 2.7 Code…](daily/2026-06-16/zh.md) | [AI Daily: ByteDance Launches Seedance 2.…](daily/2026-06-16/en.md) | [AI日報：字節發佈Seedance 2.0 Mini；Kimi 2.7 Code…](daily/2026-06-16/tw.md) | [AI日報：バイツーがSeedance 2.0 Miniを発表；Kimi 2.7 …](daily/2026-06-16/ja.md) |
| **2026-06-15** | [AI日报：豆包上线任务模式；元宝正式打通ima公开知识库；智谱GLM-5. 2 …](daily/2026-06-15/zh.md) | [AI Daily: DouBao Launches Task Mode; Yua…](daily/2026-06-15/en.md) | [AI日報：豆包上線任務模式；元寶正式打通ima公開知識庫；智譜GLM-5. 2 …](daily/2026-06-15/tw.md) | [AI日報：ドウパオがタスクモードをリリース；ヤオバオがIMA公開知識ベースと統合…](daily/2026-06-15/ja.md) |
| **2026-06-13** | [AI日报：高德问店上线AI能力开放调用；大众点评严打AI灌水评论；Kimi将发行…](daily/2026-06-13/zh.md) | [AI Daily: Gaode Wenda Launches AI Capabi…](daily/2026-06-13/en.md) | [AI日報：高德問店上線AI能力開放調用；大衆點評嚴打AI灌水評論；Kimi將發行…](daily/2026-06-13/tw.md) | [AI日報：高徳問店にAI機能の開放呼び出し機能が登場；大衆評論はAIによるインフ…](daily/2026-06-13/ja.md) |
| **2026-06-12** | [AI日报：高德问店上线AI能力开放调用；大众点评严打AI灌水评论；Kimi将发行…](daily/2026-06-12/zh.md) | [AI Daily: Gaode Wenda Launches AI Capabi…](daily/2026-06-12/en.md) | [AI日報：高德問店上線AI能力開放調用；大衆點評嚴打AI灌水評論；Kimi將發行…](daily/2026-06-12/tw.md) | [AI日報：高徳問店にAI機能の開放呼び出し機能が登場；大衆評論はAIによるインフ…](daily/2026-06-12/ja.md) |
| **2026-06-11** | [AI日报：小米开源AI编程助手MiMo Code；京东MALL首批人形机器人上岗…](daily/2026-06-11/zh.md) | [AI Daily: Xiaomi Opensources AI Coding A…](daily/2026-06-11/en.md) | [AI日報：小米開源AI編程助手MiMo Code；京東MALL首批人形機器人上崗…](daily/2026-06-11/tw.md) | [AI日報：小米がAIプログラミングアシスタントMiMo Codeをオープンソース…](daily/2026-06-11/ja.md) |
| **2026-06-10** | [AI日报：美图秀秀入局微信AI生态：千问发布全周期高考志愿填报Agent；美团 …](daily/2026-06-10/zh.md) | [AI Daily: Meitu ShowShow Enters WeChat A…](daily/2026-06-10/en.md) | [AI日報：美圖秀秀入局微信AI生態：千問發佈全週期高考志願填報Agent；美團 …](daily/2026-06-10/tw.md) | [AI日報：ミートゥーシューシュで微信のAIエコシステムに参入。Qwenは全期間の…](daily/2026-06-10/ja.md) |
| **2026-06-09** | [AI日报：Kimi Code开源编码代理升级；苹果正面回应 iOS 27 AI …](daily/2026-06-09/zh.md) | [AI Daily: Kimi Code Open Source Coding A…](daily/2026-06-09/en.md) | [AI日報：Kimi Code開源編碼代理升級；蘋果正面迴應 iOS 27 AI …](daily/2026-06-09/tw.md) | [AI日報：Kimi Codeオープンソースコードエージェントのアップグレード；ア…](daily/2026-06-09/ja.md) |
<!-- END_INDEX -->

## License & 数据来源

内容版权归原作者 / [aibase.com](https://news.aibase.com/) 所有，本仓库仅作个人学习与归档用途。
