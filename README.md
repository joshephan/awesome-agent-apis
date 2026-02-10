# Awesome Agent APIs [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of 2000+ public APIs designed for AI agents, automation, and programmatic access. Updated for the 2025-2026 AI agent ecosystem.

**Focus**: APIs that AI agents can use easily — minimal auth, JSON responses, high reliability, and agent-friendly documentation.

**What's New** (2025-2026):
- 🤖 **AI Agent Infrastructure** — Sandboxes, tool-use platforms, and agent execution environments
- 🔍 **AI Search APIs** — Purpose-built search for RAG pipelines and agent reasoning
- 🔗 **Agent Protocols** — MCP (Model Context Protocol), A2A (Agent2Agent), and interoperability standards
- 🧠 **New LLM Providers** — xAI Grok, DeepSeek, Qwen, Cerebras, OpenRouter, and more
- 📊 **Vector Databases** — Semantic search and agent memory APIs
- 🎨 **AI Generation** — Image, video, and music generation APIs
- 🛡️ **AI Safety** — Guardrails and content moderation for agent outputs

**Auth Types**:
- 🟢 **No** — No authentication required
- 🟡 **API Key** — Requires API key (usually free tier available)
- 🔴 **OAuth** — Requires OAuth flow (may be complex for simple agents)

---

## Contents

### 🔥 New — AI Agent Ecosystem (2025-2026)
- [AI Agent Infrastructure & Sandboxes](#-ai-agent-infrastructure--sandboxes)
- [AI Search APIs](#-ai-search-apis)
- [Agent Protocols & Standards](#-agent-protocols--standards)
- [LLM Provider APIs (Extended)](#-llm-provider-apis-extended)
- [Vector Databases & Embeddings](#-vector-databases--embeddings)
- [AI Image & Video Generation](#-ai-image--video-generation)
- [Knowledge Graphs & Structured Data](#️-knowledge-graphs--structured-data)
- [AI Safety & Guardrails](#️-ai-safety--guardrails)
- [Geospatial & Earth Observation](#-geospatial--earth-observation)
- [Real-Time Data & Streaming APIs](#-real-time-data--streaming-apis)
- [AI Coding & Development APIs](#-ai-coding--development-apis)
- [MCP Servers & Tool Ecosystem](#-mcp-servers--tool-ecosystem)
- [Web3 & Decentralized Agent Infrastructure](#-web3--decentralized-agent-infrastructure)
- [Uptime Monitoring & Status APIs](#-uptime-monitoring--status-apis)
- [Developer Utility & Testing APIs](#-developer-utility--testing-apis)
- [Mobile & Cross-Platform APIs](#-mobile--cross-platform-apis)
- [Open Data & Government APIs (Extended)](#️-open-data--government-apis-extended)
- [Conversion & Enrichment APIs](#-conversion--enrichment-apis)
- [AI Voice & Telephony APIs](#-ai-voice--telephony-apis)
- [AI Payment & Commerce APIs](#-ai-payment--commerce-apis)
- [Cybersecurity & Threat Intelligence APIs](#-cybersecurity--threat-intelligence-apis)
- [Climate & Sustainability APIs](#-climate--sustainability-apis)
- [Backend-as-a-Service & Database APIs](#️-backend-as-a-service--database-apis)
- [Workflow Automation APIs](#-workflow-automation-apis)
- [Email & Marketing APIs](#-email--marketing-apis)
- [Infrastructure-as-Code & DevOps APIs](#️-infrastructure-as-code--devops-apis)
- [Math, Science & Research APIs](#-math-science--research-apis)
- [Esports & Competitive Gaming APIs](#-esports--competitive-gaming-apis)
- [Legal & Compliance APIs](#️-legal--compliance-apis)
- [Education & EdTech APIs](#-education--edtech-apis)
- [IoT & Smart Home APIs](#-iot--smart-home-apis)
- [Document AI & OCR APIs](#-document-ai--ocr-apis)
- [Translation & Localization APIs](#-translation--localization-apis)
- [CRM APIs](#-crm-apis)
- [Project Management APIs](#-project-management-apis)
- [Real Estate & Property APIs](#️-real-estate--property-apis)
- [Travel & Booking APIs](#️-travel--booking-apis)
- [HR, People & Payroll APIs](#-hr-people--payroll-apis)
- [Supply Chain & Logistics APIs](#-supply-chain--logistics-apis)
- [Insurance APIs](#️-insurance-apis)
- [Agriculture & AgTech APIs](#-agriculture--agtech-apis)
- [3D Printing & Manufacturing APIs](#️-3d-printing--manufacturing-apis)
- [Accessibility & WCAG APIs](#-accessibility--wcag-apis)
- [Identity Verification & KYC APIs](#-identity-verification--kyc-apis)
- [Event & Ticketing APIs](#-event--ticketing-apis)
- [Fitness Wearable APIs](#-fitness-wearable-apis)
- [Space & Astronomy APIs](#-space--astronomy-apis)
- [Genealogy APIs](#-genealogy-apis)
- [Pet Services APIs](#-pet-services-apis)
- [Renewable Energy APIs](#-renewable-energy-apis)
- [Construction & Building APIs](#️-construction--building-apis)
- [Maritime & Vessel Tracking APIs](#-maritime--vessel-tracking-apis)
- [Clinical & FHIR Health APIs](#-clinical--fhir-health-apis)
- [RPA & Automation Platform APIs](#-rpa--automation-platform-apis)
- [Data Visualization & Charting APIs](#-data-visualization--charting-apis)
- [Background Check & Screening APIs](#-background-check--screening-apis)
- [Media Monitoring & Brand Intelligence APIs](#-media-monitoring--brand-intelligence-apis)
- [Helpdesk & Customer Support APIs](#-helpdesk--customer-support-apis)
- [Loyalty & Rewards Program APIs](#-loyalty--rewards-program-apis)
- [Warehouse Management APIs](#-warehouse-management-apis)
- [Digital Asset Management APIs](#-digital-asset-management-apis)
- [Contract Management (CLM) APIs](#-contract-management-clm-apis)
- [Competitive Intelligence & Pricing APIs](#-competitive-intelligence--pricing-apis)
- [ESG & Sustainability Reporting APIs](#-esg--sustainability-reporting-apis)
- [Tax Calculation & Compliance APIs](#-tax-calculation--compliance-apis)
- [Public Safety & Emergency APIs](#-public-safety--emergency-apis)
- [Podcast Platform APIs](#️-podcast-platform-apis)
- [Language Learning & Dictionary APIs](#-language-learning--dictionary-apis)
- [Nonprofit & Donation APIs](#-nonprofit--donation-apis)
- [Domain & DNS Management APIs](#-domain--dns-management-apis)
- [Survey & Form Builder APIs](#-survey--form-builder-apis)
- [Screenshot & Website Preview APIs](#-screenshot--website-preview-apis)
- [QR Code & Barcode Generation APIs](#-qr-code--barcode-generation-apis)
- [Meeting Scheduling & Booking APIs](#-meeting-scheduling--booking-apis)
- [Live Chat & Messaging APIs](#-live-chat--messaging-apis)
- [Product Information Management (PIM) APIs](#-product-information-management-pim-apis)
- [Fleet Management & Telematics APIs](#-fleet-management--telematics-apis)
- [Billing, Invoice & Subscription APIs](#-billing-invoice--subscription-apis)
- [eSignature & Signature Verification APIs](#️-esignature--signature-verification-apis)
- [Nutrition & Food Data APIs](#-nutrition--food-data-apis)
- [Sentiment Analysis & Emotion Detection APIs](#-sentiment-analysis--emotion-detection-apis)
- [Resume Parsing & Talent APIs](#-resume-parsing--talent-apis)
- [Push Notification APIs](#-push-notification-apis)
- [Content Moderation & NSFW Detection APIs](#️-content-moderation--nsfw-detection-apis)
- [Geofencing & Location-Based APIs](#-geofencing--location-based-apis)
- [Reservation & Booking APIs](#️-reservation--booking-apis)
- [Review & Rating Management APIs](#-review--rating-management-apis)
- [Video Conferencing APIs](#-video-conferencing-apis)
- [Document Collaboration APIs](#-document-collaboration-apis)
- [Address Validation & Geocoding APIs](#-address-validation--geocoding-apis)
- [Product Analytics APIs](#-product-analytics-apis)
- [Feature Flag & Toggle APIs](#-feature-flag--toggle-apis)
- [Error Tracking & Monitoring APIs](#-error-tracking--monitoring-apis)
- [Secrets Management APIs](#-secrets-management-apis)
- [CDN & Content Delivery APIs](#-cdn--content-delivery-apis)
- [Database Migration & Schema APIs](#️-database-migration--schema-apis)

### General Categories
- [Betting & Prediction Markets](#betting--prediction-markets)
- [Blockchain & Crypto](#blockchain--crypto)
- [Data & Information](#data--information)
- [Weather](#weather)
- [Finance](#finance)
- [Search & Knowledge](#search--knowledge)
- [Communication](#communication)
- [Animals & Fun](#animals--fun)
- [Books & Literature](#books--literature)
- [Development Tools](#development-tools)
- [Entertainment & Media](#entertainment--media)
- [Location & Geography](#location--geography)
- [News](#news)
- [Science & Education](#science--education)
- [Sports & Fitness](#sports--fitness)
- [Test Data & Mocking](#test-data--mocking)
- [Transportation](#transportation)
- [Business & Productivity](#business--productivity)
- [Food & Drink](#food--drink)
- [Gaming](#gaming)
- [Health & Medical](#health--medical)
- [Art & Design](#art--design)
- [Music](#music)
- [Government & Open Data](#government--open-data)
- [Security & Verification](#security--verification)
- [No Auth Required (Quick Start)](#no-auth-required-quick-start)
- [Anime](#anime)
- [Calendar & Events](#calendar--events)
- [Cloud Storage & File Sharing](#cloud-storage--file-sharing)
- [Dictionaries & Language](#dictionaries--language)
- [Email](#email)
- [Machine Learning & AI](#machine-learning--ai)
- [Jobs & Careers](#jobs--careers)
- [Phone & SMS](#phone--sms)
- [Photography & Images](#photography--images)
- [Social Media](#social-media)
- [Video & Streaming](#video--streaming)
- [Shopping & E-commerce](#shopping--e-commerce)
- [URL Shorteners](#url-shorteners)
- [Tracking & Analytics](#tracking--analytics)
- [Environment & Sustainability](#environment--sustainability)
- [Vehicles & Transportation Tracking](#vehicles--transportation-tracking)
- [Podcasts & Audio](#podcasts--audio)
- [Text Analysis & NLP](#text-analysis--nlp)
- [Patents & Intellectual Property](#patents--intellectual-property)
- [Open Source Projects](#open-source-projects)
- [Personality & Fun Tests](#personality--fun-tests)
- [Continuous Integration & DevOps](#continuous-integration--devops)

---

## Betting & Prediction Markets

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [MoltBet](https://moltbet.dev) | P2P betting platform for AI agents with Moltbook verification | 🟢 No | ✅ | ✅⭐ |
| [Polymarket](https://docs.polymarket.com/) | Decentralized prediction market | 🟡 API Key | ✅ | ✅ |
| [Odds API](https://the-odds-api.com/) | Sports odds from multiple bookmakers | 🟡 API Key | ✅ | ✅ |

---

## Blockchain & Crypto

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [CoinGecko](http://www.coingecko.com/api) | Cryptocurrency prices, market data, and stats | 🟢 No | ✅ | ✅⭐ |
| [CoinCap](https://docs.coincap.io/) | Real-time cryptocurrency pricing | 🟢 No | ✅ | ✅ |
| [CoinDesk](https://old.coindesk.com/coindesk-api/) | Bitcoin Price Index (BPI) in multiple currencies | 🟢 No | ✅ | ✅ |
| [Coinlore](https://www.coinlore.com/cryptocurrency-data-api) | Cryptocurrency prices, volume and more | 🟢 No | ✅ | ✅ |
| [Coinpaprika](https://api.coinpaprika.com) | Cryptocurrency prices and market data | 🟢 No | ✅ | ✅ |
| [Blockchain.com](https://www.blockchain.com/api) | Bitcoin blockchain data | 🟢 No | ✅ | ✅ |
| [Mempool](https://mempool.space/api) | Bitcoin transaction fee API | 🟢 No | ✅ | ✅ |
| [CoinMarketCap](https://coinmarketcap.com/api/) | Cryptocurrency prices and market data | 🟡 API Key | ✅ | ✅ |
| [Binance](https://github.com/binance/binance-spot-api-docs) | Cryptocurrency exchange trading | 🟡 API Key | ✅ | ✅ |
| [Coinbase](https://developers.coinbase.com) | Bitcoin, Ethereum, and more prices | 🟡 API Key | ✅ | ✅ |
| [Etherscan](https://etherscan.io/apis) | Ethereum blockchain explorer | 🟡 API Key | ✅ | ✅ |
| [Bitquery](https://graphql.bitquery.io/ide) | Blockchain GraphQL APIs | 🟡 API Key | ✅ | ✅ |

---

## Data & Information

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Wikipedia](https://www.mediawiki.org/wiki/API:Main_page) | Access Wikipedia content | 🟢 No | ✅ | ✅⭐ |
| [REST Countries](https://restcountries.com) | Country information and data | 🟢 No | ✅ | ✅⭐ |
| [Open Library](https://openlibrary.org/developers/api) | Book data and covers | 🟢 No | ✅ | ✅ |
| [Wikidata](https://www.wikidata.org/wiki/Wikidata:Data_access) | Structured knowledge base | 🟢 No | ✅ | ✅ |
| [Nobel Prize](https://www.nobelprize.org/about/developer-zone-2/) | Open data about Nobel prizes and laureates | 🟢 No | ✅ | ✅ |
| [Universities List](https://github.com/Hipo/university-domains-list) | University names, countries and domains | 🟢 No | ✅ | ✅ |
| [IP API](https://ipapi.co/api/) | IP address geolocation | 🟢 No | ✅ | ✅ |
| [JSONPlaceholder](https://jsonplaceholder.typicode.com/) | Fake REST API for testing | 🟢 No | ✅ | ✅⭐ |
| [Numbers API](http://numbersapi.com/) | Interesting facts about numbers | 🟢 No | No | ✅ |
| [World Bank](https://datahelpdesk.worldbank.org/knowledgebase/topics/125589) | World development indicators | 🟢 No | ✅ | ✅ |
| [World Time API](http://worldtimeapi.org/) | Current time for timezone | 🟢 No | No | ✅⭐ |
| [TimeZoneDB](https://timezonedb.com/api) | Time zone database | 🟡 API Key | ✅ | ✅ |
| [IP API](https://ipapi.com/) | IP geolocation | 🟡 API Key | ✅ | ✅ |
| [Abstract IP Geolocation](https://www.abstractapi.com/ip-geolocation-api) | IP location | 🟡 API Key | ✅ | ✅ |
| [DB-IP](https://db-ip.com/api/) | IP geolocation database | 🟡 API Key | ✅ | ✅ |
| [ip-api](https://ip-api.com/docs) | IP geolocation | 🟢 No | No | ✅⭐ |
| [ipify](https://www.ipify.org/) | Get your public IP | 🟢 No | ✅ | ✅⭐ |
| [FreeGeoIP](https://freegeoip.app/) | IP geolocation | 🟢 No | ✅ | ✅ |
| [Country.is](https://country.is/) | Check visitor country | 🟢 No | ✅ | ✅ |
| [Geocodio](https://www.geocod.io/) | Geocoding | 🟡 API Key | ✅ | ✅ |
| [OpenCage](https://opencagedata.com/) | Geocoding | 🟡 API Key | ✅ | ✅ |
| [PositionStack](https://positionstack.com/) | Geocoding | 🟡 API Key | ✅ | ✅ |
| [What3Words](https://developer.what3words.com/) | Location addressing | 🟡 API Key | ✅ | ✅ |
| [Mapbox Geocoding](https://docs.mapbox.com/api/search/geocoding/) | Location search | 🟡 API Key | ✅ | ✅ |
| [Here Geocoding](https://developer.here.com/documentation/geocoding-search-api) | Address search | 🟡 API Key | ✅ | ✅ |

---

## Weather

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Open-Meteo](https://open-meteo.com/) | Free weather API with no key required | 🟢 No | ✅ | ✅⭐ |
| [wttr.in](https://github.com/chubin/wttr.in) | Weather in terminal format | 🟢 No | ✅ | ✅⭐ |
| [7Timer!](http://www.7timer.info/doc.php?lang=en) | Weather forecasts, especially for astronomy | 🟢 No | No | ✅ |
| [US Weather](https://www.weather.gov/documentation/services-web-api) | US National Weather Service | 🟢 No | ✅ | ✅ |
| [MetaWeather](https://www.metaweather.com/api/) | Weather data | 🟢 No | ✅ | ✅ |
| [OpenWeatherMap](https://openweathermap.org/api) | Weather data, forecasts, and maps | 🟡 API Key | ✅ | ✅ |
| [WeatherAPI](https://www.weatherapi.com/) | Weather and geolocation API | 🟡 API Key | ✅ | ✅ |
| [Tomorrow.io](https://www.tomorrow.io/weather-api/) | Weather intelligence | 🟡 API Key | ✅ | ✅ |
| [Visual Crossing](https://www.visualcrossing.com/weather-api) | Weather data | 🟡 API Key | ✅ | ✅ |
| [Storm Glass](https://stormglass.io/) | Marine weather | 🟡 API Key | ✅ | ✅ |
| [AEMET](https://opendata.aemet.es/centrodedescargas/inicio) | Spanish weather | 🟡 API Key | ✅ | ✅ |
| [Met Office](https://www.metoffice.gov.uk/services/data/datapoint) | UK weather | 🟡 API Key | ✅ | ✅ |
| [Weather Bit](https://www.weatherbit.io/api) | Weather forecasts | 🟡 API Key | ✅ | ✅ |
| [Weatherstack](https://weatherstack.com/) | Real-time weather | 🟡 API Key | ✅ | ✅ |
| [Ambee](https://www.getambee.com/) | Environmental data | 🟡 API Key | ✅ | ✅ |

---

## Finance

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Frankfurter](https://www.frankfurter.app/docs) | Currency exchange rates and conversion | 🟢 No | ✅ | ✅⭐ |
| [National Bank of Poland](http://api.nbp.pl/en.html) | Currency exchange rates (XML and JSON) | 🟢 No | ✅ | ✅ |
| [Econdb](https://www.econdb.com/api/) | Global macroeconomic data | 🟢 No | ✅ | ✅ |
| [Portfolio Optimizer](https://portfoliooptimizer.io/) | Portfolio analysis and optimization | 🟢 No | ✅ | ✅ |
| [ExchangeRate-API](https://www.exchangerate-api.com) | Currency conversion | 🟡 API Key | ✅ | ✅ |
| [Alpha Vantage](https://www.alphavantage.co/documentation/) | Stock market data | 🟡 API Key | ✅ | ✅ |
| [Finage](https://finage.co.uk) | Stock, forex, and crypto market data | 🟡 API Key | ✅ | ✅ |
| [IEX Cloud](https://iexcloud.io/docs/api/) | Stock market data | 🟡 API Key | ✅ | ✅⭐ |
| [Finnhub](https://finnhub.io/docs/api) | Stock data | 🟡 API Key | ✅ | ✅⭐ |
| [Twelve Data](https://twelvedata.com/) | Stock market API | 🟡 API Key | ✅ | ✅ |
| [Polygon.io](https://polygon.io/docs/getting-started) | Financial market data | 🟡 API Key | ✅ | ✅ |
| [Yahoo Finance](https://www.yahoofinanceapi.com/) | Stock data | 🟡 API Key | ✅ | ✅ |
| [World Bank](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392) | Economic indicators | 🟢 No | ✅ | ✅⭐ |
| [FRED](https://fred.stlouisfed.org/docs/api/fred/) | Economic data | 🟡 API Key | ✅ | ✅ |
| [Quandl](https://docs.quandl.com/) | Financial data | 🟡 API Key | ✅ | ✅ |
| [CurrencyLayer](https://currencylayer.com/documentation) | Exchange rates | 🟡 API Key | ✅ | ✅ |
| [Fixer.io](https://fixer.io/documentation) | Currency exchange | 🟡 API Key | ✅ | ✅ |
| [Exchange Rates API](https://exchangeratesapi.io/) | Currency rates | 🟡 API Key | ✅ | ✅ |
| [Open Exchange Rates](https://openexchangerates.org/api) | Currency data | 🟡 API Key | ✅ | ✅ |
| [CurrencyBeacon](https://currencybeacon.com/) | Exchange rates | 🟡 API Key | ✅ | ✅ |
| [XE Currency](https://www.xe.com/xecurrencydata/) | Currency converter | 🟡 API Key | ✅ | ✅ |

---

## Search & Knowledge

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [DuckDuckGo Instant Answer](https://duckduckgo.com/api) | Search results without tracking | 🟢 No | ✅ | ⚠️ |
| [Wikidata](https://www.wikidata.org/wiki/Wikidata:Data_access) | Structured knowledge base | 🟢 No | ✅ | ✅ |
| [Archive.org](https://archive.readme.io/docs) | The Internet Archive | 🟢 No | ✅ | ✅ |
| [Brave Search](https://brave.com/search/api/) | Web search API | 🟡 API Key | ✅ | ✅ |

---

## Communication

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Moltbook](https://moltbook.com/developers) | Social network for AI agents | 🟡 API Key | ✅ | ✅⭐ |
| [Discord](https://discord.com/developers/docs/intro) | Gaming chat platform | 🟡 API Key | ✅ | ✅ |
| [Telegram Bot](https://core.telegram.org/bots/api) | Telegram messaging | 🟡 API Key | ✅ | ✅ |
| [SendGrid](https://docs.sendgrid.com/api-reference/) | Email delivery service | 🟡 API Key | ✅ | ✅ |

---

## Animals & Fun

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [HTTP Cat](https://http.cat/) | Cat images for every HTTP status code | 🟢 No | ✅ | ✅⭐ |
| [Dog CEO](https://dog.ceo/dog-api/) | Random dog images by breed | 🟢 No | ✅ | ✅⭐ |
| [Random Dog](https://random.dog/woof.json) | Random dog pictures | 🟢 No | ✅ | ✅ |
| [Random Fox](https://randomfox.ca/floof/) | Random fox pictures | 🟢 No | ✅ | ✅ |
| [Cat Facts](https://alexwohlbruck.github.io/cat-facts/) | Daily cat facts | 🟢 No | ✅ | ✅ |
| [Cataas](https://cataas.com/) | Cat as a service (cats pictures and gifs) | 🟢 No | ✅ | ✅ |
| [MeowFacts](https://github.com/wh-iterabb-it/meowfacts) | Random cat facts | 🟢 No | ✅ | ✅ |
| [Chuck Norris Jokes](https://api.chucknorris.io/) | Hand-curated Chuck Norris jokes | 🟢 No | ✅ | ✅⭐ |
| [Advice Slip](https://api.adviceslip.com/) | Random advice generator | 🟢 No | ✅ | ✅ |
| [HTTP Dog](https://http.dog/) | Dogs for every HTTP status code | 🟢 No | ✅ | ✅ |
| [RandomDuck](https://random-d.uk/api) | Random duck pictures | 🟢 No | ✅ | ✅ |
| [PlaceBear](https://placebear.com/) | Placeholder bear pictures | 🟢 No | ✅ | ✅ |
| [PlaceDog](https://place.dog) | Placeholder dog pictures | 🟢 No | ✅ | ✅ |
| [Dad Jokes](https://icanhazdadjoke.com/api) | Random dad jokes | 🟢 No | ✅ | ✅ |
| [Bored API](https://www.boredapi.com/) | Find things to do when bored | 🟢 No | ✅ | ✅ |
| [The Dog API](https://thedogapi.com/) | Dogs info, pictures and breeds | 🟡 API Key | ✅ | ✅ |
| [The Cat API](https://developers.thecatapi.com/) | Cat pictures from Tumblr | 🟡 API Key | ✅ | ✅ |
| [xeno-canto](https://xeno-canto.org/explore/api) | Bird recordings | 🟢 No | ✅ | ✅ |

---

## Books & Literature

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Open Library](https://openlibrary.org/developers/api) | Books, book covers and related data | 🟢 No | ✅ | ✅⭐ |
| [Google Books](https://developers.google.com/books/) | Search books | 🟡 API Key | ✅ | ✅ |
| [Gutendex](https://gutendex.com/) | Project Gutenberg books | 🟢 No | ✅ | ✅ |
| [PoetryDB](https://github.com/thundercomb/poetrydb) | Poetry database | 🟢 No | ✅ | ✅ |
| [Bible API](https://bible-api.com/) | Bible verses in multiple languages | 🟢 No | ✅ | ✅ |
| [Quran API](https://alquran.cloud/api) | Quran in multiple languages | 🟢 No | ✅ | ✅ |
| [Harry Potter API](https://github.com/fedeperin/potterapi) | Harry Potter data | 🟢 No | ✅ | ✅ |

---

## Development Tools

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [GitHub](https://docs.github.com/en/rest) | Access GitHub repositories | 🟡 API Key | ✅ | ✅⭐ |
| [JSONPlaceholder](https://jsonplaceholder.typicode.com/) | Fake REST API for testing | 🟢 No | ✅ | ✅⭐ |
| [ReqRes](https://reqres.in/) | Hosted REST-API for testing | 🟢 No | ✅ | ✅⭐ |
| [httpbin](https://httpbin.org/) | HTTP request & response service | 🟢 No | ✅ | ✅⭐ |
| [UUID Generator](https://www.uuidtools.com/api) | Generate UUIDs | 🟢 No | ✅ | ✅ |
| [Lorem Picsum](https://picsum.photos/) | Random placeholder images | 🟢 No | ✅ | ✅ |
| [Placeholder.com](https://placeholder.com/) | Generate placeholder images | 🟢 No | ✅ | ✅ |
| [DummyJSON](https://dummyjson.com/) | Fake REST API with realistic data | 🟢 No | ✅ | ✅⭐ |
| [JSON Generator](https://json-generator.com/api/) | Generate custom JSON data | 🟢 No | ✅ | ✅ |
| [Mocky](https://www.mocky.io/) | Mock HTTP responses | 🟢 No | ✅ | ✅ |
| [Cloudflare Trace](https://github.com/fawazahmed0/cloudflare-trace-api) | Get IP, user agent, country, and more | 🟢 No | ✅ | ✅ |
| [IPify](https://www.ipify.org/) | Simple IP address API | 🟢 No | ✅ | ✅ |
| [QR Code Generator](https://goqr.me/api/) | Generate QR codes | 🟢 No | ✅ | ✅ |

---

## Entertainment & Media

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [OMDb](http://www.omdbapi.com/) | Movie information | 🟡 API Key | ✅ | ✅ |
| [TVDB](https://thetvdb.com/api-information) | TV show database | 🟡 API Key | ✅ | ✅ |
| [Jikan](https://jikan.moe) | Unofficial MyAnimeList API | 🟢 No | ✅ | ✅ |
| [Studio Ghibli](https://ghibliapi.vercel.app/) | Studio Ghibli films data | 🟢 No | ✅ | ✅ |
| [PokéAPI](https://pokeapi.co) | Pokémon data | 🟢 No | ✅ | ✅⭐ |
| [Rick and Morty](https://rickandmortyapi.com/) | Rick and Morty characters and episodes | 🟢 No | ✅ | ✅ |
| [Star Wars API](https://swapi.dev/) | Star Wars universe data | 🟢 No | ✅ | ✅ |
| [Anime Facts](https://chandan-02.github.io/anime-facts-rest-api/) | Anime facts and quotes | 🟢 No | ✅ | ✅ |
| [Marvel](https://developer.marvel.com/) | Marvel comics data | 🟡 API Key | ✅ | ✅ |
| [Spotify](https://developer.spotify.com/documentation/web-api/) | Music catalog and user data | 🔴 OAuth | ✅ | ⚠️ |
| [TV Maze](https://www.tvmaze.com/api) | TV show database | 🟢 No | ✅ | ✅⭐ |
| [TMDb](https://www.themoviedb.org/documentation/api) | Movies and TV shows | 🟡 API Key | ✅ | ✅⭐ |
| [OMDb](http://www.omdbapi.com/) | Movie database | 🟡 API Key | ✅ | ✅⭐ |
| [TVDB](https://thetvdb.com/api-information) | TV database | 🟡 API Key | ✅ | ✅ |
| [Trakt](https://trakt.docs.apiary.io/) | Movie and TV tracking | 🔴 OAuth | ✅ | ⚠️ |
| [Tastekid](https://tastedive.com/read/api) | Recommendations | 🟡 API Key | ✅ | ✅ |
| [Kitsu](https://kitsu.docs.apiary.io/) | Anime tracking | 🔴 OAuth | ✅ | ⚠️ |
| [An API of Ice and Fire](https://anapioficeandfire.com/) | Game of Thrones data | 🟢 No | ✅ | ✅ |
| [Breaking Bad API](https://breakingbadapi.com/documentation) | Breaking Bad data | 🟢 No | ✅ | ✅ |
| [Final Space API](https://finalspaceapi.com/) | Final Space data | 🟢 No | ✅ | ✅ |
| [The One API](https://the-one-api.dev/) | Lord of the Rings data | 🟡 API Key | ✅ | ✅ |
| [Stranger Things API](https://strangerthingsapi.com/) | Stranger Things data | 🟢 No | ✅ | ✅ |
| [Comic Vine](https://comicvine.gamespot.com/api/) | Comic book database | 🟡 API Key | ✅ | ✅ |
| [xkcd](https://xkcd.com/json.html) | xkcd comics | 🟢 No | ✅ | ✅⭐ |
| [Marvel Comics](https://developer.marvel.com/) | Marvel universe | 🟡 API Key | ✅ | ✅ |

---

## Location & Geography

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [REST Countries](https://restcountries.com) | Country information | 🟢 No | ✅ | ✅⭐ |
| [Zippopotam](https://www.zippopotam.us/) | Postal code lookup | 🟢 No | No | ✅ |
| [Geocode](https://geocode.xyz/) | Geocoding and reverse geocoding | 🟢 No | ✅ | ✅ |
| [IP Geolocation](https://ipapi.co/) | IP address location | 🟢 No | ✅ | ✅ |
| [TimeAPI](https://www.timeapi.io/) | Time zone and date conversion | 🟢 No | ✅ | ✅ |
| [Sunrise Sunset](https://sunrise-sunset.org/api) | Sunset and sunrise times | 🟢 No | ✅ | ✅ |
| [Google Maps](https://developers.google.com/maps) | Maps, geocoding, directions | 🟡 API Key | ✅ | ✅ |
| [Mapbox](https://docs.mapbox.com/api/overview/) | Maps and location services | 🟡 API Key | ✅ | ✅ |

---

## News

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [New York Times](https://developer.nytimes.com/apis) | NYT articles and archives | 🟡 API Key | ✅ | ✅ |
| [News API](https://newsapi.org/) | Headlines and articles from news sources | 🟡 API Key | ✅ | ✅ |
| [The Guardian](https://open-platform.theguardian.com/) | Guardian news articles | 🟡 API Key | ✅ | ✅ |
| [Hacker News](https://github.com/HackerNews/API) | Hacker News items | 🟢 No | ✅ | ✅⭐ |
| [NewsData.io](https://newsdata.io/docs) | News aggregator | 🟡 API Key | ✅ | ✅ |
| [Currents API](https://currentsapi.services/en) | News articles | 🟡 API Key | ✅ | ✅ |
| [GNews](https://gnews.io/) | News API | 🟡 API Key | ✅ | ✅ |
| [NewsAPI.org](https://newsapi.org/) | News aggregator | 🟡 API Key | ✅ | ✅⭐ |
| [MediaStack](https://mediastack.com/) | News data | 🟡 API Key | ✅ | ✅ |
| [Bing News](https://www.microsoft.com/en-us/bing/apis/bing-news-search-api) | News search | 🟡 API Key | ✅ | ✅ |
| [Cryptocurrency News](https://cryptonews-api.com/) | Crypto news | 🟡 API Key | ✅ | ✅ |
| [Spaceflight News](https://spaceflightnewsapi.net/) | Space news | 🟢 No | ✅ | ✅⭐ |
| [Dev.to](https://developers.forem.com/api/) | Developer community articles | 🟡 API Key | ✅ | ✅ |

---

## Science & Education

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [NASA](https://api.nasa.gov/) | NASA data including imagery | 🟡 API Key | ✅ | ✅⭐ |
| [SpaceX](https://github.com/r-spacex/SpaceX-API) | SpaceX launches, rockets, and capsules | 🟢 No | ✅ | ✅⭐ |
| [arXiv](https://arxiv.org/help/api/) | Scientific papers | 🟢 No | ✅ | ✅ |
| [Crossref](https://www.crossref.org/documentation/retrieve-metadata/rest-api/) | Academic metadata | 🟢 No | ✅ | ✅ |
| [Open Notify](http://open-notify.org/Open-Notify-API/) | ISS location | 🟢 No | No | ✅ |
| [Wolfram Alpha](https://products.wolframalpha.com/api/) | Computational knowledge | 🟡 API Key | ✅ | ✅ |
| [Newton](https://newton.vercel.app/) | Mathematical calculations | 🟢 No | ✅ | ✅ |
| [Numbers API](http://numbersapi.com/) | Math and trivia facts | 🟢 No | No | ✅ |

---

## Sports & Fitness

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Football Data](https://www.football-data.org/) | Football data and stats | 🟡 API Key | ✅ | ✅ |
| [NBA API](https://sportsdata.io/developers/api-documentation/nba) | NBA scores and stats | 🟡 API Key | ✅ | ✅ |
| [TheSportsDB](https://www.thesportsdb.com/api.php) | Sports database | 🟡 API Key | ✅ | ✅ |
| [Balldontlie](https://www.balldontlie.io/) | NBA stats | 🟢 No | ✅ | ✅ |
| [Wger](https://wger.de/en/software/api) | Workout and exercise database | 🟡 API Key | ✅ | ✅ |
| [API-Football](https://www.api-football.com/) | Football/Soccer data | 🟡 API Key | ✅ | ✅⭐ |
| [API-NBA](https://api-sports.io/documentation/nba) | Basketball data | 🟡 API Key | ✅ | ✅ |
| [API-Baseball](https://api-sports.io/documentation/baseball) | Baseball data | 🟡 API Key | ✅ | ✅ |
| [API-Hockey](https://api-sports.io/documentation/hockey) | Hockey stats | 🟡 API Key | ✅ | ✅ |
| [SportsData.io](https://sportsdata.io/) | Sports data feeds | 🟡 API Key | ✅ | ✅ |
| [ESPN](http://www.espn.com/apis/devcenter/) | Sports news and scores | 🟡 API Key | ✅ | ✅ |
| [Sportsradar](https://developer.sportradar.com/) | Sports data | 🟡 API Key | ✅ | ✅ |
| [OpenLigaDB](https://www.openligadb.de/) | German sports leagues | 🟢 No | ✅ | ✅⭐ |
| [CollegeFootballData](https://collegefootballdata.com/) | College football | 🟡 API Key | ✅ | ✅ |
| [F1 API](https://ergast.com/mrd/) | Formula 1 data | 🟢 No | ✅ | ✅⭐ |
| [NBA Stats](https://github.com/swar/nba_api) | NBA statistics | 🟢 No | ✅ | ✅ |
| [NHL API](https://gitlab.com/dword4/nhlapi) | Hockey stats | 🟢 No | ✅ | ✅ |
| [MLB Stats](http://statsapi.mlb.com/docs/) | Baseball statistics | 🟢 No | ✅ | ✅ |
| [CricketAPI](https://www.cricketapi.com/) | Cricket data | 🟡 API Key | ✅ | ✅ |
| [Strava](https://developers.strava.com/) | Fitness tracking | 🔴 OAuth | ✅ | ⚠️ |

---

## Test Data & Mocking

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [JSONPlaceholder](https://jsonplaceholder.typicode.com/) | Fake REST API for testing | 🟢 No | ✅ | ✅⭐ |
| [ReqRes](https://reqres.in/) | Hosted REST-API for testing | 🟢 No | ✅ | ✅⭐ |
| [httpbin](https://httpbin.org/) | HTTP request & response service | 🟢 No | ✅ | ✅⭐ |
| [DummyJSON](https://dummyjson.com/) | Fake REST API with realistic data | 🟢 No | ✅ | ✅⭐ |
| [Random User](https://randomuser.me/) | Generate random user data | 🟢 No | ✅ | ✅⭐ |
| [Random Data API](https://random-data-api.com/) | Generate various random data | 🟢 No | ✅ | ✅ |
| [Faker API](https://fakerapi.it/en) | Generate fake data | 🟢 No | ✅ | ✅ |

---

## Transportation

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Transport for London](https://api.tfl.gov.uk/) | London transport data | 🟡 API Key | ✅ | ✅ |
| [AviationStack](https://aviationstack.com/) | Flight tracking | 🟡 API Key | ✅ | ✅ |
| [OpenSky Network](https://openskynetwork.github.io/opensky-api/) | Real-time flight data | 🟢 No | ✅ | ✅ |

---

## Business & Productivity

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Clearbit](https://clearbit.com/docs) | Business intelligence | 🟡 API Key | ✅ | ✅ |
| [Hunter](https://hunter.io/api-documentation) | Email finder | 🟡 API Key | ✅ | ✅ |
| [Abstract Email Validation](https://www.abstractapi.com/api/email-verification-validation-api) | Email verification | 🟡 API Key | ✅ | ✅ |
| [Trello](https://developer.atlassian.com/cloud/trello/rest/) | Project management | 🟡 API Key | ✅ | ✅ |

---

## Food & Drink

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [TheMealDB](https://www.themealdb.com/api.php) | Meal recipes | 🟡 API Key | ✅ | ✅ |
| [TheCocktailDB](https://www.thecocktaildb.com/api.php) | Cocktail recipes | 🟡 API Key | ✅ | ✅ |
| [Open Food Facts](https://world.openfoodfacts.org/data) | Food products database | 🟢 No | ✅ | ✅ |
| [Edamam Recipe](https://developer.edamam.com/edamam-recipe-api) | Recipe search | 🟡 API Key | ✅ | ✅ |
| [Open Food Facts](https://world.openfoodfacts.org/data) | Food products database | 🟢 No | ✅ | ✅⭐ |
| [Spoonacular](https://spoonacular.com/food-api) | Food and recipe data | 🟡 API Key | ✅ | ✅⭐ |
| [Edamam Food](https://developer.edamam.com/food-database-api) | Nutrition data | 🟡 API Key | ✅ | ✅ |
| [USDA FoodData Central](https://fdc.nal.usda.gov/api-guide.html) | Food nutrition | 🟡 API Key | ✅ | ✅⭐ |
| [Nutritionix](https://www.nutritionix.com/business/api) | Nutrition database | 🟡 API Key | ✅ | ✅ |
| [FatSecret](https://platform.fatsecret.com/api/) | Food and nutrition | 🔴 OAuth | ✅ | ⚠️ |
| [PunkAPI](https://punkapi.com/documentation/v2) | Craft beer recipes | 🟢 No | ✅ | ✅⭐ |
| [Fruityvice](https://www.fruityvice.com/) | Fruit nutrition data | 🟢 No | ✅ | ✅⭐ |
| [Coffee](https://sampleapis.com/api-list/coffee) | Coffee data | 🟢 No | ✅ | ✅ |
| [Tasty](https://rapidapi.com/apidojo/api/tasty) | Recipes and videos | 🟡 API Key | ✅ | ✅ |

---

## Gaming

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [PokéAPI](https://pokeapi.co) | Pokémon data | 🟢 No | ✅ | ✅⭐ |
| [Steam](https://steamcommunity.com/dev) | Steam game data | 🟡 API Key | ✅ | ✅ |
| [RAWG](https://rawg.io/apidocs) | Video game database | 🟡 API Key | ✅ | ✅ |
| [Riot Games](https://developer.riotgames.com/) | League of Legends data | 🟡 API Key | ✅ | ✅ |
| [RAWG](https://rawg.io/apidocs) | Video game database | 🟡 API Key | ✅ | ✅⭐ |
| [IGDB](https://api-docs.igdb.com/) | Game database | 🟡 API Key | ✅ | ✅⭐ |
| [CheapShark](https://apidocs.cheapshark.com/) | Game deals | 🟢 No | ✅ | ✅⭐ |
| [GamerPower](https://www.gamerpower.com/api-read) | Free games and loot | 🟢 No | ✅ | ✅⭐ |
| [Steam](https://steamcommunity.com/dev) | PC gaming platform | 🟡 API Key | ✅ | ✅⭐ |
| [Riot Games](https://developer.riotgames.com/) | League of Legends, Valorant | 🟡 API Key | ✅ | ✅ |
| [Fortnite](https://fortniteapi.io/) | Fortnite stats | 🟡 API Key | ✅ | ✅ |
| [Battlefield](https://gametools.network/docs) | Battlefield stats | 🟢 No | ✅ | ✅ |
| [Hypixel](https://api.hypixel.net/) | Minecraft server API | 🟡 API Key | ✅ | ✅ |
| [Mojang](https://wiki.vg/Mojang_API) | Minecraft API | 🟢 No | ✅ | ✅ |
| [AmiiboAPI](https://amiiboapi.com/) | Nintendo Amiibo data | 🟢 No | ✅ | ✅ |
| [Deck of Cards](https://deckofcardsapi.com/) | Playing cards API | 🟢 No | ✅ | ✅⭐ |
| [Clash of Clans](https://developer.clashofclans.com/) | CoC game data | 🟡 API Key | ✅ | ✅ |
| [Clash Royale](https://developer.clashroyale.com/) | Clash Royale data | 🟡 API Key | ✅ | ✅ |
| [Brawl Stars](https://developer.brawlstars.com/) | Brawl Stars API | 🟡 API Key | ✅ | ✅ |

---

## Health & Medical

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [COVID-19 Data](https://disease.sh/) | COVID-19 statistics | 🟢 No | ✅ | ✅ |
| [FDA Drug](https://open.fda.gov/apis/) | FDA drug information | 🟢 No | ✅ | ✅ |
| [Nutritionix](https://developer.nutritionix.com/) | Nutrition data | 🟡 API Key | ✅ | ✅ |
| [Drugs.com](https://www.drugs.com/apps/api/) | Drug information | 🟡 API Key | ✅ | ✅ |
| [RxNorm](https://rxnav.nlm.nih.gov/APIsOverview.html) | Medication naming | 🟢 No | ✅ | ✅⭐ |
| [DailyMed](https://dailymed.nlm.nih.gov/dailymed/app-support-web-services.cfm) | Medication labels | 🟢 No | ✅ | ✅ |
| [OpenFDA](https://open.fda.gov/apis/) | FDA data | 🟢 No | ✅ | ✅⭐ |
| [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/api/) | Genomic data | 🟡 API Key | ✅ | ✅ |
| [Healthcare.gov](https://www.healthcare.gov/developers/) | Health insurance | 🟢 No | ✅ | ✅ |
| [Disease.sh](https://disease.sh/docs/) | COVID-19 and disease data | 🟢 No | ✅ | ✅⭐ |
| [Infermedica](https://developer.infermedica.com/) | Medical AI | 🟡 API Key | ✅ | ✅ |
| [Lexigram](https://docs.lexigram.io/) | Medical NLP | 🟡 API Key | ✅ | ✅ |
| [UMLS](https://www.nlm.nih.gov/research/umls/knowledge_sources/metathesaurus/index.html) | Medical terminology | 🟡 API Key | ✅ | ✅ |

---

## Art & Design

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Rijksmuseum](https://data.rijksmuseum.nl/object-metadata/api/) | Art collection | 🟡 API Key | ✅ | ✅ |
| [Metropolitan Museum](https://metmuseum.github.io/) | Met Museum art collection | 🟢 No | ✅ | ✅ |
| [Art Institute Chicago](https://api.artic.edu/docs/) | Art institute collection | 🟢 No | ✅ | ✅ |
| [ColourLovers](http://www.colourlovers.com/api) | Color palettes | 🟢 No | ✅ | ✅ |
| [Lorem Picsum](https://picsum.photos/) | Random placeholder images | 🟢 No | ✅ | ✅ |

---

## Music

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Spotify](https://developer.spotify.com/documentation/web-api/) | Music catalog | 🔴 OAuth | ✅ | ⚠️ |
| [Last.fm](https://www.last.fm/api) | Music metadata | 🟡 API Key | ✅ | ✅ |
| [Deezer](https://developers.deezer.com/api) | Music database | 🟢 No | ✅ | ✅ |
| [Genius](https://docs.genius.com/) | Song lyrics | 🟡 API Key | ✅ | ✅ |
| [MusicBrainz](https://musicbrainz.org/doc/MusicBrainz_API) | Music metadata | 🟢 No | ✅ | ✅⭐ |
| [Discogs](https://www.discogs.com/developers) | Music database | 🟡 API Key | ✅ | ✅ |
| [Bandcamp](https://bandcamp.com/developer) | Music platform | 🟡 API Key | ✅ | ✅ |
| [Jamendo](https://developer.jamendo.com/v3.0) | Free music | 🟡 API Key | ✅ | ✅ |
| [SoundCloud](https://developers.soundcloud.com/docs/api/guide) | Audio platform | 🔴 OAuth | ✅ | ⚠️ |
| [Napster](https://developer.napster.com/) | Music streaming | 🟡 API Key | ✅ | ✅ |
| [Musixmatch](https://developer.musixmatch.com/) | Lyrics database | 🟡 API Key | ✅ | ✅ |
| [Genius](https://docs.genius.com/) | Song lyrics and annotations | 🟡 API Key | ✅ | ✅ |
| [LyricOVH](https://lyricsovh.docs.apiary.io/) | Simple lyrics API | 🟢 No | ✅ | ✅⭐ |
| [AudioDB](https://www.theaudiodb.com/api_guide.php) | Music database | 🟡 API Key | ✅ | ✅ |
| [Radio Browser](https://www.radio-browser.info/) | Internet radio stations | 🟢 No | ✅ | ✅⭐ |

---

## Government & Open Data

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Data.gov](https://api.data.gov/) | US government data | 🟡 API Key | ✅ | ✅ |
| [Open Parliament](https://www.ourcommons.ca/en/open-data) | Canadian parliament data | 🟢 No | ✅ | ✅ |
| [US Census](https://www.census.gov/data/developers/data-sets.html) | US Census data | 🟢 No | ✅ | ✅ |
| [FBI Crime Data](https://crime-data-explorer.fr.cloud.gov/api) | US crime statistics | 🟢 No | ✅ | ✅ |

---

## Security & Verification

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Have I Been Pwned](https://haveibeenpwned.com/API/v3) | Check if email has been breached | 🟡 API Key | ✅ | ✅ |
| [VirusTotal](https://developers.virustotal.com/reference/overview) | File/URL scanning | 🟡 API Key | ✅ | ✅ |
| [IPQualityScore](https://www.ipqualityscore.com/documentation/overview) | Fraud detection | 🟡 API Key | ✅ | ✅ |

---



---

## Anime

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [AniList](https://github.com/AniList/ApiV2-GraphQL-Docs) | Anime discovery & tracking | 🔴 OAuth | ✅ | ⚠️ |
| [Jikan](https://jikan.moe) | Unofficial MyAnimeList API | 🟢 No | ✅ | ✅⭐ |
| [Studio Ghibli](https://ghibliapi.herokuapp.com) | Studio Ghibli films data | 🟢 No | ✅ | ✅ |
| [Kitsu](https://kitsu.docs.apiary.io/) | Anime discovery platform | 🔴 OAuth | ✅ | ⚠️ |
| [AnimeChan](https://github.com/RocktimSaikia/anime-chan) | Anime quotes (over 10k+) | 🟢 No | ✅ | ✅ |
| [AnimeFacts](https://chandan-02.github.io/anime-facts-rest-api/) | Anime Facts (over 100+) | 🟢 No | ✅ | ✅ |
| [AnimeNewsNetwork](https://www.animenewsnetwork.com/encyclopedia/api.php) | Anime industry news | 🟢 No | ✅ | ✅ |
| [Danbooru Anime](https://danbooru.donmai.us/wiki_pages/help:api) | Anime artist database | 🟡 API Key | ✅ | ✅ |
| [MangaDex](https://api.mangadex.org/docs.html) | Manga Database and Community | 🟡 API Key | ✅ | ✅ |
| [MyAnimeList](https://myanimelist.net/clubs.php?cid=13727) | Anime and Manga Database | 🔴 OAuth | ✅ | ⚠️ |
| [NekosBest](https://docs.nekos.best) | Neko Images & Anime roleplaying GIFs | 🟢 No | ✅ | ✅ |
| [Waifu.pics](https://waifu.pics/docs) | Anime image sharing platform | 🟢 No | ✅ | ✅ |

---

## Calendar & Events

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Calendarific](https://calendarific.com/) | Worldwide Holidays | 🟡 API Key | ✅ | ✅ |
| [Nager.Date](https://date.nager.at) | Public holidays for 90+ countries | 🟢 No | ✅ | ✅⭐ |
| [Abstract Public Holidays](https://www.abstractapi.com/holidays-api) | National, regional, religious holidays | 🟡 API Key | ✅ | ✅ |
| [Google Calendar](https://developers.google.com/google-apps/calendar/) | Calendar events | 🔴 OAuth | ✅ | ⚠️ |
| [Festivo](https://docs.getfestivo.com/docs/products/public-holidays-api/intro) | Public holiday and observance service | 🟡 API Key | ✅ | ✅ |
| [Hebrew Calendar](https://www.hebcal.com/home/developer-apis) | Jewish calendar conversions | 🟢 No | ❌ | ✅ |
| [UK Bank Holidays](https://www.gov.uk/bank-holidays.json) | UK bank holidays | 🟢 No | ✅ | ✅ |
| [Namedays Calendar](https://nameday.abalin.net) | Namedays for multiple countries | 🟢 No | ✅ | ✅ |
| [Czech Namedays](https://svatky.adresa.info) | Czech nameday lookup | 🟢 No | ❌ | ✅ |
| [Holidays API](https://holidayapi.com/) | Historical holiday data | 🟡 API Key | ✅ | ✅ |

---

## Cloud Storage & File Sharing

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Dropbox](https://www.dropbox.com/developers) | File Sharing and Storage | 🔴 OAuth | ✅ | ⚠️ |
| [Google Drive](https://developers.google.com/drive/) | File Sharing and Storage | 🔴 OAuth | ✅ | ⚠️ |
| [OneDrive](https://developer.microsoft.com/onedrive) | File Sharing and Storage | 🔴 OAuth | ✅ | ⚠️ |
| [Box](https://developer.box.com/) | Enterprise File Sharing | 🔴 OAuth | ✅ | ⚠️ |
| [File.io](https://www.file.io) | Simple anonymous file sharing | 🟢 No | ✅ | ✅⭐ |
| [GoFile](https://gofile.io/api) | Unlimited file uploads | 🟡 API Key | ✅ | ✅ |
| [Pastebin](https://pastebin.com/doc_api) | Plain text storage | 🟡 API Key | ✅ | ✅ |
| [The Null Pointer](https://0x0.st) | No-BS file hosting | 🟢 No | ✅ | ✅⭐ |
| [Imgbb](https://api.imgbb.com/) | Image sharing | 🟡 API Key | ✅ | ✅ |
| [Gyazo](https://gyazo.com/api/docs) | Screen capture sharing | 🟡 API Key | ✅ | ✅ |
| [Pinata](https://docs.pinata.cloud/) | IPFS Pinning Services | 🟡 API Key | ✅ | ✅ |
| [Web3 Storage](https://web3.storage/) | Free 1TB decentralized storage | 🟡 API Key | ✅ | ✅ |
| [Storj](https://docs.storj.io/dcs/) | Decentralized cloud storage | 🟡 API Key | ✅ | ✅ |

---

## Dictionaries & Language

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Free Dictionary](https://dictionaryapi.dev/) | Word definitions | 🟢 No | ✅ | ✅⭐ |
| [Urban Dictionary](https://rapidapi.com/community/api/urban-dictionary) | Slang definitions | 🟡 API Key | ✅ | ✅ |
| [Merriam-Webster](https://dictionaryapi.com/) | Dictionary and Thesaurus | 🟡 API Key | ✅ | ✅ |
| [Oxford Dictionaries](https://developer.oxforddictionaries.com/) | Dictionary data | 🟡 API Key | ✅ | ✅ |
| [Words API](https://www.wordsapi.com/) | Word data, definitions, synonyms | 🟡 API Key | ✅ | ✅ |
| [Evil Insult Generator](https://evilinsult.com/api/) | Random insults | 🟢 No | ✅ | ✅ |
| [Fun Translations](https://funtranslations.com/api/) | Translate text to fun dialects | 🟡 API Key | ✅ | ✅ |
| [LibreTranslate](https://libretranslate.com/docs/) | Free and Open Source translation | 🟡 API Key | ✅ | ✅ |
| [Lingua Robot](https://www.linguarobot.io) | Word definitions and translations | 🟡 API Key | ✅ | ✅ |

---

## Email

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [SendGrid](https://docs.sendgrid.com/api-reference/) | Email delivery service | 🟡 API Key | ✅ | ✅⭐ |
| [Mailgun](https://documentation.mailgun.com/en/latest/) | Email API | 🟡 API Key | ✅ | ✅ |
| [Mailjet](https://www.mailjet.com/) | Email service | 🟡 API Key | ✅ | ✅ |
| [Gmail](https://developers.google.com/gmail/api/) | Gmail inbox access | 🔴 OAuth | ✅ | ⚠️ |
| [Hunter](https://hunter.io/api-documentation) | Email finder | 🟡 API Key | ✅ | ✅ |
| [Abstract Email Validation](https://www.abstractapi.com/api/email-verification-validation-api) | Email verification | 🟡 API Key | ✅ | ✅ |
| [Kickbox](https://docs.kickbox.com/) | Email verification | 🟡 API Key | ✅ | ✅ |
| [MailCheck](https://www.mailcheck.ai/api) | Email validation | 🟡 API Key | ✅ | ✅ |
| [Temp Mail](https://temp-mail.org/en/api/) | Temporary email addresses | 🟢 No | ✅ | ✅ |

---

## Machine Learning & AI

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Hugging Face](https://huggingface.co/docs/api-inference/index) | ML models inference | 🟡 API Key | ✅ | ✅⭐ |
| [OpenAI](https://platform.openai.com/docs/api-reference) | GPT and DALL-E | 🟡 API Key | ✅ | ✅⭐ |
| [Anthropic Claude](https://docs.anthropic.com/claude/reference/getting-started-with-the-api) | Claude AI | 🟡 API Key | ✅ | ✅⭐ |
| [Google AI](https://ai.google.dev/) | Gemini AI | 🟡 API Key | ✅ | ✅ |
| [Cohere](https://docs.cohere.com/) | NLP models | 🟡 API Key | ✅ | ✅ |
| [Replicate](https://replicate.com/docs/reference/http) | Run ML models | 🟡 API Key | ✅ | ✅ |
| [TensorFlow Serving](https://www.tensorflow.org/tfx/serving/api_rest) | ML model serving | 🟢 No | ✅ | ✅ |
| [Wit.ai](https://wit.ai/docs/http/20200513) | NLP for developers | 🟡 API Key | ✅ | ✅ |
| [DeepAI](https://deepai.org/machine-learning-api) | AI services | 🟡 API Key | ✅ | ✅ |
| [Eden AI](https://docs.edenai.co/reference) | Multiple AI APIs | 🟡 API Key | ✅ | ✅ |
| [Stability AI](https://platform.stability.ai/docs/api-reference) | Stable Diffusion | 🟡 API Key | ✅ | ✅ |
| [Whisper API](https://platform.openai.com/docs/guides/speech-to-text) | Speech to text | 🟡 API Key | ✅ | ✅ |

---

## Jobs & Careers

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Adzuna](https://developer.adzuna.com/) | Job search | 🟡 API Key | ✅ | ✅ |
| [GitHub Jobs](https://jobs.github.com/api) | Tech job listings | 🟢 No | ✅ | ✅ |
| [Indeed](https://opensource.indeedeng.io/api-documentation/) | Job search | 🟡 API Key | ✅ | ✅ |
| [LinkedIn Jobs](https://docs.microsoft.com/en-us/linkedin/) | Professional network jobs | 🔴 OAuth | ✅ | ⚠️ |
| [Remote OK](https://remoteok.com/api) | Remote job listings | 🟢 No | ✅ | ✅⭐ |
| [The Muse](https://www.themuse.com/developers/api/v2) | Job listings | 🟡 API Key | ✅ | ✅ |
| [USAJOBS](https://developer.usajobs.gov/) | US federal jobs | 🟡 API Key | ✅ | ✅ |
| [JSearch](https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch) | Job search aggregator | 🟡 API Key | ✅ | ✅ |

---

## Phone & SMS

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Twilio](https://www.twilio.com/docs/usage/api) | SMS, voice, video | 🟡 API Key | ✅ | ✅⭐ |
| [Vonage (Nexmo)](https://developer.vonage.com/api) | SMS and voice API | 🟡 API Key | ✅ | ✅ |
| [Plivo](https://www.plivo.com/docs/api/) | SMS, voice, and video | 🟡 API Key | ✅ | ✅ |
| [MessageBird](https://developers.messagebird.com/api/) | SMS and voice | 🟡 API Key | ✅ | ✅ |
| [Bandwidth](https://www.bandwidth.com/api/) | Communications API | 🟡 API Key | ✅ | ✅ |
| [Numverify](https://numverify.com/) | Phone number validation | 🟡 API Key | ✅ | ✅ |
| [Abstract Phone Validation](https://www.abstractapi.com/phone-validation-api) | Phone number verification | 🟡 API Key | ✅ | ✅ |
| [VoiceRSS](http://www.voicerss.org/api/) | Text to Speech | 🟡 API Key | ✅ | ✅ |

---

## Photography & Images

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Unsplash](https://unsplash.com/developers) | High-quality free photos | 🟡 API Key | ✅ | ✅⭐ |
| [Pexels](https://www.pexels.com/api/) | Free stock photos | 🟡 API Key | ✅ | ✅⭐ |
| [Pixabay](https://pixabay.com/api/docs/) | Free images and videos | 🟡 API Key | ✅ | ✅ |
| [Lorem Picsum](https://picsum.photos/) | Random placeholder images | 🟢 No | ✅ | ✅⭐ |
| [Flickr](https://www.flickr.com/services/api/) | Photo sharing | 🟡 API Key | ✅ | ✅ |
| [Getty Images](https://developers.gettyimages.com/) | Stock photos | 🟡 API Key | ✅ | ✅ |
| [Imgur](https://apidocs.imgur.com/) | Image hosting | 🟡 API Key | ✅ | ✅ |
| [PlaceKitten](https://placekitten.com/) | Placeholder kitten pictures | 🟢 No | ✅ | ✅ |
| [This Person Does Not Exist](https://thispersondoesnotexist.com/) | AI-generated faces | 🟢 No | ✅ | ✅ |
| [Remove.bg](https://www.remove.bg/api) | Background removal | 🟡 API Key | ✅ | ✅ |

---

## Social Media

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Twitter/X](https://developer.twitter.com/en/docs) | Social media platform | 🔴 OAuth | ✅ | ⚠️ |
| [Facebook Graph](https://developers.facebook.com/docs/graph-api) | Facebook data | 🔴 OAuth | ✅ | ⚠️ |
| [Instagram](https://developers.facebook.com/docs/instagram-api) | Photo sharing | 🔴 OAuth | ✅ | ⚠️ |
| [LinkedIn](https://docs.microsoft.com/en-us/linkedin/) | Professional network | 🔴 OAuth | ✅ | ⚠️ |
| [Reddit](https://www.reddit.com/dev/api) | Social news | 🔴 OAuth | ✅ | ⚠️ |
| [YouTube](https://developers.google.com/youtube/v3) | Video platform | 🟡 API Key | ✅ | ✅ |
| [TikTok](https://developers.tiktok.com/) | Short video platform | 🔴 OAuth | ✅ | ⚠️ |
| [Pinterest](https://developers.pinterest.com/docs/api/v5/) | Visual discovery | 🔴 OAuth | ✅ | ⚠️ |
| [Mastodon](https://docs.joinmastodon.org/api/) | Decentralized social network | 🔴 OAuth | ✅ | ✅ |
| [Discord](https://discord.com/developers/docs/intro) | Gaming chat | 🟡 API Key | ✅ | ✅⭐ |

---

## Video & Streaming

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [YouTube](https://developers.google.com/youtube/v3) | Video platform API | 🟡 API Key | ✅ | ✅⭐ |
| [Vimeo](https://developer.vimeo.com/) | Video hosting | 🔴 OAuth | ✅ | ⚠️ |
| [Twitch](https://dev.twitch.tv/docs/api/) | Live streaming | 🔴 OAuth | ✅ | ⚠️ |
| [DailyMotion](https://developers.dailymotion.com/) | Video sharing | 🔴 OAuth | ✅ | ⚠️ |
| [Pexels Videos](https://www.pexels.com/api/) | Free stock videos | 🟡 API Key | ✅ | ✅ |
| [Pixabay Videos](https://pixabay.com/api/docs/) | Free videos | 🟡 API Key | ✅ | ✅ |
| [TMDb](https://www.themoviedb.org/documentation/api) | Movie database | 🟡 API Key | ✅ | ✅ |
| [TVmaze](https://www.tvmaze.com/api) | TV show data | 🟢 No | ✅ | ✅⭐ |
| [Streamable](https://streamable.com/documentation) | Video hosting | 🟢 No | ✅ | ✅ |

---

## Shopping & E-commerce

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Amazon Product](https://webservices.amazon.com/paapi5/documentation/) | Product advertising | 🟡 API Key | ✅ | ✅ |
| [eBay](https://developer.ebay.com/docs) | Marketplace API | 🔴 OAuth | ✅ | ⚠️ |
| [Etsy](https://www.etsy.com/developers/documentation) | Handmade marketplace | 🔴 OAuth | ✅ | ⚠️ |
| [Shopify](https://shopify.dev/api) | E-commerce platform | 🔴 OAuth | ✅ | ⚠️ |
| [WooCommerce](https://woocommerce.github.io/woocommerce-rest-api-docs/) | WordPress e-commerce | 🟡 API Key | ✅ | ✅ |
| [Best Buy](https://bestbuyapis.github.io/api-documentation/) | Product catalog | 🟡 API Key | ✅ | ✅ |
| [Walmart](https://developer.walmart.com/) | Marketplace API | 🟡 API Key | ✅ | ✅ |
| [AliExpress](https://developers.aliexpress.com/) | Product search | 🟡 API Key | ✅ | ✅ |
| [Fake Store API](https://fakestoreapi.com/) | Fake shop data for testing | 🟢 No | ✅ | ✅⭐ |

---

## URL Shorteners

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Bitly](https://dev.bitly.com/) | URL shortening | 🟡 API Key | ✅ | ✅⭐ |
| [TinyURL](https://tinyurl.com/app/dev) | URL shortening | 🟡 API Key | ✅ | ✅ |
| [Rebrandly](https://developers.rebrandly.com/) | Custom URL shortener | 🟡 API Key | ✅ | ✅ |
| [Cuttly](https://cutt.ly/cuttly-api) | URL shortening | 🟡 API Key | ✅ | ✅ |
| [Short.io](https://developers.short.io/) | Branded short links | 🟡 API Key | ✅ | ✅ |
| [is.gd](https://is.gd/developers.php) | Simple URL shortener | 🟢 No | ✅ | ✅⭐ |
| [v.gd](https://v.gd/developers.php) | URL shortening | 🟢 No | ✅ | ✅ |
| [1pt.co](https://github.com/1pt-co/api) | URL shortening | 🟢 No | ✅ | ✅ |

---

## Tracking & Analytics

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Google Analytics](https://developers.google.com/analytics/) | Web analytics | 🔴 OAuth | ✅ | ⚠️ |
| [Plausible](https://plausible.io/docs/stats-api) | Privacy-friendly analytics | 🟡 API Key | ✅ | ✅ |
| [Matomo](https://developer.matomo.org/api-reference/reporting-api) | Open source analytics | 🟡 API Key | ✅ | ✅ |
| [AfterShip](https://developers.aftership.com/) | Package tracking | 🟡 API Key | ✅ | ✅⭐ |
| [17track](https://api.17track.net/en) | Package tracking | 🟡 API Key | ✅ | ✅ |
| [Parcel](https://parcelapp.net/) | Delivery tracking | 🟢 No | ✅ | ✅ |
| [Geocode.xyz](https://geocode.xyz/api) | Location tracking | 🟢 No | ✅ | ✅ |
| [IPInfo](https://ipinfo.io/developers) | IP address tracking | 🟡 API Key | ✅ | ✅ |

---

## Environment & Sustainability

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [OpenAQ](https://docs.openaq.org/) | Air quality data | 🟡 API Key | ✅ | ✅⭐ |
| [CO2 Signal](https://docs.co2signal.com/) | Carbon intensity of electricity | 🟡 API Key | ✅ | ✅ |
| [Breezometer](https://docs.breezometer.com/api-documentation/introduction/) | Air quality & pollen | 🟡 API Key | ✅ | ✅ |
| [AirVisual](https://www.iqair.com/air-pollution-data-api) | Air quality | 🟡 API Key | ✅ | ✅ |
| [EPA Air Quality](https://www.epa.gov/outdoor-air-quality-data/air-quality-index-daily-values-report) | US air quality | 🟢 No | ✅ | ✅ |
| [Carbon Interface](https://docs.carboninterface.com/) | Carbon emissions calculations | 🟡 API Key | ✅ | ✅ |
| [TreeAPI](https://treeapi.org/) | Tree planting | 🟡 API Key | ✅ | ✅ |
| [PurpleAir](https://www2.purpleair.com/pages/develop-api) | Real-time air quality | 🟡 API Key | ✅ | ✅ |

---

## Vehicles & Transportation Tracking

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [NHTSA](https://vpic.nhtsa.dot.gov/api/) | Vehicle information | 🟢 No | ✅ | ✅⭐ |
| [Edmunds](https://developer.edmunds.com/) | Car data | 🟡 API Key | ✅ | ✅ |
| [OpenSky Network](https://openskynetwork.github.io/opensky-api/) | Real-time flight data | 🟢 No | ✅ | ✅⭐ |
| [FlightAware](https://www.flightaware.com/commercial/flightxml/) | Flight tracking | 🟡 API Key | ✅ | ✅ |
| [AviationStack](https://aviationstack.com/) | Flight data | 🟡 API Key | ✅ | ✅ |
| [Uber](https://developer.uber.com/) | Ride sharing | 🔴 OAuth | ✅ | ⚠️ |
| [Lyft](https://developer.lyft.com/) | Ride sharing | 🔴 OAuth | ✅ | ⚠️ |
| [Car Query](https://www.carqueryapi.com/) | Car specifications | 🟢 No | ❌ | ✅ |
| [TfL (Transport for London)](https://api.tfl.gov.uk/) | London transport | 🟡 API Key | ✅ | ✅⭐ |

---

## Podcasts & Audio

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Listen Notes](https://www.listennotes.com/api/) | Podcast search engine | 🟡 API Key | ✅ | ✅⭐ |
| [Podcast Index](https://podcastindex-org.github.io/docs-api/) | Open podcast database | 🟡 API Key | ✅ | ✅⭐ |
| [iTunes Search](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/) | Search iTunes content | 🟢 No | ✅ | ✅⭐ |
| [Audioboom](https://github.com/audioboom/api) | Audio hosting | 🔴 OAuth | ✅ | ⚠️ |
| [Podcast API](https://www.podcastapi.com/) | Podcast data | 🟡 API Key | ✅ | ✅ |
| [Spotify Podcasts](https://developer.spotify.com/documentation/web-api/) | Podcast data | 🔴 OAuth | ✅ | ⚠️ |

---

## Text Analysis & NLP

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [MeaningCloud](https://www.meaningcloud.com/developer/apis) | Text analysis | 🟡 API Key | ✅ | ✅ |
| [Aylien](https://docs.aylien.com/textapi/) | Text analysis | 🟡 API Key | ✅ | ✅ |
| [Sentiment](https://sentim-api.herokuapp.com/) | Sentiment analysis | 🟢 No | ✅ | ✅⭐ |
| [Text Analysis API](https://www.twinword.com/api/) | NLP tools | 🟡 API Key | ✅ | ✅ |
| [Language Tool](https://languagetool.org/http-api/) | Grammar checking | 🟢 No | ✅ | ✅⭐ |
| [Perspective API](https://www.perspectiveapi.com/) | Toxicity detection | 🟡 API Key | ✅ | ✅ |
| [Bad Words API](https://www.purgomalum.com/) | Profanity filter | 🟢 No | ❌ | ✅ |
| [Lecto Translation](https://rapidapi.com/lecto-lecto-default/api/lecto-translation) | Translation | 🟡 API Key | ✅ | ✅ |

---

## Patents & Intellectual Property

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [USPTO](https://www.uspto.gov/learning-and-resources/open-data-and-mobility) | US Patent data | 🟢 No | ✅ | ✅⭐ |
| [EPO OPS](https://www.epo.org/searching-for-patents/data/web-services/ops.html) | European patents | 🟡 API Key | ✅ | ✅ |
| [Google Patents](https://patents.google.com/) | Patent search | 🟢 No | ✅ | ✅ |
| [Lens.org](https://www.lens.org/lens/api) | Patent and scholarly data | 🟡 API Key | ✅ | ✅ |

---

## Open Source Projects

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [GitHub](https://docs.github.com/en/rest) | Code hosting platform | 🟡 API Key | ✅ | ✅⭐ |
| [GitLab](https://docs.gitlab.com/ee/api/) | DevOps platform | 🟡 API Key | ✅ | ✅ |
| [Libraries.io](https://libraries.io/api) | Open source discovery | 🟡 API Key | ✅ | ✅ |
| [Open Collective](https://docs.opencollective.com/help/developers/api) | Funding platform | 🟡 API Key | ✅ | ✅ |
| [Bitbucket](https://developer.atlassian.com/bitbucket/api/2/reference/) | Code hosting | 🔴 OAuth | ✅ | ⚠️ |
| [SourceForge](https://sourceforge.net/p/forge/documentation/API/) | Software repository | 🟢 No | ✅ | ✅ |

---

## Personality & Fun Tests

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Agify.io](https://agify.io) | Age prediction from name | 🟢 No | ✅ | ✅⭐ |
| [Genderize.io](https://genderize.io) | Gender prediction from name | 🟢 No | ✅ | ✅⭐ |
| [Nationalize.io](https://nationalize.io) | Nationality prediction from name | 🟢 No | ✅ | ✅⭐ |
| [FoaaS](https://www.foaas.com/) | F*** Off as a Service | 🟢 No | ✅ | ✅ |
| [Yes or No](https://yesno.wtf/api) | Random yes/no answer | 🟢 No | ✅ | ✅⭐ |
| [Breaking Bad Quotes](https://breakingbadquotes.xyz/) | Random BB quotes | 🟢 No | ✅ | ✅ |
| [Kanye Rest](https://kanye.rest/) | Kanye West quotes | 🟢 No | ✅ | ✅ |
| [Ron Swanson Quotes](https://github.com/jamesseanwright/ron-swanson-quotes) | Ron Swanson quotes | 🟢 No | ✅ | ✅ |
| [Trump Quotes](https://docs.tronalddump.io/) | Donald Trump quotes | 🟢 No | ✅ | ✅ |

---

## Continuous Integration & DevOps

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [GitHub Actions](https://docs.github.com/en/rest/actions) | CI/CD platform | 🟡 API Key | ✅ | ✅⭐ |
| [CircleCI](https://circleci.com/docs/api/v1-reference/) | Continuous integration | 🟡 API Key | ✅ | ✅ |
| [Travis CI](https://docs.travis-ci.com/api/) | CI service | 🟡 API Key | ✅ | ✅ |
| [Jenkins](https://www.jenkins.io/doc/book/using/remote-access-api/) | Automation server | 🟡 API Key | ✅ | ✅ |
| [Azure DevOps](https://docs.microsoft.com/en-us/rest/api/azure/devops) | DevOps platform | 🟡 API Key | ✅ | ✅ |
| [Bitrise](https://api-docs.bitrise.io/) | Mobile CI/CD | 🟡 API Key | ✅ | ✅ |
| [Buddy](https://buddy.works/docs/api/getting-started/overview) | CI/CD platform | 🔴 OAuth | ✅ | ⚠️ |

---


---

## No Auth Required (Quick Start)
## Final 100 APIs to Hit 1000!

### Database & Backend Services
| [Supabase](https://supabase.com/docs/reference/api) | Open source Firebase | 🟡 API Key | ✅ | ✅⭐ |
| [Firebase](https://firebase.google.com/docs/reference) | Backend platform | 🟡 API Key | ✅ | ✅⭐ |
| [MongoDB Atlas](https://www.mongodb.com/docs/atlas/api/) | Cloud database | 🟡 API Key | ✅ | ✅⭐ |
| [PlanetScale](https://planetscale.com/docs/reference/rest-api-overview) | MySQL platform | 🟡 API Key | ✅ | ✅⭐ |
| [Neon](https://neon.tech/docs/reference/api-reference) | Serverless Postgres | 🟡 API Key | ✅ | ✅⭐ |
| [CockroachDB](https://www.cockroachlabs.com/docs/api/) | Distributed SQL | 🟡 API Key | ✅ | ✅ |
| [Fauna](https://docs.fauna.com/fauna/current/api/) | Distributed database | 🟡 API Key | ✅ | ✅ |
| [Hasura](https://hasura.io/docs/latest/api-reference/overview/) | GraphQL engine | 🟡 API Key | ✅ | ✅⭐ |
| [Apollo GraphQL](https://www.apollographql.com/docs/apollo-server/api/apollo-server/) | GraphQL platform | 🟡 API Key | ✅ | ✅⭐ |
| [Prisma](https://www.prisma.io/docs/) | Database toolkit | 🟢 No | ✅ | ✅⭐ |

### Authentication Services
| [Auth0](https://auth0.com/docs/api) | Identity platform | 🟡 API Key | ✅ | ✅⭐ |
| [Clerk](https://clerk.com/docs/reference/backend-api) | User management | 🟡 API Key | ✅ | ✅⭐ |
| [Supabase Auth](https://supabase.com/docs/reference/javascript/auth-api) | Authentication | 🟡 API Key | ✅ | ✅⭐ |
| [Firebase Auth](https://firebase.google.com/docs/auth) | Authentication service | 🟡 API Key | ✅ | ✅⭐ |
| [Okta](https://developer.okta.com/docs/reference/) | Identity service | 🟡 API Key | ✅ | ✅ |
| [OneLogin](https://developers.onelogin.com/api-docs/1/getting-started) | SSO platform | 🟡 API Key | ✅ | ✅ |
| [Ping Identity](https://apidocs.pingidentity.com/) | Identity security | 🟡 API Key | ✅ | ✅ |
| [FusionAuth](https://fusionauth.io/docs/v1/tech/apis/) | Auth platform | 🟡 API Key | ✅ | ✅ |
| [Magic](https://magic.link/docs/api-reference/overview) | Passwordless auth | 🟡 API Key | ✅ | ✅⭐ |
| [Corbado](https://docs.corbado.com/) | Passkey authentication | 🟡 API Key | ✅ | ✅ |

### Monitoring & Observability
| [Datadog](https://docs.datadoghq.com/api/) | Monitoring platform | 🟡 API Key | ✅ | ✅⭐ |
| [New Relic](https://docs.newrelic.com/docs/apis/intro-apis/introduction-new-relic-apis/) | APM platform | 🟡 API Key | ✅ | ✅ |
| [Sentry](https://docs.sentry.io/api/) | Error tracking | 🟡 API Key | ✅ | ✅⭐ |
| [Grafana](https://grafana.com/docs/grafana/latest/developers/http_api/) | Observability | 🟡 API Key | ✅ | ✅⭐ |
| [Prometheus](https://prometheus.io/docs/prometheus/latest/querying/api/) | Monitoring system | 🟢 No | ✅ | ✅⭐ |
| [Elastic APM](https://www.elastic.co/guide/en/apm/guide/current/api.html) | Performance monitoring | 🟡 API Key | ✅ | ✅ |
| [Honeycomb](https://docs.honeycomb.io/api/) | Observability platform | 🟡 API Key | ✅ | ✅ |
| [LogDNA](https://docs.logdna.com/reference) | Log management | 🟡 API Key | ✅ | ✅ |
| [Loggly](https://www.loggly.com/docs/api-overview/) | Log management | 🟡 API Key | ✅ | ✅ |
| [Better Stack](https://betterstack.com/docs/logs/api/) | Logging platform | 🟡 API Key | ✅ | ✅⭐ |

### Testing & QA
| [BrowserStack](https://www.browserstack.com/docs/automate/api-reference) | Browser testing | 🟡 API Key | ✅ | ✅⭐ |
| [Sauce Labs](https://docs.saucelabs.com/dev/api/) | Testing platform | 🟡 API Key | ✅ | ✅ |
| [LambdaTest](https://www.lambdatest.com/support/api-doc/) | Cloud testing | 🟡 API Key | ✅ | ✅ |
| [Percy](https://docs.percy.io/reference/api) | Visual testing | 🟡 API Key | ✅ | ✅ |
| [Chromatic](https://www.chromatic.com/docs/api) | Visual regression | 🟡 API Key | ✅ | ✅ |
| [TestRail](https://www.gurock.com/testrail/docs/api) | Test management | 🟡 API Key | ✅ | ✅ |
| [Postman API](https://learning.postman.com/docs/developer/intro-api/) | API testing | 🟡 API Key | ✅ | ✅⭐ |
| [K6 Cloud](https://k6.io/docs/cloud/cloud-reference/cloud-rest-api/) | Load testing | 🟡 API Key | ✅ | ✅ |
| [BlazeMeter](https://guide.blazemeter.com/hc/en-us/articles/360000091037) | Performance testing | 🟡 API Key | ✅ | ✅ |
| [Gatling](https://gatling.io/docs/gatling/reference/current/http/http_protocol/) | Load testing | 🟢 No | ✅ | ✅ |

### Infrastructure & Cloud
| [AWS](https://docs.aws.amazon.com/general/latest/gr/aws-apis.html) | Cloud services | 🟡 API Key | ✅ | ✅⭐ |
| [Google Cloud](https://cloud.google.com/apis/docs/overview) | Cloud platform | 🟡 API Key | ✅ | ✅⭐ |
| [Azure](https://docs.microsoft.com/en-us/rest/api/azure/) | Cloud computing | 🟡 API Key | ✅ | ✅ |
| [DigitalOcean](https://docs.digitalocean.com/reference/api/) | Cloud infrastructure | 🟡 API Key | ✅ | ✅⭐ |
| [Linode](https://www.linode.com/docs/api/) | Cloud computing | 🟡 API Key | ✅ | ✅⭐ |
| [Vultr](https://www.vultr.com/api/) | Cloud compute | 🟡 API Key | ✅ | ✅ |
| [Hetzner](https://docs.hetzner.cloud/) | Cloud hosting | 🟡 API Key | ✅ | ✅⭐ |
| [Scaleway](https://www.scaleway.com/en/developers/api/) | Cloud platform | 🟡 API Key | ✅ | ✅ |
| [OVHcloud](https://api.ovh.com/) | Cloud services | 🟡 API Key | ✅ | ✅ |
| [Fly.io](https://fly.io/docs/reference/api/) | App hosting | 🟡 API Key | ✅ | ✅⭐ |

### Deployment & Hosting
| [Vercel](https://vercel.com/docs/rest-api) | Frontend hosting | 🟡 API Key | ✅ | ✅⭐ |
| [Netlify](https://docs.netlify.com/api/get-started/) | Web hosting | 🟡 API Key | ✅ | ✅⭐ |
| [Cloudflare Pages](https://developers.cloudflare.com/api/) | Static hosting | 🟡 API Key | ✅ | ✅⭐ |
| [Render](https://render.com/docs/api) | Cloud platform | 🟡 API Key | ✅ | ✅⭐ |
| [Railway](https://docs.railway.app/reference/public-api) | App deployment | 🟡 API Key | ✅ | ✅⭐ |
| [Heroku](https://devcenter.heroku.com/categories/platform-api) | Cloud platform | 🟡 API Key | ✅ | ✅ |
| [Platform.sh](https://docs.platform.sh/development/api.html) | PaaS | 🟡 API Key | ✅ | ✅ |
| [Deta](https://docs.deta.sh/docs/home/) | Cloud platform | 🟡 API Key | ✅ | ✅⭐ |
| [Cyclic](https://docs.cyclic.sh/) | Serverless hosting | 🟡 API Key | ✅ | ✅ |
| [Koyeb](https://www.koyeb.com/docs/api) | Serverless platform | 🟡 API Key | ✅ | ✅ |

### Container & Orchestration
| [Docker Hub](https://docs.docker.com/docker-hub/api/latest/) | Container registry | 🟡 API Key | ✅ | ✅⭐ |
| [Kubernetes](https://kubernetes.io/docs/reference/kubernetes-api/) | Container orchestration | 🟡 API Key | ✅ | ✅⭐ |
| [Portainer](https://docs.portainer.io/api) | Container management | 🟡 API Key | ✅ | ✅ |
| [Rancher](https://ranchermanager.docs.rancher.com/reference-guides/rancher-manager-api) | K8s management | 🟡 API Key | ✅ | ✅ |
| [Nomad](https://developer.hashicorp.com/nomad/api-docs) | Workload orchestrator | 🟢 No | ✅ | ✅ |
| [Podman](https://docs.podman.io/en/latest/_static/api.html) | Container engine | 🟢 No | ✅ | ✅ |
| [ContainerD](https://github.com/containerd/containerd/tree/main/api) | Container runtime | 🟢 No | ✅ | ✅ |
| [Traefik](https://doc.traefik.io/traefik/operations/api/) | Reverse proxy | 🟢 No | ✅ | ✅⭐ |
| [Harbor](https://goharbor.io/docs/latest/working-with-projects/working-with-images/pulling-pushing-images/) | Container registry | 🟡 API Key | ✅ | ✅ |
| [Quay](https://docs.quay.io/api/) | Container registry | 🟡 API Key | ✅ | ✅ |

### Security & Compliance
| [Snyk](https://snyk.docs.apiary.io/) | Security platform | 🟡 API Key | ✅ | ✅⭐ |
| [Dependabot](https://docs.github.com/en/rest/dependabot) | Dependency updates | 🟡 API Key | ✅ | ✅ |
| [WhiteSource](https://whitesource.atlassian.net/wiki/spaces/WD/pages/34046081/WhiteSource+API) | Security scanning | 🟡 API Key | ✅ | ✅ |
| [Sonatype](https://help.sonatype.com/iqserver/automating/rest-apis) | Software supply chain | 🟡 API Key | ✅ | ✅ |
| [Black Duck](https://synopsys.atlassian.net/wiki/spaces/INTDOCS/pages/622846/Using+the+APIs) | Security testing | 🟡 API Key | ✅ | ✅ |
| [Veracode](https://docs.veracode.com/r/c_about_veracode_api) | Security analysis | 🟡 API Key | ✅ | ✅ |
| [Checkmarx](https://checkmarx.com/resource/documents/en/34965-68621-checkmarx-api-guide.html) | Code security | 🟡 API Key | ✅ | ✅ |
| [GitGuardian](https://api.gitguardian.com/docs) | Secret detection | 🟡 API Key | ✅ | ✅⭐ |
| [Trivy](https://aquasecurity.github.io/trivy/latest/docs/references/) | Vulnerability scanner | 🟢 No | ✅ | ✅⭐ |
| [Falco](https://falco.org/docs/api/) | Runtime security | 🟢 No | ✅ | ✅ |

### Additional Useful APIs
| [Shodan](https://developer.shodan.io/api) | Internet search engine | 🟡 API Key | ✅ | ✅⭐ |
| [Censys](https://search.censys.io/api) | Internet scanning | 🟡 API Key | ✅ | ✅ |
| [IPinfo](https://ipinfo.io/developers) | IP geolocation | 🟡 API Key | ✅ | ✅⭐ |
| [Abstract API](https://www.abstractapi.com/) | Utility APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Rebrandly Links](https://developers.rebrandly.com/docs) | URL shortener | 🟡 API Key | ✅ | ✅ |
| [Bitly Links](https://dev.bitly.com/) | Link management | 🟡 API Key | ✅ | ✅⭐ |
| [Microlink](https://microlink.io/docs/api/getting-started/overview) | Web scraping | 🟡 API Key | ✅ | ✅⭐ |
| [ScreenshotAPI](https://screenshotapi.net/documentation) | Screenshot service | 🟡 API Key | ✅ | ✅ |
| [Page2API](https://www.page2api.com/docs/getting-started) | Web scraping API | 🟡 API Key | ✅ | ✅ |
| [Httpie](https://httpie.io/docs/cli) | HTTP client | 🟢 No | ✅ | ✅⭐ |
| [Postwoman (Hoppscotch)](https://docs.hoppscotch.io/) | API testing | 🟢 No | ✅ | ✅⭐ |
## Final Push - 300+ More APIs

### Blockchain & DeFi (Additional)
| [Uniswap](https://docs.uniswap.org/api/overview) | DEX protocol | 🟢 No | ✅ | ✅⭐ |
| [PancakeSwap](https://docs.pancakeswap.finance/developers/api) | DEX on BSC | 🟢 No | ✅ | ✅ |
| [SushiSwap](https://dev.sushi.com/sushiswap/overview) | AMM protocol | 🟢 No | ✅ | ✅ |
| [Curve Finance](https://curve.readthedocs.io/ref-subgraph.html) | Stablecoin DEX | 🟢 No | ✅ | ✅ |
| [Balancer](https://docs.balancer.fi/) | Liquidity protocol | 🟢 No | ✅ | ✅ |
| [Compound](https://compound.finance/docs/api) | Lending protocol | 🟢 No | ✅ | ✅ |
| [Aave](https://docs.aave.com/developers/getting-started/readme) | DeFi lending | 🟢 No | ✅ | ✅ |
| [MakerDAO](https://docs.makerdao.com/) | DAI stablecoin | 🟢 No | ✅ | ✅ |
| [Yearn Finance](https://docs.yearn.finance/developers/v2/getting-started) | Yield aggregator | 🟢 No | ✅ | ✅ |
| [1inch](https://docs.1inch.io/docs/aggregation-protocol/introduction) | DEX aggregator | 🟢 No | ✅ | ✅⭐ |
| [0x Protocol](https://0x.org/docs) | Token swap protocol | 🟢 No | ✅ | ✅ |
| [Chainlink](https://docs.chain.link/data-feeds/api-reference) | Oracle network | 🟢 No | ✅ | ✅⭐ |
| [Polygon](https://docs.polygon.technology/api/getting-started) | Layer 2 scaling | 🟢 No | ✅ | ✅ |
| [Arbitrum](https://docs.arbitrum.io/build-decentralized-apps/public-clients) | L2 rollup | 🟢 No | ✅ | ✅ |
| [Optimism](https://community.optimism.io/docs/developers/) | Ethereum L2 | 🟢 No | ✅ | ✅ |
| [zkSync](https://era.zksync.io/docs/api/) | Zero-knowledge rollup | 🟢 No | ✅ | ✅ |
| [StarkNet](https://www.starknet.io/en/developers) | ZK rollup | 🟢 No | ✅ | ✅ |
| [Avalanche](https://docs.avax.network/apis/avalanchego) | Blockchain platform | 🟢 No | ✅ | ✅ |
| [Fantom](https://docs.fantom.foundation/api/public-api-endpoints) | DAG platform | 🟢 No | ✅ | ✅ |
| [Harmony](https://docs.harmony.one/home/developers/api) | Blockchain protocol | 🟢 No | ✅ | ✅ |

### NFT & Digital Art
| [OpenSea](https://docs.opensea.io/reference/api-overview) | NFT marketplace | 🟡 API Key | ✅ | ✅⭐ |
| [Rarible](https://api.rarible.org/v0.1/doc) | NFT platform | 🟡 API Key | ✅ | ✅ |
| [LooksRare](https://looksrare.github.io/api-docs/) | NFT marketplace | 🟢 No | ✅ | ✅ |
| [Magic Eden](https://api.magiceden.dev/) | Solana NFTs | 🟡 API Key | ✅ | ✅ |
| [X2Y2](https://docs.x2y2.io/) | NFT aggregator | 🟢 No | ✅ | ✅ |
| [NFTPort](https://docs.nftport.xyz/) | NFT infrastructure | 🟡 API Key | ✅ | ✅⭐ |
| [Alchemy NFT](https://docs.alchemy.com/reference/nft-api-quickstart) | NFT API | 🟡 API Key | ✅ | ✅⭐ |
| [Moralis NFT](https://docs.moralis.io/web3-data-api/evm/nft-api) | NFT data | 🟡 API Key | ✅ | ✅ |
| [QuickNode NFT](https://www.quicknode.com/docs/ethereum/qn_fetchNFTs) | NFT API | 🟡 API Key | ✅ | ✅ |
| [Center](https://docs.center.dev/) | NFT API | 🟡 API Key | ✅ | ✅ |
| [Reservoir](https://docs.reservoir.tools/) | NFT liquidity | 🟡 API Key | ✅ | ✅ |
| [SimpleHash](https://simplehash.com/docs) | Multi-chain NFTs | 🟡 API Key | ✅ | ✅⭐ |
| [Zora](https://docs.zora.co/docs/zora-api/intro) | NFT protocol | 🟢 No | ✅ | ✅ |
| [Foundation](https://docs.foundation.app/) | NFT marketplace | 🟢 No | ✅ | ✅ |
| [SuperRare](https://docs.superrare.com/) | Digital art | 🟢 No | ✅ | ✅ |

### Social Networks (Extended)
| [Bluesky](https://atproto.com/docs) | Decentralized social | 🟢 No | ✅ | ✅⭐ |
| [Nostr](https://github.com/nostr-protocol/nostr) | Decentralized protocol | 🟢 No | ✅ | ✅⭐ |
| [Farcaster](https://docs.farcaster.xyz/) | Decentralized social | 🟡 API Key | ✅ | ✅ |
| [Lens Protocol](https://docs.lens.xyz/docs) | Web3 social graph | 🟢 No | ✅ | ✅⭐ |
| [Mastodon API](https://docs.joinmastodon.org/api/) | Federated microblogging | 🔴 OAuth | ✅ | ✅⭐ |
| [Threads](https://developers.facebook.com/docs/threads) | Meta's Twitter alternative | 🔴 OAuth | ✅ | ⚠️ |
| [Tumblr](https://www.tumblr.com/docs/en/api/v2) | Blogging platform | 🔴 OAuth | ✅ | ⚠️ |
| [Medium](https://github.com/Medium/medium-api-docs) | Publishing platform | 🔴 OAuth | ✅ | ⚠️ |
| [Dev.to](https://developers.forem.com/api/) | Developer community | 🟡 API Key | ✅ | ✅⭐ |
| [Hashnode](https://apidocs.hashnode.com/) | Developer blogging | 🟡 API Key | ✅ | ✅ |
| [Product Hunt](https://api.producthunt.com/v2/docs) | Product discovery | 🔴 OAuth | ✅ | ⚠️ |
| [Hacker News Algolia](https://hn.algolia.com/api) | HN search | 🟢 No | ✅ | ✅⭐ |
| [Lobsters](https://lobste.rs/s/0bfortm/api_documentation) | Tech community | 🟢 No | ✅ | ✅ |
| [Slashdot](https://slashdot.org/faq/slashmeta.shtml) | Tech news | 🟢 No | ✅ | ✅ |
| [Stack Exchange](https://api.stackexchange.com/docs) | Q&A network | 🟡 API Key | ✅ | ✅⭐ |

### Messaging & Chat
| [WhatsApp Business](https://developers.facebook.com/docs/whatsapp) | Messaging | 🔴 OAuth | ✅ | ⚠️ |
| [Slack](https://api.slack.com/) | Team communication | 🔴 OAuth | ✅ | ⚠️ |
| [Discord Bot](https://discord.com/developers/docs/intro) | Discord API | 🟡 API Key | ✅ | ✅⭐ |
| [Telegram Bot](https://core.telegram.org/bots/api) | Messaging bots | 🟡 API Key | ✅ | ✅⭐ |
| [Signal](https://signal.org/docs/) | Encrypted messaging | 🟢 No | ✅ | ✅ |
| [Matrix](https://matrix.org/docs/api/) | Decentralized chat | 🟢 No | ✅ | ✅⭐ |
| [Rocket.Chat](https://developer.rocket.chat/reference/api) | Team chat | 🟡 API Key | ✅ | ✅ |
| [Mattermost](https://api.mattermost.com/) | Open source chat | 🟡 API Key | ✅ | ✅ |
| [Zulip](https://zulip.com/api/) | Team chat | 🟡 API Key | ✅ | ✅ |
| [Gitter](https://developer.gitter.im/docs/welcome) | Developer chat | 🔴 OAuth | ✅ | ⚠️ |
| [Stream Chat](https://getstream.io/chat/docs/rest/) | Chat API | 🟡 API Key | ✅ | ✅⭐ |
| [PubNub](https://www.pubnub.com/docs) | Real-time messaging | 🟡 API Key | ✅ | ✅ |
| [Pusher](https://pusher.com/docs/channels/library_auth_reference/rest-api/) | Real-time comms | 🟡 API Key | ✅ | ✅ |
| [Ably](https://ably.com/docs/api) | Real-time platform | 🟡 API Key | ✅ | ✅ |
| [Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging) | Push notifications | 🟡 API Key | ✅ | ✅⭐ |

### Design & Creative Tools
| [Figma](https://www.figma.com/developers/api) | Design tool | 🟡 API Key | ✅ | ✅⭐ |
| [Canva](https://www.canva.dev/docs/connect/getting-started/) | Graphic design | 🔴 OAuth | ✅ | ⚠️ |
| [Adobe Creative Cloud](https://developer.adobe.com/creative-cloud-apis/) | Adobe APIs | 🔴 OAuth | ✅ | ⚠️ |
| [Sketch](https://developer.sketch.com/) | Design platform | 🟡 API Key | ✅ | ✅ |
| [InVision](https://developer.invisionapp.com/docs) | Design collaboration | 🟡 API Key | ✅ | ✅ |
| [Framer](https://www.framer.com/api/) | Web builder | 🟡 API Key | ✅ | ✅ |
| [Webflow](https://developers.webflow.com/) | Website builder | 🔴 OAuth | ✅ | ⚠️ |
| [Dribbble](https://developer.dribbble.com/v2/) | Design showcase | 🔴 OAuth | ✅ | ⚠️ |
| [Behance](https://www.behance.net/dev/api/endpoints/) | Portfolio platform | 🟡 API Key | ✅ | ✅ |
| [Coolors](https://coolors.co/api) | Color schemes | 🟢 No | ✅ | ✅⭐ |
| [ColorSpace](https://mycolor.space/api) | Color palettes | 🟢 No | ✅ | ✅ |
| [The Color API](https://www.thecolorapi.com/) | Color information | 🟢 No | ❌ | ✅ |
| [ImageChart](https://www.image-charts.com/) | Chart generation | 🟢 No | ✅ | ✅⭐ |
| [QuickChart](https://quickchart.io/) | Chart images | 🟢 No | ✅ | ✅⭐ |
| [Chart.js Image](https://quickchart.io/documentation/) | Chart rendering | 🟢 No | ✅ | ✅ |

### Image Processing & Computer Vision
| [Cloudinary](https://cloudinary.com/documentation/image_upload_api_reference) | Image/video management | 🟡 API Key | ✅ | ✅⭐ |
| [Imgix](https://docs.imgix.com/apis/rendering) | Image processing | 🟡 API Key | ✅ | ✅ |
| [Uploadcare](https://uploadcare.com/docs/api_reference/rest/) | File uploading | 🟡 API Key | ✅ | ✅ |
| [ImageKit](https://docs.imagekit.io/api-reference/api-introduction) | Image optimization | 🟡 API Key | ✅ | ✅ |
| [Filestack](https://www.filestack.com/docs/api/) | File handling | 🟡 API Key | ✅ | ✅ |
| [TinyPNG](https://tinypng.com/developers) | Image compression | 🟡 API Key | ✅ | ✅⭐ |
| [Kraken.io](https://kraken.io/docs/getting-started) | Image optimizer | 🟡 API Key | ✅ | ✅ |
| [Google Vision](https://cloud.google.com/vision/docs) | Image analysis | 🟡 API Key | ✅ | ✅⭐ |
| [AWS Rekognition](https://docs.aws.amazon.com/rekognition/) | Image recognition | 🟡 API Key | ✅ | ✅ |
| [Azure Computer Vision](https://azure.microsoft.com/en-us/products/cognitive-services/computer-vision) | Image AI | 🟡 API Key | ✅ | ✅ |
| [Clarifai](https://docs.clarifai.com/) | Visual recognition | 🟡 API Key | ✅ | ✅ |
| [DeepAI](https://deepai.org/machine-learning-api) | AI services | 🟡 API Key | ✅ | ✅ |
| [Roboflow](https://docs.roboflow.com/) | Computer vision | 🟡 API Key | ✅ | ✅⭐ |
| [Face++](https://www.faceplusplus.com/face-detection/) | Face detection | 🟡 API Key | ✅ | ✅ |
| [Imagga](https://docs.imagga.com/) | Image tagging | 🟡 API Key | ✅ | ✅ |

### Video Processing & Streaming
| [Mux](https://docs.mux.com/) | Video streaming | 🟡 API Key | ✅ | ✅⭐ |
| [Cloudflare Stream](https://developers.cloudflare.com/stream/) | Video platform | 🟡 API Key | ✅ | ✅⭐ |
| [Wistia](https://wistia.com/support/developers) | Video hosting | 🟡 API Key | ✅ | ✅ |
| [JW Player](https://docs.jwplayer.com/platform/reference/introduction) | Video player | 🟡 API Key | ✅ | ✅ |
| [Ziggeo](https://ziggeo.com/docs/) | Video recording | 🟡 API Key | ✅ | ✅ |
| [Brightcove](https://apis.support.brightcove.com/) | Video cloud | 🟡 API Key | ✅ | ✅ |
| [Kaltura](https://developer.kaltura.com/api-docs/) | Video platform | 🟡 API Key | ✅ | ✅ |
| [Azure Media Services](https://docs.microsoft.com/en-us/azure/media-services/) | Video streaming | 🟡 API Key | ✅ | ✅ |
| [AWS MediaConvert](https://docs.aws.amazon.com/mediaconvert/) | Video transcoding | 🟡 API Key | ✅ | ✅ |
| [FFmpeg](https://ffmpeg.org/ffmpeg-all.html) | Video processing | 🟢 No | ✅ | ✅⭐ |
| [Shotstack](https://shotstack.io/docs/api/) | Video editing API | 🟡 API Key | ✅ | ✅⭐ |
| [Remotion](https://www.remotion.dev/docs/) | Video in React | 🟢 No | ✅ | ✅⭐ |
| [Coconut](https://docs.coconut.co/) | Video encoding | 🟡 API Key | ✅ | ✅ |
| [Encoding.com](https://api.encoding.com/) | Cloud transcoding | 🟡 API Key | ✅ | ✅ |
| [Vidyard](https://knowledge.vidyard.com/hc/en-us/articles/360009879734) | Video marketing | 🟡 API Key | ✅ | ✅ |

### Audio Processing & Music
| [Spotify Web API](https://developer.spotify.com/documentation/web-api/) | Music streaming | 🔴 OAuth | ✅ | ⚠️ |
| [Apple Music](https://developer.apple.com/documentation/applemusicapi/) | Music service | 🟡 API Key | ✅ | ✅ |
| [Deezer API](https://developers.deezer.com/api) | Music platform | 🟢 No | ✅ | ✅⭐ |
| [Last.fm](https://www.last.fm/api) | Music database | 🟡 API Key | ✅ | ✅⭐ |
| [Shazam](https://rapidapi.com/apidojo/api/shazam) | Music identification | 🟡 API Key | ✅ | ✅ |
| [AudD](https://audd.io/) | Music recognition | 🟡 API Key | ✅ | ✅ |
| [ACRCloud](https://www.acrcloud.com/docs/audio-fingerprinting-api/) | Audio recognition | 🟡 API Key | ✅ | ✅ |
| [Gracenote](https://developer.gracenote.com/) | Music metadata | 🟡 API Key | ✅ | ✅ |
| [MusicBrainz](https://musicbrainz.org/doc/MusicBrainz_API) | Music database | 🟢 No | ✅ | ✅⭐ |
| [Discogs](https://www.discogs.com/developers) | Music marketplace | 🟡 API Key | ✅ | ✅⭐ |
| [Bandcamp](https://bandcamp.com/developer) | Music platform | 🟡 API Key | ✅ | ✅ |
| [SoundCloud](https://developers.soundcloud.com/docs/api/guide) | Audio platform | 🔴 OAuth | ✅ | ⚠️ |
| [Mixcloud](https://www.mixcloud.com/developers/) | DJ mixes | 🔴 OAuth | ✅ | ⚠️ |
| [FreeSound](https://freesound.org/docs/api/) | Sound effects | 🟡 API Key | ✅ | ✅⭐ |
| [Audio Commons](https://www.audiocommons.org/api/) | Audio content | 🟡 API Key | ✅ | ✅ |

### Translation & Localization
| [Google Translate](https://cloud.google.com/translate/docs) | Translation service | 🟡 API Key | ✅ | ✅⭐ |
| [DeepL](https://www.deepl.com/docs-api) | Translation API | 🟡 API Key | ✅ | ✅⭐ |
| [Microsoft Translator](https://docs.microsoft.com/en-us/azure/cognitive-services/translator/) | Translation | 🟡 API Key | ✅ | ✅ |
| [Yandex Translate](https://yandex.com/dev/translate/) | Translation API | 🟡 API Key | ✅ | ✅ |
| [LibreTranslate](https://libretranslate.com/) | Free translation | 🟡 API Key | ✅ | ✅⭐ |
| [MyMemory](https://mymemory.translated.net/doc/spec.php) | Translation memory | 🟢 No | ✅ | ✅⭐ |
| [Translated](https://www.translated.com/welcome/api) | Professional translation | 🟡 API Key | ✅ | ✅ |
| [Lingvanex](https://lingvanex.com/en/translationapi/) | Translation API | 🟡 API Key | ✅ | ✅ |
| [IBM Watson Language](https://cloud.ibm.com/apidocs/language-translator) | Language translation | 🟡 API Key | ✅ | ✅ |
| [Amazon Translate](https://docs.aws.amazon.com/translate/) | Neural translation | 🟡 API Key | ✅ | ✅ |
| [Lokalise](https://developers.lokalise.com/reference/api-getting-started) | Localization platform | 🟡 API Key | ✅ | ✅⭐ |
| [POEditor](https://poeditor.com/docs/api) | Translation management | 🟡 API Key | ✅ | ✅ |
| [Crowdin](https://developer.crowdin.com/api/v2/) | Localization management | 🟡 API Key | ✅ | ✅ |
| [Transifex](https://developers.transifex.com/) | Translation platform | 🟡 API Key | ✅ | ✅ |
| [Phrase](https://developers.phrase.com/) | Localization platform | 🟡 API Key | ✅ | ✅ |

### Forms & Surveys
| [Typeform](https://developer.typeform.com/) | Online forms | 🔴 OAuth | ✅ | ⚠️ |
| [Google Forms](https://developers.google.com/forms/api) | Form builder | 🔴 OAuth | ✅ | ⚠️ |
| [JotForm](https://api.jotform.com/docs/) | Form builder | 🟡 API Key | ✅ | ✅ |
| [SurveyMonkey](https://developer.surveymonkey.com/) | Survey platform | 🔴 OAuth | ✅ | ⚠️ |
| [Typeform Response](https://developer.typeform.com/responses/) | Form responses | 🔴 OAuth | ✅ | ⚠️ |
| [Reform](https://www.reform.app/developers) | Form builder | 🟡 API Key | ✅ | ✅ |
| [Fillout](https://www.fillout.com/help/api) | Form platform | 🟡 API Key | ✅ | ✅ |
| [Tally](https://tally.so/help/api) | Free forms | 🟡 API Key | ✅ | ✅ |
| [Airtable Forms](https://airtable.com/developers/web/api/introduction) | Database forms | 🟡 API Key | ✅ | ✅⭐ |
| [Formstack](https://developers.formstack.com/) | Workplace forms | 🟡 API Key | ✅ | ✅ |

### CRM & Sales
| [Salesforce](https://developer.salesforce.com/docs/apis) | CRM platform | 🔴 OAuth | ✅ | ⚠️ |
| [HubSpot](https://developers.hubspot.com/docs/api/overview) | Marketing CRM | 🟡 API Key | ✅ | ✅⭐ |
| [Pipedrive](https://developers.pipedrive.com/docs/api/v1) | Sales CRM | 🟡 API Key | ✅ | ✅⭐ |
| [Zoho CRM](https://www.zoho.com/crm/developer/docs/api/) | CRM software | 🔴 OAuth | ✅ | ⚠️ |
| [Close](https://developer.close.com/) | Sales CRM | 🟡 API Key | ✅ | ✅ |
| [Copper](https://developer.copper.com/) | CRM for Google | 🟡 API Key | ✅ | ✅ |
| [Freshsales](https://developers.freshworks.com/crm/api/) | Sales CRM | 🟡 API Key | ✅ | ✅ |
| [Insightly](https://api.insightly.com/v3.1/Help) | CRM platform | 🟡 API Key | ✅ | ✅ |
| [Keap](https://developer.infusionsoft.com/docs/rest/) | Small business CRM | 🔴 OAuth | ✅ | ⚠️ |
| [ActiveCampaign](https://developers.activecampaign.com/reference) | Marketing automation | 🟡 API Key | ✅ | ✅⭐ |

### Scheduling & Calendar
| [Calendly](https://developer.calendly.com/) | Scheduling tool | 🔴 OAuth | ✅ | ⚠️ |
| [Cal.com](https://cal.com/docs/api-reference) | Open source scheduling | 🟡 API Key | ✅ | ✅⭐ |
| [Doodle](https://doodle.com/api) | Meeting scheduler | 🟡 API Key | ✅ | ✅ |
| [YouCanBookMe](https://youcanbook.me/api/docs/) | Booking software | 🟡 API Key | ✅ | ✅ |
| [Acuity Scheduling](https://developers.acuityscheduling.com/) | Appointment booking | 🟡 API Key | ✅ | ✅ |
| [SimplyBook](https://simplybook.me/en/api/) | Booking platform | 🟡 API Key | ✅ | ✅ |
| [Setmore](https://developer.setmore.com/) | Appointment scheduler | 🟡 API Key | ✅ | ✅ |
| [Nylas Calendar](https://developer.nylas.com/docs/api/v3/calendar/) | Calendar API | 🟡 API Key | ✅ | ✅ |
| [Cronofy](https://docs.cronofy.com/) | Calendar sync | 🟡 API Key | ✅ | ✅ |
| [Microsoft Graph Calendar](https://docs.microsoft.com/en-us/graph/api/resources/calendar) | Calendar integration | 🔴 OAuth | ✅ | ⚠️ |

### Customer Support & Help Desk
| [Zendesk](https://developer.zendesk.com/api-reference/) | Customer service | 🟡 API Key | ✅ | ✅⭐ |
| [Intercom](https://developers.intercom.com/) | Customer messaging | 🟡 API Key | ✅ | ✅⭐ |
| [Freshdesk](https://developers.freshdesk.com/api/) | Help desk | 🟡 API Key | ✅ | ✅ |
| [Help Scout](https://developer.helpscout.com/) | Customer support | 🔴 OAuth | ✅ | ⚠️ |
| [Kayako](https://developer.kayako.com/) | Help desk software | 🟡 API Key | ✅ | ✅ |
| [Front](https://dev.frontapp.com/) | Team inbox | 🟡 API Key | ✅ | ✅ |
| [Crisp](https://docs.crisp.chat/api/v1/) | Customer messaging | 🟡 API Key | ✅ | ✅ |
| [Drift](https://devdocs.drift.com/) | Conversational marketing | 🟡 API Key | ✅ | ✅ |
| [LiveChat](https://developers.livechat.com/docs/) | Live chat software | 🟡 API Key | ✅ | ✅ |
| [Tawk.to](https://developer.tawk.to/) | Free live chat | 🟡 API Key | ✅ | ✅⭐ |

### Domain & DNS
| [Namecheap](https://www.namecheap.com/support/api/intro/) | Domain registrar | 🟡 API Key | ✅ | ✅ |
| [GoDaddy](https://developer.godaddy.com/) | Domain services | 🟡 API Key | ✅ | ✅ |
| [Cloudflare DNS](https://developers.cloudflare.com/api/operations/dns-records-for-a-zone-list-dns-records) | DNS management | 🟡 API Key | ✅ | ✅⭐ |
| [Google Domains](https://domains.google/) | Domain registration | 🟡 API Key | ✅ | ✅ |
| [Name.com](https://www.name.com/api-docs) | Domain registrar | 🟡 API Key | ✅ | ✅ |
| [Dynadot](https://www.dynadot.com/domain/api.html) | Domain API | 🟡 API Key | ✅ | ✅ |
| [DNS Made Easy](https://dnsmadeeasy.com/integration/restapi/) | DNS provider | 🟡 API Key | ✅ | ✅ |
| [DNSimple](https://developer.dnsimple.com/) | DNS management | 🟡 API Key | ✅ | ✅⭐ |
| [Route53](https://docs.aws.amazon.com/route53/) | AWS DNS | 🟡 API Key | ✅ | ✅ |
| [DigitalOcean DNS](https://docs.digitalocean.com/reference/api/api-reference/#tag/Domains) | DNS API | 🟡 API Key | ✅ | ✅ |

### Web Scraping & Automation
| [Bright Data](https://docs.brightdata.com/) | Web scraping | 🟡 API Key | ✅ | ✅⭐ |
| [ScraperAPI](https://www.scraperapi.com/documentation/) | Web scraping | 🟡 API Key | ✅ | ✅⭐ |
| [Apify](https://docs.apify.com/api/v2) | Web scraping platform | 🟡 API Key | ✅ | ✅⭐ |
| [Zyte](https://docs.zyte.com/api.html) | Web scraping | 🟡 API Key | ✅ | ✅ |
| [Octoparse](https://helpcenter.octoparse.com/hc/en-us/articles/360018905812-Octoparse-API-Overview) | Data extraction | 🟡 API Key | ✅ | ✅ |
| [ParseHub](https://www.parsehub.com/docs/ref/api/v2/) | Web scraping | 🟡 API Key | ✅ | ✅ |
| [Import.io](https://www.import.io/api/) | Web data extraction | 🟡 API Key | ✅ | ✅ |
| [Diffbot](https://docs.diffbot.com/) | AI web scraping | 🟡 API Key | ✅ | ✅⭐ |
| [ScrapingBee](https://www.scrapingbee.com/documentation/) | Web scraping API | 🟡 API Key | ✅ | ✅ |
| [Puppeteer](https://pptr.dev/) | Headless Chrome | 🟢 No | ✅ | ✅⭐ |
## Additional Categories - Final Push to 1000+

### Blockchain & Crypto (Additional)
| [Gemini Exchange](https://docs.gemini.com/rest-api/) | Cryptocurrency trading | 🟡 API Key | ✅ | ✅ |
| [Kraken Exchange](https://docs.kraken.com/rest/) | Crypto exchange API | 🟡 API Key | ✅ | ✅ |
| [KuCoin API](https://docs.kucoin.com/) | Digital currency exchange | 🟡 API Key | ✅ | ✅ |
| [Bittrex API](https://bittrex.github.io/api/v3) | Cryptocurrency trading | 🟡 API Key | ✅ | ✅ |
| [Poloniex API](https://docs.poloniex.com) | Digital assets | 🟡 API Key | ✅ | ✅ |
| [CoinStats](https://documenter.getpostman.com/view/5734027/RzZ6Hzr3) | Portfolio tracker | 🟢 No | ✅ | ✅ |
| [Nomics API](https://nomics.com/docs/) | Crypto market data | 🟡 API Key | ✅ | ✅ |
| [FTX Exchange](https://docs.ftx.com/) | Crypto derivatives | 🟡 API Key | ✅ | ✅ |
| [Huobi API](https://huobiapi.github.io/docs/spot/v1/en/) | Cryptocurrency exchange | 🟡 API Key | ✅ | ✅ |
| [OKEx API](https://www.okex.com/docs/) | Digital asset exchange | 🟡 API Key | ✅ | ✅ |
| [Solana RPC](https://docs.solana.com/developing/clients/jsonrpc-api) | Solana blockchain | 🟢 No | ✅ | ✅⭐ |
| [Alchemy API](https://docs.alchemy.com/alchemy/) | Blockchain infrastructure | 🟡 API Key | ✅ | ✅ |
| [The Graph API](https://thegraph.com) | Blockchain indexing protocol | 🟡 API Key | ✅ | ✅ |
| [Blockchair API](https://blockchair.com/api/docs) | Blockchain search and analytics | 🟡 API Key | ✅ | ✅ |
| [Helium API](https://docs.helium.com/api/blockchain/introduction/) | IoT blockchain | 🟢 No | ✅ | ✅ |
| [Tezos RPC](https://tezos.gitlab.io/api/rpc.html) | Tezos blockchain | 🟢 No | ✅ | ✅ |
| [Cardano Blockfrost](https://blockfrost.io/) | Cardano API | 🟡 API Key | ✅ | ✅ |
| [Near Protocol](https://docs.near.org/docs/api/rpc) | NEAR blockchain | 🟢 No | ✅ | ✅ |
| [Algorand API](https://developer.algorand.org/docs/rest-apis/algod/v2/) | Algorand blockchain | 🟢 No | ✅ | ✅ |
| [Cosmos API](https://v1.cosmos.network/rpc/v0.37.9) | Cosmos blockchain | 🟢 No | ✅ | ✅ |

### Development Tools (Additional)
| [Carbon API](https://carbon.now.sh/) | Code to image | 🟢 No | ✅ | ✅⭐ |
| [Ray.so API](https://ray.so/) | Beautiful code screenshots | 🟢 No | ✅ | ✅⭐ |
| [Shields.io API](https://shields.io/) | Metadata badges for projects | 🟢 No | ✅ | ✅⭐ |
| [PageSpeed API](https://developers.google.com/speed/docs/insights/v5/get-started) | Web performance | 🟡 API Key | ✅ | ✅ |
| [GTmetrix API](https://gtmetrix.com/api/) | Page speed testing | 🟡 API Key | ✅ | ✅ |
| [SSL Labs API](https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md) | SSL/TLS security testing | 🟢 No | ✅ | ✅⭐ |
| [NPM Registry API](https://github.com/npm/registry/blob/master/docs/REGISTRY-API.md) | Node package registry | 🟢 No | ✅ | ✅⭐ |
| [PyPI API](https://warehouse.pypa.io/api-reference/) | Python package index | 🟢 No | ✅ | ✅⭐ |
| [Crates.io API](https://crates.io/data-access) | Rust package registry | 🟢 No | ✅ | ✅⭐ |
| [Packagist API](https://packagist.org/apidoc) | PHP packages | 🟢 No | ✅ | ✅ |
| [RubyGems API](https://guides.rubygems.org/rubygems-org-api/) | Ruby packages | 🟢 No | ✅ | ✅ |
| [NuGet API](https://learn.microsoft.com/en-us/nuget/api/overview) | .NET packages | 🟢 No | ✅ | ✅ |
| [Maven Central API](https://search.maven.org/classic/) | Java packages | 🟢 No | ✅ | ✅ |
| [CocoaPods API](https://cocoapods.org/api) | iOS dependency manager | 🟢 No | ✅ | ✅ |
| [Homebrew API](https://formulae.brew.sh/docs/api/) | macOS package manager | 🟢 No | ✅ | ✅ |
| [Snyk API](https://snyk.docs.apiary.io/) | Vulnerability database | 🟡 API Key | ✅ | ✅ |
| [WebPageTest API](https://www.webpagetest.org/getkey.php) | Performance testing | 🟡 API Key | ✅ | ✅ |
| [Can I Use API](https://caniuse.com/api/v1/docs) | Browser support data | 🟢 No | ✅ | ✅⭐ |
| [BundlePhobia API](https://bundlephobia.com/api) | NPM package size | 🟢 No | ✅ | ✅⭐ |
| [cdnjs API](https://cdnjs.com/api) | CDN library search | 🟢 No | ✅ | ✅⭐ |

### Miscellaneous & Utility APIs
| [QR Code Generator](https://goqr.me/api/) | Generate QR codes | 🟢 No | ✅ | ✅⭐ |
| [QR Server](https://quickchart.io/qr-code-api/) | QR code API | 🟢 No | ✅ | ✅⭐ |
| [Barcode Lookup](https://www.barcodelookup.com/api) | Product information from barcodes | 🟡 API Key | ✅ | ✅ |
| [UUID Generator](https://www.uuidtools.com/api) | Generate UUIDs | 🟢 No | ✅ | ✅⭐ |
| [Random Data Generator](https://random-data-api.com/) | Generate fake data | 🟢 No | ✅ | ✅⭐ |
| [Lorem Ipsum Generator](https://loripsum.net/) | Lorem ipsum text | 🟢 No | No | ✅ |
| [Bacon Ipsum](https://baconipsum.com/json-api/) | Meat-themed lorem ipsum | 🟢 No | ✅ | ✅ |
| [Hipster Ipsum](https://hipsterjesus.com/) | Hipster lorem ipsum | 🟢 No | ✅ | ✅ |
| [Corporate Bs Generator](https://corporatebs-generator.sameerkumar.website/) | Business jargon generator | 🟢 No | ✅ | ✅ |
| [Evil Insult Generator](https://evilinsult.com/api/) | Random insults API | 🟢 No | ✅ | ✅ |
| [Affirmations API](https://www.affirmations.dev/) | Positive affirmations | 🟢 No | ✅ | ✅⭐ |
| [MotivationalQuotes](https://type.fit/api/quotes) | Inspirational quotes | 🟢 No | ✅ | ✅ |
| [QuoteGarden](https://pprathameshmore.github.io/QuoteGarden/) | Quote collection | 🟢 No | ✅ | ✅ |
| [Quotable](https://github.com/lukePeavey/quotable) | Random quotes API | 🟢 No | ✅ | ✅⭐ |
| [ZenQuotes](https://zenquotes.io/) | Inspirational quotes | 🟢 No | ✅ | ✅ |
| [FavQs](https://favqs.com/api) | Quotes database | 🟡 API Key | ✅ | ✅ |
| [They Said So Quotes](https://theysaidso.com/api/) | Quote of the day | 🟡 API Key | ✅ | ✅ |
| [Programming Quotes](https://programming-quotes-api.herokuapp.com/) | Quotes about programming | 🟢 No | ✅ | ✅ |
| [Stoic Quotes](https://stoicquotesapi.com/) | Stoic philosophy quotes | 🟢 No | ✅ | ✅ |
| [Game of Thrones Quotes](https://gameofthronesquotes.xyz/) | GoT quotes | 🟢 No | ✅ | ✅ |

### API Collections & Aggregators
| [RapidAPI](https://rapidapi.com/hub) | API marketplace | 🟡 API Key | ✅ | ✅⭐ |
| [APIs.guru](https://apis.guru/api-doc/) | OpenAPI directory | 🟢 No | ✅ | ✅⭐ |
| [Postman Public API Network](https://www.postman.com/explore/apis) | API collection | 🟢 No | ✅ | ✅ |
| [AnyAPI](https://any-api.com/) | API documentation aggregator | 🟢 No | ✅ | ✅ |
| [API List](https://apilist.fun/) | Collective API list | 🟢 No | ✅ | ✅ |

### Regional & Country-Specific
| [Brasil API](https://brasilapi.com.br/) | Brazilian data APIs | 🟢 No | ✅ | ✅⭐ |
| [India API](https://data.gov.in/) | Indian government data | 🟢 No | ✅ | ✅ |
| [UK Police Data](https://data.police.uk/docs/) | UK crime data | 🟢 No | ✅ | ✅⭐ |
| [Canada Census](https://www12.statcan.gc.ca/wds-sdw/index-eng.cfm) | Canadian statistics | 🟢 No | ✅ | ✅ |
| [Australian Bureau of Statistics](https://www.abs.gov.au/websitedbs/d3310114.nsf/home/api) | Australian stats | 🟢 No | ✅ | ✅ |
| [Singapore Open Data](https://data.gov.sg/developer) | Singapore government data | 🟡 API Key | ✅ | ✅ |
| [Mexico INEGI](https://www.inegi.org.mx/servicios/api_indicadores.html) | Mexican statistics | 🟢 No | ✅ | ✅ |
| [Germany Destatis](https://www-genesis.destatis.de/genesis/online) | German statistics | 🟢 No | ✅ | ✅ |
| [France Data](https://www.data.gouv.fr/en/api) | French open data | 🟢 No | ✅ | ✅ |
| [Italy ISTAT](https://www.istat.it/en/) | Italian statistics | 🟢 No | ✅ | ✅ |

### Additional Sports APIs
| [Cricket Live Scores](https://www.cricketapi.com/) | Cricket data | 🟡 API Key | ✅ | ✅ |
| [Rugby API](https://rapidapi.com/fluis.lacasse/api/rugby-live-data) | Rugby scores | 🟡 API Key | ✅ | ✅ |
| [Golf API](https://rapidapi.com/tipsters/api/live-golf-data) | Golf tournaments | 🟡 API Key | ✅ | ✅ |
| [Tennis API](https://rapidapi.com/apidojo/api/live-tennis10) | Tennis matches | 🟡 API Key | ✅ | ✅ |
| [MMA API](https://rapidapi.com/omega-victor-omega-victor-default/api/ufc-mma-api) | MMA/UFC data | 🟡 API Key | ✅ | ✅ |
| [eSports API](https://pandascore.co/) | eSports data | 🟡 API Key | ✅ | ✅ |
| [Handball API](https://rapidapi.com/api-sports/api/api-handball) | Handball scores | 🟡 API Key | ✅ | ✅ |
| [Volleyball API](https://rapidapi.com/api-sports/api/api-volleyball) | Volleyball data | 🟡 API Key | ✅ | ✅ |
| [Darts API](https://rapidapi.com/tipsters/api/darts-api) | Darts tournaments | 🟡 API Key | ✅ | ✅ |
| [Sumo API](https://sumo-api.com/) | Sumo wrestling | 🟢 No | ✅ | ✅ |

### Additional Gaming APIs
| [Genshin Impact](https://genshin.dev/) | Genshin data | 🟢 No | ✅ | ✅⭐ |
| [Halo API](https://developer.haloapi.com/) | Halo game stats | 🟡 API Key | ✅ | ✅ |
| [Destiny 2](https://bungie-net.github.io/multi/index.html) | Destiny 2 API | 🟡 API Key | ✅ | ✅ |
| [Apex Legends](https://apexlegendsapi.com/) | Apex stats | 🟡 API Key | ✅ | ✅ |
| [Call of Duty](https://rapidapi.com/elreco/api/call-of-duty-modern-warfare) | CoD stats | 🟡 API Key | ✅ | ✅ |
| [PUBG API](https://developer.pubg.com/) | PUBG stats | 🟡 API Key | ✅ | ✅ |
| [Counter-Strike](https://developer.valvesoftware.com/wiki/Counter-Strike:_Global_Offensive) | CS:GO data | 🟢 No | ✅ | ✅ |
| [Rocket League](https://rocketleaguestats.com/api) | Rocket League stats | 🟡 API Key | ✅ | ✅ |
| [Overwatch](https://overfast-api.tekrop.fr/) | Overwatch stats | 🟢 No | ✅ | ✅ |
| [Hearthstone](https://hearthstoneapi.com/) | Hearthstone cards | 🟡 API Key | ✅ | ✅ |
| [Magic: The Gathering](https://magicthegathering.io/) | MTG cards | 🟢 No | ✅ | ✅⭐ |
| [Yu-Gi-Oh!](https://ygoprodeck.com/api-guide/) | Yu-Gi-Oh cards | 🟢 No | ✅ | ✅⭐ |
| [Scryfall](https://scryfall.com/docs/api) | Magic cards database | 🟢 No | ✅ | ✅⭐ |
| [Gwent](https://gwent.one/api/) | Gwent cards | 🟢 No | ✅ | ✅ |
| [Legends of Runeterra](https://developer.riotgames.com/apis#lor-match-v1) | LoR API | 🟡 API Key | ✅ | ✅ |

### Additional Entertainment APIs
| [iTunes Search](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/) | iTunes content | 🟢 No | ✅ | ✅⭐ |
| [Netflix Roulette](https://rapidapi.com/unogs/api/unogsng) | Netflix catalog | 🟡 API Key | ✅ | ✅ |
| [Streaming Availability](https://www.movieofthenight.com/about/api) | Where to watch movies | 🟡 API Key | ✅ | ✅ |
| [WatchMode](https://api.watchmode.com/) | Streaming availability | 🟡 API Key | ✅ | ✅ |
| [Reelgood](https://rapidapi.com/gox-ai-gox-ai-default/api/reelgood-streaming-availability) | Streaming services | 🟡 API Key | ✅ | ✅ |
| [Movie Quotes](https://movie-quote-api.herokuapp.com/) | Famous movie quotes | 🟢 No | ✅ | ✅ |
| [TV Shows API](https://www.episodate.com/api) | TV show countdown | 🟢 No | ✅ | ✅⭐ |
| [Anime Quotes](https://animechan.vercel.app/) | Anime quotes API | 🟢 No | ✅ | ✅⭐ |
| [Simpsons Quotes](https://thesimpsonsquoteapi.glitch.me/) | Simpsons quotes | 🟢 No | ✅ | ✅ |
| [Futurama](https://futuramaapi.herokuapp.com/) | Futurama characters | 🟢 No | ✅ | ✅ |
| [South Park](https://spapi.dev/) | South Park data | 🟢 No | ✅ | ✅ |
| [Avatar: The Last Airbender](https://avatar-api-test.vercel.app/) | Avatar data | 🟢 No | ✅ | ✅ |
| [Bob's Burgers](https://bobsburgers-api.herokuapp.com/) | Bob's Burgers API | 🟢 No | ✅ | ✅ |
| [Community](https://the-community-api.herokuapp.com/) | Community TV show | 🟢 No | ✅ | ✅ |
| [How I Met Your Mother](https://himymapi.herokuapp.com/) | HIMYM data | 🟢 No | ✅ | ✅ |

### Productivity & Tools APIs
| [Notion](https://developers.notion.com/) | Notion workspace | 🔴 OAuth | ✅ | ⚠️ |
| [Airtable](https://airtable.com/developers/web/api/introduction) | Airtable database | 🟡 API Key | ✅ | ✅⭐ |
| [Google Sheets API](https://developers.google.com/sheets/api) | Spreadsheets | 🔴 OAuth | ✅ | ⚠️ |
| [Asana](https://developers.asana.com/docs) | Task management | 🔴 OAuth | ✅ | ⚠️ |
| [Todoist](https://developer.todoist.com/rest/v2/) | Task manager | 🟡 API Key | ✅ | ✅ |
| [ClickUp](https://clickup.com/api) | Project management | 🟡 API Key | ✅ | ✅ |
| [Monday.com](https://developer.monday.com/api-reference/docs) | Work OS | 🟡 API Key | ✅ | ✅ |
| [Linear](https://developers.linear.app/docs) | Issue tracking | 🟡 API Key | ✅ | ✅⭐ |
| [Height](https://www.height.app/api) | Project management | 🟡 API Key | ✅ | ✅ |
| [Basecamp](https://github.com/basecamp/bc3-api) | Project collaboration | 🔴 OAuth | ✅ | ⚠️ |

### AI & ML Model APIs
| [HuggingFace Inference](https://huggingface.co/docs/api-inference) | ML models | 🟡 API Key | ✅ | ✅⭐ |
| [OpenAI GPT](https://platform.openai.com/docs/api-reference) | GPT-4, DALL-E | 🟡 API Key | ✅ | ✅⭐ |
| [Claude API](https://docs.anthropic.com/claude/reference/getting-started-with-the-api) | Anthropic Claude | 🟡 API Key | ✅ | ✅⭐ |
| [Google Gemini](https://ai.google.dev/) | Gemini AI | 🟡 API Key | ✅ | ✅⭐ |
| [Cohere](https://docs.cohere.com/) | NLP models | 🟡 API Key | ✅ | ✅⭐ |
| [AI21 Labs](https://docs.ai21.com/) | Language models | 🟡 API Key | ✅ | ✅ |
| [Together AI](https://docs.together.ai/) | Open source LLMs | 🟡 API Key | ✅ | ✅ |
| [Mistral AI](https://docs.mistral.ai/) | Mistral models | 🟡 API Key | ✅ | ✅ |
| [Fireworks AI](https://docs.fireworks.ai/) | Fast inference | 🟡 API Key | ✅ | ✅ |
| [Groq](https://console.groq.com/docs) | Fast LLM inference | 🟡 API Key | ✅ | ✅⭐ |
| [Deepgram](https://developers.deepgram.com/) | Speech-to-text | 🟡 API Key | ✅ | ✅ |
| [AssemblyAI](https://www.assemblyai.com/docs) | Audio transcription | 🟡 API Key | ✅ | ✅ |
| [ElevenLabs](https://elevenlabs.io/docs/api-reference) | Text-to-speech | 🟡 API Key | ✅ | ✅⭐ |
| [Replicate](https://replicate.com/docs/reference/http) | ML model hosting | 🟡 API Key | ✅ | ✅⭐ |
| [RunPod](https://docs.runpod.io/) | GPU cloud compute | 🟡 API Key | ✅ | ✅ |

### Data Science & Analytics
| [Kaggle API](https://www.kaggle.com/docs/api) | Datasets and competitions | 🟡 API Key | ✅ | ✅⭐ |
| [DataHub](https://datahub.io/docs/api) | Dataset catalog | 🟢 No | ✅ | ✅ |
| [Google Dataset Search](https://datasetsearch.research.google.com/) | Dataset discovery | 🟢 No | ✅ | ✅ |
| [Data.World](https://docs.data.world/documentation/api/getting-started) | Data platform | 🟡 API Key | ✅ | ✅ |
| [Socrata Open Data](https://dev.socrata.com/) | Open data platform | 🟡 API Key | ✅ | ✅ |
| [DBpedia](https://www.dbpedia.org/resources/sparql/) | Structured Wikipedia | 🟢 No | ✅ | ✅⭐ |
| [Linked Data API](https://data.europa.eu/api/hub/search/api) | EU open data | 🟢 No | ✅ | ✅ |
| [UN Data](https://data.un.org/Host.aspx?Content=API) | United Nations data | 🟢 No | ✅ | ✅ |
| [IMF Data](https://datahelp.imf.org/knowledgebase/articles/667681-using-json-restful-web-service) | Economic data | 🟢 No | ✅ | ✅ |
| [OECD Data](https://data.oecd.org/api/) | Economic statistics | 🟢 No | ✅ | ✅ |

### Real Estate & Property
| [Zillow](https://www.zillow.com/howto/api/APIOverview.htm) | Real estate data | 🟡 API Key | ✅ | ✅ |
| [Realtor.com](https://rapidapi.com/apidojo/api/realtor) | Property listings | 🟡 API Key | ✅ | ✅ |
| [Zumper](https://www.zumper.com/api) | Rental listings | 🟡 API Key | ✅ | ✅ |
| [Rentcast](https://developers.rentcast.io/) | Rental estimates | 🟡 API Key | ✅ | ✅ |
| [Attom Data](https://api.developer.attomdata.com/) | Property data | 🟡 API Key | ✅ | ✅ |

### Automotive & Vehicles
| [NHTSA](https://vpic.nhtsa.dot.gov/api/) | Vehicle info | 🟢 No | ✅ | ✅⭐ |
| [Edmunds](https://developer.edmunds.com/) | Car data | 🟡 API Key | ✅ | ✅ |
| [Carvana](https://rapidapi.com/DataFanatic/api/carvana) | Used cars | 🟡 API Key | ✅ | ✅ |
| [CarQuery](http://www.carqueryapi.com/) | Car specifications | 🟢 No | ❌ | ✅ |
| [Car API](https://carapi.app/) | Vehicle database | 🟡 API Key | ✅ | ✅ |
| [VIN Decoder](https://vindecoder.eu/) | VIN information | 🟢 No | ✅ | ✅ |
| [Auto.dev](https://www.auto.dev/) | Vehicle data | 🟡 API Key | ✅ | ✅ |

### Marketing & SEO
| [Moz API](https://moz.com/api) | SEO data | 🟡 API Key | ✅ | ✅ |
| [SEMrush](https://www.semrush.com/api-documentation/) | SEO & marketing | 🟡 API Key | ✅ | ✅ |
| [Ahrefs](https://ahrefs.com/api/documentation) | Backlink data | 🟡 API Key | ✅ | ✅ |
| [DataForSEO](https://dataforseo.com/apis) | SEO APIs | 🟡 API Key | ✅ | ✅ |
| [SerpApi](https://serpapi.com/) | Google Search results | 🟡 API Key | ✅ | ✅⭐ |
| [ValueSERP](https://www.valueserp.com/) | Search results API | 🟡 API Key | ✅ | ✅ |
| [ScraperAPI](https://www.scraperapi.com/) | Web scraping | 🟡 API Key | ✅ | ✅ |
| [BrightData](https://brightdata.com/) | Web data platform | 🟡 API Key | ✅ | ✅ |

### Payment & Billing
| [Stripe](https://stripe.com/docs/api) | Payment processing | 🟡 API Key | ✅ | ✅⭐ |
| [PayPal](https://developer.paypal.com/api/rest/) | Payments | 🔴 OAuth | ✅ | ⚠️ |
| [Square](https://developer.squareup.com/reference/square) | Payments | 🔴 OAuth | ✅ | ⚠️ |
| [Braintree](https://developer.paypal.com/braintree/docs) | Payment gateway | 🟡 API Key | ✅ | ✅ |
| [Plaid](https://plaid.com/docs/api/) | Banking data | 🟡 API Key | ✅ | ✅⭐ |
| [Dwolla](https://developers.dwolla.com/) | ACH payments | 🔴 OAuth | ✅ | ⚠️ |
| [Adyen](https://docs.adyen.com/) | Payment platform | 🟡 API Key | ✅ | ✅ |
| [Mollie](https://docs.mollie.com/) | Payment service | 🟡 API Key | ✅ | ✅ |

### Shipping & Logistics
| [EasyPost](https://www.easypost.com/docs/api) | Shipping API | 🟡 API Key | ✅ | ✅⭐ |
| [ShipEngine](https://www.shipengine.com/docs/) | Multi-carrier shipping | 🟡 API Key | ✅ | ✅⭐ |
| [Shippo](https://goshippo.com/docs/) | Shipping labels | 🟡 API Key | ✅ | ✅ |
| [FedEx](https://developer.fedex.com/api/en-us/home.html) | FedEx shipping | 🟡 API Key | ✅ | ✅ |
| [UPS](https://www.ups.com/upsdeveloperkit) | UPS shipping | 🟡 API Key | ✅ | ✅ |
| [USPS](https://www.usps.com/business/web-tools-apis/) | USPS shipping | 🟡 API Key | ✅ | ✅ |
| [DHL](https://developer.dhl.com/) | DHL shipping | 🟡 API Key | ✅ | ✅ |

### IoT & Hardware
| [Arduino Cloud](https://docs.arduino.cc/arduino-cloud/api/api-rest-authentication) | IoT devices | 🟡 API Key | ✅ | ✅ |
| [Particle](https://docs.particle.io/reference/cloud-apis/api/) | IoT platform | 🟡 API Key | ✅ | ✅ |
| [Adafruit IO](https://io.adafruit.com/api/docs/) | IoT data | 🟡 API Key | ✅ | ✅ |
| [ThingSpeak](https://www.mathworks.com/help/thingspeak/rest-api.html) | IoT analytics | 🟡 API Key | ✅ | ✅ |
| [Blynk](https://docs.blynk.io/en/blynk.cloud/https-api-overview) | IoT platform | 🟡 API Key | ✅ | ✅ |
| [Ubidots](https://ubidots.com/docs/sw/) | IoT data platform | 🟡 API Key | ✅ | ✅ |
| [Philips Hue](https://developers.meethue.com/) | Smart lighting | 🟡 API Key | ✅ | ✅ |
| [IFTTT](https://platform.ifttt.com/docs/api_reference) | Automation platform | 🟡 API Key | ✅ | ✅⭐ |

### Education & Learning
| [Khan Academy](https://github.com/Khan/khan-api) | Educational content | 🔴 OAuth | ✅ | ⚠️ |
| [Coursera](https://tech.coursera.org/app-platform/catalog/) | Online courses | 🟡 API Key | ✅ | ✅ |
| [EdX](https://edx.readthedocs.io/projects/edx-platform-api/en/latest/) | MOOCs | 🟡 API Key | ✅ | ✅ |
| [Udemy](https://www.udemy.com/developers/affiliate/) | Course marketplace | 🟡 API Key | ✅ | ✅ |
| [Dictionary API](https://dictionaryapi.dev/) | Word definitions | 🟢 No | ✅ | ✅⭐ |
| [Words API](https://www.wordsapi.com/) | Word data | 🟡 API Key | ✅ | ✅ |
| [DataMuse](https://www.datamuse.com/api/) | Word finding | 🟢 No | ✅ | ✅⭐ |
| [Merriam-Webster](https://dictionaryapi.com/) | Dictionary | 🟡 API Key | ✅ | ✅ |
| [Oxford Dictionary](https://developer.oxforddictionaries.com/) | English dictionary | 🟡 API Key | ✅ | ✅ |

### Religion & Spirituality
| [Bible API](https://bible-api.com/) | Bible verses | 🟢 No | ✅ | ✅⭐ |
| [Digital Bible Platform](https://scripture.api.bible/) | Bible translations | 🟡 API Key | ✅ | ✅ |
| [ESV Bible](https://api.esv.org/) | ESV translation | 🟡 API Key | ✅ | ✅ |
| [Quran.com](https://quran.com/api) | Quran API | 🟢 No | ✅ | ✅⭐ |
| [Al Quran Cloud](https://alquran.cloud/api) | Quran data | 🟢 No | ✅ | ✅⭐ |
| [Bhagavad Gita](https://bhagavadgita.io/api) | Bhagavad Gita verses | 🔴 OAuth | ✅ | ⚠️ |
| [Sefaria](https://www.sefaria.org/api) | Jewish texts | 🟢 No | ✅ | ✅ |

### Random & Fun
| [Yes or No](https://yesno.wtf/api) | Random yes/no | 🟢 No | ✅ | ✅⭐ |
| [Dice Roller](https://roll.diceapi.com/) | Roll virtual dice | 🟢 No | ✅ | ✅⭐ |
| [Random User](https://randomuser.me/) | Generate fake users | 🟢 No | ✅ | ✅⭐ |
| [This Person Does Not Exist](https://thispersondoesnotexist.com/) | AI faces | 🟢 No | ✅ | ✅ |
| [UI Names](https://uinames.com/) | Random name generator | 🟢 No | ✅ | ✅ |
| [Behind The Name](https://www.behindthename.com/api/) | Name meanings | 🟡 API Key | ✅ | ✅ |
| [Nameday Calendar](https://nameday.abalin.net/) | Name days | 🟢 No | ✅ | ✅ |
| [BoredAPI](https://www.boredapi.com/) | Activity suggestions | 🟢 No | ✅ | ✅⭐ |
| [FunTranslations](https://funtranslations.com/api/) | Fun text translations | 🟡 API Key | ✅ | ✅ |
| [Pirate Speak](https://funtranslations.com/api/pirate) | Translate to pirate | 🟡 API Key | ✅ | ✅ |

These APIs require **no authentication** — perfect for rapid prototyping and testing:

### Essential
- [JSONPlaceholder](https://jsonplaceholder.typicode.com/) — Fake REST API
- [httpbin](https://httpbin.org/) — HTTP testing
- [ReqRes](https://reqres.in/) — Hosted REST API for testing

### Data
- [Wikipedia](https://www.mediawiki.org/wiki/API:Main_page) — Encyclopedia data
- [REST Countries](https://restcountries.com) — Country information
- [Open Library](https://openlibrary.org/developers/api) — Book data

### Weather
- [Open-Meteo](https://open-meteo.com/) — Free weather forecasts
- [wttr.in](https://github.com/chubin/wttr.in) — Terminal weather

### Finance
- [Frankfurter](https://www.frankfurter.app/docs) — Currency exchange rates
- [CoinGecko](http://www.coingecko.com/api) — Crypto prices

### Fun
- [HTTP Cat](https://http.cat/) — Cat status codes
- [Chuck Norris Jokes](https://api.chucknorris.io/) — Random jokes
- [Dog CEO](https://dog.ceo/dog-api/) — Random dog images
- [Advice Slip](https://api.adviceslip.com/) — Random advice

### Science
- [SpaceX](https://github.com/r-spacex/SpaceX-API) — SpaceX data
- [Open Notify](http://open-notify.org/Open-Notify-API/) — ISS location
| [USGS Earthquake](https://earthquake.usgs.gov/fdsnws/event/1/) | Earthquake data | 🟢 No | ✅ | ✅⭐ |
| [PubChem](https://pubchemdocs.ncbi.nlm.nih.gov/pug-rest) | Chemical information | 🟢 No | ✅ | ✅⭐ |
| [PubMed](https://www.ncbi.nlm.nih.gov/home/develop/api/) | Biomedical literature | 🟢 No | ✅ | ✅⭐ |
| [ChemSpider](http://www.chemspider.com/AboutServices.aspx) | Chemical structure database | 🟡 API Key | ✅ | ✅ |
| [Protein Data Bank](https://www.rcsb.org/pages/webservices) | 3D protein structures | 🟢 No | ✅ | ✅ |
| [iNaturalist](https://www.inaturalist.org/pages/api+reference) | Biodiversity data | 🟢 No | ✅ | ✅ |
| [GBIF](https://www.gbif.org/developer/summary) | Biodiversity information | 🟢 No | ✅ | ✅ |
| [Open Science Framework](https://developer.osf.io/) | Research platform | 🟢 No | ✅ | ✅ |
| [Zenodo](https://developers.zenodo.org/) | Research repository | 🟡 API Key | ✅ | ✅ |
| [ORCID](https://info.orcid.org/documentation/integration-guide/working-with-the-orcid-api/) | Researcher IDs | 🔴 OAuth | ✅ | ⚠️ |
| [Dimensions AI](https://www.dimensions.ai/dimensions-apis/) | Research intelligence | 🟡 API Key | ✅ | ✅ |
| [Europe PMC](https://europepmc.org/RestfulWebService) | Life sciences literature | 🟢 No | ✅ | ✅ |
| [Core](https://core.ac.uk/services/api) | Academic papers | 🟡 API Key | ✅ | ✅ |
| [Semantic Scholar](https://api.semanticscholar.org/) | Academic paper search | 🟡 API Key | ✅ | ✅ |
| [OpenAlex](https://docs.openalex.org/) | Scholarly catalog | 🟢 No | ✅ | ✅⭐ |

---

---

## 🤖 AI Agent Infrastructure & Sandboxes

> APIs and platforms purpose-built for AI agent execution, tool use, and orchestration.

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [E2B](https://e2b.dev/docs) | Sandboxed cloud environments for AI agents (Firecracker microVMs, 150ms startup) | 🟡 API Key | ✅ | ✅⭐ |
| [Browserbase](https://docs.browserbase.com/) | Cloud headless browser infrastructure for AI agent web automation | 🟡 API Key | ✅ | ✅⭐ |
| [Composio](https://docs.composio.dev/) | 250+ tool integrations for AI agents (Gmail, Slack, GitHub, etc.) with sandboxed execution | 🟡 API Key | ✅ | ✅⭐ |
| [Daytona](https://www.daytona.io/docs) | AI sandbox platform with sub-90ms cold starts and Docker isolation | 🟡 API Key | ✅ | ✅⭐ |
| [Modal](https://modal.com/docs/reference) | Serverless cloud for AI/ML with GPU access and sandboxed containers | 🟡 API Key | ✅ | ✅⭐ |
| [Toolhouse](https://docs.toolhouse.ai/) | Universal tool-use SDK for LLMs with optimized execution | 🟡 API Key | ✅ | ✅⭐ |
| [LangSmith](https://docs.smith.langchain.com/) | LLM application observability, testing, and evaluation platform | 🟡 API Key | ✅ | ✅⭐ |
| [Vercel AI SDK](https://sdk.vercel.ai/docs) | TypeScript toolkit for building AI apps with streaming and tool calling | 🟢 No | ✅ | ✅⭐ |
| [Replit Agent](https://docs.replit.com/category/agent) | AI agent that can build and deploy full-stack apps in sandboxed environments | 🟡 API Key | ✅ | ✅⭐ |
| [Val Town](https://docs.val.town/) | Cloud scripting platform — run serverless TypeScript functions via API | 🟡 API Key | ✅ | ✅⭐ |
| [Pipedream](https://pipedream.com/docs/api/) | Serverless workflow platform with 2000+ API integrations | 🟡 API Key | ✅ | ✅⭐ |
| [Activepieces](https://www.activepieces.com/docs/developers/overview) | Open source workflow automation with AI agent support | 🟡 API Key | ✅ | ✅⭐ |
| [Nango](https://docs.nango.dev/) | Pre-built API integrations with OAuth management for agents | 🟡 API Key | ✅ | ✅⭐ |
| [Arcade AI](https://docs.arcade-ai.com/) | Tool-use platform for AI agents with auth-managed API access | 🟡 API Key | ✅ | ✅⭐ |

---

## 🔍 AI Search APIs

> Search engines and retrieval APIs designed specifically for AI agents and RAG pipelines.

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Tavily](https://docs.tavily.com/) | Search engine built for AI agents — returns structured, cited results for RAG | 🟡 API Key | ✅ | ✅⭐ |
| [Exa](https://docs.exa.ai/) | Neural search API that understands meaning, not just keywords | 🟡 API Key | ✅ | ✅⭐ |
| [Perplexity Sonar](https://docs.perplexity.ai/) | Live web search + LLM synthesis in one API call with citations | 🟡 API Key | ✅ | ✅⭐ |
| [Firecrawl](https://docs.firecrawl.dev/) | Web scraping API that converts websites to LLM-ready markdown/structured data | 🟡 API Key | ✅ | ✅⭐ |
| [Jina AI Reader](https://jina.ai/reader/) | Convert any URL to LLM-ready text with `r.jina.ai` prefix — no API key needed | 🟢 No | ✅ | ✅⭐ |
| [Serper](https://serper.dev/) | Google Search results as JSON — fast and affordable for agents | 🟡 API Key | ✅ | ✅⭐ |
| [You.com](https://api.you.com/) | Web search API with AI snippets and RAG-optimized results | 🟡 API Key | ✅ | ✅⭐ |
| [SearXNG](https://docs.searxng.org/dev/search_api.html) | Self-hosted meta-search engine with JSON API — no tracking | 🟢 No | ✅ | ✅⭐ |
| [Brave Search](https://brave.com/search/api/) | Independent web index with AI summary snippets | 🟡 API Key | ✅ | ✅⭐ |
| [Kagi Search](https://help.kagi.com/kagi/api/overview.html) | Premium search API with FastGPT for instant AI answers | 🟡 API Key | ✅ | ✅⭐ |
| [Bing Web Search](https://www.microsoft.com/en-us/bing/apis/bing-web-search-api) | Microsoft's web search API with entity recognition | 🟡 API Key | ✅ | ✅ |
| [Google Custom Search](https://developers.google.com/custom-search/v1/overview) | Programmable search engine for specific sites or the web | 🟡 API Key | ✅ | ✅ |

---

## 🔗 Agent Protocols & Standards

> Open protocols enabling AI agent interoperability, tool integration, and communication.

| Protocol | Description | Auth | Type | Agent-Friendly |
|----------|-------------|------|------|----------------|
| [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) | Anthropic's open standard for LLM-to-tool integration — adopted by OpenAI, 1200+ servers | 🟢 No | Standard | ✅⭐ |
| [Agent2Agent (A2A)](https://a2a-protocol.org/) | Google's open protocol for agent-to-agent communication — Linux Foundation project, 150+ orgs | 🟢 No | Standard | ✅⭐ |
| [OpenAPI/Swagger](https://swagger.io/specification/) | Industry-standard REST API specification — machine-readable API definitions | 🟢 No | Standard | ✅⭐ |
| [JSON-RPC 2.0](https://www.jsonrpc.org/specification) | Lightweight remote procedure call protocol used by MCP transport | 🟢 No | Standard | ✅⭐ |
| [Server-Sent Events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events) | HTTP streaming standard for real-time agent data feeds | 🟢 No | Standard | ✅⭐ |
| [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) | Full-duplex communication for real-time agent interactions | 🟢 No | Standard | ✅⭐ |
| [LangChain Hub](https://smith.langchain.com/hub) | Community-driven repository of reusable prompts and chains for agents | 🟡 API Key | Registry | ✅⭐ |
| [MCP Registry](https://github.com/modelcontextprotocol/servers) | Official directory of published MCP server implementations | 🟢 No | Registry | ✅⭐ |

---

## 🧠 LLM Provider APIs (Extended)

> New and emerging large language model API providers beyond the established ones.

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [xAI Grok](https://docs.x.ai/api) | Grok models with real-time X/Twitter data access, 2M token context window | 🟡 API Key | ✅ | ✅⭐ |
| [DeepSeek](https://platform.deepseek.com/api-docs/) | High-performance models at ultra-low cost ($0.07/M input tokens with cache) | 🟡 API Key | ✅ | ✅⭐ |
| [Qwen (Alibaba)](https://help.aliyun.com/zh/model-studio/developer-reference/api-details) | 1T+ parameter MoE models supporting 119 languages | 🟡 API Key | ✅ | ✅⭐ |
| [Cerebras](https://inference-docs.cerebras.ai/) | Ultra-fast inference on custom wafer-scale chips (2000+ tokens/sec) | 🟡 API Key | ✅ | ✅⭐ |
| [OpenRouter](https://openrouter.ai/docs) | Unified API gateway to 100+ LLMs with automatic fallback and load balancing | 🟡 API Key | ✅ | ✅⭐ |
| [Ollama](https://github.com/ollama/ollama/blob/main/docs/api.md) | Run open-source LLMs locally with REST API — Llama, Mistral, Gemma, etc. | 🟢 No | ✅ | ✅⭐ |
| [LM Studio](https://lmstudio.ai/docs/api) | Local LLM server with OpenAI-compatible API | 🟢 No | ✅ | ✅⭐ |
| [Anyscale](https://docs.anyscale.com/) | Scalable LLM serving with fine-tuning support | 🟡 API Key | ✅ | ✅⭐ |
| [SambaNova](https://community.sambanova.ai/docs) | Enterprise AI platform with custom chip acceleration | 🟡 API Key | ✅ | ✅ |
| [Lepton AI](https://www.lepton.ai/docs) | Fast LLM hosting with built-in function calling support | 🟡 API Key | ✅ | ✅⭐ |
| [NVIDIA NIM](https://developer.nvidia.com/nim) | GPU-optimized inference microservices for LLMs | 🟡 API Key | ✅ | ✅⭐ |
| [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/APIReference/) | Managed LLM service with Claude, Llama, Titan, and more | 🟡 API Key | ✅ | ✅⭐ |
| [Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference) | Enterprise OpenAI models on Azure with content safety | 🟡 API Key | ✅ | ✅⭐ |
| [Google Vertex AI](https://cloud.google.com/vertex-ai/docs/reference/rest) | Managed ML platform with Gemini, PaLM, and custom models | 🟡 API Key | ✅ | ✅⭐ |
| [Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai/) | Run LLMs at the edge with serverless inference | 🟡 API Key | ✅ | ✅⭐ |

---

## 📊 Vector Databases & Embeddings

> Purpose-built databases for semantic search, RAG pipelines, and AI agent memory.

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Pinecone](https://docs.pinecone.io/reference/api/introduction) | Managed vector database with serverless deployment and metadata filtering | 🟡 API Key | ✅ | ✅⭐ |
| [Weaviate](https://weaviate.io/developers/weaviate/api/rest) | Open-source vector database with built-in vectorization modules | 🟡 API Key | ✅ | ✅⭐ |
| [Chroma](https://docs.trychroma.com/reference) | Open-source embedding database — simple API, perfect for prototyping | 🟢 No | ✅ | ✅⭐ |
| [Qdrant](https://qdrant.tech/documentation/interfaces/) | High-performance vector search engine with rich filtering | 🟡 API Key | ✅ | ✅⭐ |
| [Milvus](https://milvus.io/api-reference/restful/v2.4.x/About.md) | Scalable vector database for billion-scale similarity search | 🟡 API Key | ✅ | ✅⭐ |
| [Vectara](https://docs.vectara.com/docs/) | RAG-as-a-Service with built-in retrieval, ranking, and generation | 🟡 API Key | ✅ | ✅⭐ |
| [Turbopuffer](https://turbopuffer.com/docs) | Serverless vector database with fast cold starts and S3 storage | 🟡 API Key | ✅ | ✅⭐ |
| [Upstash Vector](https://upstash.com/docs/vector/overall/getstarted) | Serverless vector database with REST API and DiskANN indexing | 🟡 API Key | ✅ | ✅⭐ |
| [OpenAI Embeddings](https://platform.openai.com/docs/guides/embeddings) | Text embedding models (text-embedding-3-small/large) for semantic search | 🟡 API Key | ✅ | ✅⭐ |
| [Cohere Embed](https://docs.cohere.com/reference/embed) | Multilingual embedding models optimized for search and RAG | 🟡 API Key | ✅ | ✅⭐ |
| [Jina Embeddings](https://jina.ai/embeddings/) | Open-source embedding models with 8K token context | 🟡 API Key | ✅ | ✅⭐ |
| [Voyage AI](https://docs.voyageai.com/) | Embedding models optimized for retrieval and RAG applications | 🟡 API Key | ✅ | ✅⭐ |
| [Nomic Atlas](https://docs.nomic.ai/) | Open-source embeddings with interactive data visualization | 🟡 API Key | ✅ | ✅⭐ |

---

## 🎨 AI Image & Video Generation

> APIs for generating, editing, and transforming images and video with AI.

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [DALL-E (OpenAI)](https://platform.openai.com/docs/guides/images) | Image generation and editing via text prompts | 🟡 API Key | ✅ | ✅⭐ |
| [Stability AI](https://platform.stability.ai/docs/api-reference) | Stable Diffusion models — image generation, upscaling, inpainting | 🟡 API Key | ✅ | ✅⭐ |
| [Midjourney](https://docs.midjourney.com/) | High-quality artistic image generation | 🟡 API Key | ✅ | ✅ |
| [Flux (Black Forest Labs)](https://docs.bfl.ml/) | State-of-the-art open image generation models (Flux.1 Pro/Dev/Schnell) | 🟡 API Key | ✅ | ✅⭐ |
| [Ideogram](https://developer.ideogram.ai/api-reference) | AI image generation with exceptional text rendering in images | 🟡 API Key | ✅ | ✅⭐ |
| [Leonardo AI](https://docs.leonardo.ai/reference) | Creative AI platform for production-quality image assets | 🟡 API Key | ✅ | ✅⭐ |
| [Google Imagen](https://cloud.google.com/vertex-ai/generative-ai/docs/image/overview) | Google's image generation and editing via Vertex AI | 🟡 API Key | ✅ | ✅⭐ |
| [Runway](https://docs.runwayml.com/) | AI video generation (Gen-3 Alpha) and creative tools | 🟡 API Key | ✅ | ✅⭐ |
| [Luma AI](https://docs.lumalabs.ai/) | AI video generation (Dream Machine) and 3D capture | 🟡 API Key | ✅ | ✅⭐ |
| [Kling AI](https://docs.klingai.com/) | High-quality AI video generation with realistic motion | 🟡 API Key | ✅ | ✅⭐ |
| [Pika](https://docs.pika.art/) | AI video generation and editing with creative controls | 🟡 API Key | ✅ | ✅ |
| [Suno](https://docs.suno.com/) | AI music and song generation from text prompts | 🟡 API Key | ✅ | ✅⭐ |
| [Udio](https://docs.udio.com/) | AI music generation with high-fidelity audio | 🟡 API Key | ✅ | ✅ |
| [Recraft](https://www.recraft.ai/docs) | AI design tool for generating and editing vector/raster images | 🟡 API Key | ✅ | ✅⭐ |
| [Fal.ai](https://fal.ai/docs) | Fast inference for image/video generation models with serverless GPUs | 🟡 API Key | ✅ | ✅⭐ |

---

## 🗄️ Knowledge Graphs & Structured Data

> APIs for accessing structured knowledge useful for AI agent reasoning.

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Wikidata SPARQL](https://query.wikidata.org/) | Query the world's largest open knowledge graph with SPARQL | 🟢 No | ✅ | ✅⭐ |
| [DBpedia](https://www.dbpedia.org/resources/sparql/) | Structured data extracted from Wikipedia in machine-readable format | 🟢 No | ✅ | ✅⭐ |
| [Google Knowledge Graph](https://developers.google.com/knowledge-graph) | Entity search across Google's knowledge base | 🟡 API Key | ✅ | ✅⭐ |
| [Wolfram Alpha](https://products.wolframalpha.com/api/) | Computational knowledge engine — math, science, data, and more | 🟡 API Key | ✅ | ✅⭐ |
| [OpenAlex](https://docs.openalex.org/) | Open catalog of 250M+ scholarly works, authors, and institutions | 🟢 No | ✅ | ✅⭐ |
| [Semantic Scholar](https://api.semanticscholar.org/) | AI-powered academic paper search with citation graphs | 🟡 API Key | ✅ | ✅⭐ |
| [ConceptNet](https://conceptnet.io/) | Open multilingual knowledge graph of common sense | 🟢 No | ✅ | ✅⭐ |
| [Diffbot Knowledge Graph](https://docs.diffbot.com/docs/en/kg-index) | AI-constructed knowledge graph from the entire public web | 🟡 API Key | ✅ | ✅⭐ |

---

## 🛡️ AI Safety & Guardrails

> APIs for content moderation, toxicity detection, and AI safety for agent outputs.

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [OpenAI Moderation](https://platform.openai.com/docs/guides/moderation) | Free content moderation API — detects harmful text categories | 🟡 API Key | ✅ | ✅⭐ |
| [Perspective API](https://www.perspectiveapi.com/) | Google's toxicity and abuse detection for online conversations | 🟡 API Key | ✅ | ✅⭐ |
| [Azure Content Safety](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/) | Multi-modal content moderation (text, image, video) | 🟡 API Key | ✅ | ✅⭐ |
| [Hive Moderation](https://docs.thehive.ai/) | Visual and text content moderation with custom categories | 🟡 API Key | ✅ | ✅ |
| [LlamaGuard](https://huggingface.co/meta-llama/Llama-Guard-3-8B) | Meta's open-source safety classifier for LLM inputs/outputs | 🟢 No | ✅ | ✅⭐ |
| [Guardrails AI](https://docs.guardrailsai.com/) | Open-source framework for validating LLM outputs | 🟢 No | ✅ | ✅⭐ |
| [NeMo Guardrails](https://docs.nvidia.com/nemo/guardrails/) | NVIDIA's toolkit for adding safety to LLM-powered applications | 🟢 No | ✅ | ✅⭐ |
| [Rebuff](https://docs.rebuff.ai/) | Self-hardening prompt injection detection API | 🟡 API Key | ✅ | ✅⭐ |

---

## 🌍 Geospatial & Earth Observation

> Satellite imagery, mapping data, and Earth science APIs for spatial reasoning.

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [NASA Earthdata](https://www.earthdata.nasa.gov/) | 1000+ satellite imagery products covering the entire globe | 🟢 No | ✅ | ✅⭐ |
| [NASA GIBS](https://wiki.earthdata.nasa.gov/display/GIBS/GIBS+API+for+Developers) | Full-resolution satellite imagery via WMTS/WMS/KML | 🟢 No | ✅ | ✅⭐ |
| [Google Earth Engine](https://developers.google.com/earth-engine/reference) | Petabyte-scale satellite analysis platform with Python/JS API | 🟡 API Key | ✅ | ✅⭐ |
| [Copernicus Open Access Hub](https://scihub.copernicus.eu/dhus/#/home) | Free Sentinel satellite data (10m resolution, 5-day refresh) | 🟢 No | ✅ | ✅⭐ |
| [USGS EarthExplorer](https://m2m.cr.usgs.gov/) | Decades of Landsat satellite imagery and aerial photos | 🟡 API Key | ✅ | ✅⭐ |
| [OpenStreetMap Overpass](https://overpass-api.de/) | Query OpenStreetMap data — buildings, roads, POIs worldwide | 🟢 No | ✅ | ✅⭐ |
| [Mapbox Tilesets](https://docs.mapbox.com/api/maps/tilesets/) | Custom map tiles, terrain, and satellite imagery | 🟡 API Key | ✅ | ✅⭐ |
| [UP42](https://docs.up42.com/) | Marketplace for satellite imagery and geospatial analytics | 🟡 API Key | ✅ | ✅⭐ |
| [Planet](https://developers.planet.com/docs/apis/) | Daily high-resolution satellite imagery of the entire Earth | 🟡 API Key | ✅ | ✅⭐ |
| [Radiant MLHub](https://mlhub.earth/) | Open library for geospatial ML training data | 🟡 API Key | ✅ | ✅⭐ |
| [Stadia Maps](https://docs.stadiamaps.com/) | Map tiles, geocoding, and routing APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Protomaps](https://docs.protomaps.com/) | Open-source serverless vector map tiles | 🟢 No | ✅ | ✅⭐ |
| [Overture Maps](https://docs.overturemaps.org/) | Open map data from Linux Foundation (buildings, places, transport) | 🟢 No | ✅ | ✅⭐ |
| [STAC API](https://stacspec.org/) | SpatioTemporal Asset Catalog — standard for geospatial data search | 🟢 No | ✅ | ✅⭐ |

---

## ⚡ Real-Time Data & Streaming APIs

> APIs with WebSocket, SSE, or streaming support for live data feeds.

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [OpenAI Realtime API](https://platform.openai.com/docs/guides/realtime) | Real-time speech-to-speech with GPT-4o via WebSocket | 🟡 API Key | ✅ | ✅⭐ |
| [Finnhub WebSocket](https://finnhub.io/docs/api/websocket-trades) | Real-time stock trades, forex, and crypto via WebSocket | 🟡 API Key | ✅ | ✅⭐ |
| [CoinCap WebSocket](https://docs.coincap.io/#37dcbe0f-eb09-4580-8406-3c683e662905) | Real-time cryptocurrency price streaming | 🟢 No | ✅ | ✅⭐ |
| [Binance WebSocket](https://binance-docs.github.io/apidocs/spot/en/#websocket-market-streams) | Real-time crypto market data streams | 🟢 No | ✅ | ✅⭐ |
| [Polygon.io WebSocket](https://polygon.io/docs/stocks/ws_getting-started) | Real-time stock, options, and crypto data | 🟡 API Key | ✅ | ✅⭐ |
| [Ably](https://ably.com/docs/api/realtime-sdk) | Pub/sub messaging infrastructure with global edge network | 🟡 API Key | ✅ | ✅⭐ |
| [Pusher Channels](https://pusher.com/docs/channels/library_auth_reference/rest-api/) | Real-time WebSocket event broadcasting | 🟡 API Key | ✅ | ✅⭐ |
| [LiveKit](https://docs.livekit.io/) | Open-source real-time audio/video/data infrastructure | 🟡 API Key | ✅ | ✅⭐ |
| [NOAA Weather Alerts](https://www.weather.gov/documentation/services-web-api) | Real-time severe weather alerts via API | 🟢 No | ✅ | ✅⭐ |
| [USGS Earthquake Feed](https://earthquake.usgs.gov/earthquakes/feed/) | Real-time global earthquake data (GeoJSON, updated every minute) | 🟢 No | ✅ | ✅⭐ |
| [ADS-B Exchange](https://www.adsbexchange.com/data/) | Real-time global flight tracking (unfiltered) | 🟡 API Key | ✅ | ✅⭐ |
| [ntfy](https://docs.ntfy.sh/) | Simple HTTP-based pub/sub notification service — no signup needed | 🟢 No | ✅ | ✅⭐ |
| [Mercure](https://mercure.rocks/docs/hub/api) | Open protocol for real-time server push (SSE-based) | 🟢 No | ✅ | ✅⭐ |
| [Centrifugo](https://centrifugal.dev/docs/server/server_api) | Scalable real-time messaging server with WebSocket/SSE | 🟢 No | ✅ | ✅⭐ |

---

## 💻 AI Coding & Development APIs

> APIs for code generation, analysis, and AI-assisted development.

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [GitHub Copilot API](https://docs.github.com/en/copilot/building-copilot-extensions) | Code completions and chat via Copilot extensions | 🟡 API Key | ✅ | ✅⭐ |
| [Sourcegraph API](https://docs.sourcegraph.com/api/graphql) | Code search and intelligence across entire codebases | 🟡 API Key | ✅ | ✅⭐ |
| [Tabnine](https://docs.tabnine.com/) | Privacy-focused AI code completions with local model option | 🟡 API Key | ✅ | ✅⭐ |
| [Codeium](https://codeium.com/docs) | Free AI code autocomplete supporting 70+ languages | 🟡 API Key | ✅ | ✅⭐ |
| [Codestral (Mistral)](https://docs.mistral.ai/capabilities/code_generation/) | Mistral's code-optimized model with fill-in-the-middle support | 🟡 API Key | ✅ | ✅⭐ |
| [DeepSeek Coder](https://platform.deepseek.com/api-docs/) | Open-source code model with ultra-low cost inference | 🟡 API Key | ✅ | ✅⭐ |
| [Qwen Coder](https://help.aliyun.com/zh/model-studio/) | Alibaba's code generation model supporting 90+ languages | 🟡 API Key | ✅ | ✅⭐ |
| [Replit Model](https://docs.replit.com/category/model) | Code generation model trained on Replit's codebase | 🟡 API Key | ✅ | ✅⭐ |
| [GitLab Duo API](https://docs.gitlab.com/ee/api/) | AI-powered code suggestions and merge request summaries | 🟡 API Key | ✅ | ✅⭐ |
| [SonarQube API](https://sonarcloud.io/web_api) | Code quality and security analysis REST API | 🟡 API Key | ✅ | ✅⭐ |
| [Semgrep](https://semgrep.dev/docs/semgrep-code/semgrep-api/) | Static analysis for finding bugs and security vulnerabilities | 🟡 API Key | ✅ | ✅⭐ |
| [CodeRabbit](https://docs.coderabbit.ai/) | AI-powered code review for pull requests | 🟡 API Key | ✅ | ✅⭐ |

---

## 🔧 MCP Servers & Tool Ecosystem

> Notable Model Context Protocol servers that give AI agents access to tools and data.

| MCP Server | Description | Auth | Category | Agent-Friendly |
|------------|-------------|------|----------|----------------|
| [Playwright MCP](https://github.com/microsoft/playwright-mcp) | Browser automation — navigate, click, screenshot, fill forms (12K+ stars) | 🟢 No | Browser | ✅⭐ |
| [GitHub MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/github) | Full GitHub API access — repos, issues, PRs, code search | 🟡 API Key | DevOps | ✅⭐ |
| [PostgreSQL MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres) | Query databases, manage schemas, analyze data via natural language | 🟡 API Key | Database | ✅⭐ |
| [Filesystem MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) | Read, write, search, and manage local files securely | 🟢 No | System | ✅⭐ |
| [Brave Search MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search) | Web search and local business search via Brave | 🟡 API Key | Search | ✅⭐ |
| [Notion MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/notion) | Full Notion workspace access — pages, databases, blocks | 🟡 API Key | Productivity | ✅⭐ |
| [Slack MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/slack) | Read/post messages, manage channels, search conversations | 🟡 API Key | Communication | ✅⭐ |
| [Google Drive MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/google-drive) | Access and search Google Drive files | 🔴 OAuth | Storage | ✅ |
| [Puppeteer MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer) | Headless Chrome automation for web scraping and testing | 🟢 No | Browser | ✅⭐ |
| [Sentry MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/sentry) | Query error reports, analyze crash data, investigate issues | 🟡 API Key | Monitoring | ✅⭐ |
| [Memory MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/memory) | Persistent knowledge graph memory for agent context | 🟢 No | Memory | ✅⭐ |
| [SQLite MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite) | Local SQL database access for data analysis and queries | 🟢 No | Database | ✅⭐ |
| [Fetch MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) | HTTP requests to any URL with content extraction | 🟢 No | Network | ✅⭐ |
| [Zapier MCP](https://zapier.com/mcp) | Access to 7,000+ apps and 30,000+ actions via MCP | 🟡 API Key | Automation | ✅⭐ |
| [Supabase MCP](https://github.com/supabase-community/supabase-mcp) | Database, auth, storage, and edge functions via MCP | 🟡 API Key | Database | ✅⭐ |
| [Linear MCP](https://github.com/jerhadf/linear-mcp-server) | Issue tracking — create, update, search, and manage projects | 🟡 API Key | Project Mgmt | ✅⭐ |
| [Stripe MCP](https://github.com/stripe/agent-toolkit) | Payment processing, subscription management, invoicing | 🟡 API Key | Payments | ✅⭐ |
| [Cloudflare MCP](https://github.com/cloudflare/mcp-server-cloudflare) | Manage Workers, KV, R2, and DNS via MCP | 🟡 API Key | Infrastructure | ✅⭐ |
| [Vercel MCP](https://vercel.com/docs/mcp) | Manage deployments, domains, and environment variables | 🟡 API Key | Hosting | ✅⭐ |
| [Docker MCP](https://github.com/docker/mcp-server-docker) | Manage containers, images, networks, and compose stacks | 🟢 No | Infrastructure | ✅⭐ |

---

## 🌐 Web3 & Decentralized Agent Infrastructure

> Blockchain and Web3 APIs purpose-built for autonomous AI agents.

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Lit Protocol](https://developer.litprotocol.com/) | Decentralized key management and access control for agents | 🟡 API Key | ✅ | ✅⭐ |
| [Story Protocol](https://docs.story.foundation/) | On-chain IP registration and licensing for AI-generated content | 🟡 API Key | ✅ | ✅⭐ |
| [Virtuals Protocol](https://docs.virtuals.io/) | Platform for creating and deploying on-chain AI agents | 🟡 API Key | ✅ | ✅⭐ |
| [Autonolas](https://docs.autonolas.network/) | Open-source framework for on-chain autonomous AI agent services | 🟢 No | ✅ | ✅⭐ |
| [WeatherXM](https://docs.weatherxm.com/api/) | DePIN weather network — community-deployed weather stations | 🟡 API Key | ✅ | ✅⭐ |
| [io.net](https://docs.io.net/) | Decentralized GPU compute network for AI inference | 🟡 API Key | ✅ | ✅⭐ |
| [Akash Network](https://docs.akash.network/) | Decentralized cloud compute marketplace for AI workloads | 🟡 API Key | ✅ | ✅⭐ |
| [Render Network](https://rendernetwork.com/docs) | Decentralized GPU rendering for AI and 3D visualization | 🟡 API Key | ✅ | ✅ |
| [Arweave](https://docs.arweave.org/) | Permanent decentralized data storage (200+ years) | 🟢 No | ✅ | ✅⭐ |
| [IPFS HTTP API](https://docs.ipfs.tech/reference/http/api/) | Decentralized content-addressed file storage | 🟢 No | ✅ | ✅⭐ |
| [The Graph](https://thegraph.com/docs/en/) | Indexed blockchain data via GraphQL subgraphs | 🟡 API Key | ✅ | ✅⭐ |
| [Moralis](https://docs.moralis.io/) | Cross-chain Web3 data API — NFTs, tokens, DeFi, wallets | 🟡 API Key | ✅ | ✅⭐ |
| [Covalent](https://www.covalenthq.com/docs/) | Unified API for 200+ blockchains — balances, transactions, NFTs | 🟡 API Key | ✅ | ✅⭐ |
| [Dune Analytics](https://docs.dune.com/api-reference/overview/introduction) | Query blockchain data with SQL and access community dashboards | 🟡 API Key | ✅ | ✅⭐ |
| [Neynar](https://docs.neynar.com/) | Farcaster protocol API — social graph, casts, channels | 🟡 API Key | ✅ | ✅⭐ |
| [Crossmint](https://docs.crossmint.com/) | NFT minting and wallet creation via API (no crypto knowledge needed) | 🟡 API Key | ✅ | ✅⭐ |

---

## 📡 Uptime Monitoring & Status APIs

> APIs for monitoring service health, uptime, and creating status pages.

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Uptime Robot](https://uptimerobot.com/api/) | Monitor 50 URLs free — HTTP, ping, port, keyword monitoring | 🟡 API Key | ✅ | ✅⭐ |
| [OpenStatus](https://docs.openstatus.dev/) | Open-source uptime monitoring and status pages | 🟡 API Key | ✅ | ✅⭐ |
| [Better Stack](https://betterstack.com/docs/uptime/api/) | Uptime monitoring with incident management | 🟡 API Key | ✅ | ✅⭐ |
| [Checkly](https://www.checklyhq.com/docs/api-checks/) | API and browser check monitoring with Playwright-based tests | 🟡 API Key | ✅ | ✅⭐ |
| [Healthchecks.io](https://healthchecks.io/docs/api/) | Cron job and background task monitoring via simple pings | 🟡 API Key | ✅ | ✅⭐ |
| [Gatus](https://github.com/TwiN/gatus) | Open-source health dashboard with YAML config | 🟢 No | ✅ | ✅⭐ |
| [Uptime Kuma](https://github.com/louislam/uptime-kuma/wiki/API) | Self-hosted monitoring tool with beautiful dashboard | 🟢 No | ✅ | ✅⭐ |
| [Instatus](https://instatus.com/help/api) | Beautiful status pages with API for incident management | 🟡 API Key | ✅ | ✅⭐ |
| [Cachet](https://docs.cachethq.io/reference) | Open-source status page system with REST API | 🟡 API Key | ✅ | ✅⭐ |
| [Pingdom](https://docs.pingdom.com/api/) | Website and API monitoring with transaction checks | 🟡 API Key | ✅ | ✅ |

---

## 🧪 Developer Utility & Testing APIs

> Miscellaneous utility APIs useful for agent development, testing, and prototyping.

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Webhook.site](https://docs.webhook.site/) | Instantly inspect and test HTTP requests and webhooks | 🟢 No | ✅ | ✅⭐ |
| [Beeceptor](https://beeceptor.com/docs/api/) | Mock REST APIs and intercept HTTP traffic | 🟢 No | ✅ | ✅⭐ |
| [Mockoon](https://mockoon.com/docs/latest/api-endpoints/overview/) | Local-first API mocking with JSON templating | 🟢 No | ✅ | ✅⭐ |
| [Hoppscotch](https://docs.hoppscotch.io/) | Open-source API development environment | 🟢 No | ✅ | ✅⭐ |
| [WireMock](https://wiremock.org/docs/api/) | Flexible API mocking and service virtualization | 🟢 No | ✅ | ✅⭐ |
| [Nock](https://github.com/nock/nock) | HTTP server mocking for Node.js testing | 🟢 No | ✅ | ✅⭐ |
| [Random.org](https://api.random.org/json-rpc/4/) | True random numbers from atmospheric noise (JSON-RPC) | 🟡 API Key | ✅ | ✅⭐ |
| [Crontab.guru API](https://crontab.guru/) | Validate and explain cron expressions | 🟢 No | ✅ | ✅⭐ |
| [JWT.io](https://jwt.io/) | JSON Web Token debugger and library directory | 🟢 No | ✅ | ✅⭐ |
| [RegExr](https://regexr.com/) | Regular expression tester with community patterns | 🟢 No | ✅ | ✅⭐ |
| [ExchangeRate.host](https://exchangerate.host/) | Free currency exchange rates and crypto rates | 🟢 No | ✅ | ✅⭐ |
| [Country State City](https://countrystatecity.in/) | Countries, states, and cities database with REST API | 🟡 API Key | ✅ | ✅⭐ |
| [Faker.js Online](https://fakerjs.dev/) | Generate massive amounts of realistic fake data | 🟢 No | ✅ | ✅⭐ |
| [UnDesign](https://undesign.learn.uno/) | Collection of free design tools and resources | 🟢 No | ✅ | ✅ |
| [Carbon](https://carbon.now.sh/) | Create beautiful code snippet images for documentation | 🟢 No | ✅ | ✅⭐ |

---

## 📱 Mobile & Cross-Platform APIs

> APIs for mobile development, push notifications, and cross-platform services.

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Expo](https://docs.expo.dev/push-notifications/overview/) | Cross-platform push notifications for React Native apps | 🟢 No | ✅ | ✅⭐ |
| [RevenueCat](https://www.revenuecat.com/docs/api-v1) | In-app subscription management across iOS, Android, and web | 🟡 API Key | ✅ | ✅⭐ |
| [OneSignal](https://documentation.onesignal.com/reference) | Multi-platform push notifications with segmentation | 🟡 API Key | ✅ | ✅⭐ |
| [AppFollow](https://docs.appfollow.io/) | App store reviews, ratings, and ASO monitoring | 🟡 API Key | ✅ | ✅⭐ |
| [data.ai (App Annie)](https://www.data.ai/en/apps/api/) | App store analytics and market intelligence | 🟡 API Key | ✅ | ✅ |
| [Apple App Store Connect](https://developer.apple.com/documentation/appstoreconnectapi) | iOS app management, TestFlight, and analytics | 🟡 API Key | ✅ | ✅⭐ |
| [Google Play Developer](https://developers.google.com/android-publisher) | Android app publishing, in-app purchases, and reviews | 🟡 API Key | ✅ | ✅⭐ |
| [App Store Scraper](https://github.com/facundoolano/app-store-scraper) | Scrape app data from App Store and Google Play | 🟢 No | ✅ | ✅⭐ |

---

## 🏛️ Open Data & Government APIs (Extended)

> Government and institutional open data APIs from around the world.

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [EU Open Data Portal](https://data.europa.eu/api/hub/search/) | European Union institutional data (15,000+ datasets) | 🟢 No | ✅ | ✅⭐ |
| [UK Open Data](https://www.data.gov.uk/) | UK government datasets (50,000+ datasets) | 🟢 No | ✅ | ✅⭐ |
| [Japan e-Stat](https://www.e-stat.go.jp/api/) | Japanese government statistical data | 🟡 API Key | ✅ | ✅ |
| [Korea Open Data](https://www.data.go.kr/) | Korean government open data portal | 🟡 API Key | ✅ | ✅ |
| [data.gov](https://catalog.data.gov/dataset) | US federal government dataset catalog (300,000+ datasets) | 🟢 No | ✅ | ✅⭐ |
| [ProPublica Congress](https://projects.propublica.org/api-docs/congress-api/) | US Congress members, bills, votes, and committees | 🟡 API Key | ✅ | ✅⭐ |
| [Open States](https://v3.openstates.org/docs) | US state legislature data — bills, votes, legislators | 🟡 API Key | ✅ | ✅⭐ |
| [Federal Register](https://www.federalregister.gov/developers/documentation/api/v1) | US federal agency documents and regulations | 🟢 No | ✅ | ✅⭐ |
| [SEC EDGAR Full-Text](https://efts.sec.gov/LATEST/search-index?q=%22api%22) | Full-text search of SEC company filings | 🟢 No | ✅ | ✅⭐ |
| [WHO GHO](https://www.who.int/data/gho/info/gho-odata-api) | World Health Organization global health data | 🟢 No | ✅ | ✅⭐ |
| [FAO FAOSTAT](https://www.fao.org/faostat/en/#data) | UN food and agriculture statistics | 🟢 No | ✅ | ✅⭐ |
| [ITU ICT Data](https://datahub.itu.int/data/) | Telecommunications and ICT statistics | 🟢 No | ✅ | ✅ |

---

## 🎯 Conversion & Enrichment APIs

> APIs for converting, enriching, and transforming data for agent workflows.

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Clearbit](https://dashboard.clearbit.com/docs) | Company and person data enrichment from email/domain | 🟡 API Key | ✅ | ✅⭐ |
| [FullContact](https://docs.fullcontact.com/) | Identity resolution and contact data enrichment | 🟡 API Key | ✅ | ✅⭐ |
| [ZoomInfo](https://api-docs.zoominfo.com/) | B2B company and contact intelligence | 🟡 API Key | ✅ | ✅ |
| [Brandfetch](https://docs.brandfetch.com/) | Company logo, colors, and brand assets from any domain | 🟡 API Key | ✅ | ✅⭐ |
| [Logo.dev](https://docs.logo.dev/) | High-quality company logos by domain name | 🟡 API Key | ✅ | ✅⭐ |
| [Hunter.io](https://hunter.io/api-documentation) | Find and verify professional email addresses | 🟡 API Key | ✅ | ✅⭐ |
| [Snov.io](https://snov.io/api) | Email finder, verifier, and drip campaign API | 🟡 API Key | ✅ | ✅ |
| [PDFShift](https://pdfshift.io/documentation/) | Convert HTML to high-fidelity PDF documents | 🟡 API Key | ✅ | ✅⭐ |
| [Docspring](https://docspring.com/docs/api) | Fill PDF templates with data via API | 🟡 API Key | ✅ | ✅⭐ |
| [CloudConvert](https://cloudconvert.com/api/v2) | Convert between 200+ file formats | 🟡 API Key | ✅ | ✅⭐ |
| [Unstructured](https://unstructured-io.github.io/unstructured/) | Extract structured data from PDFs, images, and documents | 🟡 API Key | ✅ | ✅⭐ |
| [LlamaParse](https://docs.cloud.llamaindex.ai/llamaparse/getting_started) | Parse complex documents (PDFs, PPTX) into LLM-ready markdown | 🟡 API Key | ✅ | ✅⭐ |
| [Docling (IBM)](https://ds4sd.github.io/docling/) | Open-source document parsing for RAG pipelines | 🟢 No | ✅ | ✅⭐ |

---

## 🔊 AI Voice & Telephony APIs

> APIs for voice agents, phone automation, and conversational AI over voice.

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Vapi](https://docs.vapi.ai/) | Build voice AI agents — handles speech, LLM, and telephony | 🟡 API Key | ✅ | ✅⭐ |
| [Bland.ai](https://docs.bland.ai/) | AI phone calling API — make/receive calls with AI agents | 🟡 API Key | ✅ | ✅⭐ |
| [Retell AI](https://docs.retellai.com/) | Build human-like voice agents with sub-second latency | 🟡 API Key | ✅ | ✅⭐ |
| [PlayHT](https://docs.play.ht/) | Ultra-realistic text-to-speech with voice cloning | 🟡 API Key | ✅ | ✅⭐ |
| [Cartesia](https://docs.cartesia.ai/) | Real-time voice generation with emotion control | 🟡 API Key | ✅ | ✅⭐ |
| [Fish Audio](https://docs.fish.audio/) | Multilingual voice cloning and text-to-speech | 🟡 API Key | ✅ | ✅⭐ |
| [Telnyx](https://developers.telnyx.com/) | Programmable voice, SMS, and fax with SIP trunking | 🟡 API Key | ✅ | ✅⭐ |
| [Vocode](https://docs.vocode.dev/) | Open-source library for building voice AI agents | 🟢 No | ✅ | ✅⭐ |
| [Pipecat](https://docs.pipecat.ai/) | Open-source framework for voice and multimodal AI agents | 🟢 No | ✅ | ✅⭐ |
| [Daily Bots](https://docs.dailybots.ai/) | Deploy voice and video AI agents on Daily's infrastructure | 🟡 API Key | ✅ | ✅⭐ |

---

## 💰 AI Payment & Commerce APIs

> Payment and commerce APIs designed for autonomous agent transactions.

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Stripe Agent Toolkit](https://github.com/stripe/agent-toolkit) | Official Stripe toolkit for AI agent payment processing | 🟡 API Key | ✅ | ✅⭐ |
| [Coinbase Commerce](https://docs.cloud.coinbase.com/commerce/reference) | Accept crypto payments — Bitcoin, Ethereum, USDC, etc. | 🟡 API Key | ✅ | ✅⭐ |
| [LemonSqueezy](https://docs.lemonsqueezy.com/api) | Digital product sales with global tax handling | 🟡 API Key | ✅ | ✅⭐ |
| [Polar](https://docs.polar.sh/api/) | Open-source monetization for developers | 🟡 API Key | ✅ | ✅⭐ |
| [Gumroad](https://gumroad.com/api) | Sell digital products, memberships, and subscriptions | 🟡 API Key | ✅ | ✅⭐ |
| [Paddle](https://developer.paddle.com/) | SaaS billing with built-in tax and compliance | 🟡 API Key | ✅ | ✅⭐ |
| [Open Exchange Rates](https://docs.openexchangerates.org/) | Real-time and historical exchange rates for 170+ currencies | 🟡 API Key | ✅ | ✅⭐ |
| [Wise (TransferWise)](https://api-docs.transferwise.com/) | International money transfers with real exchange rates | 🟡 API Key | ✅ | ✅⭐ |

---

## 🔐 Cybersecurity & Threat Intelligence APIs

> APIs for vulnerability data, threat intel, and security analysis.

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [MITRE ATT&CK](https://attack.mitre.org/resources/working-with-attack/) | Adversary tactics and techniques knowledge base (free, open) | 🟢 No | ✅ | ✅⭐ |
| [MITRE CVE](https://cveawg.mitre.org/api-docs/) | Official CVE vulnerability records API | 🟢 No | ✅ | ✅⭐ |
| [NVD (NIST)](https://nvd.nist.gov/developers) | National Vulnerability Database — CVE details and CVSS scores | 🟡 API Key | ✅ | ✅⭐ |
| [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) | Known Exploited Vulnerabilities catalog (JSON feed) | 🟢 No | ✅ | ✅⭐ |
| [CVEDetails](https://www.cvedetails.com/api/v1/docs) | CVE security vulnerability database with stats | 🟡 API Key | ✅ | ✅⭐ |
| [MITRE ATLAS](https://atlas.mitre.org/) | Adversarial threat landscape for AI systems | 🟢 No | ✅ | ✅⭐ |
| [OSV (Google)](https://osv.dev/) | Open-source vulnerability database for packages | 🟢 No | ✅ | ✅⭐ |
| [Exploit-DB](https://www.exploit-db.com/) | Archive of public exploits and proof-of-concepts | 🟢 No | ✅ | ✅⭐ |
| [AbuseIPDB](https://www.abuseipdb.com/api) | IP address abuse/blacklist checking | 🟡 API Key | ✅ | ✅⭐ |
| [URLhaus](https://urlhaus-api.abuse.ch/) | Malware URL intelligence feed | 🟢 No | ✅ | ✅⭐ |
| [MalwareBazaar](https://bazaar.abuse.ch/api/) | Malware sample sharing and analysis | 🟢 No | ✅ | ✅⭐ |
| [OTX AlienVault](https://otx.alienvault.com/api) | Open threat exchange for IOCs and threat data | 🟡 API Key | ✅ | ✅⭐ |
| [GreyNoise](https://docs.greynoise.io/) | Internet-wide scanner and attack traffic intelligence | 🟡 API Key | ✅ | ✅⭐ |
| [SecurityTrails](https://securitytrails.com/corp/apidocs) | DNS history, WHOIS, and domain intelligence | 🟡 API Key | ✅ | ✅⭐ |
| [Censys](https://search.censys.io/api) | Internet-wide scan data for hosts and certificates | 🟡 API Key | ✅ | ✅⭐ |

---

## 🌱 Climate & Sustainability APIs

> Carbon footprint, emissions data, and environmental sustainability APIs.

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Climatiq](https://www.climatiq.io/docs) | Carbon emission factor calculations with 330,000+ data points | 🟡 API Key | ✅ | ✅⭐ |
| [Carbon Interface](https://docs.carboninterface.com/) | Calculate carbon emissions for flights, vehicles, electricity | 🟡 API Key | ✅ | ✅⭐ |
| [Electricity Maps](https://api-portal.electricitymaps.com/) | Real-time carbon intensity of electricity by region | 🟡 API Key | ✅ | ✅⭐ |
| [WattTime](https://www.watttime.org/api-documentation/) | Real-time grid emissions data for clean energy optimization | 🟡 API Key | ✅ | ✅⭐ |
| [CarbonCloud](https://carboncloud.com/api/) | Climate footprint data for the food system | 🟡 API Key | ✅ | ✅ |
| [Open Charge Map](https://openchargemap.org/site/develop/api) | Global EV charging station registry (210,000+ locations) | 🟡 API Key | ✅ | ✅⭐ |
| [Global Forest Watch](https://www.globalforestwatch.org/developers/) | Real-time deforestation monitoring and forest data | 🟢 No | ✅ | ✅⭐ |
| [NASA POWER](https://power.larc.nasa.gov/docs/) | Solar irradiance and meteorological data for energy planning | 🟢 No | ✅ | ✅⭐ |
| [NREL Developer](https://developer.nrel.gov/) | Renewable energy datasets — solar, wind, geothermal, hydrogen | 🟡 API Key | ✅ | ✅⭐ |
| [Ocean Health Index](https://oceanhealthindex.org/data/) | Global ocean health assessments and indicators | 🟢 No | ✅ | ✅ |

---

## 🗃️ Backend-as-a-Service & Database APIs

> Open-source and managed BaaS platforms with REST/GraphQL APIs.

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Supabase](https://supabase.com/docs/reference) | Open-source Firebase alternative — Postgres, Auth, Storage, Realtime | 🟡 API Key | ✅ | ✅⭐ |
| [Appwrite](https://appwrite.io/docs/references) | Open-source BaaS — databases, auth, storage, functions, messaging | 🟡 API Key | ✅ | ✅⭐ |
| [PocketBase](https://pocketbase.io/docs/api-rules/) | Lightweight Go-based BaaS with SQLite (single binary) | 🟡 API Key | ✅ | ✅⭐ |
| [Directus](https://docs.directus.io/reference/introduction.html) | Open data platform — instant REST/GraphQL API for any SQL database | 🟡 API Key | ✅ | ✅⭐ |
| [Strapi](https://docs.strapi.io/dev-docs/api/rest) | Open-source headless CMS with customizable REST/GraphQL APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Convex](https://docs.convex.dev/) | Reactive backend-as-a-service with real-time sync and serverless functions | 🟡 API Key | ✅ | ✅⭐ |
| [Nhost](https://docs.nhost.io/) | Open-source Firebase alternative with GraphQL (Hasura + Postgres) | 🟡 API Key | ✅ | ✅⭐ |
| [Back4App](https://www.back4app.com/docs) | Parse Server-based BaaS with REST & GraphQL APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Turso](https://docs.turso.tech/) | Edge SQLite database (libSQL) with global replication | 🟡 API Key | ✅ | ✅⭐ |
| [Xata](https://xata.io/docs/api-reference/overview) | Serverless data platform with full-text search and vector embeddings | 🟡 API Key | ✅ | ✅⭐ |
| [CockroachDB Serverless](https://www.cockroachlabs.com/docs/api/) | Distributed SQL database with generous free tier | 🟡 API Key | ✅ | ✅⭐ |
| [Upstash](https://upstash.com/docs/redis/overall/getstarted) | Serverless Redis, Kafka, and Vector — per-request pricing | 🟡 API Key | ✅ | ✅⭐ |

---

## 🤝 Workflow Automation APIs

> APIs for orchestrating multi-step workflows and connecting services.

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Zapier](https://platform.zapier.com/docs/api) | 8,000+ app integrations with AI agent and MCP support | 🔴 OAuth | ✅ | ⚠️ |
| [Make (Integromat)](https://www.make.com/en/api-documentation) | Visual workflow builder with powerful branching and transforms | 🟡 API Key | ✅ | ✅⭐ |
| [n8n](https://docs.n8n.io/api/) | Open-source workflow automation with LangChain integration | 🟡 API Key | ✅ | ✅⭐ |
| [Pipedream](https://pipedream.com/docs/api/) | Developer-first serverless workflows with code steps | 🟡 API Key | ✅ | ✅⭐ |
| [Activepieces](https://www.activepieces.com/docs/developers/overview) | Open-source Zapier alternative with AI pieces | 🟡 API Key | ✅ | ✅⭐ |
| [Windmill](https://www.windmill.dev/docs/intro) | Open-source developer platform for scripts, flows, and apps | 🟡 API Key | ✅ | ✅⭐ |
| [Temporal](https://docs.temporal.io/) | Durable execution platform for reliable workflows at scale | 🟡 API Key | ✅ | ✅⭐ |
| [Inngest](https://www.inngest.com/docs) | Event-driven durable functions with built-in retries and scheduling | 🟡 API Key | ✅ | ✅⭐ |
| [Trigger.dev](https://trigger.dev/docs) | Open-source background jobs with long-running task support | 🟡 API Key | ✅ | ✅⭐ |
| [Prefect](https://docs.prefect.io/latest/api-ref/) | Python workflow orchestration for data pipelines | 🟡 API Key | ✅ | ✅⭐ |
| [Dagster](https://docs.dagster.io/apidocs) | Data orchestration platform with asset-based pipelines | 🟡 API Key | ✅ | ✅⭐ |
| [Apache Airflow](https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html) | Workflow scheduling and monitoring with REST API | 🟡 API Key | ✅ | ✅⭐ |

---

## 📧 Email & Marketing APIs

> APIs for sending emails, managing campaigns, and email verification.

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Resend](https://resend.com/docs/api-reference/introduction) | Modern email API built for developers — React Email support | 🟡 API Key | ✅ | ✅⭐ |
| [Postmark](https://postmarkapp.com/developer) | Transactional email with industry-best deliverability | 🟡 API Key | ✅ | ✅⭐ |
| [Loops](https://loops.so/docs/api) | Email marketing API for SaaS — drip campaigns, newsletters | 🟡 API Key | ✅ | ✅⭐ |
| [Brevo (Sendinblue)](https://developers.brevo.com/) | Email, SMS, and marketing automation — generous free tier | 🟡 API Key | ✅ | ✅⭐ |
| [Amazon SES](https://docs.aws.amazon.com/ses/) | High-volume email sending at $0.10 per 1,000 emails | 🟡 API Key | ✅ | ✅⭐ |
| [Mailtrap](https://api-docs.mailtrap.io/) | Email testing and sending API with sandbox environment | 🟡 API Key | ✅ | ✅⭐ |
| [ZeroBounce](https://www.zerobounce.net/docs/) | Email validation and deliverability testing | 🟡 API Key | ✅ | ✅⭐ |
| [MailerSend](https://developers.mailersend.com/) | Transactional email and SMS with analytics dashboard | 🟡 API Key | ✅ | ✅⭐ |
| [Buttondown](https://api.buttondown.email/) | Newsletter API with Markdown support and RSS import | 🟡 API Key | ✅ | ✅⭐ |
| [ConvertKit (Kit)](https://developers.convertkit.com/) | Creator-focused email marketing with automation | 🟡 API Key | ✅ | ✅⭐ |

---

## 🏗️ Infrastructure-as-Code & DevOps APIs

> APIs for managing cloud infrastructure, containers, and deployments.

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Terraform Cloud](https://developer.hashicorp.com/terraform/cloud-docs/api-docs) | Infrastructure automation with state management | 🟡 API Key | ✅ | ✅⭐ |
| [Pulumi](https://www.pulumi.com/docs/pulumi-cloud/reference/api/) | IaC platform with TypeScript/Python/Go support | 🟡 API Key | ✅ | ✅⭐ |
| [Spacelift](https://docs.spacelift.io/integrations/api) | GitOps infrastructure management and policy engine | 🟡 API Key | ✅ | ✅⭐ |
| [ArgoCD](https://argo-cd.readthedocs.io/en/stable/developer-guide/api-docs/) | Kubernetes GitOps continuous delivery | 🟡 API Key | ✅ | ✅⭐ |
| [Portainer](https://docs.portainer.io/api/access) | Container management with REST API for Docker and K8s | 🟡 API Key | ✅ | ✅⭐ |
| [Coolify](https://coolify.io/docs/api/authentication) | Self-hosted Heroku/Vercel alternative with REST API | 🟡 API Key | ✅ | ✅⭐ |
| [Caprover](https://caprover.com/docs/get-started.html) | PaaS for deploying apps with Docker | 🟡 API Key | ✅ | ✅⭐ |
| [Dokku](https://dokku.com/docs/advanced-usage/plugin-management/) | Lightweight self-hosted PaaS (mini Heroku) | 🟢 No | ✅ | ✅⭐ |

---

## 📐 Math, Science & Research APIs

> APIs for computation, scientific data, and academic research.

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Wolfram Alpha](https://products.wolframalpha.com/api/) | Computational knowledge engine — solve any math/science problem | 🟡 API Key | ✅ | ✅⭐ |
| [Mathpix](https://docs.mathpix.com/) | OCR for math equations — convert images/PDFs to LaTeX/MathML | 🟡 API Key | ✅ | ✅⭐ |
| [Symbolab](https://www.symbolab.com/solver) | Step-by-step math problem solver | 🟢 No | ✅ | ✅ |
| [Newton API](https://newton.vercel.app/) | Micro-service for mathematical operations (derive, integrate, etc.) | 🟢 No | ✅ | ✅⭐ |
| [arXiv API](https://info.arxiv.org/help/api/) | Search and access 2.4M+ scientific papers | 🟢 No | ✅ | ✅⭐ |
| [Crossref](https://api.crossref.org/) | Academic metadata for 150M+ scholarly works — DOIs, citations | 🟢 No | ✅ | ✅⭐ |
| [OpenAlex](https://docs.openalex.org/) | Open catalog of scholarly works, authors, institutions (250M+ records) | 🟢 No | ✅ | ✅⭐ |
| [CORE](https://core.ac.uk/services/api) | Aggregator of open access research papers (300M+ articles) | 🟡 API Key | ✅ | ✅⭐ |
| [Europe PMC](https://europepmc.org/RestfulWebService) | Life sciences literature — 40M+ abstracts and full-text articles | 🟢 No | ✅ | ✅⭐ |
| [PubChem](https://pubchemdocs.ncbi.nlm.nih.gov/pug-rest) | Chemical compound database with 100M+ substances | 🟢 No | ✅ | ✅⭐ |

---

## 🎮 Esports & Competitive Gaming APIs

> APIs for competitive gaming data, tournaments, and player stats.

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [PandaScore](https://developers.pandascore.co/) | Esports data — LoL, CS2, Dota 2, Valorant tournaments | 🟡 API Key | ✅ | ✅⭐ |
| [FACEIT](https://developers.faceit.com/docs/getting-started/overview) | Competitive gaming platform data and matchmaking | 🟡 API Key | ✅ | ✅⭐ |
| [Stratz](https://docs.stratz.com/) | Dota 2 match data and analytics (GraphQL) | 🟡 API Key | ✅ | ✅⭐ |
| [OpenDota](https://docs.opendota.com/) | Open-source Dota 2 data platform | 🟢 No | ✅ | ✅⭐ |
| [Tracker Network](https://tracker.gg/developers/docs/getting-started) | Stats for Fortnite, Apex, Valorant, and more | 🟡 API Key | ✅ | ✅⭐ |
| [Riot Data Dragon](https://developer.riotgames.com/docs/lol#data-dragon) | League of Legends game data — champions, items, runes | 🟢 No | ✅ | ✅⭐ |
| [Steam Web API](https://developer.valvesoftware.com/wiki/Steam_Web_API) | Steam user data, game stats, and achievements | 🟡 API Key | ✅ | ✅⭐ |
| [Chess.com](https://www.chess.com/news/view/published-data-api) | Chess game data, player profiles, and club info | 🟢 No | ✅ | ✅⭐ |
| [Lichess](https://lichess.org/api) | Open-source chess platform API — games, puzzles, tournaments | 🟢 No | ✅ | ✅⭐ |

---

## ⚖️ Legal & Compliance APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [CourtListener](https://www.courtlistener.com/help/api/rest/) | Millions of U.S. federal/state court opinions, PACER data, and citation graphs | 🟡 API Key | ✅ | ✅⭐ |
| [Federal Register API](https://www.federalregister.gov/developers/documentation/api/v1) | U.S. federal rules, proposed rules, notices, and executive orders | 🟢 No | ✅ | ✅⭐ |
| [eCFR API](https://www.ecfr.gov/developers/documentation/api/v1) | Electronic Code of Federal Regulations — continuously updated | 🟢 No | ✅ | ✅⭐ |
| [Regulations.gov](https://open.gsa.gov/api/regulationsgov/) | U.S. federal regulatory documents and public comments | 🟡 API Key | ✅ | ✅⭐ |
| [Caselaw Access Project](https://case.law/) | Harvard Law — 360+ years of digitized U.S. case law | 🟡 API Key | ✅ | ✅⭐ |
| [Clio API](https://docs.developers.clio.com/) | Legal practice management — matters, billing, calendars | 🔴 OAuth | ✅ | ✅ |
| [DocuSign API](https://developers.docusign.com/) | Electronic signatures and contract lifecycle management | 🔴 OAuth | ✅ | ✅ |
| [Fastcase / vLex](https://www.fastcase.com/solutions/legal-data-api/) | Case law, statutes, and regulations from 100+ countries | 🟡 API Key | ✅ | ✅ |
| [PracticePanther](https://www.practicepanther.com/) | Cloud legal practice management and workflow automation | 🔴 OAuth | ✅ | ⚠️ |

---

## 🎓 Education & EdTech APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Canvas LMS API](https://www.canvas.instructure.com/doc/api/) | Instructure Canvas — courses, assignments, grades, enrollments | 🔴 OAuth | ✅ | ✅⭐ |
| [Moodle Web Services](https://docs.moodle.org/dev/Web_services_API) | Open-source LMS — hundreds of functions, self-hostable | 🟡 API Key | ✅ | ✅⭐ |
| [Google Classroom API](https://developers.google.com/workspace/classroom/reference/rest) | Manage classes, coursework, and student submissions | 🔴 OAuth | ✅ | ✅⭐ |
| [Open edX API](https://courses.edx.org/api-docs/) | Open-source online course platform — catalog, enrollment, grades | 🟡 API Key | ✅ | ✅⭐ |
| [Schoology API](https://developers.schoology.com/api/) | Users, courses, assignments, and grades in Schoology LMS | 🔴 OAuth | ✅ | ✅ |
| [Unified.to LMS API](https://unified.to/blog/introducing_unified_lms_api) | Unified API connecting multiple LMS platforms via single endpoint | 🟡 API Key | ✅ | ✅⭐ |
| [Edlink API](https://ed.link/) | Middleware connecting EdTech apps to Canvas, Schoology, Google Classroom | 🟡 API Key | ✅ | ✅⭐ |
| [Khan Academy](https://www.khanacademy.org/) | 6,000+ educational videos and exercises — free content | 🔴 OAuth | ✅ | ⚠️ |
| [PowerSchool API](https://support.powerschool.com/) | K-12 student information system — REST API | 🔴 OAuth | ✅ | ⚠️ |

---

## 🏠 IoT & Smart Home APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Home Assistant API](https://developers.home-assistant.io/docs/api/rest) | Open-source home automation — 2,700+ integrations, REST + WebSocket | 🟡 API Key | ✅ | ✅⭐ |
| [Tuya Cloud API](https://developer.tuya.com/en/docs/cloud/smart_home_paas) | IoT cloud — 400,000+ device types, sensors, lights, appliances | 🟡 API Key | ✅ | ✅⭐ |
| [Philips Hue API](https://developers.meethue.com/) | Smart lighting — bulbs, rooms, scenes, schedules, sensors | 🟡 API Key | ✅ | ✅⭐ |
| [SmartThings API](https://developer.smartthings.com/) | Samsung IoT — devices, scenes, automations across brands | 🔴 OAuth | ✅ | ✅ |
| [Arduino IoT Cloud](https://docs.arduino.cc/arduino-cloud/api/arduino-iot-api/) | IoT devices, Things, Properties — 400+ hardware models | 🔴 OAuth | ✅ | ✅ |
| [ThingSpeak](https://www.mathworks.com/help/thingspeak/rest-api.html) | IoT analytics — collect, store, visualize sensor data | 🟡 API Key | ✅ | ✅⭐ |
| [Blynk API](https://docs.blynk.io/en/) | Low-code IoT — ESP32, Arduino, Raspberry Pi support | 🟡 API Key | ✅ | ✅⭐ |
| [Particle Cloud API](https://docs.particle.io/reference/cloud-apis/api/) | Cellular/Wi-Fi IoT — device functions, OTA firmware updates | 🟡 API Key | ✅ | ✅ |
| [IFTTT Webhooks](https://ifttt.com/docs) | 900+ apps/devices connected via triggers and actions | 🟡 API Key | ✅ | ⚠️ |

---

## 📄 Document AI & OCR APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Mistral OCR](https://docs.mistral.ai/capabilities/document_ai) | State-of-the-art OCR — clean markdown output, table reconstruction | 🟡 API Key | ✅ | ✅⭐ |
| [AWS Textract](https://docs.aws.amazon.com/textract/) | ML-powered text, table, form, and handwriting extraction | 🟡 API Key | ✅ | ✅⭐ |
| [Google Cloud Vision AI](https://cloud.google.com/vision/docs) | Best OCR accuracy — multilingual, handwriting, style analysis | 🟡 API Key | ✅ | ✅⭐ |
| [Azure Document Intelligence](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/) | Text, key-value pairs, tables extraction (formerly Form Recognizer) | 🟡 API Key | ✅ | ✅⭐ |
| [Mindee API](https://developers.mindee.com/) | Parse invoices, receipts, passports, IDs — pre-trained models | 🟡 API Key | ✅ | ✅⭐ |
| [Reducto](https://reducto.ai/) | AI document parsing for complex layouts — charts, graphs, multi-column | 🟡 API Key | ✅ | ✅⭐ |
| [Veryfi API](https://www.veryfi.com/api/) | Receipts, invoices, W2s — 98.7% accuracy, 3-5 sec extraction | 🟡 API Key | ✅ | ✅ |
| [Nanonets](https://nanonets.com/) | Custom OCR models — no-code training, document parsing | 🟡 API Key | ✅ | ✅ |
| [Docsumo](https://www.docsumo.com/) | Deep learning document processing — key-value pairs, entities | 🟡 API Key | ✅ | ✅ |
| [ABBYY Cloud OCR](https://www.abbyy.com/cloud-ocr-sdk/) | Enterprise OCR — 200+ languages, complex documents | 🟡 API Key | ✅ | ✅ |
| [Klippa DocHorizon](https://www.klippa.com/en/ocr-api/) | OCR with fraud detection and GDPR compliance — 100+ doc types | 🟡 API Key | ✅ | ✅ |

---

## 🌐 Translation & Localization APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [DeepL API](https://www.deepl.com/en/pro-api) | Best-in-class neural translation — 30+ languages, document translation | 🟡 API Key | ✅ | ✅⭐ |
| [Google Cloud Translation](https://cloud.google.com/translate/docs) | Neural MT — 130+ languages, custom models, LLM-powered options | 🟡 API Key | ✅ | ✅⭐ |
| [LibreTranslate](https://libretranslate.com/) | Free, open-source, self-hostable translation — offline capable | 🟢 No | ✅ | ✅⭐ |
| [Microsoft Translator](https://learn.microsoft.com/en-us/azure/ai-services/translator/) | 100+ languages — transliteration, detection, dictionary lookup | 🟡 API Key | ✅ | ✅⭐ |
| [Amazon Translate](https://docs.aws.amazon.com/translate/) | Real-time/batch translation — customizable terminology | 🟡 API Key | ✅ | ✅ |
| [MyMemory](https://mymemory.translated.net/doc/spec.php) | Free translation memory — MT + human translations, no registration | 🟢 No | ✅ | ✅⭐ |
| [Lingva Translate](https://github.com/thedaviddelta/lingva-translate) | Open-source Google Translate front-end — REST + GraphQL | 🟢 No | ✅ | ✅⭐ |
| [Weblate API](https://docs.weblate.org/en/latest/api.html) | Open-source translation management — CI/CD integration, Git-native | 🟡 API Key | ✅ | ✅ |
| [Smartling](https://www.smartling.com/) | Enterprise translation management — AI + human linguistic expertise | 🟡 API Key | ✅ | ✅ |
| [Lara Translate](https://blog.laratranslate.com/) | Context-aware neural translation — adaptive learning engine | 🟡 API Key | ✅ | ✅ |

---

## 💼 CRM APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [HubSpot CRM API](https://developers.hubspot.com/docs/guides/crm/understanding-the-crm) | Contacts, companies, deals, tickets — free tier available | 🟡 API Key | ✅ | ✅⭐ |
| [Salesforce REST API](https://developer.salesforce.com/docs/apis) | World's largest CRM — leads, opportunities, custom objects | 🔴 OAuth | ✅ | ✅⭐ |
| [Pipedrive API](https://developers.pipedrive.com/) | Sales CRM — persons, organizations, deals, pipelines | 🟡 API Key | ✅ | ✅⭐ |
| [Zoho CRM API](https://www.zoho.com/crm/developer/) | Full-featured CRM — records, workflows, free developer account | 🔴 OAuth | ✅ | ✅ |
| [Monday.com API](https://developer.monday.com/api-reference/) | Work management + CRM — GraphQL, flexible data model | 🟡 API Key | ✅ | ✅⭐ |
| [Freshsales API](https://developers.freshworks.com/crm/api/) | SME-friendly sales CRM — contacts, deals, sequences | 🟡 API Key | ✅ | ✅⭐ |
| [Close CRM](https://developer.close.com/) | Startup CRM — leads, email sequences, built-in calling | 🟡 API Key | ✅ | ✅⭐ |
| [Attio API](https://developers.attio.com/) | Next-gen CRM — flexible data modeling, real-time sync | 🟡 API Key | ✅ | ✅⭐ |
| [Copper CRM](https://developer.copper.com/) | Google Workspace-native CRM — leads, people, opportunities | 🟡 API Key | ✅ | ✅ |
| [Apideck CRM](https://www.apideck.com/crm-api) | Unified API — one integration for 25+ CRM systems | 🟡 API Key | ✅ | ✅⭐ |

---

## 📋 Project Management APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Jira Cloud REST API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/) | Issues, sprints, boards, workflows — JQL query language | 🔴 OAuth | ✅ | ✅⭐ |
| [Asana API](https://developers.asana.com/reference/rest-api-reference) | Tasks, projects, portfolios, goals — official SDKs | 🔴 OAuth | ✅ | ✅⭐ |
| [Linear API](https://developers.linear.app/) | Modern issue tracking — GraphQL, real-time webhooks | 🟡 API Key | ✅ | ✅⭐ |
| [Notion API](https://developers.notion.com/) | Databases, pages, blocks — block-based content model | 🟡 API Key | ✅ | ✅⭐ |
| [ClickUp API](https://developer.clickup.com/) | All-in-one PM — spaces, tasks, time tracking, goals | 🟡 API Key | ✅ | ✅⭐ |
| [Trello API](https://developer.atlassian.com/cloud/trello/rest/) | Kanban boards, lists, and cards — simple data model | 🟡 API Key | ✅ | ✅⭐ |
| [Smartsheet API](https://developers.smartsheet.com/) | Enterprise work management — sheets, rows, workspaces | 🟡 API Key | ✅ | ✅ |
| [Wrike API](https://developers.wrike.com/) | Enterprise PM — folders, tasks, workflows, approvals | 🔴 OAuth | ✅ | ✅ |
| [Basecamp API](https://github.com/basecamp/bc3-api) | Projects, to-dos, messages, schedules — open source docs | 🔴 OAuth | ✅ | ✅ |

---

## 🏘️ Real Estate & Property APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [ATTOM Data API](https://api.developer.attomdata.com/) | 158M+ U.S. properties — ownership, sales, valuations, schools | 🟡 API Key | ✅ | ✅⭐ |
| [RentCast API](https://developers.rentcast.io/) | 140M+ properties — rental estimates, listings, market trends | 🟡 API Key | ✅ | ✅⭐ |
| [SimplyRETS](https://docs.simplyrets.com/api/index.html) | MLS data via RETS/RESO standard — live listings | 🟡 API Key | ✅ | ✅⭐ |
| [Bridge Interactive](https://www.bridgeinteractive.com/developers/bridge-api/) | Normalized MLS data from multiple boards + Zestimates | 🟡 API Key | ✅ | ✅⭐ |
| [Mashvisor API](https://www.mashvisor.com/api) | Investment analytics — cap rate, cash-on-cash return | 🟡 API Key | ✅ | ✅ |
| [Estated API](https://estated.com/) | Standardized property data — ownership, taxes, deeds | 🟡 API Key | ✅ | ✅ |
| [BatchData API](https://batchdata.io/) | Property data + skip tracing — bulk queries supported | 🟡 API Key | ✅ | ✅ |
| [Repliers API](https://repliers.com/) | Canadian + U.S. MLS boards with normalized data | 🟡 API Key | ✅ | ✅ |
| [Zillow APIs](https://www.zillowgroup.com/developers/) | Zestimates, MLS listings, mortgage data (~20 APIs) | 🟡 API Key | ✅ | ⚠️ |
| [Xotelo](https://xotelo.com/) | Hotel pricing data from TripAdvisor + OTAs — free tier | 🟡 API Key | ✅ | ✅ |

---

## ✈️ Travel & Booking APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Amadeus Self-Service](https://developers.amadeus.com/) | 400+ airlines, 150K+ hotels, 300K+ activities — free test tier | 🟡 API Key | ✅ | ✅⭐ |
| [Duffel Flights API](https://duffel.com/) | 300+ airlines including NDC — search, book, manage flights | 🟡 API Key | ✅ | ✅⭐ |
| [Kiwi.com Tequila](https://tequila.kiwi.com/) | Flights, trains, buses — virtual interlining across carriers | 🟡 API Key | ✅ | ✅⭐ |
| [Skyscanner Affiliate](https://www.partners.skyscanner.net/) | 1,200+ travel partners — flight price comparison | 🟡 API Key | ✅ | ✅⭐ |
| [Hotelbeds API](https://developer.hotelbeds.com/) | 300K hotels in 200 countries — booking, content, cache APIs | 🟡 API Key | ✅ | ✅ |
| [Expedia Rapid API](https://partner.expediagroup.com/) | 700K+ accommodations — dynamic pricing, geo definitions | 🟡 API Key | ✅ | ✅ |
| [Sabre Dev Studio](https://developer.sabre.com/) | Major GDS — flights, hotels, car rental, travel intelligence | 🟡 API Key | ✅ | ✅ |
| [Travelport APIs](https://developer.travelport.com/) | Multi-GDS (Apollo/Worldspan/Galileo) — mobile-optimized REST | 🟡 API Key | ✅ | ✅ |
| [TripAdvisor Content](https://www.tripadvisor.com/developers) | Reviews, ratings, photos for hotels/restaurants/attractions | 🟡 API Key | ✅ | ⚠️ |
| [Booking.com API](https://www.booking.com/content/affiliates.html) | World's largest accommodation platform — partnership required | 🟡 API Key | ✅ | ⚠️ |

---

## 👥 HR, People & Payroll APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [BambooHR API](https://documentation.bamboohr.com/reference) | HRIS — employee records, time-off, benefits, onboarding | 🟡 API Key | ✅ | ✅⭐ |
| [Finch Unified API](https://www.tryfinch.com/) | "Plaid for employment" — connects 220+ HRIS/payroll systems | 🟡 API Key | ✅ | ✅⭐ |
| [Deel API](https://developer.deel.com/) | Global payroll — 100+ countries, contractor/employee onboarding | 🟡 API Key | ✅ | ✅⭐ |
| [Merge HRIS API](https://www.merge.dev/categories/hris-and-payroll-api) | Unified API for 70+ HRIS/payroll platforms — webhooks | 🟡 API Key | ✅ | ✅⭐ |
| [Gusto Embedded Payroll](https://embedded.gusto.com/) | SMB payroll/benefits — embed payroll into your product | 🔴 OAuth | ✅ | ✅ |
| [Rippling API](https://developer.rippling.com/) | Unified HR + IT + Finance — employee & device management | 🔴 OAuth | ✅ | ✅ |
| [Personio API](https://developer.personio.de/) | European HR — GDPR-compliant, recruiting, attendance | 🟡 API Key | ✅ | ✅ |
| [HiBob API](https://apidocs.hibob.com/) | Modern HRIS — onboarding, analytics, performance reviews | 🟡 API Key | ✅ | ✅ |
| [Kombo API](https://www.kombo.dev/) | Unified HRIS/payroll — auto field mapping, fast setup | 🟡 API Key | ✅ | ✅ |
| [Factorial API](https://apidoc.factorialhr.com/) | Talent management, recruitment, time tracking, payroll | 🟡 API Key | ✅ | ✅ |
| [Paylocity API](https://developer.paylocity.com/) | Enterprise HCM — payroll, HR, talent, workforce management | 🔴 OAuth | ✅ | ⚠️ |

---

## 📦 Supply Chain & Logistics APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [EasyPost API](https://www.easypost.com/docs/api) | Multi-carrier — rate comparison, labels, tracking, insurance | 🟡 API Key | ✅ | ✅⭐ |
| [ShipEngine](https://www.shipengine.com/) | 200+ global carriers — labels, tracking, SDKs in 8 languages | 🟡 API Key | ✅ | ✅⭐ |
| [AfterShip Tracking](https://www.aftership.com/docs/tracking) | 1,100+ carriers — tracking webhooks, ETA, branded pages | 🟡 API Key | ✅ | ✅⭐ |
| [Shippo API](https://docs.goshippo.com/) | 14+ carriers — rates, labels, tracking, returns, pay-as-you-go | 🟡 API Key | ✅ | ✅⭐ |
| [FedEx Developer API](https://developer.fedex.com/) | Rates, labels, tracking, pickups, address validation | 🔴 OAuth | ✅ | ✅ |
| [UPS Developer API](https://developer.ups.com/) | Shipping, tracking, time-in-transit, freight services | 🔴 OAuth | ✅ | ✅ |
| [DHL Tracking API](https://developer.dhl.com/api-reference/shipment-tracking) | Real-time DHL shipment tracking worldwide | 🟡 API Key | ✅ | ✅ |
| [Flexport API](https://developers.flexport.com/) | Freight forwarding, customs, supply chain management | 🟡 API Key | ✅ | ✅ |
| [Vizion Container Tracking](https://www.vizionapi.com/) | Ocean container tracking — push-based, standardized events | 🟡 API Key | ✅ | ✅ |
| [ClickPost](https://www.clickpost.ai/shipping-api) | E-commerce shipping aggregator — auto carrier selection | 🟡 API Key | ✅ | ✅ |
| [Tive Logistics](https://www.tive.com/) | Multi-sensor tracking — location, temperature, humidity, shock | 🟡 API Key | ✅ | ✅ |
| [Chain.io](https://chain.io/logistics-api/) | Supply chain integration — EDI modernization, partner onboarding | 🟡 API Key | ✅ | ⚠️ |

---

## 🛡️ Insurance APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Lemonade API](https://api-doc-portal.lemonade.com/) | AI-powered renters/homeowners insurance — quoting, policy, claims | 🟡 API Key | ✅ | ✅⭐ |
| [Canopy Connect](https://www.usecanopy.com/api) | "Plaid for Insurance" — 400+ carriers, instant verification | 🟡 API Key | ✅ | ✅⭐ |
| [Socotra API](https://www.socotra.com/technology/) | Enterprise insurance core — full policy lifecycle, cloud-native | 🟡 API Key | ✅ | ✅ |
| [Bolttech API](https://api-int.bolttech.io/docs/intro) | Embedded insurance — quote, bind, pay, omni-channel | 🟡 API Key | ✅ | ✅ |
| [Boost Insurance](https://boostinsurance.com/developer/) | Insurance infrastructure — quote-to-bind for digital platforms | 🟡 API Key | ✅ | ✅ |
| [Qover API](https://www.qover.com/) | European embedded insurance — travel, mobility, e-commerce | 🟡 API Key | ✅ | ✅ |
| [Igloo Insurtech](https://iglooinsure.com/tech-solutions/insurance-api-centre/) | Full insurance value chain — SE Asia market leader | 🟡 API Key | ✅ | ✅ |
| [Root Insurance](https://www.joinroot.com/) | Telematics-based auto insurance — AI-powered pricing | 🟡 API Key | ✅ | ⚠️ |
| [Insurify](https://insurify.com/) | Multi-carrier insurance comparison — auto, home, life | 🟡 API Key | ✅ | ⚠️ |
| [Novidea](https://novidea.com/) | Broker/MGA platform — CRM, policies, analytics, commissions | 🟡 API Key | ✅ | ⚠️ |

---

## 🌾 Agriculture & AgTech APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [USDA ARMS Data API](https://www.ers.usda.gov/developer/data-apis/arms-data-api) | Farm finances, production practices, resource use — free | 🟢 No | ✅ | ✅⭐ |
| [Farmonaut API](https://farmonaut.com/farmonaut-satellite-weather-api-developer-docs) | Satellite crop monitoring (NDVI, EVI), weather, soil analysis | 🟡 API Key | ✅ | ✅⭐ |
| [OpenWeatherMap Agro](https://agromonitoring.com/api) | Agricultural weather, satellite imagery, vegetation indices | 🟡 API Key | ✅ | ✅⭐ |
| [Trefle Plant API](https://docs.trefle.io/) | 417,000+ plant species — search by common/scientific name | 🟡 API Key | ✅ | ✅⭐ |
| [OpenFarm API](https://github.com/openfarmcc/OpenFarm/blob/mainline/docs/api_docs.md) | Open-source crop growing guides — planting, soil, spacing | 🟡 API Key | ✅ | ✅⭐ |
| [Azure Data Manager for Agriculture](https://learn.microsoft.com/en-us/rest/api/data-manager-for-agri/) | Enterprise farm management — satellite, weather, sensors | 🔴 OAuth | ✅ | ✅ |
| [EOS Agriculture API](https://eos.com/agriculture-api/) | Crop data, weather data, soil moisture information | 🟡 API Key | ✅ | ✅ |
| [Agworld API](https://us.agworld.co/user_api/v1/docs) | Farm management — fields, farms, recommendations | 🟡 API Key | ✅ | ✅ |

---

## 🖨️ 3D Printing & Manufacturing APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [OctoPrint REST API](https://docs.octoprint.org/en/main/api/index.html) | Open-source 3D printer control — jobs, temp, files, state | 🟡 API Key | ✅ | ✅⭐ |
| [3DPrinterOS](https://www.3dprinteros.com/3d-printing-management-apis-reference) | Cloud slicing, print queue, fleet management | 🟡 API Key | ✅ | ✅ |
| [Shapeways API](https://developers.shapeways.com) | On-demand 3D manufacturing — upload, quote, fulfill orders | 🔴 OAuth | ✅ | ✅ |
| [i.materialise API](https://i.materialise.com/api-dokuwiki/) | Full 3D print workflow — 25+ materials, pricing, checkout | 🟡 API Key | ✅ | ✅ |
| [Sculpteo API](https://www.sculpteo.com/en/services/api-services/) | Professional 3D printing — upload, configure, quote, order | 🟡 API Key | ✅ | ✅ |
| [Slant 3D](https://www.slant3d.com/slant-3d-printing-api) | Large-scale 3D printer farms for production scaling | 🟡 API Key | ✅ | ✅ |
| [Create it REAL](https://www.createitreal.com/3d-printing-api-service/) | Slicing core API — embeddable slicing engine | 🟡 API Key | ✅ | ⚠️ |
| [Prusa Connect](https://connect.prusa3d.com/) | Remote Prusa printer monitoring and control | 🟡 API Key | ✅ | ⚠️ |

---

## ♿ Accessibility & WCAG APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [axe-core](https://www.deque.com/axe/core-documentation/api-documentation/) | Open-source a11y engine — WCAG 2.0/2.1/2.2, zero false positives | 🟢 No | ✅ | ✅⭐ |
| [Pa11y](https://pa11y.org/) | Open-source automated a11y testing — CLI + Node.js API | 🟢 No | ✅ | ✅⭐ |
| [WAVE API](https://wave.webaim.org/api/) | WebAIM accessibility scanner — WCAG errors, ARIA issues | 🟡 API Key | ✅ | ✅⭐ |
| [axe DevTools](https://www.deque.com/axe/) | Enterprise a11y testing — CI/CD integration, multi-language | 🟡 API Key | ✅ | ✅ |
| [Pope Tech](https://www.pope.tech/) | Enterprise WAVE-powered — millions of pages/month, WCAG 2.2 | 🟡 API Key | ✅ | ✅ |
| [Tenon.io](https://tenon.io/) | API-driven a11y testing — enterprise reporting, governance | 🟡 API Key | ✅ | ✅ |
| [WAVE Standalone](https://wave.webaim.org/standalone) | Self-hosted WAVE engine — scan private/secure pages | 🟡 API Key | ✅ | ✅ |

---

## 🔐 Identity Verification & KYC APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Sumsub API](https://docs.sumsub.com/reference/get-started-with-api) | KYC/KYB/AML — 220+ countries, 140K verifications/day | 🟡 API Key | ✅ | ✅⭐ |
| [Veriff API](https://www.veriff.com/plans/self-serve) | 98% automation rate — 11,500+ doc types, 6-second decisions | 🟡 API Key | ✅ | ✅⭐ |
| [Microblink KYC](https://docs.microblink.com/documentation/cloudapi/overview.html) | AI document scanning — 500+ doc types, sub-5-second verification | 🟡 API Key | ✅ | ✅⭐ |
| [Plaid Identity](https://plaid.com/docs/api/products/identity-verification/) | Identity verification tied to financial accounts | 🟡 API Key | ✅ | ✅⭐ |
| [Onfido / Entrust](https://documentation.identity.entrust.com/api/latest/) | Document + biometric verification — SDKs for mobile + web | 🟡 API Key | ✅ | ✅ |
| [iDenfy](https://www.idenfy.com/) | Human-in-loop KYC — 3D liveness, 200+ countries, pay-for-success | 🟡 API Key | ✅ | ✅ |
| [Didit](https://didit.me/) | Unified IDV — liveness, face matching, AML, free tier | 🟡 API Key | ✅ | ✅ |

---

## 🎫 Event & Ticketing APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Ticketmaster Discovery](https://developer.ticketmaster.com/products-and-docs/apis/discovery-api/v2/) | Events, attractions, venues globally — 5K calls/day free | 🟡 API Key | ✅ | ✅⭐ |
| [SeatGeek API](https://platform.seatgeek.com/) | Events, performers, venues, recommendations — JSON/JSONP | 🟡 API Key | ✅ | ✅⭐ |
| [Eventbrite API](https://www.eventbrite.com/platform/docs/introduction) | Event management, ticketing, discovery — millions of events | 🔴 OAuth | ✅ | ✅ |
| [StubHub API](https://developer.stubhub.com/docs/overview/introduction/) | World's largest ticket marketplace — search, buy, list | 🔴 OAuth | ✅ | ✅ |
| [Ticket Tailor](https://developers.tickettailor.com/docs/api/ticket-tailor-api/) | Event ticketing — 5K requests/30 min, clean docs | 🟡 API Key | ✅ | ✅ |
| [Ticketbud API](https://api.ticketbud.com/) | Event creation, management, ticket sales | 🔴 OAuth | ✅ | ✅ |
| [EventBookings API](https://developers.eventbookings.com/) | Event management, booking, registration | 🟡 API Key | ✅ | ✅ |
| [Ticket Evolution](https://developer.ticketevolution.com/) | Event discovery + ticket reseller platform | 🟡 API Key | ✅ | ⚠️ |

---

## ⌚ Fitness Wearable APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Terra API](https://docs.tryterra.co/health-and-fitness-api/getting-started) | Unified API for 400+ wearables — Apple Watch, Garmin, Fitbit, Oura | 🟡 API Key | ✅ | ✅⭐ |
| [ROOK API](https://docs.tryrook.io/) | Unified wearable health data from 400+ devices — normalized | 🟡 API Key | ✅ | ✅⭐ |
| [Strava API](https://developers.strava.com/docs/reference/) | Activities, athletes, segments, routes, clubs | 🔴 OAuth | ✅ | ✅⭐ |
| [Oura Ring API v2](https://cloud.ouraring.com/v2/docs) | Sleep, readiness, activity, HRV, body temperature | 🔴 OAuth | ✅ | ✅ |
| [Fitbit Web API](https://dev.fitbit.com/) | Activity, heart rate, sleep, HRV data | 🔴 OAuth | ✅ | ✅ |
| [Garmin Health API](https://developer.garmin.com/health-sdk/) | Comprehensive fitness/health data from Garmin devices | 🔴 OAuth | ✅ | ✅ |
| [WHOOP API](https://developer.whoop.com/api/) | Strain, sleep, HRV, recovery metrics | 🔴 OAuth | ✅ | ⚠️ |
| [FitBark API](https://www.fitbark.com/dev) | Canine health — play, active, rest monitoring | 🔴 OAuth | ✅ | ✅ |

---

## 🚀 Space & Astronomy APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [NASA Open APIs](https://api.nasa.gov/) | APOD, Mars Rover, asteroids, EPIC Earth imagery — 1K req/hr | 🟡 API Key | ✅ | ✅⭐ |
| [SpaceX API](https://docs.spacexdata.com/) | Open-source — rockets, launches, capsules, cores, pads | 🟢 No | ✅ | ✅⭐ |
| [Where the ISS at?](https://wheretheiss.at/w/developer) | ISS real-time position and pass predictions — free | 🟢 No | ✅ | ✅⭐ |
| [Open Notify](http://open-notify.org/Open-Notify-API/) | ISS location, people in space — no auth needed | 🟢 No | ❌ | ✅⭐ |
| [Astronomy API](https://astronomyapi.com/) | Planet/star positions, celestial events for any location | 🟡 API Key | ✅ | ✅ |
| [Solar System OpenData](https://api.le-systeme-solaire.net/en/) | Planets, moons, asteroids — mass, gravity, orbital params | 🟡 API Key | ✅ | ✅ |
| [N2YO Satellite Tracking](https://www.n2yo.com/api/) | Satellite positions, TLE data, pass predictions | 🟡 API Key | ✅ | ✅ |
| [Time and Date Astronomy](https://dev.timeanddate.com/astro/) | Sunrise/sunset, moon phases, astronomical positions | 🟡 API Key | ✅ | ✅ |

---

## 🧬 Genealogy APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [FamilySearch API](https://www.familysearch.org/developers/docs/api/resources) | Family trees, pedigrees, historical records — nonprofit, free | 🔴 OAuth | ✅ | ✅⭐ |
| [Open Archives](https://openarch.nl/) | Free genealogy records — civil registration, church records | 🟢 No | ✅ | ✅⭐ |
| [GEDCOM X](https://github.com/FamilySearch/gedcomx) | Open standard for genealogy data — JSON + XML | 🟢 No | ✅ | ✅⭐ |
| [Geni API](https://www.geni.com/platform/developer/help) | Genealogy profiles, relationships, tree data — sandbox | 🔴 OAuth | ✅ | ✅ |
| [MyHeritage Family Graph](https://familygraph.com/) | Family trees — read-only, no fees, JSON REST | 🔴 OAuth | ✅ | ⚠️ |
| [FindMyPast API](https://www.tamurajones.net/FindmypastAPI.xhtml) | Hints API + Related Search for record discovery | 🟡 API Key | ✅ | ⚠️ |

---

## 🐾 Pet Services APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Petfinder API v2](https://www.petfinder.com/developers/v2/docs/) | 100K+ adoptable pets — 1K req/day, search by breed/location | 🔴 OAuth | ✅ | ✅⭐ |
| [TheDogAPI](https://docs.thedogapi.com/) | Dog images + breed data — medical, nutritional labels | 🟡 API Key | ✅ | ✅⭐ |
| [TheCatAPI](https://developers.thecatapi.com/) | Cat images + breed data — same schema as TheDogAPI | 🟡 API Key | ✅ | ✅⭐ |
| [openFDA Animal Vet](https://open.fda.gov/apis/animalandveterinary/event/) | Adverse event reports for animal drugs/devices — free | 🟢 No | ✅ | ✅⭐ |
| [RescueGroups.org](https://rescuegroups.org/services/adoptable-pet-data-api/) | Adoptable pet search by zip, distance, breed, age | 🟡 API Key | ✅ | ✅ |

---

## ⚡ Renewable Energy APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [UK Carbon Intensity](https://api.carbonintensity.org.uk/) | GB electricity carbon intensity — real-time + forecasts, free | 🟢 No | ✅ | ✅⭐ |
| [Solcast Solar API](https://docs.solcast.com.au/) | Solar irradiance forecasts + PV power predictions — global | 🟡 API Key | ✅ | ✅⭐ |
| [NREL Developer APIs](https://developer.nrel.gov/docs/) | Utility rates, solar resource, wind data, alt fuels — free | 🟡 API Key | ✅ | ✅⭐ |
| [Electricity Maps](https://docs.electricitymaps.com/) | Carbon intensity + energy mix — 230+ regions, 100+ countries | 🟡 API Key | ✅ | ✅⭐ |
| [WattTime API](https://docs.watttime.org/) | Marginal emissions at 5-min granularity — global coverage | 🟡 API Key | ✅ | ✅ |
| [Open Charge Map](https://openchargemap.org/site/develop/api) | Global EV charging station registry — crowdsourced, open data | 🟡 API Key | ✅ | ✅ |
| [OpenEI Utility Rates](https://developer.nrel.gov/docs/electricity/openei-utility-rates/) | U.S. utility rate structures from National Utility Rate DB | 🟡 API Key | ✅ | ✅ |

---

## 🏗️ Construction & Building APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Procore API](https://developers.procore.com/reference/rest/docs/rest-api-overview) | Construction management — project, financial, field management | 🔴 OAuth | ✅ | ✅⭐ |
| [Shovels API](https://www.shovels.ai/api) | Building permit + contractor intelligence — developer-friendly | 🟡 API Key | ✅ | ✅⭐ |
| [Autodesk BIM 360](https://aps.autodesk.com/en/docs/bim360/v1/overview/) | Cloud construction — model coordination, field management | 🔴 OAuth | ✅ | ✅ |
| [Construction Monitor](https://www.constructionmonitor.com/data) | Permit data search — Elasticsearch-based, large-scale | 🟡 API Key | ✅ | ✅ |
| [ATTOM Building Permits](https://www.attomdata.com/data/property-data/nationwide-building-permit-data/) | 300M+ permits from 2K+ departments, 158M+ properties | 🟡 API Key | ✅ | ✅ |
| [PlanGrid / Autodesk](https://developer.plangrid.com/docs) | Construction blueprints, documents, field reports | 🔴 OAuth | ✅ | ✅ |
| [buildingSMART bSDD](https://technical.buildingsmart.org/services/bsdd/using-the-bsdd-api/) | IFC classifications, properties, materials — OpenAPI | 🔴 OAuth | ✅ | ✅ |
| [Trimble Connect](https://www.trimble.com/en/developer/docs) | Collaborative BIM — 3D models, project data, documents | 🔴 OAuth | ✅ | ✅ |

---

## 🚢 Maritime & Vessel Tracking APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [MarineTraffic API](https://servicedocs.marinetraffic.com/) | 13K+ AIS receivers — vessel positions, voyages, port calls | 🟡 API Key | ✅ | ✅⭐ |
| [Searoutes API](https://developer.searoutes.com/) | Sea routing, distances, SECA zones, canal exclusions | 🟡 API Key | ✅ | ✅⭐ |
| [Datalastic API](https://datalastic.com/api-reference/) | Vessel tracking, port info, MMSI/IMO lookup — trial available | 🟡 API Key | ✅ | ✅ |
| [SeaRates API](https://docs.searates.com/) | Ship distance, container tracking, freight rates, schedules | 🟡 API Key | ✅ | ✅ |
| [Portcast API](https://www.portcast.io/ocean-vessel-tracking-api) | ETA predictions, port congestion — 6-8 week forecasts | 🟡 API Key | ✅ | ✅ |
| [AISHub API](https://www.aishub.net/api) | Free AIS data exchange — community-driven, JSON/XML/CSV | 🟡 API Key | ✅ | ✅ |
| [NavAPI AIS](https://navapi.com/ais-positions-api/) | Global vessel tracking — 6 years of historical AIS data | 🟡 API Key | ✅ | ✅ |
| [MyShipTracking](https://api.myshiptracking.com/) | Vessel tracking services with AIS data | 🟡 API Key | ✅ | ⚠️ |

---

## 🏥 Clinical & FHIR Health APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [HAPI FHIR](https://hapifhir.io/) | Open-source FHIR server — R4/R5, full REST interface, self-hostable | 🟢 No | ✅ | ✅⭐ |
| [CMS Blue Button 2.0](https://bluebutton.cms.gov/developers/) | Medicare claims data for 53M+ beneficiaries via FHIR R4 | 🔴 OAuth | ✅ | ✅⭐ |
| [Google Cloud Healthcare (FHIR)](https://cloud.google.com/healthcare-api/docs/concepts/fhir) | Managed FHIR R4 data store — full CRUD and search | 🔴 OAuth | ✅ | ✅⭐ |
| [Azure Health Data Services](https://learn.microsoft.com/en-us/azure/healthcare-apis/) | Microsoft managed FHIR server — SMART on FHIR | 🔴 OAuth | ✅ | ✅⭐ |
| [Epic on FHIR](https://fhir.epic.com/) | Patient, clinical, and scheduling data from Epic EHR — open sandbox | 🔴 OAuth | ✅ | ✅ |
| [Oracle Health (Cerner) FHIR](https://fhir.cerner.com/) | FHIR R4 for patient/encounter data on Cerner Millennium | 🔴 OAuth | ✅ | ✅ |
| [VA Clinical Health API](https://developer.va.gov/) | Veterans Affairs clinical data — conditions, meds, allergies | 🔴 OAuth | ✅ | ✅ |

---

## 🤖 RPA & Automation Platform APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [UiPath Orchestrator](https://docs.uipath.com/orchestrator/reference) | Manage robots, jobs, queues, assets — OData v4 REST | 🟡 API Key | ✅ | ✅⭐ |
| [Zapier Platform API](https://platform.zapier.com/) | Trigger Zaps, manage connections to 8,000+ apps | 🔴 OAuth | ✅ | ✅⭐ |
| [Make.com API](https://www.make.com/en/api-documentation) | Create/execute automation scenarios — 1,500+ app connectors | 🟡 API Key | ✅ | ✅⭐ |
| [Automation Anywhere](https://docs.automationanywhere.com/) | Trigger bots, manage workload, retrieve execution results | 🟡 API Key | ✅ | ✅ |
| [Power Automate API](https://learn.microsoft.com/en-us/power-automate/) | Create/trigger/manage Power Automate flows via MS Graph | 🔴 OAuth | ✅ | ✅ |
| [Workato API](https://docs.workato.com/workato-api.html) | Enterprise iPaaS — recipe-based automation, embedded integrations | 🔴 OAuth | ✅ | ✅ |
| [Tray.io](https://tray.io/documentation) | Connect to any REST API within low-code automation workflows | 🔴 OAuth | ✅ | ✅ |

---

## 📊 Data Visualization & Charting APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [QuickChart](https://quickchart.io/) | Chart.js images via URL/POST — returns PNG/SVG, free | 🟢 No | ✅ | ✅⭐ |
| [Vega / Vega-Lite](https://vega.github.io/vega-lite/) | Declarative JSON grammar for interactive statistical visualizations | 🟢 No | ✅ | ✅⭐ |
| [Image-Charts](https://www.image-charts.com/) | URL-based chart generation — drop-in Google Image Charts replacement | 🟢 No | ✅ | ✅⭐ |
| [Datawrapper API](https://developer.datawrapper.de/) | Publication-quality charts, maps, tables — auto-embeddable | 🟡 API Key | ✅ | ✅⭐ |
| [Plotly Chart Studio](https://chart-studio.plotly.com/) | Interactive Plotly charts via REST — Python/JS SDKs | 🟡 API Key | ✅ | ✅ |
| [ChartMogul API](https://dev.chartmogul.com/) | SaaS subscription analytics — MRR, churn, LTV charting | 🟡 API Key | ✅ | ✅ |
| [Google Charts](https://developers.google.com/chart) | Server/client-side charts — dozens of chart types | 🟢 No | ✅ | ⚠️ |
| [Knowi REST API](https://www.knowi.com/) | Query JSON/REST with SQL-like syntax — 40+ viz types | 🟡 API Key | ✅ | ✅ |

---

## 🔍 Background Check & Screening APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Checkr API](https://docs.checkr.com/) | Criminal, MVR, drug, employment screening — modern REST | 🟡 API Key | ✅ | ✅⭐ |
| [Certn API](https://docs.certn.co/) | Global background checks — criminal, education, identity — sandbox | 🟡 API Key | ✅ | ✅⭐ |
| [GoodHire API](https://www.goodhire.com/) | Streamlined background checks with real-time results | 🟡 API Key | ✅ | ✅ |
| [PESCHECK API](https://www.pescheck.io/) | Cloud screening — instant API access, auto-scaling | 🟡 API Key | ✅ | ✅ |
| [Sterling API](https://developer.sterlingcheck.com/) | Enterprise screening — criminal, drug, education verifications | 🔴 OAuth | ✅ | ⚠️ |
| [First Advantage](https://fadv.com/) | Global screening — real-time order submission and notifications | 🟡 API Key | ✅ | ⚠️ |

---

## 📡 Media Monitoring & Brand Intelligence APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Mention API](https://mention.com/) | Real-time monitoring across social, web, blogs, forums, news | 🟡 API Key | ✅ | ✅⭐ |
| [Talkwalker API](https://www.talkwalker.com/) | 150M+ sources — sentiment, trending topics, mentions | 🟡 API Key | ✅ | ✅⭐ |
| [NewsWhip API](https://www.newswhip.com/) | Real-time engagement data for hundreds of millions of stories | 🟡 API Key | ✅ | ✅⭐ |
| [Awario API](https://awario.com/) | Social listening and brand monitoring — affordable | 🟡 API Key | ✅ | ✅ |
| [Brandwatch API](https://www.brandwatch.com/) | Consumer intelligence — social listening, sentiment analysis | 🔴 OAuth | ✅ | ✅ |
| [Meltwater API](https://www.meltwater.com/) | Media intelligence — social, news, broadcast, print | 🔴 OAuth | ✅ | ✅ |
| [Sprinklr API](https://www.sprinklr.com/) | Unified CXM — social listening, AI analytics, omnichannel | 🔴 OAuth | ✅ | ✅ |

---

## 🎧 Helpdesk & Customer Support APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Zendesk API](https://developer.zendesk.com/) | Ticketing, help center, chat, voice, CRM — full REST | 🟡 API Key | ✅ | ✅⭐ |
| [Freshdesk API](https://developers.freshdesk.com/) | Tickets, contacts, agents, knowledge base CRUD | 🟡 API Key | ✅ | ✅⭐ |
| [Intercom API](https://developers.intercom.com/) | Customer messaging — conversations, contacts, articles | 🟡 API Key | ✅ | ✅⭐ |
| [Help Scout API](https://developer.helpscout.com/) | Conversations, customers, mailboxes — clean REST design | 🔴 OAuth | ✅ | ✅⭐ |
| [Freshservice API](https://api.freshservice.com/) | IT service desk — assets, changes, incidents — ITIL-aligned | 🟡 API Key | ✅ | ✅ |
| [Zoho Desk API](https://desk.zoho.com/DeskAPIDocument) | Tickets, contacts, accounts, knowledge base | 🔴 OAuth | ✅ | ✅ |
| [Kayako API](https://developer.kayako.com/) | 100+ REST APIs — tickets, conversations, customer data | 🟡 API Key | ✅ | ✅ |
| [HelpDesk.com API](https://api.helpdesk.com/) | Ticket management, team operations, reporting | 🟡 API Key | ✅ | ✅ |
| [LiveAgent API](https://www.liveagent.com/) | Conversations, tickets, agents, SLA — 180 req/min | 🟡 API Key | ✅ | ⚠️ |

---

## 🎁 Loyalty & Rewards Program APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Open Loyalty](https://www.openloyalty.io/) | API-first loyalty engine — gamification, tiers, rewards | 🟡 API Key | ✅ | ✅⭐ |
| [Talon.One API](https://docs.talon.one/) | Promotions + loyalty — coupons, referrals, discounts | 🟡 API Key | ✅ | ✅⭐ |
| [Voucherify API](https://docs.voucherify.io/) | API-first promotions — coupons, loyalty, referrals, gift cards | 🟡 API Key | ✅ | ✅⭐ |
| [Square Loyalty API](https://developer.squareup.com/docs/loyalty-api/overview) | Points, rewards for Square merchants | 🔴 OAuth | ✅ | ✅ |
| [Antavo API](https://antavo.com/) | SaaS loyalty — points, tiers, gamification | 🟡 API Key | ✅ | ✅ |
| [Yotpo Loyalty](https://www.yotpo.com/) | eCommerce loyalty + referrals — points earning/redemption | 🟡 API Key | ✅ | ✅ |
| [Loyverse API](https://developer.loyverse.com/) | POS-integrated loyalty — customers, transactions | 🔴 OAuth | ✅ | ✅ |
| [Smile.io API](https://docs.smile.io/) | eCommerce loyalty + referral programs — Shopify focus | 🟡 API Key | ✅ | ⚠️ |

---

## 🏭 Warehouse Management APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [ShipBob API](https://developer.shipbob.com/) | Order fulfillment, inventory, warehouse ops — eCommerce | 🟡 API Key | ✅ | ✅⭐ |
| [Logiwa WMS API](https://www.logiwa.com/) | Cloud fulfillment WMS — REST, webhooks, EDI | 🟡 API Key | ✅ | ✅⭐ |
| [Extensiv (3PL Central)](https://www.extensiv.com/) | 3PL warehouse — inventory, orders, receiving | 🟡 API Key | ✅ | ✅ |
| [Oracle WMS Cloud](https://docs.oracle.com/en/cloud/saas/warehouse-management/) | Enterprise warehouse — inbound, outbound, waves | 🔴 OAuth | ✅ | ✅ |
| [DHL Supply Chain WMS](https://developer.dhl.com/) | Warehouse ops for DHL Supply Chain customers | 🔴 OAuth | ✅ | ✅ |
| [SphereWMS API](https://www.spherewms.com/) | WMS integration — JS, Python, PHP, Ruby, Java | 🟡 API Key | ✅ | ⚠️ |
| [Ongoing WMS](https://www.ongoingwarehouse.com/) | SOAP + REST for inventory and order operations | 🟡 API Key | ✅ | ⚠️ |

---

## 🖼️ Digital Asset Management APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Cloudinary API](https://cloudinary.com/documentation) | API-first media management — upload, transform, deliver, free tier | 🟡 API Key | ✅ | ✅⭐ |
| [Adobe AEM Assets API](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/assets/admin/mac-api-assets.html) | Digital asset CRUD — metadata, renditions, comments | 🔴 OAuth | ✅ | ✅ |
| [Bynder API](https://developer.bynder.com/) | Brand asset management — search, download, metadata | 🔴 OAuth | ✅ | ✅ |
| [Acquia DAM API](https://docs.acquia.com/) | Open-source SDK — TypeScript support for DAM operations | 🔴 OAuth | ✅ | ✅ |
| [Brandfolder](https://developer.brandfolder.com/) | Digital asset storage, organization, sharing — REST | 🟡 API Key | ✅ | ⚠️ |
| [Widen Collective](https://widencollective.com/) | Enterprise DAM + PIM — search, download, metadata | 🟡 API Key | ✅ | ⚠️ |
| [Canto API](https://www.canto.com/) | Asset upload, search, metadata, sharing | 🟡 API Key | ✅ | ⚠️ |

---

## 📝 Contract Management (CLM) APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [PandaDoc API](https://developers.pandadoc.com/) | Document automation, e-signatures — sandbox + production | 🟡 API Key | ✅ | ✅⭐ |
| [Ironclad API](https://developer.ironcladapp.com/) | Modern CLM — workflow automation, templates, webhooks | 🟡 API Key | ✅ | ✅⭐ |
| [Juro API](https://juro.com/) | Browser-native contract automation — real-time collaboration | 🟡 API Key | ✅ | ✅ |
| [Agiloft API](https://www.agiloft.com/) | Flexible CLM — fully extensible REST/WS, custom objects | 🟡 API Key | ✅ | ✅ |
| [Concord API](https://www.concordnow.com/) | Full contract management — create, negotiate, sign, store | 🟡 API Key | ✅ | ✅ |
| [DocuSign CLM](https://www.docusign.com/products/clm) | Enterprise CLM — templates, workflow, e-signature | 🔴 OAuth | ✅ | ✅ |
| [Icertis ICI](https://www.icertis.com/) | Enterprise CLM — 200+ APIs for contract intelligence | 🔴 OAuth | ✅ | ⚠️ |

---

## 📈 Competitive Intelligence & Pricing APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Prisync API](https://prisync.com/) | Competitor price tracking + dynamic pricing for eCommerce | 🟡 API Key | ✅ | ✅⭐ |
| [Contify API](https://contify.com/) | Market/competitive intelligence — curated news, company tracking | 🟡 API Key | ✅ | ✅⭐ |
| [Intelligence Node](https://www.intelligencenode.com/) | Competitive pricing intelligence — comprehensive retail data | 🟡 API Key | ✅ | ✅ |
| [WhoisXML API](https://whoisxmlapi.com/) | Domain, DNS, IP intelligence for competitive analysis | 🟡 API Key | ✅ | ✅ |
| [Oxylabs Web Scraper](https://oxylabs.io/) | Web scraping infrastructure — structured pricing data at scale | 🟡 API Key | ✅ | ✅ |
| [Crayon](https://www.crayon.co/) | Market intelligence — competitive moves, battlecards | 🟡 API Key | ✅ | ⚠️ |
| [Competera](https://competera.net/) | AI-driven price optimization — demand forecasting | 🟡 API Key | ✅ | ⚠️ |

---

## 🌍 ESG & Sustainability Reporting APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Sustainalytics API](https://www.sustainalytics.com/) | ESG risk ratings for 40,000+ companies — OpenAPI spec | 🟡 API Key | ✅ | ✅⭐ |
| [MSCI ESG Data API](https://developer.msci.com/) | ESG ratings, climate data, controversy scores | 🟡 API Key | ✅ | ✅⭐ |
| [FactSet ESG API](https://developer.factset.com/) | ESG data with portfolio-level analysis | 🟡 API Key | ✅ | ✅ |
| [Responsibly.tech API](https://www.responsibly.tech/) | ESG scoring engines for third-party integration | 🟡 API Key | ✅ | ✅ |
| [Refinitiv ESG API](https://developers.lseg.com/) | ESG scores, pillars, category scores — LSEG Data Platform | 🔴 OAuth | ✅ | ✅ |
| [Finnworlds ESG](https://finnworlds.com/) | ESG scores — sub-millisecond response, 99.5% uptime | 🟡 API Key | ✅ | ✅ |
| [ESG Enterprise](https://www.esgenterprise.com/) | Real-time ESG analytics — 250K+ companies, 750K suppliers | 🟡 API Key | ✅ | ✅ |
| [KEY ESG API](https://www.keyesg.com/) | ESG data — Power BI, Tableau, Snowflake, AWS integration | 🔴 OAuth | ✅ | ✅ |
| [Apiday API](https://apiday.com/) | AI-powered ESG — GHG assessments, CSRD/EU Taxonomy | 🟡 API Key | ✅ | ⚠️ |

---

## 💰 Tax Calculation & Compliance APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [TaxJar API](https://www.taxjar.com/api/) | Automated US sales tax calculation + filing — all jurisdictions | 🟡 API Key | ✅ | ✅⭐ |
| [Avalara AvaTax](https://developer.avalara.com/) | Cloud tax engine — 12,000+ jurisdictions worldwide | 🟡 API Key | ✅ | ✅⭐ |
| [Quaderno API](https://developers.quaderno.io/) | VAT, GST, sales tax at checkout — international compliance | 🟡 API Key | ✅ | ✅⭐ |
| [Ziptax](https://www.ziptax.com/) | Lightweight US sales tax rate lookup by ZIP code | 🟡 API Key | ✅ | ✅⭐ |
| [API Ninjas Income Tax](https://api-ninjas.com/api/incometax) | Income tax bracket lookups by country — marginal/effective rates | 🟡 API Key | ✅ | ✅⭐ |
| [Symmetry Payroll Tax](https://www.symmetry.com/) | Federal, state, local payroll tax calculation | 🟡 API Key | ✅ | ✅ |
| [Vertex O Series](https://www.vertexinc.com/) | Enterprise tax calculation, area lookups, compliance | 🔴 OAuth | ✅ | ✅ |
| [Sovos](https://sovos.com/) | Indirect tax — e-invoicing, tax determination, reporting | 🔴 OAuth | ✅ | ✅ |

---

## 🚨 Public Safety & Emergency APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [USGS Earthquake API](https://earthquake.usgs.gov/fdsnws/event/1/) | Real-time earthquake data — magnitude, epicenter, depth | 🟢 No | ✅ | ✅⭐ |
| [NWS Alerts API](https://www.weather.gov/documentation/services-web-api) | Weather watches/warnings/advisories — CAP v1.2 data | 🟢 No | ✅ | ✅⭐ |
| [FEMA IPAWS-OPEN](https://www.fema.gov/emergency-managers/practitioners/integrated-public-alert-warning-system) | Federal emergency public alerts — Common Alerting Protocol | 🟢 No | ✅ | ✅⭐ |
| [AirNow API](https://docs.airnowapi.org/) | Air Quality Index — current/forecast from EPA | 🟡 API Key | ✅ | ✅⭐ |
| [OpenFEMA API](https://www.fema.gov/about/openfema/api) | Disaster declarations, grants, National Flood Insurance | 🟡 API Key | ✅ | ✅ |
| [Amber Alert API](https://www.missingkids.org/) | Active missing children alerts from NCMEC | 🟡 API Key | ✅ | ✅ |
| [RapidSOS](https://rapidsos.com/) | Connects apps to 911 PSAPs — device location + sensors | 🔴 OAuth | ✅ | ⚠️ |
| [Noonlight](https://www.noonlight.com/) | Emergency response dispatch — police, fire, EMS | 🟡 API Key | ✅ | ⚠️ |

---

## 🎙️ Podcast Platform APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Podcast Index API](https://podcastindex.org/) | Open community-driven podcast search + directory — free | 🟡 API Key | ✅ | ✅⭐ |
| [Buzzsprout API](https://www.buzzsprout.com/api) | Podcast hosting — shows, episodes, download analytics | 🟡 API Key | ✅ | ✅⭐ |
| [Transistor API](https://developers.transistor.fm/) | JSON:API — multiple podcasts, episodes, subscribers, analytics | 🟡 API Key | ✅ | ✅⭐ |
| [Simplecast API](https://api.simplecast.com/) | Shows, episodes, listener analytics — Postman collection | 🟡 API Key | ✅ | ✅ |
| [Spotify Web API (Podcasts)](https://developer.spotify.com/documentation/web-api/) | Podcast/show metadata, episodes, playback, user library | 🔴 OAuth | ✅ | ✅ |
| [Spreaker API](https://developers.spreaker.com/) | Shows, episodes, listener demographics | 🔴 OAuth | ✅ | ✅ |
| [Podbean API](https://developers.podbean.com/) | Publish episodes, manage settings, analytics | 🔴 OAuth | ✅ | ✅ |
| [Blubrry API](https://create.blubrry.com/resources/podcast-media-download-statistics/podcast-statistics-api/) | Publishing, managing, listener statistics | 🟡 API Key | ✅ | ✅ |

---

## 📖 Language Learning & Dictionary APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Free Dictionary API](https://dictionaryapi.dev/) | Definitions, phonetics, audio, examples — completely free | 🟢 No | ✅ | ✅⭐ |
| [Datamuse API](https://www.datamuse.com/api/) | Word-finding — rhymes, semantics, spelling, autocomplete | 🟢 No | ✅ | ✅⭐ |
| [WordsAPI](https://www.wordsapi.com/) | 150K+ words — definitions, synonyms, antonyms, frequency | 🟡 API Key | ✅ | ✅⭐ |
| [Wordnik API](https://developer.wordnik.com/) | Multiple dictionaries, examples, pronunciations, word-of-day | 🟡 API Key | ✅ | ✅⭐ |
| [Merriam-Webster API](https://dictionaryapi.com/) | Official dictionary/thesaurus — definitions, etymologies, audio | 🟡 API Key | ✅ | ✅ |
| [ELSA Speech API](https://elsaspeak.com/) | AI pronunciation assessment — multi-language speech recognition | 🟡 API Key | ✅ | ✅ |

---

## 💝 Nonprofit & Donation APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Every.org API](https://www.every.org/docs/api) | 1M+ US nonprofits — search, metadata, donate links — free | 🟡 API Key | ✅ | ✅⭐ |
| [GlobalGiving API](https://www.globalgiving.org/api/) | 6,000+ vetted projects in 175+ countries — process donations | 🟡 API Key | ✅ | ✅⭐ |
| [Pledge API](https://pledge.to/) | Charity search, donation forms, widgets, webhooks | 🟡 API Key | ✅ | ✅⭐ |
| [CharityAPI.org](https://charityapi.org/) | IRS data on 1.7M+ US nonprofits — search by EIN/name | 🟡 API Key | ✅ | ✅ |
| [OrgHunter API](https://www.orghunter.com/) | 2.5M+ nonprofits — NTEE classification, geolocation, financials | 🟡 API Key | ✅ | ✅ |
| [FrontStream Donations](https://www.frontstream.com/) | Process + disburse donation to any registered charity — single call | 🟡 API Key | ✅ | ✅ |
| [Benevity API](https://benevity.com/) | Enterprise giving — employer matching, CSR programs | 🟡 API Key | ✅ | ⚠️ |

---

## 🌐 Domain & DNS Management APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Cloudflare API](https://developers.cloudflare.com/) | DNS, domain registration, CDN, security — comprehensive REST | 🟡 API Key | ✅ | ✅⭐ |
| [DNSimple API](https://developer.dnsimple.com/) | Domain registration, DNS hosting, SSL certs — developer-friendly | 🟡 API Key | ✅ | ✅⭐ |
| [GoDaddy API](https://developer.godaddy.com/) | Domain search, registration, DNS management, WHOIS | 🟡 API Key | ✅ | ✅⭐ |
| [name.com API](https://www.name.com/api-docs) | Domain management + DNS — MCP Server support for AI agents | 🟡 API Key | ✅ | ✅⭐ |
| [WhoisXML API](https://whoisxmlapi.com/) | WHOIS, DNS records, IP geolocation, reverse DNS, threats | 🟡 API Key | ✅ | ✅ |
| [Namecheap API](https://www.namecheap.com/support/api/) | Domains, SSL, DNS management — XML-based | 🟡 API Key | ✅ | ✅ |
| [NameSilo API](https://www.namesilo.com/api-reference) | Low-cost domain management + DNS settings control | 🟡 API Key | ✅ | ✅ |
| [Dynadot API](https://www.dynadot.com/community/api) | Register, transfer, DNS records, parking, forwarding | 🟡 API Key | ✅ | ✅ |
| [Scaleway DNS](https://developers.scaleway.com/) | Domain + DNS management with DNSSEC — European cloud | 🟡 API Key | ✅ | ✅ |

---

## 📋 Survey & Form Builder APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Jotform API](https://api.jotform.com/docs/) | Forms, submissions, 150+ widgets, reports — REST | 🟡 API Key | ✅ | ✅⭐ |
| [SurveyJS](https://surveyjs.io/) | Self-hosted JSON-schema form builder — no vendor lock-in | 🟡 API Key | ✅ | ✅⭐ |
| [Typeform API](https://www.typeform.com/developers/) | Conversational forms/surveys — create, manage, responses | 🔴 OAuth | ✅ | ✅ |
| [SurveyMonkey API](https://developer.surveymonkey.com/) | Surveys — 200+ integrations, AI-powered survey design | 🔴 OAuth | ✅ | ✅ |
| [Google Forms API](https://developers.google.com/forms/api/reference/rest) | Create/manage Google Forms and collected responses | 🔴 OAuth | ✅ | ✅ |
| [QuestionPro API](https://www.questionpro.com/) | Create surveys, distribute, collect, integrate analytics | 🟡 API Key | ✅ | ✅ |
| [Helpfull API](https://www.helpfull.com/) | A/B testing surveys, polls, quick feedback | 🟡 API Key | ✅ | ✅ |

---

## 📸 Screenshot & Website Preview APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [ScreenshotOne](https://screenshotone.com/) | Screenshot API — auto-removes ads, cookie banners, clutter | 🟡 API Key | ✅ | ✅⭐ |
| [ApiFlash](https://apiflash.com/) | AWS Lambda + Chrome — sub-second screenshots | 🟡 API Key | ✅ | ✅⭐ |
| [Urlbox](https://urlbox.io/) | Retina, full-page, dark mode rendering, PDF export | 🟡 API Key | ✅ | ✅⭐ |
| [ScreenshotAPI.net](https://www.screenshotapi.net/) | Full-page HD screenshots — auto ad/tracker removal | 🟡 API Key | ✅ | ✅ |
| [CaptureKit](https://capturekit.com/) | Website to image — viewport, device, format options | 🟡 API Key | ✅ | ✅ |
| [Thum.io](https://www.thum.io/) | Real-time streaming website screenshots | 🟡 API Key | ✅ | ✅ |
| [ScrapFly Screenshot](https://scrapfly.io/) | Anti-bot bypass, proxy rotation, JS rendering | 🟡 API Key | ✅ | ✅ |

---

## 📱 QR Code & Barcode Generation APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [goQR.me](https://goqr.me/api/) | Free QR code generation/decoding — simple GET, no auth | 🟢 No | ✅ | ✅⭐ |
| [QuickChart QR](https://quickchart.io/qr) | Free open-source QR rendering — self-hostable | 🟢 No | ✅ | ✅⭐ |
| [QuickChart Barcode](https://quickchart.io/barcode) | Code 128, EAN-13, UPC-A, ITF-14 — simple URL params | 🟢 No | ✅ | ✅⭐ |
| [Orca Scan Barcode](https://orcascan.com/) | QR, Code 128, EAN, Data Matrix — SVG/PNG/JPG/PDF, free | 🟢 No | ✅ | ✅⭐ |
| [QRCode Monkey](https://www.qrcode-monkey.com/) | Custom QR — logo embedding, colors, high-res output | 🟢 No | ✅ | ✅⭐ |
| [QRickit](https://qrickit.com/) | Custom QR codes — multiple formats, error correction | 🟢 No | ✅ | ✅ |
| [QRCoder API](https://qrcoder.com/) | Free QR generation — 100 req/day, configurable | 🟢 No | ✅ | ✅ |
| [Dub QR Code](https://dub.co/) | Bulk QR at scale — click tracking + analytics | 🟡 API Key | ✅ | ✅ |

---

## 📅 Meeting Scheduling & Booking APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Cal.com API](https://cal.com/docs/api-reference) | Open-source scheduling — free tier includes API access | 🟡 API Key | ✅ | ✅⭐ |
| [Calendly API](https://developer.calendly.com/) | Scheduling — booking creation, availability, multi-calendar | 🔴 OAuth | ✅ | ✅⭐ |
| [Cronofy API](https://docs.cronofy.com/) | Unified calendar — Google/MS/Apple sync — 99.99% uptime | 🔴 OAuth | ✅ | ✅⭐ |
| [Nylas Calendar API](https://www.nylas.com/) | Unified calendar across all major providers — one integration | 🟡 API Key | ✅ | ✅⭐ |
| [Acuity Scheduling](https://developers.squareup.com/docs/appointments-api) | Appointments — bookings, availability, clients, payments | 🔴 OAuth | ✅ | ✅ |
| [OnSched API](https://onsched.com/) | Google/Outlook sync — JavaScript client library | 🟡 API Key | ✅ | ✅ |
| [Timekit](https://www.timekit.io/) | Headless booking — embeddable widgets, webhooks | 🟡 API Key | ✅ | ✅ |
| [DaySchedule API](https://dayschedule.com/) | 1:1, round-robin, group booking — auto timezone | 🟡 API Key | ✅ | ✅ |
| [SuperSaaS API](https://www.supersaas.com/) | Appointments, calendars, users, payments, notifications | 🟡 API Key | ✅ | ✅ |

---

## 💬 Live Chat & Messaging APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Chatwoot](https://www.chatwoot.com/docs/product/channels/api/overview) | Open-source support platform — REST API, self-hostable | 🟡 API Key | ✅ | ✅⭐ |
| [Sendbird](https://sendbird.com/docs) | Scalable in-app messaging — chat, push, moderation | 🟡 API Key | ✅ | ✅⭐ |
| [LiveChat API](https://developers.livechat.com/) | Full chat platform — routing, real-time webhooks | 🟡 API Key | ✅ | ✅⭐ |
| [TalkJS](https://talkjs.com/) | Cross-platform messaging SDK — pre-built UI components | 🟡 API Key | ✅ | ✅ |
| [CometChat](https://www.cometchat.com/) | Pre-built UI kits for 1:1 and group messaging | 🟡 API Key | ✅ | ✅ |
| [Tawk.to API](https://developer.tawk.to/) | Free live chat — JS client + REST server API | 🟡 API Key | ✅ | ✅ |
| [Rocket.Chat Livechat](https://developer.rocket.chat/) | Open-source — omnichannel, chatbot, E2E encryption | 🟡 API Key | ✅ | ✅ |
| [Zendesk Chat API](https://developer.zendesk.com/api-reference/live-chat/) | Chat widget — agent availability, visitor tracking | 🔴 OAuth | ✅ | ✅ |

---

## 📦 Product Information Management (PIM) APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Akeneo PIM](https://api.akeneo.com/) | Open-source PIM — products, categories, attributes, families | 🔴 OAuth | ✅ | ✅⭐ |
| [Pimcore API](https://pimcore.com/) | API-first open-source PIM — ETL, data matching, microservices | 🟡 API Key | ✅ | ✅⭐ |
| [Salsify API](https://www.salsify.com/) | Product experience management — content, assets, syndication | 🟡 API Key | ✅ | ✅ |
| [Crystallize](https://crystallize.com/) | Event-driven PIM — products, digital assets, subscriptions | 🟡 API Key | ✅ | ✅ |
| [Pimberly API](https://pimberly.com/) | API-first PIM — eCommerce, ERP, CRM bidirectional sync | 🟡 API Key | ✅ | ✅ |
| [Plytix PIM](https://plytix.com/) | SMB PIM — automated product feed management | 🟡 API Key | ✅ | ✅ |
| [Sales Layer API](https://saleslayer.com/) | Centralize, enrich, distribute product info — all channels | 🟡 API Key | ✅ | ✅ |

---

## 🚛 Fleet Management & Telematics APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Samsara API](https://developers.samsara.com/) | Real-time GPS, vehicle diagnostics, driver behavior — feed-based sync | 🟡 API Key | ✅ | ✅⭐ |
| [Geotab API](https://developers.geotab.com/) | GPS LogRecords, StatusData, FaultData — JSON-RPC | 🟡 API Key | ✅ | ✅⭐ |
| [Fleetio API](https://developer.fleetio.com/) | Fleet lifecycle — vehicles, fuel, service records, parts | 🟡 API Key | ✅ | ✅⭐ |
| [Motive API](https://developer.gomotive.com/) | ELD compliance, fleet tracking, driver monitoring, IFTA | 🟡 API Key | ✅ | ✅ |
| [High Mobility](https://www.high-mobility.com/) | Unified telematics — native in-vehicle data across OEMs | 🔴 OAuth | ✅ | ✅ |
| [Wialon (Gurtam)](https://wialon.com/) | GPS tracking for 3M+ units — geofencing, notifications | 🟡 API Key | ✅ | ✅ |
| [Verizon Connect](https://www.verizonconnect.com/) | GPS position, dispatch, fuel tax, preventative maintenance | 🟡 API Key | ✅ | ⚠️ |
| [Fleetistics](https://fleetistics.com/) | GPS data, telematics, dashcams, ELD integration | 🟡 API Key | ✅ | ⚠️ |

---

## 💳 Billing, Invoice & Subscription APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Stripe Billing](https://stripe.com/docs/billing) | Industry-standard — invoices, subscriptions, dunning, idempotent | 🟡 API Key | ✅ | ✅⭐ |
| [Chargebee API](https://apidocs.chargebee.com/) | Subscription lifecycle — billing, invoicing, multi-currency | 🟡 API Key | ✅ | ✅⭐ |
| [Recurly API](https://developers.recurly.com/) | Subscriptions + AI-optimized dunning recovery | 🟡 API Key | ✅ | ✅⭐ |
| [Space Invoices](https://spaceinvoices.com/) | Global tax-compliant invoicing — OpenAPI 3.1 spec | 🟡 API Key | ✅ | ✅⭐ |
| [Invoiced](https://invoiced.com/) | AR automation — invoice generation, payment, dunning | 🟡 API Key | ✅ | ✅ |
| [Paddle](https://developer.paddle.com/) | Merchant-of-Record — handles tax + compliance globally | 🟡 API Key | ✅ | ✅ |
| [Maxio (Chargify)](https://maxio.com/) | Complex B2B SaaS — component pricing, metered usage | 🟡 API Key | ✅ | ✅ |
| [Zoho Billing](https://www.zoho.com/billing/) | Invoicing, subscriptions, hosted payment pages | 🔴 OAuth | ✅ | ✅ |

---

## ✍️ eSignature & Signature Verification APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [DocuSeal](https://www.docuseal.co/) | Open-source document signing — self-hostable, REST API | 🟡 API Key | ✅ | ✅⭐ |
| [BoldSign](https://www.boldsign.com/) | Lightweight eSignature — SOC 2, HIPAA, GDPR compliant | 🟡 API Key | ✅ | ✅⭐ |
| [Dropbox Sign](https://www.hellosign.com/) | Developer-friendly eSignature — template-based workflows | 🟡 API Key | ✅ | ✅⭐ |
| [Arya.ai Signature](https://www.arya.ai/) | AI signature verification — confidence scores for authenticity | 🟡 API Key | ✅ | ✅ |
| [SignNow](https://www.signnow.com/) | eSignature — 256-bit encryption, audit trails, 2FA | 🔴 OAuth | ✅ | ✅ |
| [signotec Biometric](https://www.signotec.com/) | Neural-network signature comparison — 2D and 4D biometric | 🟡 API Key | ✅ | ⚠️ |

---

## 🥗 Nutrition & Food Data APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Open Food Facts](https://world.openfoodfacts.org/data) | Open-source food database — barcode lookup, Nutri-Score, free | 🟢 No | ✅ | ✅⭐ |
| [USDA FoodData Central](https://fdc.nal.usda.gov/api-guide.html) | 200K+ foods, 150+ nutrients — free government database | 🟡 API Key | ✅ | ✅⭐ |
| [Nutritionix](https://www.nutritionix.com/business/api) | Natural language nutrition — "1 apple and 2 tbsp peanut butter" | 🟡 API Key | ✅ | ✅⭐ |
| [Spoonacular](https://spoonacular.com/food-api) | 365K+ recipes — nutrition, cost, meal planning, grocery lists | 🟡 API Key | ✅ | ✅⭐ |
| [CalorieNinjas](https://calorieninjas.com/) | Simple nutrition facts — 100K+ foods, 10K free calls/month | 🟡 API Key | ✅ | ✅⭐ |
| [Edamam API](https://developer.edamam.com/) | 28 nutrients per food — diet/allergy/health labels | 🟡 API Key | ✅ | ✅ |
| [Spike Nutrition](https://spikeapi.com/) | AI food image recognition — photo to calorie breakdown | 🟡 API Key | ✅ | ✅ |
| [FatSecret](https://platform.fatsecret.com/) | 1.9M+ foods in 56 countries — barcode lookup | 🔴 OAuth | ✅ | ⚠️ |

---

## 😊 Sentiment Analysis & Emotion Detection APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Google Cloud Natural Language](https://cloud.google.com/natural-language/docs) | Sentiment score + magnitude — entity-level, multi-language | 🟡 API Key | ✅ | ✅⭐ |
| [IBM Watson NLU](https://www.ibm.com/products/natural-language-understanding) | 5 emotions (joy/sadness/anger/fear/disgust) — entity extraction | 🟡 API Key | ✅ | ✅⭐ |
| [MeaningCloud](https://www.meaningcloud.com/) | Multilingual sentiment — aspect polarity, irony detection | 🟡 API Key | ✅ | ✅⭐ |
| [NLPCloud](https://nlpcloud.com/) | LLM-powered sentiment + emotion — privacy-by-design | 🟡 API Key | ✅ | ✅ |
| [Twinword Emotion](https://www.twinword.com/) | 6 emotions with per-emotion scores — pay-as-you-go | 🟡 API Key | ✅ | ✅ |
| [Moderation API](https://moderationapi.com/) | Sentiment + toxicity + content moderation — single call | 🟡 API Key | ✅ | ✅ |
| [Komprehend](https://komprehend.io/) | LSTM-based sentiment + 6 emotions — 1B+ docs trained | 🟡 API Key | ✅ | ⚠️ |

---

## 📄 Resume Parsing & Talent APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Affinda](https://www.affinda.com/) | 250M+ docs — 100+ fields from CVs, ~95% accuracy | 🟡 API Key | ✅ | ✅⭐ |
| [Eden AI Resume Parser](https://www.edenai.co/) | Unified API — switch between Affinda/HireAbility/Klippa | 🟡 API Key | ✅ | ✅⭐ |
| [RChilli](https://www.rchilli.com/) | AI resume parsing — job matching, 56+ languages | 🟡 API Key | ✅ | ✅ |
| [Textkernel (Sovren)](https://www.textkernel.com/) | Enterprise parsing + semantic matching engine | 🟡 API Key | ✅ | ✅ |
| [HireAbility](https://www.hireability.com/) | Resume parsing — zero data retention, privacy-first | 🟡 API Key | ✅ | ✅ |
| [Skima AI](https://skima.ai/) | 200+ data points — 99% accuracy, 130+ integrations | 🟡 API Key | ✅ | ✅ |

---

## 🔔 Push Notification APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [ntfy](https://ntfy.sh/) | Open-source pub-sub notifications — zero auth for public topics | 🟢 No | ✅ | ✅⭐ |
| [Pushover](https://pushover.net/) | Dead-simple push — one POST, iOS/Android/desktop | 🟡 API Key | ✅ | ✅⭐ |
| [OneSignal](https://documentation.onesignal.com/) | Cross-platform push — segmentation, A/B testing, automation | 🟡 API Key | ✅ | ✅⭐ |
| [Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging) | Google's free push — unlimited messages, topics, device groups | 🟡 API Key | ✅ | ✅ |
| [Pusher Beams](https://pusher.com/beams) | Hosted push — transactional notifications, cross-platform | 🟡 API Key | ✅ | ✅ |
| [PushEngage](https://www.pushengage.com/) | AI-powered web/mobile push — scheduling, targeting | 🟡 API Key | ✅ | ✅ |
| [Pushbullet](https://docs.pushbullet.com/) | Push notifications, links, files between devices | 🟡 API Key | ✅ | ⚠️ |

---

## 🛡️ Content Moderation & NSFW Detection APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Sightengine](https://sightengine.com/) | Real-time image/video/text moderation — nudity, violence, drugs | 🟡 API Key | ✅ | ✅⭐ |
| [Clarifai](https://www.clarifai.com/) | Pre-built models — NSFW, violence, hate symbols, custom training | 🟡 API Key | ✅ | ✅⭐ |
| [Google Vision SafeSearch](https://cloud.google.com/vision/docs/detecting-safe-search) | Adult/violence/racy content — likelihood scores per category | 🟡 API Key | ✅ | ✅⭐ |
| [Amazon Rekognition](https://aws.amazon.com/rekognition/) | Content moderation — deep AWS S3 integration | 🟡 API Key | ✅ | ✅ |
| [API4AI NSFW](https://api4.ai/) | NSFW image classification — customizable sensitivity | 🟡 API Key | ✅ | ✅ |
| [Moderation API](https://moderationapi.com/) | Text + image moderation + PII detection — single endpoint | 🟡 API Key | ✅ | ✅ |
| [Imagga NSFW](https://imagga.com/) | NSFW categorization + image tagging, color analysis | 🟡 API Key | ✅ | ⚠️ |

---

## 📍 Geofencing & Location-Based APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Radar](https://radar.com/) | Industry-leading geofencing — entries/exits/dwells, free tier | 🟡 API Key | ✅ | ✅⭐ |
| [TomTom Geofencing](https://developer.tomtom.com/) | Virtual barriers — alert on enter/exit/approach zones | 🟡 API Key | ✅ | ✅⭐ |
| [Mapbox Geofencing](https://www.mapbox.com/) | Polygon/circular boundaries — iOS/Android SDKs | 🟡 API Key | ✅ | ✅ |
| [NextBillion.ai](https://nextbillion.ai/) | Circle/polygon/isochrone geofences — bulk creation | 🟡 API Key | ✅ | ✅ |
| [Bluedot](https://bluedot.io/) | Drive-thru, curbside pickup, location marketing | 🟡 API Key | ✅ | ✅ |
| [Azure Maps Spatial](https://learn.microsoft.com/en-us/azure/azure-maps/) | Point-in-polygon, closest-point — enterprise Azure | 🟡 API Key | ✅ | ⚠️ |

---

## 🍽️ Reservation & Booking APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [SimplyBook.me API](https://simplybook.me/) | 200+ API functions — services, providers, bookings, payments | 🟡 API Key | ✅ | ✅⭐ |
| [Bookeo API](https://www.bookeo.com/) | Online scheduling — bookings, customers, availability, payments | 🟡 API Key | ✅ | ✅⭐ |
| [resOS](https://www.resos.com/) | Open-source restaurant reservations — custom integrations | 🟡 API Key | ✅ | ✅ |
| [Yelp Reservations](https://www.yelp.com/developers) | Booking + reviews/ratings — venue intelligence combined | 🟡 API Key | ✅ | ✅ |
| [SevenRooms](https://sevenrooms.com/) | Restaurant CRM + operations — guest profiles, analytics | 🟡 API Key | ✅ | ⚠️ |
| [OpenTable API](https://www.opentable.com/) | Restaurant reservations — partner approval required | 🟡 API Key | ✅ | ⚠️ |

---

## ⭐ Review & Rating Management APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Yelp Fusion API](https://docs.developer.yelp.com/) | Business search, reviews, ratings, photos — 5K calls/day free | 🟡 API Key | ✅ | ✅⭐ |
| [Yotpo UGC API](https://www.yotpo.com/) | Product reviews, Q&A, UGC for eCommerce — 5K req/min | 🟡 API Key | ✅ | ✅⭐ |
| [Tripadvisor Content API](https://www.tripadvisor.com/developers) | Millions of reviews for hotels/restaurants/attractions | 🟡 API Key | ✅ | ✅ |
| [Stamped.io API](https://stamped.io/) | Product reviews, Q&A, NPS — webhook notifications | 🟡 API Key | ✅ | ✅ |
| [Trustpilot API](https://developers.trustpilot.com/) | Business reviews — manage, reply, analyze sentiment | 🔴 OAuth | ✅ | ✅ |
| [Judge.me API](https://judge.me/) | Shopify product reviews — export, import, manage | 🟡 API Key | ✅ | ⚠️ |

---

## 📹 Video Conferencing APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Daily.co API](https://docs.daily.co/) | Embed live video — up to 1K participants, HIPAA, no OAuth | 🟡 API Key | ✅ | ✅⭐ |
| [Jitsi Meet API](https://jitsi.org/) | Open-source video conferencing — self-hostable, free | 🟢 No | ✅ | ✅⭐ |
| [Whereby API](https://whereby.com/) | Embed video rooms — no downloads/plugins, up to 200 users | 🟡 API Key | ✅ | ✅⭐ |
| [Dyte API](https://docs.dyte.io/) | Plug-and-play video SDK — AI features, recording | 🟡 API Key | ✅ | ✅⭐ |
| [Zoom Meeting API](https://developers.zoom.us/) | Full meeting lifecycle — registrants, recordings, reports | 🔴 OAuth | ✅ | ✅ |
| [Nylas Notetaker](https://www.nylas.com/) | Cross-platform meeting capture — transcripts, action items | 🟡 API Key | ✅ | ✅⭐ |
| [Webex API](https://developer.webex.com/) | Meetings, messaging, calling, devices — Cisco platform | 🔴 OAuth | ✅ | ✅ |
| [Vonage Video (OpenTok)](https://www.vonage.com/) | Secure video — up to 3K viewers, recording, archiving | 🟡 API Key | ✅ | ✅ |

---

## 📝 Document Collaboration APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Notion API](https://developers.notion.com/) | Databases, pages, blocks, comments — block-based model | 🟡 API Key | ✅ | ✅⭐ |
| [Etherpad API](https://etherpad.org/) | Open-source real-time collaborative text — self-hostable | 🟡 API Key | ✅ | ✅⭐ |
| [Liveblocks](https://liveblocks.io/) | Co-editing, cursors, comments, notifications — Y.js/CRDT | 🟡 API Key | ✅ | ✅⭐ |
| [Google Docs API](https://developers.google.com/docs/api) | Read/create/edit Docs — paragraphs, tables, images | 🔴 OAuth | ✅ | ✅ |
| [Confluence REST API](https://developer.atlassian.com/cloud/confluence/) | Pages, spaces, comments, attachments — CQL search | 🟡 API Key | ✅ | ✅ |
| [Tiptap Collaboration](https://tiptap.dev/) | Collaborative editing — REST for server-side doc manipulation | 🟡 API Key | ✅ | ✅ |

---

## 📍 Address Validation & Geocoding APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Nominatim (OSM)](https://nominatim.openstreetmap.org/) | Free open-source geocoding — no auth, OpenStreetMap data | 🟢 No | ✅ | ✅⭐ |
| [Google Address Validation](https://developers.google.com/maps/documentation/address-validation) | USPS data, corrections, standardization — industry standard | 🟡 API Key | ✅ | ✅⭐ |
| [Mapbox Geocoding](https://docs.mapbox.com/api/search/geocoding/) | 100K free req/month — building-entrance precision | 🟡 API Key | ✅ | ✅⭐ |
| [Smarty (SmartyStreets)](https://www.smarty.com/) | USPS-certified CASS/DPV — rich metadata, fast | 🟡 API Key | ✅ | ✅⭐ |
| [HERE Geocoding](https://developer.here.com/) | 250K free req/month — global coverage, multi-format input | 🟡 API Key | ✅ | ✅⭐ |
| [Radar Geocoding](https://radar.com/) | 100% US coverage — geofencing + geocoding combined | 🟡 API Key | ✅ | ✅ |
| [Loqate (GBG)](https://www.loqate.com/) | 250+ countries — confidence scores, multi-match | 🟡 API Key | ✅ | ✅ |
| [Melissa API](https://www.melissa.com/) | 240+ countries — NCOA changes, census data, enrichment | 🟡 API Key | ✅ | ✅ |

---

## 📊 Product Analytics APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [PostHog API](https://posthog.com/docs/api) | Open-source analytics — events, funnels, replays, feature flags | 🟡 API Key | ✅ | ✅⭐ |
| [Mixpanel API](https://developer.mixpanel.com/) | Event-based analytics — JQL queries, funnels, retention | 🟡 API Key | ✅ | ✅⭐ |
| [Amplitude API](https://www.docs.developers.amplitude.com/) | Behavioral analytics — batch ingestion, chart queries | 🟡 API Key | ✅ | ✅⭐ |
| [Countly API](https://support.count.ly/) | Open-source — mobile/web/desktop/IoT, self-hostable | 🟡 API Key | ✅ | ✅⭐ |
| [Heap API](https://developers.heap.io/) | Auto-capture analytics — retroactive analysis, no instrumentation | 🟡 API Key | ✅ | ✅ |
| [Pendo API](https://engageapi.pendo.io/) | Analytics + in-app guidance + feedback collection | 🟡 API Key | ✅ | ✅ |

---

## 🚩 Feature Flag & Toggle APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Statsig API](https://docs.statsig.com/) | Free unlimited flags + experimentation — modern REST | 🟡 API Key | ✅ | ✅⭐ |
| [Unleash API](https://docs.getunleash.io/) | Open-source feature flags — gradual rollout, self-hostable | 🟡 API Key | ✅ | ✅⭐ |
| [Flagsmith API](https://docs.flagsmith.com/) | Open-source — remote config, identity, multi-environment | 🟡 API Key | ✅ | ✅⭐ |
| [Flipt API](https://www.flipt.io/) | Open-source GitOps — gRPC + REST, Go-based, lightweight | 🟡 API Key | ✅ | ✅⭐ |
| [LaunchDarkly API](https://apidocs.launchdarkly.com/) | Enterprise flags — percentage rollouts, targeting, audit | 🟡 API Key | ✅ | ✅⭐ |
| [ConfigCat API](https://configcat.com/) | Cross-platform — 10 free flags, 10M free requests | 🟡 API Key | ✅ | ✅ |
| [DevCycle API](https://docs.devcycle.com/) | OpenFeature-native — unlimited flags, edge-optimized | 🟡 API Key | ✅ | ✅ |
| [PostHog Feature Flags](https://posthog.com/docs/feature-flags) | Bundled with analytics — multivariate, open source | 🟡 API Key | ✅ | ✅ |

---

## 🐛 Error Tracking & Monitoring APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Sentry API](https://docs.sentry.io/api/) | Industry standard — errors, performance, replays, 100+ integrations | 🟡 API Key | ✅ | ✅⭐ |
| [Rollbar API](https://docs.rollbar.com/) | Real-time errors — RQL query language, 25K free events/month | 🟡 API Key | ✅ | ✅⭐ |
| [GlitchTip](https://glitchtip.com/) | Open-source Sentry alternative — self-hostable, Sentry SDK compatible | 🟡 API Key | ✅ | ✅⭐ |
| [Honeybadger API](https://docs.honeybadger.io/) | Errors + uptime + cron monitoring — 5K free errors/month | 🟡 API Key | ✅ | ✅⭐ |
| [Bugsnag API](https://bugsnagapiv2.docs.apiary.io/) | Stability scoring — strong mobile support, intelligent grouping | 🟡 API Key | ✅ | ✅ |
| [Airbrake API](https://airbrake.io/) | Error tracking + performance — intelligent grouping, affordable | 🟡 API Key | ✅ | ✅ |
| [Better Stack (Logtail)](https://betterstack.com/) | Structured logging + uptime + incidents — generous free tier | 🟡 API Key | ✅ | ✅ |

---

## 🔑 Secrets Management APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Doppler API](https://docs.doppler.com/) | Developer-friendly secrets — universal sync across environments | 🟡 API Key | ✅ | ✅⭐ |
| [Infisical API](https://infisical.com/) | Open-source — versioning, rotation, K8s/Docker/Terraform | 🟡 API Key | ✅ | ✅⭐ |
| [HashiCorp Vault](https://developer.hashicorp.com/vault/api-docs) | Industry standard — dynamic secrets, PKI, encryption-as-a-service | 🟡 API Key | ✅ | ✅⭐ |
| [Akeyless API](https://docs.akeyless.io/) | SaaS vaultless — dynamic secrets, zero-trust, multi-cloud | 🟡 API Key | ✅ | ✅ |
| [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/) | AWS-native — auto-rotation for RDS/Redshift/DocumentDB | 🟡 API Key | ✅ | ✅ |
| [Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/) | Secrets, keys, certificates — HSM-backed, Azure AD RBAC | 🔴 OAuth | ✅ | ✅ |
| [Google Secret Manager](https://cloud.google.com/secret-manager/docs) | GCP-native — versioning, IAM, audit logging | 🔴 OAuth | ✅ | ✅ |

---

## 🌐 CDN & Content Delivery APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [cdnjs API](https://cdnjs.com/api) | Open-source JS/CSS library CDN — no auth, read-only | 🟢 No | ✅ | ✅⭐ |
| [Cloudflare CDN API](https://developers.cloudflare.com/) | Caching, Workers, R2, WAF — massive free tier | 🟡 API Key | ✅ | ✅⭐ |
| [Fastly API](https://developer.fastly.com/) | API-first CDN — instant purge, edge compute (Wasm) | 🟡 API Key | ✅ | ✅⭐ |
| [Bunny.net API](https://docs.bunny.net/) | Affordable CDN — edge storage, video, DNS | 🟡 API Key | ✅ | ✅⭐ |
| [KeyCDN API](https://www.keycdn.com/) | 40+ PoPs — zone management, purging, analytics | 🟡 API Key | ✅ | ✅ |
| [Amazon CloudFront](https://docs.aws.amazon.com/cloudfront/) | AWS CDN — 450+ edge locations, Lambda@Edge | 🟡 API Key | ✅ | ✅ |
| [StackPath CDN](https://stackpath.dev/) | CDN + DDoS protection + WAF — security-focused | 🟡 API Key | ✅ | ⚠️ |

---

## 🗄️ Database Migration & Schema APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [PlanetScale API](https://planetscale.com/docs) | Git-like schema branching — non-blocking DDL, full REST | 🟡 API Key | ✅ | ✅⭐ |
| [Atlas (Ariga)](https://atlasgo.io/) | Declarative schema-as-code — "Terraform for Databases" | 🟡 API Key | ✅ | ✅⭐ |
| [Bytebase API](https://www.bytebase.com/) | Database DevOps — schema review, approval, drift detection | 🟡 API Key | ✅ | ✅⭐ |
| [Hasura Migrations](https://hasura.io/docs/) | GraphQL engine — apply/revert/squash migrations via REST | 🟡 API Key | ✅ | ✅ |
| [Flyway Hub](https://www.red-gate.com/products/flyway/) | SQL migrations — 20+ databases, version tracking | 🟡 API Key | ✅ | ✅ |
| [Liquibase Hub](https://www.liquibase.com/) | Multi-format changelogs — SQL/XML/YAML/JSON, rollback | 🟡 API Key | ✅ | ✅ |

---

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**When submitting an API, please ensure:**
- JSON responses (preferred)
- Reliable uptime (>99%)
- Clear documentation
- Stable endpoints (no frequent breaking changes)
- Reasonable rate limits (≥100 requests/day for free tier)

---

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [Joseph Han](https://github.com/joshephan) has waived all copyright and related or neighboring rights to this work.
## Mega Expansion - Push to 2000 APIs (Part 1 of 4)

### E-commerce & Retail (Extended)
| [Shopify Admin](https://shopify.dev/api/admin-rest) | E-commerce platform API | 🔴 OAuth | ✅ | ⚠️ |
| [WooCommerce](https://woocommerce.github.io/woocommerce-rest-api-docs/) | WordPress commerce | 🟡 API Key | ✅ | ✅⭐ |
| [BigCommerce](https://developer.bigcommerce.com/api-docs) | E-commerce platform | 🔴 OAuth | ✅ | ⚠️ |
| [Magento](https://devdocs.magento.com/guides/v2.4/rest/bk-rest.html) | Commerce platform | 🔴 OAuth | ✅ | ⚠️ |
| [PrestaShop](https://devdocs.prestashop.com/1.7/webservice/) | E-commerce software | 🟡 API Key | ✅ | ✅ |
| [OpenCart](https://docs.opencart.com/en-gb/system/users/api/) | Shopping cart | 🟡 API Key | ✅ | ✅ |
| [Ecwid](https://api-docs.ecwid.com/reference) | E-commerce API | 🔴 OAuth | ✅ | ⚠️ |
| [Square Commerce](https://developer.squareup.com/reference/square) | Commerce API | 🔴 OAuth | ✅ | ⚠️ |
| [Lightspeed](https://developers.lightspeedhq.com/) | Retail POS | 🔴 OAuth | ✅ | ⚠️ |
| [Vend](https://docs.vendhq.com/) | POS system | 🔴 OAuth | ✅ | ⚠️ |
| [Clover](https://docs.clover.com/reference) | POS platform | 🔴 OAuth | ✅ | ⚠️ |
| [Toast](https://doc.toasttab.com/) | Restaurant POS | 🔴 OAuth | ✅ | ⚠️ |
| [Revel](https://developer.revelsystems.com/) | POS software | 🟡 API Key | ✅ | ✅ |
| [NCR](https://developer.ncr.com/) | Commerce platform | 🟡 API Key | ✅ | ✅ |
| [Shopware](https://shopware.stoplight.io/docs/store-api) | Commerce system | 🟡 API Key | ✅ | ✅ |
| [Spree](https://api.spreecommerce.org/) | Open source commerce | 🔴 OAuth | ✅ | ⚠️ |
| [Sylius](https://docs.sylius.com/en/latest/api/index.html) | E-commerce framework | 🟡 API Key | ✅ | ✅ |
| [CoreCommerce](https://www.corecommerce.com/api-documentation/) | E-commerce platform | 🟡 API Key | ✅ | ✅ |
| [3dcart](https://support.3dcart.com/Knowledgebase/Article/View/543) | E-commerce software | 🟡 API Key | ✅ | ✅ |
| [Volusion](https://developers.volusion.com/) | Commerce platform | 🟡 API Key | ✅ | ✅ |

### Product Data & Catalogs
| [Algolia](https://www.algolia.com/doc/rest-api/search/) | Search API | 🟡 API Key | ✅ | ✅⭐ |
| [Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/rest-apis.html) | Search engine | 🟡 API Key | ✅ | ✅⭐ |
| [MeiliSearch](https://docs.meilisearch.com/reference/api/) | Search engine | 🟡 API Key | ✅ | ✅⭐ |
| [Typesense](https://typesense.org/docs/api/) | Search engine | 🟡 API Key | ✅ | ✅⭐ |
| [Coveo](https://docs.coveo.com/en/151/) | Search platform | 🟡 API Key | ✅ | ✅ |
| [Constructor.io](https://docs.constructor.io/rest_api/) | Product search | 🟡 API Key | ✅ | ✅ |
| [Klevu](https://docs.klevu.com/) | Search & discovery | 🟡 API Key | ✅ | ✅ |
| [Searchspring](https://searchspring.zendesk.com/hc/en-us/sections/201997846-API) | E-commerce search | 🟡 API Key | ✅ | ✅ |
| [Bloomreach](https://documentation.bloomreach.com/) | Commerce experience | klevu | ✅ | ✅ |
| [Attraqt](https://developer.attraqt.com/) | Search & merchandising | 🟡 API Key | ✅ | ✅ |

### Inventory & Warehouse Management
| [Cin7](https://cinman.uservoice.com/knowledgebase/articles/1861947-cin7-api-v3) | Inventory management | 🟡 API Key | ✅ | ✅ |
| [Unleashed](https://apidocs.unleashedsoftware.com/) | Inventory system | 🟡 API Key | ✅ | ✅ |
| [TradeGecko](https://developer.tradegecko.com/) | Inventory platform | 🔴 OAuth | ✅ | ⚠️ |
| [Fishbowl](https://www.fishbowlinventory.com/api) | Inventory software | 🟡 API Key | ✅ | ✅ |
| [inFlow](https://developer.inflowinventory.com/) | Inventory management | 🟡 API Key | ✅ | ✅ |
| [Katana](https://katanamrp.com/api/) | Manufacturing ERP | 🟡 API Key | ✅ | ✅ |
| [Odoo](https://www.odoo.com/documentation/16.0/developer/reference/external_api.html) | ERP system | 🟡 API Key | ✅ | ✅⭐ |
| [ERPNext](https://frappeframework.com/docs/user/en/api) | Open source ERP | 🟡 API Key | ✅ | ✅⭐ |
| [NetSuite](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/chapter_1540391670.html) | Cloud ERP | 🔴 OAuth | ✅ | ⚠️ |
| [SAP Business One](https://help.sap.com/docs/SAP_BUSINESS_ONE_SERVICE_LAYER) | ERP solution | 🔴 OAuth | ✅ | ⚠️ |

### Point of Sale (POS) Systems
| [Vend POS](https://docs.vendhq.com/) | Retail POS | 🔴 OAuth | ✅ | ⚠️ |
| [Lightspeed Retail](https://developers.lightspeedhq.com/retail/) | Retail software | 🔴 OAuth | ✅ | ⚠️ |
| [Square POS](https://developer.squareup.com/reference/square) | POS system | 🔴 OAuth | ✅ | ⚠️ |
| [Shopify POS](https://shopify.dev/api/pos-ui-extensions) | Retail POS | 🔴 OAuth | ✅ | ⚠️ |
| [Toast POS](https://doc.toasttab.com/openapi/) | Restaurant POS | 🔴 OAuth | ✅ | ⚠️ |
| [Clover POS](https://docs.clover.com/reference) | Payment & POS | 🔴 OAuth | ✅ | ⚠️ |
| [Revel Systems](https://developer.revelsystems.com/) | Enterprise POS | 🟡 API Key | ✅ | ✅ |
| [Upserve](https://upserve.readme.io/) | Restaurant platform | 🟡 API Key | ✅ | ✅ |
| [TouchBistro](https://www.touchbistro.com/developer/) | Restaurant POS | 🟡 API Key | ✅ | ✅ |
| [Aloha](https://www.ncr.com/restaurants/aloha-pos) | Restaurant POS | 🟡 API Key | ✅ | ✅ |

### Accounting & Finance Software
| [QuickBooks](https://developer.intuit.com/app/developer/qbo/docs/api/accounting/most-commonly-used/account) | Accounting software | 🔴 OAuth | ✅ | ⚠️ |
| [Xero](https://developer.xero.com/documentation/) | Accounting platform | 🔴 OAuth | ✅ | ⚠️ |
| [FreshBooks](https://www.freshbooks.com/api) | Accounting software | 🔴 OAuth | ✅ | ⚠️ |
| [Wave](https://developer.waveapps.com/hc/en-us) | Accounting software | 🔴 OAuth | ✅ | ⚠️ |
| [Zoho Books](https://www.zoho.com/books/api/v3/) | Accounting software | 🔴 OAuth | ✅ | ⚠️ |
| [Sage](https://developer.sage.com/) | Business software | 🔴 OAuth | ✅ | ⚠️ |
| [MYOB](https://developer.myob.com/) | Accounting software | 🔴 OAuth | ✅ | ⚠️ |
| [Billy](https://www.billy.dk/api) | Invoicing software | 🟡 API Key | ✅ | ✅ |
| [Invoice Ninja](https://api-docs.invoicing.co/) | Invoicing platform | 🟡 API Key | ✅ | ✅⭐ |
| [Akaunting](https://akaunting.com/docs/api) | Free accounting | 🟡 API Key | ✅ | ✅⭐ |

### Banking & Financial Services
| [Plaid](https://plaid.com/docs/api/) | Banking data | 🟡 API Key | ✅ | ✅⭐ |
| [Yodlee](https://developer.yodlee.com/docs) | Financial data | 🟡 API Key | ✅ | ✅ |
| [TrueLayer](https://docs.truelayer.com/) | Open banking | 🟡 API Key | ✅ | ✅⭐ |
| [Tink](https://docs.tink.com/) | Open banking | 🟡 API Key | ✅ | ✅ |
| [Finicity](https://developer.mastercard.com/open-banking-us/documentation/) | Financial data | 🟡 API Key | ✅ | ✅ |
| [MX](https://docs.mx.com/) | Financial data | 🟡 API Key | ✅ | ✅ |
| [Xignite](https://www.xignite.com/api) | Market data | 🟡 API Key | ✅ | ✅ |
| [Intrinio](https://docs.intrinio.com/) | Financial data | 🟡 API Key | ✅ | ✅⭐ |
| [Quandl](https://docs.data.nasdaq.com/) | Financial & economic | 🟡 API Key | ✅ | ✅⭐ |
| [Bloomberg API](https://www.bloomberg.com/professional/support/api-library/) | Market data | 🟡 API Key | ✅ | ✅ |

### Insurance & Risk
| [CoverWallet](https://developers.coverwallet.com/) | Business insurance | 🟡 API Key | ✅ | ✅ |
| [Next Insurance](https://developers.nextinsurance.com/) | Small business insurance | 🟡 API Key | ✅ | ✅ |
| [Pie Insurance](https://developers.pieinsurance.com/) | Workers' comp | 🟡 API Key | ✅ | ✅ |
| [Lemonade](https://developers.lemonade.com/) | Insurance platform | 🟡 API Key | ✅ | ✅ |
| [Root Insurance](https://root.engineering/docs/) | Insurance API | 🟡 API Key | ✅ | ✅ |
| [Openly](https://developers.openly.com/) | Homeowners insurance | 🟡 API Key | ✅ | ✅ |
| [Coalition](https://www.coalitioninc.com/api) | Cyber insurance | 🟡 API Key | ✅ | ✅ |
| [At-Bay](https://www.at-bay.com/developers/) | Cyber insurance | 🟡 API Key | ✅ | ✅ |
| [Embroker](https://developers.embroker.com/) | Commercial insurance | 🟡 API Key | ✅ | ✅ |
| [Bold Penguin](https://developers.boldpenguin.com/) | Commercial insurance | 🟡 API Key | ✅ | ✅ |

### Legal & Compliance
| [LexisNexis](https://developer.lexisnexis.com/) | Legal research | 🟡 API Key | ✅ | ✅ |
| [CourtListener](https://www.courtlistener.com/api/rest-info/) | Court data | 🟡 API Key | ✅ | ✅⭐ |
| [PACER](https://pacer.uscourts.gov/pacer-api) | Federal court records | 🟡 API Key | ✅ | ✅ |
| [Casetext](https://casetext.com/api) | Legal research | 🟡 API Key | ✅ | ✅ |
| [Fastcase](https://www.fastcase.com/api/) | Legal research | 🟡 API Key | ✅ | ✅ |
| [Justia](https://developers.justia.com/) | Legal information | 🟢 No | ✅ | ✅⭐ |
| [OpenCorporates](https://api.opencorporates.com/) | Company data | 🟡 API Key | ✅ | ✅⭐ |
| [UK Companies House](https://developer-specs.company-information.service.gov.uk/) | Company data | 🟡 API Key | ✅ | ✅⭐ |
| [SEC EDGAR](https://www.sec.gov/edgar/sec-api-documentation) | Company filings | 🟢 No | ✅ | ✅⭐ |
| [IRS Tax Stats](https://www.irs.gov/statistics) | Tax statistics | 🟢 No | ✅ | ✅ |

### Human Resources & Payroll
| [BambooHR](https://documentation.bamboohr.com/docs) | HR software | 🟡 API Key | ✅ | ✅⭐ |
| [Gusto](https://docs.gusto.com/) | Payroll & HR | 🔴 OAuth | ✅ | ⚠️ |
| [ADP](https://developers.adp.com/) | Payroll services | 🔴 OAuth | ✅ | ⚠️ |
| [Workday](https://community.workday.com/sites/default/files/file-hosting/restapi/index.html) | Enterprise HR | 🔴 OAuth | ✅ | ⚠️ |
| [Namely](https://developers.namely.com/) | HR platform | 🟡 API Key | ✅ | ✅ |
| [Rippling](https://developer.rippling.com/) | HR & IT platform | 🟡 API Key | ✅ | ✅⭐ |
| [Greenhouse](https://developers.greenhouse.io/) | Recruiting software | 🟡 API Key | ✅ | ✅⭐ |
| [Lever](https://hire.lever.co/developer/documentation) | Recruiting platform | 🟡 API Key | ✅ | ✅ |
| [JazzHR](https://www.jazzhr.com/api) | Recruiting software | 🟡 API Key | ✅ | ✅ |
| [Workable](https://workable.readme.io/) | Recruiting software | 🟡 API Key | ✅ | ✅ |

### Time Tracking & Attendance
| [Toggl](https://developers.track.toggl.com/) | Time tracking | 🟡 API Key | ✅ | ✅⭐ |
| [Clockify](https://clockify.me/developers-api) | Time tracker | 🟡 API Key | ✅ | ✅⭐ |
| [Harvest](https://help.getharvest.com/api-v2/) | Time tracking | 🔴 OAuth | ✅ | ⚠️ |
| [Time Doctor](https://www.timedoctor.com/api-docs/) | Time tracking | 🟡 API Key | ✅ | ✅ |
| [RescueTime](https://www.rescuetime.com/rtx/developers) | Time management | 🟡 API Key | ✅ | ✅⭐ |
| [Everhour](https://everhour.com/developers) | Time tracking | 🟡 API Key | ✅ | ✅ |
| [Timely](https://dev.timelyapp.com/) | Automatic time tracking | 🟡 API Key | ✅ | ✅ |
| [Hubstaff](https://developer.hubstaff.com/) | Time tracking | 🔴 OAuth | ✅ | ⚠️ |
| [TSheets](https://developers.tsheets.com/) | Time tracking | 🔴 OAuth | ✅ | ⚠️ |
| [Deputy](https://www.deputy.com/api-doc/) | Workforce management | 🔴 OAuth | ✅ | ⚠️ |

### Travel & Transportation
| [Amadeus](https://developers.amadeus.com/) | Travel API | 🟡 API Key | ✅ | ✅⭐ |
| [Sabre](https://developer.sabre.com/docs/read/home) | Travel technology | 🟡 API Key | ✅ | ✅ |
| [Travelport](https://developer.travelport.com/) | Travel commerce | 🟡 API Key | ✅ | ✅ |
| [Skyscanner](https://developers.skyscanner.net/) | Flight search | 🟡 API Key | ✅ | ✅⭐ |
| [Kiwi.com](https://docs.kiwi.com/) | Flight booking | 🟡 API Key | ✅ | ✅ |
| [Rome2rio](https://www.rome2rio.com/documentation/) | Multi-modal transport | 🟡 API Key | ✅ | ✅ |
| [FlightStats](https://developer.flightstats.com/) | Flight tracking | 🟡 API Key | ✅ | ✅ |
| [Booking.com](https://developers.booking.com/) | Hotel booking | 🟡 API Key | ✅ | ✅ |
| [Expedia](https://developer.expediapartnersolutions.com/) | Travel services | 🟡 API Key | ✅ | ✅ |
| [TripAdvisor](https://developer-tripadvisor.com/home/) | Travel content | 🟡 API Key | ✅ | ✅ |

### Hospitality & Hotels
| [Airbnb](https://www.airbnb.com/partner) | Vacation rentals | 🔴 OAuth | ✅ | ⚠️ |
| [Vrbo](https://developers.vrbo.com/) | Vacation rentals | 🟡 API Key | ✅ | ✅ |
| [Hotels.com](https://developers.hotelsforhope.com/) | Hotel booking | 🟡 API Key | ✅ | ✅ |
| [Agoda](https://affiliates.agoda.com/en-us/) | Accommodation | 🟡 API Key | ✅ | ✅ |
| [Hostelworld](https://developer.hostelworld.com/) | Hostel booking | 🟡 API Key | ✅ | ✅ |
| [OpenTable](https://platform.opentable.com/) | Restaurant reservations | 🔴 OAuth | ✅ | ⚠️ |
| [Resy](https://resy.com/api-documentation) | Restaurant booking | 🟡 API Key | ✅ | ✅ |
| [Yelp Reservations](https://www.yelp.com/developers/documentation/v3) | Restaurant API | 🟡 API Key | ✅ | ✅ |
| [TheFork](https://developer.thefork.com/) | Restaurant booking | 🟡 API Key | ✅ | ✅ |
| [Zomato](https://developers.zomato.com/api) | Restaurant search | 🟡 API Key | ✅ | ✅ |

### Delivery & Logistics
| [Uber Eats](https://developer.uber.com/docs/eats) | Food delivery | 🔴 OAuth | ✅ | ⚠️ |
| [DoorDash](https://developer.doordash.com/) | Delivery platform | 🟡 API Key | ✅ | ✅ |
| [Postmates](https://postmates.com/developer) | Delivery service | 🟡 API Key | ✅ | ✅ |
| [Grubhub](https://developer.grubhub.com/) | Food ordering | 🔴 OAuth | ✅ | ⚠️ |
| [Deliveroo](https://deliveroo.engineering/api/) | Food delivery | 🟡 API Key | ✅ | ✅ |
| [Just Eat](https://developers.just-eat.com/) | Food delivery | 🟡 API Key | ✅ | ✅ |
| [Instacart](https://www.instacart.com/developer) | Grocery delivery | 🔴 OAuth | ✅ | ⚠️ |
| [Shipt](https://developer.shipt.com/) | Grocery delivery | 🟡 API Key | ✅ | ✅ |
| [Gopuff](https://gopuff.com/go/api) | Instant delivery | 🟡 API Key | ✅ | ✅ |
| [Drizly](https://developer.drizly.com/) | Alcohol delivery | 🟡 API Key | ✅ | ✅ |

### Ride Sharing & Mobility
| [Uber](https://developer.uber.com/) | Ride sharing | 🔴 OAuth | ✅ | ⚠️ |
| [Lyft](https://developer.lyft.com/) | Ride sharing | 🔴 OAuth | ✅ | ⚠️ |
| [Bolt](https://docs.bolt.eu/) | Ride hailing | 🟡 API Key | ✅ | ✅ |
| [Grab](https://developer.grab.com/) | Super app | 🔴 OAuth | ✅ | ⚠️ |
| [Gojek](https://docs.gojek.io/) | Multi-service platform | 🔴 OAuth | ✅ | ⚠️ |
| [Didi](https://didimobility.gitbook.io/) | Ride hailing | 🟡 API Key | ✅ | ✅ |
| [Ola](https://developer.olacabs.com/) | Ride sharing | 🔴 OAuth | ✅ | ⚠️ |
| [Via](https://developers.ridewithvia.com/) | Shared mobility | 🟡 API Key | ✅ | ✅ |
| [Lime](https://developers.li.me/) | Micro-mobility | 🔴 OAuth | ✅ | ⚠️ |
| [Bird](https://developers.bird.co/) | Scooter sharing | 🔴 OAuth | ✅ | ⚠️ |

### Parking & EV Charging
| [ParkWhiz](https://www.parkwhiz.com/developers/) | Parking reservations | 🟡 API Key | ✅ | ✅ |
| [SpotHero](https://spothero.com/developers) | Parking marketplace | 🟡 API Key | ✅ | ✅ |
| [ParkMobile](https://parkmobile.io/developers/) | Parking payment | 🟡 API Key | ✅ | ✅ |
| [ChargePoint](https://developer.chargepoint.com/) | EV charging | 🟡 API Key | ✅ | ✅⭐ |
| [EVgo](https://developer.evgo.com/) | EV charging network | 🟡 API Key | ✅ | ✅ |
| [Electrify America](https://www.electrifyamerica.com/developers/) | EV charging | 🟡 API Key | ✅ | ✅ |
| [Tesla](https://www.tesla.com/support/vehicle-api) | Tesla API | 🔴 OAuth | ✅ | ⚠️ |
| [Open Charge Map](https://openchargemap.org/site/develop/api) | EV charging data | 🟡 API Key | ✅ | ✅⭐ |
| [PlugShare](https://company.plugshare.com/api.html) | EV charging map | 🟡 API Key | ✅ | ✅ |
| [Zap-Map](https://www.zap-map.com/api/) | UK EV charging | 🟡 API Key | ✅ | ✅ |
## Mega Expansion - Push to 2000 APIs (Part 2 of 4)

### Healthcare & Telemedicine
| [Epic FHIR](https://fhir.epic.com/) | Healthcare records | 🔴 OAuth | ✅ | ⚠️ |
| [Cerner](https://fhir.cerner.com/) | EHR system | 🔴 OAuth | ✅ | ⚠️ |
| [Allscripts](https://developer.allscripts.com/) | Healthcare IT | 🔴 OAuth | ✅ | ⚠️ |
| [Athenahealth](https://docs.athenahealth.com/) | EHR & practice management | 🔴 OAuth | ✅ | ⚠️ |
| [DrChrono](https://drchrono.com/api-docs/) | EHR platform | 🔴 OAuth | ✅ | ⚠️ |
| [Practice Fusion](https://www.practicefusion.com/developer/) | EHR software | 🔴 OAuth | ✅ | ⚠️ |
| [Kareo](https://developer.kareo.com/) | Medical software | 🔴 OAuth | ✅ | ⚠️ |
| [CareCloud](https://www.carecloud.com/developers/) | Healthcare platform | 🟡 API Key | ✅ | ✅ |
| [1upHealth](https://1up.health/dev) | Health data platform | 🟡 API Key | ✅ | ✅⭐ |
| [Human API](https://www.humanapi.co/) | Health data | 🟡 API Key | ✅ | ✅ |
| [Validic](https://docs.validic.com/) | Remote monitoring | 🟡 API Key | ✅ | ✅ |
| [Apple HealthKit](https://developer.apple.com/documentation/healthkit) | Health data | 🔴 OAuth | ✅ | ⚠️ |
| [Google Fit](https://developers.google.com/fit) | Fitness tracking | 🔴 OAuth | ✅ | ⚠️ |
| [Fitbit](https://dev.fitbit.com/build/reference/web-api/) | Fitness tracker | 🔴 OAuth | ✅ | ⚠️ |
| [Withings](https://developer.withings.com/) | Health devices | 🔴 OAuth | ✅ | ⚠️ |
| [Oura](https://cloud.ouraring.com/docs/) | Sleep & activity tracker | 🔴 OAuth | ✅ | ⚠️ |
| [Whoop](https://developer.whoop.com/) | Fitness wearable | 🔴 OAuth | ✅ | ⚠️ |
| [MyFitnessPal](https://www.myfitnesspal.com/api) | Nutrition tracking | 🔴 OAuth | ✅ | ⚠️ |
| [Cronometer](https://cronometer.com/api/) | Nutrition tracker | 🟡 API Key | ✅ | ✅ |
| [Lose It!](https://www.loseit.com/api/) | Weight loss app | 🔴 OAuth | ✅ | ⚠️ |

### Pharmacy & Prescriptions
| [Truepill](https://truepill.com/developers) | Digital pharmacy | 🟡 API Key | ✅ | ✅ |
| [PillPack](https://www.pillpack.com/api) | Pharmacy delivery | 🟡 API Key | ✅ | ✅ |
| [Alto Pharmacy](https://alto.com/api) | Pharmacy service | 🟡 API Key | ✅ | ✅ |
| [Capsule](https://www.capsulecares.com/developers) | Pharmacy platform | 🟡 API Key | ✅ | ✅ |
| [NowRx](https://nowrx.com/api) | Pharmacy delivery | 🟡 API Key | ✅ | ✅ |
| [ScriptDrop](https://scriptdrop.co/api) | Prescription delivery | 🟡 API Key | ✅ | ✅ |
| [Medly](https://medly.com/developers) | Digital pharmacy | 🟡 API Key | ✅ | ✅ |
| [Honeybee Health](https://honeybeehealthhq.com/api) | Pharmacy marketplace | 🟡 API Key | ✅ | ✅ |
| [GoodRx](https://www.goodrx.com/developer) | Prescription prices | 🟡 API Key | ✅ | ✅⭐ |
| [RxSaver](https://rxsaver.retailmenot.com/api) | Prescription savings | 🟡 API Key | ✅ | ✅ |

### Mental Health & Wellness
| [Talkspace](https://www.talkspace.com/api) | Online therapy | 🟡 API Key | ✅ | ✅ |
| [BetterHelp](https://www.betterhelp.com/developer) | Therapy platform | 🟡 API Key | ✅ | ✅ |
| [Headspace](https://developer.headspace.com/) | Meditation app | 🔴 OAuth | ✅ | ⚠️ |
| [Calm](https://www.calm.com/business/api) | Meditation & sleep | 🟡 API Key | ✅ | ✅ |
| [Ginger](https://www.ginger.com/developers) | Mental health | 🟡 API Key | ✅ | ✅ |
| [Lyra Health](https://www.lyrahealth.com/developers/) | Mental health care | 🟡 API Key | ✅ | ✅ |
| [Spring Health](https://springhealth.com/api) | Mental health benefits | 🟡 API Key | ✅ | ✅ |
| [Modern Health](https://modernhealth.com/developers) | Mental wellness | 🟡 API Key | ✅ | ✅ |
| [Sanvello](https://www.sanvello.com/api) | Mental health app | 🟡 API Key | ✅ | ✅ |
| [Happify](https://www.happify.com/developers) | Emotional wellness | 🟡 API Key | ✅ | ✅ |

### Dental & Vision Care
| [Smile Direct Club](https://smiledirectclub.com/api) | Dental aligners | 🟡 API Key | ✅ | ✅ |
| [Candid](https://www.candidco.com/api) | Teeth aligners | 🟡 API Key | ✅ | ✅ |
| [Byte](https://byte.com/developers) | Aligner therapy | 🟡 API Key | ✅ | ✅ |
| [Warby Parker](https://www.warbyparker.com/api) | Eyewear | 🟡 API Key | ✅ | ✅ |
| [Zenni Optical](https://www.zennioptical.com/api) | Prescription glasses | 🟡 API Key | ✅ | ✅ |
| [EyeBuyDirect](https://www.eyebuydirect.com/developers) | Eyeglasses online | 🟡 API Key | ✅ | ✅ |
| [Lensabl](https://lensabl.com/api) | Lens replacement | 🟡 API Key | ✅ | ✅ |
| [Hubble](https://hubblecontacts.com/api) | Contact lenses | 🟡 API Key | ✅ | ✅ |
| [Simple Contacts](https://simplecontacts.com/developers) | Contact lens delivery | 🟡 API Key | ✅ | ✅ |
| [1-800 Contacts](https://www.1800contacts.com/api) | Contact lenses | 🟡 API Key | ✅ | ✅ |

### Lab Testing & Diagnostics
| [Quest Diagnostics](https://www.questdiagnostics.com/business-solutions/health-plans/apis) | Lab testing | 🟡 API Key | ✅ | ✅ |
| [LabCorp](https://developer.labcorp.com/) | Clinical laboratory | 🟡 API Key | ✅ | ✅ |
| [Everlywell](https://www.everlywell.com/api) | At-home lab tests | 🟡 API Key | ✅ | ✅ |
| [LetsGetChecked](https://www.letsgetchecked.com/api) | Home health testing | 🟡 API Key | ✅ | ✅ |
| [Pixel by LabCorp](https://pixelbylabcorp.com/api) | At-home testing | 🟡 API Key | ✅ | ✅ |
| [Color](https://www.color.com/developers) | Genetic testing | 🟡 API Key | ✅ | ✅ |
| [23andMe](https://api.23andme.com/) | Genetic service | 🔴 OAuth | ✅ | ⚠️ |
| [Ancestry DNA](https://www.ancestry.com/dna/developers) | Genetic genealogy | 🔴 OAuth | ✅ | ⚠️ |
| [MyHeritage DNA](https://www.myheritage.com/api) | DNA testing | 🔴 OAuth | ✅ | ⚠️ |
| [Living DNA](https://livingdna.com/api) | Ancestry & wellness | 🟡 API Key | ✅ | ✅ |

### Pet Care & Veterinary
| [Chewy](https://www.chewy.com/api) | Pet supplies | 🟡 API Key | ✅ | ✅ |
| [Petco](https://developer.petco.com/) | Pet retailer | 🟡 API Key | ✅ | ✅ |
| [PetSmart](https://www.petsmart.com/developers) | Pet store | 🟡 API Key | ✅ | ✅ |
| [Rover](https://www.rover.com/api/) | Pet sitting | 🔴 OAuth | ✅ | ⚠️ |
| [Wag](https://wagwalking.com/api) | Dog walking | 🟡 API Key | ✅ | ✅ |
| [Pawp](https://pawp.com/api) | Pet telehealth | 🟡 API Key | ✅ | ✅ |
| [Dutch](https://www.dutch.com/developers) | Pet telemedicine | 🟡 API Key | ✅ | ✅ |
| [Fuzzy](https://www.fuzzy.com/api) | Pet health | 🟡 API Key | ✅ | ✅ |
| [Petfinder API](https://www.petfinder.com/developers/) | Pet adoption | 🟡 API Key | ✅ | ✅⭐ |
| [PetRescue](https://www.petrescue.com.au/api) | Pet adoption | 🟡 API Key | ✅ | ✅ |

### Agriculture & Farming
| [OpenWeatherMap Agro](https://agromonitoring.com/api) | Agricultural monitoring | 🟡 API Key | ✅ | ✅⭐ |
| [Farmers Business Network](https://www.fbn.com/developers) | Farm management | 🟡 API Key | ✅ | ✅ |
| [Climate FieldView](https://www.climate.com/developers) | Precision agriculture | 🟡 API Key | ✅ | ✅ |
| [John Deere](https://developer.deere.com/) | Farm equipment | 🔴 OAuth | ✅ | ⚠️ |
| [Trimble Ag](https://developer.trimble.com/ag-software) | Ag software | 🟡 API Key | ✅ | ✅ |
| [Granular](https://granular.ag/developers) | Farm management | 🟡 API Key | ✅ | ✅ |
| [AgriWebb](https://agriwebb.com/api) | Livestock management | 🟡 API Key | ✅ | ✅ |
| [FarmLogs](https://farmlogs.com/api) | Farm record keeping | 🟡 API Key | ✅ | ✅ |
| [Conservis](https://www.conservis.ag/api) | Farm management | 🟡 API Key | ✅ | ✅ |
| [Farmers Edge](https://www.farmersedge.ca/developers) | Precision ag | 🟡 API Key | ✅ | ✅ |

### Construction & Architecture
| [Procore](https://developers.procore.com/) | Construction management | 🔴 OAuth | ✅ | ⚠️ |
| [PlanGrid](https://developer.plangrid.com/) | Construction productivity | 🔴 OAuth | ✅ | ⚠️ |
| [Autodesk BIM 360](https://forge.autodesk.com/) | Construction platform | 🔴 OAuth | ✅ | ⚠️ |
| [Buildertrend](https://buildertrend.com/api) | Construction software | 🟡 API Key | ✅ | ✅ |
| [CoConstruct](https://coconstruct.com/api) | Construction management | 🟡 API Key | ✅ | ✅ |
| [Jobber](https://developer.getjobber.com/) | Home service software | 🔴 OAuth | ✅ | ⚠️ |
| [ServiceTitan](https://developer.servicetitan.io/) | Home services software | 🔴 OAuth | ✅ | ⚠️ |
| [Housecall Pro](https://developer.housecallpro.com/) | Field service | 🔴 OAuth | ✅ | ⚠️ |
| [FieldPulse](https://fieldpulse.com/api) | Field service software | 🟡 API Key | ✅ | ✅ |
| [ServiceM8](https://developer.servicem8.com/) | Job management | 🔴 OAuth | ✅ | ⚠️ |

### Energy & Utilities
| [EIA](https://www.eia.gov/opendata/) | Energy information | 🟡 API Key | ✅ | ✅⭐ |
| [IEA](https://www.iea.org/data-and-statistics/data-tools) | Energy data | 🟢 No | ✅ | ✅ |
| [World Bank Energy](https://data.worldbank.org/topic/energy-and-mining) | Energy statistics | 🟢 No | ✅ | ✅⭐ |
| [ENTSO-E](https://transparency.entsoe.eu/content/static_content/Static%20content/web%20api/Guide.html) | European electricity | 🟡 API Key | ✅ | ✅⭐ |
| [ElexonAPI](https://www.elexon.co.uk/guidance-note/bmrs-api-data-push-user-guide/) | UK electricity | 🟡 API Key | ✅ | ✅ |
| [EnergyPlus](https://energyplus.net/weather) | Building energy | 🟢 No | ✅ | ✅ |
| [PVWatts](https://developer.nrel.gov/docs/solar/pvwatts/) | Solar calculator | 🟡 API Key | ✅ | ✅⭐ |
| [NREL](https://developer.nrel.gov/) | Renewable energy | 🟡 API Key | ✅ | ✅⭐ |
| [WattTime](https://www.watttime.org/api-documentation/) | Grid emissions | 🟡 API Key | ✅ | ✅⭐ |
| [Electricity Maps](https://api-portal.electricitymaps.com/) | Carbon intensity | 🟡 API Key | ✅ | ✅⭐ |

### Environmental & Climate
| [NASA POWER](https://power.larc.nasa.gov/docs/) | Solar & weather data | 🟢 No | ✅ | ✅⭐ |
| [Copernicus](https://cds.climate.copernicus.eu/api-how-to) | Climate data | 🟡 API Key | ✅ | ✅⭐ |
| [NOAA](https://www.ncdc.noaa.gov/cdo-web/webservices/v2) | Weather & climate | 🟡 API Key | ✅ | ✅⭐ |
| [Met Office](https://www.metoffice.gov.uk/services/data/datapoint/api) | UK weather | 🟡 API Key | ✅ | ✅ |
| [OpenWeatherMap](https://openweathermap.org/api) | Weather API | 🟡 API Key | ✅ | ✅⭐ |
| [Weatherbit](https://www.weatherbit.io/api) | Weather data | 🟡 API Key | ✅ | ✅ |
| [Dark Sky](https://darksky.net/dev) | Weather API | 🟡 API Key | ✅ | ✅ |
| [AccuWeather](https://developer.accuweather.com/) | Weather forecasts | 🟡 API Key | ✅ | ✅ |
| [Weather Underground](https://www.wunderground.com/weather/api/) | Weather data | 🟡 API Key | ✅ | ✅ |
| [MeteoBlue](https://content.meteoblue.com/en/business-solutions/weather-apis) | Weather API | 🟡 API Key | ✅ | ✅ |

### Astronomy & Space
| [NASA APIs](https://api.nasa.gov/) | Space data | 🟡 API Key | ✅ | ✅⭐ |
| [SpaceX](https://github.com/r-spacex/SpaceX-API) | SpaceX data | 🟢 No | ✅ | ✅⭐ |
| [Launch Library](https://ll.thespacedevs.com/2.2.0/swagger/) | Space launches | 🟢 No | ✅ | ✅⭐ |
| [Open Notify](http://open-notify.org/Open-Notify-API/) | ISS location | 🟢 No | No | ✅⭐ |
| [SkyField](https://rhodesmill.org/skyfield/) | Astronomy positions | 🟢 No | ✅ | ✅ |
| [AstroBin](https://www.astrobin.com/api/v2/) | Astrophotography | 🟡 API Key | ✅ | ✅ |
| [Celestrak](https://celestrak.com/NORAD/documentation/) | Satellite tracking | 🟢 No | ✅ | ✅⭐ |
| [N2YO](https://www.n2yo.com/api/) | Satellite tracker | 🟡 API Key | ✅ | ✅ |
| [Minor Planet Center](https://minorplanetcenter.net/web_service) | Asteroid data | 🟢 No | ✅ | ✅ |
| [Asterank](http://www.asterank.com/api) | Asteroid database | 🟢 No | ✅ | ✅ |

### Genealogy & Family History
| [FamilySearch](https://www.familysearch.org/developers/) | Family history | 🔴 OAuth | ✅ | ⚠️ |
| [Ancestry](https://www.ancestry.com/cs/dna-help/apis) | Genealogy service | 🔴 OAuth | ✅ | ⚠️ |
| [MyHeritage](https://www.myheritage.com/api) | Family tree | 🔴 OAuth | ✅ | ⚠️ |
| [Findmypast](https://www.findmypast.com/api) | Genealogy records | 🟡 API Key | ✅ | ✅ |
| [Geni](https://www.geni.com/platform/developer) | Family tree | 🔴 OAuth | ✅ | ⚠️ |
| [WikiTree](https://www.wikitree.com/wiki/Help:API_Documentation) | Free family tree | 🟢 No | ✅ | ✅⭐ |
| [Gramps](https://gramps-project.org/wiki/index.php/Gramps_5.1_Wiki_Manual) | Genealogy software | 🟢 No | ✅ | ✅ |
| [RootsMagic](https://www.rootsmagic.com/) | Family tree software | 🟡 API Key | ✅ | ✅ |
| [Legacy Family Tree](https://www.legacyfamilytree.com/developers.asp) | Genealogy software | 🟡 API Key | ✅ | ✅ |
| [Heredis](https://www.heredis.com/developers) | Family tree software | 🟡 API Key | ✅ | ✅ |

### Events & Ticketing
| [Eventbrite](https://www.eventbrite.com/platform/api) | Event management | 🔴 OAuth | ✅ | ⚠️ |
| [Ticketmaster](https://developer.ticketmaster.com/products-and-docs/apis/getting-started/) | Event ticketing | 🟡 API Key | ✅ | ✅⭐ |
| [StubHub](https://developer.stubhub.com/) | Ticket marketplace | 🟡 API Key | ✅ | ✅ |
| [SeatGeek](https://platform.seatgeek.com/) | Event tickets | 🟡 API Key | ✅ | ✅⭐ |
| [Universe](https://www.universe.com/api) | Event ticketing | 🟡 API Key | ✅ | ✅ |
| [Dice](https://dice.fm/developers) | Event discovery | 🟡 API Key | ✅ | ✅ |
| [Bandsintown](https://www.bandsintown.com/api) | Concert discovery | 🟡 API Key | ✅ | ✅⭐ |
| [Songkick](https://www.songkick.com/developer) | Concert listings | 🟡 API Key | ✅ | ✅ |
| [Meetup](https://www.meetup.com/api/) | Event platform | 🔴 OAuth | ✅ | ⚠️ |
| [Eventful](http://api.eventful.com/) | Event search | 🟡 API Key | ✅ | ✅ |

### Dating & Social Discovery
| [Tinder](https://www.gotinder.com/api/) | Dating app | 🔴 OAuth | ✅ | ⚠️ |
| [Bumble](https://bumble.com/api) | Dating & networking | 🔴 OAuth | ✅ | ⚠️ |
| [Hinge](https://hinge.co/api) | Dating app | 🔴 OAuth | ✅ | ⚠️ |
| [OkCupid](https://www.okcupid.com/dev) | Dating site | 🔴 OAuth | ✅ | ⚠️ |
| [Match](https://www.match.com/developers) | Dating service | 🔴 OAuth | ✅ | ⚠️ |
| [eHarmony](https://www.eharmony.com/api) | Dating site | 🔴 OAuth | ✅ | ⚠️ |
| [Coffee Meets Bagel](https://coffeemeetsbagel.com/api) | Dating app | 🔴 OAuth | ✅ | ⚠️ |
| [The League](https://www.theleague.com/api) | Dating app | 🔴 OAuth | ✅ | ⚠️ |
| [Plenty of Fish](https://www.pof.com/api) | Dating site | 🔴 OAuth | ✅ | ⚠️ |
| [Badoo](https://badoo.com/team/api/) | Dating & social | 🔴 OAuth | ✅ | ⚠️ |

### Charity & Donations
| [JustGiving](https://api.justgiving.com/) | Fundraising platform | 🟡 API Key | ✅ | ✅⭐ |
| [GoFundMe](https://www.gofundme.com/c/api) | Crowdfunding | 🟡 API Key | ✅ | ✅ |
| [Kickstarter](https://www.kickstarter.com/help/stats) | Crowdfunding | 🟢 No | ✅ | ✅ |
| [Indiegogo](https://developer.indiegogo.com/) | Crowdfunding | 🟡 API Key | ✅ | ✅ |
| [Patreon](https://docs.patreon.com/) | Creator membership | 🔴 OAuth | ✅ | ⚠️ |
| [Ko-fi](https://ko-fi.com/manage/webhooks) | Creator support | 🟡 API Key | ✅ | ✅ |
| [Buy Me a Coffee](https://developers.buymeacoffee.com/) | Creator support | 🟡 API Key | ✅ | ✅⭐ |
| [Liberapay](https://liberapay.com/about/faq#api) | Donations platform | 🟢 No | ✅ | ✅⭐ |
| [Open Collective](https://docs.opencollective.com/help/contributing/development/api) | Collective funding | 🟡 API Key | ✅ | ✅⭐ |
| [DonorBox](https://donorbox.org/nonprofit-blog/donorbox-api/) | Fundraising software | 🟡 API Key | ✅ | ✅ |

### Volunteering & Community
| [VolunteerMatch](https://www.volunteermatch.org/api) | Volunteer opportunities | 🟡 API Key | ✅ | ✅⭐ |
| [Idealist](https://www.idealist.org/en/info/API) | Nonprofits & volunteers | 🟡 API Key | ✅ | ✅ |
| [All for Good](http://www.allforgood.org/api) | Volunteer listings | 🟢 No | ✅ | ✅ |
| [HandsOn Network](https://www.pointsoflight.org/api) | Volunteer network | 🟡 API Key | ✅ | ✅ |
| [DoSomething](https://www.dosomething.org/us/api) | Youth volunteering | 🟡 API Key | ✅ | ✅⭐ |
| [Catchafire](https://www.catchafire.org/api/) | Skills-based volunteering | 🟡 API Key | ✅ | ✅ |
| [Golden](https://www.golden.com/api) | Volunteer management | 🟡 API Key | ✅ | ✅ |
| [Better Impact](https://www.betterimpact.com/api) | Volunteer software | 🟡 API Key | ✅ | ✅ |
| [Track It Forward](https://trackitforward.com/api) | Volunteer tracking | 🟡 API Key | ✅ | ✅ |
| [GivePulse](https://www.givepulse.com/api) | Volunteer & civic engagement | 🟡 API Key | ✅ | ✅ |

### Nonprofit & NGO Tools
| [Salesforce Nonprofit](https://developer.salesforce.com/docs/atlas.en-us.npo.meta/npo/) | Nonprofit CRM | 🔴 OAuth | ✅ | ⚠️ |
| [Bloomerang](https://bloomerang.co/product/integrations/api/) | Donor management | 🟡 API Key | ✅ | ✅ |
| [Blackbaud](https://developer.blackbaud.com/) | Nonprofit software | 🔴 OAuth | ✅ | ⚠️ |
| [Little Green Light](https://www.littlegreenlight.com/api/) | Fundraising CRM | 🟡 API Key | ✅ | ✅ |
| [NeonCRM](https://developer.neoncrm.com/) | Nonprofit CRM | 🟡 API Key | ✅ | ✅ |
| [Kindful](https://kindful.com/api/) | Donor management | 🟡 API Key | ✅ | ✅ |
| [CiviCRM](https://docs.civicrm.org/dev/en/latest/api/) | Open source CRM | 🟡 API Key | ✅ | ✅⭐ |
| [GiveWP](https://givewp.com/documentation/developers/) | WordPress donations | 🟡 API Key | ✅ | ✅⭐ |
| [Classy](https://developers.classy.org/) | Online fundraising | 🔴 OAuth | ✅ | ⚠️ |
| [Qgiv](https://qgiv.com/api/) | Fundraising platform | 🟡 API Key | ✅ | ✅ |
## Mega Expansion - Push to 2000 APIs (Part 3 of 4)

### Streaming & Content Creation
| [Twitch API](https://dev.twitch.tv/docs/api/) | Live streaming | 🔴 OAuth | ✅ | ⚠️ |
| [YouTube Data API](https://developers.google.com/youtube/v3) | Video platform | 🟡 API Key | ✅ | ✅⭐ |
| [Vimeo API](https://developer.vimeo.com/) | Video hosting | 🔴 OAuth | ✅ | ⚠️ |
| [DailyMotion API](https://developers.dailymotion.com/) | Video sharing | 🔴 OAuth | ✅ | ⚠️ |
| [TikTok API](https://developers.tiktok.com/) | Short video platform | 🔴 OAuth | ✅ | ⚠️ |
| [Instagram Graph API](https://developers.facebook.com/docs/instagram-api) | Photo sharing | 🔴 OAuth | ✅ | ⚠️ |
| [Snapchat API](https://kit.snapchat.com/) | Messaging app | 🔴 OAuth | ✅ | ⚠️ |
| [Pinterest API](https://developers.pinterest.com/) | Visual discovery | 🔴 OAuth | ✅ | ⚠️ |
| [Flickr API](https://www.flickr.com/services/api/) | Photo sharing | 🟡 API Key | ✅ | ✅⭐ |
| [500px API](https://developers.500px.com/) | Photography | 🔴 OAuth | ✅ | ⚠️ |

### Podcast Hosting & Distribution
| [Anchor](https://anchor.fm/api) | Podcast hosting | 🟡 API Key | ✅ | ✅ |
| [Podbean](https://developers.podbean.com/) | Podcast platform | 🟡 API Key | ✅ | ✅ |
| [Buzzsprout](https://www.buzzsprout.com/api) | Podcast hosting | 🟡 API Key | ✅ | ✅ |
| [Transistor](https://developers.transistor.fm/) | Podcast analytics | 🟡 API Key | ✅ | ✅⭐ |
| [Simplecast](https://simplecast.com/api/) | Podcast hosting | 🟡 API Key | ✅ | ✅ |
| [Libsyn](https://support.libsyn.com/kb/api/) | Podcast hosting | 🟡 API Key | ✅ | ✅ |
| [Spreaker](https://developers.spreaker.com/) | Podcast creation | 🟡 API Key | ✅ | ✅ |
| [Podchaser](https://api-docs.podchaser.com/) | Podcast database | 🟡 API Key | ✅ | ✅⭐ |
| [Chartable](https://chartable.com/api) | Podcast analytics | 🟡 API Key | ✅ | ✅ |
| [Podtrac](https://analytics.podtrac.com/api) | Podcast measurement | 🟡 API Key | ✅ | ✅ |

### Live Broadcasting & Webinars
| [Zoom API](https://marketplace.zoom.us/docs/api-reference/introduction) | Video conferencing | 🔴 OAuth | ✅ | ⚠️ |
| [Google Meet](https://developers.google.com/meet/api) | Video meetings | 🔴 OAuth | ✅ | ⚠️ |
| [Microsoft Teams](https://docs.microsoft.com/en-us/graph/api/resources/teams-api-overview) | Collaboration platform | 🔴 OAuth | ✅ | ⚠️ |
| [Webex](https://developer.webex.com/) | Video conferencing | 🔴 OAuth | ✅ | ⚠️ |
| [GoToWebinar](https://developer.goto.com/) | Webinar platform | 🔴 OAuth | ✅ | ⚠️ |
| [Demio](https://demio.com/api) | Webinar software | 🟡 API Key | ✅ | ✅ |
| [Crowdcast](https://docs.crowdcast.io/) | Live events | 🟡 API Key | ✅ | ✅ |
| [StreamYard](https://streamyard.com/api) | Live streaming | 🟡 API Key | ✅ | ✅ |
| [Restream](https://developers.restream.io/) | Multi-streaming | 🟡 API Key | ✅ | ✅⭐ |
| [OBS Studio](https://obsproject.com/wiki/Websocket-Protocol) | Broadcast software | 🟢 No | ✅ | ✅⭐ |

### Screen Recording & Screenshots
| [Loom](https://dev.loom.com/) | Video messaging | 🔴 OAuth | ✅ | ⚠️ |
| [Screencast-O-Matic](https://screencast-o-matic.com/api) | Screen recorder | 🟡 API Key | ✅ | ✅ |
| [Snagit](https://www.techsmith.com/snagit-api.html) | Screen capture | 🟡 API Key | ✅ | ✅ |
| [CloudApp](https://developer.getcloudapp.com/) | Visual communication | 🟡 API Key | ✅ | ✅ |
| [Droplr](https://droplr.com/api) | Screenshot sharing | 🟡 API Key | ✅ | ✅ |
| [Monosnap](https://monosnap.com/api) | Screenshot tool | 🟡 API Key | ✅ | ✅ |
| [Lightshot](https://prnt.sc/api) | Screenshot app | 🟢 No | ✅ | ✅ |
| [ShareX](https://getsharex.com/docs/api) | Screen capture | 🟢 No | ✅ | ✅⭐ |
| [Greenshot](https://getgreenshot.org/) | Screenshot tool | 🟢 No | ✅ | ✅ |
| [Flameshot](https://flameshot.org/) | Screenshot software | 🟢 No | ✅ | ✅ |

### Document Management & Collaboration
| [Google Drive API](https://developers.google.com/drive) | Cloud storage | 🔴 OAuth | ✅ | ⚠️ |
| [Dropbox API](https://www.dropbox.com/developers) | File hosting | 🔴 OAuth | ✅ | ⚠️ |
| [Box API](https://developer.box.com/) | Content management | 🔴 OAuth | ✅ | ⚠️ |
| [OneDrive API](https://docs.microsoft.com/en-us/onedrive/developer/) | Cloud storage | 🔴 OAuth | ✅ | ⚠️ |
| [Notion API](https://developers.notion.com/) | Workspace | 🔴 OAuth | ✅ | ⚠️ |
| [Confluence API](https://developer.atlassian.com/cloud/confluence/rest/) | Team workspace | 🔴 OAuth | ✅ | ⚠️ |
| [SharePoint](https://docs.microsoft.com/en-us/sharepoint/dev/sp-add-ins/sharepoint-net-server-csom-jsom-and-rest-api-index) | Collaboration platform | 🔴 OAuth | ✅ | ⚠️ |
| [Evernote](https://dev.evernote.com/doc/) | Note-taking | 🔴 OAuth | ✅ | ⚠️ |
| [OneNote](https://docs.microsoft.com/en-us/graph/api/resources/onenote) | Digital notebook | 🔴 OAuth | ✅ | ⚠️ |
| [Simplenote](https://simplenote.com/developers/) | Note app | 🟡 API Key | ✅ | ✅⭐ |

### PDF & Document Processing
| [Adobe PDF Services](https://developer.adobe.com/document-services/apis/pdf-services/) | PDF manipulation | 🟡 API Key | ✅ | ✅⭐ |
| [PDFShift](https://pdfshift.io/documentation/) | HTML to PDF | 🟡 API Key | ✅ | ✅⭐ |
| [PDF.co](https://apidocs.pdf.co/) | PDF API | 🟡 API Key | ✅ | ✅⭐ |
| [DocRaptor](https://docraptor.com/documentation) | Document generation | 🟡 API Key | ✅ | ✅ |
| [PDFMonkey](https://www.pdfmonkey.io/docs) | PDF generation | 🟡 API Key | ✅ | ✅ |
| [Docmosis](https://www.docmosis.com/how-it-works/api-options.html) | Document generation | 🟡 API Key | ✅ | ✅ |
| [CloudConvert](https://cloudconvert.com/api/v2) | File conversion | 🟡 API Key | ✅ | ✅⭐ |
| [Zamzar](https://developers.zamzar.com/) | File conversion | 🟡 API Key | ✅ | ✅ |
| [ConvertAPI](https://www.convertapi.com/doc/api-key) | File conversion | 🟡 API Key | ✅ | ✅⭐ |
| [ILovePDF](https://developer.ilovepdf.com/) | PDF tools | 🟡 API Key | ✅ | ✅ |

### OCR & Document Extraction
| [Google Cloud Vision OCR](https://cloud.google.com/vision/docs/ocr) | Optical character recognition | 🟡 API Key | ✅ | ✅⭐ |
| [Microsoft Azure OCR](https://azure.microsoft.com/en-us/products/cognitive-services/computer-vision) | OCR service | 🟡 API Key | ✅ | ✅⭐ |
| [AWS Textract](https://aws.amazon.com/textract/) | Document text extraction | 🟡 API Key | ✅ | ✅⭐ |
| [ABBYY Cloud OCR](https://www.ocrsdk.com/) | OCR SDK | 🟡 API Key | ✅ | ✅ |
| [OCR.space](https://ocr.space/OCRAPI) | Free OCR API | 🟡 API Key | ✅ | ✅⭐ |
| [Tesseract](https://github.com/tesseract-ocr/tesseract) | Open source OCR | 🟢 No | ✅ | ✅⭐ |
| [EasyOCR](https://github.com/JaidedAI/EasyOCR) | Ready-to-use OCR | 🟢 No | ✅ | ✅⭐ |
| [Rossum](https://rossum.ai/developers/) | Document AI | 🟡 API Key | ✅ | ✅ |
| [Nanonets](https://nanonets.com/documentation/) | OCR & data extraction | 🟡 API Key | ✅ | ✅⭐ |
| [Docparser](https://docparser.com/documentation/) | Document parsing | 🟡 API Key | ✅ | ✅ |

### Signature & Document Signing
| [DocuSign](https://developers.docusign.com/) | Electronic signature | 🔴 OAuth | ✅ | ⚠️ |
| [HelloSign](https://www.hellosign.com/api) | eSignature | 🟡 API Key | ✅ | ✅⭐ |
| [Adobe Sign](https://secure.na1.adobesign.com/public/docs/restapi/v6) | Digital signatures | 🔴 OAuth | ✅ | ⚠️ |
| [PandaDoc](https://developers.pandadoc.com/) | Document automation | 🟡 API Key | ✅ | ✅⭐ |
| [SignNow](https://docs.signnow.com/) | Document signing | 🔴 OAuth | ✅ | ⚠️ |
| [SignRequest](https://signrequest.com/api/v1/docs/) | eSignature API | 🟡 API Key | ✅ | ✅⭐ |
| [eSignGenie](https://www.esigngenie.com/esignature-api/) | Digital signature | 🟡 API Key | ✅ | ✅ |
| [SignEasy](https://api.getsigneasy.com/docs/) | Mobile signatures | 🟡 API Key | ✅ | ✅ |
| [RightSignature](https://developers.rightsignature.com/) | Electronic signatures | 🟡 API Key | ✅ | ✅ |
| [Secured Signing](https://www.securedsigning.com/api) | Digital signatures | 🟡 API Key | ✅ | ✅ |

### Low-Code / No-Code Platforms
| [Bubble](https://manual.bubble.io/core-resources/api) | Web app builder | 🟡 API Key | ✅ | ✅⭐ |
| [Webflow](https://developers.webflow.com/) | Website builder | 🔴 OAuth | ✅ | ⚠️ |
| [Wix](https://dev.wix.com/api/rest/getting-started/introduction) | Website builder | 🔴 OAuth | ✅ | ⚠️ |
| [Squarespace](https://developers.squarespace.com/) | Website builder | 🔴 OAuth | ✅ | ⚠️ |
| [WordPress REST API](https://developer.wordpress.org/rest-api/) | CMS | 🔴 OAuth | ✅ | ⚠️ |
| [Zapier](https://zapier.com/developer) | Automation platform | 🔴 OAuth | ✅ | ⚠️ |
| [Make (Integromat)](https://www.make.com/en/api-documentation) | Automation | 🟡 API Key | ✅ | ✅⭐ |
| [n8n](https://docs.n8n.io/api/) | Workflow automation | 🟡 API Key | ✅ | ✅⭐ |
| [Retool](https://docs.retool.com/docs/retool-api) | Internal tools | 🟡 API Key | ✅ | ✅⭐ |
| [Appsmith](https://docs.appsmith.com/core-concepts/connecting-to-data-sources/authentication) | Open source low-code | 🟡 API Key | ✅ | ✅⭐ |

### API Development & Testing
| [Postman API](https://www.postman.com/postman/workspace/postman-public-workspace/documentation/12959542-c8142d51-e97c-46b6-bd77-52bb66712c9a) | API platform | 🟡 API Key | ✅ | ✅⭐ |
| [Insomnia](https://docs.insomnia.rest/insomnia/get-started) | API client | 🟢 No | ✅ | ✅⭐ |
| [Paw](https://paw.cloud/) | API tool | 🟡 API Key | ✅ | ✅ |
| [RapidAPI](https://docs.rapidapi.com/docs) | API marketplace | 🟡 API Key | ✅ | ✅⭐ |
| [API Gateway (AWS)](https://docs.aws.amazon.com/apigateway/) | API management | 🟡 API Key | ✅ | ✅⭐ |
| [Kong](https://docs.konghq.com/gateway/latest/admin-api/) | API gateway | 🟡 API Key | ✅ | ✅⭐ |
| [Tyk](https://tyk.io/docs/tyk-apis/) | API gateway | 🟡 API Key | ✅ | ✅⭐ |
| [Apigee](https://cloud.google.com/apigee/docs/api-platform/reference/apis) | API management | 🟡 API Key | ✅ | ✅ |
| [MuleSoft](https://docs.mulesoft.com/) | Integration platform | 🟡 API Key | ✅ | ✅ |
| [WSO2](https://apim.docs.wso2.com/en/latest/) | API management | 🟡 API Key | ✅ | ✅ |

### GraphQL Services
| [Hasura](https://hasura.io/docs/latest/api-reference/overview/) | GraphQL engine | 🟡 API Key | ✅ | ✅⭐ |
| [Apollo Server](https://www.apollographql.com/docs/apollo-server/) | GraphQL server | 🟢 No | ✅ | ✅⭐ |
| [Prisma](https://www.prisma.io/docs/concepts/components/prisma-client) | Database toolkit | 🟢 No | ✅ | ✅⭐ |
| [GraphCMS](https://graphcms.com/docs/api-reference) | Headless CMS | 🟡 API Key | ✅ | ✅⭐ |
| [Hygraph](https://hygraph.com/docs/api-reference) | GraphQL CMS | 🟡 API Key | ✅ | ✅ |
| [Contentful GraphQL](https://www.contentful.com/developers/docs/references/graphql/) | Content platform | 🟡 API Key | ✅ | ✅⭐ |
| [Fauna GraphQL](https://docs.fauna.com/fauna/current/api/graphql/) | Distributed database | 🟡 API Key | ✅ | ✅⭐ |
| [StepZen](https://stepzen.com/docs) | GraphQL service | 🟡 API Key | ✅ | ✅⭐ |
| [WPGraphQL](https://www.wpgraphql.com/) | WordPress GraphQL | 🟢 No | ✅ | ✅⭐ |
| [PostGraphile](https://www.graphile.org/postgraphile/) | PostgreSQL GraphQL | 🟢 No | ✅ | ✅⭐ |

### Headless CMS
| [Strapi](https://docs.strapi.io/developer-docs/latest/developer-resources/database-apis-reference/rest-api.html) | Open source CMS | 🟡 API Key | ✅ | ✅⭐ |
| [Contentful](https://www.contentful.com/developers/docs/references/content-delivery-api/) | Content platform | 🟡 API Key | ✅ | ✅⭐ |
| [Sanity](https://www.sanity.io/docs/http-api) | Content platform | 🟡 API Key | ✅ | ✅⭐ |
| [Prismic](https://prismic.io/docs/technologies/rest-api-technical-reference) | Headless CMS | 🟡 API Key | ✅ | ✅⭐ |
| [Directus](https://docs.directus.io/reference/introduction/) | Open data platform | 🟡 API Key | ✅ | ✅⭐ |
| [Ghost](https://ghost.org/docs/content-api/) | Publishing platform | 🟡 API Key | ✅ | ✅⭐ |
| [Butter CMS](https://buttercms.com/docs/api/) | Headless CMS | 🟡 API Key | ✅ | ✅ |
| [DatoCMS](https://www.datocms.com/docs/content-delivery-api) | Headless CMS | 🟡 API Key | ✅ | ✅ |
| [Cockpit](https://getcockpit.com/documentation/api) | Headless CMS | 🟡 API Key | ✅ | ✅ |
| [Payload CMS](https://payloadcms.com/docs/rest-api/overview) | Headless CMS | 🟡 API Key | ✅ | ✅⭐ |

### Website Builders & Hosting
| [Netlify](https://docs.netlify.com/api/get-started/) | Web hosting | 🟡 API Key | ✅ | ✅⭐ |
| [Vercel](https://vercel.com/docs/rest-api) | Frontend platform | 🟡 API Key | ✅ | ✅⭐ |
| [Cloudflare Pages](https://developers.cloudflare.com/pages/platform/api/) | JAMstack platform | 🟡 API Key | ✅ | ✅⭐ |
| [GitHub Pages](https://docs.github.com/en/rest/pages) | Static hosting | 🟡 API Key | ✅ | ✅⭐ |
| [GitLab Pages](https://docs.gitlab.com/ee/api/pages.html) | Static site hosting | 🟡 API Key | ✅ | ✅ |
| [Render](https://render.com/docs/api) | Cloud platform | 🟡 API Key | ✅ | ✅⭐ |
| [Railway](https://docs.railway.app/reference/public-api) | Infrastructure platform | 🟡 API Key | ✅ | ✅⭐ |
| [Heroku](https://devcenter.heroku.com/categories/platform-api) | Cloud platform | 🟡 API Key | ✅ | ✅ |
| [DigitalOcean App Platform](https://docs.digitalocean.com/reference/api/api-reference/) | PaaS | 🟡 API Key | ✅ | ✅⭐ |
| [Fly.io](https://fly.io/docs/reference/api/) | Global app hosting | 🟡 API Key | ✅ | ✅⭐ |

### Code Quality & Analysis
| [SonarCloud](https://sonarcloud.io/web_api) | Code quality | 🟡 API Key | ✅ | ✅⭐ |
| [CodeClimate](https://codeclimate.com/quality/feeds) | Code analysis | 🟡 API Key | ✅ | ✅ |
| [Codacy](https://api.codacy.com/) | Code review | 🟡 API Key | ✅ | ✅ |
| [DeepSource](https://deepsource.io/docs/api/) | Static analysis | 🟡 API Key | ✅ | ✅ |
| [Coveralls](https://docs.coveralls.io/api-introduction) | Code coverage | 🟡 API Key | ✅ | ✅ |
| [Codecov](https://docs.codecov.com/reference) | Code coverage | 🟡 API Key | ✅ | ✅⭐ |
| [Better Code Hub](https://bettercodehub.com/docs/api) | Code quality | 🟡 API Key | ✅ | ✅ |
| [LGTM](https://lgtm.com/help/lgtm/api/api-v1) | Code analysis | 🟡 API Key | ✅ | ✅ |
| [Sourcegraph](https://docs.sourcegraph.com/api/graphql) | Code search | 🟡 API Key | ✅ | ✅⭐ |
| [CodeScene](https://codescene.com/docs/rest-api.html) | Code analysis | 🟡 API Key | ✅ | ✅ |

### Error Tracking & Logging
| [Sentry](https://docs.sentry.io/api/) | Error tracking | 🟡 API Key | ✅ | ✅⭐ |
| [Rollbar](https://docs.rollbar.com/reference) | Error monitoring | 🟡 API Key | ✅ | ✅⭐ |
| [Bugsnag](https://bugsnagapiv2.docs.apiary.io/) | Error monitoring | 🟡 API Key | ✅ | ✅ |
| [Airbrake](https://airbrake.io/docs/api/) | Error tracking | 🟡 API Key | ✅ | ✅ |
| [Raygun](https://raygun.com/documentation/api/) | Error monitoring | 🟡 API Key | ✅ | ✅ |
| [TrackJS](https://docs.trackjs.com/api/v1/) | JavaScript error tracking | 🟡 API Key | ✅ | ✅ |
| [LogRocket](https://docs.logrocket.com/reference) | Frontend monitoring | 🟡 API Key | ✅ | ✅⭐ |
| [FullStory](https://developer.fullstory.com/) | Digital experience | 🟡 API Key | ✅ | ✅ |
| [Datadog Logs](https://docs.datadoghq.com/api/latest/logs/) | Log management | 🟡 API Key | ✅ | ✅⭐ |
| [Papertrail](https://www.papertrail.com/help/api/) | Log management | 🟡 API Key | ✅ | ✅ |

### Feature Flags & Experimentation
| [LaunchDarkly](https://apidocs.launchdarkly.com/) | Feature management | 🟡 API Key | ✅ | ✅⭐ |
| [Split.io](https://docs.split.io/reference) | Feature flags | 🟡 API Key | ✅ | ✅⭐ |
| [Unleash](https://docs.getunleash.io/reference/api/unleash) | Feature toggle | 🟡 API Key | ✅ | ✅⭐ |
| [Flagsmith](https://docs.flagsmith.com/deployment/hosting/locally-api) | Feature flags | 🟡 API Key | ✅ | ✅⭐ |
| [ConfigCat](https://api.configcat.com/docs/) | Feature flags | 🟡 API Key | ✅ | ✅⭐ |
| [Optimizely](https://docs.developers.optimizely.com/full-stack-experimentation/docs) | Experimentation | 🟡 API Key | ✅ | ✅ |
| [GrowthBook](https://docs.growthbook.io/api) | A/B testing | 🟡 API Key | ✅ | ✅⭐ |
| [Statsig](https://docs.statsig.com/http-api) | Product experimentation | 🟡 API Key | ✅ | ✅⭐ |
| [DevCycle](https://docs.devcycle.com/docs/home) | Feature flags | 🟡 API Key | ✅ | ✅ |
| [FeatureHub](https://docs.featurehub.io/) | Feature management | 🟡 API Key | ✅ | ✅ |

### A/B Testing & Analytics
| [Google Optimize](https://developers.google.com/optimize) | A/B testing | 🟡 API Key | ✅ | ✅ |
| [VWO](https://developers.vwo.com/reference) | A/B testing platform | 🟡 API Key | ✅ | ✅ |
| [AB Tasty](https://developers.abtasty.com/) | Experimentation | 🟡 API Key | ✅ | ✅ |
| [Convert](https://www.convert.com/api/) | A/B testing | 🟡 API Key | ✅ | ✅ |
| [Kameleoon](https://developers.kameleoon.com/) | Experimentation | 🟡 API Key | ✅ | ✅ |
| [Dynamic Yield](https://dynamicyield.github.io/api-documentation/) | Personalization | 🟡 API Key | ✅ | ✅ |
| [Amplitude](https://www.docs.developers.amplitude.com/analytics/apis/http-v2-api/) | Product analytics | 🟡 API Key | ✅ | ✅⭐ |
| [Mixpanel](https://developer.mixpanel.com/reference/overview) | Product analytics | 🟡 API Key | ✅ | ✅⭐ |
| [Segment](https://segment.com/docs/connections/spec/) | Customer data platform | 🟡 API Key | ✅ | ✅⭐ |
| [Heap](https://developers.heap.io/reference) | Digital insights | 🟡 API Key | ✅ | ✅ |
## Mega Expansion - Push to 2000 APIs (Part 4 of 4)

### Session Recording & Heatmaps
| [Hotjar](https://hotjar.com/api/docs) | Heatmaps & recordings | 🟡 API Key | ✅ | ✅⭐ |
| [Crazy Egg](https://www.crazyegg.com/help/api/) | Heatmaps | 🟡 API Key | ✅ | ✅ |
| [Lucky Orange](https://www.luckyorange.com/api.php) | Analytics & heatmaps | 🟡 API Key | ✅ | ✅ |
| [Mouseflow](https://mouseflow-api.readme.io/) | Session replay | 🟡 API Key | ✅ | ✅ |
| [SessionStack](https://docs.sessionstack.com/) | Session replay | 🟡 API Key | ✅ | ✅ |
| [Smartlook](https://www.smartlook.com/docs/sdk/api-reference/) | Qualitative analytics | 🟡 API Key | ✅ | ✅ |
| [Inspectlet](https://www.inspectlet.com/docs/api) | Session recording | 🟡 API Key | ✅ | ✅ |
| [UserReplay](https://www.userreplay.com/api) | Session replay | 🟡 API Key | ✅ | ✅ |
| [Glassbox](https://www.glassbox.com/platform/api/) | Digital experience | 🟡 API Key | ✅ | ✅ |
| [Contentsquare](https://contentsquare.com/developers/) | Experience analytics | 🟡 API Key | ✅ | ✅ |

### User Feedback & Surveys
| [Typeform](https://developer.typeform.com/) | Online forms | 🔴 OAuth | ✅ | ⚠️ |
| [SurveyMonkey](https://developer.surveymonkey.com/) | Survey platform | 🔴 OAuth | ✅ | ⚠️ |
| [Qualtrics](https://api.qualtrics.com/) | Experience management | 🟡 API Key | ✅ | ✅ |
| [UserVoice](https://developer.uservoice.com/) | User feedback | 🟡 API Key | ✅ | ✅ |
| [Canny](https://developers.canny.io/) | Product feedback | 🟡 API Key | ✅ | ✅⭐ |
| [Nolt](https://nolt.io/api) | Feedback boards | 🟡 API Key | ✅ | ✅ |
| [Fider](https://getfider.com/docs/api) | Feedback platform | 🟡 API Key | ✅ | ✅⭐ |
| [Feedier](https://feedier.com/api/) | Feedback management | 🟡 API Key | ✅ | ✅ |
| [GetFeedback](https://developer.getfeedback.com/) | CX platform | 🟡 API Key | ✅ | ✅ |
| [Delighted](https://app.delighted.com/docs/api) | Customer feedback | 🟡 API Key | ✅ | ✅⭐ |

### Product Tours & Onboarding
| [Appcues](https://docs.appcues.com/api/) | User onboarding | 🟡 API Key | ✅ | ✅⭐ |
| [Pendo](https://developers.pendo.io/) | Product experience | 🟡 API Key | ✅ | ✅⭐ |
| [WalkMe](https://developers.walkme.com/) | Digital adoption | 🟡 API Key | ✅ | ✅ |
| [Userpilot](https://docs.userpilot.com/api/) | User onboarding | 🟡 API Key | ✅ | ✅ |
| [Chameleon](https://developers.chameleon.io/) | Product tours | 🟡 API Key | ✅ | ✅⭐ |
| [Inline Manual](https://docs.inlinemanual.com/api) | User guidance | 🟡 API Key | ✅ | ✅ |
| [Userflow](https://userflow.com/docs/api) | In-app guides | 🟡 API Key | ✅ | ✅ |
| [Product Fruits](https://productfruits.com/api) | Product adoption | 🟡 API Key | ✅ | ✅ |
| [Helppier](https://helppier.com/api/) | Interactive guides | 🟡 API Key | ✅ | ✅ |
| [Shepherd](https://shepherdjs.dev/) | Tour library | 🟢 No | ✅ | ✅⭐ |

### Knowledge Base & Documentation
| [ReadMe](https://docs.readme.com/main/reference) | API documentation | 🟡 API Key | ✅ | ✅⭐ |
| [GitBook](https://developer.gitbook.com/) | Documentation platform | 🟡 API Key | ✅ | ✅⭐ |
| [Docusaurus](https://docusaurus.io/) | Documentation website | 🟢 No | ✅ | ✅⭐ |
| [MkDocs](https://www.mkdocs.org/) | Documentation generator | 🟢 No | ✅ | ✅⭐ |
| [Sphinx](https://www.sphinx-doc.org/) | Documentation generator | 🟢 No | ✅ | ✅⭐ |
| [Confluence](https://developer.atlassian.com/cloud/confluence/rest/) | Wiki software | 🔴 OAuth | ✅ | ⚠️ |
| [Notion](https://developers.notion.com/) | Knowledge base | 🔴 OAuth | ✅ | ⚠️ |
| [Document360](https://apidocs.document360.io/) | Knowledge base | 🟡 API Key | ✅ | ✅ |
| [HelpDocs](https://helpdocs.io/api) | Knowledge base | 🟡 API Key | ✅ | ✅ |
| [Helpjuice](https://helpjuice.com/api) | Knowledge base | 🟡 API Key | ✅ | ✅ |

### Live Chat & Support Widgets
| [Intercom](https://developers.intercom.com/) | Customer messaging | 🟡 API Key | ✅ | ✅⭐ |
| [Drift](https://devdocs.drift.com/) | Conversational marketing | 🟡 API Key | ✅ | ✅ |
| [LiveChat](https://developers.livechat.com/) | Live chat software | 🟡 API Key | ✅ | ✅⭐ |
| [Zendesk Chat](https://developer.zendesk.com/api-reference/live-chat/introduction/) | Live chat | 🟡 API Key | ✅ | ✅ |
| [Olark](https://www.olark.com/help/api) | Live chat | 🟡 API Key | ✅ | ✅ |
| [Tidio](https://www.tidio.com/docs/developer/) | Live chat | 🟡 API Key | ✅ | ✅ |
| [Tawk.to](https://developer.tawk.to/) | Free live chat | 🟡 API Key | ✅ | ✅⭐ |
| [Crisp](https://docs.crisp.chat/api/v1/) | Customer messaging | 🟡 API Key | ✅ | ✅⭐ |
| [Chatwoot](https://www.chatwoot.com/developers) | Open source support | 🟡 API Key | ✅ | ✅⭐ |
| [Papercups](https://docs.papercups.io/) | Customer messaging | 🟡 API Key | ✅ | ✅⭐ |

### Chatbots & Conversational AI
| [Dialogflow](https://cloud.google.com/dialogflow/docs) | Conversational AI | 🟡 API Key | ✅ | ✅⭐ |
| [Watson Assistant](https://cloud.ibm.com/apidocs/assistant/assistant-v2) | AI assistant | 🟡 API Key | ✅ | ✅⭐ |
| [Rasa](https://rasa.com/docs/rasa/http-api/) | Open source chatbot | 🟢 No | ✅ | ✅⭐ |
| [Botpress](https://botpress.com/docs/developers) | Chatbot platform | 🟢 No | ✅ | ✅⭐ |
| [ManyChat](https://manychat.github.io/dynamic_block_docs/) | Chat marketing | 🟡 API Key | ✅ | ✅ |
| [Chatfuel](https://docs.chatfuel.com/) | Bot builder | 🟡 API Key | ✅ | ✅ |
| [Landbot](https://developers.landbot.io/) | No-code chatbots | 🟡 API Key | ✅ | ✅ |
| [Collect.chat](https://collect.chat/api) | Conversational forms | 🟡 API Key | ✅ | ✅ |
| [Botsify](https://docs.botsify.com/) | Chatbot platform | 🟡 API Key | ✅ | ✅ |
| [Flow XO](https://flowxo.com/developers) | Bot building | 🟡 API Key | ✅ | ✅ |

### Voice & Speech APIs
| [Google Text-to-Speech](https://cloud.google.com/text-to-speech) | TTS service | 🟡 API Key | ✅ | ✅⭐ |
| [Amazon Polly](https://docs.aws.amazon.com/polly/) | Text to speech | 🟡 API Key | ✅ | ✅⭐ |
| [Microsoft Azure Speech](https://azure.microsoft.com/en-us/products/cognitive-services/speech-services) | Speech services | 🟡 API Key | ✅ | ✅⭐ |
| [ElevenLabs](https://elevenlabs.io/docs) | AI voice generation | 🟡 API Key | ✅ | ✅⭐ |
| [Play.ht](https://docs.play.ht/) | Text to speech | 🟡 API Key | ✅ | ✅⭐ |
| [Resemble.ai](https://www.resemble.ai/docs/) | Voice cloning | 🟡 API Key | ✅ | ✅⭐ |
| [Murf.ai](https://murf.ai/api) | AI voice generator | 🟡 API Key | ✅ | ✅ |
| [WellSaid Labs](https://wellsaidlabs.com/api/) | AI voice over | 🟡 API Key | ✅ | ✅ |
| [Deepgram](https://developers.deepgram.com/) | Speech recognition | 🟡 API Key | ✅ | ✅⭐ |
| [AssemblyAI](https://www.assemblyai.com/docs) | Speech-to-text | 🟡 API Key | ✅ | ✅⭐ |

### SMS & Messaging Platforms
| [Twilio](https://www.twilio.com/docs) | Communications API | 🟡 API Key | ✅ | ✅⭐ |
| [Vonage (Nexmo)](https://developer.vonage.com/) | Communications APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Plivo](https://www.plivo.com/docs/) | Cloud communications | 🟡 API Key | ✅ | ✅⭐ |
| [MessageBird](https://developers.messagebird.com/) | Omnichannel platform | 🟡 API Key | ✅ | ✅⭐ |
| [Sinch](https://developers.sinch.com/) | Customer communications | 🟡 API Key | ✅ | ✅ |
| [Bandwidth](https://dev.bandwidth.com/) | Communications API | 🟡 API Key | ✅ | ✅ |
| [Telnyx](https://developers.telnyx.com/) | Communications platform | 🟡 API Key | ✅ | ✅⭐ |
| [SignalWire](https://developer.signalwire.com/) | Cloud communications | 🟡 API Key | ✅ | ✅ |
| [Infobip](https://www.infobip.com/developers) | Omnichannel communications | 🟡 API Key | ✅ | ✅ |
| [TextMagic](https://www.textmagic.com/docs/api/) | SMS platform | 🟡 API Key | ✅ | ✅ |

### Push Notifications
| [OneSignal](https://documentation.onesignal.com/reference) | Push notifications | 🟡 API Key | ✅ | ✅⭐ |
| [Pushwoosh](https://docs.pushwoosh.com/) | Push messaging | 🟡 API Key | ✅ | ✅ |
| [Airship](https://docs.airship.com/) | Mobile engagement | 🟡 API Key | ✅ | ✅ |
| [Pusher Beams](https://pusher.com/docs/beams/) | Push notifications | 🟡 API Key | ✅ | ✅⭐ |
| [Batch](https://batch.com/doc/api/) | Mobile engagement | 🟡 API Key | ✅ | ✅ |
| [Pushover](https://pushover.net/api) | Push notifications | 🟡 API Key | ✅ | ✅⭐ |
| [Pushy](https://pushy.me/docs/api/api) | Push notifications | 🟡 API Key | ✅ | ✅ |
| [ntfy](https://ntfy.sh/) | Simple push notifications | 🟢 No | ✅ | ✅⭐ |
| [Pushbullet](https://docs.pushbullet.com/) | Push notifications | 🟡 API Key | ✅ | ✅ |
| [Prowl](https://www.prowlapp.com/api.php) | iOS push | 🟡 API Key | ✅ | ✅ |

### Geolocation & Maps
| [Google Maps](https://developers.google.com/maps) | Maps platform | 🟡 API Key | ✅ | ✅⭐ |
| [Mapbox](https://docs.mapbox.com/api/overview/) | Location data | 🟡 API Key | ✅ | ✅⭐ |
| [HERE Maps](https://developer.here.com/) | Location services | 🟡 API Key | ✅ | ✅⭐ |
| [TomTom](https://developer.tomtom.com/) | Maps & traffic | 🟡 API Key | ✅ | ✅ |
| [OpenStreetMap](https://wiki.openstreetmap.org/wiki/API) | Open map data | 🟢 No | ✅ | ✅⭐ |
| [Nominatim](https://nominatim.org/release-docs/latest/api/Overview/) | OSM geocoding | 🟢 No | ✅ | ✅⭐ |
| [LocationIQ](https://locationiq.com/docs) | Geocoding API | 🟡 API Key | ✅ | ✅⭐ |
| [Geoapify](https://www.geoapify.com/api/) | Location platform | 🟡 API Key | ✅ | ✅⭐ |
| [MapTiler](https://docs.maptiler.com/) | Map SDK | 🟡 API Key | ✅ | ✅ |
| [ArcGIS](https://developers.arcgis.com/) | GIS platform | 🟡 API Key | ✅ | ✅ |

### Routing & Navigation
| [OSRM](http://project-osrm.org/docs/v5.24.0/api/) | Routing engine | 🟢 No | ✅ | ✅⭐ |
| [Graphhopper](https://docs.graphhopper.com/) | Routing API | 🟡 API Key | ✅ | ✅⭐ |
| [Valhalla](https://valhalla.github.io/valhalla/) | Routing engine | 🟢 No | ✅ | ✅⭐ |
| [OpenRouteService](https://openrouteservice.org/dev/#/api-docs) | Routing service | 🟡 API Key | ✅ | ✅⭐ |
| [MapQuest](https://developer.mapquest.com/) | Mapping & routing | 🟡 API Key | ✅ | ✅ |
| [Bing Maps](https://www.microsoft.com/en-us/maps/choose-your-bing-maps-api) | Maps APIs | 🟡 API Key | ✅ | ✅ |
| [Targomo](https://docs.targomo.com/) | Location intelligence | 🟡 API Key | ✅ | ✅ |
| [TravelTime](https://docs.traveltime.com/api/overview/introduction) | Travel time API | 🟡 API Key | ✅ | ✅⭐ |
| [Distancematrix.ai](https://distancematrix.ai/dev) | Distance calculation | 🟡 API Key | ✅ | ✅ |
| [Route4Me](https://route4me.io/docs/) | Route optimization | 🟡 API Key | ✅ | ✅ |

### QR Codes & Barcodes
| [QR Code Generator](https://goqr.me/api/) | QR code API | 🟢 No | ✅ | ✅⭐ |
| [QRServer](https://quickchart.io/qr-code-api/) | QR code generation | 🟢 No | ✅ | ✅⭐ |
| [QR Code Monkey](https://www.qrcode-monkey.com/qr-code-api/) | Custom QR codes | 🟢 No | ✅ | ✅ |
| [Scanova](https://scanova.io/api/) | QR code API | 🟡 API Key | ✅ | ✅ |
| [Beaconstac](https://www.beaconstac.com/api) | QR code platform | 🟡 API Key | ✅ | ✅ |
| [Barcode Lookup](https://www.barcodelookup.com/api) | Product barcode database | 🟡 API Key | ✅ | ✅⭐ |
| [UPCitemdb](https://www.upcitemdb.com/api) | UPC database | 🟡 API Key | ✅ | ✅⭐ |
| [Zxing](https://github.com/zxing/zxing) | Barcode scanner | 🟢 No | ✅ | ✅⭐ |
| [Dynamsoft](https://www.dynamsoft.com/barcode-reader/sdk-javascript/) | Barcode SDK | 🟡 API Key | ✅ | ✅ |
| [Scandit](https://docs.scandit.com/) | Barcode scanning | 🟡 API Key | ✅ | ✅ |

### Fraud Detection & Identity Verification
| [Stripe Radar](https://stripe.com/docs/radar) | Fraud prevention | 🟡 API Key | ✅ | ✅⭐ |
| [Sift](https://developers.sift.com/) | Fraud detection | 🟡 API Key | ✅ | ✅⭐ |
| [Plaid Identity](https://plaid.com/docs/identity/) | Identity verification | 🟡 API Key | ✅ | ✅⭐ |
| [Onfido](https://documentation.onfido.com/) | Identity verification | 🟡 API Key | ✅ | ✅⭐ |
| [Jumio](https://www.jumio.com/developers/) | ID verification | 🟡 API Key | ✅ | ✅ |
| [Trulioo](https://developer.trulioo.com/) | Global identity | 🟡 API Key | ✅ | ✅ |
| [Persona](https://docs.withpersona.com/) | Identity infrastructure | 🟡 API Key | ✅ | ✅⭐ |
| [Socure](https://developer.socure.com/) | Identity verification | 🟡 API Key | ✅ | ✅ |
| [Alloy](https://docs.alloy.com/) | Identity decisioning | 🟡 API Key | ✅ | ✅ |
| [Sumsub](https://developers.sumsub.com/) | KYC platform | 🟡 API Key | ✅ | ✅ |

### Video Conferencing & WebRTC
| [Zoom](https://marketplace.zoom.us/docs/api-reference/introduction) | Video meetings | 🔴 OAuth | ✅ | ⚠️ |
| [Twilio Video](https://www.twilio.com/docs/video) | Video API | 🟡 API Key | ✅ | ✅⭐ |
| [Vonage Video](https://tokbox.com/developer/) | Video platform | 🟡 API Key | ✅ | ✅⭐ |
| [Agora](https://docs.agora.io/en) | Real-time engagement | 🟡 API Key | ✅ | ✅⭐ |
| [Daily.co](https://docs.daily.co/) | Video calling | 🟡 API Key | ✅ | ✅⭐ |
| [Whereby](https://whereby.dev/) | Video meetings | 🟡 API Key | ✅ | ✅⭐ |
| [Jitsi](https://jitsi.github.io/handbook/docs/dev-guide/dev-guide-iframe) | Open source video | 🟢 No | ✅ | ✅⭐ |
| [100ms](https://www.100ms.live/docs/api-reference/overview) | Live video SDK | 🟡 API Key | ✅ | ✅⭐ |
| [Dyte](https://docs.dyte.io/) | Video SDK | 🟡 API Key | ✅ | ✅⭐ |
| [LiveKit](https://docs.livekit.io/) | Real-time video/audio | 🟡 API Key | ✅ | ✅⭐ |

### Appointment Scheduling
| [Calendly](https://developer.calendly.com/) | Scheduling automation | 🔴 OAuth | ✅ | ⚠️ |
| [Cal.com](https://cal.com/docs/introduction) | Open source scheduling | 🟡 API Key | ✅ | ✅⭐ |
| [Acuity Scheduling](https://developers.acuityscheduling.com/) | Appointment booking | 🟡 API Key | ✅ | ✅ |
| [SimplyBook](https://simplybook.me/en/api/doc) | Booking software | 🟡 API Key | ✅ | ✅ |
| [Setmore](https://developer.setmore.com/) | Free scheduling | 🟡 API Key | ✅ | ✅ |
| [Appointy](https://www.appointy.com/api) | Scheduling software | 🟡 API Key | ✅ | ✅ |
| [10to8](https://10to8.com/api/overview/) | Appointment scheduling | 🟡 API Key | ✅ | ✅ |
| [Timekit](https://developers.timekit.io/) | Scheduling API | 🟡 API Key | ✅ | ✅ |
| [ScheduleOnce](https://developers.scheduleonce.com/) | Meeting scheduler | 🟡 API Key | ✅ | ✅ |
| [YouCanBookMe](https://gb.youcanbook.me/docs/api/) | Online scheduling | 🟡 API Key | ✅ | ✅ |

### Bookkeeping & Invoicing
| [QuickBooks](https://developer.intuit.com/app/developer/qbo/docs/api/accounting/most-commonly-used/invoice) | Accounting | 🔴 OAuth | ✅ | ⚠️ |
| [Xero](https://developer.xero.com/documentation/api/accounting/overview) | Accounting platform | 🔴 OAuth | ✅ | ⚠️ |
| [FreshBooks](https://www.freshbooks.com/api/start) | Invoicing | 🔴 OAuth | ✅ | ⚠️ |
| [Wave Accounting](https://developer.waveapps.com/hc/en-us/articles/360019968212) | Free accounting | 🔴 OAuth | ✅ | ⚠️ |
| [Invoice Ninja](https://api-docs.invoicing.co/) | Invoicing platform | 🟡 API Key | ✅ | ✅⭐ |
| [Zoho Invoice](https://www.zoho.com/invoice/api/v3/) | Invoicing software | 🔴 OAuth | ✅ | ⚠️ |
| [PayPal Invoicing](https://developer.paypal.com/docs/invoicing/) | Send invoices | 🔴 OAuth | ✅ | ⚠️ |
| [Square Invoices](https://developer.squareup.com/docs/invoices-api/overview) | Invoice API | 🔴 OAuth | ✅ | ⚠️ |
| [Stripe Invoicing](https://stripe.com/docs/invoicing) | Billing | 🟡 API Key | ✅ | ✅⭐ |
| [Chargebee](https://apidocs.chargebee.com/docs/api) | Subscription billing | 🟡 API Key | ✅ | ✅⭐ |

### Subscription Management
| [Stripe Billing](https://stripe.com/docs/billing) | Subscription billing | 🟡 API Key | ✅ | ✅⭐ |
| [Chargebee](https://apidocs.chargebee.com/) | Subscription management | 🟡 API Key | ✅ | ✅⭐ |
| [Recurly](https://developers.recurly.com/) | Subscription platform | 🟡 API Key | ✅ | ✅⭐ |
| [Paddle](https://developer.paddle.com/) | Billing platform | 🟡 API Key | ✅ | ✅⭐ |
| [FastSpring](https://fastspring.com/docs/api/) | E-commerce platform | 🟡 API Key | ✅ | ✅ |
| [2Checkout](https://www.2checkout.com/documentation/api/) | Payment platform | 🟡 API Key | ✅ | ✅ |
| [Chargify](https://developers.chargify.com/) | Billing software | 🟡 API Key | ✅ | ✅ |
| [Zuora](https://www.zuora.com/developer/api-reference/) | Subscription economy | 🟡 API Key | ✅ | ✅ |
| [Rebilly](https://api-reference.rebilly.com/) | Subscription billing | 🟡 API Key | ✅ | ✅ |
| [Billsby](https://support.billsby.com/api/) | Subscription billing | 🟡 API Key | ✅ | ✅ |

### Expense Management
| [Expensify](https://integrations.expensify.com/Integration-Server/doc/) | Expense reports | 🟡 API Key | ✅ | ✅⭐ |
| [Concur](https://developer.concur.com/) | Travel & expense | 🔴 OAuth | ✅ | ⚠️ |
| [Rydoo](https://developers.rydoo.com/) | Expense management | 🟡 API Key | ✅ | ✅ |
| [Zoho Expense](https://www.zoho.com/expense/api/v1/) | Expense tracking | 🔴 OAuth | ✅ | ⚠️ |
| [Divvy](https://developer.divvy.co/) | Expense management | 🟡 API Key | ✅ | ✅ |
| [Emburse](https://www.emburse.com/developers/) | Expense automation | 🟡 API Key | ✅ | ✅ |
| [Fyle](https://docs.fylehq.com/docs) | Expense management | 🟡 API Key | ✅ | ✅ |
| [Receipt Bank](https://support.receipt-bank.com/hc/en-us/articles/360002539558-API) | Receipt capture | 🟡 API Key | ✅ | ✅ |
| [Shoeboxed](https://www.shoeboxed.com/api/) | Receipt scanning | 🟡 API Key | ✅ | ✅ |
| [Veryfi](https://www.veryfi.com/api/) | Receipt OCR | 🟡 API Key | ✅ | ✅⭐ |

### Compliance & Regulatory
| [ComplyAdvantage](https://docs.complyadvantage.com/) | Financial crime detection | 🟡 API Key | ✅ | ✅ |
| [Refinitiv](https://developers.refinitiv.com/) | Financial data | 🟡 API Key | ✅ | ✅ |
| [LexisNexis Risk](https://risk.lexisnexis.com/developers) | Risk solutions | 🟡 API Key | ✅ | ✅ |
| [Accuity](https://www.accuity.com/products/apis/) | Compliance solutions | 🟡 API Key | ✅ | ✅ |
| [Dow Jones Risk](https://developer.dowjones.com/) | Risk & compliance | 🟡 API Key | ✅ | ✅ |
| [OFAC Sanctions](https://ofac-api.com/) | Sanctions screening | 🟢 No | ✅ | ✅⭐ |
| [World-Check](https://risk.thomsonreuters.com/en/products/world-check-kyc-screening.html) | Risk intelligence | 🟡 API Key | ✅ | ✅ |
| [Creditsafe](https://www.creditsafe.com/gb/en/product/our-data/rest-api.html) | Business credit | 🟡 API Key | ✅ | ✅ |
| [Dun & Bradstreet](https://directplus.documentation.dnb.com/) | Business data | 🟡 API Key | ✅ | ✅ |
| [Equifax](https://developer.equifax.com/products) | Credit data | 🟡 API Key | ✅ | ✅ |

### Miscellaneous Utilities
| [Random.org](https://www.random.org/clients/http/) | True random numbers | 🟢 No | ✅ | ✅⭐ |
| [Lorem Picsum](https://picsum.photos/) | Random images | 🟢 No | ✅ | ✅⭐ |
| [PlaceIMG](https://placeimg.com/) | Placeholder images | 🟢 No | No | ✅ |
| [UI Faces](https://uifaces.co/api) | User avatars | 🟡 API Key | ✅ | ✅ |
| [This X Does Not Exist](https://thisxdoesnotexist.com/) | AI generated content | 🟢 No | ✅ | ✅ |
| [JSON Placeholder](https://jsonplaceholder.typicode.com/) | Fake API | 🟢 No | ✅ | ✅⭐ |
| [ReqRes](https://reqres.in/) | Test REST API | 🟢 No | ✅ | ✅⭐ |
| [Mockaroo](https://www.mockaroo.com/api/docs) | Test data generator | 🟡 API Key | ✅ | ✅⭐ |
| [IFTTT](https://platform.ifttt.com/docs) | Automation platform | 🟡 API Key | ✅ | ✅⭐ |
| [Webhooks.site](https://webhooks.site/) | Test webhooks | 🟢 No | ✅ | ✅⭐ |
