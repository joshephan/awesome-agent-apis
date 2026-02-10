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
- [Accounting & Bookkeeping APIs](#-accounting--bookkeeping-apis)
- [Anti-Fraud & Risk Management APIs](#️-anti-fraud--risk-management-apis)
- [Aviation & Flight Data APIs](#️-aviation--flight-data-apis)
- [Banking & Open Banking APIs](#-banking--open-banking-apis)
- [Conversational AI & Chatbot APIs](#-conversational-ai--chatbot-apis)
- [Pharmacy & Drug Database APIs](#-pharmacy--drug-database-apis)
- [Game Development & Engine APIs](#-game-development--engine-apis)
- [Genomics & Genetic Testing APIs](#-genomics--genetic-testing-apis)
- [Business Intelligence & Analytics APIs](#-business-intelligence--analytics-apis)
- [ETL & Data Pipeline APIs](#-etl--data-pipeline-apis)
- [Telemedicine & Telehealth APIs](#-telemedicine--telehealth-apis)
- [ERP & Enterprise Resource Planning APIs](#-erp--enterprise-resource-planning-apis)
- [Expense Management APIs](#-expense-management-apis)
- [Facial Recognition & Biometric APIs](#-facial-recognition--biometric-apis)
- [Influencer Marketing APIs](#-influencer-marketing-apis)
- [Inventory Management APIs](#-inventory-management-apis)
- [Investment & Portfolio Management APIs](#-investment--portfolio-management-apis)
- [IT Service Management (ITSM) APIs](#-it-service-management-itsm-apis)
- [Last Mile Delivery APIs](#-last-mile-delivery-apis)
- [Lending & Loan APIs](#-lending--loan-apis)
- [Knowledge Base & Wiki APIs](#-knowledge-base--wiki-apis)
- [Lead Generation & Enrichment APIs](#-lead-generation--enrichment-apis)
- [Marketplace & E-commerce Platform APIs](#-marketplace--e-commerce-platform-apis)
- [Media Encoding & Transcoding APIs](#-media-encoding--transcoding-apis)
- [Mental Health & Wellness APIs](#-mental-health--wellness-apis)
- [Metaverse & Virtual Reality APIs](#-metaverse--virtual-reality-apis)
- [Mining & Natural Resources APIs](#️-mining--natural-resources-apis)
- [Package Tracking & Shipment APIs](#-package-tracking--shipment-apis)
- [Parking & Mobility APIs](#️-parking--mobility-apis)
- [PDF Generation & Manipulation APIs](#-pdf-generation--manipulation-apis)
- [Predictive Analytics & ML Ops APIs](#-predictive-analytics--ml-ops-apis)
- [Pricing & Revenue Optimization APIs](#-pricing--revenue-optimization-apis)
- [Property Management APIs](#️-property-management-apis)
- [Privacy & Data Protection APIs](#-privacy--data-protection-apis)
- [Public Speaking & Presentation APIs](#️-public-speaking--presentation-apis)
- [Robotic Process Automation (RPA) APIs](#-robotic-process-automation-rpa-apis)
- [Satellite & Remote Sensing APIs](#️-satellite--remote-sensing-apis)
- [SEO & Web Analytics APIs](#-seo--web-analytics-apis)
- [Sound & Audio Processing APIs](#-sound--audio-processing-apis)
- [Student Information System APIs](#-student-information-system-apis)
- [API Gateway & Management APIs](#-api-gateway--management-apis)
- [Design & Prototyping APIs](#-design--prototyping-apis)
- [IoT Platform & Device Management APIs](#-iot-platform--device-management-apis)
- [Telecommunications APIs](#-telecommunications-apis)
- [Fitness & Gym APIs](#️-fitness--gym-apis)
- [Newsletter & Content APIs](#-newsletter--content-apis)
- [Event & Conference APIs](#-event--conference-apis)
- [Laboratory & LIMS APIs](#-laboratory--lims-apis)
- [Hospitality & Hotel Management APIs](#-hospitality--hotel-management-apis)
- [Automotive & Vehicle APIs](#-automotive--vehicle-apis)
- [Ticketing & Venue APIs](#-ticketing--venue-apis)
- [Grocery & Food Delivery APIs](#-grocery--food-delivery-apis)
- [Accounting Tax Compliance APIs](#-accounting-tax-compliance-apis)
- [Contact Center & CCaaS APIs](#-contact-center--ccaas-apis)
- [BIM & Architecture APIs](#️-bim--architecture-apis)
- [Online Learning Platform APIs](#-online-learning-platform-apis)
- [Luxury & Fashion APIs](#-luxury--fashion-apis)
- [Sports Data & Odds APIs](#️-sports-data--odds-apis)
- [Cannabis & CBD APIs](#-cannabis--cbd-apis)
- [Battery & Energy Storage APIs](#-battery--energy-storage-apis)
- [Casino & iGaming APIs](#-casino--igaming-apis)
- [Computer Vision & Object Detection APIs](#-computer-vision--object-detection-apis)
- [Cold Chain & Temperature Monitoring APIs](#-cold-chain--temperature-monitoring-apis)
- [Museum & Cultural Heritage APIs](#️-museum--cultural-heritage-apis)
- [Encryption & Key Management APIs](#-encryption--key-management-apis)
- [Electronic Health Records (EHR) APIs](#-electronic-health-records-ehr-apis)
- [Data Catalog & Metadata APIs](#-data-catalog--metadata-apis)
- [Data Quality & Cleansing APIs](#-data-quality--cleansing-apis)
- [Low-Code & No-Code Platform APIs](#️-low-code--no-code-platform-apis)
- [Text-to-Speech (TTS) APIs](#-text-to-speech-tts-apis)
- [App Store & Mobile Analytics APIs](#-app-store--mobile-analytics-apis)
- [Coworking & Office Space APIs](#-coworking--office-space-apis)
- [A/B Testing & Experimentation APIs](#-ab-testing--experimentation-apis)
- [URL & Link Management APIs](#-url--link-management-apis)
- [Container & Kubernetes APIs](#-container--kubernetes-apis)
- [Stock Market & Trading APIs](#-stock-market--trading-apis)
- [Music Streaming & Licensing APIs](#-music-streaming--licensing-apis)
- [Barcode & Product Lookup APIs](#️-barcode--product-lookup-apis)
- [Data Sync & Replication APIs](#-data-sync--replication-apis)
- [Environmental Monitoring APIs](#️-environmental-monitoring-apis)
- [Advertising & Ad Tech APIs](#-advertising--ad-tech-apis)
- [Medical Imaging APIs](#-medical-imaging-apis)
- [Bioinformatics & Protein APIs](#-bioinformatics--protein-apis)
- [Random Data & Generator APIs](#-random-data--generator-apis)
- [Serverless & FaaS APIs](#️-serverless--faas-apis)
- [CAD & 3D Modeling APIs](#-cad--3d-modeling-apis)
- [Ocean & Marine Data APIs](#-ocean--marine-data-apis)
- [Brain-Computer Interface APIs](#-brain-computer-interface-apis)
- [Wine & Beverage APIs](#-wine--beverage-apis)
- [Print & Publishing APIs](#-print--publishing-apis)
- [Library & Archival APIs](#-library--archival-apis)
- [Childcare & Parenting APIs](#-childcare--parenting-apis)
- [Veterinary & Animal Health APIs](#-veterinary--animal-health-apis)
- [Jewelry & Gemstone APIs](#-jewelry--gemstone-apis)
- [Moving & Relocation APIs](#-moving--relocation-apis)
- [Funeral & Memorial APIs](#️-funeral--memorial-apis)
- [Pest Control & Extermination APIs](#-pest-control--extermination-apis)
- [Cleaning & Janitorial APIs](#-cleaning--janitorial-apis)
- [Landscaping & Garden APIs](#-landscaping--garden-apis)
- [Home Improvement & DIY APIs](#-home-improvement--diy-apis)
- [Antiques & Collectibles APIs](#-antiques--collectibles-apis)
- [Astrology & Horoscope APIs](#-astrology--horoscope-apis)
- [Fishing & Hunting APIs](#-fishing--hunting-apis)
- [Camping & Outdoor Recreation APIs](#-camping--outdoor-recreation-apis)
- [Mortgage & Home Loan APIs](#-mortgage--home-loan-apis)
- [Network Monitoring & SNMP APIs](#-network-monitoring--snmp-apis)
- [Procurement & Sourcing APIs](#-procurement--sourcing-apis)
- [Public Records & FOIA APIs](#-public-records--foia-apis)
- [Queue & Task Management APIs](#-queue--task-management-apis)
- [Robotics & Drone APIs](#-robotics--drone-apis)
- [Sales Intelligence & Enablement APIs](#-sales-intelligence--enablement-apis)
- [Social Listening & Brand Monitoring APIs](#-social-listening--brand-monitoring-apis)
- [Talent & Workforce Management APIs](#-talent--workforce-management-apis)
- [Virtual Events & Webinar APIs](#-virtual-events--webinar-apis)
- [Waste & Recycling Management APIs](#️-waste--recycling-management-apis)
- [Water Quality & Utility APIs](#-water-quality--utility-apis)
- [Wedding & Event Planning APIs](#-wedding--event-planning-apis)
- [WiFi & Network Analytics APIs](#-wifi--network-analytics-apis)
- [Dynamic Pricing & Revenue Management APIs](#-dynamic-pricing--revenue-management-apis)
- [Customer Data Platform (CDP) APIs](#-customer-data-platform-cdp-apis)
- [Consent & Privacy Management APIs](#-consent--privacy-management-apis)
- [Employee Engagement & Culture APIs](#-employee-engagement--culture-apis)
- [Digital Twin & Simulation APIs](#-digital-twin--simulation-apis)
- [Edge Computing & CDN APIs](#-edge-computing--cdn-apis)
- [AIOps & IT Operations APIs](#-aiops--it-operations-apis)
- [Unified Communications (UCaaS) APIs](#-unified-communications-ucaas-apis)
- [Visual Search & Image Recognition APIs](#️-visual-search--image-recognition-apis)
- [Customer Success & Retention APIs](#-customer-success--retention-apis)
- [Revenue Operations & Intelligence APIs](#-revenue-operations--intelligence-apis)
- [Data Governance & Lineage APIs](#-data-governance--lineage-apis)
- [Service Mesh & API Gateway APIs](#-service-mesh--api-gateway-apis)
- [Web Performance & Core Web Vitals APIs](#-web-performance--core-web-vitals-apis)
- [Voice Assistant & Smart Speaker APIs](#️-voice-assistant--smart-speaker-apis)
- [Process Mining & Analytics APIs](#️-process-mining--analytics-apis)
- [Industrial IoT & SCADA APIs](#-industrial-iot--scada-apis)
- [Forestry & Natural Resources APIs](#-forestry--natural-resources-apis)
- [Affiliate Marketing & Partner APIs](#-affiliate-marketing--partner-apis)
- [Augmented Reality & AR Cloud APIs](#-augmented-reality--ar-cloud-apis)
- [Backup & Disaster Recovery APIs](#-backup--disaster-recovery-apis)
- [Browser Extension & Web Automation APIs](#-browser-extension--web-automation-apis)
- [Cloud Cost Management & FinOps APIs](#-cloud-cost-management--finops-apis)
- [Crowdfunding & Fundraising APIs](#-crowdfunding--fundraising-apis)
- [Cryptocurrency Exchange APIs](#-cryptocurrency-exchange-apis)
- [Data Anonymization & Synthetic Data APIs](#-data-anonymization--synthetic-data-apis)
- [DevSecOps & Security Scanning APIs](#️-devsecops--security-scanning-apis)
- [Electric Vehicle Charging APIs](#-electric-vehicle-charging-apis)
- [Employee Benefits & Perks APIs](#-employee-benefits--perks-apis)
- [Enterprise Search APIs](#-enterprise-search-apis)
- [Facility Management & Workplace APIs](#-facility-management--workplace-apis)
- [Fashion & Apparel APIs](#-fashion--apparel-apis)
- [Gift Card & Voucher APIs](#-gift-card--voucher-apis)
- [Government Grant & Funding APIs](#️-government-grant--funding-apis)
- [Healthcare Claims & Billing APIs](#-healthcare-claims--billing-apis)
- [Identity Access Management (IAM) APIs](#-identity-access-management-iam-apis)
- [Influencer & Creator Economy APIs](#-influencer--creator-economy-apis)
- [Climate Risk & ESG Scoring APIs](#-climate-risk--esg-scoring-apis)
- [Community & Forum Platform APIs](#-community--forum-platform-apis)
- [Content Marketing & SEO Content APIs](#-content-marketing--seo-content-apis)
- [Credential & Digital Badge APIs](#-credential--digital-badge-apis)
- [Customer Feedback & NPS APIs](#-customer-feedback--nps-apis)
- [Data Room & Virtual Due Diligence APIs](#-data-room--virtual-due-diligence-apis)
- [Debt Collection & Recovery APIs](#-debt-collection--recovery-apis)
- [Document Generation & Template APIs](#-document-generation--template-apis)
- [E-Learning & LMS APIs](#-e-learning--lms-apis)
- [Fan Engagement & Sports Tech APIs](#-fan-engagement--sports-tech-apis)
- [Food Safety & Inspection APIs](#-food-safety--inspection-apis)
- [Franchise Management APIs](#-franchise-management-apis)
- [Geospatial Intelligence & GIS APIs](#-geospatial-intelligence--gis-apis)
- [Ticketing & Support Queue APIs](#-ticketing--support-queue-apis)
- [Subscription Box & Commerce APIs](#-subscription-box--commerce-apis)
- [Podcast Analytics & Monetization APIs](#-podcast-analytics--monetization-apis)
- [Password & Credential Management APIs](#-password--credential-management-apis)
- [Notification & Alert Orchestration APIs](#-notification--alert-orchestration-apis)
- [Music Rights & Royalty APIs](#-music-rights--royalty-apis)
- [Mobile Device Management (MDM) APIs](#-mobile-device-management-mdm-apis)
- [Logistics & Freight Brokerage APIs](#-logistics--freight-brokerage-apis)
- [Knowledge Graph & Ontology APIs](#-knowledge-graph--ontology-apis)
- [Insurance Claims Processing APIs](#-insurance-claims-processing-apis)
- [Healthcare Interoperability (HL7/FHIR) APIs](#-healthcare-interoperability-hl7fhir-apis)
- [Green Energy & Carbon Offset APIs](#-green-energy--carbon-offset-apis)
- [Gamification & Rewards APIs](#-gamification--rewards-apis)
- [Food Ordering & Menu APIs](#-food-ordering--menu-apis)
- [Digital Wallet & Mobile Payment APIs](#-digital-wallet--mobile-payment-apis)
- [Church & Nonprofit Management APIs](#-church--nonprofit-management-apis)
- [Appointment Scheduling & Booking APIs](#-appointment-scheduling--booking-apis)
- [Background Check & Screening APIs](#-background-check--screening-apis)
- [Business Intelligence & Analytics APIs](#-business-intelligence--analytics-apis)
- [Calendar & Time Management APIs](#-calendar--time-management-apis)
- [Chat & Messaging Platform APIs](#-chat--messaging-platform-apis)
- [Cloud Storage & File Management APIs](#-cloud-storage--file-management-apis)
- [Code Repository & Version Control APIs](#-code-repository--version-control-apis)
- [Compliance & Regulatory APIs](#-compliance--regulatory-apis)
- [Contract Management & CLM APIs](#-contract-management--clm-apis)
- [CRM & Sales Automation APIs](#-crm--sales-automation-apis)
- [Customer Data Platform APIs](#-customer-data-platform-apis)
- [Data Enrichment & Business Data APIs](#-data-enrichment--business-data-apis)
- [Design & Creative Tool APIs](#-design--creative-tool-apis)
- [Email Marketing & Automation APIs](#-email-marketing--automation-apis)
- [Event Management & Registration APIs](#-event-management--registration-apis)
- [Fleet Management & Telematics APIs](#-fleet-management--telematics-apis)
- [Form Builder & Survey APIs](#-form-builder--survey-apis)
- [Fraud Detection & Risk Management APIs](#-fraud-detection--risk-management-apis)
- [Help Desk & ITSM APIs](#-help-desk--itsm-apis)
- [HR & Workforce Management APIs](#-hr--workforce-management-apis)
- [Image & Video Processing APIs](#-image--video-processing-apis)
- [Invoice & Expense Management APIs](#-invoice--expense-management-apis)
- [Legal Tech & Case Management APIs](#-legal-tech--case-management-apis)
- [Localization & Translation APIs](#-localization--translation-apis)
- [Marketing Attribution & Analytics APIs](#-marketing-attribution--analytics-apis)
- [Network & Infrastructure Monitoring APIs](#-network--infrastructure-monitoring-apis)
- [No-Code & Low-Code Platform APIs](#-no-code--low-code-platform-apis)
- [OCR & Document Intelligence APIs](#-ocr--document-intelligence-apis)
- [Payroll & Tax Filing APIs](#-payroll--tax-filing-apis)
- [Product Information Management APIs](#-product-information-management-apis)
- [Project Management & Collaboration APIs](#-project-management--collaboration-apis)
- [Property & Real Estate APIs](#-property--real-estate-apis)
- [Proposal & Quote Management APIs](#-proposal--quote-management-apis)
- [Quality Assurance & Testing APIs](#-quality-assurance--testing-apis)
- [Recruitment & ATS APIs](#-recruitment--ats-apis)
- [Remote Desktop & Access APIs](#-remote-desktop--access-apis)
- [Reputation & Review Management APIs](#-reputation--review-management-apis)
- [Retail & POS APIs](#-retail--pos-apis)
- [SIEM & Security Operations APIs](#-siem--security-operations-apis)
- [Smart Home & IoT Hub APIs](#-smart-home--iot-hub-apis)
- [Social Media Management APIs](#-social-media-management-apis)
- [Speech & Voice Recognition APIs](#-speech--voice-recognition-apis)
- [Supply Chain & Procurement APIs](#-supply-chain--procurement-apis)
- [Tax Calculation & Compliance APIs](#-tax-calculation--compliance-apis)
- [Telehealth & Virtual Care APIs](#-telehealth--virtual-care-apis)
- [Time Tracking & Productivity APIs](#-time-tracking--productivity-apis)
- [Travel & Hospitality APIs](#-travel--hospitality-apis)
- [Video Conferencing & Webinar APIs](#-video-conferencing--webinar-apis)
- [Banking & Open Finance APIs](#-banking--open-finance-apis)
- [Database & Backend-as-a-Service APIs](#-database--backend-as-a-service-apis)
- [Data Visualization & BI APIs](#-data-visualization--bi-apis)
- [Cybersecurity & Threat Intelligence APIs](#-cybersecurity--threat-intelligence-apis)
- [Chatbot & Conversational AI APIs](#-chatbot--conversational-ai-apis)
- [Warehouse & Inventory Management APIs](#-warehouse--inventory-management-apis)
- [Advertising & Ad Tech APIs](#-advertising--ad-tech-apis)
- [Push Notification & In-App Messaging APIs](#-push-notification--in-app-messaging-apis)
- [Contact Center & Telephony APIs](#-contact-center--telephony-apis)
- [Bioinformatics & Life Sciences APIs](#-bioinformatics--life-sciences-apis)
- [Construction & Building APIs](#-construction--building-apis)
- [EdTech & Student Management APIs](#-edtech--student-management-apis)
- [Energy & Utilities APIs](#-energy--utilities-apis)
- [Election & Civic Data APIs](#-election--civic-data-apis)
- [Arts & Culture APIs](#-arts--culture-apis)
- [Chemistry & Material Science APIs](#-chemistry--material-science-apis)
- [Clinical Trials & Drug Data APIs](#-clinical-trials--drug-data-apis)
- [Ticketing & Events Discovery APIs](#-ticketing--events-discovery-apis)
- [Space & Astronomy APIs](#-space--astronomy-apis)
- [Ocean & Marine APIs](#-ocean--marine-apis)
- [Museum & Archive APIs](#-museum--archive-apis)
- [Research & Academic APIs](#-research--academic-apis)
- [Data Warehouse & ETL APIs](#-data-warehouse--etl-apis)
- [Knowledge Management & Wiki APIs](#-knowledge-management--wiki-apis)
- [Survey & Market Research APIs](#-survey--market-research-apis)
- [Fitness & Wellness APIs](#-fitness--wellness-apis)
- [Random & Fun APIs](#-random--fun-apis)
- [CDN & Edge Computing APIs](#-cdn--edge-computing-apis)
- [Authentication & Identity APIs](#-authentication--identity-apis)
- [CAD & 3D Modeling APIs](#-cad--3d-modeling-apis)
- [Community & HOA Management APIs](#-community--hoa-management-apis)
- [Audio & Sound APIs](#-audio--sound-apis)
- [Coworking & Space Management APIs](#-coworking--space-management-apis)
- [Jewelry & Luxury Goods APIs](#-jewelry--luxury-goods-apis)
- [Agriculture & Farming APIs](#-agriculture--farming-apis)
- [Manufacturing & Industrial IoT APIs](#-manufacturing--industrial-iot-apis)
- [Casino & Gaming Regulation APIs](#-casino--gaming-regulation-apis)
- [Cleaning & Facility Services APIs](#-cleaning--facility-services-apis)
- [Radio & Broadcast APIs](#-radio--broadcast-apis)
- [Outdoor & Adventure APIs](#-outdoor--adventure-apis)
- [Toy & Children Product APIs](#-toy--children-product-apis)
- [Battery & EV Charging APIs](#-battery--ev-charging-apis)
- [Beauty & Salon APIs](#-beauty--salon-apis)
- [Cold Chain & Temperature Monitoring APIs](#-cold-chain--temperature-monitoring-apis)
- [Certification & E-Exam APIs](#-certification--e-exam-apis)
- [Satellite & Remote Sensing APIs](#-satellite--remote-sensing-apis)
- [Wine & Spirits APIs](#-wine--spirits-apis)
- [Plumbing & HVAC APIs](#-plumbing--hvac-apis)

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

## 🏦 Accounting & Bookkeeping APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [QuickBooks Online API](https://developer.intuit.com/app/developer/qbo/docs/develop) | Full accounting API: invoices, expenses, reports, bank reconciliation | 🔴 OAuth | ✅ | ✅⭐ |
| [Xero API](https://developer.xero.com/) | Cloud accounting with contacts, invoices, bank transactions, payroll | 🔴 OAuth | ✅ | ✅⭐ |
| [FreshBooks API](https://www.freshbooks.com/api/start) | Invoicing, time tracking, expenses, and client management for freelancers | 🔴 OAuth | ✅ | ✅ |
| [Wave API](https://developer.waveapps.com/hc/en-us) | Free accounting platform API with GraphQL for invoices, payments, receipts | 🔴 OAuth | ✅ | ⚠️ |
| [Sage Intacct API](https://developer.intacct.com/) | Enterprise cloud financial management with GL, AP, AR, and reporting | 🟡 API Key | ✅ | ✅ |
| [Zoho Books API](https://www.zoho.com/books/api/v3/introduction/) | Full accounting API: invoices, bills, banking, chart of accounts | 🔴 OAuth | ✅ | ✅⭐ |
| [NetSuite API](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_157373386674.html) | Oracle ERP suite with financials, inventory, CRM via REST and SOAP | 🔴 OAuth | ✅ | ✅ |
| [FreeAgent API](https://dev.freeagent.com/docs) | UK-focused small business accounting: invoices, expenses, bank feeds | 🔴 OAuth | ✅ | ✅ |
| [Harvest API](https://help.getharvest.com/api-v2/) | Time tracking and invoicing API for project-based businesses | 🔴 OAuth | ✅ | ✅⭐ |
| [Dynamics 365 Business Central API](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/) | Microsoft ERP with financials, sales, purchasing, inventory management | 🔴 OAuth | ✅ | ✅ |
| [Odoo External API](https://www.odoo.com/documentation/18.0/developer/reference/external_api.html) | Open-source ERP with accounting, invoicing, inventory via JSON-RPC/XML-RPC | 🟡 API Key | ✅ | ⚠️ |
| [Apideck Accounting API](https://www.apideck.com/connectors/zoho-books) | Unified accounting API connecting to 30+ accounting platforms via one interface | 🟡 API Key | ✅ | ✅⭐ |
| [Workday Financials API](https://community.workday.com/sites/default/files/file-hosting/productionapi/) | Enterprise financial management, GL, procurement, and expense management | 🔴 OAuth | ✅ | ⚠️ |
| [Bill.com API](https://developer.bill.com/hc/en-us) | AP/AR automation, payments, invoicing, and approval workflows | 🟡 API Key | ✅ | ✅ |

---

## 🛡️ Anti-Fraud & Risk Management APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Sift API](https://developers.sift.com/) | Digital trust platform for payment fraud, account takeover, and content abuse | 🟡 API Key | ✅ | ✅⭐ |
| [Riskified API](https://www.riskified.com/documentation/) | Ecommerce fraud protection with guaranteed chargeback coverage | 🟡 API Key | ✅ | ✅ |
| [Forter API](https://docs.forter.com/) | Real-time fraud decisioning for ecommerce transactions and account events | 🟡 API Key | ✅ | ✅ |
| [Sardine API](https://docs.sardine.ai/home) | Fraud, compliance, and identity verification for fintechs via behavioral analytics | 🟡 API Key | ✅ | ✅ |
| [Signifyd API](https://developer.signifyd.com/) | Revenue protection with guaranteed fraud decisions for ecommerce | 🟡 API Key | ✅ | ✅⭐ |
| [MaxMind minFraud API](https://dev.maxmind.com/minfraud/) | IP geolocation and transaction risk scoring for fraud prevention | 🟡 API Key | ✅ | ✅⭐ |
| [SEON Fraud API](https://docs.seon.io/api-reference) | Email, phone, IP, and device intelligence for fraud detection in a single call | 🟡 API Key | ✅ | ✅⭐ |
| [IPQualityScore API](https://www.ipqualityscore.com/documentation/overview) | Proxy/VPN detection, email validation, phone validation, and fraud scoring | 🟡 API Key | ✅ | ✅⭐ |
| [Fingerprint API](https://docs.fingerprint.com/) | 99.5% accurate browser and device identification for fraud prevention | 🟡 API Key | ✅ | ✅⭐ |
| [Telesign API](https://www.telesign.com/) | Phone number intelligence, SMS verification, and fraud risk scoring | 🟡 API Key | ✅ | ✅⭐ |
| [Jumio API](https://www.jumio.com/) | AI-powered identity verification with ID document and biometric checks | 🟡 API Key | ✅ | ✅ |
| [Onfido API](https://onfido.com/) | Document and biometric identity verification for onboarding | 🟡 API Key | ✅ | ✅ |
| [Kount API](https://developer.kount.com/hc/en-us) | AI-driven digital fraud prevention for payments and account creation | 🟡 API Key | ✅ | ✅ |

---

## ✈️ Aviation & Flight Data APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [FlightAware AeroAPI](https://www.flightaware.com/commercial/aeroapi) | Real-time and historical flight tracking with 60+ REST endpoints | 🟡 API Key | ✅ | ✅⭐ |
| [AviationStack API](https://aviationstack.com/) | Real-time flight status, schedules, airlines, airports, and aircraft data | 🟡 API Key | ✅ | ✅⭐ |
| [Flightradar24 API](https://fr24api.flightradar24.com/) | Real-time flight tracking data from the world's largest flight tracker | 🟡 API Key | ✅ | ✅ |
| [Cirium / FlightStats API](https://developer.cirium.com/) | Comprehensive flight status, delays, schedules, and historical performance | 🟡 API Key | ✅ | ✅⭐ |
| [OpenSky Network API](https://opensky-network.org/) | Free crowdsourced ADS-B flight tracking data with REST and Python access | 🟢 No | ✅ | ✅ |
| [AeroDataBox API](https://doc.aerodatabox.com/) | Flight status, delays, schedules, airports, and aircraft data for SMBs | 🟡 API Key | ✅ | ✅⭐ |
| [Aviation Edge API](https://aviation-edge.com/developers/) | Real-time flight tracker, timetables, routes, airlines, and airports data | 🟡 API Key | ✅ | ✅ |
| [Amadeus Self-Service APIs](https://developers.amadeus.com/) | Flight search, booking, fare prediction, trip management for travel apps | 🟡 API Key | ✅ | ✅⭐ |
| [Lufthansa Open API](https://developer.lufthansa.com/docs) | Flight status, schedules, seat maps, and reference data for Lufthansa Group | 🟡 API Key | ✅ | ✅ |
| [Skyscanner API](https://developers.skyscanner.net/) | Meta-search flight pricing, routes, and live quotes from global carriers | 🟡 API Key | ✅ | ✅ |
| [Kiwi.com Tequila API](https://tequila.kiwi.com/) | Flight search with multi-city and virtual interlining for complex itineraries | 🟡 API Key | ✅ | ✅ |
| [ADS-B Exchange API](https://www.adsbexchange.com/data/) | Unfiltered, crowdsourced real-time ADS-B aircraft tracking data | 🟡 API Key | ✅ | ✅ |

---

## 🏧 Banking & Open Banking APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Plaid API](https://plaid.com/docs/api/) | US/EU account linking, transactions, identity, balance, and income data | 🟡 API Key | ✅ | ✅⭐ |
| [Tink API](https://docs.tink.com/api) | PSD2-compliant access to 6,000+ European banks for data and payments | 🔴 OAuth | ✅ | ✅ |
| [TrueLayer API](https://docs.truelayer.com/) | Open banking payments and data access for UK and European banks | 🔴 OAuth | ✅ | ✅⭐ |
| [Yapily API](https://docs.yapily.com/) | Open banking data and payment initiation across UK, Europe, and beyond | 🟡 API Key | ✅ | ✅⭐ |
| [MX API](https://docs.mx.com/) | Financial data aggregation, cleansing, and enrichment for US institutions | 🟡 API Key | ✅ | ✅ |
| [Finicity API](https://developer.finicity.com/) | Mastercard's open banking for account verification, income, and credit insights | 🟡 API Key | ✅ | ✅ |
| [Yodlee API](https://developer.yodlee.com/) | Global account aggregation, transactions, income analysis, and identity | 🟡 API Key | ✅ | ✅ |
| [Salt Edge API](https://docs.saltedge.com/general/v5/) | PSD2 open banking gateway for account info and payment initiation in Europe | 🟡 API Key | ✅ | ✅ |
| [GoCardless / Nordigen API](https://gocardless.com/developers/) | Free open banking API access to 2,300+ European banks via PSD2 | 🟡 API Key | ✅ | ✅ |
| [Belvo API](https://developers.belvo.com/) | Open finance API for Latin America: banking, fiscal, and employment data | 🟡 API Key | ✅ | ✅⭐ |
| [Basiq API](https://www.basiq.io/) | Australian open banking data platform for account and transaction access | 🟡 API Key | ✅ | ✅ |
| [Stripe Financial Connections](https://stripe.com/docs/financial-connections) | Bank account linking and verification within the Stripe ecosystem | 🟡 API Key | ✅ | ✅⭐ |
| [Flinks API](https://docs.flinks.com/) | Canadian financial data aggregation for bank accounts and transactions | 🟡 API Key | ✅ | ✅ |

---

## 🤖 Conversational AI & Chatbot APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Google Dialogflow API](https://cloud.google.com/dialogflow/docs/) | NLU-based chatbot platform with ES and CX editions, 20+ languages | 🔴 OAuth | ✅ | ✅⭐ |
| [Amazon Lex API](https://docs.aws.amazon.com/lexv2/latest/APIReference/welcome.html) | AWS conversational AI powered by Alexa technology for text and voice bots | 🟡 API Key | ✅ | ✅⭐ |
| [Rasa HTTP API](https://rasa.com/docs/openapi/http-api/) | Open-source conversational AI with NLU and dialogue management | 🟡 API Key | ✅ | ✅ |
| [Botpress API](https://botpress.com/docs/api-reference/introduction) | Open-source chatbot platform with visual builder and GPT integration | 🟡 API Key | ✅ | ✅ |
| [Wit.ai API](https://wit.ai/docs/http) | Facebook/Meta's free NLU platform for building voice and text chatbots | 🟡 API Key | ✅ | ✅ |
| [Anthropic Claude API](https://docs.anthropic.com/) | Claude models for safe, helpful conversational AI with 200K context window | 🟡 API Key | ✅ | ✅⭐ |
| [Cohere API](https://docs.cohere.com/) | Enterprise NLP with chat, embeddings, reranking, and RAG capabilities | 🟡 API Key | ✅ | ✅⭐ |
| [Voiceflow API](https://docs.voiceflow.com/reference/api-overview) | Visual chatbot builder with dialog manager, transcript, and analytics APIs | 🟡 API Key | ✅ | ✅ |
| [Google Gemini API](https://ai.google.dev/gemini-api/docs) | Multimodal AI API supporting text, image, audio, and video conversations | 🟡 API Key | ✅ | ✅⭐ |
| [Cognigy API](https://docs.cognigy.com/) | Enterprise conversational AI platform for contact center automation | 🟡 API Key | ✅ | ✅ |
| [Landbot API](https://api.landbot.io/) | No-code chatbot builder with API access for web, WhatsApp, and Messenger | 🟡 API Key | ✅ | ✅ |

---

## 💊 Pharmacy & Drug Database APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [OpenFDA Drug API](https://open.fda.gov/apis/drug/) | FDA drug adverse events, labeling, NDC directory, and recall data | 🟢 No | ✅ | ✅⭐ |
| [RxNorm API](https://lhncbc.nlm.nih.gov/RxNav/APIs/RxNormAPIs.html) | NLM normalized drug names, ingredients, strengths, and dose forms | 🟢 No | ✅ | ✅ |
| [DailyMed API](https://dailymed.nlm.nih.gov/dailymed/app-support-web-services.cfm) | FDA structured product labeling (SPL) data in XML/JSON for US drugs | 🟢 No | ✅ | ✅ |
| [DrugBank API](https://dev.drugbank.com/) | Comprehensive drug database with interactions, targets, and clinical info | 🟡 API Key | ✅ | ✅⭐ |
| [NLM Drug Interaction API](https://rxnav.nlm.nih.gov/InteractionAPIREST.html) | Drug-drug interaction checks using DrugBank and ONCHigh sources | 🟢 No | ✅ | ✅ |
| [ClinicalTrials.gov API](https://clinicaltrials.gov/data-api/about-api) | Search and retrieve clinical trial study data from the NIH registry | 🟢 No | ✅ | ✅⭐ |
| [FDA NDC Directory API](https://open.fda.gov/apis/drug/ndc/) | National Drug Code directory with product and package information | 🟢 No | ✅ | ✅⭐ |
| [ChEMBL API](https://www.ebi.ac.uk/chembl/api/data/docs) | Open large-scale bioactivity database for drug discovery research | 🟢 No | ✅ | ✅⭐ |
| [PubChem API](https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest) | Chemical compound, substance, and bioassay data from NIH/NCBI | 🟢 No | ✅ | ✅ |
| [MedlinePlus Connect API](https://medlineplus.gov/connect/overview.html) | Patient-friendly health information linked to medical codes (ICD, SNOMED) | 🟢 No | ✅ | ✅ |

---

## 🎮 Game Development & Engine APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Steamworks Web API](https://partner.steamgames.com/doc/webapi) | Steam platform: achievements, leaderboards, matchmaking, user stats, store | 🟡 API Key | ✅ | ✅ |
| [Unity Gaming Services API](https://services.docs.unity.com/) | Cloud services: analytics, authentication, cloud save, economy, multiplayer | 🟡 API Key | ✅ | ✅ |
| [PlayFab API](https://learn.microsoft.com/en-us/gaming/playfab/api-references/) | Microsoft's LiveOps backend: player data, leaderboards, economy, multiplayer | 🟡 API Key | ✅ | ✅⭐ |
| [Epic Online Services API](https://dev.epicgames.com/docs/api-ref) | Cross-platform services: matchmaking, lobbies, achievements, voice chat | 🟡 API Key | ✅ | ✅ |
| [Nakama Server API](https://heroiclabs.com/docs/) | Open-source game server: auth, matchmaking, chat, leaderboards, storage | 🟡 API Key | ✅ | ✅⭐ |
| [LootLocker API](https://ref.lootlocker.com/game-api/) | Game backend: player management, leaderboards, virtual economy, storage | 🟡 API Key | ✅ | ✅⭐ |
| [AccelByte API](https://docs.accelbyte.io/api-explorer/) | Enterprise game backend: IAM, matchmaking, commerce, analytics, UGC | 🟡 API Key | ✅ | ✅ |
| [Xsolla API](https://developers.xsolla.com/) | Game monetization: payments, subscriptions, in-game store, launcher | 🟡 API Key | ✅ | ✅⭐ |
| [RAWG Video Games API](https://rawg.io/apidocs) | Database of 500K+ games with metadata, screenshots, and ratings | 🟡 API Key | ✅ | ✅⭐ |
| [IGDB API](https://api-docs.igdb.com/) | Twitch's game database API with comprehensive game metadata and imagery | 🟡 API Key | ✅ | ✅ |

---

## 🧬 Genomics & Genetic Testing APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [NCBI E-utilities API](https://www.ncbi.nlm.nih.gov/home/develop/api/) | Access to 38+ NCBI databases including GenBank, Gene, SNP, and ClinVar | 🟡 API Key | ✅ | ✅ |
| [Ensembl REST API](https://rest.ensembl.org/) | Genome annotation data: genes, variants, sequences, and comparative genomics | 🟢 No | ✅ | ✅⭐ |
| [UCSC Genome Browser API](https://genome.ucsc.edu/goldenPath/help/api.html) | Genome assembly data: tracks, sequences, chromosome info in JSON format | 🟢 No | ✅ | ✅ |
| [MyVariant.info API](https://myvariant.info/) | High-performance variant annotation aggregating 14+ data sources | 🟢 No | ✅ | ✅⭐ |
| [MyGene.info API](https://mygene.info/) | Gene annotation as a service with high-performance query and retrieval | 🟢 No | ✅ | ✅⭐ |
| [GA4GH Beacon API](https://beacon-project.io/) | Federated discovery protocol for querying genomic variant existence | 🟢 No | ✅ | ✅ |
| [DNAnexus API](https://documentation.dnanexus.com/developer/api) | Cloud genomics platform for managing data, workflows, and analysis pipelines | 🟡 API Key | ✅ | ✅ |
| [Galaxy Project API](https://galaxyproject.org/develop/api/) | Open-source bioinformatics workflow platform with REST API access | 🟡 API Key | ✅ | ✅ |
| [PDB REST API (RCSB)](https://data.rcsb.org/) | Protein Data Bank structural biology data for macromolecular structures | 🟢 No | ✅ | ✅⭐ |
| [UniProt API](https://www.uniprot.org/help/api) | Universal protein resource with sequence, function, and classification data | 🟢 No | ✅ | ✅ |

---

## 📊 Business Intelligence & Analytics APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Looker API](https://cloud.google.com/looker/docs/api-intro) | Google Cloud BI: LookML modeling, query execution, dashboard management | 🔴 OAuth | ✅ | ✅⭐ |
| [Tableau REST API](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api.htm) | Server/Cloud resource management: workbooks, datasources, permissions | 🟡 API Key | ✅ | ✅⭐ |
| [Power BI REST API](https://learn.microsoft.com/en-us/rest/api/power-bi/) | Microsoft BI: embedded analytics, dataset refresh, report deployment | 🔴 OAuth | ✅ | ✅⭐ |
| [Metabase API](https://www.metabase.com/docs/latest/api) | Open-source BI: questions, dashboards, collections, and database queries | 🟡 API Key | ✅ | ✅ |
| [Grafana HTTP API](https://grafana.com/docs/grafana/latest/developer-resources/api-reference/http-api/) | Dashboards, datasources, alerts, annotations, and organization management | 🟡 API Key | ✅ | ✅⭐ |
| [Domo API](https://developer.domo.com/) | Cloud BI platform: datasets, cards, pages, users, and group management | 🔴 OAuth | ✅ | ✅ |
| [Apache Superset API](https://superset.apache.org/docs/api/) | Open-source BI with OpenAPI-spec REST endpoints for full platform control | 🟡 API Key | ✅ | ✅⭐ |
| [Redash API](https://redash.io/help/user-guide/integrations-and-api/api) | Open-source query and visualization tool with REST API for queries and dashboards | 🟡 API Key | ✅ | ✅ |
| [Qlik Sense API](https://qlik.dev/apis/) | Enterprise BI: apps, engine, repository, and proxy management APIs | 🟡 API Key | ✅ | ✅ |
| [Lightdash API](https://docs.lightdash.com/references/api-reference) | Open-source BI built for dbt with REST API for charts and dashboards | 🟡 API Key | ✅ | ✅ |

---

## 🔄 ETL & Data Pipeline APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Fivetran REST API](https://fivetran.com/docs/rest-api) | Managed ELT: connector management, sync triggers, destination config | 🟡 API Key | ✅ | ✅⭐ |
| [Airbyte API](https://reference.airbyte.com/) | Open-source ELT: 300+ connectors, source/destination/connection management | 🟡 API Key | ✅ | ✅⭐ |
| [dbt Cloud API](https://docs.getdbt.com/docs/dbt-cloud-apis/overview) | Transformation platform: job triggers, run status, discovery, semantic layer | 🟡 API Key | ✅ | ✅⭐ |
| [Prefect API](https://docs.prefect.io/v3/api-ref) | Modern workflow orchestration: flows, deployments, and task scheduling | 🟡 API Key | ✅ | ✅ |
| [Dagster API](https://docs.dagster.io/api) | Asset-based orchestration: pipelines, schedules, sensors, and run management | 🟡 API Key | ✅ | ✅ |
| [Apache Airflow REST API](https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html) | Workflow orchestration: DAG management, task runs, variables, connections | 🟡 API Key | ✅ | ✅ |
| [Census API](https://developers.getcensus.com/getting-started/introduction) | Reverse ETL: sync warehouse data to 60+ SaaS tools programmatically | 🟡 API Key | ✅ | ✅ |
| [Hightouch API](https://hightouch.com/docs/api-reference) | Reverse ETL: sync models, manage destinations, trigger and monitor syncs | 🟡 API Key | ✅ | ✅ |
| [Matillion API](https://docs.matillion.com/data-productivity-cloud/api/docs/intro/) | Cloud-native ETL: job management, pipelines, and environment configuration | 🟡 API Key | ✅ | ✅ |
| [Hevo Data API](https://docs.hevodata.com/references/rest-api/) | No-code data pipeline: connectors, transformations, and monitoring | 🟡 API Key | ✅ | ✅ |

---

## 🏥 Telemedicine & Telehealth APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Twilio Video](https://www.twilio.com/docs/video) | HIPAA-eligible programmable video for telehealth virtual visits | 🟡 API Key | ✅ | ✅⭐ |
| [Vonage Video API](https://developer.vonage.com/en/video/overview) | Real-time video, voice, and messaging with HIPAA-compliant options | 🟡 API Key | ✅ | ✅⭐ |
| [Agora](https://docs.agora.io/en/) | Real-time voice, video, and interactive streaming SDK for telehealth | 🟡 API Key | ✅ | ✅⭐ |
| [Daily.co](https://docs.daily.co/) | Developer-focused video call API with HIPAA BAA support | 🟡 API Key | ✅ | ✅⭐ |
| [Zoom Video SDK](https://developers.zoom.us/docs/video-sdk/) | Embed Zoom video/audio into custom telehealth applications | 🟡 API Key | ✅ | ✅ |
| [Whereby](https://docs.whereby.com/) | Embeddable browser-based video meetings, no downloads required | 🟡 API Key | ✅ | ✅⭐ |
| [Dyte](https://docs.dyte.io/api) | Live video SDK with REST API and pre-built UI components for health apps | 🟡 API Key | ✅ | ✅⭐ |
| [CometChat](https://www.cometchat.com/docs) | In-app messaging, voice, and video chat API for healthcare apps | 🟡 API Key | ✅ | ✅ |
| [VideoSDK](https://www.videosdk.live/solutions/telehealth) | HIPAA-compliant video conferencing API for telemedicine apps | 🟡 API Key | ✅ | ✅ |
| [SteadyMD](https://www.steadymd.com/technology/) | Telehealth infrastructure API with licensed clinician network | 🟡 API Key | ✅ | ✅ |

---

## 🏢 ERP & Enterprise Resource Planning APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [SAP Business One Service Layer](https://help.sap.com/doc/056f69366b5345a386bb8149f1700c19/10.0/en-US/Service%20Layer%20API%20Reference.html) | RESTful OData API for SAP Business One ERP | 🔴 OAuth | ✅ | ✅ |
| [Oracle NetSuite REST API](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/book_1559132836.html) | SuiteTalk REST web services for NetSuite ERP integration | 🔴 OAuth | ✅ | ✅ |
| [Odoo](https://www.odoo.com/documentation/18.0/developer.html) | Open-source ERP with XML-RPC and JSON-RPC external APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Microsoft Dynamics 365](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/services-home-page) | REST APIs for Dynamics 365 Finance, Supply Chain, and Commerce | 🔴 OAuth | ✅ | ✅ |
| [ERPNext / Frappe](https://frappe.io/erpnext) | Open-source cloud ERP with full REST API on the Frappe framework | 🟡 API Key | ✅ | ✅⭐ |
| [Acumatica](https://www.acumatica.com/developers/) | Cloud ERP with contract-based REST and SOAP APIs | 🔴 OAuth | ✅ | ✅ |
| [Sage Intacct](https://developer.intacct.com/) | Cloud financial management REST and XML APIs for mid-market ERP | 🟡 API Key | ✅ | ✅⭐ |
| [Epicor Kinetic](https://api.xchange.epicor.com/) | REST APIs and OData for Epicor manufacturing and distribution ERP | 🔴 OAuth | ✅ | ✅ |
| [SAP S/4HANA Cloud](https://api.sap.com/products/SAPS4HANACloud/apis/REST) | REST APIs for SAP S/4HANA next-gen ERP suite | 🔴 OAuth | ✅ | ✅ |
| [SAP Concur](https://developer.concur.com/) | APIs for travel, expense, and invoice management (SAP ecosystem) | 🔴 OAuth | ✅ | ✅⭐ |

---

## 💼 Expense Management APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Expensify](https://integrations.expensify.com/) | Expense report automation API with SmartScan receipt OCR | 🟡 API Key | ✅ | ✅ |
| [SAP Concur Expense](https://api.sap.com/package/ConcurExpense) | Enterprise expense management REST APIs for reports, entries, receipts | 🔴 OAuth | ✅ | ✅⭐ |
| [Brex](https://developer.brex.com/) | Corporate card and expense management API with transactions and cards | 🟡 API Key | ✅ | ✅⭐ |
| [Ramp](https://docs.ramp.com/) | Corporate card and spend management API for transactions, cards, users | 🟡 API Key | ✅ | ✅⭐ |
| [Zoho Expense](https://www.zoho.com/expense/api/v1/introduction/) | Expense tracking, reports, receipts, and trip management API | 🔴 OAuth | ✅ | ✅⭐ |
| [Emburse](https://www.emburse.com/api-docs) | Corporate cards and expense management API (formerly Abacus/Center) | 🟡 API Key | ✅ | ✅ |
| [Tipalti](https://tipalti.com/product/platform/api/) | Global payables automation and expense API for mass payments | 🟡 API Key | ✅ | ✅ |
| [Fyle](https://docs.fylehq.com/) | Expense management API with real-time card feeds and receipt matching | 🔴 OAuth | ✅ | ✅ |

---

## 🔬 Facial Recognition & Biometric APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [AWS Rekognition](https://docs.aws.amazon.com/rekognition/latest/dg/what-is.html) | Image and video face detection, comparison, and analysis at scale | 🟡 API Key | ✅ | ✅⭐ |
| [Azure AI Face](https://learn.microsoft.com/en-us/rest/api/face/) | Face detection, verification, identification, and emotion analysis | 🟡 API Key | ✅ | ✅⭐ |
| [Face++ (Megvii)](https://console.faceplusplus.com/documents/5679127) | Face detection, recognition, landmarks, and attributes analysis | 🟡 API Key | ✅ | ✅ |
| [Kairos](https://www.kairos.com/docs) | Face recognition, identity verification, and emotion analysis API | 🟡 API Key | ✅ | ✅⭐ |
| [Clarifai](https://docs.clarifai.com/) | Visual recognition platform with face detection and custom models | 🟡 API Key | ✅ | ✅⭐ |
| [BioID](https://developer.bioid.com/) | Liveness detection and face recognition biometric web service | 🟡 API Key | ✅ | ✅ |
| [iProov](https://docs.iproov.com/) | Genuine Presence Assurance liveness detection biometric API | 🟡 API Key | ✅ | ✅ |
| [Onfido (Entrust)](https://documentation.onfido.com/) | Document verification and facial biometric identity checks | 🟡 API Key | ✅ | ✅⭐ |
| [Google Cloud Vision](https://cloud.google.com/vision/docs) | Face detection with landmark, emotion, and likelihood attributes | 🟡 API Key | ✅ | ✅⭐ |
| [ID Analyzer](https://www.idanalyzer.com/products/biometric-api.html) | Biometric face matching and ID document verification API | 🟡 API Key | ✅ | ✅ |

---

## 🎯 Influencer Marketing APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [CreatorIQ](https://creatoriq.com/) | Enterprise influencer management with real-time data across major platforms | 🟡 API Key | ✅ | ✅ |
| [Modash](https://docs.modash.io/) | 350M+ creator database API with Raw API for live monitoring | 🟡 API Key | ✅ | ✅⭐ |
| [HypeAuditor](https://hypeauditor.com/api-integration/) | 219M+ creator fraud detection, audience quality, and analytics API | 🟡 API Key | ✅ | ✅⭐ |
| [Upfluence](https://www.upfluence.com/) | 12M+ creator database API with e-commerce and affiliate tracking | 🟡 API Key | ✅ | ✅ |
| [Phyllo](https://www.getphyllo.com/) | Unified API for influencer data from 20+ social media platforms | 🟡 API Key | ✅ | ✅⭐ |
| [NeoReach](https://neoreach.com/api/) | 400+ data points per creator, social insights via REST API | 🟡 API Key | ✅ | ✅ |
| [Favikon](https://www.favikon.com/) | AI-powered influencer discovery and ranking platform with API | 🟡 API Key | ✅ | ✅ |
| [Emplifi](https://docs.emplifi.io/) | Social media marketing platform with influencer management API | 🟡 API Key | ✅ | ✅ |

---

## 📦 Inventory Management APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Cin7 Omni](https://api.cin7.com/) | Cloud inventory, POS, 3PL, and production planning API | 🟡 API Key | ✅ | ✅⭐ |
| [Cin7 Core (DEAR)](https://dearinventory.docs.apiary.io/) | Multi-channel inventory and order management REST API | 🟡 API Key | ✅ | ✅⭐ |
| [SkuVault](https://dev.skuvault.com/reference) | Warehouse management and inventory accuracy API for ecommerce | 🟡 API Key | ✅ | ✅ |
| [Ordoro](https://docs.ordoro.com/) | Order management, shipping, and inventory sync API | 🟡 API Key | ✅ | ✅⭐ |
| [Zoho Inventory](https://www.zoho.com/inventory/api/v1/introduction/) | Inventory tracking, orders, shipments, and warehouse API | 🔴 OAuth | ✅ | ✅⭐ |
| [Katana MRP](https://katanamrp.com/ecommerce-api/) | Manufacturing and inventory planning API with Shopify integration | 🟡 API Key | ✅ | ✅ |
| [Lightspeed Retail](https://x-series-api.lightspeedhq.com/) | POS and retail inventory management API (X-Series and R-Series) | 🔴 OAuth | ✅ | ✅⭐ |
| [Shopify Inventory](https://shopify.dev/docs/api/admin-rest/current/resources/inventorylevel) | Inventory levels, locations, and adjustments via Shopify Admin API | 🟡 API Key | ✅ | ✅⭐ |
| [Square Inventory](https://developer.squareup.com/reference/square/inventory-api) | Inventory counts, adjustments, and transfers for Square merchants | 🔴 OAuth | ✅ | ✅⭐ |
| [Unleashed](https://apidocs.unleashedsoftware.com/) | Cloud-based inventory management API for manufacturers and distributors | 🟡 API Key | ✅ | ✅⭐ |

---

## 📈 Investment & Portfolio Management APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Alpaca](https://alpaca.markets/docs/) | Commission-free stock, options, and crypto trading REST and WebSocket API | 🟡 API Key | ✅ | ✅⭐ |
| [Morningstar](https://developer.morningstar.com/) | Investment data, fund analytics, and portfolio analysis APIs | 🟡 API Key | ✅ | ✅ |
| [Tradier](https://documentation.tradier.com/brokerage-api) | Brokerage API for equities and options trading with market data | 🟡 API Key | ✅ | ✅⭐ |
| [Polygon.io](https://polygon.io/) | Real-time and historical stock, options, forex, and crypto market data | 🟡 API Key | ✅ | ✅⭐ |
| [Alpha Vantage](https://www.alphavantage.co/documentation/) | Free stock, forex, crypto, and technical indicator API | 🟡 API Key | ✅ | ✅⭐ |
| [Intrinio](https://intrinio.com/) | Financial data API with fundamentals, prices, and options data | 🟡 API Key | ✅ | ✅⭐ |
| [Finnhub](https://finnhub.io/docs/api) | Real-time stock, forex, and crypto API with alternative data | 🟡 API Key | ✅ | ✅⭐ |
| [Twelve Data](https://twelvedata.com/docs) | Stock, forex, crypto, ETF, and indices real-time and historical data API | 🟡 API Key | ✅ | ✅⭐ |
| [Quandl (Nasdaq Data Link)](https://data.nasdaq.com/) | Financial, economic, and alternative datasets for quantitative analysis | 🟡 API Key | ✅ | ✅⭐ |

---

## 📋 IT Service Management (ITSM) APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [ServiceNow](https://developer.servicenow.com/) | Enterprise ITSM REST API for incidents, changes, CMDB, and workflows | 🔴 OAuth | ✅ | ✅⭐ |
| [Jira Service Management](https://developer.atlassian.com/cloud/jira/service-desk/rest/) | Cloud REST API for service requests, queues, SLAs, and customer portals | 🟡 API Key | ✅ | ✅⭐ |
| [Freshservice](https://api.freshservice.com/) | Cloud ITSM REST API v2 for tickets, assets, changes, and problems | 🟡 API Key | ✅ | ✅⭐ |
| [PagerDuty](https://developer.pagerduty.com/) | Incident management and on-call scheduling REST API v2 | 🟡 API Key | ✅ | ✅⭐ |
| [TOPdesk](https://developers.topdesk.com/) | Open REST API for incident, change, and asset management | 🟡 API Key | ✅ | ✅⭐ |
| [Opsgenie (Atlassian)](https://docs.opsgenie.com/docs/api-overview) | Alert and incident management REST API with on-call scheduling | 🟡 API Key | ✅ | ✅⭐ |
| [Statuspage (Atlassian)](https://developer.statuspage.io/) | Status page and incident communication REST API | 🟡 API Key | ✅ | ✅⭐ |
| [xMatters](https://help.xmatters.com/ondemand/xmodref/rest_api.htm) | Incident communication and event management REST API | 🟡 API Key | ✅ | ✅ |

---

## 🚚 Last Mile Delivery APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Onfleet](https://docs.onfleet.com/) | RESTful API for dispatch, routing, tracking, and delivery management | 🟡 API Key | ✅ | ✅⭐ |
| [Route4Me](https://integrate.route4me.com/) | Route optimization and fleet management API with multi-language SDKs | 🟡 API Key | ✅ | ✅⭐ |
| [Bringg](https://developers.bringg.com/) | Modular delivery management API for Own Fleet and Delivery Hub | 🟡 API Key | ✅ | ✅⭐ |
| [Shipday](https://docs.shipday.com/) | Local delivery management and on-demand delivery network API | 🟡 API Key | ✅ | ✅⭐ |
| [EasyPost](https://docs.easypost.com/) | Multi-carrier shipping API for labels, tracking, and address verification | 🟡 API Key | ✅ | ✅⭐ |
| [eLogii](https://api-docs.elogii.com/) | Route optimization and delivery management API with dynamic routing | 🟡 API Key | ✅ | ✅⭐ |
| [OptimoRoute](https://optimoroute.com/api/) | Route planning and schedule optimization REST API v1 | 🟡 API Key | ✅ | ✅⭐ |
| [Locus](https://docs.locus.sh/) | End-to-end logistics API for route planning and dispatch optimization | 🟡 API Key | ✅ | ✅ |

---

## 🏦 Lending & Loan APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Plaid](https://plaid.com/docs/) | Financial data API for income verification, bank auth, and asset reports | 🟡 API Key | ✅ | ✅⭐ |
| [Finicity (Mastercard)](https://developer.mastercard.com/open-banking-us/documentation/api-reference) | Open banking API for income/employment verification and credit decisioning | 🟡 API Key | ✅ | ✅⭐ |
| [MX Platform](https://docs.mx.com/api-reference/platform-api/overview/) | Financial data aggregation and enhancement API for lending workflows | 🟡 API Key | ✅ | ✅⭐ |
| [Blend](https://blend.com/platform/) | Digital lending platform API for mortgage and consumer loan origination | 🟡 API Key | ✅ | ✅ |
| [LendAPI](https://www.lendapi.com/developers) | RESTful API for launching fintech lending products and onboarding | 🟡 API Key | ✅ | ✅⭐ |
| [Equifax](https://developer.equifax.com/products/apiproducts) | Credit reports, scores, income verification, and identity APIs | 🟡 API Key | ✅ | ✅ |
| [Ocrolus](https://www.ocrolus.com/) | AI-powered bank statement and financial document analysis API | 🟡 API Key | ✅ | ✅ |
| [CRS Credit API](https://crscreditapi.com/) | Unified credit bureau API for Equifax, TransUnion, and Experian data | 🟡 API Key | ✅ | ✅ |

---

## 📚 Knowledge Base & Wiki APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Notion API](https://developers.notion.com/) | All-in-one workspace with pages, databases, blocks; RESTful API | 🟡 API Key | ✅ | ✅⭐ |
| [Confluence Cloud API](https://developer.atlassian.com/cloud/confluence/rest/v2/) | Atlassian enterprise wiki and documentation platform REST API | 🟡 API Key | ✅ | ✅⭐ |
| [GitBook API](https://developer.gitbook.com/) | Git-based documentation platform; manage spaces, content, and publishing | 🟡 API Key | ✅ | ✅⭐ |
| [MediaWiki API](https://www.mediawiki.org/wiki/API:REST_API) | Powers Wikipedia; search, read, edit wiki pages via REST or Action API | 🟢 No | ✅ | ✅⭐ |
| [Outline API](https://www.getoutline.com/developers) | Open-source team knowledge base; documents, collections, search | 🟡 API Key | ✅ | ✅ |
| [Coda API](https://coda.io/developers) | Docs-as-apps platform; manage docs, tables, rows, formulas via REST | 🟡 API Key | ✅ | ✅⭐ |
| [BookStack API](https://demo.bookstackapp.com/api/docs) | Open-source wiki with books/chapters/pages structure; built-in REST API | 🟡 API Key | ✅ | ✅ |
| [Guru API](https://developer.getguru.com/docs/getting-started) | Knowledge management platform; cards, boards, collections via REST | 🟡 API Key | ✅ | ✅ |
| [Document360 API](https://apidocs.document360.com/apidocs/getting-started) | Knowledge base platform for internal and customer-facing docs | 🟡 API Key | ✅ | ✅ |
| [Zendesk Guide API](https://developer.zendesk.com/api-reference/help_center/) | Help Center and knowledge base management within Zendesk | 🟡 API Key | ✅ | ✅⭐ |

---

## 🎯 Lead Generation & Enrichment APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Clearbit API](https://clearbit.com/docs) | Person and Company enrichment from email/domain; real-time lookups | 🟡 API Key | ✅ | ✅⭐ |
| [Apollo.io API](https://docs.apollo.io/) | 200M+ contacts database; prospecting, enrichment, sequences | 🟡 API Key | ✅ | ✅⭐ |
| [Hunter.io API](https://hunter.io/api) | Email finder and verifier; domain search, email count, verification | 🟡 API Key | ✅ | ✅⭐ |
| [ZoomInfo API](https://docs.zoominfo.com/) | Enterprise B2B database; 321M+ profiles, intent data, company insights | 🟡 API Key | ✅ | ✅ |
| [Lusha API](https://docs.lusha.com/) | B2B contact enrichment; direct dials, emails, company data | 🟡 API Key | ✅ | ✅ |
| [FullContact API](https://docs.fullcontact.com/) | Person-Centered Identity Graph; enrich and resolve customer profiles | 🟡 API Key | ✅ | ✅⭐ |
| [People Data Labs API](https://docs.peopledatalabs.com/) | Person and company enrichment, search, and bulk operations | 🟡 API Key | ✅ | ✅⭐ |
| [Snov.io API](https://snov.io/api) | Email finder, verifier, and drip campaign automation via REST | 🟡 API Key | ✅ | ✅ |
| [RocketReach API](https://docs.rocketreach.co/reference/rocketreach-api) | 700M+ contacts; email and phone lookup for professionals | 🟡 API Key | ✅ | ✅ |
| [UpLead API](https://docs.uplead.com/) | B2B contacts from 200+ countries; person and company enrichment | 🟡 API Key | ✅ | ✅ |

---

## 🏪 Marketplace & E-commerce Platform APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Shopify API](https://shopify.dev/docs/api) | Full e-commerce platform; products, orders, customers via REST and GraphQL | 🔴 OAuth | ✅ | ✅⭐ |
| [WooCommerce REST API](https://woocommerce.github.io/woocommerce-rest-api-docs/) | WordPress e-commerce plugin; products, orders, coupons, reports | 🟡 API Key | ✅ | ✅⭐ |
| [BigCommerce API](https://developer.bigcommerce.com/docs/api) | Enterprise e-commerce; REST and GraphQL for catalog, orders, carts | 🟡 API Key | ✅ | ✅⭐ |
| [Amazon SP-API](https://developer-docs.amazon.com/sp-api/) | Amazon Selling Partner API; orders, catalog, fulfillment, reports | 🔴 OAuth | ✅ | ✅ |
| [eBay API](https://developer.ebay.com/develop) | Marketplace integration; browse, buy, sell, fulfillment APIs | 🔴 OAuth | ✅ | ✅ |
| [Etsy Open API v3](https://developers.etsy.com/) | Handmade marketplace; listings, shops, transactions, reviews | 🔴 OAuth | ✅ | ✅ |
| [Saleor API](https://docs.saleor.io/api-reference/) | Open-source headless commerce; GraphQL-first, products, checkout | 🟡 API Key | ✅ | ✅⭐ |
| [Square API](https://developer.squareup.com/) | Commerce platform; payments, catalog, inventory, orders, customers | 🔴 OAuth | ✅ | ✅⭐ |
| [API2Cart](https://api2cart.com/docs/) | Unified API connecting 60+ e-commerce platforms in one integration | 🟡 API Key | ✅ | ✅ |
| [Stripe API](https://stripe.com/docs/api) | Payment processing; charges, subscriptions, customers, invoices | 🟡 API Key | ✅ | ✅⭐ |

---

## 🎬 Media Encoding & Transcoding APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Mux API](https://www.mux.com/docs/core/make-api-requests) | API-first video platform; upload, encode, stream, and analytics | 🟡 API Key | ✅ | ✅⭐ |
| [Cloudinary API](https://cloudinary.com/documentation) | Image and video management; upload, transform, optimize, deliver | 🟡 API Key | ✅ | ✅⭐ |
| [Coconut API](https://www.coconut.co/features/coconut-api) | Cloud video encoding; 99% codec support, HLS/DASH, 4K Ultrafast | 🟡 API Key | ✅ | ✅⭐ |
| [Bitmovin API](https://developer.bitmovin.com/) | Enterprise video encoding; per-title optimization, multi-codec, DRM | 🟡 API Key | ✅ | ✅⭐ |
| [Transloadit API](https://transloadit.com/) | File processing engine; video encoding, image resize, document convert | 🟡 API Key | ✅ | ✅⭐ |
| [Cloudflare Stream API](https://developers.cloudflare.com/stream/) | Video upload, encode, store, and deliver via Cloudflare edge network | 🟡 API Key | ✅ | ✅⭐ |
| [Vimeo API](https://developer.vimeo.com/) | Video hosting platform; upload, transcode, embed, analytics | 🔴 OAuth | ✅ | ✅ |
| [JW Player API](https://developer.jwplayer.com/jwplayer/docs) | Video player and hosting; upload, manage, stream, analytics | 🟡 API Key | ✅ | ✅ |
| [Wistia API](https://docs.wistia.com/) | Business video hosting; upload, embed, customization, analytics | 🟡 API Key | ✅ | ✅ |

---

## 🧘 Mental Health & Wellness APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Sahha API](https://sahha.ai/) | Unified health and wellness API; mood, sleep, activity from 100+ wearables | 🟡 API Key | ✅ | ✅⭐ |
| [Terra API](https://docs.tryterra.co) | Unified wearable health data API; 150+ device integrations | 🟡 API Key | ✅ | ✅⭐ |
| [Fitbit Web API](https://dev.fitbit.com/build/reference/web-api/) | Activity, heart rate, sleep, nutrition data from Fitbit devices | 🔴 OAuth | ✅ | ✅⭐ |
| [WHOOP API](https://developer.whoop.com/api/) | Recovery, strain, sleep, and workout data from WHOOP wearable | 🔴 OAuth | ✅ | ✅ |
| [Oura Ring API](https://cloud.ouraring.com/v2/docs) | Sleep, readiness, and activity data from Oura smart ring | 🔴 OAuth | ✅ | ✅ |

---

## 🌐 Metaverse & Virtual Reality APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Meta Quest / Horizon API](https://developers.meta.com/horizon/reference/) | Meta Quest VR headset development; Spatial SDK, Mixed Reality | 🟡 API Key | ✅ | ✅ |
| [OpenXR API](https://www.khronos.org/openxr/) | Khronos royalty-free open standard for cross-platform XR development | 🟢 No | ✅ | ✅⭐ |
| [Roblox Open Cloud API](https://create.roblox.com/docs/cloud/reference) | Roblox platform APIs; datastores, assets, messaging, place management | 🟡 API Key | ✅ | ✅⭐ |
| [Decentraland SDK/API](https://developers.decentraland.org/) | Open metaverse platform; build 3D scenes, manage LAND, Ethereum txns | 🟡 API Key | ✅ | ✅ |
| [WebXR Device API](https://immersiveweb.dev/) | W3C standard for VR/AR in web browsers; sessions, input, rendering | 🟢 No | ✅ | ✅⭐ |
| [NVIDIA Omniverse API](https://docs.omniverse.nvidia.com/) | 3D simulation and collaboration platform; Python API, USD, extensions | 🟡 API Key | ✅ | ✅ |
| [A-Frame](https://aframe.io/) | Declarative HTML framework for WebVR/WebXR built on three.js | 🟢 No | ✅ | ✅ |
| [Babylon.js XR](https://doc.babylonjs.com/) | JavaScript 3D engine with built-in WebXR support | 🟢 No | ✅ | ✅ |

---

## ⛏️ Mining & Natural Resources APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Metals-API](https://metals-api.com/) | LME precious and base metals prices; real-time and historical rates | 🟡 API Key | ✅ | ✅⭐ |
| [MetalpriceAPI](https://metalpriceapi.com/) | Gold, silver, platinum, palladium prices in 170+ currencies | 🟡 API Key | ✅ | ✅⭐ |
| [GoldAPI.io](https://www.goldapi.io/) | Free real-time gold and silver spot prices via REST JSON API | 🟡 API Key | ✅ | ✅⭐ |
| [Commodities-API](https://commodities-api.com/) | Real-time commodity prices for 100+ commodities; oil, gold, gas, coffee | 🟡 API Key | ✅ | ✅⭐ |
| [Nasdaq Data Link (Quandl)](https://docs.data.nasdaq.com/) | Financial and commodity data; metals, energy, agriculture prices | 🟡 API Key | ✅ | ✅⭐ |
| [USGS Mineral Resources API](https://mrdata.usgs.gov/catalog/api.php) | U.S. geological mineral data; deposits, geochemistry, spatial data | 🟢 No | ✅ | ✅ |
| [World Bank Data API](https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information) | Global development data including commodity prices and resources | 🟢 No | ✅ | ✅⭐ |
| [OpenEI API](https://openei.org/wiki/OpenEI:API) | Open Energy Information; energy resources, utility rates, geolocations | 🟡 API Key | ✅ | ✅ |

---

## 📦 Package Tracking & Shipment APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [AfterShip Tracking API](https://www.aftership.com/docs/tracking/quickstart/api-quick-start) | Track shipments across 1,000+ carriers worldwide; webhooks support | 🟡 API Key | ✅ | ✅⭐ |
| [EasyPost API](https://docs.easypost.com/) | Multi-carrier shipping; rates, labels, tracking, address verification | 🟡 API Key | ✅ | ✅⭐ |
| [Shippo API](https://docs.goshippo.com/) | 85+ carrier aggregator; labels, tracking, returns, customs docs | 🟡 API Key | ✅ | ✅⭐ |
| [ShipStation API](https://docs.shipstation.com/) | Order management and shipping; 70+ sales channels, label printing | 🟡 API Key | ✅ | ✅⭐ |
| [ShipEngine API](https://www.shipengine.com/docs/) | Multi-carrier shipping; 100+ carriers, rates, labels, tracking webhooks | 🟡 API Key | ✅ | ✅⭐ |
| [FedEx API](https://developer.fedex.com/api/en-us/home.html) | Official FedEx; rates, ship, track, address validation, pickup | 🟡 API Key | ✅ | ✅ |
| [UPS API](https://developer.ups.com/) | Official UPS; shipping, tracking, rating, time in transit | 🟡 API Key | ✅ | ✅ |
| [USPS API](https://developers.usps.com/) | Official USPS; tracking, pricing, labels, address verification | 🟡 API Key | ✅ | ✅ |
| [DHL API](https://developer.dhl.com/) | Official DHL; shipment, tracking, location finder across DHL divisions | 🟡 API Key | ✅ | ✅ |
| [17TRACK API](https://api.17track.net/en/doc) | Global package tracking across 2,600+ carriers worldwide | 🟡 API Key | ✅ | ✅ |

---

## 🅿️ Parking & Mobility APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [SpotHero API](https://spothero.com/developers) | Parking marketplace; search, reserve parking garages and lots | 🟡 API Key | ✅ | ✅⭐ |
| [INRIX Parking API](https://docs.inrix.com/) | On-street and off-street parking availability, pricing, reservations | 🟡 API Key | ✅ | ✅⭐ |
| [HERE Parking API](https://www.here.com/docs/bundle/off-street-parking-api-developer-guide/page/topics/overview.html) | Off-street parking locations, availability, pricing data globally | 🟡 API Key | ✅ | ✅⭐ |
| [TomTom Parking API](https://developer.tomtom.com/parking-availability-api/documentation/product-information/introduction) | Real-time parking availability for garages and surface lots | 🟡 API Key | ✅ | ✅⭐ |
| [Parkopedia API](https://business.parkopedia.com/parking-data) | 90M+ parking spaces globally in 90 countries; RESTful API or feed | 🟡 API Key | ✅ | ✅ |
| [Open Charge Map API](https://openchargemap.org/site/develop/api) | Global EV charging station registry; locations, availability, connectors | 🟢 No | ✅ | ✅⭐ |
| [Citymapper API](https://docs.external.citymapper.com/api/) | Multimodal transit routing; walk, bike, scooter, public transit directions | 🟡 API Key | ✅ | ✅ |
| [Mapbox Navigation API](https://docs.mapbox.com/api/navigation/) | Directions, traffic, turn-by-turn instructions; parking-relevant routing | 🟡 API Key | ✅ | ✅⭐ |

---

## 📄 PDF Generation & Manipulation APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [PDFShift API](https://docs.pdfshift.io) | Fast HTML/URL to PDF conversion via REST; Chromium-based rendering | 🟡 API Key | ✅ | ✅⭐ |
| [DocRaptor API](https://docraptor.com/documentation/api) | HTML to PDF/XLS via PrinceXML engine; 99.99% uptime, SOC 2 compliant | 🟡 API Key | ✅ | ✅⭐ |
| [PDF.co API](https://docs.pdf.co/) | PDF generation, conversion, splitting, merging, OCR, barcode, parsing | 🟡 API Key | ✅ | ✅⭐ |
| [Anvil PDF API](https://www.useanvil.com/docs/api/generate-pdf/) | Generate PDFs from HTML/CSS or Markdown; e-sign, fill templates | 🟡 API Key | ✅ | ✅⭐ |
| [PDFMonkey API](https://docs.pdfmonkey.io/references/api) | Generate PDFs from HTML templates with dynamic JSON data | 🟡 API Key | ✅ | ✅⭐ |
| [PDF Generator API](https://docs.pdfgeneratorapi.com/v4) | Drag-and-drop template editor; generate PDFs from JSON data | 🟡 API Key | ✅ | ✅⭐ |
| [Api2Pdf](https://www.api2pdf.com/) | HTML to PDF, URL to PDF, merge PDFs, Office to PDF via REST API | 🟡 API Key | ✅ | ✅ |
| [ConvertAPI](https://docs.convertapi.com/) | 300+ file format conversions including PDF; fast REST API service | 🟡 API Key | ✅ | ✅ |
| [Zamzar API](https://developers.zamzar.com/docs) | 1,100+ file conversions; PDF to/from Word, Excel, images, and more | 🟡 API Key | ✅ | ✅ |
| [Nutrient (PSPDFKit) API](https://www.nutrient.io/api/) | PDF SDK and cloud API; viewing, editing, signing, AI processing | 🟡 API Key | ✅ | ✅⭐ |

---

## 🔮 Predictive Analytics & ML Ops APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [DataRobot](https://docs.datarobot.com/en/docs/api/index.html) | Automated ML platform with model deployment, monitoring, and prediction APIs | 🟡 API Key | ✅ | ✅⭐ |
| [H2O.ai](https://docs.h2o.ai/) | Open-source ML platform with AutoML, model training, and scoring REST endpoints | 🟡 API Key | ✅ | ✅ |
| [MLflow](https://www.mlflow.org/docs/latest/rest-api.html) | Open-source MLOps platform for experiment tracking, model registry, and serving | 🟢 No | ✅ | ✅⭐ |
| [Weights & Biases](https://docs.wandb.ai/) | Experiment tracking, model registry, and inference APIs for ML teams | 🟡 API Key | ✅ | ✅⭐ |
| [Neptune.ai](https://docs.neptune.ai/api/) | Experiment tracker with Query API for logging and fetching ML metadata | 🟡 API Key | ✅ | ✅ |
| [ClearML](https://clear.ml/docs/latest/docs/references/api/) | Open-source MLOps with REST API for experiment tracking and orchestration | 🟡 API Key | ✅ | ✅⭐ |
| [BentoML](https://docs.bentoml.com/) | Open-source framework for packaging and deploying ML models as REST endpoints | 🟢 No | ✅ | ✅⭐ |
| [Google Vertex AI](https://cloud.google.com/vertex-ai/docs/reference/rest) | Google Cloud ML platform with AutoML, custom training, and prediction endpoints | 🔴 OAuth | ✅ | ✅⭐ |
| [Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/APIReference/) | AWS ML platform with training, batch transform, and real-time inference | 🟡 API Key | ✅ | ✅⭐ |
| [Azure Machine Learning](https://learn.microsoft.com/en-us/rest/api/azureml/) | Microsoft cloud ML platform with model training, deployment, and endpoints | 🔴 OAuth | ✅ | ✅⭐ |
| [Databricks MLflow](https://docs.databricks.com/api/workspace/experiments) | Managed MLflow on Databricks with experiment tracking and model serving | 🟡 API Key | ✅ | ✅⭐ |
| [ZenML](https://docs.zenml.io/api-reference) | Open-source MLOps framework for reproducible ML pipelines with REST API | 🟡 API Key | ✅ | ✅ |

---

## 💲 Pricing & Revenue Optimization APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Prisync](https://prisync.com/api) | Competitor price tracking and dynamic pricing API for e-commerce | 🟡 API Key | ✅ | ✅⭐ |
| [Price2Spy](https://www.price2spy.com/api.html) | Competitive price monitoring REST API with Swagger documentation | 🟡 API Key | ✅ | ✅ |
| [Stripe Billing](https://docs.stripe.com/api) | Subscription billing, invoicing, usage-based pricing, and revenue recovery | 🟡 API Key | ✅ | ✅⭐ |
| [Chargebee](https://apidocs.chargebee.com/) | Subscription management and recurring billing REST API | 🟡 API Key | ✅ | ✅⭐ |
| [Zuora](https://developer.zuora.com/) | Enterprise subscription billing with REST APIs for dynamic pricing models | 🟡 API Key | ✅ | ✅⭐ |
| [Paddle](https://developer.paddle.com/api-reference/overview) | Payments and billing platform with subscription and pricing APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Recurly](https://recurly.com/developers/api/) | Subscription and billing management with comprehensive REST API (v3) | 🟡 API Key | ✅ | ✅⭐ |
| [Lago](https://www.getlago.com/docs/api-reference) | Open-source usage-based billing API with metering and invoicing endpoints | 🟡 API Key | ✅ | ✅⭐ |
| [Pricefx](https://www.pricefx.com/) | Cloud-native pricing software with APIs for price optimization and CPQ | 🟡 API Key | ✅ | ✅ |

---

## 🏘️ Property Management APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [AppFolio](https://www.appfolio.com/stack/partners/api) | Property management API for rentals, accounting, and maintenance workflows | 🟡 API Key | ✅ | ✅ |
| [Buildium](https://www.buildium.com/features/open-api/) | Open API for property and accounting data with tenant and lease management | 🟡 API Key | ✅ | ✅⭐ |
| [Entrata](https://docs.entrata.com/api/v1/documentation) | Modernized API gateway for multifamily property management operations | 🟡 API Key | ✅ | ✅⭐ |
| [Propertyware](https://www.propertyware.com/open-api/) | Open API for single-family property management data and workflows | 🟡 API Key | ✅ | ✅ |
| [Propexo](https://propexo.com/) | Unified API aggregator for property management system integrations | 🟡 API Key | ✅ | ✅⭐ |
| [Guesty](https://docs.guesty.com/) | Vacation rental and short-term property management with REST API | 🟡 API Key | ✅ | ✅⭐ |
| [Hostaway](https://api.hostaway.com/) | Vacation rental management platform with comprehensive REST API | 🟡 API Key | ✅ | ✅⭐ |
| [Lodgify](https://docs.lodgify.com/) | Vacation rental software with REST API for property, booking, and rate management | 🟡 API Key | ✅ | ✅ |

---

## 🔒 Privacy & Data Protection APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [OneTrust](https://developer.onetrust.com/onetrust/reference/onetrust-api-reference) | Comprehensive privacy platform API for consent, DSAR, and data governance | 🟡 API Key | ✅ | ✅⭐ |
| [BigID](https://docs.bigid.com/) | Data intelligence API for discovery, classification, and privacy compliance | 🟡 API Key | ✅ | ✅ |
| [Transcend](https://docs.transcend.io/docs/api-reference) | Privacy platform API for data subject requests, consent, and data mapping | 🟡 API Key | ✅ | ✅⭐ |
| [Osano](https://developers.osano.com/) | Privacy compliance platform with Customer REST API and consent JS API | 🟡 API Key | ✅ | ✅⭐ |
| [Didomi](https://developers.didomi.io/) | Consent management platform API for collecting and managing user preferences | 🟡 API Key | ✅ | ✅⭐ |
| [DataGrail](https://www.datagrail.io/) | Automated data subject request API integrating with 100+ business systems | 🟡 API Key | ✅ | ✅ |
| [Ketch](https://www.ketch.com/) | Privacy orchestration platform API for consent, rights, and data governance | 🟡 API Key | ✅ | ✅ |
| [Ethyca/Fides](https://docs.ethyca.com/) | Open-source privacy engineering platform with REST API for data privacy | 🟡 API Key | ✅ | ✅⭐ |

---

## 🎙️ Public Speaking & Presentation APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Google Slides API](https://developers.google.com/workspace/slides/api/reference/rest) | Create, read, and edit Google Slides presentations programmatically | 🔴 OAuth | ✅ | ✅⭐ |
| [Microsoft Graph - PowerPoint](https://learn.microsoft.com/en-us/graph/api/resources/presentation) | Create and manage PowerPoint files via Microsoft 365 cloud APIs | 🔴 OAuth | ✅ | ✅⭐ |
| [Canva API](https://www.canva.com/developers/) | Design platform Apps SDK for creating and manipulating presentations | 🔴 OAuth | ✅ | ✅⭐ |
| [SlideSpeak API](https://slidespeak.co/slidespeak-api) | AI presentation API for generating and summarizing PowerPoint presentations | 🟡 API Key | ✅ | ✅⭐ |
| [Aspose.Slides Cloud](https://reference.aspose.cloud/slides/) | Cloud REST API for creating, editing, and converting PowerPoint files | 🟡 API Key | ✅ | ✅⭐ |
| [FlashDocs](https://www.flashdocs.com/) | AI-powered API for generating PowerPoint presentations from data | 🟡 API Key | ✅ | ✅⭐ |
| [PowerPoint Generator API](https://powerpointgeneratorapi.com/) | Template-based PowerPoint generation from JSON data via REST API | 🟡 API Key | ✅ | ✅ |

---

## 🤖 Robotic Process Automation (RPA) APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [UiPath Orchestrator](https://docs.uipath.com/orchestrator/automation-cloud/latest/api-guide/introduction) | OData v4 REST API for managing robots, jobs, queues, and schedules | 🟡 API Key | ✅ | ✅⭐ |
| [Automation Anywhere](https://docs.automationanywhere.com/bundle/enterprise-v2019/page/enterprise-cloud/topics/control-room/control-room-api/cloud-control-room-apis.html) | Control Room REST API for bot deployment and workload management | 🟡 API Key | ✅ | ✅⭐ |
| [Microsoft Power Automate](https://learn.microsoft.com/en-us/power-automate/web-api) | Cloud flow automation with connectors and REST API via Microsoft Graph | 🔴 OAuth | ✅ | ✅⭐ |
| [Nintex](https://developer.nintex.com/) | Workflow automation platform with REST API for process and forms management | 🟡 API Key | ✅ | ✅⭐ |
| [Zapier](https://platform.zapier.com/) | Workflow automation platform with REST API and webhook-based triggers | 🟡 API Key | ✅ | ✅⭐ |
| [Make (Integromat)](https://www.make.com/en/api-documentation) | Visual automation platform with API for scenarios, data stores, and webhooks | 🟡 API Key | ✅ | ✅⭐ |
| [n8n](https://docs.n8n.io/api/) | Open-source workflow automation with REST API for execution and management | 🟡 API Key | ✅ | ✅⭐ |
| [Temporal](https://docs.temporal.io/) | Open-source workflow engine with gRPC and REST APIs for durable execution | 🟡 API Key | ✅ | ✅⭐ |

---

## 🛰️ Satellite & Remote Sensing APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Sentinel Hub](https://docs.sentinel-hub.com/api/latest/) | RESTful API for processing Sentinel, Landsat, and commercial satellite imagery | 🟡 API Key | ✅ | ✅⭐ |
| [Planet](https://developers.planet.com/docs/apis/) | High-cadence satellite imagery API with daily global coverage and analytics | 🟡 API Key | ✅ | ✅⭐ |
| [Maxar](https://developers.maxar.com/docs) | High-resolution satellite imagery API for ordering and streaming data | 🟡 API Key | ✅ | ✅ |
| [NASA Earthdata](https://www.earthdata.nasa.gov/engage/open-data-services-software/earthdata-developer-portal) | Portal for NASA satellite data, GIBS imagery, and CMR search APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Copernicus Data Space](https://documentation.dataspace.copernicus.eu/APIs.html) | European satellite data ecosystem with REST APIs for Sentinel data | 🟡 API Key | ✅ | ✅⭐ |
| [UP42](https://up42.com/) | Geospatial platform with APIs and Python SDK for satellite imagery access | 🟡 API Key | ✅ | ✅⭐ |
| [Arlula](https://www.arlula.com/documentation/) | Single-integration satellite imagery API aggregating global providers | 🟡 API Key | ✅ | ✅⭐ |
| [Google Earth Engine](https://developers.google.com/earth-engine/reference/rest) | Planetary-scale geospatial analysis platform with REST and Python APIs | 🔴 OAuth | ✅ | ✅⭐ |
| [NASA Open APIs](https://api.nasa.gov/) | Collection of NASA APIs including EPIC, Mars Rover imagery, and DONKI | 🟡 API Key | ✅ | ✅⭐ |

---

## 🔍 SEO & Web Analytics APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Ahrefs](https://ahrefs.com/api) | Backlink analysis, keyword research, and site audit data via REST API | 🟡 API Key | ✅ | ✅⭐ |
| [SEMrush](https://developer.semrush.com/api/) | Analytics, position tracking, and site audit APIs for SEO and SEM data | 🟡 API Key | ✅ | ✅⭐ |
| [Moz](https://moz.com/products/api) | Domain Authority, backlinks, and keyword data via Moz Links API | 🟡 API Key | ✅ | ✅⭐ |
| [Google Search Console](https://developers.google.com/webmaster-tools) | Search performance, URL inspection, and sitemap management APIs | 🔴 OAuth | ✅ | ✅⭐ |
| [DataForSEO](https://docs.dataforseo.com/) | Comprehensive SEO data APIs for SERP, backlinks, keywords, and on-page | 🟡 API Key | ✅ | ✅⭐ |
| [SerpApi](https://serpapi.com/) | Real-time SERP data from Google, Bing, Yahoo, and other search engines | 🟡 API Key | ✅ | ✅⭐ |
| [Google PageSpeed Insights](https://developers.google.com/speed/docs/insights/v5/get-started) | Web performance analysis API with Core Web Vitals and Lighthouse data | 🟡 API Key | ✅ | ✅⭐ |
| [Google Analytics Data API](https://developers.google.com/analytics/devguides/reporting/data/v1) | GA4 reporting API for retrieving website traffic and user analytics data | 🔴 OAuth | ✅ | ✅⭐ |
| [Matomo](https://developer.matomo.org/api-reference/reporting-api) | Open-source web analytics with comprehensive reporting and management APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Plausible Analytics](https://plausible.io/docs/stats-api) | Privacy-friendly, cookieless web analytics with Stats API | 🟡 API Key | ✅ | ✅⭐ |

---

## 🎵 Sound & Audio Processing APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Dolby.io Media APIs](https://docs.dolby.io/media-apis/docs) | Cloud APIs for audio analysis, enhancement, transcoding, and loudness correction | 🟡 API Key | ✅ | ✅⭐ |
| [AudioStack](https://docs.audiostack.ai/) | AI audio production API with 1750+ voices, mixing, mastering, and TTS | 🟡 API Key | ✅ | ✅⭐ |
| [ElevenLabs](https://elevenlabs.io/developers) | High-quality AI text-to-speech, voice cloning, and audio generation APIs | 🟡 API Key | ✅ | ✅⭐ |
| [AssemblyAI](https://www.assemblyai.com/docs/) | Speech-to-text API with speaker diarization, summaries, and audio intelligence | 🟡 API Key | ✅ | ✅⭐ |
| [Deepgram](https://developers.deepgram.com/) | Real-time and batch speech-to-text API with language detection | 🟡 API Key | ✅ | ✅⭐ |
| [Speechmatics](https://docs.speechmatics.com/api-ref) | Enterprise speech-to-text REST and WebSocket APIs with real-time transcription | 🟡 API Key | ✅ | ✅⭐ |
| [Resemble.ai](https://www.resemble.ai/) | AI voice cloning and emotional text-to-speech API with watermarking | 🟡 API Key | ✅ | ✅⭐ |
| [AudD](https://docs.audd.io/) | Music recognition API for identifying songs from audio clips | 🟡 API Key | ✅ | ✅⭐ |
| [Rev.ai](https://docs.rev.ai/) | Speech-to-text API with async and streaming transcription and diarization | 🟡 API Key | ✅ | ✅⭐ |

---

## 🏫 Student Information System APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [PowerSchool](https://support.powerschool.com/developer) | SIS REST API with Core API (students, grades, attendance) and Plugin API | 🔴 OAuth | ✅ | ✅⭐ |
| [Clever](https://dev.clever.com/) | Secure school data platform API for rostering, SSO, and SIS data sync | 🔴 OAuth | ✅ | ✅⭐ |
| [ClassLink](https://developer.classlink.com/) | OneRoster-based API for rostering, SSO, and identity management in K-12 | 🔴 OAuth | ✅ | ✅⭐ |
| [Edlink](https://ed.link/docs) | Unified API for LMS and SIS integrations across education platforms | 🟡 API Key | ✅ | ✅⭐ |
| [Aeries](https://support.aeries.com/support/solutions/articles/14000113683-aeries-api-student-related-end-points) | California K-12 SIS with REST API for student, enrollment, and grade data | 🟡 API Key | ✅ | ✅⭐ |
| [Blackbaud SKY API](https://developer.sky.blackbaud.com/) | Open REST API for K-12 school management, enrollment, and student records | 🔴 OAuth | ✅ | ✅⭐ |
| [Canvas LMS](https://developerdocs.instructure.com/services/canvas) | Learning management system REST API with SIS integration and grade passback | 🔴 OAuth | ✅ | ✅⭐ |
| [Schoology](https://developers.schoology.com/api/) | LMS API for courses, assignments, grades, and SIS rostering integration | 🔴 OAuth | ✅ | ✅⭐ |

---

## 🔧 API Gateway & Management APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Kong Gateway Admin API](https://docs.konghq.com/gateway/api/admin-oss/latest/) | Open-source API gateway with RESTful admin API for full gateway control | 🟡 API Key | ✅ | ✅ |
| [AWS API Gateway](https://docs.aws.amazon.com/apigateway/latest/api/API_Operations.html) | Fully managed gateway for creating and managing REST/WebSocket APIs | 🟡 API Key | ✅ | ✅ |
| [Tyk Gateway API](https://tyk.io/docs/tyk-gateway-api/) | Open-source API gateway with REST API for managing APIs, keys, and policies | 🟡 API Key | ✅ | ✅ |
| [Apache APISIX Admin API](https://apisix.apache.org/docs/apisix/admin-api/) | High-performance cloud-native API gateway processing 1T+ API calls daily | 🟡 API Key | ✅ | ✅ |
| [KrakenD API Gateway](https://www.krakend.io/docs/overview/) | Ultra-high-performance stateless API gateway with declarative config | 🟢 No | ✅ | ✅⭐ |
| [Traefik API](https://doc.traefik.io/traefik/) | Cloud-native API gateway with automatic service discovery | 🟡 API Key | ✅ | ✅ |
| [Zuplo API Gateway](https://zuplo.com/docs) | Programmable API gateway with built-in developer portal | 🟡 API Key | ✅ | ✅ |
| [Gravitee Management API](https://documentation.gravitee.io/apim/management-api-reference) | Open-source API management platform with RESTful management endpoints | 🟡 API Key | ✅ | ✅ |

---

## 🎨 Design & Prototyping APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Figma REST API](https://developers.figma.com/) | Access Figma files, comments, components, and design tokens | 🔴 OAuth | ✅ | ✅⭐ |
| [Canva Connect API](https://www.canva.dev/docs/connect/) | Create, manage, and sync designs, assets, and comments in Canva | 🔴 OAuth | ✅ | ✅ |
| [Penpot API](https://help.penpot.app/plugins/api/) | Open-source design platform with webhooks and access token-based API | 🟡 API Key | ✅ | ✅⭐ |
| [IconScout API](https://iconscout.com/developers) | Access millions of icons, illustrations, and 3D assets via API | 🟡 API Key | ✅ | ✅⭐ |
| [Lottie Files API](https://lottiefiles.com/developers) | Search, retrieve, and manage Lottie animations programmatically | 🟡 API Key | ✅ | ✅⭐ |
| [Zeplin API](https://docs.zeplin.dev/reference) | Access design specs, style guides, and components for developer handoff | 🔴 OAuth | ✅ | ✅ |
| [Framer Developer API](https://www.framer.com/developers/reference) | Build apps that interact with the Framer Editor and CMS content | 🟡 API Key | ✅ | ✅ |

---

## 🔌 IoT Platform & Device Management APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [AWS IoT Core API](https://docs.aws.amazon.com/iot/latest/apireference/Welcome.html) | Secure bi-directional communication between IoT devices and AWS cloud | 🟡 API Key | ✅ | ✅ |
| [ThingSpeak API](https://thingspeak.com/docs) | Free open-source IoT analytics platform for sensor data | 🟡 API Key | ✅ | ✅⭐ |
| [Home Assistant REST API](https://developers.home-assistant.io/docs/api/rest/) | Open-source home automation platform with RESTful and WebSocket APIs | 🟡 API Key | ✅ | ✅⭐ |
| [ThingsBoard API](https://thingsboard.io/docs/reference/rest-api/) | Open-source IoT platform with device management and data collection | 🟡 API Key | ✅ | ✅⭐ |
| [Adafruit IO API](https://io.adafruit.com/api/docs/) | Cloud service for storing, sharing, and visualizing IoT sensor data | 🟡 API Key | ✅ | ✅⭐ |
| [Particle Cloud API](https://docs.particle.io/reference/cloud-apis/api/) | Secure IoT connectivity platform with comprehensive device management | 🔴 OAuth | ✅ | ✅ |
| [Tuya IoT Open API](https://developer.tuya.com/en/docs/iot/open-apis?id=Kaiuyvvxud2le) | Manage smart home devices and IoT hardware across Tuya's ecosystem | 🟡 API Key | ✅ | ✅ |
| [Blynk API](https://docs.blynk.io/en/) | Low-code IoT platform supporting 400+ hardware boards | 🟡 API Key | ✅ | ✅ |
| [Balena API](https://docs.balena.io/reference/api/overview/) | IoT fleet management with OData-based REST API | 🟡 API Key | ✅ | ✅ |

---

## 📡 Telecommunications APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Twilio API](https://www.twilio.com/docs/usage/api) | Industry-leading APIs for SMS, voice, video, and WhatsApp messaging | 🟡 API Key | ✅ | ✅⭐ |
| [Vonage (Nexmo) API](https://developer.vonage.com/) | Communication APIs for SMS, MMS, voice across 225 countries | 🟡 API Key | ✅ | ✅ |
| [Plivo API](https://www.plivo.com/docs/) | Budget-friendly SMS and voice APIs with 1,600+ global operators | 🟡 API Key | ✅ | ✅ |
| [Sinch API](https://developers.sinch.com/) | REST APIs for voice, SMS, and messaging with native SDK support | 🟡 API Key | ✅ | ✅ |
| [Bandwidth API](https://dev.bandwidth.com/docs/) | Voice, messaging, and 911 APIs with dedicated US telephony | 🟡 API Key | ✅ | ✅ |
| [Telnyx API](https://developers.telnyx.com/) | Low-latency voice, SMS, fax, and IP services with global network | 🟡 API Key | ✅ | ✅ |
| [Infobip API](https://www.infobip.com/docs/api) | CPaaS APIs for SMS, voice, email, WhatsApp, and Viber | 🟡 API Key | ✅ | ✅ |
| [Africa's Talking API](https://developers.africastalking.com/) | Communication APIs for SMS, voice, USSD, and airtime built for Africa | 🟡 API Key | ✅ | ✅⭐ |

---

## 🏋️ Fitness & Gym APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Strava API](https://developers.strava.com/docs/reference/) | Access athlete activities, routes, clubs, gear, and segment data | 🔴 OAuth | ✅ | ✅⭐ |
| [Terra Fitness API](https://docs.tryterra.co/) | Unified API aggregating 500+ health data sources from wearables | 🟡 API Key | ✅ | ✅⭐ |
| [Mindbody API](https://developers.mindbodyonline.com/) | Fitness studio API for scheduling, client management, and payments | 🔴 OAuth | ✅ | ✅ |
| [Peloton API](https://peloton.readthedocs.io/en/latest/api-guide/) | Workout and membership data from Peloton connected fitness | 🟡 API Key | ✅ | ✅ |
| [Polar AccessLink API](https://www.polar.com/accesslink-api/) | Access training, activity, and physical data from Polar wearables | 🔴 OAuth | ✅ | ✅ |
| [Garmin Health API](https://developer.garmin.com/health-api/overview/) | Historical and real-time fitness data with webhook delivery | 🔴 OAuth | ✅ | ⚠️ |

---

## 📰 Newsletter & Content APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Mailchimp Marketing API](https://mailchimp.com/developer/marketing/api/) | Full-featured email marketing API for campaigns, lists, and automation | 🔴 OAuth | ✅ | ✅⭐ |
| [SendGrid API](https://docs.sendgrid.com/api-reference) | Scalable email API for transactional and marketing email delivery | 🟡 API Key | ✅ | ✅⭐ |
| [Ghost Content API](https://docs.ghost.org/) | Headless CMS with Content and Admin APIs for posts and members | 🟡 API Key | ✅ | ✅⭐ |
| [Buttondown API](https://docs.buttondown.com/api-introduction) | Simple RESTful newsletter API for emails and subscribers | 🟡 API Key | ✅ | ✅⭐ |
| [Postmark API](https://postmarkapp.com/developer) | Fast transactional email delivery with detailed analytics | 🟡 API Key | ✅ | ✅⭐ |
| [Mailgun API](https://documentation.mailgun.com/docs/mailgun/api-reference/) | Powerful email API for sending, receiving, and tracking at scale | 🟡 API Key | ✅ | ✅⭐ |
| [ConvertKit (Kit) API](https://developers.kit.com/welcome) | Creator-focused email API for forms, sequences, and subscribers | 🟡 API Key | ✅ | ✅ |
| [Beehiiv API](https://www.beehiiv.com/features/api-and-integrations) | RESTful newsletter API for subscribers and publication management | 🟡 API Key | ✅ | ✅ |

---

## 🎤 Event & Conference APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Eventbrite API](https://www.eventbrite.com/platform/api) | Full REST API for creating, managing, and searching events | 🔴 OAuth | ✅ | ✅⭐ |
| [Bizzabo API](https://bizzabo.stoplight.io/docs/bizzabo-rest-api/) | Event experience OS API for registration and attendee management | 🟡 API Key | ✅ | ✅ |
| [Cvent Developer API](https://developers.cvent.com/docs) | Enterprise event management API with CRM integration | 🔴 OAuth | ✅ | ✅ |
| [Luma API](https://help.luma.com/p/luma-api) | Event management API for creating and automating events | 🟡 API Key | ✅ | ✅ |
| [Meetup API](https://www.meetup.com/api/) | Access Meetup groups, events, venues, and RSVP data | 🔴 OAuth | ✅ | ✅ |
| [Zoom Meetings API](https://developers.zoom.us/docs/api/) | Create, manage, and customize Zoom meetings and webinars | 🔴 OAuth | ✅ | ✅ |

---

## 🔬 Laboratory & LIMS APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Benchling API](https://benchling.com/api/reference) | Life science data management with CRUD for notebooks and sequences | 🔴 OAuth | ✅ | ✅⭐ |
| [elabFTW API](https://doc.elabftw.net/api.html) | Open-source electronic lab notebook with full REST API | 🟡 API Key | ✅ | ✅⭐ |
| [Sapio Sciences API](https://www.sapiosciences.com/) | Unified LIMS + ELN platform with workflow designers and REST APIs | 🟡 API Key | ✅ | ✅ |
| [Scispot API](https://www.scispot.com/) | API-first lab platform with uniform schema across ELN and LIMS | 🟡 API Key | ✅ | ✅ |
| [eLabNext Developer API](https://developer.elabnext.com/) | RESTful API for electronic lab notebook and LIMS modules | 🟡 API Key | ✅ | ✅ |
| [CloudLIMS API](https://cloudlims.com/) | REST API for samples, subjects, and inventory management | 🟡 API Key | ✅ | ✅ |

---

## 🏨 Hospitality & Hotel Management APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Mews Open API](https://www.mews.com/en/developers) | Modern hospitality cloud API for payments and guest experience | 🟡 API Key | ✅ | ✅⭐ |
| [Apaleo Open API](https://apaleo.dev/index.html) | API-first open hospitality PMS with self-provisioned API keys | 🔴 OAuth | ✅ | ✅⭐ |
| [Amadeus Hotel API](https://developers.amadeus.com/self-service/category/hotels) | Hotel search, booking, and content APIs powered by GDS data | 🟡 API Key | ✅ | ✅⭐ |
| [Cloudbeds API](https://developers.cloudbeds.com/) | PMS, channel manager, and booking engine API with 300+ endpoints | 🔴 OAuth | ✅ | ✅ |
| [Expedia Rapid API](https://developers.expediagroup.com/docs) | Access 600,000+ hotel properties with booking and content APIs | 🟡 API Key | ✅ | ✅ |
| [TripAdvisor Content API](https://www.tripadvisor.com/developers) | Access traveler reviews, ratings, photos, and destination content | 🟡 API Key | ✅ | ✅ |

---

## 🚗 Automotive & Vehicle APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [NHTSA Vehicle API](https://vpic.nhtsa.dot.gov/api/) | Free government API for VIN decoding and vehicle specs | 🟢 No | ✅ | ✅⭐ |
| [Smartcar API](https://smartcar.com/docs/api/) | Connected car API to read data and send commands to 40+ OEM brands | 🔴 OAuth | ✅ | ✅⭐ |
| [CarAPI](https://carapi.app/) | Year/make/model/trim data and 9,000+ OBD codes | 🟡 API Key | ✅ | ✅⭐ |
| [Fueleconomy.gov API](https://www.fueleconomy.gov/feg/ws/index.shtml) | Free US government API for vehicle fuel economy and emissions data | 🟢 No | ✅ | ✅⭐ |
| [Edmunds API](https://developer.edmunds.com/api-documentation/overview/) | Vehicle specs, pricing, reviews, and VIN decoding since 1990 | 🟡 API Key | ✅ | ✅ |
| [PlateRecognizer API](https://guides.platerecognizer.com/) | Automatic license plate recognition via cloud and on-premise APIs | 🟡 API Key | ✅ | ✅ |
| [CarsXE API](https://api.carsxe.com/) | VIN decoding, vehicle history, recalls, market value, and plate lookup | 🟡 API Key | ✅ | ✅ |

---

## 🎪 Ticketing & Venue APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Ticketmaster Discovery API](https://developer.ticketmaster.com/products-and-docs/apis/discovery-api/v2/) | Search events, attractions, and venues with 5,000 calls/day free | 🟡 API Key | ✅ | ✅⭐ |
| [SeatGeek Platform API](https://platform.seatgeek.com/) | RESTful API for events, performers, venues, and recommendations | 🟡 API Key | ✅ | ✅⭐ |
| [TicketsData API](https://ticketsdata.com/docs) | Unified API normalizing data from Ticketmaster, StubHub, SeatGeek | 🟡 API Key | ✅ | ✅⭐ |
| [StubHub API](https://developer.stubhub.com/docs/overview/introduction/) | Search events, purchase and list tickets on largest resale marketplace | 🔴 OAuth | ✅ | ✅ |
| [Ticket Tailor API](https://developers.tickettailor.com/) | Self-service event ticketing API with seat maps and box office | 🟡 API Key | ✅ | ✅ |

---

## 🛒 Grocery & Food Delivery APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [DoorDash Drive API](https://developer.doordash.com/en-US/api/drive/) | White-label delivery API using DoorDash courier network | 🟡 API Key | ✅ | ✅⭐ |
| [Spoonacular API](https://spoonacular.com/food-api) | 360,000+ recipes, 80,000+ food products, meal plans, and nutrition | 🟡 API Key | ✅ | ✅⭐ |
| [Open Food Facts API](https://world.openfoodfacts.org/data) | Free open-source food product database with nutrition and barcodes | 🟢 No | ✅ | ✅⭐ |
| [Edamam API](https://developer.edamam.com/) | Nutrition analysis, recipe search, food database, and meal planning | 🟡 API Key | ✅ | ✅⭐ |
| [Kroger API](https://developer.kroger.com/reference/) | Grocery shopping API for products, carts, and store locations | 🔴 OAuth | ✅ | ✅ |
| [Uber Direct API](https://developer.uber.com/docs/deliveries/overview) | White-label delivery-as-a-service using Uber's courier network | 🔴 OAuth | ✅ | ✅ |

---

## 🧮 Accounting Tax Compliance APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Avalara AvaTax](https://developer.avalara.com/) | Sales tax calculation, compliance, and filing with 1,200+ integrations | 🟡 API Key | ✅ | ✅⭐ |
| [TaxJar](https://developers.taxjar.com/api/) | Developer-friendly REST API for sales tax calculation and reporting | 🟡 API Key | ✅ | ✅⭐ |
| [Stripe Tax](https://docs.stripe.com/tax) | Automatic tax calculation built into Stripe payment flows | 🟡 API Key | ✅ | ✅⭐ |
| [TaxCloud](https://taxcloud.com/for-developers/) | Free-tier sales tax API for US-based small businesses | 🟡 API Key | ✅ | ✅⭐ |
| [Quaderno](https://developers.quaderno.io/) | Cross-border tax calculation, VAT/GST validation, and invoicing | 🟡 API Key | ✅ | ✅⭐ |
| [Fonoa](https://docs.fonoa.com/) | Tax automation API for real-time tax determination and e-invoicing | 🟡 API Key | ✅ | ✅ |
| [Vertex Cloud](https://developer.vertexinc.com/) | Enterprise tax calculation, address cleansing, and returns | 🟡 API Key | ✅ | ✅ |

---

## 📞 Contact Center & CCaaS APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Genesys Cloud](https://developer.genesys.cloud/) | Enterprise CCaaS platform API with full REST and SDK support | 🔴 OAuth | ✅ | ✅⭐ |
| [Twilio Flex](https://www.twilio.com/docs/flex) | Programmable cloud contact center with full UI and API customization | 🟡 API Key | ✅ | ✅⭐ |
| [Amazon Connect](https://docs.aws.amazon.com/connect/latest/APIReference/Welcome.html) | AWS cloud contact center service with comprehensive REST API | 🟡 API Key | ✅ | ✅⭐ |
| [Talkdesk](https://docs.talkdesk.com/) | CCaaS API with industry-specific solutions and embedded contact center | 🟡 API Key | ✅ | ✅⭐ |
| [Aircall](https://developer.aircall.io/) | Cloud-based phone system API for call center integrations | 🟡 API Key | ✅ | ✅⭐ |
| [Five9](https://www.five9.com/products/capabilities/call-center-apis-and-sdks) | Cloud contact center APIs and SDKs for voice, chat, and AI | 🟡 API Key | ✅ | ✅ |

---

## 🏗️ BIM & Architecture APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Autodesk Platform Services](https://aps.autodesk.com/) | 3D viewing, data management, design automation (formerly Forge) | 🔴 OAuth | ✅ | ✅⭐ |
| [Speckle](https://speckle.systems/) | Open-source AEC data platform with GraphQL and REST APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Procore](https://developers.procore.com/) | Construction management REST API for projects, financials, and docs | 🔴 OAuth | ✅ | ✅⭐ |
| [xeokit SDK](https://xeokit.io/) | Open-source 3D BIM viewer SDK with JavaScript API | 🟢 No | ✅ | ✅⭐ |
| [IFC.js / That Open Engine](https://github.com/ThatOpenCompany) | Open-source JavaScript library for loading and editing IFC models | 🟢 No | ✅ | ✅⭐ |
| [Bentley iTwin Platform](https://developer.bentley.com/) | Digital twin APIs for infrastructure with iModel services | 🔴 OAuth | ✅ | ✅ |

---

## 🎓 Online Learning Platform APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Canvas LMS API](https://canvas.instructure.com/doc/api/) | Full REST API for course management, grading, and user admin | 🔴 OAuth | ✅ | ✅⭐ |
| [Moodle Web Services](https://docs.moodle.org/en/Web_services) | Open-source LMS with extensive REST/SOAP/XML-RPC APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Google Classroom API](https://developers.google.com/workspace/classroom/reference/rest) | Manage classes, rosters, invitations, and coursework | 🔴 OAuth | ✅ | ✅⭐ |
| [CourseKit](https://coursekit.dev/) | Headless course platform with flexible API-first architecture | 🟡 API Key | ✅ | ✅⭐ |
| [Thinkific Admin API](https://developers.thinkific.com/api/api-documentation) | Manage courses, users, enrollments, and orders programmatically | 🟡 API Key | ✅ | ✅⭐ |
| [Skilljar API](https://api.skilljar.com/docs/) | Customer education LMS with REST API for courses and analytics | 🟡 API Key | ✅ | ✅ |

---

## 💎 Luxury & Fashion APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Retailed API](https://docs.retailed.io/) | Live product data from StockX, GOAT, Chrono24, and luxury markets | 🟡 API Key | ✅ | ✅⭐ |
| [KicksDB (Sneakers API)](https://kicks.dev/) | Structured sneaker data from StockX, GOAT, and Shopify stores | 🟡 API Key | ✅ | ✅⭐ |
| [Lykdat Fashion Search](https://apidocs.lykdat.com/) | Fashion image search, visual similarity, and deep tagging API | 🟡 API Key | ✅ | ✅⭐ |
| [Algolia Product Search](https://www.algolia.com/doc/) | AI-powered search API used by luxury fashion e-commerce | 🟡 API Key | ✅ | ✅⭐ |
| [StockX API](https://developer.stockx.com/) | Sneaker and luxury resale marketplace product and pricing data | 🔴 OAuth | ✅ | ✅ |

---

## 🏋️‍♂️ Sports Data & Odds APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Sportradar](https://developer.sportradar.com/) | Premium sports data, odds, and imagery for global leagues | 🟡 API Key | ✅ | ✅⭐ |
| [The Odds API](https://the-odds-api.com/) | Live and upcoming sports betting odds from 70+ bookmakers | 🟡 API Key | ✅ | ✅⭐ |
| [API-Football](https://www.api-football.com/) | RESTful football/soccer API with fixtures, standings, and stats | 🟡 API Key | ✅ | ✅⭐ |
| [balldontlie](https://www.balldontlie.io/) | NBA, NFL, MLB, NHL, EPL, MMA stats and historical data | 🟡 API Key | ✅ | ✅⭐ |
| [TheSportsDB](https://www.thesportsdb.com/documentation) | Free sports data API with live scores, stats, and team info | 🟡 API Key | ✅ | ✅⭐ |
| [Football-Data.org](https://www.football-data.org/) | Free football API with competitions, matches, and standings | 🟡 API Key | ✅ | ✅⭐ |

---

## 🌿 Cannabis & CBD APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Otreeba (Open Cannabis API)](https://otreeba.com/) | Open cannabis data API for strains, brands, products, and studies | 🟡 API Key | ✅ | ✅⭐ |
| [Cannabis Reports API](https://www.cannabisreports.com/api) | Open database of 20,000+ strains, products, and dispensaries | 🟡 API Key | ✅ | ✅⭐ |
| [METRC Open API](https://www.metrc.com/track-and-trace-technology/open-api/) | State-mandated seed-to-sale cannabis tracking and compliance | 🟡 API Key | ✅ | ✅ |
| [Dutchie Plus API](https://business.dutchie.com/integrations) | Cannabis e-commerce and POS platform with developer-first APIs | 🟡 API Key | ✅ | ✅ |

---

## 🔋 Battery & Energy Storage APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Tesla Fleet API (Energy)](https://developer.tesla.com/docs/fleet-api/endpoints/energy) | Control and monitor Tesla Powerwall and solar systems | 🔴 OAuth | ✅ | ✅⭐ |
| [Enphase Enlighten API](https://developer-v4.enphase.com/) | Solar and battery monitoring API with real-time and historical data | 🟡 API Key | ✅ | ✅⭐ |
| [Enode API](https://developers.enode.com/api) | Unified API connecting to 1,000+ energy devices (solar, battery, EV) | 🔴 OAuth | ✅ | ✅⭐ |
| [Sunvoy API](https://sunvoy.com/api) | Multi-brand energy device API: Enphase, SolarEdge, Tesla, and more | 🟡 API Key | ✅ | ✅⭐ |
| [NREL PVWatts API](https://developer.nrel.gov/docs/solar/pvwatts/) | Estimate PV energy production for grid-connected systems | 🟡 API Key | ✅ | ✅⭐ |

---

## 🎰 Casino & iGaming APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [SOFTSWISS Game Aggregator](https://www.softswiss.com/game-aggregator/) | 40,000+ games from 300+ studios via single API integration | 🟡 API Key | ✅ | ✅ |
| [SoftGamings Casino API](https://www.softgamings.com/casino-api/) | 10,000+ games from 250+ providers with unified API | 🟡 API Key | ✅ | ✅ |
| [Slotegrator APIgrator](https://slotegrator.pro/apigrator.html) | 30,000+ certified games from 180+ licensed developers | 🟡 API Key | ✅ | ✅ |
| [NuxGame Casino API](https://nuxgame.com/casino-api) | 16,500+ games from 130+ providers through single integration | 🟡 API Key | ✅ | ✅ |

---

## 📸 Computer Vision & Object Detection APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Roboflow Inference API](https://roboflow.com/) | Deploy custom CV models with pre-built detection, segmentation, OCR | 🟡 API Key | ✅ | ✅⭐ |
| [Google Cloud Vision API](https://cloud.google.com/vision/docs) | Image labeling, OCR, face detection, and landmark recognition | 🟡 API Key | ✅ | ✅⭐ |
| [Ultralytics YOLO (HUB)](https://hub.ultralytics.com/) | Train and deploy YOLO models via cloud with API endpoints | 🟡 API Key | ✅ | ✅⭐ |
| [Eden AI](https://www.edenai.co/) | Unified API aggregating Google, AWS, Azure, and other CV services | 🟡 API Key | ✅ | ✅⭐ |
| [Hugging Face Inference API](https://huggingface.co/docs/api-inference/) | 150,000+ pre-trained models including object detection | 🟡 API Key | ✅ | ✅⭐ |
| [Imagga](https://docs.imagga.com/) | Image tagging, categorization, color extraction, and face recognition | 🟡 API Key | ✅ | ✅ |

---

## 🧊 Cold Chain & Temperature Monitoring APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Tive API](https://developers.tive.com/) | Real-time shipment tracking with GPS and temperature sensors | 🟡 API Key | ✅ | ✅⭐ |
| [Particle IoT](https://docs.particle.io/) | IoT device cloud with REST API for sensor data and fleet management | 🟡 API Key | ✅ | ✅⭐ |
| [Controlant API](https://api-docs.controlant.com/) | Pharma cold chain as a service with REST API | 🟡 API Key | ✅ | ✅ |
| [SafetyCulture (iAuditor)](https://developer.safetyculture.com/) | Inspection and monitoring platform with temperature sensor API | 🟡 API Key | ✅ | ✅ |

---

## 🏛️ Museum & Cultural Heritage APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Europeana API](https://apis.europeana.eu/) | 50M+ items from 4,000+ European cultural institutions | 🟡 API Key | ✅ | ✅⭐ |
| [Smithsonian Open Access API](https://www.si.edu/openaccess/devtools) | 2.8M open-access items across all Smithsonian museums (CC0) | 🟡 API Key | ✅ | ✅⭐ |
| [Metropolitan Museum of Art API](https://metmuseum.github.io/) | 470,000+ artworks with images, metadata, and search | 🟢 No | ✅ | ✅⭐ |
| [Rijksmuseum API](https://data.rijksmuseum.nl/) | 500,000+ art objects with search and OAI-PMH APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Art Institute of Chicago API](https://www.artic.edu/open-access/public-api) | Unified API for collections, publications, events, and more | 🟢 No | ✅ | ✅⭐ |
| [Library of Congress API](https://www.loc.gov/apis/) | Digital collections, maps, photos, newspapers in JSON | 🟢 No | ✅ | ✅⭐ |
| [Harvard Art Museums API](https://harvardartmuseums.org/collections/api) | REST API for exploring extensive art collections | 🟡 API Key | ✅ | ✅⭐ |
| [Victoria & Albert Museum API](https://developers.vam.ac.uk/) | 1M+ collection records and 500K+ images with v2 REST API | 🟢 No | ✅ | ✅⭐ |

---

## 🔐 Encryption & Key Management APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [AWS KMS](https://docs.aws.amazon.com/kms/latest/APIReference/Welcome.html) | Fully managed encryption key creation, rotation, and control on AWS | 🟡 API Key | ✅ | ✅⭐ |
| [Google Cloud KMS](https://cloud.google.com/security/products/security-key-management) | Cloud-hosted key management with HSM and external key manager support | 🟡 API Key | ✅ | ✅⭐ |
| [Azure Key Vault](https://learn.microsoft.com/en-us/rest/api/keyvault/) | Safeguard cryptographic keys, certificates, and secrets on Azure | 🔴 OAuth | ✅ | ✅⭐ |
| [HashiCorp Vault](https://developer.hashicorp.com/vault/api-docs) | Open-source secrets management, encryption-as-a-service, and key management | 🟡 API Key | ✅ | ✅⭐ |
| [Doppler](https://docs.doppler.com/reference/api) | Centralized cloud-based secrets and environment variable management | 🟡 API Key | ✅ | ✅⭐ |
| [1Password Secrets Automation](https://developer.1password.com/docs/connect/api-reference/) | Programmatic access to secrets stored in 1Password vaults via REST API | 🟡 API Key | ✅ | ✅ |
| [CyberArk Conjur](https://docs.conjur.org/Latest/en/Content/Developer/lp_REST_API.htm) | Enterprise secrets management with policy-based access control | 🟡 API Key | ✅ | ✅ |
| [Akeyless](https://docs.akeyless.io/) | Vaultless secrets management with dynamic secrets and encryption | 🟡 API Key | ✅ | ✅ |
| [Google Tink](https://developers.google.com/tink) | Open-source multi-language cryptographic API library by Google | 🟢 No | ✅ | ✅ |
| [Virtru](https://developer.virtru.com/docs/cpp-encryption) | Data-centric encryption SDKs with granular access controls (TDF standard) | 🟡 API Key | ✅ | ⚠️ |
| [Fortanix SDKMS](https://support.fortanix.com/docs/) | Runtime encryption and cloud key management with HSM-grade security | 🟡 API Key | ✅ | ✅ |
| [Thales CipherTrust](https://thalesdocs.com/ctp/cm/latest/reference/index.html) | Enterprise data discovery, classification, encryption, and key management | 🟡 API Key | ✅ | ⚠️ |

---

## 🏥 EHR (Electronic Health Records) APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Epic on FHIR](https://fhir.epic.com/) | FHIR R4 APIs for Epic EHR with 750+ free endpoints and sandbox access | 🔴 OAuth | ✅ | ✅⭐ |
| [Oracle Health / Cerner FHIR](https://docs.oracle.com/en/industries/health/millennium-platform-apis/mfrap/r4_overview.html) | FHIR R4 APIs for Oracle Health (formerly Cerner) Millennium platform | 🔴 OAuth | ✅ | ✅⭐ |
| [Veradigm / Allscripts FHIR](https://developer.veradigm.com/) | FHIR-enabled APIs for Veradigm EHR and Practice Fusion systems | 🔴 OAuth | ✅ | ✅ |
| [SMART on FHIR](https://docs.smarthealthit.org/) | Open standard framework for FHIR app authorization and launch | 🔴 OAuth | ✅ | ✅⭐ |
| [HL7 FHIR](https://www.hl7.org/fhir/) | The foundational healthcare interoperability standard specification (R4/R5) | 🟢 No | ✅ | ✅⭐ |
| [CMS Blue Button 2.0](https://bluebutton.cms.gov/developers/) | Medicare beneficiary claims data via FHIR for 60M+ patients | 🔴 OAuth | ✅ | ✅⭐ |
| [Apple Health Records API](https://developer.apple.com/documentation/healthkit) | Access FHIR clinical records from participating institutions via HealthKit | 🔴 OAuth | ✅ | ✅ |
| [1up Health](https://1up.health/developers) | Unified FHIR API connecting to 300+ EHR systems for health data | 🔴 OAuth | ✅ | ✅ |
| [Redox](https://developer.redoxengine.com/) | Healthcare integration platform connecting apps to 2500+ EHR endpoints | 🟡 API Key | ✅ | ✅ |
| [Flexpa](https://www.flexpa.com/docs) | Patient-authorized access to health plan FHIR APIs for claims data | 🔴 OAuth | ✅ | ✅ |
| [Open Dental API](https://www.opendental.com/site/apiservice.html) | REST API for Open Dental practice management and clinical data | 🟡 API Key | ✅ | ✅ |
| [athenahealth API](https://docs.athenahealth.com/api/) | APIs for athenaOne EHR including clinical, scheduling, and billing data | 🔴 OAuth | ✅ | ✅ |

---

## 📚 Data Catalog & Metadata APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Google Cloud Data Catalog](https://docs.cloud.google.com/data-catalog/docs/reference/rest) | Fully managed metadata management and data discovery on GCP | 🔴 OAuth | ✅ | ✅⭐ |
| [OpenMetadata](https://docs.open-metadata.org/latest/main-concepts/metadata-standard/apis) | Open-source unified metadata platform with REST APIs for discovery and governance | 🟡 API Key | ✅ | ✅⭐ |
| [Apache Atlas](https://atlas.apache.org/api/v2/index.html) | Open-source metadata management and governance framework for Hadoop ecosystems | 🟡 API Key | ✅ | ✅ |
| [Collibra](https://developer.collibra.com/api) | Enterprise data intelligence platform with REST and GraphQL APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Alation](https://developer.alation.com/dev) | Data catalog with REST APIs for metadata, lineage, and governance | 🟡 API Key | ✅ | ✅ |
| [Atlan](https://developer.atlan.com/) | Active metadata platform with open API architecture and SDK support | 🟡 API Key | ✅ | ✅⭐ |
| [Informatica Catalog](https://developer.informatica.com/) | Enterprise metadata management with REST APIs for profiling and governance | 🟡 API Key | ✅ | ✅ |
| [Snowflake Horizon](https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference) | Native Snowflake cataloging and governance layer with REST API access | 🟡 API Key | ✅ | ✅ |
| [AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api.html) | Managed metadata repository for data lake analytics on AWS | 🟡 API Key | ✅ | ✅⭐ |
| [Amundsen](https://www.amundsen.io/amundsen/) | Open-source data discovery and metadata engine by LyftOSS | 🟡 API Key | ✅ | ✅ |
| [DataHub](https://datahubproject.io/docs/api/restli/restli-overview) | Open-source metadata platform (LinkedIn) with REST and GraphQL APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Secoda](https://docs.secoda.co/secoda-api) | AI-powered data catalog and documentation with REST API | 🟡 API Key | ✅ | ✅ |

---

## 🧹 Data Quality & Cleansing APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Great Expectations](https://docs.greatexpectations.io/docs/home/) | Open-source Python framework for data validation and quality testing | 🟢 No | ✅ | ✅⭐ |
| [Soda Core](https://docs.soda.io/) | Open-source data quality testing with CLI and Python API (SodaCL DSL) | 🟢 No | ✅ | ✅⭐ |
| [Melissa Global Address](https://docs.melissa.com/cloud-api/global-address-verification/global-address-verification-index.html) | Address verification, cleansing, and enrichment for 240+ countries | 🟡 API Key | ✅ | ✅⭐ |
| [Precisely](https://developer.precisely.com/) | Data integrity APIs for address verification, geocoding, and enrichment | 🟡 API Key | ✅ | ✅ |
| [Informatica Data Quality](https://docs.informatica.com/data-governance-and-quality-cloud/data-quality.html) | Cloud data quality with profiling, standardization, and matching APIs | 🟡 API Key | ✅ | ✅ |
| [Alteryx / Trifacta](https://api.trifacta.com/) | Data wrangling and quality platform with REST API for data prep pipelines | 🟡 API Key | ✅ | ✅ |
| [Talend Data Quality](https://help.talend.com/r/en-US/8.0/data-quality-user-guide) | Open-source and enterprise data quality with profiling and cleansing | 🟡 API Key | ✅ | ⚠️ |
| [Ataccama ONE](https://docs.ataccama.com/one/latest/) | AI-powered data quality, catalog, and governance unified platform | 🟡 API Key | ✅ | ✅ |
| [ZoomInfo](https://developer.zoominfo.com/) | B2B data intelligence with automated data cleansing and enrichment | 🟡 API Key | ✅ | ✅ |
| [Clearbit (HubSpot)](https://dashboard.clearbit.com/docs) | Real-time company and contact data enrichment and verification APIs | 🟡 API Key | ✅ | ✅⭐ |
| [OpenRefine](https://openrefine.org/docs) | Open-source tool for messy data cleansing and transformation | 🟢 No | ✅ | ⚠️ |
| [Deequ](https://github.com/awslabs/deequ) | Open-source data quality library for Spark by AWS Labs | 🟢 No | ✅ | ⚠️ |

---

## 🧩 Low-Code & No-Code APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Bubble](https://manual.bubble.io/core-resources/api) | Full-stack no-code platform with Data API and Workflow API | 🟡 API Key | ✅ | ✅⭐ |
| [Retool](https://docs.retool.com/api/) | Low-code platform for building internal tools with REST API management | 🟡 API Key | ✅ | ✅⭐ |
| [Zapier](https://zapier.com/developer-platform) | Automation platform connecting 8,000+ apps with developer platform APIs | 🟡 API Key | ✅ | ✅⭐ |
| [n8n](https://docs.n8n.io/api/) | Open-source workflow automation with public REST API and code nodes | 🟡 API Key | ✅ | ✅⭐ |
| [Appsmith](https://docs.appsmith.com/) | Open-source low-code framework for internal tools with REST/GraphQL support | 🟡 API Key | ✅ | ✅⭐ |
| [ToolJet](https://docs.tooljet.com/docs/tooljet-api/) | Open-source low-code platform with REST API for building business apps | 🟡 API Key | ✅ | ✅ |
| [Microsoft Power Automate](https://learn.microsoft.com/en-us/power-automate/web-api) | Enterprise workflow automation with connectors and REST APIs | 🔴 OAuth | ✅ | ✅ |
| [Mendix](https://docs.mendix.com/apidocs-mxsdk/apidocs/) | Enterprise low-code platform with comprehensive REST and OData APIs | 🟡 API Key | ✅ | ✅ |
| [Airtable](https://airtable.com/developers/web/api/introduction) | Spreadsheet-database hybrid with full REST API for CRUD operations | 🟡 API Key | ✅ | ✅⭐ |
| [Make (Integromat)](https://www.make.com/en/api-documentation) | Visual automation platform with API for building integration scenarios | 🟡 API Key | ✅ | ✅ |
| [Directus](https://docs.directus.io/reference/introduction.html) | Open-source headless CMS with auto-generated REST and GraphQL APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Superblocks](https://docs.superblocks.com/) | Developer platform for building internal apps with API-first workflows | 🟡 API Key | ✅ | ✅ |

---

## 🗣️ Text-to-Speech (TTS) APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [ElevenLabs](https://elevenlabs.io/docs/api-reference/text-to-speech/convert) | Ultra-realistic AI voices with voice cloning; 32 languages, ~75ms latency | 🟡 API Key | ✅ | ✅⭐ |
| [OpenAI TTS](https://platform.openai.com/docs/guides/text-to-speech) | GPT-4o mini TTS with 11+ built-in voices and real-time streaming | 🟡 API Key | ✅ | ✅⭐ |
| [Google Cloud TTS](https://cloud.google.com/text-to-speech) | 300+ voices in 50+ languages with WaveNet and Neural2 models | 🟡 API Key | ✅ | ✅⭐ |
| [Amazon Polly](https://docs.aws.amazon.com/polly/latest/dg/API_Reference.html) | AWS neural TTS with 60+ voices across 30+ languages and SSML support | 🟡 API Key | ✅ | ✅⭐ |
| [Microsoft Azure Speech](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/rest-text-to-speech) | 129 neural voices spanning 54 languages with on-premise container support | 🟡 API Key | ✅ | ✅⭐ |
| [Deepgram Aura](https://developers.deepgram.com/docs/text-to-speech) | Ultra-low latency TTS (~90ms) designed for real-time voice AI agents | 🟡 API Key | ✅ | ✅⭐ |
| [Murf AI](https://murf.ai/api/docs) | 150+ AI voices across 35+ languages with speech customization controls | 🟡 API Key | ✅ | ✅ |
| [Play.ht](https://docs.play.ht/reference/api-getting-started) | AI voice generation with voice cloning and streaming via REST and SDK | 🟡 API Key | ✅ | ✅ |
| [Resemble AI](https://docs.app.resemble.ai/) | Voice cloning and speech synthesis with real-time streaming API | 🟡 API Key | ✅ | ✅ |
| [IBM Watson TTS](https://cloud.ibm.com/apidocs/text-to-speech) | Enterprise TTS with expressive neural voices and customization | 🟡 API Key | ✅ | ✅ |
| [Speechify API](https://docs.sws.speechify.com/) | TTS API with lifelike AI voices for content reading and accessibility | 🟡 API Key | ✅ | ✅ |
| [Cartesia](https://docs.cartesia.ai/) | Sonic model TTS with sub-100ms latency and multi-language streaming | 🟡 API Key | ✅ | ✅ |

---

## 📱 App Store & Mobile Analytics APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Apple App Store Connect](https://developer.apple.com/documentation/appstoreconnectapi/analytics) | Official Apple API with 50+ analytics reports for App Store performance | 🟡 API Key | ✅ | ✅⭐ |
| [Google Play Developer](https://developers.google.com/android-publisher) | Official Google API for Play Store stats, reviews, and financial reports | 🔴 OAuth | ✅ | ✅⭐ |
| [Appfigures](https://docs.appfigures.com/) | App store analytics API for sales, ranks, reviews, and competitor data | 🟡 API Key | ✅ | ✅⭐ |
| [Sensor Tower](https://sensortower.com/product/connect) | Mobile intelligence API for download/revenue estimates and market trends | 🟡 API Key | ✅ | ✅ |
| [data.ai (App Annie)](https://helpcenter.data.ai/community/s/article/API-Introduction) | App market intelligence with usage, download, and revenue estimates | 🟡 API Key | ✅ | ✅ |
| [AppFollow](https://appfollow.io/appfollow-api) | Review management, keyword tracking, and ranking analysis API | 🟡 API Key | ✅ | ✅ |
| [Mixpanel](https://developer.mixpanel.com/reference/overview) | Product analytics with event tracking, funnels, and retention analysis | 🟡 API Key | ✅ | ✅⭐ |
| [AppsFlyer](https://dev.appsflyer.com/hc/docs/api) | Mobile attribution and marketing analytics with server-to-server APIs | 🟡 API Key | ✅ | ✅ |
| [Adjust](https://dev.adjust.com/en/api/) | Mobile measurement and fraud prevention with reporting and campaign APIs | 🟡 API Key | ✅ | ✅ |
| [Firebase Analytics](https://firebase.google.com/docs/analytics) | Free app analytics with automatic event tracking and BigQuery export | 🟡 API Key | ✅ | ✅⭐ |
| [UXCam](https://developer.uxcam.com/) | Mobile app analytics with session replay, heatmaps, and user data APIs | 🟡 API Key | ✅ | ✅ |
| [Amplitude](https://www.docs.developers.amplitude.com/analytics/) | Product analytics platform with event tracking and experiment APIs | 🟡 API Key | ✅ | ✅⭐ |

---

## 🏢 Coworking & Office Space APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Nexudus](https://developers.nexudus.com/reference/getting-started-with-your-api-1) | Coworking management REST API with 60+ integrations and SDK support | 🟡 API Key | ✅ | ✅⭐ |
| [OfficeRnD](https://www.officernd.com/developers/) | Flex space management platform with developer hub and REST APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Cobot](https://dev.cobot.me/api-docs) | Coworking management API for bookings, members, invoices, and access control | 🔴 OAuth | ✅ | ✅⭐ |
| [LiquidSpace](https://developer.liquidspace.com/) | Workspace search and reservation booking API for flexible offices | 🟡 API Key | ✅ | ✅ |
| [Spacebring](https://developer.spacebring.com/) | Coworking software REST API with webhooks for event-driven automation | 🟡 API Key | ✅ | ✅ |
| [Robin](https://docs.robinpowered.com/docs/getting-started) | Workplace platform API for desk booking, room scheduling, and presence | 🟡 API Key | ✅ | ✅⭐ |
| [Deskbird](https://developer.deskbird.com/welcome-to-the-deskbird-public-api-857686m0) | Desk and room booking API with scheduling, check-in, and analytics | 🟡 API Key | ✅ | ✅ |
| [Skedda](https://www.skedda.com/booking-system-api) | Space scheduling and booking system with REST API and webhook support | 🟡 API Key | ✅ | ✅ |
| [Envoy](https://developers.envoy.com/) | Workplace platform API for visitor management and room booking | 🔴 OAuth | ✅ | ✅ |
| [Archie](https://archieapp.co/integrations) | Workspace management with open API for coworking and hybrid spaces | 🟡 API Key | ✅ | ⚠️ |
| [Optix](https://www.optixapp.com/) | Coworking management software with integration APIs and Zapier support | 🟡 API Key | ✅ | ⚠️ |
| [OfficeSpace Software](https://support.officespacesoftware.com/s/article/Using-the-OfficeSpace-API-HC) | Office space management API for floor plans, moves, and desk booking | 🟡 API Key | ✅ | ✅ |

---

## 🧪 A/B Testing & Experimentation APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Optimizely](https://docs.developers.optimizely.com/web-experimentation/docs/rest-api-introduction) | Enterprise experimentation with REST API, OpenAPI spec, and Postman collection | 🔴 OAuth | ✅ | ✅⭐ |
| [LaunchDarkly](https://apidocs.launchdarkly.com/) | Feature flags and controlled rollouts with comprehensive REST API | 🟡 API Key | ✅ | ✅⭐ |
| [Statsig](https://docs.statsig.com/http-api/) | High-scale experimentation platform (1T+ events/day) with HTTP and Console APIs | 🟡 API Key | ✅ | ✅⭐ |
| [GrowthBook](https://docs.growthbook.io/api/) | Open-source feature flagging and A/B testing with full REST API | 🟡 API Key | ✅ | ✅⭐ |
| [PostHog](https://posthog.com/docs/api/experiments) | Open-source product analytics with experimentation and feature flags APIs | 🟡 API Key | ✅ | ✅⭐ |
| [VWO FullStack](https://developers.vwo.com/reference/introduction-1) | Server-side testing and feature management with REST API and SDKs | 🟡 API Key | ✅ | ✅ |
| [Split.io](https://docs.split.io/reference/introduction) | Feature delivery platform with experimentation REST API and event streaming | 🟡 API Key | ✅ | ✅ |
| [Amplitude Experiment](https://www.docs.developers.amplitude.com/experiment/) | Experimentation with statistical engine tied to Amplitude analytics | 🟡 API Key | ✅ | ✅ |
| [Flagsmith](https://docs.flagsmith.com/clients/rest/) | Open-source feature flag and remote config service with REST API | 🟡 API Key | ✅ | ✅ |
| [Convert Experiences](https://www.convert.com/features/ab-testing/api/) | Privacy-first enterprise A/B testing with secure HMAC-authenticated API | 🟡 API Key | ✅ | ✅ |
| [Unleash](https://docs.getunleash.io/reference/api/legacy/unleash) | Open-source feature flag management with client and admin APIs | 🟡 API Key | ✅ | ✅ |
| [Eppo](https://docs.geteppo.com/api) | Warehouse-native experimentation platform with REST API and SDKs | 🟡 API Key | ✅ | ✅ |

---

## 🔗 URL & Link Management APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Bitly](https://dev.bitly.com/api-reference) | Industry-leading URL shortener with analytics, QR codes, and 99.9% uptime | 🟡 API Key | ✅ | ✅⭐ |
| [Rebrandly](https://developers.rebrandly.com/docs/api-custom-url-shortener) | Custom branded short links with link editing, expiration, and retargeting | 🟡 API Key | ✅ | ✅⭐ |
| [Short.io](https://developers.short.io/docs/cre) | Link shortener with bulk API (1000 links/call), analytics, and webhooks | 🟡 API Key | ✅ | ✅⭐ |
| [Dub.co](https://dub.co/docs/api-reference/introduction) | Modern open-source link management with analytics, conversions, and SDKs | 🟡 API Key | ✅ | ✅⭐ |
| [Cuttly](https://cutt.ly/api-documentation/cuttly-links-api) | URL shortener with QR codes, branded domains, and link analytics API | 🟡 API Key | ✅ | ✅ |
| [TinyURL](https://tinyurl.com/app/dev) | Classic URL shortener with developer API for link creation and management | 🟡 API Key | ✅ | ✅ |
| [BL.INK](https://app.bl.ink/developer) | Enterprise branded link management with analytics and team APIs | 🟡 API Key | ✅ | ✅ |
| [Kutt.it](https://github.com/thedevs-network/kutt) | Open-source modern URL shortener with API and custom domain support | 🟡 API Key | ✅ | ✅ |
| [T.LY](https://t.ly/docs/api) | URL shortener API with link tracking, bulk creation, and smart links | 🟡 API Key | ✅ | ✅ |
| [Shrtco.de](https://shrtco.de/docs) | Free URL shortening API with no authentication required | 🟢 No | ✅ | ✅⭐ |
| [Firebase Dynamic Links](https://firebase.google.com/docs/dynamic-links) | Deep links that work across platforms (iOS, Android, web) with analytics | 🟡 API Key | ✅ | ✅ |
| [Branch.io](https://help.branch.io/developers-hub/docs/deep-linking-api) | Deep linking and attribution platform with link creation and analytics API | 🟡 API Key | ✅ | ✅ |

---

## 🐳 Container & Kubernetes APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Kubernetes API](https://kubernetes.io/docs/reference/kubernetes-api/) | Official Kubernetes REST API for managing all cluster resources and objects | 🟡 API Key | ✅ | ✅⭐ |
| [Docker Engine API](https://docs.docker.com/reference/api/engine/) | RESTful API for managing containers, images, volumes, and networks | 🟡 API Key | ✅ | ✅⭐ |
| [Amazon EKS](https://docs.aws.amazon.com/eks/latest/APIReference/Welcome.html) | AWS managed Kubernetes service API for cluster lifecycle management | 🟡 API Key | ✅ | ✅⭐ |
| [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/docs/reference/rest) | GKE REST API for managing GCP Kubernetes clusters and workloads | 🔴 OAuth | ✅ | ✅⭐ |
| [Azure AKS](https://learn.microsoft.com/en-us/rest/api/aks/) | Azure Kubernetes Service REST API for cluster management | 🔴 OAuth | ✅ | ✅⭐ |
| [Portainer](https://docs.portainer.io/api/docs) | Container management REST API (Docker, K8s, Podman) with reverse-proxy | 🟡 API Key | ✅ | ✅⭐ |
| [Rancher](https://ranchermanager.docs.rancher.com/api/api-reference) | Multi-cluster Kubernetes management API using native K8s CRDs | 🟡 API Key | ✅ | ✅ |
| [Helm](https://helm.sh/docs/) | Kubernetes package manager for defining, installing, and upgrading apps | 🟢 No | ✅ | ✅⭐ |
| [Red Hat OpenShift](https://docs.openshift.com/container-platform/latest/rest_api/index.html) | Enterprise Kubernetes platform with extended REST API endpoints | 🔴 OAuth | ✅ | ✅ |
| [Northflank](https://northflank.com/docs/v1/api) | Developer platform API for deploying containers with built-in CI/CD | 🟡 API Key | ✅ | ✅ |
| [DigitalOcean Kubernetes](https://docs.digitalocean.com/reference/api/api-reference/#tag/Kubernetes) | Managed Kubernetes API for cluster provisioning and node pool management | 🟡 API Key | ✅ | ✅⭐ |
| [Spacelift](https://docs.spacelift.io/vendors/kubernetes) | Infrastructure orchestration for Terraform and Kubernetes with GraphQL API | 🟡 API Key | ✅ | ✅ |

---

## 📈 Stock Market & Trading APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Alpaca](https://docs.alpaca.markets/docs/trading-api) | Commission-free stock and crypto trading API with paper trading sandbox | 🟡 API Key | ✅ | ✅⭐ |
| [Polygon.io](https://polygon.io/docs/stocks) | Real-time and historical market data for stocks, options, forex, and crypto | 🟡 API Key | ✅ | ✅⭐ |
| [Alpha Vantage](https://www.alphavantage.co/) | Free stock APIs with 50+ technical indicators in JSON and CSV formats | 🟡 API Key | ✅ | ✅⭐ |
| [Finnhub](https://finnhub.io/) | Free real-time stock, forex, and crypto data with company fundamentals | 🟡 API Key | ✅ | ✅⭐ |
| [Twelve Data](https://twelvedata.com/) | Stock, forex, and crypto data from 50+ exchanges with 100+ indicators | 🟡 API Key | ✅ | ✅⭐ |
| [Interactive Brokers](https://www.interactivebrokers.com/campus/ibkr-api-page/ibkr-api-home/) | Full brokerage API (Web, TWS, FIX) for stocks, options, futures, and forex | 🟡 API Key | ✅ | ✅ |
| [Tradier](https://docs.tradier.com/) | Brokerage API for equities and options with real-time data and paper trading | 🟡 API Key | ✅ | ✅⭐ |
| [Financial Modeling Prep](https://site.financialmodelingprep.com/developer/docs) | Stock screener, financial statements, and real-time data with 99.9% uptime | 🟡 API Key | ✅ | ✅⭐ |
| [EODHD](https://eodhd.com/financial-apis/) | End-of-day, intraday, and fundamental data for global exchanges | 🟡 API Key | ✅ | ✅ |
| [Finage](https://finage.co.uk/) | Ultra-low latency market data processing 600M+ API calls daily | 🟡 API Key | ✅ | ✅ |
| [Yahoo Finance (via RapidAPI)](https://rapidapi.com/sparior/api/yahoo-finance15) | Stock quotes, historical data, and financial news via unofficial API | 🟡 API Key | ✅ | ✅ |
| [Marketstack](https://marketstack.com/documentation) | Free REST API for real-time and historical stock market data worldwide | 🟡 API Key | ✅ | ✅⭐ |
| [IEX Cloud](https://iexcloud.io/docs/) | Financial data platform with stock data, news, and analytics APIs | 🟡 API Key | ✅ | ✅ |

---

## 🎵 Music Streaming & Licensing APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Spotify Web API](https://developer.spotify.com/documentation/web-api) | Access Spotify catalog data, manage playlists, control playback | 🔴 OAuth | ✅ | ✅⭐ |
| [Apple Music API](https://developer.apple.com/documentation/applemusicapi/) | Stream Apple Music catalog, manage libraries, get recommendations | 🟡 API Key | ✅ | ✅⭐ |
| [Deezer API](https://developers.deezer.com/) | Search tracks, artists, albums; access playlists and user data | 🔴 OAuth | ✅ | ✅⭐ |
| [Last.fm API](https://www.last.fm/api) | Scrobbling, music recommendations, artist/track metadata | 🟡 API Key | ✅ | ✅⭐ |
| [SoundCloud API](https://developers.soundcloud.com/docs) | Access tracks, playlists, user profiles on the SoundCloud platform | 🔴 OAuth | ✅ | ✅ |
| [Musixmatch API](https://developer.musixmatch.com/) | World's largest lyrics catalog; search songs, retrieve lyrics | 🟡 API Key | ✅ | ✅⭐ |
| [Genius API](https://docs.genius.com/) | Song lyrics, annotations, and artist metadata | 🔴 OAuth | ✅ | ✅ |
| [Jamendo API](https://developer.jamendo.com/v3.0) | Half-million royalty-free tracks; music discovery and radios | 🔴 OAuth | ✅ | ✅⭐ |
| [Freesound API](https://freesound.org/docs/api/) | Browse, search, and download Creative Commons licensed sounds | 🔴 OAuth | ✅ | ✅⭐ |
| [MusicAPI](https://musicapi.com/) | Unified API integrating 10+ streaming services (Spotify, Apple Music, Tidal, etc.) | 🟡 API Key | ✅ | ✅⭐ |
| [Songlink/Odesli API](https://odesli.co/) | Generate universal smart links across all major streaming platforms | 🟢 No | ✅ | ✅⭐ |
| [Feed.fm Music API](https://www.feed.fm/music-streaming-api) | Licensed commercial music streaming for apps with automated compliance | 🟡 API Key | ✅ | ✅ |
| [Mubert API](https://mubert.com/use-cases/developers) | AI-generated royalty-free music for apps, games, and livestreams | 🟡 API Key | ✅ | ✅ |
| [Soundcharts API](https://soundcharts.com/en/blog/music-data-api) | Music industry analytics, chart tracking, and social data | 🟡 API Key | ✅ | ✅ |

---

## 📊 Barcode & Product Lookup APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Barcode Lookup API](https://www.barcodelookup.com/api) | Product data lookup by UPC, EAN, or ISBN barcode numbers | 🟡 API Key | ✅ | ✅⭐ |
| [Go-UPC Product API](https://go-upc.com/) | Access to over 1 billion products across six continents by barcode | 🟡 API Key | ✅ | ✅⭐ |
| [UPCitemdb API](https://devs.upcitemdb.com/) | RESTful lookup and search across 495M+ products by UPC/EAN | 🟡 API Key | ✅ | ✅⭐ |
| [Open Food Facts API](https://openfoodfacts.github.io/openfoodfacts-server/api/) | Open-source collaborative food database with barcode lookup (2.8M+ products) | 🟢 No | ✅ | ✅⭐ |
| [Barcode Spider API](https://www.barcodespider.com/) | Fast barcode database access via UPC, EAN, ISBN, or ASIN in JSON/CSV | 🟡 API Key | ✅ | ✅⭐ |
| [GS1 US APIs](https://www.gs1us.org/tools/gs1-us-data-hub/gs1-us-apis) | Official GTIN/GLN data lookup for supply chain and inventory management | 🟡 API Key | ✅ | ✅ |
| [Nutritionix API](https://developer.nutritionix.com/) | Nutrition data for 800K+ packaged products and restaurant menu items | 🟡 API Key | ✅ | ✅⭐ |
| [Edamam Food Database API](https://developer.edamam.com/food-database-api) | 900K+ foods with nutrition labeling, diet, and allergy data | 🟡 API Key | ✅ | ✅⭐ |
| [Zyla EAN Lookup API](https://zylalabs.com/api-marketplace/data/ean+lookup+api/1411) | Search products by EAN barcode or name; retrieve pricing and descriptions | 🟡 API Key | ✅ | ✅ |
| [Cloudmersive Barcode API](https://cloudmersive.com/barcode-api) | Generate and read 1D/2D barcodes (QR, UPC-A, EAN-13, etc.) | 🟡 API Key | ✅ | ✅⭐ |
| [Scandit Barcode SDK](https://www.scandit.com/developers/) | High-performance barcode scanning SDK for mobile and web apps | 🟡 API Key | ✅ | ✅ |
| [Brocade.io](https://github.com/EventideSystems/brocade.io) | Free and open GTIN/barcode and product database | 🟢 No | ✅ | ✅ |

---

## 🔄 Data Sync & Replication APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Airbyte API](https://docs.airbyte.com/api-documentation/) | Open-source data integration platform with 600+ connectors; programmatic pipeline management | 🟡 API Key | ✅ | ✅⭐ |
| [Fivetran REST API](https://fivetran.com/docs/rest-api) | Automated data replication; manage connectors, sync jobs, and pipelines | 🟡 API Key | ✅ | ✅⭐ |
| [CData Sync API](https://www.cdata.com/sync/docs/) | OData 4.0 compliant REST API for data replication across 100s of sources | 🟡 API Key | ✅ | ✅ |
| [Firebase Realtime Database REST API](https://firebase.google.com/docs/database/rest/start) | Cloud-hosted JSON database with real-time sync to all connected clients | 🔴 OAuth | ✅ | ✅⭐ |
| [Supabase Realtime API](https://supabase.com/docs/guides/api) | Listen to PostgreSQL inserts, updates, deletes via websockets in real-time | 🟡 API Key | ✅ | ✅⭐ |
| [Ably Realtime API](https://ably.com/docs/api) | Pub/sub messaging platform for real-time data synchronization at scale | 🟡 API Key | ✅ | ✅⭐ |
| [Liveblocks API](https://liveblocks.io/docs/products/realtime-apis) | Real-time collaboration engine with Yjs support for sync and conflict resolution | 🟡 API Key | ✅ | ✅⭐ |
| [Debezium](https://debezium.io/documentation/reference/stable/features.html) | Open-source CDC platform streaming database changes to Apache Kafka | 🟢 No | ✅ | ⚠️ |
| [Hevo Data API](https://api-docs.hevodata.com/reference/introduction) | No-code data pipeline platform; REST API for managing pipelines and ingestion | 🟡 API Key | ✅ | ✅ |
| [PlanetScale API](https://planetscale.com/docs) | Serverless MySQL platform with branching, deploy requests, and schema management | 🟡 API Key | ✅ | ✅⭐ |
| [Yjs](https://github.com/yjs/yjs) | Open-source CRDT framework for building collaborative real-time apps | 🟢 No | ✅ | ⚠️ |
| [Stacksync](https://www.stacksync.com/blog/9-data-replication-tools-you-need-2025) | Real-time bi-directional sync with sub-second latency and conflict resolution | 🟡 API Key | ✅ | ✅ |

---

## 🌍 Environmental Monitoring APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [AQICN API](https://aqicn.org/api/) | Real-time air quality index data from global monitoring stations | 🟡 API Key | ✅ | ✅⭐ |
| [Google Air Quality API](https://developers.google.com/maps/documentation/air-quality/overview) | Real-time, historical, and forecast AQ data at 500m resolution for 100+ countries | 🟡 API Key | ✅ | ✅⭐ |
| [Open-Meteo Air Quality API](https://open-meteo.com/en/docs/air-quality-api) | Free air quality forecasts for PM, gases, and pollen worldwide | 🟢 No | ✅ | ✅⭐ |
| [IQAir AirVisual API](https://www.iqair.com/commercial-air-quality-monitors/api) | Air quality data from 80+ countries; current conditions and forecasts | 🟡 API Key | ✅ | ✅⭐ |
| [Ambee Air Quality API](https://www.getambee.com/api/air-quality) | Hyperlocal air quality data with pollen, fire, and soil monitoring | 🟡 API Key | ✅ | ✅⭐ |
| [PurpleAir API](https://community.purpleair.com/c/data/api/18) | Real-time data from a global network of low-cost air quality sensors | 🟡 API Key | ✅ | ✅ |
| [OpenWeatherMap Air Pollution API](https://openweathermap.org/api/air-pollution) | Current, forecast, and historical air pollution data (CO, NO2, O3, PM) | 🟡 API Key | ✅ | ✅⭐ |
| [Plume Labs API](https://plumelabs.com/en/forecast-api/) | Accurate live and forecast air quality data with street-level resolution | 🟡 API Key | ✅ | ✅ |
| [EPA AirNow API](https://docs.airnowapi.org/) | US EPA official air quality observations and forecasts for the United States | 🟡 API Key | ✅ | ✅⭐ |
| [Visual Crossing Weather API](https://www.visualcrossing.com/resources/blog/air-quality-data-iot-integration-for-smarter-environmental-monitoring-systems/) | Weather and environmental data including IoT sensor integration | 🟡 API Key | ✅ | ✅⭐ |
| [Weatherbit Air Quality API](https://www.weatherbit.io/api/airquality-current) | Detailed air pollution data integrated with weather information | 🟡 API Key | ✅ | ✅⭐ |
| [Copernicus Atmosphere Monitoring Service](https://atmosphere.copernicus.eu/) | European-scale air quality forecasts and reanalysis data | 🟢 No | ✅ | ⚠️ |

---

## 📢 Advertising & Ad Tech APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Google Ads API](https://developers.google.com/google-ads/api) | Programmatic management of Google Ads campaigns, bidding, and reporting | 🔴 OAuth | ✅ | ✅⭐ |
| [Google Ad Manager API](https://developers.google.com/ad-manager) | Manage ad inventory, create orders, pull reports for publishers | 🔴 OAuth | ✅ | ✅⭐ |
| [Google AdMob API](https://developers.google.com/admob/api/reference/rest) | Mobile app monetization; manage ad units, mediation groups, and reports | 🔴 OAuth | ✅ | ✅⭐ |
| [Meta Marketing API](https://developers.facebook.com/docs/marketing-apis) | Create/manage Facebook and Instagram ad campaigns programmatically | 🔴 OAuth | ✅ | ✅⭐ |
| [X (Twitter) Ads API](https://developer.x.com/en/docs/x-ads-api) | Programmatically create, schedule, and manage ad campaigns on X | 🔴 OAuth | ✅ | ✅ |
| [Snapchat Ads API](https://developers.snap.com/api/marketing-api/Ads-API/introduction) | Full advertising lifecycle management on Snapchat | 🔴 OAuth | ✅ | ✅ |
| [Amazon Advertising API](https://advertising.amazon.com/API/docs/en-us/reference/api-overview) | Plan, activate, and measure programmatic ad strategies on Amazon | 🔴 OAuth | ✅ | ✅⭐ |
| [The Trade Desk API](https://partner.thetradedesk.com/v3/portal/api/doc/ApiPlatformGetStarted) | Enterprise DSP API for programmatic media buying on the open internet | 🟡 API Key | ✅ | ✅ |
| [Criteo API](https://developers.criteo.com/marketing-solutions/docs/developer-support) | Retargeting and commerce media; reporting and audience management | 🔴 OAuth | ✅ | ✅ |
| [AdRoll API](https://developers.adroll.com/) | Manage retargeting campaigns, bulk import creatives, and generate reports | 🟡 API Key | ✅ | ✅ |
| [StackAdapt](https://www.stackadapt.com/) | AI-powered programmatic advertising platform for multi-channel campaigns | 🟡 API Key | ✅ | ⚠️ |
| [ironSource/Unity LevelPlay](https://developers.is.com/ironsource-mobile/unity/unity-plugin/) | Mobile ad mediation SDK supporting 20+ ad networks for monetization | 🟡 API Key | ✅ | ⚠️ |

---

## 🩻 Medical Imaging APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Google Cloud Healthcare API (DICOM)](https://cloud.google.com/healthcare-api/docs/concepts/dicom) | Store, retrieve, and search DICOM instances via DICOMweb standard on GCP | 🔴 OAuth | ✅ | ✅⭐ |
| [Orthanc REST API](https://www.orthanc-server.com/) | Open-source lightweight DICOM server with RESTful API (JSON/PNG output) | 🟢 No | ✅ | ✅⭐ |
| [OHIF Viewer](https://docs.ohif.org/) | Open-source web-based medical imaging viewer with extension API system | 🟢 No | ✅ | ✅⭐ |
| [Cornerstone.js](https://www.cornerstonejs.org/) | JavaScript library for rendering DICOM images in browsers with GPU acceleration | 🟢 No | ✅ | ✅⭐ |
| [3D Slicer API](https://slicer.readthedocs.io/en/latest/developer_guide/api.html) | Open-source platform for medical image analysis with Python/C++ API | 🟢 No | ✅ | ✅ |
| [DICOMweb Standard](https://www.dicomstandard.org/using/dicomweb) | RESTful services for web-based medical imaging (WADO-RS, STOW-RS, QIDO-RS) | 🟡 API Key | ✅ | ✅⭐ |
| [Medicai API](https://www.medicai.io/products/medicai-api) | Cloud PACS with REST API; HL7/FHIR compliant medical imaging integration | 🟡 API Key | ✅ | ✅ |
| [Merge DICOM Toolkit](https://www.merative.com/merge-imaging/dicom-toolkit) | Comprehensive API conforming to latest DICOM standards for any modality | 🟡 API Key | ✅ | ⚠️ |
| [Pydicom](https://pydicom.github.io/) | Pure Python library for reading, modifying, and writing DICOM files | 🟢 No | ✅ | ✅⭐ |
| [PDBe API (Structural)](https://www.ebi.ac.uk/pdbe/pdbe-rest-api) | Protein Data Bank in Europe REST API for macromolecular structure data | 🟢 No | ✅ | ✅⭐ |
| [MONAI Label](https://github.com/Project-MONAI/MONAILabel) | AI-assisted annotation platform for medical image labeling with API | 🟢 No | ✅ | ✅ |
| [Autodesk Platform Services (Medical)](https://aps.autodesk.com/developer/overview/autocad) | Cloud-based 3D visualization including medical model rendering | 🔴 OAuth | ✅ | ✅ |

---

## 🧬 Bioinformatics & Protein APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [UniProt REST API](https://www.uniprot.org/help/api) | Access 250M+ protein sequences, functional annotations, and cross-references | 🟢 No | ✅ | ✅⭐ |
| [RCSB PDB Data API](https://data.rcsb.org/) | Retrieve 3D macromolecular structure data from the Protein Data Bank in JSON | 🟢 No | ✅ | ✅⭐ |
| [AlphaFold API](https://www.alphafold.ebi.ac.uk/api-docs) | Access 200M+ AI-predicted protein structures from DeepMind | 🟢 No | ✅ | ✅⭐ |
| [NCBI E-utilities API](https://www.ncbi.nlm.nih.gov/home/develop/api/) | Programmatic access to PubMed, Gene, Protein, and all Entrez databases | 🟡 API Key | ✅ | ✅⭐ |
| [EMBL-EBI Proteins API](https://www.ebi.ac.uk/proteins/api/doc/) | Integrated protein data from UniProt and Large Scale Studies | 🟢 No | ✅ | ✅⭐ |
| [Ensembl REST API](https://rest.ensembl.org/) | Access genes, variants, orthologs, genomic alignments across species | 🟢 No | ✅ | ✅⭐ |
| [InterPro API](https://www.ebi.ac.uk/interpro/api/) | Protein families, domains, and functional sites classification data | 🟢 No | ✅ | ✅⭐ |
| [STRING API](https://string-db.org/help/api/) | Protein-protein interaction networks and functional enrichment analysis | 🟢 No | ✅ | ✅⭐ |
| [Reactome Content Service](https://reactome.org/ContentService/) | Biological pathway knowledge base with REST API (Open API/Swagger) | 🟢 No | ✅ | ✅⭐ |
| [KEGG REST API](https://www.kegg.jp/kegg/rest/keggapi.html) | Kyoto Encyclopedia of Genes and Genomes pathway and molecular data | 🟢 No | ✅ | ✅⭐ |
| [PubChem PUG REST](https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest) | Chemical compound information, bioactivity, and substance data | 🟢 No | ✅ | ✅⭐ |
| [RCSB PDB Search API](https://search.rcsb.org/) | Advanced search across PDB structures with attribute and sequence queries | 🟢 No | ✅ | ✅⭐ |
| [PDBe REST API](https://www.ebi.ac.uk/pdbe/pdbe-rest-api) | Protein Data Bank in Europe; structural data and validation reports | 🟢 No | ✅ | ✅⭐ |

---

## 🎲 Random Data & Generator APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Random.org API](https://api.random.org/json-rpc/4/basic) | True random numbers generated from atmospheric noise via JSON-RPC | 🟡 API Key | ✅ | ✅⭐ |
| [Random User Generator](https://randomuser.me/) | Generate random realistic user profiles (names, photos, addresses) | 🟢 No | ✅ | ✅⭐ |
| [Faker.js](https://fakerjs.dev/api/) | Generate massive amounts of realistic fake data (names, addresses, finance) | 🟢 No | ✅ | ✅⭐ |
| [Mockaroo](https://www.mockaroo.com/) | Custom datasets in JSON/CSV/SQL/Excel with 200+ data types and formulas | 🟡 API Key | ✅ | ✅⭐ |
| [JSONPlaceholder](https://jsonplaceholder.typicode.com/) | Free fake REST API with posts, comments, users, and photos for testing | 🟢 No | ✅ | ✅⭐ |
| [Randommer](https://randommer.io/) | Generate random names, addresses, phones, text, and social numbers via REST | 🟡 API Key | ✅ | ✅⭐ |
| [Chance.js](https://chancejs.com/) | JavaScript random data generator for strings, names, addresses, dice, etc. | 🟢 No | ✅ | ✅⭐ |
| [Random Data API](https://random-data-api.com/documentation) | Generate random users, addresses, beers, banks, and more via REST | 🟢 No | ✅ | ✅⭐ |
| [RandomAPI](https://randomapi.com/) | Create custom APIs that return random data using user-defined snippets | 🟡 API Key | ✅ | ✅ |
| [UUID Generator API](https://www.uuidtools.com/docs) | Generate UUIDs v1-v5 programmatically via simple REST endpoints | 🟢 No | ✅ | ✅⭐ |
| [Generate-Random.org API](https://generate-random.org/) | 50+ generators (passwords, numbers, strings, coordinates) with JSON responses | 🟢 No | ✅ | ✅⭐ |
| [Fun Generators UUID API](https://fungenerators.com/api/uuid/) | RFC 4122 UUID generation including non-standard v6 UUIDs via REST | 🟡 API Key | ✅ | ✅ |

---

## ⚡ Serverless & FaaS APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [AWS Lambda](https://docs.aws.amazon.com/lambda/) | Pioneer FaaS platform; event-driven compute with 15-minute max execution | 🟡 API Key | ✅ | ✅⭐ |
| [Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/) | Microsoft serverless compute with Durable Functions for stateful workflows | 🟡 API Key | ✅ | ✅⭐ |
| [Google Cloud Functions](https://cloud.google.com/functions/docs) | Lightweight FaaS with HTTP endpoints by default; ideal for event-driven backends | 🟡 API Key | ✅ | ✅⭐ |
| [Cloudflare Workers](https://developers.cloudflare.com/workers/) | Edge serverless on 300+ data centers with V8 isolates and sub-5ms cold starts | 🟡 API Key | ✅ | ✅⭐ |
| [Vercel Functions](https://vercel.com/docs/functions) | Serverless and edge functions tightly integrated with Next.js framework | 🟡 API Key | ✅ | ✅⭐ |
| [Netlify Functions](https://docs.netlify.com/functions/overview/) | Serverless functions built on AWS Lambda for JAMstack applications | 🟡 API Key | ✅ | ✅⭐ |
| [OpenFaaS](https://docs.openfaas.com/) | Open-source serverless framework for Kubernetes; any language, any binary | 🟢 No | ✅ | ✅⭐ |
| [Knative](https://knative.dev/docs/) | Kubernetes-native serverless platform with scale-to-zero and eventing | 🟢 No | ✅ | ✅ |
| [Nuclio](https://docs.nuclio.io/) | High-performance serverless for data-intensive and real-time AI workloads | 🟢 No | ✅ | ✅ |
| [Deno Deploy](https://deno.com/deploy) | Global edge serverless for TypeScript/JavaScript with zero config | 🟡 API Key | ✅ | ✅⭐ |
| [Supabase Edge Functions](https://supabase.com/docs/guides/functions) | Deno-based serverless functions integrated with Supabase Postgres backend | 🟡 API Key | ✅ | ✅⭐ |
| [IBM Cloud Functions](https://cloud.ibm.com/functions/) | Apache OpenWhisk-based serverless platform on IBM Cloud | 🟡 API Key | ✅ | ✅ |
| [Fastly Compute](https://developer.fastly.com/learning/compute/) | Edge compute platform running WebAssembly with sub-millisecond startup | 🟡 API Key | ✅ | ✅ |

---

## 🏗️ CAD & 3D Modeling APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Onshape API](https://onshape-public.github.io/) | Full-featured cloud CAD REST API with OAuth2; models, assemblies, drawings | 🔴 OAuth | ✅ | ✅⭐ |
| [Autodesk Platform Services (Fusion)](https://aps.autodesk.com/developer/overview/autodesk-fusion-api) | Cloud API for Fusion 360 CAD models, viewing, translation, and data management | 🔴 OAuth | ✅ | ✅⭐ |
| [Trimble Connect API](https://developer.trimble.com/docs/connect/) | RESTful API for managing 3D BIM projects, files, views, and collaboration | 🔴 OAuth | ✅ | ✅ |
| [ShapeDiver API](https://help.shapediver.com/doc/apis-and-sdks) | Parametric 3D model computation and visualization via Grasshopper backend | 🟡 API Key | ✅ | ✅⭐ |
| [Speckle API](https://docs.speckle.systems/) | Open-source 3D data platform for AEC with GraphQL API and webhooks | 🟡 API Key | ✅ | ✅⭐ |
| [Three.js](https://threejs.org/docs/) | Widely-used JavaScript 3D library for WebGL rendering in browsers | 🟢 No | ✅ | ✅⭐ |
| [rhino3dm.js](https://mcneel.github.io/rhino3dm/javascript/api/) | McNeel OpenNURBS geometry library compiled to WebAssembly for browser use | 🟢 No | ✅ | ✅ |
| [That Open Engine (IFC.js)](https://docs.thatopen.com/Tutorials/Components/Core/IfcLoader) | Open-source BIM/IFC loader and viewer built on Three.js for web apps | 🟢 No | ✅ | ✅⭐ |
| [xeokit SDK](https://xeokit.io/) | Open-source SDK for high-performance 3D BIM visualization in the browser | 🟢 No | ✅ | ✅ |
| [IfcOpenShell](https://ifcopenshell.org/) | Open-source toolkit for working with IFC building data (Python/C++) | 🟢 No | ✅ | ✅ |
| [Tech Soft 3D (HOOPS)](https://www.techsoft3d.com/solutions/) | Commercial SDKs for 3D visualization, file conversion, and publishing | 🟡 API Key | ✅ | ⚠️ |
| [Tripo AI Text-to-CAD API](https://3dprintingindustry.com/news/tripo-ai-launches-new-text-to-cad-api-for-3d-model-generation-237984/) | AI-powered 3D model generation from text prompts via REST API | 🟡 API Key | ✅ | ✅ |

---

## 🌊 Ocean & Marine Data APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [NOAA CO-OPS Tides & Currents API](https://api.tidesandcurrents.noaa.gov/api/prod/) | Official US tidal predictions, water levels, currents, and meteorological data | 🟢 No | ✅ | ✅⭐ |
| [NOAA ERDDAP](https://www.ncei.noaa.gov/erddap/) | RESTful access to gridded and tabular oceanographic/environmental datasets | 🟢 No | ✅ | ✅⭐ |
| [Copernicus Marine Toolbox](https://marine.copernicus.eu/access-data/) | Free open marine data: ocean temperature, salinity, currents, and forecasts | 🟡 API Key | ✅ | ✅⭐ |
| [Global Fishing Watch API](https://globalfishingwatch.org/our-apis/documentation) | Vessel tracking, fishing activity, port visits, and marine infrastructure data | 🟡 API Key | ✅ | ✅⭐ |
| [Storm Glass API](https://stormglass.io/) | Marine weather data: wave height, swell, wind, tides from 20+ sources | 🟡 API Key | ✅ | ✅⭐ |
| [WorldTides API](https://www.worldtides.info/apidocs) | Global tidal predictions and heights for any location worldwide | 🟡 API Key | ✅ | ✅⭐ |
| [EMODnet Bathymetry REST API](https://rest.emodnet-bathymetry.eu/) | European marine bathymetry data; depth samples along profiles and locations | 🟢 No | ✅ | ✅⭐ |
| [GEBCO Gridded Bathymetry](https://www.gebco.net/data-products/gridded-bathymetry-data) | Authoritative global ocean floor elevation data at 15 arc-second resolution | 🟢 No | ✅ | ⚠️ |
| [Argovis API](https://argovis.colorado.edu/) | Access Argo float profiles: ocean temperature, salinity, and BGC data | 🟢 No | ✅ | ✅⭐ |
| [ADMIRALTY Marine APIs](https://www.admiralty.co.uk/access-data/apis) | UK Hydrographic Office tidal, navigation, and marine chart data | 🟡 API Key | ✅ | ✅ |
| [IODE Ocean Data Portal](https://iode.org/) | International Oceanographic Data Exchange network for 100+ countries | 🟢 No | ✅ | ⚠️ |
| [OceanSync API](https://oceansync.com) | Cloud infrastructure for ocean data storage and API access | 🟡 API Key | ✅ | ✅ |

---

## 🧠 Brain-Computer Interface APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [BrainFlow](https://brainflow.readthedocs.io/) | Hardware-agnostic library for EEG/EMG/ECG biosensor data in 9+ languages | 🟢 No | ✅ | ✅⭐ |
| [EMOTIV Cortex API](https://emotiv.gitbook.io/cortex-api) | JSON/WebSocket API for EMOTIV headsets; BCI, mental commands, facial expressions | 🟡 API Key | ✅ | ✅⭐ |
| [NeuroSky Developer Tools](https://developer.neurosky.com/) | SDK and API for ThinkGear brainwave sensor; attention and meditation metrics | 🟡 API Key | ✅ | ✅ |
| [OpenBCI Developer Tools](https://docs.openbci.com/ForDevelopers/SoftwareDevelopment/) | Open-source EEG/EMG hardware with SDKs in Python, Java, and Node.js | 🟢 No | ✅ | ✅⭐ |
| [MNE-Python](https://mne.tools/stable/index.html) | Comprehensive Python library for EEG/MEG signal processing and analysis | 🟢 No | ✅ | ✅⭐ |
| [MNE-LSL](https://mne.tools/mne-lsl/) | Real-time brain signal streaming framework integrated with MNE-Python via LSL | 🟢 No | ✅ | ✅ |
| [Lab Streaming Layer (LSL)](https://labstreaminglayer.org/) | Open-source middleware for synchronized streaming of neural/physiological data | 🟢 No | ✅ | ✅ |
| [OpenNeuro API](https://docs.openneuro.org/api.html) | Free platform for sharing and accessing neuroimaging datasets (BIDS format) | 🟡 API Key | ✅ | ✅⭐ |
| [BrainAccess SDK](https://www.brainaccess.ai/) | EEG hardware and Python SDK for cognitive monitoring and neurofeedback apps | 🟡 API Key | ✅ | ✅ |
| [NeuroMore Studio](https://github.com/neuromore/studio) | Open-source biofeedback and neurofeedback platform with visual signal processing | 🟢 No | ✅ | ⚠️ |
| [NextMind SDK](https://github.com/Snapchat/NextMind) | Attention-based BCI SDK with Unity integration for mind-controlled apps | 🟢 No | ✅ | ⚠️ |
| [PyEEG / EEGLib](https://github.com/forrestbao/pyeeg) | Python library for EEG feature extraction and analysis for BCI pipelines | 🟢 No | ✅ | ⚠️ |

---

## 🍷 Wine & Beverage APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Wine-Searcher API](https://www.wine-searcher.com/trade/api) | Wine price comparison and tasting data via REST | 🟡 API Key | ✅ | ✅ |
| [WineVybe API](https://winevybe.com/wine-api/) | Wine, beer and liquor database with regions and tasting notes | 🟡 API Key | ✅ | ✅ |
| [Global Wine Score API](https://globalwinescore.docs.apiary.io/) | Aggregated wine scores from top critics | 🟡 API Key | ✅ | ✅⭐ |
| [Open Brewery DB](https://www.openbrewerydb.org/documentation) | Free open-source brewery dataset worldwide | 🟢 No | ✅ | ✅⭐ |
| [TheCocktailDB](https://www.thecocktaildb.com/api.php) | Open cocktail database with drink recipes and images | 🟡 API Key | ✅ | ✅⭐ |
| [Untappd API](https://untappd.com/api/docs) | Social beer discovery with check-ins and ratings | 🔴 OAuth | ✅ | ✅ |
| [Open Food Facts API](https://openfoodfacts.github.io/openfoodfacts-server/api/) | Crowdsourced food and beverage product data | 🟢 No | ✅ | ✅⭐ |
| [API Ninjas Cocktail](https://api-ninjas.com/api/cocktail) | Search thousands of cocktail recipes by name or ingredient | 🟡 API Key | ✅ | ✅⭐ |
| [Catalog.beer API](https://catalog.beer/api-docs) | Open beer catalog database in JSON | 🟡 API Key | ✅ | ✅⭐ |
| [Vivino API](https://www.apiorb.com/apis/vivino-api) | Wine ratings, reviews, prices and barcode scanning | 🟡 API Key | ✅ | ✅ |

---

## 📰 Print & Publishing APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Lulu Print API](https://developers.lulu.com/) | Print-on-demand book printing and global fulfillment | 🔴 OAuth | ✅ | ✅⭐ |
| [Printify API](https://developers.printify.com/) | Print-on-demand product creation and order fulfillment | 🟡 API Key | ✅ | ✅⭐ |
| [Issuu API v2](https://developer.issuu.com/) | Digital publishing platform for documents | 🟡 API Key | ✅ | ✅⭐ |
| [ISBNdb API](https://isbndb.com/isbndb-api-documentation-v2) | Largest book database with 107M+ titles | 🟡 API Key | ✅ | ✅⭐ |
| [Open Library API](https://openlibrary.org/developers/api) | Free book data in JSON/YAML/RDF | 🟢 No | ✅ | ✅⭐ |
| [Crossref REST API](https://www.crossref.org/documentation/retrieve-metadata/rest-api/) | Scholarly metadata with DOIs and citations | 🟢 No | ✅ | ✅⭐ |
| [PrintAPI.io](https://www.printapi.io/services/rest-api) | Send print orders directly to printers worldwide | 🟡 API Key | ✅ | ✅ |
| [Peecho Print API](https://www.peecho.com/blog/issuu-api-checkout) | Print checkout integration for digital publishers | 🟡 API Key | ✅ | ✅ |

---

## 📚 Library & Archival APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Library of Congress API](https://www.loc.gov/apis/) | Millions of digitized items and collections in JSON | 🟢 No | ✅ | ✅⭐ |
| [DPLA API](https://pro.dp.la/developers/api-basics) | Digital Public Library of America with 40M+ items | 🟡 API Key | ✅ | ✅⭐ |
| [Europeana APIs](https://apis.europeana.eu/en) | 50M+ cultural heritage items from European institutions | 🟡 API Key | ✅ | ✅⭐ |
| [HathiTrust API](https://www.hathitrust.org/member-libraries/resources-for-librarians/data-resources/bibliographic-api/) | Bibliographic and rights data for digital collection | 🟢 No | ✅ | ✅ |
| [Harvard LibraryCloud API](https://library.harvard.edu/services-tools/harvard-library-apis-datasets) | 12.7M+ bib records from Harvard collections | 🟢 No | ✅ | ✅ |
| [Internet Archive API](https://archive.org/developers/) | Wayback Machine, book scans, audio, video and metadata | 🟢 No | ✅ | ✅⭐ |
| [OCLC WorldCat API](https://www.oclc.org/developer/api/oclc-apis.en.html) | World's largest library catalog search | 🟡 API Key | ✅ | ✅ |

---

## 👶 Childcare & Parenting APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [CDC Open Data API](https://open.cdc.gov/apis.html) | Public health data including child vaccinations | 🟢 No | ✅ | ✅⭐ |
| [Child Care Aware API](https://info.childcareaware.org/blog/child-care-aware-of-america-announces-web-services-api-module-for-nds) | National Data System for childcare facility search | 🟡 API Key | ✅ | ✅ |
| [Brightwheel](https://mybrightwheel.com/) | Childcare management — attendance, billing, communication | 🟡 API Key | ✅ | ⚠️ |
| [Procare Solutions](https://www.procare.com/) | Childcare center management and check-in/out | 🟡 API Key | ✅ | ⚠️ |
| [HHS Developer APIs](https://www.hhs.gov/web/developer/index.html) | US Health and Human Services child welfare data | 🟢 No | ✅ | ✅ |
| [ChildCareCRM API](https://apitracker.io/a/childcarecrm) | Childcare center CRM for enrollments and leads | 🟡 API Key | ✅ | ✅ |

---

## 🐕 Veterinary & Animal Health APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [FDA Animal & Veterinary API](https://open.fda.gov/apis/animalandveterinary/) | Adverse event reports and drug safety for animals | 🟢 No | ✅ | ✅⭐ |
| [ezyVet API](https://developers.ezyvet.com/) | Veterinary practice management via REST/OAuth 2.0 | 🔴 OAuth | ✅ | ✅⭐ |
| [Provet REST API](https://developers.provetcloud.com/restapi/) | Cloud vet practice management for medical records | 🟡 API Key | ✅ | ✅⭐ |
| [Vetspire API](https://developer.vetspire.com/) | Veterinary practice data via GraphQL | 🟡 API Key | ✅ | ✅ |
| [iNaturalist API](https://api.inaturalist.org/v1/docs/) | Wildlife and species observations and identification | 🟢 No | ✅ | ✅⭐ |
| [Kindwise Insect.id API](https://github.com/flowerchecker/insect-id-examples) | ML-based insect identification from images | 🟡 API Key | ✅ | ✅⭐ |
| [USDA APHIS API](https://www.aphis.usda.gov/) | Animal health inspection and disease tracking | 🟢 No | ✅ | ✅ |
| [FishWatch API](https://www.fishwatch.gov/api-tos) | NOAA sustainable seafood species data | 🟢 No | ✅ | ✅⭐ |
| [Global Fishing Watch API](https://globalfishingwatch.org/our-apis/documentation) | Vessel tracking and marine species monitoring | 🟡 API Key | ✅ | ✅⭐ |

---

## 💎 Jewelry & Gemstone APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [GIA Report Results API](https://www.gia.edu/report-results-api) | Official GIA diamond and gemstone grading reports | 🟡 API Key | ✅ | ✅⭐ |
| [Rapaport API](https://raptech.rapaport.com/rapaport-developer-documentation/) | Diamond price lists and RapNet marketplace data | 🟡 API Key | ✅ | ✅ |
| [OpenFacet Diamond Pricing](https://openfacet.net/en/api-docs/) | Free real-time GIA-certified diamond prices | 🟢 No | ✅ | ✅⭐ |
| [Nivoda API](https://github.com/Nivoda/nivoda-api) | B2B diamond marketplace via GraphQL | 🟡 API Key | ✅ | ✅ |
| [IDEX API Center](https://api.idexonline.com/) | Diamond trading platform for inventory and pricing | 🟡 API Key | ✅ | ✅ |
| [Ximilar Collectibles AI](https://docs.ximilar.com/services/collectibles_recognition/) | Visual AI for jewelry authentication and grading | 🟡 API Key | ✅ | ✅⭐ |
| [Numista API](https://en.numista.com/api/doc/index.php) | Numismatic catalog for precious metal coins | 🟡 API Key | ✅ | ✅⭐ |

---

## 🚚 Moving & Relocation APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [SmartMoving API](https://smartmoving-prod-api-management.developer.azure-api.net/) | Moving company CRM for leads, estimates and jobs | 🟡 API Key | ✅ | ✅⭐ |
| [Intellizence Relocation API](https://docs.intellizence.com/dataset-api-v1.0/relocation-dataset-api) | Company relocation tracking dataset | 🟡 API Key | ✅ | ✅⭐ |
| [Walkscore API](https://www.walkscore.com/professional/api.php) | Walk Score, Transit Score and Bike Score | 🟡 API Key | ✅ | ✅⭐ |
| [AreaVibes API](https://www.areavibes.com/developer/) | Livability scores, cost of living and demographics | 🟡 API Key | ✅ | ✅⭐ |
| [ServiceTitan API](https://developer.servicetitan.io/) | Field service management for home services | 🟡 API Key | ✅ | ✅⭐ |
| [Jobber API](https://developer.getjobber.com/docs/) | Field service management via GraphQL | 🔴 OAuth | ✅ | ✅ |
| [Homesage.ai API](https://homesage.ai/docs/) | AI home valuation and renovation cost estimates | 🟡 API Key | ✅ | ✅⭐ |

---

## ⚱️ Funeral & Memorial APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [funeralOne API](https://api.funeralone.com/docs/) | Funeral home management for cases and services | 🟡 API Key | ✅ | ✅⭐ |
| [Passare Public API](https://www.passare.com/blog/what-is-a-public-api) | Cloud-based funeral case management | 🟡 API Key | ✅ | ✅ |
| [Obituary Assistant API](https://www.obituary-assistant.com/api/) | Automate adding and displaying obituaries | 🟡 API Key | ✅ | ✅⭐ |
| [Funeral Live API](https://www.postman.com/universal-moon-540385/workspace/funeral-live-api/) | Live streaming and memorial service management | 🟡 API Key | ✅ | ✅⭐ |
| [MemoryGiving API](https://www.memorygiving.com/api-information.aspx) | Memorial donation management and tribute pages | 🟡 API Key | ✅ | ✅ |
| [Express Funeral Funding API](https://www.expressfuneralfunding.com/api/) | Funeral funding and insurance assignment processing | 🟡 API Key | ✅ | ✅ |

---

## 🐛 Pest Control & Extermination APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [WorkWave/PestPac API](https://developer.workwave.com/) | Pest control business management and routing | 🟡 API Key | ✅ | ✅⭐ |
| [Briostack Public API](https://www.briostack.com/public-api) | Pest control CRM for customer and service data | 🟡 API Key | ✅ | ✅⭐ |
| [Pest Prophet API](https://www.pestprophet.com/api) | Weather-based pest and disease prediction | 🟡 API Key | ✅ | ✅⭐ |
| [Canada PPID API](https://health.canada.ca/en/open-data/pmra-ppid-arla-bdipa/index-050342) | Canadian pesticide product information database | 🟢 No | ✅ | ✅ |
| [NextBillion.ai Pest Control](https://nextbillion.ai/solutions/pest-control) | Route optimization for pest control fleets | 🟡 API Key | ✅ | ✅⭐ |

---

## 🧹 Cleaning & Janitorial APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [TIDY API](https://www.tidy.com/developers) | Cleaning service booking and management | 🟡 API Key | ✅ | ✅⭐ |
| [CleanCloud API](https://cleancloudapp.com/api) | Dry cleaning and laundry management | 🟡 API Key | ✅ | ✅⭐ |
| [Housecall Pro API](https://docs.housecallpro.com/) | Home cleaning business management | 🟡 API Key | ✅ | ✅ |
| [WorkWave API](https://developer.workwave.com/) | Route optimization for janitorial fleets | 🟡 API Key | ✅ | ✅⭐ |
| [Fieldwire API](https://developers.fieldwire.com/) | Task management for facility cleaning crews | 🟡 API Key | ✅ | ✅⭐ |

---

## 🌿 Landscaping & Garden APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Trefle API](https://trefle.io/) | Open-source botanical API with 400K+ plant species | 🟡 API Key | ✅ | ✅⭐ |
| [Perenual Plant API](https://perenual.com/) | Plant species data, care guides and hardiness zones | 🟡 API Key | ✅ | ✅⭐ |
| [Pl@ntNet API](https://my.plantnet.org/) | AI plant identification from photos with 35K+ species | 🟡 API Key | ✅ | ✅⭐ |
| [Plant.id API](https://www.kindwise.com/plant-id) | ML plant identification and health diagnosis | 🟡 API Key | ✅ | ✅⭐ |
| [OpenWeather Agro API](https://agromonitoring.com/api) | Agricultural weather and soil data for gardens | 🟡 API Key | ✅ | ✅⭐ |
| [Permapeople API](https://permapeople.org/knowledgebase/api-docs.html) | Permaculture plant database with companion planting | 🟡 API Key | ✅ | ✅ |
| [USDA Plants Database API](https://data.nal.usda.gov/dataset/usda-plants-database-api-r) | Official USDA plant data and conservation status | 🟢 No | ✅ | ✅ |
| [APIFarmer Plant Database](https://apifarmer.com/plant-database-api/) | 100K+ plant species with taxonomy data | 🟡 API Key | ✅ | ✅⭐ |

---

## 🏠 Home Improvement & DIY APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Home Assistant REST API](https://developers.home-assistant.io/docs/api/rest/) | Smart home automation via REST JSON | 🟡 API Key | ✅ | ✅⭐ |
| [Home Connect API](https://api-docs.home-connect.com/) | Control BSH home appliances (Bosch, Siemens) | 🔴 OAuth | ✅ | ✅⭐ |
| [Backyard API](https://docs.trajectdata.com/backyardapi/home-improvement-product-data-api/overview) | Home improvement product data from major retailers | 🟡 API Key | ✅ | ✅⭐ |
| [Homesage.ai API](https://homesage.ai/docs/) | AI renovation cost estimates and ROI analysis | 🟡 API Key | ✅ | ✅⭐ |
| [SONOFF DIY API](https://sonoff.tech/diy-developer/) | Local LAN control of SONOFF smart devices | 🟢 No | ✅ | ✅⭐ |
| [SerpApi Home Depot](https://serpapi.com/home-depot-product) | Home Depot product search with pricing and reviews | 🟡 API Key | ✅ | ✅⭐ |

---

## 🏺 Antiques & Collectibles APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Discogs API](https://www.discogs.com/developers) | Music collectibles, vinyl records and marketplace | 🔴 OAuth | ✅ | ✅⭐ |
| [TCGplayer API](https://docs.tcgplayer.com/docs/welcome) | Trading card game marketplace and pricing | 🟡 API Key | ✅ | ✅⭐ |
| [Numista API](https://en.numista.com/api/doc/index.php) | Numismatic catalog for coin search and pricing | 🟡 API Key | ✅ | ✅⭐ |
| [Ximilar Collectibles AI](https://docs.ximilar.com/services/collectibles_recognition/) | Visual AI for trading cards, coins and stamps | 🟡 API Key | ✅ | ✅⭐ |
| [Artsy API](https://developers.artsy.net/) | Art world data for artists, artworks and auctions | 🟡 API Key | ✅ | ✅⭐ |

---

## 🔮 Astrology & Horoscope APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [AstrologyAPI](https://astrologyapi.com/docs) | Full astrology platform for horoscopes and charts | 🟡 API Key | ✅ | ✅⭐ |
| [Prokerala Astrology API](https://api.prokerala.com/) | Vedic and Western astrology with Panchang | 🟡 API Key | ✅ | ✅⭐ |
| [Aztro API](https://aztro.sameerkumar.website/) | Free daily horoscope for all zodiac signs | 🟢 No | ✅ | ✅⭐ |
| [VedicAstroAPI](https://vedicastroapi.com/) | Vedic, Western, and Tarot in 21 languages | 🟡 API Key | ✅ | ✅⭐ |
| [Free Astrology API](https://freeastrologyapi.com/) | Free Indian and Western astrology calculations | 🟢 No | ✅ | ✅⭐ |
| [API Ninjas Horoscope](https://www.api-ninjas.com/api/horoscope) | Simple daily horoscope via REST JSON | 🟡 API Key | ✅ | ✅⭐ |
| [Vedic Rishi API](https://vedicrishi.in/web-astro-api) | Vedic astrology engine for Kundli and numerology | 🟡 API Key | ✅ | ✅ |

---

## 🎣 Fishing & Hunting APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Global Fishing Watch API](https://globalfishingwatch.org/our-apis/documentation) | Vessel tracking and fishing activity monitoring | 🟡 API Key | ✅ | ✅⭐ |
| [FishSource API](https://www.fishsource.org/apipie/v4/fisheries.html) | Fisheries sustainability data and assessments | 🟡 API Key | ✅ | ✅ |
| [OpenFisheries API](https://github.com/OpenFisheries/api.openfisheries.org) | Global fisheries landings data in JSON | 🟢 No | ✅ | ✅⭐ |
| [Idaho Fish & Game API](https://fishandgame.idaho.gov/ifwis/rest/services/wildlife/mhr/readme.html) | Real-time hunter harvest reports | 🟢 No | ✅ | ✅⭐ |
| [National Park Service API](https://www.nps.gov/subjects/developer/api-documentation.htm) | Park data including fishing/hunting regulations | 🟡 API Key | ✅ | ✅⭐ |
| [US Fish & Wildlife API](https://ecos.fws.gov/ServCatServices/servcat/v4/documentation/servcat-api.html) | Conservation and wildlife management records | 🟢 No | ✅ | ✅ |
| [TrailAPI](https://rapidapi.com/trailapi/api/trailapi) | Outdoor recreation locations and fishing spots | 🟡 API Key | ✅ | ✅⭐ |

---

## ⛺ Camping & Outdoor Recreation APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [RIDB API (Recreation.gov)](https://ridb.recreation.gov/docs) | Federal recreation areas, campsites and permits | 🟡 API Key | ✅ | ✅⭐ |
| [Campflare API](https://campflare.com/api) | Campground data with amenities and availability | 🟢 No | ✅ | ✅⭐ |
| [National Park Service API](https://www.nps.gov/subjects/developer/api-documentation.htm) | 400+ NPS parks with campgrounds and trails | 🟡 API Key | ✅ | ✅⭐ |
| [ACTIVE Campground API](https://developer.active.com/docs/read/Campground_APIs) | Campground search for US/Canada parks | 🟡 API Key | ✅ | ✅ |
| [Outdooractive Data API](https://developers.outdooractive.com/API-Reference/Data-API.v1.html) | European outdoor recreation data and trails | 🟡 API Key | ✅ | ✅ |
| [Camping.care API](https://documenter.getpostman.com/view/9467805/VUjQkj1d) | Campsite management and reservations | 🟡 API Key | ✅ | ✅⭐ |
| [Trailforks API](https://www.trailforks.com/about/api/) | Trail database with GPS tracks and conditions | 🟡 API Key | ✅ | ✅ |
| [Hiking Project Data API](https://www.hikingproject.com/data) | Trail data with routes, difficulty and GPS coordinates | 🟡 API Key | ✅ | ✅⭐ |

---

## 🏠 Mortgage & Home Loan APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Zillow Mortgages API](https://www.zillowgroup.com/developers/mortgage/) | Aggregated mortgage rate data and loan information | 🟡 API Key | ✅ | ✅⭐ |
| [Fannie Mae APIs](https://singlefamily.fanniemae.com/applications-technology/application-programming-interfaces-apis-developer-portal) | Loan performance, economics, and housing data | 🟡 API Key | ✅ | ✅ |
| [Freddie Mac Origination APIs](https://sf.freddiemac.com/tools-learning/apis/origination-apis) | Loan origination data and digital preapproval | 🟡 API Key | ✅ | ✅ |
| [Blend API](https://developers.blend.com/) | Digital lending platform for home loans and reports | 🟡 API Key | ✅ | ✅⭐ |
| [Polly Developer Hub](https://docs.polly.io/) | Mortgage product and pricing engine | 🟡 API Key | ✅ | ✅⭐ |
| [Optimal Blue API](https://www2.optimalblue.com/developer) | Mortgage pricing, lock management, best execution | 🟡 API Key | ✅ | ✅ |
| [ICE Mortgage Technology APIs](https://mortgagetech.ice.com/products/developer-portal) | Servicing and origination APIs for mortgage workflows | 🟡 API Key | ✅ | ✅ |
| [Floify API](https://floify.com/blog/mortgage-real-estate-open-api) | Mortgage point-of-sale platform integration | 🟡 API Key | ✅ | ✅ |
| [Brickflow API](https://brickflow.com/api) | Property finance comparison and loan data | 🟡 API Key | ✅ | ✅ |

---

## 📡 Network Monitoring & SNMP APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Cisco Meraki Dashboard API](https://developer.cisco.com/meraki/api-v1/get-network-snmp/) | Cloud network management and SNMP monitoring | 🟡 API Key | ✅ | ✅⭐ |
| [Datadog API](https://docs.datadoghq.com/api/latest/) | Infrastructure monitoring, metrics, and alerting | 🟡 API Key | ✅ | ✅⭐ |
| [Zabbix API](https://www.zabbix.com/documentation/current/en/manual/api) | Open-source network monitoring with JSON-RPC | 🟡 API Key | ✅ | ✅ |
| [PRTG API v2](https://www.paessler.com/support/prtg/api/v2/overview/index.html) | Network monitor with REST API and Swagger docs | 🟡 API Key | ✅ | ✅ |
| [LibreNMS API](https://docs.librenms.org/API/) | Open-source network monitoring via REST | 🟡 API Key | ✅ | ✅⭐ |
| [OpenNMS REST API](https://docs.opennms.com/horizon/33/development/rest/rest-api.html) | Enterprise open-source network monitoring | 🟡 API Key | ✅ | ✅ |
| [SolarWinds Observability API](https://documentation.solarwinds.com/en/success_center/observability/content/api/api-swagger.htm) | SaaS network and infrastructure observability | 🟡 API Key | ✅ | ✅ |
| [Nagios XI REST API](https://support.nagios.com/kb/category.php?id=105) | Classic network monitoring with REST/JSON interface | 🟡 API Key | ✅ | ⚠️ |

---

## 🛒 Procurement & Sourcing APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Coupa Core API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api) | Procurement platform for suppliers, POs and invoices | 🟡 API Key | ✅ | ✅⭐ |
| [SAP Ariba APIs](https://api.sap.com/package/SAPAribaOpenAPIs/rest) | Enterprise sourcing and procurement management | 🔴 OAuth | ✅ | ✅ |
| [Oracle Fusion Procurement](https://docs.oracle.com/en/cloud/saas/procurement/23b/fapra/api-suppliers.html) | Enterprise procurement REST APIs for suppliers | 🔴 OAuth | ✅ | ✅ |
| [JAGGAER ASO API](https://asodocs.jaggaer.com/) | Advanced sourcing optimizer with REST API | 🟡 API Key | ✅ | ✅ |
| [Google Cloud Commerce Procurement](https://cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest) | Cloud marketplace procurement management | 🔴 OAuth | ✅ | ✅⭐ |
| [ProcurementFlow API](https://www.procurementflow.com/helpcenter/api-documentation) | Purchase request and workflow management | 🟡 API Key | ✅ | ✅ |

---

## 📋 Public Records & FOIA APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [FOIA.gov API](https://www.foia.gov/developer/) | National FOIA Portal for submitting and tracking requests | 🟡 API Key | ✅ | ✅⭐ |
| [GovInfo API](https://api.govinfo.gov/docs/) | US government documents, bills, and federal records | 🟡 API Key | ✅ | ✅⭐ |
| [Federal Register API](https://www.federalregister.gov/developers/documentation/api/v1) | Federal rules, notices, and presidential documents | 🟢 No | ✅ | ✅⭐ |
| [MuckRock API](https://www.muckrock.com/api/) | FOIA request tracking and public records management | 🟡 API Key | ✅ | ✅⭐ |
| [OpenCorporates API](https://api.opencorporates.com/documentation/API-Reference) | Global company registry data for 200M+ companies | 🟡 API Key | ✅ | ✅⭐ |
| [CourtListener REST API](https://www.courtlistener.com/help/api/rest/) | Federal/state case law and PACER data | 🟡 API Key | ✅ | ✅⭐ |
| [data.gov APIs](https://api.data.gov/) | Centralized API key service for US federal data | 🟡 API Key | ✅ | ✅ |

---

## 📬 Queue & Task Management APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Google Cloud Tasks API](https://cloud.google.com/tasks/docs/reference/rest) | Managed task queue for asynchronous execution | 🔴 OAuth | ✅ | ✅⭐ |
| [RabbitMQ Management API](https://www.rabbitmq.com/docs/http-api-reference) | Message broker management with REST/JSON | 🟡 API Key | ✅ | ✅⭐ |
| [Cloudflare Queue Tasks](https://developers.cloudflare.com/agents/api-reference/queue-tasks/) | Task queue for async background processing | 🟡 API Key | ✅ | ✅⭐ |
| [Queue-it Management API](https://queue-it.com/developers/rest-api/) | Virtual waiting room queue management | 🟡 API Key | ✅ | ✅⭐ |
| [AWS SQS API](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/) | Managed message queue for microservices | 🟡 API Key | ✅ | ✅ |
| [Azure Queue Storage REST API](https://learn.microsoft.com/en-us/rest/api/storageservices/queue-service-rest-api) | Cloud message queue storage service | 🟡 API Key | ✅ | ✅ |

---

## 🤖 Robotics & Drone APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [DJI Developer SDKs](https://developer.dji.com/) | Mobile, Onboard, Cloud, and Payload SDKs for DJI drones | 🟡 API Key | ✅ | ✅ |
| [DJI Cloud API](https://developer.dji.com/doc/cloud-api-tutorial/en/) | MQTT/HTTPS APIs for DJI drone fleet management | 🟡 API Key | ✅ | ✅ |
| [MAVLink Protocol](https://mavlink.io/en/) | Open standard messaging protocol for drones | 🟢 No | ✅ | ⚠️ |
| [DroneKit](https://dronekit.io/) | Open-source drone app development | 🟢 No | ✅ | ✅ |
| [FlytBase Drone APIs](https://www.flytbase.com/drone-api) | Unified cloud APIs abstracting drone complexity | 🟡 API Key | ✅ | ✅⭐ |
| [Parrot Drone REST API](https://developer.parrot.com/docs/webserver-api/overview.html) | REST and WebSocket endpoints for Parrot drones | 🟢 No | ✅ | ✅⭐ |
| [Autel Developer SDK](https://developer.autelrobotics.com/) | SDKs for autonomous flying, gimbal and camera | 🟡 API Key | ✅ | ✅ |
| [MAVSDK (Dronecode)](https://dronecode.org/sdk/) | Standards-compliant MAVLink API in multiple languages | 🟢 No | ✅ | ✅ |

---

## 📊 Sales Intelligence & Enablement APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [ZoomInfo API](https://docs.zoominfo.com/) | 200M+ B2B contact/company data and intent signals | 🟡 API Key | ✅ | ✅⭐ |
| [Apollo.io API](https://docs.apollo.io/) | B2B sales intelligence with 210M+ contacts | 🟡 API Key | ✅ | ✅⭐ |
| [Clearbit Enrichment API](https://help.clearbit.com/hc/en-us/sections/360002035034--Enrichment-API) | Person and company data enrichment for B2B | 🟡 API Key | ✅ | ✅⭐ |
| [Lusha API](https://docs.lusha.com/) | B2B contact enrichment and prospecting | 🟡 API Key | ✅ | ✅⭐ |
| [UpLead API](https://docs.uplead.com/) | B2B lead data enrichment and contact lookups | 🟡 API Key | ✅ | ✅⭐ |
| [Gong.io API](https://help.gong.io/docs/what-the-gong-api-provides) | Conversation intelligence for call recordings | 🟡 API Key | ✅ | ✅⭐ |
| [Outreach REST API](https://developers.outreach.io/api/) | Sales engagement sequences and analytics | 🔴 OAuth | ✅ | ✅⭐ |
| [Salesloft API](https://developers.salesloft.com/) | Sales engagement with cadences and people | 🔴 OAuth | ✅ | ✅⭐ |
| [Highspot API](https://www.highspot.com/integrations/) | Sales enablement content management | 🔴 OAuth | ✅ | ✅ |
| [Seismic API](https://apitracker.io/a/seismic) | Sales enablement content delivery | 🔴 OAuth | ✅ | ✅ |

---

## 👂 Social Listening & Brand Monitoring APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Brandwatch API](https://developers.brandwatch.com/) | Enterprise social listening and sentiment analysis | 🟡 API Key | ✅ | ✅⭐ |
| [Talkwalker API](https://developer.talkwalker.com/) | Social listening with image recognition | 🟡 API Key | ✅ | ✅⭐ |
| [Sprout Social API](https://api.sproutsocial.com/docs/) | Social media analytics and listening | 🔴 OAuth | ✅ | ✅⭐ |
| [Mention API](https://mention.com/en/media-monitoring-api/) | Media monitoring across web and social | 🟡 API Key | ✅ | ✅ |
| [Awario API](https://awario.com/social-listening-api/) | Real-time brand mention tracking | 🟡 API Key | ✅ | ✅ |
| [Phyllo Social Listening](https://www.getphyllo.com/social-listening-api) | Consent-based social data with sentiment | 🟡 API Key | ✅ | ✅⭐ |
| [Mentionlytics API](https://www.mentionlytics.com/social-media-monitoring-api/) | Social media monitoring across 25+ platforms | 🟡 API Key | ✅ | ✅ |
| [DataForSEO Brand Mentions](https://dataforseo.com/help-center/automated-mention-tracking-with-api-in-make) | Automated brand mention tracking | 🟡 API Key | ✅ | ✅⭐ |

---

## 👥 Talent & Workforce Management APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [BambooHR API](https://documentation.bamboohr.com/docs) | HR platform for employee data and ATS | 🟡 API Key | ✅ | ✅⭐ |
| [Workday API](https://community.workday.com/api) | Enterprise HCM with REST APIs for HR | 🔴 OAuth | ✅ | ✅ |
| [UKG Developer Hub](https://developer.ukg.com/) | Workforce management for scheduling and time | 🔴 OAuth | ✅ | ✅ |
| [ADP Developer Resources](https://developers.adp.com/) | Workforce, payroll, and HR REST APIs | 🔴 OAuth | ✅ | ✅ |
| [Google Cloud Talent Solution](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest) | Job search and talent matching powered by ML | 🔴 OAuth | ✅ | ✅⭐ |
| [Greenhouse API](https://developers.greenhouse.io/) | Recruiting ATS with Harvest and Job Board APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Lever API](https://hire.lever.co/developer/documentation) | Recruiting platform REST API | 🟡 API Key | ✅ | ✅⭐ |
| [TalentLyft API](https://developers.talentlyft.com/) | Recruiting platform partner API | 🟡 API Key | ✅ | ✅ |
| [Namely API](https://developers.namely.com/) | All-in-one HR for payroll, benefits, talent | 🔴 OAuth | ✅ | ✅ |

---

## 🎥 Virtual Events & Webinar APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Zoom Webinars & Events API](https://developers.zoom.us/docs/api/rest/zoom-events-api/) | Webinar scheduling, registration, and reporting | 🔴 OAuth | ✅ | ✅⭐ |
| [Microsoft Graph Virtual Events](https://learn.microsoft.com/en-us/graph/api/resources/virtualeventwebinar) | Teams webinar and virtual event management | 🔴 OAuth | ✅ | ✅⭐ |
| [GoTo Webinar API](https://developer.goto.com/GoToWebinarV2) | Webinar scheduling and attendance | 🔴 OAuth | ✅ | ✅⭐ |
| [Webex Webinar API](https://developer.webex.com/docs/api/guides/webinar-guide) | Cisco Webex webinar management via REST | 🔴 OAuth | ✅ | ✅⭐ |
| [RingCentral Webinar API](https://developers.ringcentral.com/webinar-api) | Programmable webinar with analytics | 🔴 OAuth | ✅ | ✅⭐ |
| [Eventbrite API](https://www.eventbrite.com/platform/api) | Event creation, ticketing and discovery | 🔴 OAuth | ✅ | ✅⭐ |
| [Cvent REST API](https://developers.cvent.com/) | Enterprise event management platform | 🔴 OAuth | ✅ | ✅ |
| [Bizzabo REST API](https://bizzabo.stoplight.io/docs/bizzabo-rest-api/) | Event management for hybrid and virtual events | 🟡 API Key | ✅ | ✅⭐ |
| [Accelevents API](https://developer.accelevents.com/) | Virtual networking, ticketing and gamification | 🟡 API Key | ✅ | ✅⭐ |
| [Google Meet REST API](https://developers.google.com/workspace/meet/api/guides/overview) | Google Meet meeting management | 🔴 OAuth | ✅ | ✅⭐ |

---

## ♻️ Waste & Recycling Management APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Waste Management API](https://api.wm.com/) | Customer data, balance, contracts and pickup status | 🟡 API Key | ✅ | ✅⭐ |
| [EPA I-WASTE API](https://iwaste.epa.gov/developers) | EPA waste characterization and disposal support | 🟡 API Key | ✅ | ✅⭐ |
| [UK Waste Services API](https://communitiesuk.github.io/waste-service-standards/apis/waste_services.html) | Council waste and recycling collection data | 🟡 API Key | ✅ | ✅⭐ |
| [Earth911 Search API](https://api.earth911.com/) | Largest recycling directory with 350+ materials | 🟡 API Key | ✅ | ✅ |
| [Sensoneo Developer API](https://developer.sensoneo.com/) | Smart waste bin sensors and fill-level monitoring | 🟡 API Key | ✅ | ✅ |
| [EPA Envirofacts API](https://www.epa.gov/enviro/envirofacts-data-service-api) | Environmental facility data including waste handlers | 🟢 No | ✅ | ✅⭐ |

---

## 💧 Water Quality & Utility APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [USGS Water Data APIs](https://api.waterdata.usgs.gov/) | Modernized REST API for streamflow and groundwater | 🟢 No | ✅ | ✅⭐ |
| [Water Quality Portal (WQP)](https://www.waterqualitydata.us/webservices_documentation/) | Water quality data from USGS, EPA and 400+ agencies | 🟢 No | ✅ | ✅⭐ |
| [EPA Envirofacts API](https://www.epa.gov/enviro/envirofacts-data-service-api) | RESTful access to EPA environmental data | 🟢 No | ✅ | ✅⭐ |
| [USGS Water Services](https://waterservices.usgs.gov/) | Real-time and historical water data | 🟢 No | ✅ | ✅⭐ |
| [UK EA Water Quality](https://www.api.gov.uk/ea/water-quality/) | Water quality archive in JSON, CSV, and RDF | 🟢 No | ✅ | ✅⭐ |
| [Meersens Water Quality API](https://meersens.com/api/?lang=en) | Tap water quality and WHO compliance | 🟡 API Key | ✅ | ✅⭐ |
| [Water Atlas API](https://api.wateratlas.usf.edu/Docs) | Florida water body information and monitoring | 🟢 No | ✅ | ✅ |

---

## 💒 Wedding & Event Planning APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Eventtia API](https://www.eventtia.com/en/api-services/) | Event management with custom workflows | 🟡 API Key | ✅ | ✅ |
| [Grenadine Event APIs](https://grenadine.co/apis/) | Event planner data exchange with Swagger UI | 🟡 API Key | ✅ | ✅⭐ |
| [Hire Space API](https://hirespace.com/c/api-partner) | Thousands of venues for events globally | 🟡 API Key | ✅ | ✅ |
| [Eventzilla API](https://developer.eventzilla.net/docs/) | Event registration and ticketing | 🟡 API Key | ✅ | ✅ |
| [Splash API](https://api-docs.splashthat.com/) | Event marketing platform with branded pages | 🟡 API Key | ✅ | ✅ |

---

## 📶 WiFi & Network Analytics APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Cisco Meraki API](https://developer.cisco.com/meraki/) | Cloud-managed WiFi monitoring and analytics | 🟡 API Key | ✅ | ✅⭐ |
| [Ubiquiti UniFi API](https://help.ui.com/hc/en-us/articles/30076656117655) | Network management, device status and health | 🟡 API Key | ✅ | ✅⭐ |
| [Juniper Mist REST API](https://www.juniper.net/documentation/us/en/software/mist/automation-integration/topics/concept/restful-api-overview.html) | AI-driven WiFi analytics and location services | 🟡 API Key | ✅ | ✅⭐ |
| [HPE Aruba Central REST API](https://developer.arubanetworks.com/central/docs/rest-api-getting-started) | WiFi analytics and device management | 🔴 OAuth | ✅ | ✅⭐ |
| [Datadog Network Monitoring](https://docs.datadoghq.com/api/latest/) | Network performance monitoring and analytics | 🟡 API Key | ✅ | ✅⭐ |

---

## 💲 Dynamic Pricing & Revenue Management APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [PredictHQ Demand Intelligence](https://docs.predicthq.com/) | Global events data for demand-driven pricing | 🔴 OAuth | ✅ | ✅⭐ |
| [PriceLabs Dynamic Pricing](https://hello.pricelabs.co/dynamic-pricing-api/) | Vacation rental dynamic pricing and revenue | 🟡 API Key | ✅ | ✅⭐ |
| [Prisync API](https://prisync.com/api) | Competitor price tracking and pricing rules | 🟡 API Key | ✅ | ✅⭐ |
| [Competera](https://competera.ai/) | AI-powered retail pricing optimization | 🟡 API Key | ✅ | ✅ |
| [Zuplo API Monetization](https://zuplo.com/blog/2025/03/31/api-pricing-strategies) | API gateway with usage-based pricing | 🟡 API Key | ✅ | ✅⭐ |

---

## 📊 Customer Data Platform (CDP) APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Twilio Segment Public API](https://docs.segmentapis.com/) | Sources, destinations, warehouses and tracking | 🟡 API Key | ✅ | ✅⭐ |
| [mParticle Developer API](https://docs.mparticle.com/developers/) | CDP with 250+ integrations and profile API | 🟡 API Key | ✅ | ✅⭐ |
| [RudderStack API](https://www.rudderstack.com/docs/api/) | Warehouse-first open-source CDP | 🟡 API Key | ✅ | ✅⭐ |
| [Treasure Data CDP API](https://api-docs.treasuredata.com/) | Enterprise CDP with audience APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Tealium API](https://docs.tealium.com/api/) | AudienceStream CDP with Collect HTTP API | 🟡 API Key | ✅ | ✅ |
| [CM.com CDP API](https://developers.cm.com/mobile-marketing-cloud/docs/introduction-cdp-profiles) | CDP profiles and events REST APIs | 🟡 API Key | ✅ | ✅⭐ |

---

## 🔒 Consent & Privacy Management APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [OneTrust](https://developer.onetrust.com/) | Enterprise privacy management with consent and DSAR APIs | 🔴 OAuth | ✅ | ✅⭐ |
| [Didomi](https://developers.didomi.io/) | Consent management platform for GDPR/CCPA compliance | 🟡 API Key | ✅ | ✅⭐ |
| [Osano](https://developers.osano.com/) | Unified consent platform with REST API | 🟡 API Key | ✅ | ✅⭐ |
| [Usercentrics](https://docs.usercentrics.com/) | CMP with consent management API for web and mobile | 🟡 API Key | ✅ | ✅ |
| [Cookiebot](https://www.cookiebot.com/en/developer/) | Cookie consent platform with REST data extraction | 🟡 API Key | ✅ | ✅ |
| [Twilio Consent API](https://www.twilio.com/docs/messaging/features/consent-api) | Messaging consent management for opt-in/opt-out | 🟡 API Key | ✅ | ✅⭐ |
| [Google Consent Management](https://cloud.google.com/healthcare-api/docs/concepts/consent) | Cloud Healthcare consent module | 🔴 OAuth | ✅ | ✅⭐ |
| [Salesforce Consent API](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_consent.htm) | REST API for data subject consent preferences | 🔴 OAuth | ✅ | ✅⭐ |
| [Securiti.ai](https://securiti.ai/developers/) | AI-powered data privacy and consent orchestration | 🔴 OAuth | ✅ | ✅ |

---

## 😊 Employee Engagement & Culture APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Culture Amp](https://docs.api.cultureamp.com/) | Employee engagement, performance and development API | 🔴 OAuth | ✅ | ✅⭐ |
| [Lattice](https://lattice.com/api) | People management for engagement and analytics | 🟡 API Key | ✅ | ✅⭐ |
| [15Five](https://success.15five.com/hc/en-us/articles/360002699631-API) | Performance management for feedback and OKRs | 🟡 API Key | ✅ | ✅ |
| [Qualtrics](https://api.qualtrics.com/) | Experience management REST API for surveys | 🟡 API Key | ✅ | ✅⭐ |
| [Medallia](https://developer.medallia.com/) | Experience cloud API for employee feedback | 🔴 OAuth | ✅ | ✅⭐ |
| [Microsoft Viva Insights](https://learn.microsoft.com/en-us/graph/api/resources/viva-insights-overview) | Workplace analytics and employee wellbeing | 🔴 OAuth | ✅ | ✅⭐ |
| [HiBob](https://apidocs.hibob.com/) | HR platform REST API for people data | 🟡 API Key | ✅ | ✅⭐ |

---

## 🪞 Digital Twin & Simulation APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Azure Digital Twins](https://learn.microsoft.com/en-us/rest/api/azure-digitaltwins/) | Cloud platform for IoT-connected digital models | 🔴 OAuth | ✅ | ✅⭐ |
| [Eclipse Ditto](https://eclipse.dev/ditto/) | Open-source digital twin framework with REST/WebSocket | 🟡 API Key | ✅ | ✅⭐ |
| [AWS IoT TwinMaker](https://docs.aws.amazon.com/iot-twinmaker/) | AWS service for building digital twins | 🟡 API Key | ✅ | ✅⭐ |
| [Siemens Insights Hub](https://documentation.mindsphere.io/) | Industrial IoT platform for digital twin modeling | 🔴 OAuth | ✅ | ✅ |
| [Ansys PyTwin](https://twin.docs.pyansys.com/) | Python library for simulation-based digital twins | 🟢 No | ✅ | ✅ |
| [AnyLogic Cloud](https://www.anylogic.com/features/digital-twin/) | Simulation platform with REST API for digital twin models | 🟡 API Key | ✅ | ✅ |
| [Bentley iTwin Platform](https://developer.bentley.com/apis/) | Infrastructure digital twin with REST APIs | 🔴 OAuth | ✅ | ✅⭐ |

---

## ⚡ Edge Computing & CDN APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Cloudflare Workers](https://developers.cloudflare.com/workers/) | Serverless edge compute at 300+ locations | 🟡 API Key | ✅ | ✅⭐ |
| [Fastly Compute](https://developer.fastly.com/) | High-performance edge computing with Wasm | 🟡 API Key | ✅ | ✅⭐ |
| [Akamai EdgeWorkers](https://techdocs.akamai.com/edgeworkers/reference/api) | Deploy JavaScript on Akamai edge servers | 🟡 API Key | ✅ | ✅⭐ |
| [AWS Lambda@Edge](https://docs.aws.amazon.com/lambda/latest/dg/lambda-edge.html) | Serverless functions at CloudFront edge locations | 🟡 API Key | ✅ | ✅⭐ |
| [Vercel Edge Functions](https://vercel.com/docs/functions/runtimes/edge) | Edge-native JavaScript/TypeScript functions | 🟡 API Key | ✅ | ✅⭐ |
| [Deno Deploy](https://docs.deno.com/deploy/) | Globally distributed edge runtime | 🟡 API Key | ✅ | ✅⭐ |
| [Supabase Edge Functions](https://supabase.com/docs/guides/functions) | Deno-powered edge functions with Supabase | 🟡 API Key | ✅ | ✅⭐ |
| [Netlify Edge Functions](https://docs.netlify.com/edge-functions/overview/) | Deno-based edge functions on Netlify CDN | 🟡 API Key | ✅ | ✅⭐ |

---

## 🤖 AIOps & IT Operations APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [PagerDuty](https://developer.pagerduty.com/api-reference) | Incident management for alerts and escalations | 🟡 API Key | ✅ | ✅⭐ |
| [Splunk ITSI](https://docs.splunk.com/Documentation/ITSI/latest/RESTAPI/ITSIRESTAPIreference) | IT Service Intelligence REST API | 🟡 API Key | ✅ | ✅⭐ |
| [New Relic](https://docs.newrelic.com/docs/apis/intro-apis/introduction-new-relic-apis/) | Full-stack observability with REST and GraphQL | 🟡 API Key | ✅ | ✅⭐ |
| [BigPanda](https://docs.bigpanda.io/) | AIOps for event correlation and incident management | 🟡 API Key | ✅ | ✅⭐ |
| [ServiceNow ITOM](https://developer.servicenow.com/) | IT Operations Management REST API | 🔴 OAuth | ✅ | ✅⭐ |
| [Dynatrace](https://docs.dynatrace.com/docs/dynatrace-api) | Software intelligence for automated AIOps | 🟡 API Key | ✅ | ✅⭐ |
| [Keep (Open Source)](https://www.keephq.dev/) | Open-source AIOps for alert management | 🟡 API Key | ✅ | ✅⭐ |

---

## 📞 Unified Communications (UCaaS) APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [RingCentral](https://developers.ringcentral.com/api-reference/voice) | Unified voice, messaging, video, and fax API | 🔴 OAuth | ✅ | ✅⭐ |
| [Vonage (Nexmo)](https://developer.vonage.com/en/documentation) | Communications APIs for voice, SMS and video | 🟡 API Key | ✅ | ✅⭐ |
| [Webex Connect](https://cpaas.webex.com/products/webex-connect/apis-and-sdks) | Cisco CPaaS for SMS, voice and omnichannel | 🔴 OAuth | ✅ | ✅ |
| [8x8 Communication APIs](https://www.8x8.com/products/apis) | Voice, video and messaging APIs | 🟡 API Key | ✅ | ✅ |
| [Plivo](https://www.plivo.com/docs/) | Cloud communications for voice and SMS | 🟡 API Key | ✅ | ✅⭐ |
| [MessageBird](https://developers.messagebird.com/) | Omnichannel SMS, voice and WhatsApp API | 🟡 API Key | ✅ | ✅⭐ |
| [Bandwidth](https://dev.bandwidth.com/) | Enterprise voice, messaging and emergency APIs | 🟡 API Key | ✅ | ✅⭐ |

---

## 👁️ Visual Search & Image Recognition APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Google Cloud Vision](https://cloud.google.com/vision/docs) | Image analysis for labeling, OCR and product search | 🟡 API Key | ✅ | ✅⭐ |
| [AWS Rekognition](https://docs.aws.amazon.com/rekognition/latest/dg/what-is.html) | Deep learning image and video analysis | 🟡 API Key | ✅ | ✅⭐ |
| [Clarifai](https://docs.clarifai.com/) | AI platform for image/video recognition | 🟡 API Key | ✅ | ✅⭐ |
| [ViSenze ViSearch](https://developers.visenze.com/api/) | Visual search and product recommendation | 🟡 API Key | ✅ | ✅⭐ |
| [Imagga](https://docs.imagga.com/) | Image tagging and visual similarity search | 🟡 API Key | ✅ | ✅⭐ |
| [Sightengine](https://sightengine.com/docs/) | Image and video moderation REST API | 🟡 API Key | ✅ | ✅⭐ |
| [Nyris](https://www.nyris.io/products/visual-search-api) | Visual search for product recognition | 🟡 API Key | ✅ | ✅ |
| [Ximilar](https://docs.ximilar.com/) | Custom image recognition and visual search | 🟡 API Key | ✅ | ✅⭐ |
| [Roboflow](https://docs.roboflow.com/) | Computer vision for object detection and segmentation | 🟡 API Key | ✅ | ✅⭐ |

---

## 🎯 Customer Success & Retention APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Gainsight](https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/) | Customer success platform for CTAs and usage data | 🟡 API Key | ✅ | ✅⭐ |
| [ChurnZero](https://churnzero.com/features/rest-api/) | Customer success for churn tracking | 🟡 API Key | ✅ | ✅⭐ |
| [Totango](https://support.totango.com/hc/en-us/sections/360005893212-Totango-API) | Customer data hub for account health | 🟡 API Key | ✅ | ✅ |
| [Planhat](https://www.planhat.com/developers) | Customer platform for health scores and revenue | 🟡 API Key | ✅ | ✅⭐ |
| [Vitally](https://docs.vitally.io/api/) | Customer success for health scores and analytics | 🟡 API Key | ✅ | ✅⭐ |
| [Customer.io](https://docs.customer.io/integrations/api/customerio-apis/) | Messaging automation for behavioral campaigns | 🟡 API Key | ✅ | ✅⭐ |

---

## 💹 Revenue Operations & Intelligence APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Gong](https://help.gong.io/docs/what-the-gong-api-provides) | Revenue intelligence for calls and transcripts | 🟡 API Key | ✅ | ✅⭐ |
| [Clari](https://developer.clari.com/) | Revenue orchestration for forecasting and deals | 🔴 OAuth | ✅ | ✅⭐ |
| [Outreach](https://developers.outreach.io/api/) | Sales execution for sequences and engagement | 🔴 OAuth | ✅ | ✅⭐ |
| [Pipedrive](https://developers.pipedrive.com/docs/api/v1) | Sales CRM for deals and pipelines | 🟡 API Key | ✅ | ✅⭐ |
| [Close CRM](https://developer.close.com/) | Sales CRM for leads and activities | 🟡 API Key | ✅ | ✅⭐ |
| [People.ai](https://developer.people.ai/) | Revenue intelligence for activity capture | 🔴 OAuth | ✅ | ✅ |

---

## 📊 Data Governance & Lineage APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Collibra](https://developer.collibra.com/api/rest/data-governance) | Data governance platform with OpenAPI 3.0 | 🔴 OAuth | ✅ | ✅⭐ |
| [OpenLineage](https://openlineage.io/) | Open standard for data pipeline lineage | 🟢 No | ✅ | ✅⭐ |
| [OpenMetadata](https://open-metadata.org/) | Open-source metadata platform for catalog and lineage | 🟡 API Key | ✅ | ✅⭐ |
| [DataHub](https://docs.datahub.com/) | Open-source metadata platform with REST and GraphQL | 🟡 API Key | ✅ | ✅⭐ |
| [Apache Atlas](https://atlas.apache.org/) | Open-source metadata management framework | 🟡 API Key | ✅ | ✅ |
| [Google Dataplex Lineage](https://cloud.google.com/dataplex/docs/about-data-lineage) | Google Cloud lineage API for data flows | 🔴 OAuth | ✅ | ✅⭐ |
| [Databricks Unity Catalog](https://docs.databricks.com/api/workspace/catalogs) | Unified data governance and lineage on Databricks | 🔴 OAuth | ✅ | ✅⭐ |
| [Atlan](https://developer.atlan.com/) | Active metadata platform with OpenLineage support | 🟡 API Key | ✅ | ✅⭐ |
| [Microsoft Purview](https://learn.microsoft.com/en-us/purview/) | Data governance with catalog, scanning and lineage | 🔴 OAuth | ✅ | ✅⭐ |

---

## 🔗 Service Mesh & API Gateway APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Kong Gateway](https://developer.konghq.com/gateway/) | Open-source API gateway with Admin REST API | 🟡 API Key | ✅ | ✅⭐ |
| [Traefik](https://doc.traefik.io/traefik/operations/api/) | Cloud-native reverse proxy with REST API | 🟡 API Key | ✅ | ✅⭐ |
| [HashiCorp Consul](https://developer.hashicorp.com/consul/docs/use-case/service-mesh) | Service mesh and service discovery with HTTP API | 🟡 API Key | ✅ | ✅⭐ |
| [Tyk](https://tyk.io/docs/) | Open-source API gateway with REST API | 🟡 API Key | ✅ | ✅⭐ |
| [Apache APISIX](https://apisix.apache.org/docs/) | Cloud-native API gateway with Admin REST API | 🟡 API Key | ✅ | ✅⭐ |
| [AWS API Gateway](https://docs.aws.amazon.com/apigateway/) | Managed API gateway service | 🟡 API Key | ✅ | ✅⭐ |
| [Kuma](https://kuma.io/docs/) | Envoy-based service mesh by Kong | 🟡 API Key | ✅ | ✅⭐ |

---

## 🌐 Web Performance & Core Web Vitals APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Google PageSpeed Insights](https://developers.google.com/speed/docs/insights/v5/get-started) | Page performance analysis with Lighthouse and CrUX | 🟡 API Key | ✅ | ✅⭐ |
| [Chrome UX Report (CrUX)](https://developer.chrome.com/docs/crux/api) | Real-user Core Web Vitals data | 🟡 API Key | ✅ | ✅⭐ |
| [WebPageTest](https://docs.webpagetest.org/api/) | Performance testing from 30+ global locations | 🟡 API Key | ✅ | ✅⭐ |
| [GTmetrix](https://gtmetrix.com/api/docs/2.0/) | Automated website performance testing | 🟡 API Key | ✅ | ✅⭐ |
| [Pingdom](https://www.pingdom.com/api/) | Uptime monitoring and page speed checks | 🟡 API Key | ✅ | ✅⭐ |
| [DebugBear](https://www.debugbear.com/docs/api) | Core Web Vitals and Lighthouse monitoring | 🟡 API Key | ✅ | ✅⭐ |
| [Cloudflare Web Analytics](https://developers.cloudflare.com/web-analytics/) | Privacy-first analytics with Core Web Vitals | 🟡 API Key | ✅ | ✅⭐ |

---

## 🎙️ Voice Assistant & Smart Speaker APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Amazon Alexa Skills Kit](https://developer.amazon.com/en-US/docs/alexa/documentation-home.html) | Build voice skills and smart home controls | 🔴 OAuth | ✅ | ✅ |
| [Google Dialogflow](https://cloud.google.com/dialogflow/docs/) | Conversational AI platform for voice bots | 🔴 OAuth | ✅ | ✅⭐ |
| [Google Cloud Speech-to-Text](https://cloud.google.com/speech-to-text/docs) | Audio to text conversion in 125+ languages | 🟡 API Key | ✅ | ✅⭐ |
| [Picovoice](https://picovoice.ai/docs/) | On-device voice AI for wake word and STT | 🟡 API Key | ✅ | ✅⭐ |
| [Azure Speech Service](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/) | Microsoft speech-to-text and text-to-speech | 🟡 API Key | ✅ | ✅⭐ |
| [Deepgram](https://developers.deepgram.com/) | Speech recognition with real-time transcription | 🟡 API Key | ✅ | ✅⭐ |
| [AssemblyAI](https://www.assemblyai.com/docs/) | Speech-to-text with diarization and summarization | 🟡 API Key | ✅ | ✅⭐ |

---

## ⚙️ Process Mining & Analytics APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Celonis](https://developer.celonis.com/) | Process intelligence REST APIs | 🔴 OAuth | ✅ | ✅⭐ |
| [SAP Signavio](https://documentation.signavio.com/) | Process mining with OData endpoints | 🔴 OAuth | ✅ | ✅ |
| [UiPath Process Mining](https://docs.uipath.com/process-mining/) | Automation platform for process discovery | 🔴 OAuth | ✅ | ✅ |
| [ABBYY Timeline](https://www.abbyy.com/timeline/) | Process intelligence with REST API | 🟡 API Key | ✅ | ✅ |
| [QPR ProcessAnalyzer](https://support.qpr.com/processanalyzer_docs/) | Process mining for event log analysis | 🟡 API Key | ✅ | ✅ |
| [PM4Py](https://pm4py.fit.fraunhofer.de/) | Open-source Python process mining library | 🟢 No | ✅ | ✅ |

---

## 🏭 Industrial IoT & SCADA APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/Welcome.html) | Industrial IoT for asset modeling and monitoring | 🟡 API Key | ✅ | ✅⭐ |
| [ThingsBoard](https://thingsboard.io/docs/api/) | Open-source IoT with REST API and SCADA dashboards | 🟡 API Key | ✅ | ✅⭐ |
| [Open Automation Software](https://openautomationsoftware.com/products/developer-tools-apis/rest-api/) | IIoT REST API for real-time industrial data | 🟡 API Key | ✅ | ✅⭐ |
| [SCADACore](https://www.scadacore.com/live/features/api/) | IoT/SCADA REST API for sensor data | 🟡 API Key | ✅ | ✅ |
| [Siemens Insights Hub](https://developer.siemens.com/) | Industrial IoT platform with REST APIs | 🔴 OAuth | ✅ | ✅⭐ |
| [Azure IoT Hub](https://learn.microsoft.com/en-us/azure/iot-hub/) | Cloud IoT for device management and telemetry | 🔴 OAuth | ✅ | ✅⭐ |

---

## 🌲 Forestry & Natural Resources APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Global Forest Watch API](https://data-api.globalforestwatch.org/) | Tree cover loss and deforestation alerts | 🟡 API Key | ✅ | ✅⭐ |
| [NASA FIRMS](https://firms.modaps.eosdis.nasa.gov/api/) | Near real-time active fire data from MODIS/VIIRS | 🟡 API Key | ✅ | ✅⭐ |
| [NatureServe Explorer](https://explorer.natureserve.org/api-docs/) | Biodiversity and conservation status data | 🟡 API Key | ✅ | ✅⭐ |
| [OpenTreeMap](https://github.com/OpenTreeMap/otm-core/blob/develop/doc/api.md) | Open-source tree inventory and urban forestry | 🟢 No | ✅ | ✅ |
| [Sust Global Nature API](https://developers.sustglobal.com/nature-api-guide) | Nature-based carbon project durability indicators | 🟡 API Key | ✅ | ✅⭐ |
| [NOAA Climate Data API](https://www.ncdc.noaa.gov/cdo-web/webservices/v2) | Historical climate and weather data | 🟡 API Key | ✅ | ✅⭐ |

---

## 🤝 Affiliate Marketing & Partner APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Amazon Product Advertising API](https://webservices.amazon.com/paapi5/documentation/) | Amazon product data for affiliate monetization | 🟡 API Key | ✅ | ✅ |
| [CJ Affiliate API](https://developers.cj.com/) | Commission Junction advertiser/publisher data | 🟡 API Key | ✅ | ✅ |
| [Awin API](https://wiki.awin.com/index.php/Publisher_API) | Affiliate transactions, reports and promotions | 🟡 API Key | ✅ | ✅ |
| [Impact.com API](https://integrations.impact.com/) | Partnership management, conversions and catalog | 🟡 API Key | ✅ | ✅ |
| [Rakuten Advertising API](https://developers.rakutenadvertising.com/) | Affiliate link generation and reporting | 🔴 OAuth | ✅ | ✅ |
| [ShareASale API](https://account.shareasale.com/a-apimanager.cfm) | Merchant data and transaction reports | 🟡 API Key | ✅ | ✅ |
| [Travelpayouts API](https://travelpayouts.github.io/slate/) | Travel affiliate data for flights and hotels | 🟡 API Key | ✅ | ✅⭐ |
| [PartnerStack API](https://docs.partnerstack.com/reference) | B2B SaaS partner program management | 🟡 API Key | ✅ | ✅ |
| [Strackr API](https://strackr.com/affiliate-api) | Unified affiliate API for 190+ networks | 🟡 API Key | ✅ | ✅⭐ |
| [Rewardful API](https://www.rewardful.com/docs) | Affiliate tracking for Stripe/Paddle SaaS | 🟡 API Key | ✅ | ✅ |

---

## 🥽 Augmented Reality & AR Cloud APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Google ARCore API](https://developers.google.com/ar/reference) | Cross-platform AR SDK for Android, iOS, Unity | 🟡 API Key | ✅ | ✅ |
| [Niantic Lightship SDK](https://lightship.dev/docs/) | Advanced AR with VPS, meshing and segmentation | 🟡 API Key | ✅ | ✅ |
| [8th Wall WebAR](https://www.8thwall.com/docs/) | WebAR platform for browser-based AR | 🟡 API Key | ✅ | ✅ |
| [Vuforia Engine Web API](https://developer.vuforia.com/library/web-api/vuforia-web-services-api) | Enterprise AR with image/object recognition | 🟡 API Key | ✅ | ✅⭐ |
| [AR.js](https://ar-js-org.github.io/AR.js-Docs/) | Open-source web-based AR with JavaScript | 🟢 No | ✅ | ✅ |
| [Google Geospatial API](https://developers.google.com/ar/develop) | ARCore Geospatial for global-scale AR anchoring | 🟡 API Key | ✅ | ✅ |
| [FASHN Virtual Try-On API](https://docs.fashn.ai/) | AI fashion virtual try-on image generation | 🟡 API Key | ✅ | ✅⭐ |
| [Google Vertex AI Virtual Try-On](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/virtual-try-on-api) | Google Cloud AI-based virtual clothing try-on | 🟡 API Key | ✅ | ✅⭐ |

---

## 💾 Backup & Disaster Recovery APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [AWS Backup API](https://docs.aws.amazon.com/aws-backup/) | Centralized backup management across AWS services | 🟡 API Key | ✅ | ✅⭐ |
| [Azure Backup REST API](https://learn.microsoft.com/en-us/rest/api/backup/) | Programmatic backup and restore for Azure | 🔴 OAuth | ✅ | ✅⭐ |
| [Google Cloud Backup & DR API](https://cloud.google.com/backup-disaster-recovery/docs/reference/rest) | Managed backup and DR for Google Cloud | 🔴 OAuth | ✅ | ✅⭐ |
| [Veeam Backup REST API](https://helpcenter.veeam.com/docs/backup/vbr_rest/overview.html) | Veeam Backup & Replication management | 🟡 API Key | ✅ | ✅⭐ |
| [Backblaze B2 API](https://www.backblaze.com/apidocs/introduction-to-the-b2-native-api) | Cloud storage native and S3-compatible API | 🟡 API Key | ✅ | ✅⭐ |
| [Acronis Cyber Protect API](https://developer.acronis.com/doc/) | REST API for cyber protection and backup | 🟡 API Key | ✅ | ✅ |
| [Rubrik CDM API](https://github.com/rubrikinc/api-documentation) | Cloud Data Management cluster operations | 🟡 API Key | ✅ | ✅ |
| [Cohesity DataProtect API](https://developer.cohesity.com/) | Data protection and management workflows | 🟡 API Key | ✅ | ✅ |
| [Druva Cloud Platform API](https://developer.druva.com/) | Cloud-native data protection and governance | 🟡 API Key | ✅ | ✅ |
| [Commvault REST API](https://documentation.commvault.com/v11/essential/rest_api_overview.html) | Enterprise data management and backup automation | 🟡 API Key | ✅ | ✅ |
| [Wasabi Cloud Storage API](https://docs.wasabi.com/docs/rest-api-introduction) | S3-compatible hot cloud storage for backups | 🟡 API Key | ✅ | ✅⭐ |

---

## 🌐 Browser Extension & Web Automation APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Browserless API](https://www.browserless.io/) | Headless Chrome browser-as-a-service | 🟡 API Key | ✅ | ✅⭐ |
| [ScrapingBee API](https://www.scrapingbee.com/documentation/) | Web scraping with proxies and JS rendering | 🟡 API Key | ✅ | ✅⭐ |
| [Apify API](https://docs.apify.com/) | Cloud platform for web scraping and automation | 🟡 API Key | ✅ | ✅⭐ |
| [PhantomBuster API](https://hub.phantombuster.com/docs/developer-quick-start) | Cloud automation for lead generation and scraping | 🟡 API Key | ✅ | ✅ |
| [ZenRows API](https://www.zenrows.com/documentation) | Web scraping with anti-bot bypass | 🟡 API Key | ✅ | ✅⭐ |
| [Steel Browser API](https://github.com/steel-dev/steel-browser) | Open-source browser sandbox for AI agents | 🟡 API Key | ✅ | ✅ |
| [BrowserStack Automate API](https://www.browserstack.com/docs/automate/api-reference/selenium/introduction) | Cross-browser testing automation | 🟡 API Key | ✅ | ✅ |
| [Crawlee](https://crawlee.dev/docs/introduction) | Open-source web scraping framework by Apify | 🟢 No | ✅ | ✅ |

---

## 💰 Cloud Cost Management & FinOps APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [AWS Cost Explorer API](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-api.html) | AWS cost and usage data with filtering | 🟡 API Key | ✅ | ✅⭐ |
| [Azure Cost Management API](https://learn.microsoft.com/en-us/rest/api/cost-management/) | Azure cost/usage data and budgets | 🔴 OAuth | ✅ | ✅⭐ |
| [GCP Cloud Billing API](https://docs.cloud.google.com/billing/docs/reference/rest) | Google Cloud billing account info and pricing | 🔴 OAuth | ✅ | ✅⭐ |
| [Infracost Cloud Pricing API](https://www.infracost.io/docs/) | Free GraphQL API with 3M+ cloud prices | 🟡 API Key | ✅ | ✅⭐ |
| [Kubecost API](https://docs.kubecost.com/apis/monitoring-apis/cloud-cost-api) | Kubernetes cost allocation and monitoring | 🟡 API Key | ✅ | ✅ |
| [Vantage API](https://vantage.sh/docs) | Multi-cloud cost visibility and FinOps | 🟡 API Key | ✅ | ✅ |
| [OpenCost API](https://www.opencost.io/docs/) | Open-source CNCF Kubernetes cost monitoring | 🟢 No | ✅ | ✅ |
| [CloudHealth API](https://apidocs.vmware.com/cloudhealth-platform/index.html) | Multi-cloud cost management and governance | 🟡 API Key | ✅ | ✅ |

---

## 🎁 Crowdfunding & Fundraising APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [GoFundMe Pro API](https://developers.gofundme.com/) | Fundraising campaign management via REST | 🔴 OAuth | ✅ | ✅ |
| [Patreon API](https://docs.patreon.com/) | Creator campaigns, pledges and patron data | 🔴 OAuth | ✅ | ✅ |
| [JustGiving API](https://developer.justgiving.com/) | Fundraising pages, donations and charity search | 🟡 API Key | ✅ | ✅⭐ |
| [Raisely API](https://www.raisely.com/developers) | Custom fundraising features for charities | 🟡 API Key | ✅ | ✅ |
| [Blackbaud SKY Fundraising API](https://developer.blackbaud.com/skyapi/products/renxt/fundraising) | Enterprise nonprofit fundraising management | 🔴 OAuth | ✅ | ✅ |
| [Fundraise Up API](https://fundraiseup.com/docs/develop/) | Nonprofit donation platform and CRM | 🟡 API Key | ✅ | ✅ |
| [Candid Grants API](https://developer.candid.org/) | Grants, funders and nonprofit recipients search | 🟡 API Key | ✅ | ✅⭐ |

---

## 💱 Cryptocurrency Exchange APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Binance Spot API](https://developers.binance.com/docs/binance-spot-api-docs/rest-api) | Full spot trading with order management | 🟡 API Key | ✅ | ✅⭐ |
| [Coinbase Exchange API](https://docs.cdp.coinbase.com/exchange/introduction/welcome) | REST and WebSocket for trading and market data | 🟡 API Key | ✅ | ✅⭐ |
| [Kraken REST API](https://docs.kraken.com/api/) | Spot and futures trading with advanced orders | 🟡 API Key | ✅ | ✅⭐ |
| [OKX API v5](https://www.okx.com/docs-v5/en/) | Unified trading API across spot, futures, options | 🟡 API Key | ✅ | ✅⭐ |
| [Bybit API](https://bybit-exchange.github.io/docs/) | Spot and derivatives trading REST/WebSocket | 🟡 API Key | ✅ | ✅⭐ |
| [Gate.io API v4](https://www.gate.io/docs/developers/apiv4/) | Spot and futures trading with 1700+ pairs | 🟡 API Key | ✅ | ✅ |
| [KuCoin API](https://docs.kucoin.com/) | Spot and margin trading with sandbox | 🟡 API Key | ✅ | ✅ |
| [CCXT Library](https://docs.ccxt.com/) | Unified open-source API for 100+ exchanges | 🟢 No | ✅ | ✅⭐ |
| [CoinAPI](https://www.coinapi.io/) | Aggregated market data from 400+ exchanges | 🟡 API Key | ✅ | ✅⭐ |

---

## 🎭 Data Anonymization & Synthetic Data APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Gretel.ai API](https://docs.gretel.ai/) | Synthetic data generation and privacy engineering | 🟡 API Key | ✅ | ✅⭐ |
| [MOSTLY AI API](https://api-docs.mostly.ai/) | Generative AI for tabular and text synthetic data | 🟡 API Key | ✅ | ✅ |
| [Tonic.ai API](https://docs.tonic.ai/app/api/api-documentation) | Synthetic data platform for realistic test data | 🟡 API Key | ✅ | ✅ |
| [ARX Anonymization API](https://arx.deidentifier.org/development/api/) | Open-source k-anonymity and l-diversity | 🟢 No | ✅ | ✅ |
| [Neosync](https://www.neosync.dev/) | Open-source data anonymization for developers | 🟡 API Key | ✅ | ✅ |
| [YData Synthesizers](https://docs.synthetic.ydata.ai/) | Synthetic data generation with privacy guarantees | 🟡 API Key | ✅ | ✅ |
| [DataCebo SDV](https://docs.sdv.dev/) | Open-source Synthetic Data Vault for tabular data | 🟢 No | ✅ | ✅ |

---

## 🛡️ DevSecOps & Security Scanning APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Snyk REST API](https://apidocs.snyk.io/) | SCA, container, IaC and code scanning | 🟡 API Key | ✅ | ✅⭐ |
| [SonarQube Web API](https://docs.sonarsource.com/sonarqube-server/latest/extension-guide/web-api/) | Code quality and security analysis for 30+ languages | 🟡 API Key | ✅ | ✅⭐ |
| [Semgrep API](https://semgrep.dev/api/v1/docs/) | SAST and SCA findings via OpenAPI endpoints | 🟡 API Key | ✅ | ✅ |
| [OWASP ZAP API](https://www.zaproxy.org/docs/api/) | Open-source DAST for automated pen testing | 🟢 No | ✅ | ✅⭐ |
| [GitGuardian API](https://api.gitguardian.com/docs) | Secrets detection and incident management | 🟡 API Key | ✅ | ✅ |
| [Veracode Scan API](https://docs.veracode.com/r/Scan_APIs) | SAST, DAST and SCA scanning | 🟡 API Key | ✅ | ✅ |
| [GitHub Code Scanning API](https://docs.github.com/en/rest/code-scanning) | Code scanning alerts via GitHub REST API | 🔴 OAuth | ✅ | ✅⭐ |
| [AWS Security Hub API](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) | Aggregate security findings across AWS | 🟡 API Key | ✅ | ✅⭐ |
| [Escape.tech API](https://escape.tech/) | API-first DAST for GraphQL and REST | 🟡 API Key | ✅ | ✅ |

---

## ⚡ Electric Vehicle Charging APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Open Charge Map API](https://openchargemap.org/site/develop/api) | Global public registry of EV charging locations | 🟡 API Key | ✅ | ✅⭐ |
| [NREL Alt Fuel Stations API](https://developer.nrel.gov/docs/transportation/alt-fuel-stations-v1/) | US EV and alternative fuel station data | 🟡 API Key | ✅ | ✅⭐ |
| [TomTom EV Charging API](https://developer.tomtom.com/ev-charging-stations-availability-api/documentation/product-information/introduction) | Real-time EV charging station availability | 🟡 API Key | ✅ | ✅⭐ |
| [HERE EV Charge Points API](https://developer.here.com/documentation/charging-stations/dev_guide/topics/overview.html) | Global EV charging station search | 🟡 API Key | ✅ | ✅⭐ |
| [Enode EV API](https://developers.enode.com/) | Connect and control 45+ EV brands | 🟡 API Key | ✅ | ✅⭐ |
| [Smartcar EV API](https://smartcar.com/docs/) | Standardized EV integrations for battery and charging | 🔴 OAuth | ✅ | ✅⭐ |
| [PlugShare API](https://developer.plugshare.com/) | EV charging station data with community reviews | 🟡 API Key | ✅ | ✅ |
| [Google Places EV Charging](https://developers.google.com/maps/documentation/places/web-service/ev-charging) | EV charging via Google Places API | 🟡 API Key | ✅ | ✅⭐ |
| [OCPI Protocol](https://github.com/ocpi/ocpi) | Open Charge Point Interface standard | 🟢 No | ✅ | ✅ |

---

## 🎁 Employee Benefits & Perks APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Finch Unified API](https://developer.tryfinch.com/) | Single API for HR, payroll and benefits from 200+ providers | 🟡 API Key | ✅ | ✅⭐ |
| [Gusto API](https://docs.gusto.com/) | Payroll, benefits and HR management | 🔴 OAuth | ✅ | ✅⭐ |
| [Rippling API](https://developer.rippling.com/) | Unified HR, payroll and benefits platform | 🟡 API Key | ✅ | ✅ |
| [Deel API](https://developer.deel.com/) | Global payroll, contractor and benefits | 🟡 API Key | ✅ | ✅ |
| [PlanSource API](https://developer.plansource.com/docs/plansource-administrative-api) | Benefits administration for enrollment | 🟡 API Key | ✅ | ✅ |
| [Noyo Benefits API](https://docs.noyo.com/) | Group benefits connecting to carriers | 🟡 API Key | ✅ | ✅ |
| [Merge HRIS API](https://www.merge.dev/integrations) | Single API for 60+ HRIS and payroll integrations | 🟡 API Key | ✅ | ✅⭐ |

---

## 🔎 Enterprise Search APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Elasticsearch API](https://www.elastic.co/docs/api/doc/elasticsearch/) | Distributed search and analytics engine | 🟡 API Key | ✅ | ✅⭐ |
| [Algolia Search API](https://www.algolia.com/doc/rest-api/search) | Hosted search with typo tolerance and AI | 🟡 API Key | ✅ | ✅⭐ |
| [Typesense API](https://typesense.org/docs/) | Open-source typo-tolerant search engine | 🟡 API Key | ✅ | ✅⭐ |
| [Meilisearch API](https://www.meilisearch.com/docs) | Open-source instant search engine (Rust) | 🟡 API Key | ✅ | ✅⭐ |
| [Pinecone API](https://docs.pinecone.io/) | Vector database for semantic search | 🟡 API Key | ✅ | ✅⭐ |
| [Weaviate API](https://weaviate.io/developers/weaviate) | Open-source vector database with hybrid search | 🟡 API Key | ✅ | ✅⭐ |
| [Coveo Search API](https://docs.coveo.com/en/52/) | AI-powered enterprise search | 🟡 API Key | ✅ | ✅ |
| [Apache Solr API](https://solr.apache.org/guide/solr/latest/) | Open-source enterprise search platform | 🟢 No | ✅ | ✅ |
| [Qdrant API](https://qdrant.tech/documentation/) | Open-source vector similarity search | 🟡 API Key | ✅ | ✅⭐ |

---

## 🏢 Facility Management & Workplace APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Robin API](https://docs.robinpowered.com/) | Workspace management for spaces and desks | 🟡 API Key | ✅ | ✅ |
| [Envoy API](https://developers.envoy.com/) | Visitor management and desk booking | 🔴 OAuth | ✅ | ✅ |
| [OfficeRnD API](https://www.officernd.com/developers/) | Flex space and coworking management | 🟡 API Key | ✅ | ✅ |
| [Nexudus API](https://nexudus.com/api-first-coworking-platform/) | API-first coworking platform | 🟡 API Key | ✅ | ✅ |
| [FMX API](https://help.gofmx.com/hc/en-us/categories/21441716408717-API-Integrations) | Facilities maintenance work orders and assets | 🟡 API Key | ✅ | ✅ |
| [Microsoft Graph Places API](https://learn.microsoft.com/en-us/graph/api/resources/place) | Rooms, workspaces and floor plans in M365 | 🔴 OAuth | ✅ | ✅⭐ |

---

## 👗 Fashion & Apparel APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [FASHN API](https://docs.fashn.ai/) | AI virtual try-on and fashion image generation | 🟡 API Key | ✅ | ✅⭐ |
| [Lykdat API](https://apidocs.lykdat.com/) | Fashion image search and visual similarity | 🟡 API Key | ✅ | ✅⭐ |
| [Google Shopping Content API](https://developers.google.com/shopping-content) | Product listings and fashion product data | 🔴 OAuth | ✅ | ✅⭐ |
| [Fashion Cloud API](https://fashioncloudv2.docs.apiary.io/) | B2B fashion content exchange platform | 🟡 API Key | ✅ | ✅ |
| [ShopStyle API](https://www.shopstylecollective.com/) | Fashion product aggregation and affiliate | 🟡 API Key | ✅ | ✅ |
| [The New Black AI Fashion](https://thenewblack.ai/) | AI-powered clothing design | 🟡 API Key | ✅ | ✅ |

---

## 🎫 Gift Card & Voucher APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Tremendous API](https://www.tremendous.com/gift-card-api/) | 2000+ digital reward options globally | 🟡 API Key | ✅ | ✅⭐ |
| [Tango RaaS API](https://developers.tangocard.com/) | Rewards as a Service for gift card delivery | 🟡 API Key | ✅ | ✅⭐ |
| [Reloadly Gift Card API](https://www.reloadly.com/products/gift-card-api/) | Bulk gift cards to 1000+ brands in 160+ countries | 🟡 API Key | ✅ | ✅⭐ |
| [Giftbit API](https://www.giftbit.com/gift-card-api) | Digital gift card delivery with sandbox | 🟡 API Key | ✅ | ✅⭐ |
| [Amazon Incentives API](https://developer.amazon.com/incentives-api) | Distribute Amazon Gift Codes programmatically | 🟡 API Key | ✅ | ✅ |
| [Square Gift Cards API](https://developer.squareup.com/docs/gift-cards/using-gift-cards-api) | Gift cards within the Square ecosystem | 🔴 OAuth | ✅ | ✅⭐ |
| [Voucherify API](https://docs.voucherify.io/docs) | Coupons, gift cards, loyalty and referrals engine | 🟡 API Key | ✅ | ✅⭐ |

---

## 🏛️ Government Grant & Funding APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Grants.gov REST API](https://www.grants.gov/api/) | All US federal grant opportunities | 🟢 No | ✅ | ✅⭐ |
| [USAspending API](https://api.usaspending.gov/) | Comprehensive US government spending data | 🟢 No | ✅ | ✅⭐ |
| [NIH Reporter API](https://api.reporter.nih.gov/) | NIH funded research projects and grants | 🟢 No | ✅ | ✅⭐ |
| [NSF Awards API](https://www.nsf.gov/developer/) | National Science Foundation award data | 🟢 No | ✅ | ✅⭐ |
| [EU Funding & Tenders API](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/support/apis) | European Commission funding opportunities | 🟡 API Key | ✅ | ✅ |
| [SAM.gov Entity API](https://sam.gov/data-services) | Award Management entity registrations | 🟡 API Key | ✅ | ✅ |
| [Federal Audit Clearinghouse API](https://api.fac.gov/) | Single audit data for federal awards | 🟢 No | ✅ | ✅ |

---

## 🏥 Healthcare Claims & Billing APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [CMS BCDA](https://bcda.cms.gov/api-documentation.html) | Beneficiary Claims Data API for Medicare Part A/B/D claims via Bulk FHIR | 🟡 API Key | ✅ | ✅ |
| [Stedi Healthcare](https://www.stedi.com/docs/healthcare) | API-first clearinghouse for 837P/837I claims, 270/271 eligibility in JSON and X12 | 🟡 API Key | ✅ | ✅⭐ |
| [Availity](https://developer.availity.com/) | Multi-payer 270/271 eligibility, 276/277 claims status, and 278 prior-auth REST APIs | 🟡 API Key | ✅ | ✅ |
| [Eligible](https://eligible.com/documentation) | Insurance billing APIs for real-time eligibility, claims, and payment integration | 🟡 API Key | ✅ | ✅ |
| [Flexpa](https://www.flexpa.com/) | Patient-consented claims and clinical data from insurers via FHIR and SMART Health Links | 🔴 OAuth | ✅ | ✅⭐ |
| [Optum Eligibility](https://developer.optum.com/) | X12 270/271 eligibility and 276/277 claim status APIs with JSON wrapping | 🟡 API Key | ✅ | ✅ |
| [pVerify](https://pverify.com/api-developers/) | 50+ real-time eligibility endpoints; RESTful, X12, FHIR, HL7, and SOAP support | 🔴 OAuth | ✅ | ✅ |
| [Change Healthcare](https://developers.changehealthcare.com/) | Claims submission, eligibility, prior authorization, and ERA via X12 and REST | 🔴 OAuth | ✅ | ✅ |
| [Redox](https://docs.redoxengine.com/) | Healthcare data integration engine supporting FHIR, HL7v2, and X12 transactions | 🟡 API Key | ✅ | ✅ |
| [openFDA](https://open.fda.gov/apis/) | FDA drug labeling, adverse events, food enforcement, and device recall data | 🟢 No | ✅ | ✅⭐ |
| [Claim.MD](https://docs.claim.md/) | Clearinghouse API for 837P/837I claims, eligibility, and ERA in JSON/XML/X12 | 🟡 API Key | ✅ | ✅ |
| [CMS Developer Tools](https://developer.cms.gov/) | Blue Button 2.0, DPC, BCDA, and Marketplace APIs for Medicare and Medicaid data | 🔴 OAuth | ✅ | ✅ |
| [DocuSign eSignature](https://developers.docusign.com/docs/esign-rest-api/) | Electronic signature and healthcare document workflow automation REST API | 🔴 OAuth | ✅ | ✅⭐ |

---

## 🔐 Identity Access Management (IAM) APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Okta](https://developer.okta.com/docs/reference/core-okta-api/) | Enterprise SSO, MFA, user lifecycle, and org management APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Auth0](https://auth0.com/docs/api/management/v2) | Developer-focused authentication and authorization Management and Auth APIs | 🔴 OAuth | ✅ | ✅⭐ |
| [Keycloak](https://www.keycloak.org/docs-api/latest/rest-api/index.html) | Open-source IAM Admin REST API for realms, users, clients, roles, and groups | 🔴 OAuth | ✅ | ✅ |
| [FusionAuth](https://fusionauth.io/docs/apis/) | API-first CIAM with 100+ endpoints for auth, users, tenants, and themes | 🟡 API Key | ✅ | ✅⭐ |
| [Stytch](https://stytch.com/docs/api) | Magic links, OTP, OAuth, passwords, sessions, and biometrics REST API | 🟡 API Key | ✅ | ✅⭐ |
| [AWS IAM](https://docs.aws.amazon.com/IAM/latest/APIReference/welcome.html) | Create and manage users, roles, policies, and permissions for AWS resources | 🟡 API Key | ✅ | ✅ |
| [Google Cloud IAM](https://cloud.google.com/iam/docs/reference/rest/) | Manage roles, permissions, and service accounts for Google Cloud via REST | 🔴 OAuth | ✅ | ✅ |
| [Microsoft Entra ID](https://learn.microsoft.com/en-us/graph/api/resources/identity-overview) | Azure AD identity management via Microsoft Graph for users, groups, and apps | 🔴 OAuth | ✅ | ✅ |
| [JumpCloud](https://docs.jumpcloud.com/) | Cloud directory platform with v1/v2 REST APIs for users, groups, and policies | 🟡 API Key | ✅ | ✅ |
| [Ping Identity](https://developer.pingidentity.com/) | PingOne, PingID, and Advanced Identity Cloud enterprise authentication APIs | 🟡 API Key | ✅ | ✅ |
| [OneLogin](https://developers.onelogin.com/) | Unified access management with user, app, and API authorization management | 🟡 API Key | ✅ | ✅ |
| [IBM Cloud IAM](https://cloud.ibm.com/apidocs/iam-identity-token-api) | Manage service IDs, API keys, trusted profiles, and access tokens on IBM Cloud | 🟡 API Key | ✅ | ✅ |
| [Akamai IAM](https://techdocs.akamai.com/iam-api/reference/api) | Manage users and access to Akamai Control Center applications and resources | 🟡 API Key | ✅ | ✅ |
| [Twilio IAM](https://www.twilio.com/docs/iam) | Account management, API key authentication, and access control for Twilio services | 🟡 API Key | ✅ | ✅ |

---

## 📸 Influencer & Creator Economy APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Phyllo](https://docs.getphyllo.com/) | Universal RESTful API for creator data: engagement, audience, earnings across platforms | 🟡 API Key | ✅ | ✅⭐ |
| [CreatorDB](https://www.creatordb.app/api-services/) | RESTful OpenAPI-spec influencer data across YouTube, Instagram, TikTok, Facebook | 🟡 API Key | ✅ | ✅⭐ |
| [Modash](https://www.modash.io/influencer-marketing-api) | Discovery and analytics for 350M+ influencers on Instagram, TikTok, YouTube | 🟡 API Key | ✅ | ✅ |
| [HypeAuditor](https://hypeauditor.com/api-integration/) | Influencer discovery, audience quality analytics, and fraud detection API | 🟡 API Key | ✅ | ✅ |
| [Upfluence](https://www.upfluence.com/influencer-marketing-api) | Influencer metrics and audience demographics from Instagram, TikTok, YouTube | 🟡 API Key | ✅ | ✅ |
| [GRIN](https://grin.co/) | E-commerce influencer marketing with revenue attribution and UGC management | 🟡 API Key | ✅ | ⚠️ |
| [Aspire](https://www.aspire.io/) | Influencer discovery, campaign management, and product seeding automation | 🟡 API Key | ✅ | ⚠️ |
| [Traackr](https://www.traackr.com/) | Enterprise influencer management with audience vetting, fraud detection, analytics | 🟡 API Key | ✅ | ⚠️ |
| [Klear (Meltwater)](https://www.meltwater.com/en/klear) | Multi-platform influencer analytics connected to Meltwater media monitoring | 🟡 API Key | ✅ | ⚠️ |
| [Strava](https://developers.strava.com/docs/reference/) | Fitness and creator data API for athletes, activities, segments, routes, clubs | 🔴 OAuth | ✅ | ✅⭐ |
| [Fanatics Sports Data](https://www.sportsfirst.net/sportsapi/fanatics-sports-data-api) | Sports creator and fan merchandise API for licensed product integration | 🟡 API Key | ✅ | ✅ |
| [Wobb](https://wobb.ai/influencer-api) | Influencer marketing API with 400M+ creators, UGC data, and audience insights | 🟡 API Key | ✅ | ✅ |

---

## 🌍 Climate Risk & ESG Scoring APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Sustainalytics](https://www.sustainalytics.com/api-data-feeds) | ESG risk ratings and data feeds for 13,000+ companies via OpenAPI/Swagger | 🟡 API Key | ✅ | ✅ |
| [MSCI ESG Ratings](https://www.msci.com/our-solutions/esg-investing/esg-ratings-climate-search-tool) | ESG ratings and climate search tools for investment-grade ESG analysis | 🟡 API Key | ✅ | ⚠️ |
| [S&P Global ESG Scores](https://www.spglobal.com/sustainable1/en/solutions/esg-scores-data) | Comprehensive ESG scores, Trucost environmental data, and raw emissions data | 🟡 API Key | ✅ | ⚠️ |
| [AlphaGeo Climate Risk](https://docs.alphageo.ai/products/climate-risk-and-resilience-index) | Climate risk scoring at 30m resolution for TCFD, ISSB, EU Taxonomy compliance | 🟡 API Key | ✅ | ✅ |
| [Moody's ESG](https://www.economy.com/products/esg) | ESG and climate risk analytics from Moody's Analytics for financial institutions | 🟡 API Key | ✅ | ⚠️ |
| [FactSet ESG](https://developer.factset.com/) | ESG data access and analysis from multiple sources via FactSet developer platform | 🟡 API Key | ✅ | ✅ |
| [Refinitiv / LSEG](https://developers.lseg.com/) | ESG data on 13,000+ listed companies covering environmental, social, governance | 🟡 API Key | ✅ | ✅ |
| [ISS ESG](https://www.issgovernance.com/) | Corporate governance, responsible investment, and ESG ratings data | 🟡 API Key | ✅ | ⚠️ |
| [ESG Enterprise](https://www.esgenterprise.com/) | Real-time ESG risk analytics for 250,000+ companies and 750,000+ suppliers | 🟡 API Key | ✅ | ✅ |
| [Climate TRACE](https://climatetrace.org/) | Independent global inventory of greenhouse gas emissions with open data access | 🟢 No | ✅ | ✅⭐ |
| [CDP](https://www.cdp.net/) | Global disclosure system for carbon, water, and deforestation data | 🟡 API Key | ✅ | ⚠️ |
| [OpenWeatherMap Air Pollution](https://openweathermap.org/api/air-pollution) | Air quality and pollution data with current, forecast, and historical endpoints | 🟡 API Key | ✅ | ✅⭐ |
| [Bloomberg ESG](https://www.bloomberg.com/professional/products/data/enterprise/) | ESG and emissions data for public companies via Bloomberg Terminal and data feeds | 🟡 API Key | ✅ | ⚠️ |

---

## 💬 Community & Forum Platform APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Discourse](https://docs.discourse.org/) | Full REST API for the open-source forum platform; topics, posts, users, categories | 🟡 API Key | ✅ | ✅⭐ |
| [Reddit](https://www.reddit.com/dev/api/) | Official Reddit API for subreddits, posts, comments, users, and moderation | 🔴 OAuth | ✅ | ✅ |
| [Discord](https://discord.com/developers/docs/intro) | Community server API for channels, messages, guilds, roles, and bot integration | 🔴 OAuth | ✅ | ✅⭐ |
| [Slack](https://api.slack.com/) | Workspace messaging with Web API, Events API, and real-time messaging support | 🔴 OAuth | ✅ | ✅⭐ |
| [Telegram Bot API](https://core.telegram.org/bots/api) | Bot platform for groups, channels, messages, inline queries, and payments | 🟡 API Key | ✅ | ✅⭐ |
| [Circle.so](https://api.circle.so/) | Community platform with Admin, Member, Auth, and Data APIs for spaces and posts | 🟡 API Key | ✅ | ✅ |
| [Bettermode](https://developers.bettermode.com/docs/graphql/schema/) | GraphQL API for community platform with webhooks and Liquid template engine | 🟡 API Key | ✅ | ✅ |
| [Forem](https://developers.forem.com/api) | Open-source community platform (powers DEV.to) with REST API for articles, users | 🟡 API Key | ✅ | ✅ |
| [Flarum](https://docs.flarum.org/) | Open-source forum with JSON:API-based REST API and Extension API | 🟡 API Key | ✅ | ✅ |
| [NodeBB](https://docs.nodebb.org/api/write/) | Real-time forum platform with read/write REST API and WebSocket support | 🟡 API Key | ✅ | ✅ |
| [Vanilla Forums](https://docs.vanillaforums.com/api/) | REST API for discussions, comments, users, and categories in Vanilla communities | 🟡 API Key | ✅ | ✅ |
| [Mighty Networks](https://www.mightynetworks.com/) | Community platform with Zapier integration and webhooks for automation | 🟡 API Key | ✅ | ⚠️ |

---

## 📊 Content Marketing & SEO Content APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Semrush](https://developer.semrush.com/api/) | SEO analytics API for keyword research, domain analytics, backlinks, position tracking | 🟡 API Key | ✅ | ✅ |
| [Ahrefs](https://ahrefs.com/api/documentation) | Backlink analysis, keyword data, and site explorer API for SEO research | 🟡 API Key | ✅ | ✅ |
| [Moz Links API](https://moz.com/help/links-api) | URL metrics, top pages, anchor text, and domain authority data via REST | 🟡 API Key | ✅ | ✅ |
| [DataForSEO](https://docs.dataforseo.com/v3/) | Comprehensive SEO data API covering SERP, keywords, backlinks, on-page, and more | 🟡 API Key | ✅ | ✅⭐ |
| [Google Search Console](https://developers.google.com/webmaster-tools) | Search analytics, URL inspection, indexing status, and sitemap management | 🔴 OAuth | ✅ | ✅ |
| [Google PageSpeed Insights](https://developers.google.com/speed/docs/insights/v5/get-started) | Page performance, Core Web Vitals, and Lighthouse audit data via REST v5 | 🟡 API Key | ✅ | ✅⭐ |
| [Copyscape](https://www.copyscape.com/api-guide.php) | Plagiarism detection and content originality checking API in JSON/XML/HTML | 🟡 API Key | ✅ | ✅ |
| [SE Ranking](https://seranking.com/) | Keyword rank tracker, competitor analysis, and site audit API | 🟡 API Key | ✅ | ✅ |
| [WordLift](https://wordlift.io/) | AI-powered structured data, content knowledge graph, and SEO automation API | 🟡 API Key | ✅ | ✅ |
| [BrightEdge](https://www.brightedge.com/) | Enterprise SEO platform REST API for rankings, social signals, and analytics | 🟡 API Key | ✅ | ⚠️ |
| [Surfer SEO](https://surferseo.com/) | Content optimization and SERP analysis with integration APIs | 🟡 API Key | ✅ | ⚠️ |
| [MarketMuse](https://www.marketmuse.com/) | AI content strategy and optimization platform with content scoring | 🟡 API Key | ✅ | ⚠️ |
| [Conductor](https://www.conductor.com/platform/capabilities/api-integrations/) | Enterprise SEO and content intelligence platform with API integrations | 🟡 API Key | ✅ | ⚠️ |

---

## 🏅 Credential & Digital Badge APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Credly](https://www.credly.com/docs/web_service_api) | Digital badge and certification platform with OAuth and token-based REST API | 🔴 OAuth | ✅ | ✅ |
| [Accredible](https://docs.api.accredible.com/) | Digital certificates and badges REST API for issuance, management, verification | 🟡 API Key | ✅ | ✅⭐ |
| [Badgr (Parchment)](https://badgr.com/) | Open Badges platform for issuing, managing, and verifying digital credentials | 🔴 OAuth | ✅ | ✅ |
| [BadgeCert](https://badgecert.com/api-integrations/) | RESTful APIs for creating, issuing, updating, and tracking digital badges | 🟡 API Key | ✅ | ✅ |
| [Sertifier](https://sertifier.docs.apiary.io/) | Digital badge and certificate creation, sending, and verification REST API | 🟡 API Key | ✅ | ✅ |
| [Certifier](https://certifier.io/features/api-and-integrations) | Digital credential management with bulk issuance, webhooks, and verification API | 🟡 API Key | ✅ | ✅ |
| [1EdTech Open Badges](https://www.imsglobal.org/spec/ob/v3p0) | Open standard (v3.0) specification for creating and verifying digital badges | 🟢 No | ✅ | ✅ |
| [Credential Engine](https://credentialengine.org/develop-solutions/apis/) | Registry API for publishing and searching credentials via CTDL and JSON-LD | 🟡 API Key | ✅ | ✅ |
| [Blockcerts](https://www.blockcerts.org/guide/) | Open standard for blockchain-based academic credentials; issuance and verification | 🟢 No | ✅ | ✅ |
| [Canvas Credentials](https://www.instructure.com/higher-education/products/canvas/canvas-credentials) | Instructure credential platform integrated with Canvas LMS | 🟡 API Key | ✅ | ✅ |
| [VerifyEd](https://www.verifyed.io/) | Blockchain-verified digital credentials with issuance and verification API | 🟡 API Key | ✅ | ✅ |
| [Digital Credentials Consortium](https://digitalcredentials.mit.edu/) | MIT-led open-source digital credentials infrastructure with Verifiable Credentials | 🟢 No | ✅ | ✅ |

---

## 📋 Customer Feedback & NPS APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [SurveyMonkey](https://api.surveymonkey.com/v3/docs) | Create surveys, collect responses, and analyze results via REST API v3 | 🔴 OAuth | ✅ | ✅⭐ |
| [Typeform](https://www.typeform.com/developers/) | Create interactive forms/surveys and retrieve responses; REST API with webhooks | 🔴 OAuth | ✅ | ✅⭐ |
| [Delighted](https://app.delighted.com/docs/api) | Simple NPS, CSAT, CES survey API with people, responses, metrics, and webhooks | 🟡 API Key | ✅ | ✅⭐ |
| [Qualtrics](https://api.qualtrics.com/) | Enterprise experience management with survey, distribution, and response APIs | 🟡 API Key | ✅ | ✅ |
| [Medallia](https://developer.medallia.com/) | Enterprise CX platform with feedback collection and analytics APIs | 🟡 API Key | ✅ | ✅ |
| [Survicate](https://developers.survicate.com/) | In-app and website surveys with JavaScript SDK, mobile SDK, and Data Export API | 🟡 API Key | ✅ | ✅ |
| [Wootric (InMoment)](https://docs.wootric.com/api/) | In-app NPS, CSAT, CES micro-surveys with REST API and multi-region support | 🟡 API Key | ✅ | ✅ |
| [UserVoice](https://developer.uservoice.com/) | Customer feedback and product management with idea voting and survey APIs | 🟡 API Key | ✅ | ✅ |
| [Nicereply](https://www.nicereply.com/) | CSAT, NPS, and CES surveys embedded in helpdesk workflows with API access | 🟡 API Key | ✅ | ✅ |
| [Hotjar](https://www.hotjar.com/) | Behavior analytics and feedback tools with heatmaps, recordings, and surveys | 🟡 API Key | ✅ | ⚠️ |
| [Refiner](https://refiner.io/) | In-product microsurveys for SaaS with NPS, CSAT, CES, and custom survey API | 🟡 API Key | ✅ | ✅ |
| [AskNicely](https://www.asknicely.com/integrations) | NPS-focused feedback platform with API, Salesforce, Slack, and CRM integrations | 🟡 API Key | ✅ | ✅ |
| [GetFeedback](https://www.getfeedback.com/) | Salesforce-native customer feedback and survey platform with REST API | 🟡 API Key | ✅ | ⚠️ |

---

## 📁 Data Room & Virtual Due Diligence APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Box Platform](https://developer.box.com/reference) | 150+ REST endpoints for secure file management, collaboration, metadata, workflows | 🔴 OAuth | ✅ | ✅⭐ |
| [Google Drive API](https://developers.google.com/drive/api) | File storage, sharing, permissions, and collaboration via REST API | 🔴 OAuth | ✅ | ✅⭐ |
| [Dropbox Business API](https://www.dropbox.com/developers) | File operations, team management, sharing, and paper documents via REST API | 🔴 OAuth | ✅ | ✅⭐ |
| [Datasite](https://www.datasite.com/en/resources/datasite-apis) | M&A data room APIs for document management, user access, and deal workflows | 🟡 API Key | ✅ | ✅ |
| [SharePoint REST API](https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/get-to-know-the-sharepoint-rest-service) | Document libraries, lists, sites, and permissions management via REST/OData | 🔴 OAuth | ✅ | ✅ |
| [DocuSign Rooms](https://developers.docusign.com/docs/rooms-api/) | Virtual transaction rooms for real estate and M&A with room, task, document APIs | 🔴 OAuth | ✅ | ✅ |
| [Citrix ShareFile](https://api.sharefile.com/) | Secure file sharing and storage OData-based REST API for enterprise data rooms | 🔴 OAuth | ✅ | ✅ |
| [Intralinks](https://www.intralinks.com/) | SS&C Intralinks VDR for M&A deals with document and user management APIs | 🟡 API Key | ✅ | ⚠️ |
| [Ansarada](https://www.ansarada.com/) | AI-powered virtual data rooms with automated reporting and access management | 🟡 API Key | ✅ | ⚠️ |
| [Firmex](https://www.firmex.com/) | Virtual data room platform for M&A, compliance, and litigation with API access | 🟡 API Key | ✅ | ⚠️ |
| [iDeals](https://www.idealsvdr.com/) | Virtual data room for M&A with granular permissions and activity tracking | 🟡 API Key | ✅ | ⚠️ |
| [ShareVault](https://sharevault.com/) | Secure data room for M&A and due diligence with document management API | 🟡 API Key | ✅ | ⚠️ |

---

## 💰 Debt Collection & Recovery APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [TrueAccord Recover](https://docs.trueaccord.com/recover/recover-api-reference) | ML-powered debt collection REST API for uploading customers and tracking recovery | 🟡 API Key | ✅ | ✅⭐ |
| [Riverty Collection](https://docs.riverty.com/back_in_flow/getting_started/collection_api) | RESTful debt collection API with JSON, predictable URLs, and standard HTTP auth | 🟡 API Key | ✅ | ✅⭐ |
| [Debitura](https://www.debitura.com/integration/debt-collection-api) | Worldwide debt recovery API for managing, tracking, and automating collections | 🟡 API Key | ✅ | ✅ |
| [Tratta](https://docs.tratta.io/api.html) | Debt collection platform with REST APIs, sandbox, and secure integrations | 🟡 API Key | ✅ | ✅ |
| [Experian](https://developer.experian.com/) | Consumer and commercial credit data, skip tracing, and debt recovery APIs | 🔴 OAuth | ✅ | ✅ |
| [Creditsafe](https://doc.creditsafe.com/) | Global credit data, company information, and collections intelligence Connect API | 🟡 API Key | ✅ | ✅ |
| [Peach Finance](https://docs.peach.finance/) | API-first loan servicing and collections platform with Compliance Guard APIs | 🟡 API Key | ✅ | ✅ |
| [Tracers](https://www.tracers.com/api/collection-agency-api/) | Skip tracing and people search API for locating debtors and verifying identity | 🟡 API Key | ✅ | ✅ |
| [CollBox](https://www.collbox.co/) | Automated small business debt collection with accounting software integration | 🟡 API Key | ✅ | ⚠️ |
| [YayPay (Quadient)](https://www.quadient.com/en/ar-automation) | Accounts receivable automation and collections platform with API | 🟡 API Key | ✅ | ⚠️ |
| [Debtist](https://www.debtist.de/en/tech/inkasso-api/) | Debt collection REST API for partner integration and outstanding invoices | 🟡 API Key | ✅ | ✅ |
| [DebtRecuva](https://www.debtrecuva.com/api.html) | Debt recovery API with documented REST endpoints for automated collections | 🟡 API Key | ✅ | ✅ |

---

## 📄 Document Generation & Template APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [PandaDoc](https://developers.pandadoc.com/) | Document generation from templates, e-signatures, and workflow automation REST API | 🟡 API Key | ✅ | ✅⭐ |
| [Carbone.io](https://carbone.io/documentation/developer/http-api/introduction.html) | Template-based report generator from JSON to PDF, DOCX, XLSX; REST API and SDKs | 🟡 API Key | ✅ | ✅⭐ |
| [Anvil](https://www.useanvil.com/docs/api/generate-pdf/) | PDF filling, generation from HTML/CSS, and e-signature workflows via REST/GraphQL | 🟡 API Key | ✅ | ✅⭐ |
| [PDFMonkey](https://docs.pdfmonkey.io/references/api) | Dynamic PDF generation from HTML templates with data merge via REST API | 🟡 API Key | ✅ | ✅⭐ |
| [DocuSign eSignature](https://developers.docusign.com/docs/esign-rest-api/) | Document generation, template management, and electronic signature REST API | 🔴 OAuth | ✅ | ✅⭐ |
| [DocSpring](https://docspring.com/docs/) | PDF generation API from fillable templates with data merge and e-signatures | 🟡 API Key | ✅ | ✅ |
| [Docmosis](https://resources.docmosis.com/api-sdk/cloud-dws4-api) | Cloud REST API for merging data with templates to generate PDF/DOCX documents | 🟡 API Key | ✅ | ✅ |
| [Formstack Documents](https://www.webmerge.me/developers) | Document automation from templates (formerly WebMerge) with open REST API | 🟡 API Key | ✅ | ✅ |
| [Adobe PDF Services](https://developer.adobe.com/document-services/docs/overview/pdf-services-api/) | Create, convert, compress, OCR, and manipulate PDFs via Adobe cloud REST API | 🟡 API Key | ✅ | ✅ |
| [PSPDFKit (Nutrient)](https://pspdfkit.com/api/) | PDF processing, generation, editing, and conversion API | 🟡 API Key | ✅ | ✅ |
| [Apryse (PDFTron)](https://docs.apryse.com/) | PDF manipulation, generation, viewing, and annotation APIs for web and mobile | 🟡 API Key | ✅ | ✅ |
| [LaTeX.Online](https://latexonline.cc/) | Compile LaTeX documents to PDF via REST API calls | 🟢 No | ✅ | ✅ |

---

## 📚 E-Learning & LMS APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Canvas LMS](https://canvas.instructure.com/doc/api/) | Comprehensive REST API for courses, users, assignments, gradebooks, and modules | 🔴 OAuth | ✅ | ✅⭐ |
| [Moodle Web Services](https://docs.moodle.org/dev/Web_service_API_functions) | Open-source LMS with web service functions via REST, SOAP, and XML-RPC | 🟡 API Key | ✅ | ✅ |
| [Blackboard Learn](https://developer.blackboard.com/portal/displayApi/Learn) | Enterprise LMS REST API for courses, users, content, grades, and announcements | 🔴 OAuth | ✅ | ✅ |
| [Docebo](https://help.docebo.com/hc/en-us/sections/360005441800-APIs) | AI-powered enterprise LMS with REST API browser and comprehensive endpoints | 🔴 OAuth | ✅ | ✅ |
| [Thinkific](https://developers.thinkific.com/api/api-documentation) | Online course platform Admin API for courses, users, enrollments, and orders | 🟡 API Key | ✅ | ✅ |
| [TalentLMS](https://market.talentlms.com/pages/docs/TalentLMS-API-Documentation.pdf) | Cloud LMS REST API with 50+ endpoints for users, courses, groups, enrollments | 🟡 API Key | ✅ | ✅ |
| [Skilljar](https://api.skilljar.com/docs/) | Customer education LMS with REST API for domains, courses, users, and paths | 🟡 API Key | ✅ | ✅ |
| [LearnUpon](https://docs.learnupon.com/api/) | Corporate LMS API with Basic Auth over HTTPS for user and course management | 🟡 API Key | ✅ | ✅ |
| [Open edX](https://docs.openedx.org/projects/edx-platform/en/latest/references/lms_apis.html) | Open-source learning platform with REST APIs for courses, enrollments, grades | 🔴 OAuth | ✅ | ✅ |
| [Udemy Business](https://www.udemy.com/developers/) | Course catalog, user activity, and organization management API (Enterprise) | 🟡 API Key | ✅ | ✅ |
| [Teachable](https://docs.teachable.com/) | Online course platform API for courses, users, enrollments, and transactions | 🔴 OAuth | ✅ | ✅ |
| [Absorb LMS](https://absorblms.com/) | Enterprise LMS with REST API for administration, enrollment, and reporting | 🟡 API Key | ✅ | ✅ |
| [Coursera for Business](https://build.coursera.org/) | Enterprise learning platform with content catalog and enrollment APIs | 🟡 API Key | ✅ | ⚠️ |

---

## ⚽ Fan Engagement & Sports Tech APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Sportradar](https://developer.sportradar.com/) | Comprehensive sports data for NFL, NBA, MLB, NHL with live play-by-play and odds | 🟡 API Key | ✅ | ✅⭐ |
| [SportsDataIO](https://sportsdata.io/developers/apis) | Real-time scores, stats, odds, projections, and fantasy data for major sports | 🟡 API Key | ✅ | ✅⭐ |
| [Ticketmaster Discovery](https://developer.ticketmaster.com/products-and-docs/apis/discovery-api/v2/) | Event discovery API for live events, venues, artists, and attractions search | 🟡 API Key | ✅ | ✅⭐ |
| [API-Football](https://www.api-football.com/documentation) | Football/soccer data for 1,200+ competitions with livescore, standings, stats | 🟡 API Key | ✅ | ✅⭐ |
| [football-data.org](https://docs.football-data.org/general/v4/index.html) | Free RESTful football data API v4 with scores, fixtures, tables, and squads | 🟡 API Key | ✅ | ✅⭐ |
| [Strava](https://developers.strava.com/docs/reference/) | Fitness and athletic data for activities, segments, routes, and athlete profiles | 🔴 OAuth | ✅ | ✅⭐ |
| [TheSportsDB](https://www.thesportsdb.com/documentation) | Open crowdsourced sports data with teams, players, events, livescores, artwork | 🟡 API Key | ✅ | ✅ |
| [Fanatics Sports Data](https://www.sportsfirst.net/sportsapi/fanatics-sports-data-api) | Real-time scores, player stats, and team info across major sports leagues | 🟡 API Key | ✅ | ✅ |
| [Stats Perform / Opta](https://www.statsperform.com/) | Premium real-time sports data, analytics, and AI-driven insights via feeds | 🟡 API Key | ✅ | ⚠️ |
| [Genius Sports](https://www.geniussports.com/) | Official sports data and fan engagement platform for leagues and sportsbooks | 🟡 API Key | ✅ | ⚠️ |
| [iSportsAPI](https://www.isportsapi.com/) | Real-time sports data API for soccer, basketball, tennis, and cricket | 🟡 API Key | ✅ | ✅ |
| [ESPN (Unofficial)](https://gist.github.com/akeaswaran/b48b02f1c94f873c6655e7129910fc3b) | Hidden ESPN API endpoints for scores, standings, teams, and schedules | 🟢 No | ✅ | ⚠️ |

---

## 🍽️ Food Safety & Inspection APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [USDA FSIS Recall API](https://www.fsis.usda.gov/science-data/developer-resources/recall-api) | Food recall and public health alert data from USDA in JSON with attribute queries | 🟢 No | ✅ | ✅⭐ |
| [USDA FSIS MPI API](https://www.fsis.usda.gov/science-data/developer-resources/mpi-api) | Meat, poultry, and egg product inspection establishment data via REST | 🟢 No | ✅ | ✅⭐ |
| [openFDA Food API](https://open.fda.gov/apis/food/) | FDA food enforcement, recall, adverse event, and labeling data via REST | 🟡 API Key | ✅ | ✅⭐ |
| [USDA FoodData Central](https://fdc.nal.usda.gov/api-guide/) | Comprehensive food composition and nutrient data for 300K+ items via REST | 🟡 API Key | ✅ | ✅⭐ |
| [Open Food Facts](https://openfoodfacts.github.io/openfoodfacts-server/api/) | Open database of food products worldwide with ingredients, Nutri-Score, allergens | 🟢 No | ✅ | ✅⭐ |
| [Spoonacular](https://spoonacular.com/food-api) | Recipe search, nutrition analysis, meal planning, and ingredient data API | 🟡 API Key | ✅ | ✅⭐ |
| [Nutritionix](https://www.nutritionix.com/business/api) | Nutrition database with natural language queries and 1M+ restaurant items | 🟡 API Key | ✅ | ✅⭐ |
| [Edamam](https://developer.edamam.com/) | Food and nutrition data, recipe analysis, meal planner, and diet/health label APIs | 🟡 API Key | ✅ | ✅ |
| [CalorieNinjas](https://calorieninjas.com/api) | Natural language nutrition data API returning calories, macros, micronutrients | 🟡 API Key | ✅ | ✅⭐ |
| [FatSecret Platform](https://platform.fatsecret.com/platform-api) | Food and nutrition database API with barcode lookup and recipe analysis | 🔴 OAuth | ✅ | ✅ |
| [CPSC Recalls API](https://www.cpsc.gov/Recalls/CPSC-Recalls-Application-Program-Interface-API-Information) | Consumer Product Safety Commission recall data in XML/JSON via REST | 🟢 No | ✅ | ✅ |
| [SaferProducts.gov](https://www.saferproducts.gov/) | Consumer product safety incident reports and recall data via OData API | 🟢 No | ✅ | ✅ |

---

## 🏪 Franchise Management APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [FranConnect](https://docs.franconnect.net/) | Franchise lifecycle management API for finance, sales, CRM, and admin modules | 🟡 API Key | ✅ | ✅ |
| [ServiceTitan](https://developer.servicetitan.io/) | Field service management API for franchises with CRM, dispatch, and accounting | 🟡 API Key | ✅ | ✅⭐ |
| [Jobber](https://developer.getjobber.com/docs/) | Field service management with GraphQL API for clients, jobs, invoices | 🔴 OAuth | ✅ | ✅ |
| [Housecall Pro](https://docs.housecallpro.com/) | Home service franchise management with scheduling, dispatch, payment APIs | 🟡 API Key | ✅ | ✅ |
| [ServiceM8](https://developer.servicem8.com/) | Field service management REST API for jobs, clients, scheduling, invoicing | 🟡 API Key | ✅ | ✅ |
| [Salesforce](https://developer.salesforce.com/docs/apis) | Enterprise CRM for franchise management with REST, SOAP, and Bulk APIs | 🔴 OAuth | ✅ | ✅⭐ |
| [HubSpot](https://developers.hubspot.com/) | CRM and marketing platform for franchise lead management with REST API | 🔴 OAuth | ✅ | ✅⭐ |
| [Pipedrive](https://developers.pipedrive.com/docs/api/v1) | Sales CRM REST API for deals, contacts, organizations, pipeline management | 🟡 API Key | ✅ | ✅⭐ |
| [Monday.com](https://developer.monday.com/api-reference/) | Work management platform GraphQL API for franchise operations, project tracking | 🟡 API Key | ✅ | ✅ |
| [Zuper](https://www.zuper.co/) | Field service management for franchise operations with REST API integrations | 🟡 API Key | ✅ | ✅ |
| [Naranga](https://naranga.com/) | Franchise management platform with operations, training, and compliance tools | 🟡 API Key | ✅ | ⚠️ |
| [BrandWide](https://brandwide.com/) | All-in-one franchise management with desktop, mobile, and API integration | 🟡 API Key | ✅ | ⚠️ |
| [FranchiseSoft](https://franchisesoft.com/) | Franchise CRM and operations management software with API capabilities | 🟡 API Key | ✅ | ⚠️ |

---

## 🗺️ Geospatial Intelligence & GIS APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [ArcGIS REST API (Esri)](https://developers.arcgis.com/rest/) | Full GIS platform with geocoding, routing, spatial analysis, basemap services | 🟡 API Key | ✅ | ✅⭐ |
| [Mapbox](https://docs.mapbox.com/api/) | Maps, geocoding, navigation, and spatial analysis with vector tile rendering | 🟡 API Key | ✅ | ✅⭐ |
| [HERE Maps](https://developer.here.com/) | Geocoding, routing, traffic, fleet management, and map rendering REST APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Google Maps Platform](https://developers.google.com/maps) | Geocoding, directions, places, elevation, and Street View via REST and SDKs | 🟡 API Key | ✅ | ✅⭐ |
| [Google Earth Engine](https://developers.google.com/earth-engine) | Petabyte-scale geospatial analysis with Python/JS APIs and REST interface | 🔴 OAuth | ✅ | ✅ |
| [OpenStreetMap Nominatim](https://nominatim.org/release-docs/latest/api/Overview/) | Free geocoding (forward and reverse) using OpenStreetMap data | 🟢 No | ✅ | ✅⭐ |
| [Overpass API (OSM)](https://wiki.openstreetmap.org/wiki/Overpass_API) | Query OpenStreetMap data using Overpass QL for nodes, ways, and relations | 🟢 No | ✅ | ✅ |
| [Cesium ion](https://cesium.com/learn/ion/rest-api/) | 3D geospatial visualization with globe rendering, terrain, 3D Tiles REST API | 🟡 API Key | ✅ | ✅ |
| [GeoServer](https://docs.geoserver.org/stable/en/user/rest/) | Open-source geospatial server with WMS, WFS, WCS, and REST configuration API | 🟡 API Key | ✅ | ✅ |
| [Mapillary (Meta)](https://www.mapillary.com/developer/api-documentation) | Street-level imagery and map data for computer vision and geospatial apps | 🔴 OAuth | ✅ | ✅ |
| [QGIS API](https://api.qgis.org/api/) | Open-source GIS with Python (PyQGIS) and C++ APIs for spatial analysis | 🟢 No | ✅ | ✅ |
| [PostGIS](https://postgis.net/documentation/) | Spatial database extension for PostgreSQL with geographic functions and queries | 🟢 No | ✅ | ✅ |
| [OpenWeatherMap](https://openweathermap.org/api) | Weather and geospatial climate data API with geocoding and map tile layers | 🟡 API Key | ✅ | ✅⭐ |
| [Turf.js](https://turfjs.org/) | Open-source JavaScript library for client-side geospatial analysis | 🟢 No | ✅ | ✅⭐ |

---

## 🎫 Ticketing & Support Queue APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Zendesk API](https://developer.zendesk.com/api-reference/) | Full-featured helpdesk with tickets, users, orgs, SLAs, and automations | 🟡 API Key | ✅ | ✅⭐ |
| [Freshdesk API](https://developers.freshdesk.com/api/) | Helpdesk ticketing with contacts, groups, and SLA management | 🟡 API Key | ✅ | ✅⭐ |
| [Jira Service Management API](https://developer.atlassian.com/cloud/jira/service-desk/rest/) | ITSM ticketing with queues, request types, and approvals | 🔴 OAuth | ✅ | ✅ |
| [ServiceNow REST API](https://developer.servicenow.com/dev.do#!/reference/api/orlando/rest/c_TableAPI) | Enterprise ITSM with incident, problem, and change management | 🔴 OAuth | ✅ | ✅ |
| [Help Scout API](https://developer.helpscout.com/) | Customer support with mailboxes, conversations, and customer profiles | 🔴 OAuth | ✅ | ✅ |
| [Zoho Desk API](https://desk.zoho.com/DeskAPIDocument) | Helpdesk with tickets, contacts, accounts, and knowledge base | 🔴 OAuth | ✅ | ✅ |
| [HappyFox API](https://support.happyfox.com/kb/article/360-api-for-happyfox/) | RESTful helpdesk for creating tickets, listing users, and updates | 🟡 API Key | ✅ | ✅ |
| [osTicket API](https://docs.osticket.com/en/latest/Developer%20Documentation/API%20Docs.html) | Open-source helpdesk ticket creation and management | 🟡 API Key | ✅ | ⚠️ |
| [LiveAgent API](https://support.liveagent.com/840770-Complete-API-reference) | Multi-channel helpdesk with live chat, email, and phone ticketing | 🟡 API Key | ✅ | ✅ |
| [Freshservice API](https://api.freshservice.com/) | IT service management with assets, changes, and incident tracking | 🟡 API Key | ✅ | ✅ |
| [HubSpot Tickets API](https://developers.hubspot.com/docs/api/crm/tickets) | CRM-integrated support tickets with pipelines and associations | 🔴 OAuth | ✅ | ✅⭐ |
| [Intercom API](https://developers.intercom.com/docs/build-an-integration/learn-more/rest-apis/) | Conversational support with tickets, contacts, and messenger | 🔴 OAuth | ✅ | ✅ |

---

## 📦 Subscription Box & Commerce APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Cratejoy API](https://docs.cratejoy.com/) | Subscription box platform with orders, subscriptions, and shipments | 🟡 API Key | ✅ | ✅ |
| [Chargebee API](https://apidocs.chargebee.com/docs/api/) | Subscription billing with plans, invoices, and customer lifecycle | 🟡 API Key | ✅ | ✅⭐ |
| [Recurly API](https://recurly.com/developers/api/) | Recurring billing with subscriptions, plans, and dunning management | 🟡 API Key | ✅ | ✅⭐ |
| [Stripe Billing API](https://docs.stripe.com/api/subscriptions) | Subscription management with invoicing, metering, and pricing | 🟡 API Key | ✅ | ✅⭐ |
| [Recharge API](https://docs.getrecharge.com/) | Subscription commerce for Shopify with recurring orders and bundles | 🟡 API Key | ✅ | ✅ |
| [Ordergroove API](https://developer.ordergroove.com/) | Relationship commerce with subscription management and analytics | 🟡 API Key | ✅ | ✅ |
| [Shopify Subscriptions API](https://shopify.dev/docs/apps/build/purchase-options/subscriptions) | Native subscription contracts and billing within Shopify ecosystem | 🔴 OAuth | ✅ | ✅ |
| [WooCommerce Subscriptions API](https://woocommerce.github.io/subscriptions-rest-api-docs/) | WordPress-based recurring payments and subscription management | 🟡 API Key | ✅ | ✅ |
| [Bold Subscriptions API](https://support.boldcommerce.com/hc/en-us/articles/4403958620820-APIs-in-Subscriptions-for-Shopify-Checkout) | Shopify subscription app with checkout and order management | 🟡 API Key | ✅ | ⚠️ |
| [PayPal Subscriptions API](https://developer.paypal.com/docs/api/subscriptions/v1/) | Subscription plans and billing agreements via PayPal | 🔴 OAuth | ✅ | ✅ |
| [Paddle API](https://developer.paddle.com/api-reference/overview) | SaaS subscription billing with tax compliance and checkout | 🟡 API Key | ✅ | ✅ |
| [Subbly API](https://www.subbly.co/) | Subscription box platform for ecommerce with recurring orders | 🟡 API Key | ✅ | ⚠️ |

---

## 🎙️ Podcast Analytics & Monetization APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Spotify Web API (Podcasts)](https://developer.spotify.com/documentation/web-api) | Search, browse, and manage podcast shows and episodes | 🔴 OAuth | ✅ | ✅⭐ |
| [Podbean API](https://developers.podbean.com/podbean-api-docs/) | Podcast hosting with episode publishing, analytics, and monetization | 🔴 OAuth | ✅ | ✅ |
| [Buzzsprout API](https://github.com/buzzsprout/buzzsprout-api) | Podcast hosting with episode management and download statistics | 🟡 API Key | ✅ | ✅ |
| [Transistor.fm API](https://developers.transistor.fm/) | Podcast hosting with analytics, transcripts, and episode management | 🟡 API Key | ✅ | ✅ |
| [Simplecast API](https://apidocs.simplecast.com/) | Podcast management with analytics, distribution, and monetization | 🟡 API Key | ✅ | ✅ |
| [Libsyn API](https://status.libsyn.com/api) | Veteran podcast hosting with distribution and statistics | 🟡 API Key | ✅ | ⚠️ |
| [Spreaker API](https://developers.spreaker.com/api/) | Podcast creation, hosting, distribution, and monetization | 🔴 OAuth | ✅ | ✅ |
| [Apple Podcasts Connect API](https://developer.apple.com/documentation/applepodcastsconnectapi) | Apple Podcasts analytics and show management | 🔴 OAuth | ✅ | ⚠️ |
| [Chartable API](https://chartable.com/developers) | Podcast attribution analytics and SmartLinks | 🟡 API Key | ✅ | ✅ |
| [Podcast Index API](https://podcastindex-org.github.io/docs-api/) | Open podcast directory with search, episodes, and value4value | 🟡 API Key | ✅ | ✅⭐ |
| [Listen Notes API](https://www.listennotes.com/api/) | Podcast search engine with full-text search across episodes | 🟡 API Key | ✅ | ✅⭐ |
| [Audioboom API](https://api.audioboom.com/) | Podcast hosting and distribution with monetization features | 🔴 OAuth | ✅ | ✅ |

---

## 🔑 Password & Credential Management APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [1Password Connect API](https://developer.1password.com/docs/connect/api-reference/) | Access vault items and secrets via private REST API server | 🟡 API Key | ✅ | ✅⭐ |
| [Bitwarden API](https://bitwarden.com/help/bitwarden-apis/) | Vault management and organization administration | 🟡 API Key | ✅ | ✅ |
| [HashiCorp Vault API](https://developer.hashicorp.com/vault/api-docs) | Secrets engine with dynamic secrets, encryption, and PKI | 🟡 API Key | ✅ | ✅⭐ |
| [CyberArk API](https://api-docs.cyberark.com/) | Privileged access management with safe and account operations | 🔴 OAuth | ✅ | ✅ |
| [Doppler API](https://docs.doppler.com/reference/api) | Cloud-based secrets management with sync across environments | 🟡 API Key | ✅ | ✅⭐ |
| [Keeper Secrets Manager API](https://docs.keeper.io/en/enterprise-guide/developer-tools) | Zero-knowledge secrets management with rotation and SDK tools | 🟡 API Key | ✅ | ✅ |
| [Delinea Secret Server API](https://docs.delinea.com/online-help/secret-server/api-scripting/rest-api/index.htm) | Privileged credential storage with REST and SOAP interfaces | 🔴 OAuth | ✅ | ✅ |
| [Akeyless API](https://docs.akeyless.io/) | Vaultless secrets management with dynamic secrets and SSO | 🟡 API Key | ✅ | ✅ |
| [AWS Secrets Manager API](https://docs.aws.amazon.com/secretsmanager/latest/apireference/) | AWS-native secrets storage with automatic rotation | 🟡 API Key | ✅ | ✅⭐ |
| [Azure Key Vault API](https://learn.microsoft.com/en-us/rest/api/keyvault/) | Microsoft cloud key and secret management with HSM backing | 🔴 OAuth | ✅ | ✅ |
| [Google Secret Manager API](https://cloud.google.com/secret-manager/docs/reference/rest) | GCP secrets storage with versioning and IAM access control | 🔴 OAuth | ✅ | ✅ |
| [Infisical API](https://infisical.com/docs/api-reference/overview/introduction) | Open-source secrets management with E2E encryption | 🟡 API Key | ✅ | ✅ |

---

## 🔔 Notification & Alert Orchestration APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [OneSignal API](https://documentation.onesignal.com/reference/rest-api-overview) | Cross-platform push notifications for web, mobile, email, and SMS | 🟡 API Key | ✅ | ✅⭐ |
| [Firebase Cloud Messaging API](https://firebase.google.com/docs/reference/fcm/rest) | Google's cross-platform messaging for push notifications | 🔴 OAuth | ✅ | ✅ |
| [Courier API](https://www.courier.com/docs/welcome) | Unified multi-channel notification orchestration platform | 🟡 API Key | ✅ | ✅⭐ |
| [Novu API](https://docs.novu.co/platform/overview) | Open-source notification infrastructure for email, SMS, push, chat | 🟡 API Key | ✅ | ✅⭐ |
| [Knock API](https://docs.knock.app/) | Notification engine with feeds, preferences, and workflows | 🟡 API Key | ✅ | ✅⭐ |
| [Pushover API](https://pushover.net/api) | Simple push notifications to Android, iOS, and desktop devices | 🟡 API Key | ✅ | ✅ |
| [ntfy API](https://docs.ntfy.sh/) | Open-source HTTP-based pub-sub push notification service | 🟢 No | ✅ | ✅⭐ |
| [PagerDuty API](https://developer.pagerduty.com/api-reference/) | Incident alerting and on-call management for DevOps teams | 🟡 API Key | ✅ | ✅⭐ |
| [Twilio API](https://www.twilio.com/docs/usage/api) | SMS, voice, email, and WhatsApp messaging at global scale | 🟡 API Key | ✅ | ✅⭐ |
| [Amazon SNS API](https://docs.aws.amazon.com/sns/latest/api/welcome.html) | AWS pub-sub messaging for push, SMS, email, and SQS | 🟡 API Key | ✅ | ✅ |
| [Pushbullet API](https://docs.pushbullet.com/) | Push notifications, file sharing, and mirroring across devices | 🟡 API Key | ✅ | ✅ |
| [MagicBell API](https://www.magicbell.com/docs/rest-api/overview) | In-app notification inbox with real-time delivery and preferences | 🟡 API Key | ✅ | ✅ |
| [Opsgenie API](https://docs.opsgenie.com/docs/api-overview) | Alert management with on-call scheduling and escalation policies | 🟡 API Key | ✅ | ✅ |

---

## 🎵 Music Rights & Royalty APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Revelator API](https://api-docs.revelator.com/en/getting-started) | Music distribution, rights management, royalty reporting, and analytics | 🟡 API Key | ✅ | ✅⭐ |
| [Spotify Web API](https://developer.spotify.com/documentation/web-api) | Music metadata, track info, artist data, and audio features | 🔴 OAuth | ✅ | ✅⭐ |
| [MusicBrainz API](https://musicbrainz.org/doc/MusicBrainz_API) | Open music encyclopedia with recordings, releases, and artist data | 🟢 No | ✅ | ✅⭐ |
| [Audius API](https://docs.audius.org/api/) | Decentralized music streaming with tracks, playlists, and tips | 🟡 API Key | ✅ | ✅ |
| [Epidemic Sound API](https://developers.epidemicsound.com/) | Licensed music catalog for content creators with track search | 🟡 API Key | ✅ | ✅ |
| [ASCAP ACE Repertory](https://www.ascap.com/repertory) | Search ASCAP's catalog of registered musical works and rights holders | 🟢 No | ✅ | ⚠️ |
| [BMI Repertoire Search](https://repertoire.bmi.com/) | Search BMI's database of musical work registrations and publishers | 🟢 No | ✅ | ⚠️ |
| [SoundExchange ISRC Search](https://isrc.soundexchange.com/) | Look up ISRC codes and sound recording data for digital royalties | 🟢 No | ✅ | ⚠️ |
| [TheAudioDB API](https://www.theaudiodb.com/api_guide.php) | Community music database with artist, album, and track metadata | 🟡 API Key | ✅ | ✅ |
| [Songview (ASCAP/BMI)](https://songview.com/) | Joint ASCAP/BMI database of copyright ownership for 38M+ works | 🟢 No | ✅ | ⚠️ |
| [Feed.fm Music API](https://www.feed.fm/music-api) | Licensed music streaming API for apps and businesses | 🟡 API Key | ✅ | ✅ |
| [Loudly AI Music API](https://www.loudly.com/knowledge-base/ai-music-api-developers) | AI-generated royalty-free music for apps and games | 🟡 API Key | ✅ | ✅ |

---

## 📱 Mobile Device Management (MDM) APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Jamf Pro API](https://developer.jamf.com/jamf-pro/docs/jamf-pro-api-overview) | Apple device management with profiles, apps, and inventory | 🔴 OAuth | ✅ | ✅⭐ |
| [Microsoft Intune API (Graph)](https://learn.microsoft.com/en-us/graph/intune-concept-overview) | Windows and cross-platform device management via Microsoft Graph | 🔴 OAuth | ✅ | ✅⭐ |
| [Kandji API](https://api-docs.kandji.io/) | Apple MDM with device actions, blueprints, and app management | 🟡 API Key | ✅ | ✅ |
| [Hexnode API](https://www.hexnode.com/mobile-device-management/developers/api-reference/) | Unified endpoint management for iOS, Android, Windows, and macOS | 🟡 API Key | ✅ | ✅ |
| [ManageEngine MDM API](https://www.manageengine.com/mobile-device-management/api/) | Device enrollment, profiles, apps, and content management | 🟡 API Key | ✅ | ✅ |
| [SureMDM API (42Gears)](https://developer.42gears.com/suremdm/api/v2/) | Multi-OS endpoint management with jobs, profiles, and alerts | 🟡 API Key | ✅ | ✅ |
| [Scalefusion API](https://help.scalefusion.com/docs/scalefusion-developer-api) | MDM with kiosk lockdown, remote troubleshooting, and geofencing | 🟡 API Key | ✅ | ✅ |
| [Mosyle API](https://business.mosyle.com/) | Apple-focused MDM with automated enrollment and app management | 🟡 API Key | ✅ | ⚠️ |
| [VMware Workspace ONE API](https://docs.omnissa.com/bundle/WorkspaceONEUEMRestAPIDoc/) | Enterprise UEM with identity, apps, and compliance management | 🟡 API Key | ✅ | ✅ |
| [Codeproof MDM API](https://www.codeproof.com/resources/mdm-api/) | Modern cloud MDM with RESTful API for device management | 🟡 API Key | ✅ | ✅ |
| [SOTI MobiControl API](https://www.soti.net/products/soti-mobicontrol/) | Enterprise mobility management with device tracking and control | 🟡 API Key | ✅ | ⚠️ |
| [Apple MDM Protocol](https://developer.apple.com/documentation/devicemanagement) | Apple's native device management protocol and command framework | 🔴 OAuth | ✅ | ⚠️ |

---

## 🚚 Logistics & Freight Brokerage APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Flexport API](https://developers.flexport.com/) | Supply chain logistics with shipments, documents, and trade data | 🟡 API Key | ✅ | ✅⭐ |
| [project44 API](https://developers.project44.com/api-reference/) | Multi-modal visibility with real-time tracking and rate quoting | 🟡 API Key | ✅ | ✅ |
| [ShipEngine API](https://www.shipengine.com/docs/) | Multi-carrier shipping with rates, labels, and tracking (UPS, FedEx, USPS) | 🟡 API Key | ✅ | ✅⭐ |
| [EasyPost API](https://docs.easypost.com/) | Shipping with address verification, rate comparison, and tracking | 🟡 API Key | ✅ | ✅⭐ |
| [Shippo API](https://docs.goshippo.com/) | Multi-carrier shipping rates, labels, and tracking | 🟡 API Key | ✅ | ✅⭐ |
| [Freightos API](https://developers.freightos.com/) | International freight rates from top forwarders with instant quotes | 🟡 API Key | ✅ | ✅ |
| [ShipBob API](https://developer.shipbob.com/) | Fulfillment with inventory, orders, returns, and warehouse management | 🟡 API Key | ✅ | ✅ |
| [AfterShip API](https://www.aftership.com/docs) | Shipment tracking across 1100+ carriers with delivery predictions | 🟡 API Key | ✅ | ✅⭐ |
| [Shipwell API](https://docs.shipwell.com/) | Freight management with rate quotes, dispatch, and invoice processing | 🟡 API Key | ✅ | ✅ |
| [Flexport Logistics API](https://docs.logistics-api.flexport.com/) | E-commerce fulfillment, returns, freight, and parcel operations | 🟡 API Key | ✅ | ✅ |
| [Shipstation API](https://www.shipstation.com/docs/api/) | Order management and multi-carrier shipping for ecommerce | 🟡 API Key | ✅ | ✅ |
| [FedEx API](https://developer.fedex.com/) | Shipping rates, tracking, labels, and pickup scheduling | 🔴 OAuth | ✅ | ✅ |

---

## 🧠 Knowledge Graph & Ontology APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Google Knowledge Graph API](https://developers.google.com/knowledge-graph) | Search entities in Google's Knowledge Graph by name or ID | 🟡 API Key | ✅ | ✅⭐ |
| [Wikidata SPARQL API](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service) | Query the open knowledge base with 100M+ items via SPARQL | 🟢 No | ✅ | ✅⭐ |
| [DBpedia SPARQL Endpoint](https://dbpedia.org/sparql) | Structured data from Wikipedia with RDF triples and SPARQL queries | 🟢 No | ✅ | ✅ |
| [Wikidata REST API](https://www.wikidata.org/wiki/Wikidata:REST_API) | RESTful access to Wikidata entities, statements, and labels | 🟢 No | ✅ | ✅⭐ |
| [ConceptNet API](http://conceptnet.io/) | Open multilingual knowledge graph of common-sense relationships | 🟢 No | ✅ | ✅ |
| [DBpedia Lookup API](https://lookup.dbpedia.org/) | Keyword search over DBpedia resources and classifications | 🟢 No | ✅ | ✅ |
| [OpenLink Virtuoso SPARQL](https://virtuoso.openlinksw.com/) | High-performance SPARQL endpoint for RDF knowledge graphs | 🟢 No | ✅ | ⚠️ |
| [BioPortal API](https://data.bioontology.org/documentation) | Biomedical ontology repository with class, mapping, and search APIs | 🟡 API Key | ✅ | ✅ |
| [EBI Ontology Lookup Service](https://www.ebi.ac.uk/ols4/swagger-ui/index.html) | Search and browse biomedical and life science ontologies | 🟢 No | ✅ | ✅ |
| [Linked Open Vocabularies API](https://lov.linkeddata.es/dataset/lov/api) | Search and discover RDF vocabularies and ontologies | 🟢 No | ✅ | ✅ |
| [Wolfram Knowledgebase API](https://products.wolframalpha.com/api) | Curated knowledge base with computed answers to factual queries | 🟡 API Key | ✅ | ✅ |
| [Microsoft Academic Knowledge API](https://learn.microsoft.com/en-us/academic-services/) | Academic entity graph with papers, authors, and citation data | 🟡 API Key | ✅ | ⚠️ |

---

## 🛡️ Insurance Claims Processing APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Guidewire ClaimCenter API](https://docs.guidewire.com/cloud/cc/202411/apiref/) | P&C claims management with FNOL, reserves, and payments | 🔴 OAuth | ✅ | ✅ |
| [Guidewire Cloud API](https://www.guidewire.com/developers/apis/cloud-apis) | RESTful system APIs for InsuranceSuite (Policy, Billing, Claims) | 🔴 OAuth | ✅ | ✅ |
| [Socotra API](https://docs.socotra.com/) | Cloud-native insurance platform with policy, claims, and billing | 🟡 API Key | ✅ | ✅⭐ |
| [Duck Creek API](https://www.duckcreek.com/product/anywhere-integration/) | P&C policy and claims with RESTful integration framework | 🟡 API Key | ✅ | ⚠️ |
| [ClaimVantage (Majesco)](https://www.majesco.com/core-software-insurance-solutions/claimvantage/) | L&H claims management on Salesforce with REST APIs | 🔴 OAuth | ✅ | ✅ |
| [Snapsheet Claims API](https://www.snapsheetclaims.com/) | Virtual appraisal and claims management automation platform | 🟡 API Key | ✅ | ⚠️ |
| [CoverGo API](https://www.covergo.com/api-platform) | No-code insurance platform with policy and claims REST APIs | 🟡 API Key | ✅ | ✅ |
| [Insly API](https://docs.insly.com/) | Insurance management system with policies, claims, and accounting | 🟡 API Key | ✅ | ✅ |
| [Root Insurance API](https://root.co.za/docs/insurance-api/) | Programmable insurance platform for embedded policy and claims | 🟡 API Key | ✅ | ✅ |
| [Lemonade API](https://developer.lemonade.com/) | AI-driven insurance with instant claims processing | 🟡 API Key | ✅ | ⚠️ |
| [Bold Penguin API](https://www.boldpenguin.com/) | Commercial insurance exchange with quoting and binding APIs | 🟡 API Key | ✅ | ⚠️ |
| [EIS API](https://www.eisgroup.com/) | Core insurance platform with policy admin and claims processing | 🟡 API Key | ✅ | ⚠️ |

---

## 🏥 Healthcare Interoperability (HL7/FHIR) APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Epic on FHIR](https://fhir.epic.com/) | FHIR R4 APIs for patient data, appointments, medications, and labs | 🔴 OAuth | ✅ | ✅⭐ |
| [Oracle Health (Cerner) FHIR API](https://fhir.cerner.com/) | Cerner Ignite FHIR APIs for clinical data and patient access | 🔴 OAuth | ✅ | ✅⭐ |
| [Allscripts FHIR API](https://developer.allscripts.com/content/fhir/) | FHIR R4 and DSTU2 APIs for ambulatory and acute care data | 🔴 OAuth | ✅ | ✅ |
| [SMART on FHIR](https://docs.smarthealthit.org/) | Open standard for launching FHIR apps with OAuth2 authorization | 🔴 OAuth | ✅ | ✅⭐ |
| [CMS Blue Button 2.0 API](https://bluebutton.cms.gov/developers/) | Medicare Part A, B, and D claims data for 60M+ beneficiaries | 🔴 OAuth | ✅ | ✅⭐ |
| [HAPI FHIR Server](https://hapifhir.io/) | Open-source Java FHIR server and client implementation | 🟢 No | ✅ | ✅⭐ |
| [Redox API](https://docs.redoxengine.com/) | Healthcare data integration platform with FHIR and legacy support | 🟡 API Key | ✅ | ✅ |
| [1upHealth API](https://1up.health/docs/) | FHIR-based patient data aggregation across 10,000+ health systems | 🔴 OAuth | ✅ | ✅ |
| [Health Gorilla API](https://developer.healthgorilla.com/docs) | Lab ordering, results, referrals, and patient access via FHIR | 🔴 OAuth | ✅ | ✅ |
| [Medplum API](https://www.medplum.com/docs/api) | Open-source FHIR server with custom workflows and automation | 🟡 API Key | ✅ | ✅⭐ |
| [FHIR.org Test Server](https://hapi.fhir.org/) | Public HAPI FHIR test server for development and testing | 🟢 No | ✅ | ✅ |
| [Google Cloud Healthcare API](https://cloud.google.com/healthcare-api/docs) | GCP-hosted FHIR, HL7v2, and DICOM data stores and APIs | 🔴 OAuth | ✅ | ✅ |

---

## 🌿 Green Energy & Carbon Offset APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Climatiq API](https://www.climatiq.io/docs) | Carbon emission calculations for transport, energy, and supply chain | 🟡 API Key | ✅ | ✅⭐ |
| [Cloverly API](https://cloverly.com/api) | Carbon offsets for ecommerce, freight, travel, and utilities | 🟡 API Key | ✅ | ✅⭐ |
| [WattTime API](https://docs.watttime.org/) | Real-time marginal emissions data for electric grids worldwide | 🟡 API Key | ✅ | ✅⭐ |
| [Electricity Maps API](https://portal.electricitymaps.com/docs) | 24/7 grid carbon intensity data (historical, real-time, forecast) | 🟡 API Key | ✅ | ✅ |
| [Carbon Interface API](https://docs.carboninterface.com/) | Carbon footprint estimates for electricity, flights, and vehicles | 🟡 API Key | ✅ | ✅⭐ |
| [Patch API](https://www.patch.io/) | Carbon offset purchasing with verified removal projects | 🟡 API Key | ✅ | ✅ |
| [Open Charge Map API](https://openchargemap.org/site/develop/api) | Global registry of EV charging locations with 250K+ stations | 🟡 API Key | ✅ | ✅⭐ |
| [CO2 Signal API](https://docs.co2signal.com/) | Real-time carbon intensity of electricity by country and region | 🟡 API Key | ✅ | ✅ |
| [Green Web Foundation API](https://developers.thegreenwebfoundation.org/) | Check if websites are hosted on green energy infrastructure | 🟢 No | ✅ | ✅ |
| [EPA ENERGY STAR API](https://www.energystar.gov/buildings/tools-and-resources/portfolio-manager-web-services) | Building energy performance benchmarking and certification | 🟡 API Key | ✅ | ⚠️ |
| [National Renewable Energy Lab API](https://developer.nrel.gov/) | Solar, wind, and renewable energy datasets and calculators | 🟡 API Key | ✅ | ✅ |
| [OpenWeather Solar Radiation API](https://openweathermap.org/api/solar-radiation) | Solar irradiance and UV data for renewable energy planning | 🟡 API Key | ✅ | ✅ |

---

## 🎮 Gamification & Rewards APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Tremendous API](https://developers.tremendous.com/docs/introduction) | Digital rewards, gift cards, and payouts with 2000+ options globally | 🟡 API Key | ✅ | ✅⭐ |
| [Voucherify API](https://api-examples.voucherify.io/) | Coupon, discount, referral, and loyalty campaign management | 🟡 API Key | ✅ | ✅⭐ |
| [Open Loyalty API](https://www.openloyalty.io/technology/loyalty-program-api) | Open-source loyalty program with points, tiers, and rewards | 🟡 API Key | ✅ | ✅ |
| [Smile.io API](https://dev.smile.io/) | Loyalty points, VIP tiers, and referral programs for ecommerce | 🟡 API Key | ✅ | ✅ |
| [LoyaltyLion API](https://developers.loyaltylion.com/api/) | Ecommerce loyalty with points, rewards, and customer management | 🟡 API Key | ✅ | ✅ |
| [Yotpo Loyalty API](https://loyaltyapi.yotpo.com/reference/introduction-1) | Loyalty and referrals with rewards redemption and customer data | 🟡 API Key | ✅ | ✅ |
| [Talon.One API](https://docs.talon.one/docs/dev/getting-started/overview) | Promotion engine with gamification, coupons, and loyalty campaigns | 🟡 API Key | ✅ | ✅⭐ |
| [Giftbit API](https://www.giftbit.com/resources/gift-card-api-basics) | Gift card ordering, sending, and tracking at scale | 🟡 API Key | ✅ | ✅ |
| [GameLayer API](https://gamelayer.co/) | API-first gamification with achievements, leaderboards, and XP | 🟡 API Key | ✅ | ✅ |
| [Antavo API](https://developers.antavo.com/) | Enterprise loyalty management with events, rewards, and tiers | 🟡 API Key | ✅ | ✅ |
| [Rybbon API](https://www.rybbon.net/) | Digital reward delivery and tracking for incentive programs | 🟡 API Key | ✅ | ⚠️ |
| [Bprogram API](https://bprogram.io/) | Gamification-as-a-service with missions, badges, and leaderboards | 🟡 API Key | ✅ | ⚠️ |

---

## 🍔 Food Ordering & Menu APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [DoorDash Drive API](https://developer.doordash.com/en-US/api/drive/) | On-demand delivery with quotes, serviceability, and order creation | 🟡 API Key | ✅ | ✅⭐ |
| [Uber Eats Marketplace API](https://developer.uber.com/docs/eats/introduction) | Store, menu, and order management on Uber Eats platform | 🔴 OAuth | ✅ | ✅ |
| [Grubhub Developer API](https://developer.grubhub.com/api/orders) | Menu ingestion and order management for restaurant partners | 🟡 API Key | ✅ | ⚠️ |
| [Square Orders API](https://developer.squareup.com/reference/square/orders-api) | Restaurant ordering with itemized payments and POS integration | 🔴 OAuth | ✅ | ✅⭐ |
| [Toast API](https://doc.toasttab.com/doc/devguide/apiOverview.html) | Restaurant POS with menus, orders, and location management | 🟡 API Key | ✅ | ✅ |
| [MealMe API](https://www.mealme.ai/) | Aggregated ordering across 1M+ restaurants and grocery stores | 🟡 API Key | ✅ | ✅ |
| [Olo Omnivore API](https://www.olo.com/omnivoreapi) | Universal POS integration for restaurant menu and order sync | 🟡 API Key | ✅ | ✅ |
| [GloriaFood API](https://www.gloriafood.com/restaurant-ordering-system-with-food-ordering-api) | Free online ordering system with menu and order post-processing | 🟡 API Key | ✅ | ✅ |
| [CloudWaitress API](https://www.cloudwaitress.com/features/api-access/) | Restaurant ordering with delivery, pickup, and table ordering | 🟡 API Key | ✅ | ✅ |
| [KitchenHub API](https://www.trykitchenhub.com/developer) | Unified API connecting DoorDash, Uber Eats, and Grubhub orders | 🟡 API Key | ✅ | ✅ |
| [Delivery Hero API](https://developers.deliveryhero.com/documentation/pos.html) | Restaurant POS integration for delivery platforms globally | 🟡 API Key | ✅ | ⚠️ |
| [Spoonacular API](https://spoonacular.com/food-api) | Recipe, ingredient, menu, and meal planning data API | 🟡 API Key | ✅ | ✅⭐ |

---

## 💳 Digital Wallet & Mobile Payment APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Stripe API](https://docs.stripe.com/api) | Complete payment platform with cards, wallets, and subscriptions | 🟡 API Key | ✅ | ✅⭐ |
| [PayPal REST API](https://developer.paypal.com/api/rest/) | Online payments, checkout, and payouts with 400M+ active accounts | 🔴 OAuth | ✅ | ✅⭐ |
| [Apple Pay JS API](https://developer.apple.com/documentation/applepayontheweb/apple-pay-js-api) | Secure in-app and web payments via Apple Pay tokenization | 🔴 OAuth | ✅ | ⚠️ |
| [Google Pay API](https://developers.google.com/pay/api) | In-app and web payments with Google Pay tokenized cards | 🟡 API Key | ✅ | ✅ |
| [Google Wallet API](https://developers.google.com/wallet/reference/rest) | Create and manage passes, loyalty cards, and tickets in Google Wallet | 🔴 OAuth | ✅ | ✅ |
| [Adyen API](https://docs.adyen.com/) | Enterprise payments with 250+ local methods and intelligent routing | 🟡 API Key | ✅ | ✅⭐ |
| [Braintree API](https://developer.paypal.com/braintree/docs/) | PayPal-owned payment gateway with vault, PayPal, and Venmo | 🟡 API Key | ✅ | ✅ |
| [Square Payments API](https://developer.squareup.com/reference/square) | Omnichannel payments with in-person, online, and mobile support | 🔴 OAuth | ✅ | ✅⭐ |
| [Marqeta API](https://www.marqeta.com/docs/core-api/introduction) | Card issuing with digital wallet tokenization and spend controls | 🟡 API Key | ✅ | ✅ |
| [Dwolla API](https://developers.dwolla.com/docs/api-reference/api-fundamentals) | ACH bank transfers with programmable payment workflows | 🔴 OAuth | ✅ | ✅ |
| [Wise (TransferWise) API](https://docs.wise.com/api-reference) | International money transfers with real exchange rates | 🟡 API Key | ✅ | ✅ |
| [Sila Money API](https://www.silamoney.com/wallet-api) | Digital wallet with ACH, KYC/KYB, and virtual account management | 🟡 API Key | ✅ | ✅ |
| [NovoPayment API](https://developer.novopayment.com/api/digital-wallets) | Digital wallet management with card issuance for Latin America | 🟡 API Key | ✅ | ⚠️ |

---

## ⛪ Church & Nonprofit Management APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Planning Center API](https://developer.planning.center/docs/) | Church management with people, giving, services, and groups | 🔴 OAuth | ✅ | ✅⭐ |
| [Breeze ChMS API](https://app.breezechms.com/api) | Simple church management with people, contributions, and events | 🟡 API Key | ✅ | ✅ |
| [Pushpay API](https://pushpay.io/docs/api) | Church giving and payment processing with donor management | 🔴 OAuth | ✅ | ✅ |
| [Tithe.ly API](https://docs.tithe.ly/reference/introduction) | Online church giving with donor records and transaction data | 🟡 API Key | ✅ | ✅ |
| [Church Community Builder API](https://designccb.s3.amazonaws.com/helpdesk/files/official_docs/api.html) | Process-driven ChMS with groups, events, and giving management | 🟡 API Key | ✅ | ⚠️ |
| [FellowshipOne API](https://developer.fellowshipone.com/) | Church management with people, attributes, and communications | 🔴 OAuth | ✅ | ⚠️ |
| [Blackbaud SKY API](https://developer.blackbaud.com/skyapi) | Nonprofit CRM with fundraising, constituent, and financial data | 🔴 OAuth | ✅ | ✅⭐ |
| [Bloomerang API](https://bloomerang.com/api/) | Nonprofit donor management with constituents and donations | 🟡 API Key | ✅ | ✅ |
| [Virtuous API](https://virtuous.org/api/) | Responsive nonprofit CRM with giving, contacts, and automation | 🟡 API Key | ✅ | ✅ |
| [Donorbox API](https://donorbox.org/) | Nonprofit online fundraising with recurring donations and campaigns | 🟡 API Key | ✅ | ⚠️ |
| [Subsplash API](https://www.subsplash.com/) | Church engagement platform with apps, giving, and media | 🟡 API Key | ✅ | ⚠️ |
| [Kindful (Bloomerang) API](https://kindful.com/) | Nonprofit donor CRM with flexible integrations and reporting | 🟡 API Key | ✅ | ✅ |
| [Salesforce Nonprofit Cloud API](https://developer.salesforce.com/docs/atlas.en-us.npc.meta/npc/) | Enterprise nonprofit CRM with program, grant, and donor management | 🔴 OAuth | ✅ | ✅⭐ |

---

## 📅 Appointment Scheduling & Booking APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Calendly](https://developer.calendly.com/) | REST API for scheduling events, managing availability, and webhooks | 🔴 OAuth | ✅ | ✅⭐ |
| [Acuity Scheduling](https://developers.acuityscheduling.com/) | Book, cancel, and reschedule appointments with powerful scheduling rules | 🔴 OAuth | ✅ | ✅⭐ |
| [Square Bookings](https://developer.squareup.com/reference/square/bookings-api) | Create, retrieve, update, and cancel service appointments for Square sellers | 🔴 OAuth | ✅ | ✅⭐ |
| [SimplyBook.me](https://simplybook.me/en/api/developer-api) | Create booking records with provider/service availability management | 🟡 API Key | ✅ | ✅ |
| [OnSched](https://www.onsched.com/) | White-label scheduling API for healthcare, beauty, and enterprise booking | 🟡 API Key | ✅ | ✅⭐ |
| [Cal.com](https://cal.com/docs/api-reference) | Open-source scheduling with REST and GraphQL endpoints for full booking control | 🟡 API Key | ✅ | ✅⭐ |
| [Cronofy](https://docs.cronofy.com/developers/api/) | Unified calendar sync and scheduling API across Google, Outlook, and iCloud | 🔴 OAuth | ✅ | ✅⭐ |
| [Setmore](https://setmore.docs.apiary.io/) | Appointment scheduling with customer and staff management endpoints | 🔴 OAuth | ✅ | ✅ |
| [SuperSaaS](https://www.supersaas.com/info/dev/appointment_api) | CRUD operations on appointments with availability and agenda endpoints | 🟡 API Key | ✅ | ✅ |
| [DaySchedule](https://dayschedule.com/docs/api) | Scheduling API for 1:1, round-robin, and group bookings | 🟡 API Key | ✅ | ✅ |
| [Timekit](https://www.timekit.io/) | Flexible booking calendar API with availability and resource management | 🟡 API Key | ✅ | ✅ |
| [MakePlans](https://makeplans.com/en/api/) | Online booking for appointments and events with REST endpoints | 🟡 API Key | ✅ | ✅ |
| [Nylas Scheduler](https://developer.nylas.com/docs/v3/calendar/) | Unified calendar and scheduling API with secure user calendar connections | 🔴 OAuth | ✅ | ✅⭐ |

---

## 🔍 Background Check & Screening APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Checkr](https://docs.checkr.com/) | Modern RESTful background screening with webhooks and candidate management | 🟡 API Key | ✅ | ✅⭐ |
| [Sterling](https://www.sterlingcheck.com/services/api/) | Initiate background checks and receive screening status updates via REST | 🟡 API Key | ✅ | ✅ |
| [Certn](https://docs.certn.co/api) | RESTful background screening API with sandbox and international checks | 🟡 API Key | ✅ | ✅⭐ |
| [GoodHire](https://www.goodhire.com/api/) | Launch background checks with Partner and Customer API modes | 🟡 API Key | ✅ | ✅ |
| [BackgroundChecks.com](https://www.backgroundchecks.com/developers/api) | Integrate background screening with token-based authentication | 🟡 API Key | ✅ | ✅ |
| [First Advantage](https://fadv.com/integrations-and-apis/) | XChange REST API for real-time screening orders and status notifications | 🟡 API Key | ✅ | ⚠️ |
| [Onfido (Entrust)](https://documentation.identity.entrust.com/) | Identity verification with document and biometric checks via REST | 🟡 API Key | ✅ | ✅⭐ |
| [Jumio](https://documentation.jumio.ai/docs/developer-resources/API/) | AI-powered identity verification with Account, Credentials, and Retrieval APIs | 🟡 API Key | ✅ | ✅ |
| [Persona](https://docs.withpersona.com/api-introduction) | Identity verification, risk assessment, and compliance via REST endpoints | 🟡 API Key | ✅ | ✅⭐ |
| [Sumsub](https://docs.sumsub.com/) | All-in-one KYC/KYB, AML screening and fraud verification platform | 🟡 API Key | ✅ | ✅⭐ |
| [Trulioo](https://developer.trulioo.com/reference/welcome) | Global identity verification with Platform API, KYC API, and KYB API | 🟡 API Key | ✅ | ✅ |
| [PESCHECK](https://pescheck.io/background-check-api/) | RESTful background check API with JSON responses and sandbox environment | 🟡 API Key | ✅ | ✅ |
| [Verifile](https://support.verifile.co.uk/support/solutions/articles/101000496880-verifile-s-global-background-check-api) | Global background check API with modern REST and JSON architecture | 🟡 API Key | ✅ | ✅ |

---

## 📊 Business Intelligence & Analytics APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Microsoft Power BI](https://learn.microsoft.com/en-us/rest/api/power-bi/) | Embed, administer, and manage Power BI resources programmatically | 🔴 OAuth | ✅ | ✅⭐ |
| [Tableau REST API](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api.htm) | Manage workbooks, data sources, users, and sites on Tableau Server/Cloud | 🟡 API Key | ✅ | ✅⭐ |
| [Looker (Google Cloud)](https://cloud.google.com/looker/docs/api-reference) | Data exploration, embedded analytics, and custom dashboards via REST | 🔴 OAuth | ✅ | ✅⭐ |
| [Metabase](https://www.metabase.com/learn/metabase-basics/administration/administration-and-operation/metabase-api) | Open-source BI with REST API for dashboards, questions, and data queries | 🟡 API Key | ✅ | ✅⭐ |
| [Sisense](https://developer.sisense.com/guides/restApi/) | Embedded analytics REST API for dashboards, widgets, and data models | 🟡 API Key | ✅ | ✅ |
| [Domo](https://developer.domo.com/) | Cloud BI platform with APIs for datasets, cards, pages, and user management | 🔴 OAuth | ✅ | ✅ |
| [Google Analytics Data API](https://developers.google.com/analytics/devguides/reporting/data/v1) | Programmatic access to Google Analytics reporting data | 🔴 OAuth | ✅ | ✅⭐ |
| [Mixpanel](https://developer.mixpanel.com/) | Product analytics API for events, funnels, retention, and user cohorts | 🟡 API Key | ✅ | ✅⭐ |
| [Amplitude](https://www.docs.developers.amplitude.com/) | Behavioral analytics with REST APIs for events, user profiles, and cohorts | 🟡 API Key | ✅ | ✅⭐ |
| [Celonis](https://developer.celonis.com/process-intelligence-apis/intelligence-api/overview/) | Process intelligence API for embedding actionable insights into platforms | 🟡 API Key | ✅ | ✅ |
| [Heap](https://developers.heap.io/) | Auto-capture analytics with APIs for event tracking and user data | 🟡 API Key | ✅ | ✅ |
| [Plausible Analytics](https://plausible.io/docs/stats-api) | Privacy-friendly web analytics with a simple stats query API | 🟡 API Key | ✅ | ✅⭐ |

---

## 🗓️ Calendar & Time Management APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Google Calendar API](https://developers.google.com/calendar/api/guides/overview) | Create, read, and manage events and calendars on Google Calendar | 🔴 OAuth | ✅ | ✅⭐ |
| [Microsoft Graph Calendar](https://learn.microsoft.com/en-us/graph/outlook-calendar-concept-overview) | Manage Outlook calendars, events, meeting times, and attendees | 🔴 OAuth | ✅ | ✅⭐ |
| [Nylas Calendar](https://developer.nylas.com/docs/v3/calendar/) | Unified REST interface for calendars across Google, Outlook, and Exchange | 🔴 OAuth | ✅ | ✅⭐ |
| [Cronofy](https://docs.cronofy.com/developers/api/) | Calendar sync and availability API across multiple calendar providers | 🔴 OAuth | ✅ | ✅⭐ |
| [Zoho Calendar](https://www.zoho.com/calendar/help/api/introduction.html) | REST API for calendar and event management within the Zoho ecosystem | 🔴 OAuth | ✅ | ✅ |
| [Calendly](https://developer.calendly.com/) | Scheduling and event type management with availability controls | 🔴 OAuth | ✅ | ✅⭐ |
| [Aurinko](https://docs.aurinko.io/unified-apis/calendar-api) | Unified calendar API across Google, Outlook, iCloud, and more | 🔴 OAuth | ✅ | ✅ |
| [Cal.com](https://cal.com/docs/api-reference) | Open-source scheduling with bookings, availability, and event type APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Timekit](https://www.timekit.io/) | Calendar infrastructure API for managing time slots and booking rules | 🟡 API Key | ✅ | ✅ |
| [Notion](https://developers.notion.com/reference/intro) | Database and page management API with date properties for time tracking | 🟡 API Key | ✅ | ✅⭐ |
| [Clockify](https://docs.clockify.me/) | Time tracking REST API for projects, tasks, time entries, and reports | 🟡 API Key | ✅ | ✅⭐ |
| [Toggl Track](https://engineering.toggl.com/docs/) | Time tracking API with workspace, project, and time entry management | 🟡 API Key | ✅ | ✅ |
| [Harvest](https://help.getharvest.com/api-v2/) | Time tracking and invoicing REST API for projects and team time entries | 🔴 OAuth | ✅ | ✅⭐ |

---

## 💬 Chat & Messaging Platform APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Slack API](https://docs.slack.dev/) | Build apps with messaging, channels, workflows, and real-time events | 🔴 OAuth | ✅ | ✅⭐ |
| [Discord API](https://discord.com/developers/docs/reference) | Bot creation, messaging, guild management, and interaction endpoints | 🟡 API Key | ✅ | ✅⭐ |
| [Telegram Bot API](https://core.telegram.org/) | Create bots for messaging, inline queries, payments, and notifications | 🟡 API Key | ✅ | ✅⭐ |
| [Twilio Messaging](https://www.twilio.com/docs/messaging) | Send and receive SMS, MMS, and WhatsApp messages via REST API | 🟡 API Key | ✅ | ✅⭐ |
| [SendBird](https://sendbird.com/docs/chat) | In-app chat SDK and Platform API for messaging, channels, and moderation | 🟡 API Key | ✅ | ✅⭐ |
| [Stream Chat](https://getstream.io/chat/docs/) | Scalable chat API with real-time messaging, threads, and reactions | 🟡 API Key | ✅ | ✅⭐ |
| [Google Chat API](https://developers.google.com/workspace/chat/api/reference/rest) | Manage spaces, members, and messages in Google Workspace Chat | 🔴 OAuth | ✅ | ✅ |
| [Vonage Messages](https://developer.vonage.com/en/messages/concepts/whatsapp) | Multi-channel messaging across SMS, WhatsApp, Viber, and Messenger | 🟡 API Key | ✅ | ✅⭐ |
| [MessageBird](https://developers.messagebird.com/) | Omnichannel messaging API for SMS, WhatsApp, and conversational flows | 🟡 API Key | ✅ | ✅⭐ |
| [WhatsApp Business API](https://developers.facebook.com/docs/whatsapp) | Official WhatsApp messaging for business notifications and customer support | 🟡 API Key | ✅ | ✅ |
| [Rocket.Chat](https://developer.rocket.chat/) | Open-source team chat with REST API for channels, messages, and users | 🟡 API Key | ✅ | ✅⭐ |
| [Mattermost](https://api.mattermost.com/) | Open-source messaging with RESTful API for teams, channels, and posts | 🟡 API Key | ✅ | ✅⭐ |
| [Microsoft Teams (Graph)](https://learn.microsoft.com/en-us/graph/teams-concept-overview) | Manage teams, channels, chats, and messages via Microsoft Graph | 🔴 OAuth | ✅ | ✅ |

---

## ☁️ Cloud Storage & File Management APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Dropbox API](https://www.dropbox.com/developers/documentation/http/overview) | File upload, download, sharing, search, and folder management | 🔴 OAuth | ✅ | ✅⭐ |
| [Google Drive API](https://developers.google.com/drive/api/guides/about-sdk) | Create, read, and manage files and folders in Google Drive | 🔴 OAuth | ✅ | ✅⭐ |
| [Box Platform](https://developer.box.com/reference) | 150+ endpoints for file management, collaboration, and content security | 🔴 OAuth | ✅ | ✅⭐ |
| [Microsoft OneDrive (Graph)](https://learn.microsoft.com/en-us/graph/api/resources/onedrive) | File storage and sharing via Microsoft Graph REST API | 🔴 OAuth | ✅ | ✅⭐ |
| [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html) | Industry-standard object storage with REST API for buckets and objects | 🟡 API Key | ✅ | ✅⭐ |
| [Google Cloud Storage](https://docs.cloud.google.com/storage/docs/apis) | Scalable object storage with JSON and XML REST APIs | 🔴 OAuth | ✅ | ✅⭐ |
| [Backblaze B2](https://www.backblaze.com/docs/cloud-storage-apis) | S3-compatible and native B2 APIs for affordable cloud object storage | 🟡 API Key | ✅ | ✅⭐ |
| [Wasabi](https://docs.wasabi.com/apidocs/wasabi-api) | S3-compatible hot cloud storage API with no egress fees | 🟡 API Key | ✅ | ✅⭐ |
| [Cloudinary](https://cloudinary.com/documentation/solution_overview) | Media management with Upload, Admin, and Search APIs for images/video | 🟡 API Key | ✅ | ✅⭐ |
| [Filestack](https://www.filestack.com/docs/) | File upload, transformation, and delivery API with CDN | 🟡 API Key | ✅ | ✅ |
| [Uploadcare](https://uploadcare.com/api-refs/rest-api/) | File upload and processing REST API with CDN delivery | 🟡 API Key | ✅ | ✅⭐ |
| [MinIO](https://min.io/docs/minio/linux/developers/minio-drivers.html) | Open-source S3-compatible object storage with full API compatibility | 🟡 API Key | ✅ | ✅⭐ |
| [Azure Blob Storage](https://learn.microsoft.com/en-us/rest/api/storageservices/blob-service-rest-api) | Microsoft's scalable object storage with REST API for blobs and containers | 🟡 API Key | ✅ | ✅⭐ |

---

## 💻 Code Repository & Version Control APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [GitHub REST API](https://docs.github.com/en/rest) | Manage repos, pull requests, issues, actions, and releases on GitHub | 🔴 OAuth | ✅ | ✅⭐ |
| [GitLab REST API](https://docs.gitlab.com/api/rest/) | Full DevOps lifecycle API for projects, merge requests, CI/CD, and more | 🟡 API Key | ✅ | ✅⭐ |
| [Bitbucket Cloud API](https://developer.atlassian.com/cloud/bitbucket/rest/) | REST API for repos, pull requests, pipelines, and Jira integration | 🔴 OAuth | ✅ | ✅⭐ |
| [Azure DevOps REST API](https://learn.microsoft.com/en-us/rest/api/azure/devops/) | Manage repos, pipelines, work items, and builds on Azure DevOps | 🔴 OAuth | ✅ | ✅⭐ |
| [Gitea API](https://gitea.io/en-us/) | Self-hosted Git service with Swagger-documented REST API | 🟡 API Key | ✅ | ✅⭐ |
| [Gitee (China)](https://gitee.com/api/v5/swagger) | Chinese Git hosting platform with REST API for repos and collaboration | 🔴 OAuth | ✅ | ✅ |
| [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/APIReference/Welcome.html) | Managed Git repos in AWS with API for repositories, branches, and PRs | 🟡 API Key | ✅ | ✅ |
| [Codeberg](https://codeberg.org/api/swagger) | Free, open-source Git hosting with Gitea-based REST API | 🟡 API Key | ✅ | ✅ |
| [GitHub GraphQL API](https://docs.github.com/en/graphql) | Flexible GraphQL interface for precise GitHub data queries | 🔴 OAuth | ✅ | ✅⭐ |
| [GitLab GraphQL API](https://docs.gitlab.com/api/graphql/) | GraphQL endpoint for efficient GitLab resource queries | 🟡 API Key | ✅ | ✅⭐ |
| [Bitbucket Server API](https://developer.atlassian.com/server/bitbucket/rest/v1000/) | Self-hosted Bitbucket Data Center REST API for enterprise Git management | 🟡 API Key | ✅ | ✅ |
| [Gogs API](https://github.com/gogs/gogs) | Lightweight self-hosted Git service with RESTful API endpoints | 🟡 API Key | ✅ | ✅ |

---

## ✅ Compliance & Regulatory APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [ComplyAdvantage](https://docs.complyadvantage.com/api-docs) | AML screening, sanctions lists, PEP checks, and adverse media via REST | 🟡 API Key | ✅ | ✅⭐ |
| [Sumsub](https://docs.sumsub.com/) | All-in-one KYC/KYB verification with AML screening and fraud detection | 🟡 API Key | ✅ | ✅⭐ |
| [Trulioo](https://developer.trulioo.com/reference/welcome) | Global identity verification covering KYC, KYB, and Person Match | 🟡 API Key | ✅ | ✅⭐ |
| [Persona](https://docs.withpersona.com/api-introduction) | Identity verification and risk assessment with government ID checks | 🟡 API Key | ✅ | ✅⭐ |
| [Onfido (Entrust)](https://documentation.identity.entrust.com/) | Document verification and biometric identity checks via REST API | 🟡 API Key | ✅ | ✅⭐ |
| [Jumio](https://documentation.jumio.ai/docs/developer-resources/API/) | AI-powered identity proofing with document and selfie verification | 🟡 API Key | ✅ | ✅ |
| [ComplyCube](https://www.complycube.com/en/developers/) | KYC API and SaaS for identity verification and document checks | 🟡 API Key | ✅ | ✅⭐ |
| [KYC-Chain](https://kyc-chain.com/developers/) | KYC onboarding with token-based authentication and quick integration | 🟡 API Key | ✅ | ✅ |
| [SwiftDil](https://www.swiftdil.com/) | AML, KYC, and ID verification API with screening and monitoring | 🟡 API Key | ✅ | ✅ |
| [Moody's KYC (Kompany)](https://www.moodys.com/web/en/us/kyc/products/kompany.html) | Business verification and AML compliance via RESTful API | 🟡 API Key | ✅ | ⚠️ |
| [KYC Portal](https://www.kycportal.com/full-seamless-api-integration) | CDD, AML, and compliance management with full API integration | 🟡 API Key | ✅ | ⚠️ |
| [Smile ID](https://usesmileid.com/blog/kyc-api/) | KYC and AML compliance API focused on African identity verification | 🟡 API Key | ✅ | ✅ |

---

## 📝 Contract Management & CLM APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [DocuSign eSignature](https://developers.docusign.com/docs/esign-rest-api/) | Send, sign, and manage documents and envelopes via REST API | 🔴 OAuth | ✅ | ✅⭐ |
| [DocuSign CLM](https://developers.docusign.com/docs/clm-api/) | Contract lifecycle management with workflow, doc gen, and task APIs | 🔴 OAuth | ✅ | ✅⭐ |
| [Ironclad](https://developer.ironcladapp.com/) | API-first CLM platform with workflow and contract data endpoints | 🟡 API Key | ✅ | ✅⭐ |
| [PandaDoc](https://developers.pandadoc.com/) | Create, send, sign, and track documents with flexible REST API | 🔴 OAuth | ✅ | ✅⭐ |
| [Agiloft](https://wiki.agiloft.com/display/help/rest+interface) | No-code CLM with RESTful API and Swagger/OpenAPI documentation | 🟡 API Key | ✅ | ✅ |
| [HelloSign (Dropbox Sign)](https://developers.hellosign.com/) | eSignature API for embedded signing and template-based documents | 🟡 API Key | ✅ | ✅⭐ |
| [Adobe Sign](https://developer.adobe.com/document-services/docs/overview/) | Enterprise eSignature with agreement creation and management REST APIs | 🔴 OAuth | ✅ | ✅ |
| [SignNow](https://docs.signnow.com/) | eSignature REST API for document creation, sending, and signing | 🔴 OAuth | ✅ | ✅ |
| [Juro](https://juro.com/) | AI-native contract management with API-driven collaboration features | 🟡 API Key | ✅ | ⚠️ |
| [ContractWorks](https://www.contractworks.com/) | Contract repository and management with integration capabilities | 🟡 API Key | ✅ | ⚠️ |
| [Concord](https://www.concord.app/) | Full contract lifecycle management with collaboration and audit trail | 🟡 API Key | ✅ | ⚠️ |
| [eSign Genie](https://www.esigngenie.com/developer-api) | eSignature and document automation REST API for developers | 🟡 API Key | ✅ | ✅ |

---

## 🤝 CRM & Sales Automation APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Salesforce REST API](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/) | Industry-leading CRM with data manipulation, SOQL queries, and automation | 🔴 OAuth | ✅ | ✅⭐ |
| [HubSpot CRM API](https://developers.hubspot.com/) | Contacts, companies, deals, tickets, and marketing automation endpoints | 🔴 OAuth | ✅ | ✅⭐ |
| [Pipedrive API](https://developers.pipedrive.com/docs/api/v1) | RESTful CRM API for deals, contacts, activities, and pipelines | 🔴 OAuth | ✅ | ✅⭐ |
| [Zoho CRM API](https://www.zoho.com/crm/developer/docs/api/v8/) | V8 REST APIs for leads, contacts, deals, and custom modules | 🔴 OAuth | ✅ | ✅⭐ |
| [Freshsales API](https://developers.freshworks.com/crm/api/) | RESTful CRM API for contacts, deals, accounts, and sales sequences | 🟡 API Key | ✅ | ✅⭐ |
| [Close CRM API](https://developer.close.com/) | REST API for leads, contacts, opportunities, and sales activities | 🟡 API Key | ✅ | ✅⭐ |
| [Insightly API](https://api.na1.insightly.com/v3.1/) | REST + JSON API for contacts, organizations, projects, and pipelines | 🟡 API Key | ✅ | ✅ |
| [Copper CRM API](https://developer.copper.com/) | Google Workspace-native CRM with RESTful API for contacts and deals | 🟡 API Key | ✅ | ✅ |
| [Monday.com API](https://developer.monday.com/api-reference/) | GraphQL API for boards, items, columns, and automations | 🟡 API Key | ✅ | ✅⭐ |
| [Agile CRM](https://www.agilecrm.com/api) | REST API for contacts, deals, tasks, and campaign management | 🟡 API Key | ✅ | ✅ |
| [SugarCRM](https://support.sugarcrm.com/Documentation/Sugar_Developer/Sugar_Developer_Guide_13.0/Integration/Web_Services/REST_API/) | Enterprise CRM with REST v11+ API for modules and relationships | 🔴 OAuth | ✅ | ✅ |
| [Microsoft Dynamics 365](https://learn.microsoft.com/en-us/dynamics365/customer-engagement/web-api/about) | Enterprise CRM Web API for accounts, contacts, and opportunities | 🔴 OAuth | ✅ | ✅ |
| [Streak CRM](https://streak.readme.io/) | Gmail-integrated CRM with REST API for pipelines and boxes | 🔴 OAuth | ✅ | ✅ |

---

## 🧩 Customer Data Platform APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Segment](https://docs.segmentapis.com/) | Collect, unify, and route customer data with Tracking and Config APIs | 🟡 API Key | ✅ | ✅⭐ |
| [mParticle](https://docs.mparticle.com/developers/) | SDK and API for collecting, organizing, and managing customer data | 🟡 API Key | ✅ | ✅⭐ |
| [Tealium](https://docs.tealium.com/api/) | Customer data orchestration with V3 APIs for audiences and profiles | 🟡 API Key | ✅ | ✅ |
| [Treasure Data](https://api-docs.treasuredata.com/) | CDP API for bulk imports, database management, and job scheduling | 🟡 API Key | ✅ | ✅ |
| [Hightouch](https://hightouch.com/docs/developer-tools/api-guide) | Reverse ETL with REST API for syncs, models, sources, and destinations | 🟡 API Key | ✅ | ✅⭐ |
| [RudderStack](https://www.rudderstack.com/docs/api/http-api/) | Open-source CDP with HTTP API for event streaming and warehousing | 🟡 API Key | ✅ | ✅⭐ |
| [Customer.io](https://docs.customer.io/integrations/api/cdp/) | CDP API for tracking events, managing customer profiles, and messaging | 🟡 API Key | ✅ | ✅⭐ |
| [Bloomreach](https://documentation.bloomreach.com/) | CDP with personalization APIs for e-commerce customer engagement | 🟡 API Key | ✅ | ✅ |
| [Lytics](https://docs.lytics.com/) | Decision engine CDP with APIs for audience management and insights | 🟡 API Key | ✅ | ✅ |
| [Adobe Experience Platform](https://developer.adobe.com/experience-platform-apis/) | Enterprise CDP with APIs for profiles, segments, and data ingestion | 🔴 OAuth | ✅ | ✅ |
| [Salesforce Data Cloud](https://developer.salesforce.com/docs/atlas.en-us.c360a_api.meta/c360a_api/) | Unified customer profiles with data ingestion and query REST APIs | 🔴 OAuth | ✅ | ✅ |
| [PostHog](https://posthog.com/docs/api) | Open-source product analytics and CDP with REST API for events/persons | 🟡 API Key | ✅ | ✅⭐ |

---

## 📇 Data Enrichment & Business Data APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Clearbit (HubSpot)](https://clearbit.com/docs) | 100+ B2B attributes from 250+ sources for contact and company enrichment | 🟡 API Key | ✅ | ✅⭐ |
| [ZoomInfo](https://api-docs.zoominfo.com/) | Comprehensive B2B database for company and contact data enrichment | 🟡 API Key | ✅ | ✅ |
| [Apollo.io](https://docs.apollo.io/) | People and company enrichment with email finding and engagement data | 🟡 API Key | ✅ | ✅⭐ |
| [FullContact](https://www.fullcontact.com/developer-portal/) | Person and company data enrichment with identity resolution APIs | 🟡 API Key | ✅ | ✅⭐ |
| [People Data Labs](https://docs.peopledatalabs.com/) | 3 billion profiles with person, company, IP, and skill enrichment APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Hunter.io](https://hunter.io/api-documentation/v2) | Email finder, verifier, and lead enrichment with 100+ attributes | 🟡 API Key | ✅ | ✅⭐ |
| [Snov.io](https://snov.io/api) | Email finder, verifier, and drip campaign API for sales outreach | 🟡 API Key | ✅ | ✅ |
| [Lusha](https://www.lusha.com/docs/) | Contact and company enrichment with phone numbers and email addresses | 🟡 API Key | ✅ | ⚠️ |
| [Crunchbase](https://data.crunchbase.com/docs/crunchbase-basic-getting-started) | Company and funding data with search and autocomplete REST APIs | 🟡 API Key | ✅ | ✅⭐ |
| [OpenCorporates](https://api.opencorporates.com/) | Open database of global company registrations and officer data | 🟡 API Key | ✅ | ✅⭐ |
| [Pipl](https://docs.pipl.com/) | People search API for identity verification and fraud detection | 🟡 API Key | ✅ | ✅ |
| [Abstract API](https://www.abstractapi.com/) | Suite of enrichment APIs for email validation, geolocation, and more | 🟡 API Key | ✅ | ✅⭐ |
| [Diffbot](https://docs.diffbot.com/) | AI-powered web data extraction with Knowledge Graph and NLP APIs | 🟡 API Key | ✅ | ✅⭐ |

---

## 🎨 Design & Creative Tool APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Figma REST API](https://developers.figma.com/docs/rest-api/) | Access files, components, styles, and comments in Figma documents | 🔴 OAuth | ✅ | ✅⭐ |
| [Canva API](https://www.canva.dev/docs/connect/) | Programmatic design creation, asset management, and export | 🔴 OAuth | ✅ | ✅ |
| [Adobe Photoshop API](https://developer.adobe.com/photoshop/photoshop-api-docs/) | Cloud-based image editing, compositing, and smart object manipulation | 🔴 OAuth | ✅ | ✅⭐ |
| [Adobe Creative Cloud Libraries](https://developer.adobe.com/creative-cloud-libraries/docs/api/) | Manage shared design assets, colors, and components across Adobe apps | 🔴 OAuth | ✅ | ✅ |
| [Unsplash API](https://unsplash.com/documentation) | Access the largest library of free high-resolution photos via REST | 🟡 API Key | ✅ | ✅⭐ |
| [Pexels API](https://www.pexels.com/api/documentation/) | Free stock photos and videos with search and curated collection APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Remove.bg API](https://www.remove.bg/api) | Automated background removal from images via simple HTTP API | 🟡 API Key | ✅ | ✅⭐ |
| [Cloudinary](https://cloudinary.com/documentation/solution_overview) | Image and video upload, transformation, optimization, and delivery API | 🟡 API Key | ✅ | ✅⭐ |
| [imgix](https://docs.imgix.com/apis/rendering) | Real-time image processing and CDN delivery with URL-based transforms | 🟡 API Key | ✅ | ✅⭐ |
| [Pixlr API](https://pixlr.com/developer/) | Photo editing and design tools with SDK for embedded creative workflows | 🟡 API Key | ✅ | ✅ |
| [Bannerbear](https://developers.bannerbear.com/) | Auto-generate images and videos from templates via REST API | 🟡 API Key | ✅ | ✅⭐ |
| [Placid](https://placid.app/docs/2.0/) | Template-based image and PDF generation API for automated creatives | 🟡 API Key | ✅ | ✅⭐ |
| [Stability AI](https://platform.stability.ai/docs/api-reference) | AI image generation and editing with Stable Diffusion REST API | 🟡 API Key | ✅ | ✅⭐ |

---

## 📧 Email Marketing & Automation APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Mailchimp](https://mailchimp.com/developer/marketing/) | Marketing API for audiences, campaigns, automations, and analytics | 🔴 OAuth | ✅ | ✅⭐ |
| [SendGrid](https://docs.sendgrid.com/) | Transactional and marketing email with RESTful APIs and SMTP relay | 🟡 API Key | ✅ | ✅⭐ |
| [Brevo (Sendinblue)](https://developers.brevo.com/) | Unified API for email, SMS, and WhatsApp with contact management | 🟡 API Key | ✅ | ✅⭐ |
| [Mailgun](https://documentation.mailgun.com/) | Powerful email sending, receiving, and tracking APIs for developers | 🟡 API Key | ✅ | ✅⭐ |
| [Postmark](https://postmarkapp.com/developer/api/email-api) | Fast transactional email delivery with clean REST API and webhooks | 🟡 API Key | ✅ | ✅⭐ |
| [Amazon SES](https://docs.aws.amazon.com/ses/latest/APIReference/Welcome.html) | Low-cost, highly scalable email sending service integrated with AWS | 🟡 API Key | ✅ | ✅⭐ |
| [ActiveCampaign](https://developers.activecampaign.com/) | CRM and email automation API for contacts, campaigns, and automations | 🟡 API Key | ✅ | ✅⭐ |
| [Constant Contact](https://developer.constantcontact.com/) | Email campaign creation, scheduling, contact management, and reporting | 🔴 OAuth | ✅ | ✅ |
| [Campaign Monitor](https://www.campaignmonitor.com/api/) | Email campaign API for lists, subscribers, transactional, and journeys | 🟡 API Key | ✅ | ✅ |
| [Kit (ConvertKit)](https://developers.kit.com/v3) | Creator-focused email API for subscribers, broadcasts, and automations | 🟡 API Key | ✅ | ✅ |
| [Resend](https://resend.com/docs/api-reference/introduction) | Modern email API built for developers with React Email support | 🟡 API Key | ✅ | ✅⭐ |
| [SparkPost (Bird)](https://developers.sparkpost.com/) | High-volume email delivery API with analytics and deliverability tools | 🟡 API Key | ✅ | ✅ |
| [Customer.io](https://customer.io/docs/api/track/) | Event-driven email and messaging automation with tracking API | 🟡 API Key | ✅ | ✅⭐ |

---

## 🎪 Event Management & Registration APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Eventbrite API](https://www.eventbrite.com/platform/docs/introduction) | Create and manage events, tickets, attendees, and venues via REST | 🔴 OAuth | ✅ | ✅⭐ |
| [Cvent REST API](https://developers.cvent.com/docs/rest-api/overview) | Enterprise event management with registration, sessions, and contacts | 🔴 OAuth | ✅ | ✅⭐ |
| [Luma API](https://docs.luma.com/reference/getting-started-with-your-api) | Event creation, calendar management, and guest list endpoints | 🟡 API Key | ✅ | ✅⭐ |
| [Bizzabo API](https://bizzabo.api-docs.io/v2.0/events) | B2B event management with attendee, agenda, and analytics endpoints | 🟡 API Key | ✅ | ✅ |
| [Ticket Tailor](https://developers.tickettailor.com/) | Event ticketing API with REST endpoints for events, orders, and tickets | 🟡 API Key | ✅ | ✅⭐ |
| [Splash](https://splashthat.com/) | Branded event marketing platform with attendee management APIs | 🟡 API Key | ✅ | ⚠️ |
| [Jotform](https://api.jotform.com/docs/) | Form and registration API for event sign-ups with data collection | 🟡 API Key | ✅ | ✅⭐ |
| [Meetup API](https://www.meetup.com/api/) | Community event platform with GraphQL API for groups and events | 🔴 OAuth | ✅ | ✅ |
| [Tito](https://ti.to/docs/api/) | Event registration and ticketing with RESTful API for organizers | 🟡 API Key | ✅ | ✅⭐ |
| [Accelevents](https://www.accelevents.com/) | Virtual and hybrid event platform with registration and engagement APIs | 🟡 API Key | ✅ | ⚠️ |
| [Eventzilla](https://www.eventzilla.net/api) | Event registration and ticketing with REST API for attendee management | 🟡 API Key | ✅ | ✅ |
| [RSVPify](https://rsvpify.com/) | Event registration with guest management, seating, and check-in tools | 🟡 API Key | ✅ | ⚠️ |

---

## 🚛 Fleet Management & Telematics APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Samsara](https://developers.samsara.com/docs/rest-api-overview) | Comprehensive fleet API for GPS tracking, diagnostics, and safety data | 🟡 API Key | ✅ | ✅⭐ |
| [Geotab (MyGeotab SDK)](https://developers.geotab.com/) | Language-agnostic API for vehicle tracking, engine data, and driver logs | 🟡 API Key | ✅ | ✅⭐ |
| [Motive (KeepTruckin)](https://developer.gomotive.com/) | Fleet API for ELD, vehicle stats, driver logs, and IFTA reporting | 🟡 API Key | ✅ | ✅⭐ |
| [Fleetio](https://www.fleetio.com/features/developer-api) | Fleet maintenance API with webhooks and data connectors for fleet ops | 🟡 API Key | ✅ | ✅⭐ |
| [Verizon Connect](https://www.verizonconnect.com/services/api-integration/) | Telematics API for GPS, fuel, diagnostics, and driver behavior data | 🟡 API Key | ✅ | ✅ |
| [HERE Fleet Telematics](https://developer.here.com/documentation/fleet-telematics/dev_guide/index.html) | Location-aware routing, geofencing, and fleet optimization REST API | 🟡 API Key | ✅ | ✅⭐ |
| [Trimble Maps Fleet](https://developer.trimblemaps.com/restful-apis/fleet-configuration/) | Fleet configuration, routing, and vehicle settings REST APIs | 🟡 API Key | ✅ | ✅ |
| [Spireon](https://api.spireon.com/doc) | FleetLocate API for GPS tracking, alerts, and vehicle data access | 🟡 API Key | ✅ | ✅ |
| [Teletrac Navman](https://www.teletracnavman.com/) | Fleet GPS tracking with telematics data integration and reporting | 🟡 API Key | ✅ | ⚠️ |
| [Open Telematics API](https://opentelematicsapi.docs.apiary.io/) | Open standard API specification for fleet telematics data exchange | 🟡 API Key | ✅ | ✅ |
| [Azuga](https://www.azuga.com/) | GPS fleet tracking with driver behavior scoring and route optimization | 🟡 API Key | ✅ | ⚠️ |
| [Linxup](https://www.linxup.com/) | GPS tracking API for vehicles and assets with geofencing and alerts | 🟡 API Key | ✅ | ⚠️ |

---

## 📋 Form Builder & Survey APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Typeform](https://developer.typeform.com/) | Create, manage, and retrieve responses from conversational forms and surveys | 🔴 OAuth | ✅ | ✅⭐ |
| [SurveyMonkey](https://api.surveymonkey.com/v3/docs) | Design surveys, collect responses, and analyze results programmatically | 🔴 OAuth | ✅ | ✅⭐ |
| [Google Forms](https://developers.google.com/forms/api/reference/rest) | Programmatically create, read, and manage Google Forms and responses | 🔴 OAuth | ✅ | ✅⭐ |
| [Qualtrics](https://api.qualtrics.com/) | Enterprise experience management with survey creation and analytics APIs | 🟡 API Key | ✅ | ✅ |
| [Formstack](https://developers.formstack.com/) | Build forms, collect data, and automate workflows via REST API | 🔴 OAuth | ✅ | ✅⭐ |
| [JotForm](https://api.jotform.com/docs/) | Create and manage online forms with submission retrieval and reporting | 🟡 API Key | ✅ | ✅⭐ |
| [Cognito Forms](https://www.cognitoforms.com/support/475/data-integration/cognito-forms-api) | Entry-based form data integration with payment support | 🟡 API Key | ✅ | ✅ |
| [SurveyJS](https://surveyjs.io/form-library/documentation/api-reference/survey-data-model) | Self-hosted JSON-based survey and form builder library with full API | 🟢 No | ✅ | ✅⭐ |
| [Alchemer](https://apihelp.alchemer.com/help/version-5-introduction) | Advanced survey platform (formerly SurveyGizmo) with full REST API | 🟡 API Key | ✅ | ✅ |
| [Form.io](https://help.form.io/developers/api) | Self-hosted form builder that auto-generates submission APIs from JSON schemas | 🟡 API Key | ✅ | ✅⭐ |
| [SurveySparrow](https://developers.surveysparrow.com/rest-apis) | Conversational survey platform with omnichannel distribution APIs | 🟡 API Key | ✅ | ✅ |
| [Tally](https://tally.so/help/webhooks) | Simple no-code form builder with webhook-based integrations | 🟢 No | ✅ | ⚠️ |
| [Tripetto](https://tripetto.com/sdk/) | Programmable conversational form builder with embeddable SDK | 🟡 API Key | ✅ | ✅ |

---

## 🛡️ Fraud Detection & Risk Management APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Stripe Radar](https://docs.stripe.com/radar) | AI-powered fraud detection built into Stripe payments with custom rules engine | 🟡 API Key | ✅ | ✅⭐ |
| [Sift](https://developers.sift.com/docs) | Real-time machine learning fraud scoring across payment, content, and account abuse | 🟡 API Key | ✅ | ✅⭐ |
| [IPQualityScore](https://www.ipqualityscore.com/documentation/overview) | Proxy/VPN detection, email verification, phone validation, and fraud scoring | 🟡 API Key | ✅ | ✅⭐ |
| [MaxMind minFraud](https://dev.maxmind.com/minfraud/) | Transaction risk scoring with IP intelligence and device fingerprinting | 🟡 API Key | ✅ | ✅⭐ |
| [Signifyd](https://developer.signifyd.com/) | Guaranteed commerce protection with pre- and post-authorization fraud checks | 🟡 API Key | ✅ | ✅ |
| [Kount](https://developer.kount.com/) | AI-driven digital fraud prevention with device data collection and risk analysis | 🟡 API Key | ✅ | ✅ |
| [Riskified](https://www.riskified.com/documentation/) | E-commerce fraud prevention with chargeback guarantee and ML decisioning | 🟡 API Key | ✅ | ✅ |
| [Fraud.net](https://api-docs.fraud.net/docs/public-apis/b2edb775739e6-api-documentation) | Unified fraud management platform with collective intelligence network | 🟡 API Key | ✅ | ✅ |
| [Amazon Fraud Detector](https://docs.aws.amazon.com/frauddetector/latest/api/Welcome.html) | AWS managed fraud detection service using custom ML models | 🟡 API Key | ✅ | ✅⭐ |
| [SEON](https://docs.seon.io/) | Digital footprint-based fraud prevention with email/phone/IP enrichment | 🟡 API Key | ✅ | ✅⭐ |
| [Emailage (LexisNexis)](https://risk.lexisnexis.com/global/en/products/lexisnexis-emailage) | Email-based risk assessment for identity verification and fraud scoring | 🟡 API Key | ✅ | ✅ |
| [Sardine](https://docs.sardine.ai/) | Behavioral biometrics and device intelligence for real-time fraud monitoring | 🟡 API Key | ✅ | ✅ |
| [APIVoid](https://www.apivoid.com/) | Threat analysis APIs for IP reputation, domain checks, and URL scanning | 🟡 API Key | ✅ | ✅⭐ |

---

## 🎧 Help Desk & ITSM APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Zendesk](https://developer.zendesk.com/api-reference/) | Full-featured support platform with ticketing, help center, and live chat APIs | 🔴 OAuth | ✅ | ✅⭐ |
| [Freshdesk](https://developers.freshdesk.com/api/) | Cloud-based customer support with ticket, contact, and knowledge base management | 🟡 API Key | ✅ | ✅⭐ |
| [Freshservice](https://api.freshservice.com/) | IT service management with incident, problem, change, and asset management APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Jira Service Management](https://developer.atlassian.com/cloud/jira/service-desk/rest/) | Enterprise ITSM with request, queue, SLA, and knowledge base endpoints | 🔴 OAuth | ✅ | ✅⭐ |
| [ServiceNow](https://developer.servicenow.com/dev.do#!/reference) | Enterprise IT workflow automation with REST Table API and scripted APIs | 🔴 OAuth | ✅ | ✅⭐ |
| [HelpDesk](https://api.helpdesk.com/docs) | Simple ticketing system API with automation and team management | 🟡 API Key | ✅ | ✅ |
| [ManageEngine ServiceDesk Plus](https://help.servicedeskplus.com/api/rest-api.html) | IT help desk with CMDB, asset management, and change management APIs | 🟡 API Key | ✅ | ✅ |
| [TOPdesk](https://developers.topdesk.com/) | Service management with incident, change, and asset REST API endpoints | 🟡 API Key | ✅ | ✅ |
| [SysAid](https://documentation.sysaid.com/docs/rest-api-guide) | IT service automation with help desk, asset management, and CMDB APIs | 🟡 API Key | ✅ | ✅ |
| [osTicket](https://docs.osticket.com/en/latest/Developer%20Documentation/API%20Docs.html) | Open-source support ticket system with JSON/XML ticket creation API | 🟡 API Key | ✅ | ⚠️ |
| [SolarWinds Service Desk](https://apidoc.samanage.com/) | IT service management with incident, problem, and change APIs | 🟡 API Key | ✅ | ✅ |
| [HaloITSM](https://halopsa.com/apidoc/) | Unified ITSM platform with tickets, assets, CMDB, and SLA management APIs | 🟡 API Key | ✅ | ✅ |
| [Ivanti Neurons for ITSM](https://help.ivanti.com/ht/help/en_US/ISM/2022/admin/Content/Configure/API/RestAPI-Introduction.htm) | Enterprise ITSM with business object CRUD operations via REST API | 🔴 OAuth | ✅ | ✅ |

---

## 👥 HR & Workforce Management APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [BambooHR](https://documentation.bamboohr.com/docs/getting-started) | HRIS platform with employee data, time-off, and benefits management APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Gusto](https://docs.gusto.com/) | Embedded payroll, benefits, and HR platform with comprehensive REST API | 🔴 OAuth | ✅ | ✅⭐ |
| [Personio](https://developer.personio.de/) | European HR platform with employee, recruiting, and attendance APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Rippling](https://developer.rippling.com/) | Unified workforce platform with HRIS, payroll, and IT management APIs | 🔴 OAuth | ✅ | ✅ |
| [Deel](https://developer.deel.com/) | Global workforce management with EOR, contractor, payroll, and immigration APIs | 🔴 OAuth | ✅ | ✅⭐ |
| [ADP](https://developers.adp.com/) | Enterprise HCM with payroll, HR, time, talent, and benefits APIs | 🔴 OAuth | ✅ | ✅ |
| [UKG Pro (Kronos)](https://developer.ukg.com/) | Workforce management with scheduling, timekeeping, and attendance APIs | 🔴 OAuth | ✅ | ✅ |
| [Sage HR](https://developer.sage.com/hr/reference/api-ref) | HR management with employee records, leave, and performance APIs | 🟡 API Key | ✅ | ✅ |
| [Zendesk WFM](https://developer.zendesk.com/api-reference/wfm/introduction/) | Workforce management with scheduling, forecasting, and adherence APIs | 🔴 OAuth | ✅ | ✅ |
| [Genesys Cloud WFM](https://developer.genesys.cloud/useragentman/workforcemanagement/) | Contact center workforce management with forecasting and scheduling APIs | 🔴 OAuth | ✅ | ✅ |
| [Finch](https://developer.tryfinch.com/) | Unified API connecting 220+ HRIS and payroll systems through one interface | 🟡 API Key | ✅ | ✅⭐ |
| [HiBob](https://apidocs.hibob.com/reference/get_people) | Modern HR platform with people data, time-off, and onboarding APIs | 🟡 API Key | ✅ | ✅ |
| [Paycor](https://developers.paycor.com/explore) | HCM platform with payroll, HR, talent, and workforce management APIs | 🔴 OAuth | ✅ | ✅ |

---

## 🖼️ Image & Video Processing APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Cloudinary](https://cloudinary.com/documentation) | End-to-end image and video management with upload, transform, and delivery APIs | 🟡 API Key | ✅ | ✅⭐ |
| [imgix](https://docs.imgix.com/) | Real-time image processing and CDN delivery via URL-based rendering API | 🟡 API Key | ✅ | ✅⭐ |
| [Mux Video](https://docs.mux.com/api-reference/video) | Video hosting, encoding, streaming, and analytics with simple upload API | 🟡 API Key | ✅ | ✅⭐ |
| [Google Cloud Vision](https://cloud.google.com/vision/docs) | AI-powered image analysis with label detection, OCR, face, and object recognition | 🟡 API Key | ✅ | ✅⭐ |
| [Google Video Intelligence](https://cloud.google.com/video-intelligence/docs) | ML-powered video content analysis with object tracking and scene detection | 🟡 API Key | ✅ | ✅⭐ |
| [Azure Computer Vision](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/) | Image analysis, spatial analysis, and OCR with Azure AI services | 🟡 API Key | ✅ | ✅⭐ |
| [AWS Rekognition](https://docs.aws.amazon.com/rekognition/latest/dg/what-is.html) | Image and video analysis with face detection, content moderation, and custom labels | 🟡 API Key | ✅ | ✅⭐ |
| [Thumbor](https://thumbor.readthedocs.io/) | Open-source smart image cropping and resizing with face detection filters | 🟢 No | ✅ | ✅ |
| [Remove.bg](https://www.remove.bg/api) | AI-powered automatic background removal from images via simple API | 🟡 API Key | ✅ | ✅⭐ |
| [Kraken.io](https://kraken.io/docs/getting-started) | Image optimization and resizing API with lossy and lossless compression | 🟡 API Key | ✅ | ✅ |
| [Shotstack](https://shotstack.io/docs/guide/) | Cloud-based video editing and rendering API using JSON timeline definitions | 🟡 API Key | ✅ | ✅⭐ |
| [api.video](https://docs.api.video/) | Video hosting, live streaming, and delivery API with player customization | 🟡 API Key | ✅ | ✅⭐ |
| [TinyPNG](https://tinypng.com/developers/reference) | Smart PNG and JPEG compression API for web image optimization | 🟡 API Key | ✅ | ✅⭐ |

---

## 🧾 Invoice & Expense Management APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Xero](https://developer.xero.com/documentation/api/accounting/invoices) | Cloud accounting with invoicing, expense claims, and bank reconciliation APIs | 🔴 OAuth | ✅ | ✅⭐ |
| [FreshBooks](https://www.freshbooks.com/api/start) | Small business invoicing and expense tracking with full REST API | 🔴 OAuth | ✅ | ✅⭐ |
| [Zoho Invoice](https://www.zoho.com/invoice/api/v3/introduction/) | Invoicing platform with estimates, payments, and recurring billing APIs | 🔴 OAuth | ✅ | ✅⭐ |
| [QuickBooks Online](https://developer.intuit.com/app/developer/qbo/docs/api/accounting/most-commonly-used/invoice) | Accounting platform with invoice, expense, and payment management APIs | 🔴 OAuth | ✅ | ✅⭐ |
| [Invoiced](https://docs.invoiced.com/dev) | Accounts receivable automation with invoicing, payments, and collection APIs | 🟡 API Key | ✅ | ✅⭐ |
| [SAP Concur](https://developer.concur.com/) | Enterprise expense management with report submission, approval, and receipt APIs | 🔴 OAuth | ✅ | ✅ |
| [Expensify](https://integrations.expensify.com/) | Expense report creation, submission, and export with integration server API | 🟡 API Key | ✅ | ✅ |
| [Wave](https://developer.waveapps.com/hc/en-us/categories/360001114072-Documentation) | Free accounting and invoicing with both REST and GraphQL APIs | 🔴 OAuth | ✅ | ✅ |
| [Harvest](https://help.getharvest.com/api-v2/) | Time tracking and invoicing with project, expense, and invoice APIs | 🔴 OAuth | ✅ | ✅⭐ |
| [Codat](https://docs.codat.io/) | Unified accounting API connecting to Xero, QuickBooks, FreshBooks, and more | 🟡 API Key | ✅ | ✅⭐ |
| [Stripe Invoicing](https://docs.stripe.com/invoicing) | Automated invoice creation, sending, and payment collection via Stripe | 🟡 API Key | ✅ | ✅⭐ |
| [Bill.com](https://developer.bill.com/hc/en-us) | Accounts payable and receivable automation with approval workflow APIs | 🔴 OAuth | ✅ | ✅ |
| [Ramp](https://docs.ramp.com/) | Corporate card and expense management with real-time spend tracking APIs | 🟡 API Key | ✅ | ✅ |

---

## ⚖️ Legal Tech & Case Management APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Clio](https://docs.developers.clio.com/) | Legal practice management with matters, contacts, billing, and document APIs | 🔴 OAuth | ✅ | ✅⭐ |
| [PracticePanther](https://support.practicepanther.com/en/articles/479897-practicepanther-api) | Law firm management with cases, contacts, billing, and task APIs via OAuth 2 | 🔴 OAuth | ✅ | ✅ |
| [MyCase](https://www.mycase.com/blog/cloud-saas-for-lawyers/how-to-use-mycases-open-api-to-get-more-of-your-time-back/) | Case management with client communication, billing, and document APIs | 🟡 API Key | ✅ | ✅ |
| [Actionstep](https://docs.actionstep.com/) | Practice management with workflow automation and matter management REST APIs | 🔴 OAuth | ✅ | ✅ |
| [Rocket Matter](https://developer.rocketmatter.com/) | Legal practice management with time tracking, billing, and contact APIs | 🟡 API Key | ✅ | ✅ |
| [Smokeball](https://docs.smokeball.com/docs/api-docs/1e13a13124aee-introduction) | Practice management with matter, contact, and document REST API endpoints | 🟡 API Key | ✅ | ✅ |
| [case.dev](https://case.dev/) | API platform for legal tech with document processing, search, and AI models | 🟡 API Key | ✅ | ✅ |
| [Rocket Lawyer](https://developer.rocketlawyer.com/apis) | Legal document creation and management with template and signing APIs | 🔴 OAuth | ✅ | ✅ |
| [Lawmatics](https://www.lawmatics.com/integrations) | Legal CRM and intake platform with client management and automation APIs | 🟡 API Key | ✅ | ✅ |
| [OpenLaws](https://openlaws.us/api/) | U.S. legal data API with case law, statutes, and regulatory information | 🟡 API Key | ✅ | ✅⭐ |
| [DocuSign](https://developers.docusign.com/docs/esign-rest-api/) | Electronic signature and agreement management with envelopes and templates APIs | 🔴 OAuth | ✅ | ✅⭐ |
| [LexisNexis](https://developer.lexisnexis.com/) | Legal research and data analytics with case law, statutes, and citation APIs | 🟡 API Key | ✅ | ✅ |

---

## 🌐 Localization & Translation APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [DeepL](https://developers.deepl.com/docs) | High-quality neural machine translation for 33+ languages with glossary support | 🟡 API Key | ✅ | ✅⭐ |
| [Google Cloud Translation](https://cloud.google.com/translate/docs) | Neural machine translation for 100+ languages with language detection | 🟡 API Key | ✅ | ✅⭐ |
| [Microsoft Translator](https://learn.microsoft.com/en-us/azure/ai-services/translator/) | Azure AI translation service with text, document, and custom translation APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Lokalise](https://developers.lokalise.com/reference/lokalise-rest-api) | Translation management with projects, keys, translations, and file import/export APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Phrase](https://developers.phrase.com/) | Localization platform with strings, TMS, and translation workflow management APIs | 🔴 OAuth | ✅ | ✅⭐ |
| [Crowdin](https://support.crowdin.com/developer/api/) | Continuous localization platform with project, file, and translation REST APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Transifex](https://developers.transifex.com/) | Translation management with JSON:API-based resource and project endpoints | 🟡 API Key | ✅ | ✅⭐ |
| [Smartling](https://api-reference.smartling.com/) | Enterprise translation management with file upload, download, and job workflow APIs | 🟡 API Key | ✅ | ✅ |
| [POEditor](https://poeditor.com/docs/api) | Localization management with project, language, and term management API v2 | 🟡 API Key | ✅ | ✅ |
| [Loco (Localise.biz)](https://localise.biz/api) | Translation management with asset, locale, and export REST API endpoints | 🟡 API Key | ✅ | ✅ |
| [SimpleLocalize](https://simplelocalize.io/docs/api/) | Developer-focused translation management with i18n hosting and CDN delivery | 🟡 API Key | ✅ | ✅⭐ |
| [Localize](https://developers.localizejs.com/docs/rest-api) | Website and app localization with content detection and translation APIs | 🟡 API Key | ✅ | ✅ |
| [Amazon Translate](https://docs.aws.amazon.com/translate/latest/dg/what-is.html) | AWS neural machine translation with real-time and batch translation APIs | 🟡 API Key | ✅ | ✅⭐ |

---

## 📈 Marketing Attribution & Analytics APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Google Analytics Data API](https://developers.google.com/analytics/devguides/reporting/data/v1) | Query GA4 property data for reports on traffic, conversions, and user behavior | 🔴 OAuth | ✅ | ✅⭐ |
| [Mixpanel](https://developer.mixpanel.com/) | Product analytics with event ingestion, user profiles, and funnel query APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Segment](https://segment.com/docs/api/public-api/) | Customer data platform with source, destination, and tracking plan management APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Amplitude](https://amplitude.com/docs/apis/analytics/attribution) | Product analytics with attribution, event taxonomy, and behavioral cohort APIs | 🟡 API Key | ✅ | ✅⭐ |
| [AppsFlyer](https://dev.appsflyer.com/hc/docs) | Mobile attribution and marketing analytics with install and in-app event APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Adjust](https://dev.adjust.com/en/api/) | Mobile attribution with server-to-server callbacks and aggregated reporting APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Branch](https://help.branch.io/developers-hub/reference/branch-links-api-overview) | Deep linking and mobile attribution with link creation and analytics APIs | 🟡 API Key | ✅ | ✅ |
| [HubSpot Marketing](https://developers.hubspot.com/docs/api-reference/overview) | Inbound marketing with email, campaign, analytics, and attribution APIs | 🔴 OAuth | ✅ | ✅⭐ |
| [Adobe Analytics](https://developer.adobe.com/analytics-apis/docs/2.0/) | Enterprise analytics with reporting, segmentation, and attribution modeling APIs | 🔴 OAuth | ✅ | ✅ |
| [Singular](https://developers.singular.net/) | Marketing analytics with cross-platform attribution, ROI, and fraud prevention APIs | 🟡 API Key | ✅ | ✅ |
| [Kochava](https://support.kochava.com/reference-information/kochava-api/) | Mobile attribution with install, event, and audience-building REST APIs | 🟡 API Key | ✅ | ✅ |
| [Matomo](https://developer.matomo.org/api-reference/reporting-api) | Open-source web analytics with visitor, action, and goal reporting APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Plausible Analytics](https://plausible.io/docs/stats-api) | Privacy-friendly web analytics with aggregate stats and time-series APIs | 🟡 API Key | ✅ | ✅⭐ |

---

## 🖥️ Network & Infrastructure Monitoring APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Datadog](https://docs.datadoghq.com/api/latest/) | Full-stack observability with metrics, logs, traces, and dashboard management APIs | 🟡 API Key | ✅ | ✅⭐ |
| [New Relic](https://docs.newrelic.com/docs/apis/intro-apis/introduction-new-relic-apis/) | Application and infrastructure monitoring with NerdGraph (GraphQL) and REST APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Zabbix](https://www.zabbix.com/documentation/current/en/manual/api) | Open-source monitoring with host, item, trigger, and template JSON-RPC APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Nagios XI](https://www.nagios.com/products/nagios-xi/) | Infrastructure monitoring with host/service status and configuration REST APIs | 🟡 API Key | ✅ | ✅ |
| [PRTG Network Monitor](https://www.paessler.com/manuals/prtg/application_programming_interface_api_definition) | Network monitoring with sensor data, device management, and alerting REST APIs | 🟡 API Key | ✅ | ✅ |
| [UptimeRobot](https://uptimerobot.com/api/) | Website uptime monitoring with monitor CRUD, alert contacts, and status page APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Prometheus](https://prometheus.io/docs/prometheus/latest/querying/api/) | Open-source time-series monitoring with PromQL query and metadata HTTP APIs | 🟢 No | ✅ | ✅⭐ |
| [Grafana](https://grafana.com/docs/grafana/latest/developers/http_api/) | Observability dashboarding with data source, dashboard, and alerting REST APIs | 🟡 API Key | ✅ | ✅⭐ |
| [PagerDuty](https://developer.pagerduty.com/api-reference/) | Incident management with event routing, escalation, and on-call schedule APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Pingdom](https://docs.pingdom.com/api/) | Website performance monitoring with uptime, page speed, and transaction check APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Site24x7](https://www.site24x7.com/help/api/) | Cloud monitoring with server, network, application, and website monitoring APIs | 🟡 API Key | ✅ | ✅ |
| [Dynatrace](https://docs.dynatrace.com/docs/dynatrace-api) | AI-powered observability with entity, metrics, events, and topology APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Cisco ACI](https://developer.cisco.com/docs/aci/) | Data center network infrastructure management and monitoring REST APIs | 🟡 API Key | ✅ | ✅ |

---

## 🧩 No-Code & Low-Code Platform APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Airtable](https://airtable.com/developers/web/api) | Spreadsheet-database hybrid with record CRUD and metadata REST APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Bubble](https://manual.bubble.io/core-resources/api) | No-code app builder with Data API for database operations and Workflow API | 🟡 API Key | ✅ | ✅ |
| [Retool](https://docs.retool.com/api/) | Internal tool builder with organization management and resource configuration APIs | 🟡 API Key | ✅ | ✅ |
| [Zapier](https://platform.zapier.com/) | Workflow automation platform with integration builder and embedded editor APIs | 🔴 OAuth | ✅ | ✅⭐ |
| [Make (Integromat)](https://www.make.com/en/api-documentation) | Visual automation platform with scenario, connection, and webhook management APIs | 🟡 API Key | ✅ | ✅ |
| [n8n](https://docs.n8n.io/api/) | Open-source workflow automation with execution, credential, and workflow REST APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Xano](https://docs.xano.com/) | No-code backend builder with auto-generated CRUD APIs and custom function stacks | 🟡 API Key | ✅ | ✅⭐ |
| [Appsmith](https://docs.appsmith.com/) | Open-source low-code platform for building internal tools with API data sources | 🟡 API Key | ✅ | ✅⭐ |
| [Notion](https://developers.notion.com/) | Connected workspace with database, page, block, and user management REST APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Google AppSheet](https://cloud.google.com/appsheet/docs) | No-code app builder on Google Cloud with data connectors and automation APIs | 🔴 OAuth | ✅ | ✅ |
| [OutSystems](https://success.outsystems.com/documentation/11/reference/outsystems_apis/) | Enterprise low-code platform with app lifecycle, deployment, and runtime APIs | 🟡 API Key | ✅ | ✅ |
| [Directus](https://docs.directus.io/reference/introduction.html) | Open-source headless CMS with auto-generated REST and GraphQL APIs for any database | 🟡 API Key | ✅ | ✅⭐ |
| [NocoDB](https://docs.nocodb.com/developer-resources/rest-APIs/overview/) | Open-source Airtable alternative that auto-generates REST APIs from databases | 🟡 API Key | ✅ | ✅⭐ |

---

## 📄 OCR & Document Intelligence APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Google Document AI](https://cloud.google.com/document-ai/docs) | Enterprise document processing with OCR, form parsing, and entity extraction | 🟡 API Key | ✅ | ✅⭐ |
| [Azure AI Document Intelligence](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/) | Pre-built and custom document models for invoices, receipts, IDs, and forms | 🟡 API Key | ✅ | ✅⭐ |
| [AWS Textract](https://docs.aws.amazon.com/textract/latest/dg/what-is.html) | ML-powered text, table, and form extraction from scanned documents | 🟡 API Key | ✅ | ✅⭐ |
| [ABBYY Cloud OCR](https://www.abbyy.com/ai-document-processing/api/) | Enterprise OCR with 200+ language support and document classification APIs | 🟡 API Key | ✅ | ✅ |
| [Mindee](https://developers.mindee.com/docs) | API-first document parsing for invoices, receipts, passports, and custom models | 🟡 API Key | ✅ | ✅⭐ |
| [Nanonets](https://nanonets.com/documentation/) | AI-powered OCR with pre-trained models for invoices, tables, and custom documents | 🟡 API Key | ✅ | ✅⭐ |
| [Rossum](https://elis.rossum.ai/api/docs/) | AI document processing platform optimized for invoice and purchase order extraction | 🟡 API Key | ✅ | ✅ |
| [Docparser](https://docparser.com/api) | Template-based document parsing for extracting fields from PDFs and images | 🟡 API Key | ✅ | ✅ |
| [Klippa](https://www.klippa.com/en/ocr/ocr-api/) | OCR API for receipts, invoices, passports, and contracts with JSON output | 🟡 API Key | ✅ | ✅ |
| [Mistral OCR](https://docs.mistral.ai/) | LLM-powered OCR at scale with high-accuracy document understanding | 🟡 API Key | ✅ | ✅⭐ |
| [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) | Open-source OCR engine supporting 100+ languages with trainable models | 🟢 No | ✅ | ⚠️ |
| [Google Cloud Vision OCR](https://cloud.google.com/vision/docs/ocr) | Detect and extract text from images with handwriting and multi-language support | 🟡 API Key | ✅ | ✅⭐ |
| [OCR.space](https://ocr.space/ocrapi) | Free hosted OCR API with multi-language support and table recognition | 🟡 API Key | ✅ | ✅⭐ |

---

## 💰 Payroll & Tax Filing APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Gusto Embedded Payroll](https://docs.gusto.com/) | Full-service payroll with employee, pay schedule, tax, and benefits APIs | 🔴 OAuth | ✅ | ✅⭐ |
| [Check (Checkr Payroll)](https://docs.checkhq.com/docs/overview) | Payroll infrastructure API handling taxes, money movement, and W-2 filings | 🟡 API Key | ✅ | ✅⭐ |
| [ADP Payroll](https://developers.adp.com/) | Enterprise payroll processing with tax filing, garnishments, and pay statement APIs | 🔴 OAuth | ✅ | ✅ |
| [Paychex](https://developer.paychex.com/) | Payroll and HCM with employee, pay component, and check management APIs | 🔴 OAuth | ✅ | ✅ |
| [Paycor](https://developers.paycor.com/explore) | Payroll platform with earnings, deductions, and tax information APIs | 🔴 OAuth | ✅ | ✅ |
| [TaxBandits](https://developer.taxbandits.com/) | IRS e-filing API for W-2, 1099, 940, 941, and ACA forms with TIN matching | 🟡 API Key | ✅ | ✅⭐ |
| [Vertex Payroll Tax](https://developer.vertexinc.com/payroll) | Precise payroll tax calculation for U.S. and Canada via RESTful APIs | 🟡 API Key | ✅ | ✅ |
| [Avalara](https://developer.avalara.com/) | Tax compliance with payroll tax registration, sales tax calculation, and filing APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Finch](https://developer.tryfinch.com/) | Unified payroll API connecting 220+ HRIS and payroll providers in one interface | 🟡 API Key | ✅ | ✅⭐ |
| [Rippling](https://developer.rippling.com/) | Modern payroll with global payment processing, tax filing, and compliance APIs | 🔴 OAuth | ✅ | ✅ |
| [Deel](https://developer.deel.com/) | Global payroll for contractors and employees in 150+ countries with tax support | 🔴 OAuth | ✅ | ✅⭐ |
| [QuickBooks Payroll](https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/employee) | Small business payroll with employee management, pay runs, and tax forms APIs | 🔴 OAuth | ✅ | ✅ |

---

## 📦 Product Information Management APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Akeneo](https://api.akeneo.com/) | Open-source PIM with product, category, attribute, and media REST API endpoints | 🔴 OAuth | ✅ | ✅⭐ |
| [Salsify](https://developers.salsify.com/) | Product experience management with records, digital assets, and export APIs | 🟡 API Key | ✅ | ✅ |
| [Pimberly](https://apidocs.pimberly.com/) | Enterprise PIM with product data, channel syndication, and workflow APIs | 🟡 API Key | ✅ | ✅ |
| [Plytix](https://apidocs.plytix.com/) | PIM platform with product, asset, relationship, and feed management APIs | 🟡 API Key | ✅ | ✅ |
| [Erply PIM](https://learn-api.erply.com/new-apis/pim-api) | Retail PIM with product, assortment, and parameter management REST APIs | 🟡 API Key | ✅ | ✅ |
| [Pimcore](https://pimcore.com/docs/pimcore/current/Development_Documentation/Web_Services/index.html) | Open-source digital platform with PIM, DAM, and CMS APIs and data objects | 🟡 API Key | ✅ | ✅⭐ |
| [Contentful](https://www.contentful.com/developers/docs/references/) | Headless CMS with content delivery, management, and preview REST/GraphQL APIs | 🟡 API Key | ✅ | ✅⭐ |
| [PIMinto](https://piminto.com/api) | PIM API serving structured product data directly to channels and visitors | 🟡 API Key | ✅ | ✅ |
| [inRiver](https://apidoc.inriver.com/) | Product marketing cloud with entity, link, and media management REST APIs | 🟡 API Key | ✅ | ✅ |
| [Shopify Products](https://shopify.dev/docs/api/admin-rest/current/resources/product) | E-commerce product management with variants, images, and collection APIs | 🔴 OAuth | ✅ | ✅⭐ |
| [BigCommerce Catalog](https://developer.bigcommerce.com/docs/rest-catalog) | E-commerce catalog with product, category, brand, and variant REST APIs | 🔴 OAuth | ✅ | ✅⭐ |
| [Algolia](https://www.algolia.com/doc/rest-api/search/) | Search and discovery API for product catalogs with faceting and personalization | 🟡 API Key | ✅ | ✅⭐ |

---

## 📋 Project Management & Collaboration APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Asana](https://developers.asana.com/) | Work management with tasks, projects, sections, portfolios, and goals REST APIs | 🔴 OAuth | ✅ | ✅⭐ |
| [Monday.com](https://developer.monday.com/api-reference/) | Work OS with boards, items, columns, and updates via GraphQL API | 🔴 OAuth | ✅ | ✅⭐ |
| [ClickUp](https://developer.clickup.com/) | All-in-one productivity with tasks, spaces, lists, and time tracking REST APIs | 🔴 OAuth | ✅ | ✅⭐ |
| [Notion](https://developers.notion.com/) | Connected workspace with databases, pages, blocks, and comments REST APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Wrike](https://developers.wrike.com/) | Enterprise work management with tasks, folders, projects, and timelog APIs | 🔴 OAuth | ✅ | ✅⭐ |
| [Basecamp](https://github.com/basecamp/bc3-api) | Project management with to-dos, message boards, schedules, and campfire REST APIs | 🔴 OAuth | ✅ | ✅ |
| [Trello](https://developer.atlassian.com/cloud/trello/rest/) | Kanban-style boards with cards, lists, labels, and checklists REST APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Jira](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/) | Agile project tracking with issues, sprints, boards, and workflow REST APIs | 🔴 OAuth | ✅ | ✅⭐ |
| [Linear](https://developers.linear.app/docs/graphql/working-with-the-graphql-api) | Modern issue tracking with issues, projects, cycles, and teams GraphQL API | 🔴 OAuth | ✅ | ✅⭐ |
| [Todoist](https://developer.todoist.com/rest/v2/) | Task management with projects, sections, labels, and comments REST API | 🔴 OAuth | ✅ | ✅⭐ |
| [GitLab Projects](https://docs.gitlab.com/ee/api/projects.html) | DevOps platform with project, issue, merge request, and pipeline REST APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Smartsheet](https://smartsheet.redoc.ly/) | Enterprise work management with sheets, rows, columns, and attachment APIs | 🟡 API Key | ✅ | ✅⭐ |
| [ProjectManager.com](https://developer.projectmanager.com/) | Project and portfolio management with tasks, timesheets, and resource APIs | 🟡 API Key | ✅ | ✅ |

---

## 🏠 Property & Real Estate APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Zillow (Bridge/Zestimates)](https://www.zillowgroup.com/developers/) | Property valuations, listings, and market data from Zillow Group's 20+ APIs | 🟡 API Key | ✅ | ✅ |
| [ATTOM Data](https://api.developer.attomdata.com/docs) | Property data on 155M+ U.S. properties with sales, tax, mortgage, and AVM data | 🟡 API Key | ✅ | ✅⭐ |
| [RealEstateAPI](https://developer.realestateapi.com/) | Property data, MLS listings, valuations, boundaries, and SkipTrace APIs | 🟡 API Key | ✅ | ✅⭐ |
| [RentCast](https://www.rentcast.io/api) | Rental market data with property records, rent estimates, and market statistics | 🟡 API Key | ✅ | ✅⭐ |
| [HouseCanary](https://api-docs.housecanary.com/) | Property analytics with ML-powered valuations, market forecasts, and risk scores | 🟡 API Key | ✅ | ✅⭐ |
| [Bridge Interactive](https://www.bridgeinteractive.com/developers/) | Normalized MLS listing data with RESO-compliant real estate data access | 🟡 API Key | ✅ | ✅ |
| [Estated](https://estated.com/developers) | Real-time property data and valuations covering U.S. residential properties | 🟡 API Key | ✅ | ✅⭐ |
| [SimplyRETS](https://docs.simplyrets.com/) | MLS listing data API for building real estate websites and applications | 🟡 API Key | ✅ | ✅⭐ |
| [Pubrec (PropMix)](https://pubrec.propmix.io/) | Public record APIs for property, tax, assessment, mortgage, and deed data | 🟡 API Key | ✅ | ✅ |
| [Datafiniti (Real Estate)](https://developer.datafiniti.co/) | Property listing aggregation with sale/rental data and historical pricing APIs | 🟡 API Key | ✅ | ✅ |
| [Mashvisor](https://www.mashvisor.com/api-doc/) | Investment property analytics with rental income, occupancy, and ROI APIs | 🟡 API Key | ✅ | ✅ |
| [Precisely (Property)](https://developer.precisely.com/) | Property attributes, boundaries, risk scores, and neighborhood data APIs | 🟡 API Key | ✅ | ✅ |
| [CoreLogic](https://www.corelogic.com/data-solutions/property-data-solutions/) | Property intelligence with AVM, ownership, tax, and MLS data APIs | 🟡 API Key | ✅ | ✅ |

---

## 📄 Proposal & Quote Management APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [PandaDoc](https://developers.pandadoc.com/) | Create, send, sign, and manage documents and proposals via REST API | 🔴 OAuth | ✅ | ✅⭐ |
| [Proposify](https://www.proposify.com/platform/api) | Automate proposal creation, send documents, and manage prospect information | 🟡 API Key | ✅ | ✅ |
| [Qwilr](https://docs.qwilr.com/) | Automate smart document creation with templates, tokens, and page management | 🟡 API Key | ✅ | ✅⭐ |
| [Better Proposals](https://betterproposals.io/resources/api/) | Manage proposals, templates, companies, and track proposal status via REST | 🟡 API Key | ✅ | ✅ |
| [DocSend](https://www.docsend.com/integrations/) | Track document engagement, manage links, and monitor visitor analytics | 🟡 API Key | ✅ | ✅ |
| [Nusii](https://developer.nusii.com/) | Create and manage proposals with clients, templates, and sections via JSON API | 🟡 API Key | ✅ | ✅⭐ |
| [QuoteWerks](https://www.quotewerks.com/sdk.asp) | COM-based API and SDK for quoting automation and document management | 🟡 API Key | ✅ | ⚠️ |
| [ConnectWise CPQ](https://developer.connectwise.com/) | Configure, price, and quote integration across ConnectWise product suite | 🟡 API Key | ✅ | ✅ |
| [DealHub](https://developers.dealhub.io/docs/introduction-to-dealhub-apis) | CPQ and quote-to-cash ecosystem with headless quoting and deal management | 🔴 OAuth | ✅ | ✅ |
| [Responsive](https://developer.responsive.io/) | Manage RFP/RFI response projects, content library, and user workflows | 🟡 API Key | ✅ | ✅ |
| [Bidsketch](https://www.bidsketch.com/) | Create and deliver professional client proposals with e-signatures | 🟡 API Key | ✅ | ⚠️ |
| [RFPIO](https://developer.responsive.io/) | Automate response management for RFPs, RFIs, and security questionnaires | 🟡 API Key | ✅ | ✅ |

---

## 🧪 Quality Assurance & Testing APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Sauce Labs](https://docs.saucelabs.com/dev/api/) | Cross-browser and mobile testing with REST APIs for jobs, tunnels, and devices | 🟡 API Key | ✅ | ✅⭐ |
| [BrowserStack](https://www.browserstack.com/docs/) | Automate browser and real device testing with session management APIs | 🟡 API Key | ✅ | ✅⭐ |
| [LambdaTest](https://www.lambdatest.com/support/docs/) | Cloud cross-browser testing with Selenium, Appium, and Smart UI automation APIs | 🟡 API Key | ✅ | ✅ |
| [Applitools](https://applitools.com/docs/) | AI-powered visual testing and monitoring with Eyes SDKs and REST APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Percy](https://www.browserstack.com/docs/percy/api-reference/percy-apis) | Visual testing and review platform with snapshot comparison and CI/CD integration | 🟡 API Key | ✅ | ✅ |
| [Testim](https://help.testim.io/docs/api-access) | AI-powered test authoring and execution with REST API and branch management | 🟡 API Key | ✅ | ✅ |
| [Mabl](https://help.mabl.com/) | AI-driven testing platform for API, UI, and performance testing automation | 🟡 API Key | ✅ | ✅ |
| [Rainforest QA](https://help.rainforestqa.com/) | No-code QA automation platform with API for test runs and integrations | 🟡 API Key | ✅ | ✅ |
| [TestRail](https://support.testrail.com/hc/en-us/categories/7076541806228-API-Manual) | Test case management with HTTP-based API for cases, runs, results, and plans | 🟡 API Key | ✅ | ✅⭐ |
| [Zephyr Scale](https://support.smartbear.com/zephyr-scale-cloud/api-docs/) | Jira-integrated test management with REST API for cases, cycles, and executions | 🟡 API Key | ✅ | ✅ |
| [qTest](https://qtest.dev.tricentis.com/) | Enterprise test management by Tricentis with interactive Swagger-based API docs | 🟡 API Key | ✅ | ✅ |
| [PractiTest](https://www.practitest.com/api-v2/) | Test management platform with JSON API for projects, tests, runs, and automation | 🟡 API Key | ✅ | ✅⭐ |

---

## 👔 Recruitment & ATS APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Greenhouse](https://developers.greenhouse.io/) | Full-featured ATS with Harvest, Job Board, Ingestion, and Assessment APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Lever](https://hire.lever.co/developer/documentation) | Modern ATS with REST API for candidates, opportunities, and job postings | 🔴 OAuth | ✅ | ✅⭐ |
| [Workable](https://workable.readme.io/) | Recruiting platform API for jobs, candidates, stages, and activity management | 🟡 API Key | ✅ | ✅⭐ |
| [SmartRecruiters](https://developers.smartrecruiters.com/) | Enterprise ATS with Application, Customer, and Interview APIs | 🔴 OAuth | ✅ | ✅ |
| [JazzHR](https://apidoc.jazzhrapis.com/) | SMB recruiting software with API for applicants, jobs, and hiring workflows | 🟡 API Key | ✅ | ✅ |
| [Breezy HR](https://developer.breezy.hr/) | Modern recruiting platform with REST API v3 for positions, candidates, and flows | 🟡 API Key | ✅ | ✅ |
| [Recruitee](https://docs.recruitee.com/reference/getting-started) | Collaborative hiring platform with Careers Site and ATS REST APIs | 🟡 API Key | ✅ | ✅ |
| [Ashby](https://developers.ashbyhq.com/) | All-in-one recruiting platform with RESTful API for jobs, candidates, and offers | 🟡 API Key | ✅ | ✅⭐ |
| [Teamtailor](https://docs.teamtailor.com/) | Employer branding and ATS with JSON API spec-compliant REST interface | 🟡 API Key | ✅ | ✅ |
| [Pinpoint](https://developers.pinpointhq.com/docs/introduction) | Applicant tracking with JSON API spec REST endpoints for recruitment data | 🟡 API Key | ✅ | ✅ |
| [Jobvite](https://help.jobvite.com/hc/en-us/articles/8870636608925-Jobvite-API) | Enterprise recruiting suite with REST and SOAP APIs for candidates and jobs | 🟡 API Key | ✅ | ⚠️ |

---

## 🖥️ Remote Desktop & Access APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [TeamViewer](https://webapi.teamviewer.com/api/v1/docs/index) | Remote desktop and device management with OAuth 2.0 REST API | 🔴 OAuth | ✅ | ✅⭐ |
| [AnyDesk](https://anydesk.com/en/features/rest-api) | Remote access REST API for session data, billing automation, and device management | 🟡 API Key | ✅ | ✅ |
| [Splashtop](https://support-splashtopbusiness.splashtop.com/hc/en-us/articles/16772899906459) | Remote support and access APIs for session logs, file transfers, and automation | 🔴 OAuth | ✅ | ✅ |
| [ConnectWise Control](https://developer.connectwise.com/Products/ConnectWise_ScreenConnect) | ScreenConnect remote support with Session Manager API and RESTful endpoints | 🟡 API Key | ✅ | ✅ |
| [BeyondTrust](https://docs.beyondtrust.com/pra/docs/api) | Privileged remote access and support with OpenAPI-standard REST API | 🔴 OAuth | ✅ | ✅ |
| [Datto RMM](https://rmm.datto.com/help/en/Content/2SETUP/APIv2.htm) | Remote monitoring and management REST API v2 with Swagger documentation | 🔴 OAuth | ✅ | ✅ |
| [NinjaOne](https://app.ninjarmm.com/apidocs/) | IT management platform with comprehensive Public API 2.0 for RMM operations | 🔴 OAuth | ✅ | ✅⭐ |
| [Atera](https://support.atera.com/hc/en-us/articles/219083397-APIs) | All-in-one IT management with Swagger V3-powered REST API for tickets and devices | 🟡 API Key | ✅ | ✅ |
| [GoTo Resolve](https://developer.goto.com/LogMeInResolve) | Remote IT support and management with REST API for customized integrations | 🔴 OAuth | ✅ | ✅ |
| [Zoho Assist](https://www.zoho.com/assist/api/introduction.html) | Remote support and access with OAuth 2.0 REST API and embeddable widgets | 🔴 OAuth | ✅ | ✅ |
| [Level.io](https://level.io/) | Modern remote access platform with endpoint management and automation APIs | 🟡 API Key | ✅ | ✅ |
| [LogMeIn](https://developer.goto.com/) | Remote access and support tools via GoTo developer center REST APIs | 🔴 OAuth | ✅ | ⚠️ |

---

## ⭐ Reputation & Review Management APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Trustpilot](https://developers.trustpilot.com/) | Service and product reviews with invitation, resources, and review APIs | 🔴 OAuth | ✅ | ✅⭐ |
| [G2](https://data.g2.com/api/docs) | B2B software reviews API for products, categories, and review data syndication | 🔴 OAuth | ✅ | ✅ |
| [Yotpo](https://apidocs.yotpo.com/reference/welcome) | UGC, reviews, and loyalty platform with Core, Reviews, and App Developer APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Bazaarvoice](https://developer.bazaarvoice.com/) | Ratings, reviews, Q&A, and UGC with Conversations and Response REST APIs | 🟡 API Key | ✅ | ✅ |
| [Birdeye](https://developers.birdeye.com/) | Online reputation and customer experience management with RESTful APIs | 🟡 API Key | ✅ | ✅ |
| [Podium](https://docs.podium.com/docs/getting-started) | Customer interaction platform with OAuth 2.0 API for messaging and reviews | 🔴 OAuth | ✅ | ✅ |
| [ReviewTrackers](https://www.reviewtrackers.com/blog/api-integrations/) | Online reputation management with API for review data and reporting sync | 🟡 API Key | ✅ | ⚠️ |
| [Reputation.com](https://apidocs.reputation.com/) | Enterprise reputation management with REST API for feedback and metrics | 🟡 API Key | ✅ | ✅ |
| [Stamped.io](https://developers.stamped.io/) | Product reviews, Q&A, NPS, and loyalty with REST API and webhook support | 🟡 API Key | ✅ | ✅⭐ |
| [Judge.me](https://judge.me/api/docs) | Shopify product reviews with OpenAPI-compliant REST API for review management | 🟡 API Key | ✅ | ✅⭐ |
| [Capterra](https://www.capterra.com/) | Software review aggregation platform with partner data feeds and syndication | 🟡 API Key | ✅ | ⚠️ |
| [Grade.us](https://grade.us/) | Review management and marketing platform with API for multi-location review flow | 🟡 API Key | ✅ | ⚠️ |

---

## 🏪 Retail & POS APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Shopify POS](https://shopify.dev/docs/api/pos-ui-extensions/latest) | Unified commerce POS with App Bridge, UI Extensions, and Admin REST/GraphQL APIs | 🔴 OAuth | ✅ | ✅⭐ |
| [Square](https://developer.squareup.com/) | Full commerce platform with Payments, Orders, Catalog, Terminal, and POS APIs | 🔴 OAuth | ✅ | ✅⭐ |
| [Lightspeed](https://developers.retail.lightspeed.app/) | Multi-series retail POS with R-Series and X-Series REST APIs for inventory and sales | 🔴 OAuth | ✅ | ✅ |
| [Vend (X-Series)](https://x-series-api.lightspeedhq.com/) | Cloud retail POS with REST API for products, sales, customers, and registers | 🔴 OAuth | ✅ | ✅ |
| [Toast](https://doc.toasttab.com/doc/devguide/index.html) | Restaurant POS platform with Orders, Menus, Payments, and Configuration APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Clover](https://docs.clover.com/dev/docs/home) | Open commerce platform with REST API and Pay Display API for SMB merchants | 🔴 OAuth | ✅ | ✅⭐ |
| [Revel Systems](https://developer.revelsystems.com/) | Enterprise POS with ~140 public REST API endpoints for orders, products, and payments | 🟡 API Key | ✅ | ✅ |
| [Heartland](https://developer.heartlandpaymentsystems.com/) | Payment processing and POS integration with REST APIs for retail transactions | 🟡 API Key | ✅ | ✅ |
| [NCR Voyix](https://developer.ncrvoyix.com/) | Enterprise retail and restaurant POS with Order, Catalog, and Sites APIs | 🔴 OAuth | ✅ | ✅ |
| [Oracle Retail](https://docs.oracle.com/en/industries/retail/) | Enterprise merchandising with 300+ REST APIs for retail operations management | 🔴 OAuth | ✅ | ⚠️ |
| [SAP Retail](https://api.sap.com/) | Enterprise retail management with RESTful APIs via SAP Business Accelerator Hub | 🔴 OAuth | ✅ | ⚠️ |
| [Retail Pro](https://www.retailpro.com/) | Specialty retail POS with integration APIs for multi-store operations | 🟡 API Key | ✅ | ⚠️ |

---

## 🔒 SIEM & Security Operations APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Splunk](https://dev.splunk.com/enterprise/docs) | Enterprise SIEM with REST API for search, alerting, and security analytics | 🟡 API Key | ✅ | ✅⭐ |
| [IBM QRadar](https://ibmsecuritydocs.github.io/qradar_api_overview/) | Enterprise SIEM with RESTful API for offenses, searches, and reference data | 🟡 API Key | ✅ | ✅ |
| [Microsoft Sentinel](https://learn.microsoft.com/en-us/rest/api/securityinsights/) | Cloud SIEM with REST APIs for incidents, rules, bookmarks, and data connectors | 🔴 OAuth | ✅ | ✅⭐ |
| [Elastic Security](https://www.elastic.co/guide/en/security/current/security-apis.html) | Open-source SIEM with Detections, Entity Analytics, and Kibana REST APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Sumo Logic](https://api.sumologic.com/docs/) | Cloud SIEM and analytics with REST API for collectors, sources, and searches | 🟡 API Key | ✅ | ✅ |
| [LogRhythm](https://developers.exabeam.com/logrhythm-siem/) | SIEM with REST API for administration, investigation, and search functions | 🟡 API Key | ✅ | ✅ |
| [Exabeam](https://developers.exabeam.com/exabeam) | Next-gen SIEM with developer portal for threat detection and response APIs | 🟡 API Key | ✅ | ✅ |
| [Securonix](https://documentation.securonix.com/) | UEBA and SIEM with API for threat analysis, alerts, and incident response | 🟡 API Key | ✅ | ⚠️ |
| [Devo](https://docs.devo.com/) | Cloud-native SIEM with REST API for alerting, analysis, enrichment, and queries | 🟡 API Key | ✅ | ✅ |
| [Chronicle (Google SecOps)](https://cloud.google.com/chronicle/docs) | Google cloud SIEM with Ingestion and Search APIs for security telemetry | 🔴 OAuth | ✅ | ✅ |
| [Rapid7 InsightIDR](https://docs.rapid7.com/insightidr/insightidr-rest-api/) | Cloud SIEM with REST API for investigations, detections, alerts, and log search | 🟡 API Key | ✅ | ✅ |
| [AlienVault OTX](https://otx.alienvault.com/api) | Open threat exchange with REST API for threat intelligence indicators and pulses | 🟡 API Key | ✅ | ✅ |

---

## 🏠 Smart Home & IoT Hub APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [SmartThings](https://developer.smartthings.com/docs/api/public) | Samsung IoT platform with RESTful API for devices, automations, and locations | 🔴 OAuth | ✅ | ✅⭐ |
| [Home Assistant](https://developers.home-assistant.io/docs/api/rest/) | Open-source home automation with REST API for states, services, and events | 🟡 API Key | ✅ | ✅⭐ |
| [Tuya](https://developer.tuya.com/en/docs/iot/open-apis?id=Kaiuyvvxud2le) | IoT cloud platform with OpenAPIs for device management, control, and scenes | 🟡 API Key | ✅ | ✅ |
| [Hubitat](https://docs2.hubitat.com/en/developer) | Local-processing smart home hub with Maker API for device control and events | 🟡 API Key | ✅ | ✅ |
| [Apple HomeKit](https://developer.apple.com/homekit/) | Apple smart home framework with HomeKit Accessory Protocol and Matter support | 🔴 OAuth | ✅ | ⚠️ |
| [Google Home](https://developers.home.google.com/) | Google smart home ecosystem with Device Access API and Matter integration | 🔴 OAuth | ✅ | ✅ |
| [Amazon Alexa](https://developer.amazon.com/en-US/docs/alexa/smarthome/understand-the-smart-home-skill-api.html) | Smart Home Skill API with capability interfaces for device control via Alexa | 🔴 OAuth | ✅ | ✅ |
| [IFTTT](https://ifttt.com/docs/connect_api) | Automation platform with Webhooks and Connect API for 750+ service integrations | 🟡 API Key | ✅ | ✅ |
| [Philips Hue](https://developers.meethue.com/) | Smart lighting with REST API v2 for lights, rooms, scenes, and entertainment | 🟡 API Key | ✅ | ✅⭐ |
| [Wyze](https://developer-api-console.wyze.com/) | Smart home devices with developer API console and Python SDK for cameras and locks | 🟡 API Key | ✅ | ⚠️ |
| [Ecobee](https://www.ecobee.com/en-us/developers/) | Smart thermostat with OAuth 2.0 REST API for climate control and scheduling | 🔴 OAuth | ✅ | ✅ |
| [Ring](https://python-ring-doorbell.readthedocs.io/) | Smart security devices with community-maintained APIs for doorbells and cameras | 🟡 API Key | ✅ | ⚠️ |

---

## 📱 Social Media Management APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Hootsuite](https://developer.hootsuite.com/) | Social media management with REST API for publishing, scheduling, and analytics | 🔴 OAuth | ✅ | ✅⭐ |
| [Buffer](https://buffer.com/developers/api) | Social media scheduling with REST API for profiles, updates, and publishing | 🔴 OAuth | ✅ | ✅ |
| [Sprout Social](https://api.sproutsocial.com/docs/) | Enterprise social management with REST API for analytics, posts, and messages | 🔴 OAuth | ✅ | ✅ |
| [Later](https://docs.getlate.dev/) | Unified social media API for scheduling across 13 platforms with one endpoint | 🟡 API Key | ✅ | ✅⭐ |
| [Agorapulse](https://api.agorapulse.com/docs) | Social management with Analytics Open API for reporting data export | 🟡 API Key | ✅ | ✅ |
| [Sendible](https://www.sendible.com/) | Multi-platform social media management with API for scheduling and analytics | 🟡 API Key | ✅ | ⚠️ |
| [SocialBee](https://socialbee.com/) | Social media management with content categories, scheduling, and posting APIs | 🟡 API Key | ✅ | ⚠️ |
| [Publer](https://publer.com/docs) | Social media automation with REST API for publishing across 13 platforms | 🟡 API Key | ✅ | ✅⭐ |
| [Iconosquare](https://www.iconosquare.com/) | Social media analytics platform with API access for Instagram and Facebook data | 🟡 API Key | ✅ | ⚠️ |
| [Loomly](https://www.loomly.com/) | Brand management platform with content calendar and publishing integrations | 🟡 API Key | ✅ | ⚠️ |
| [Planable](https://planable.io/) | Social media collaboration platform with content approval and scheduling APIs | 🟡 API Key | ✅ | ⚠️ |
| [CoSchedule](https://coschedule.com/) | Marketing calendar platform with webhook integrations for content workflows | 🟡 API Key | ✅ | ⚠️ |

---

## 🎤 Speech & Voice Recognition APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Google Speech-to-Text](https://cloud.google.com/speech-to-text/docs) | Cloud ASR supporting 85+ languages with REST and gRPC APIs for batch and streaming | 🔴 OAuth | ✅ | ✅⭐ |
| [Amazon Transcribe](https://docs.aws.amazon.com/transcribe/latest/APIReference/Welcome.html) | AWS speech recognition with batch, streaming, medical, and call analytics APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Azure Speech](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/) | Microsoft cognitive speech service with SDK and REST APIs for STT and TTS | 🟡 API Key | ✅ | ✅⭐ |
| [Deepgram](https://developers.deepgram.com/) | Enterprise voice AI with STT, TTS, and agent APIs for real-time transcription | 🟡 API Key | ✅ | ✅⭐ |
| [AssemblyAI](https://www.assemblyai.com/docs/) | AI speech-to-text with REST API for transcription, summarization, and analysis | 🟡 API Key | ✅ | ✅⭐ |
| [Rev.ai](https://docs.rev.ai/) | Speech-to-text with async and streaming APIs plus topic and sentiment analysis | 🟡 API Key | ✅ | ✅⭐ |
| [Speechmatics](https://docs.speechmatics.com/) | Enterprise ASR with REST API for real-time and batch transcription in 55+ languages | 🟡 API Key | ✅ | ✅ |
| [Whisper (OpenAI)](https://platform.openai.com/docs/guides/speech-to-text) | Open-source speech recognition model with OpenAI API endpoint for transcription | 🟡 API Key | ✅ | ✅⭐ |
| [Picovoice](https://picovoice.ai/docs/) | On-device voice AI with SDKs for wake word, STT, NLU, and voice activity detection | 🟡 API Key | ✅ | ✅ |
| [Otter.ai](https://help.otter.ai/hc/en-us/articles/4412365535895) | Meeting transcription with REST API using OAuth 2.0 and webhooks | 🔴 OAuth | ✅ | ⚠️ |
| [Vosk](https://alphacephei.com/vosk/) | Offline open-source speech recognition with lightweight API for 20+ languages | 🟢 No | ✅ | ✅ |
| [Mozilla DeepSpeech](https://deepspeech.readthedocs.io/) | Open-source STT engine with Python and Node.js APIs for offline transcription | 🟢 No | ✅ | ✅ |

---

## 🚢 Supply Chain & Procurement APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [SAP Ariba](https://developer.ariba.com/) | Cloud procurement platform with APIs for sourcing, contracts, and purchasing | 🔴 OAuth | ✅ | ✅ |
| [Coupa](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api) | Business spend management with REST API for suppliers, POs, invoices, and approvals | 🔴 OAuth | ✅ | ✅ |
| [Jaggaer](https://www.jaggaer.com/) | Autonomous commerce platform with procurement and supplier management APIs | 🟡 API Key | ✅ | ⚠️ |
| [Oracle Procurement](https://docs.oracle.com/en/cloud/saas/procurement/) | Cloud procurement suite with REST APIs for purchasing, sourcing, and contracts | 🔴 OAuth | ✅ | ✅ |
| [GEP](https://www.gep.com/) | Unified procurement platform with API integration for spend and supply chain | 🟡 API Key | ✅ | ⚠️ |
| [Ivalua](https://www.ivalua.com/) | Source-to-pay platform with API-driven procurement and supplier management | 🟡 API Key | ✅ | ⚠️ |
| [Procurify](https://developer.procurify.com/) | Real-time spend management with REST API for POs, users, locations, and vendors | 🔴 OAuth | ✅ | ✅ |
| [Precoro](https://precoro.com/) | Cloud procurement software with API for purchase orders and approval workflows | 🟡 API Key | ✅ | ✅ |
| [Kissflow](https://kissflow.com/) | Low-code procurement workflows with REST API for process automation | 🟡 API Key | ✅ | ⚠️ |
| [Tradogram](https://www.tradogram.com/) | Procurement management with API integration for purchase orders and sourcing | 🟡 API Key | ✅ | ⚠️ |
| [Tradeshift](https://developers.tradeshift.com/docs/api) | B2B commerce platform with REST API using OAuth for supply chain documents | 🔴 OAuth | ✅ | ✅ |
| [Basware](https://www.basware.com/) | AP automation and procurement with API for invoices, POs, and payment workflows | 🟡 API Key | ✅ | ⚠️ |

---

## 🧮 Tax Calculation & Compliance APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Avalara](https://developer.avalara.com/) | Real-time tax calculation with AvaTax REST API for sales, use, and VAT compliance | 🟡 API Key | ✅ | ✅⭐ |
| [TaxJar](https://developers.taxjar.com/) | Sales tax API with calculation, reporting, and filing in 7 language SDKs | 🟡 API Key | ✅ | ✅⭐ |
| [Vertex](https://developer.vertexinc.com/) | Enterprise tax engine with REST APIs for indirect tax, payroll, and address cleansing | 🟡 API Key | ✅ | ✅ |
| [Sovos](https://developer.sovos.com/) | Global tax compliance with Simple Connect, Tax Determination, and Indirect Tax APIs | 🔴 OAuth | ✅ | ✅ |
| [Thomson Reuters ONESOURCE](https://developers.thomsonreuters.com/) | Enterprise tax technology with APIs for indirect tax determination and compliance | 🟡 API Key | ✅ | ⚠️ |
| [Wolters Kluwer](https://www.wolterskluwer.com/) | Tax and accounting technology with API integration for compliance workflows | 🟡 API Key | ✅ | ⚠️ |
| [CrowdReason](https://www.crowdreason.com/) | Property tax management with data analytics and API integration capabilities | 🟡 API Key | ✅ | ⚠️ |
| [Taxify (Sovos)](https://developer.sovos.com/) | Cloud-based sales tax automation with REST API now part of Sovos platform | 🟡 API Key | ✅ | ✅ |
| [Anrok](https://www.anrok.com/integrations) | SaaS sales tax automation with API for Stripe, billing systems, and compliance | 🟡 API Key | ✅ | ✅ |
| [Fonoa](https://docs.fonoa.com/reference/welcome-to-fonoa) | Global tax automation with REST API for lookup, e-invoicing, and tax determination | 🟡 API Key | ✅ | ✅⭐ |
| [Lovat](https://www.vatcompliance.co/) | Global VAT compliance with API for tax calculation and cross-border transactions | 🟡 API Key | ✅ | ✅ |
| [TaxCloud](https://docs.taxcloud.com/) | Free sales tax API with REST endpoints for calculation, exemptions, and reporting | 🟡 API Key | ✅ | ✅⭐ |

---

## 🏥 Telehealth & Virtual Care APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Twilio Video](https://www.twilio.com/docs/video) | Programmable video with HIPAA-eligible REST API for rooms, recordings, and tokens | 🟡 API Key | ✅ | ✅⭐ |
| [Vonage Video](https://tokbox.com/developer/) | WebRTC video platform (formerly TokBox) with REST API and multi-platform SDKs | 🟡 API Key | ✅ | ✅⭐ |
| [Doxy.me](https://developer.doxy.me/) | Simple HIPAA-compliant telemedicine platform with developer API portal | 🟡 API Key | ✅ | ⚠️ |
| [Zoom for Healthcare](https://developers.zoom.us/docs/) | HIPAA-compliant video with Meeting and Video SDK APIs for virtual care | 🔴 OAuth | ✅ | ✅⭐ |
| [Teladoc](https://www.teladoc.com/) | Virtual care platform with enterprise API integration for telehealth workflows | 🟡 API Key | ✅ | ⚠️ |
| [Amwell](https://www.amwell.com/) | Digital health platform with API for virtual visits, scheduling, and clinical tools | 🔴 OAuth | ✅ | ⚠️ |
| [VSee](https://vsee.com/) | HIPAA-compliant telehealth with SDK and API for video visits and clinic management | 🟡 API Key | ✅ | ✅ |
| [Vidyo (Enghouse)](https://www.vidyo.com/) | Enterprise video platform with SDK for embedding HD video into health applications | 🟡 API Key | ✅ | ✅ |
| [SimplePractice](https://www.simplepractice.com/) | Practice management platform with enterprise API for behavioral health scheduling | 🔴 OAuth | ✅ | ⚠️ |
| [TherapyNotes](https://www.therapynotes.com/) | EHR for behavioral health with practice management and telehealth integration | 🟡 API Key | ✅ | ⚠️ |
| [DrChrono](https://app.drchrono.com/api-docs/) | Open EHR platform with OAuth 2.0 REST API for patients, appointments, and clinical data | 🔴 OAuth | ✅ | ✅⭐ |
| [Kareo (Tebra)](https://www.tebra.com/) | Practice management and telehealth platform with API for scheduling and billing | 🟡 API Key | ✅ | ⚠️ |

---

## ⏱️ Time Tracking & Productivity APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Toggl Track](https://developers.track.toggl.com/) | Time tracking with REST API v9 for time entries, projects, reports, and webhooks | 🟡 API Key | ✅ | ✅⭐ |
| [Clockify](https://docs.clockify.me/) | Free time tracking with REST API for entries, projects, workspaces, and reports | 🟡 API Key | ✅ | ✅⭐ |
| [Harvest](https://help.getharvest.com/api-v2/) | Time tracking and invoicing with REST API v2 for entries, projects, and expenses | 🔴 OAuth | ✅ | ✅⭐ |
| [TimeCamp](https://developer.timecamp.com/) | Automatic time tracking with REST API v2/v3 for entries, tasks, and users | 🟡 API Key | ✅ | ✅ |
| [Hubstaff](https://developer.hubstaff.com/) | Employee time tracking with OpenID Connect REST API for activities and screenshots | 🔴 OAuth | ✅ | ✅⭐ |
| [RescueTime](https://www.rescuetime.com/rtx/developers) | Productivity analytics with Analytic Data, Daily Summary, and Alerts Feed APIs | 🔴 OAuth | ✅ | ✅ |
| [Everhour](https://everhour.docs.apiary.io/) | Project time tracking with REST API for time entries, projects, and budgets | 🟡 API Key | ✅ | ✅ |
| [TMetric](https://tmetric.com/) | Time tracking with REST API for work entries, projects, and team management | 🟡 API Key | ✅ | ✅ |
| [Timely](https://timelyapp.com/) | AI-powered time tracking with REST API for automatic hours and project management | 🔴 OAuth | ✅ | ✅ |
| [DeskTime](https://desktime.com/) | Automatic employee time tracking with API for productivity data and reports | 🟡 API Key | ✅ | ⚠️ |
| [Time Doctor](https://www.timedoctor.com/) | Employee monitoring and time tracking with REST API for users and time data | 🔴 OAuth | ✅ | ✅ |
| [Paymo](https://github.com/paymo-org/api) | Project management and time tracking with REST API for entries, tasks, and invoices | 🟡 API Key | ✅ | ✅ |

---

## ✈️ Travel & Hospitality APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Amadeus](https://developers.amadeus.com/) | Self-service travel APIs for flights, hotels, destinations, and itineraries with SDKs | 🟡 API Key | ✅ | ✅⭐ |
| [Sabre](https://developer.sabre.com/) | GDS travel APIs in REST/JSON and SOAP/XML for airline, hotel, and car booking | 🟡 API Key | ✅ | ✅ |
| [Travelport](https://developer.travelport.com/) | JSON travel API microservices for air, hotel, car rental, and rail search/booking | 🟡 API Key | ✅ | ✅ |
| [Booking.com](https://developers.booking.com/) | Accommodation affiliate and connectivity APIs for property listings and bookings | 🟡 API Key | ✅ | ✅ |
| [Expedia](https://developers.expedia.com/) | Travel platform with Rapid API for lodging, flights, and package availability | 🟡 API Key | ✅ | ✅ |
| [Skyscanner](https://developers.skyscanner.net/docs/intro) | Flight search API with Live Prices, Autosuggest, and Geo APIs for travel apps | 🟡 API Key | ✅ | ✅⭐ |
| [Kiwi.com (Tequila)](https://tequila.kiwi.com/) | B2B travel platform with Search, Booking, Location, and Multicity flight APIs | 🟡 API Key | ✅ | ✅ |
| [TripAdvisor](https://developer-tripadvisor.com/) | Travel content with partner API for reviews, ratings, photos, and location data | 🟡 API Key | ✅ | ✅ |
| [Hotels.com](https://developers.expedia.com/) | Hotel booking via Expedia Rapid API for availability, rates, and reservations | 🟡 API Key | ✅ | ✅ |
| [Airbnb](https://www.airbnb.com/partner) | Vacation rental platform with partner and property management connectivity APIs | 🔴 OAuth | ✅ | ⚠️ |
| [Viator](https://docs.viator.com/partner-api/) | Tours and experiences booking with Partner API for products, pricing, and reviews | 🟡 API Key | ✅ | ✅ |
| [Google Hotels](https://developers.google.com/hotels) | Hotel pricing and availability feed APIs for integration with Google travel search | 🟡 API Key | ✅ | ✅ |

---

## 📹 Video Conferencing & Webinar APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Zoom](https://developers.zoom.us/docs/api/) | Video meetings with REST API for rooms, recordings, meetings, and webinars | 🔴 OAuth | ✅ | ✅⭐ |
| [Microsoft Teams](https://learn.microsoft.com/en-us/graph/api/resources/teams-api-overview) | Teams collaboration via Microsoft Graph API for calls, meetings, and channels | 🔴 OAuth | ✅ | ✅⭐ |
| [Google Meet](https://developers.google.com/meet/api) | Video meetings via Google Workspace API for conference creation and management | 🔴 OAuth | ✅ | ✅ |
| [Webex](https://developer.webex.com/) | Cisco video platform with REST API for meetings, messaging, and calling | 🔴 OAuth | ✅ | ✅⭐ |
| [GoTo Meeting](https://developer.goto.com/) | Video conferencing with REST API via GoTo developer center for meetings and webinars | 🔴 OAuth | ✅ | ✅ |
| [BlueJeans](https://developer.bluejeans.com/) | Enterprise video with REST API for meetings, recordings, and user management | 🔴 OAuth | ✅ | ✅ |
| [Vonage Video](https://developer.vonage.com/en/video/overview) | WebRTC video API (formerly TokBox OpenTok) with multi-platform SDKs | 🟡 API Key | ✅ | ✅⭐ |
| [Daily.co](https://docs.daily.co/) | WebRTC video API with REST API for rooms, tokens, and recording management | 🟡 API Key | ✅ | ✅⭐ |
| [Whereby](https://docs.whereby.com/) | Embeddable video calls with REST API and web component for room management | 🟡 API Key | ✅ | ✅⭐ |
| [Jitsi](https://jitsi.org/api/) | Open-source video conferencing with IFrame API and lib-jitsi-meet low-level API | 🟢 No | ✅ | ✅⭐ |
| [Livestorm](https://developers.livestorm.co/docs/introduction) | Video engagement platform with REST API for events, sessions, and webinar management | 🟡 API Key | ✅ | ✅ |
| [BigMarker](https://docs.bigmarker.com/) | Webinar platform with REST API for webinar creation, registrants, and content | 🟡 API Key | ✅ | ✅ |

---

## 🏦 Banking & Open Finance APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Plaid](https://plaid.com/docs/api/) | Connect to bank accounts for transactions, identity, and balance data | 🔴 OAuth | ✅ | ✅⭐ |
| [Stripe Treasury](https://docs.stripe.com/treasury) | Embed financial services with banking-as-a-service for platforms | 🟡 API Key | ✅ | ✅⭐ |
| [Tink](https://docs.tink.com/api) | European open banking platform connecting 6000+ banks via one API | 🔴 OAuth | ✅ | ✅ |
| [TrueLayer](https://docs.truelayer.com/reference/welcome-api-reference) | Open banking APIs for account data and payment initiation in Europe | 🔴 OAuth | ✅ | ✅⭐ |
| [Yodlee](https://developer.yodlee.com/documentation) | Financial data aggregation from 17,000+ data sources worldwide | 🟡 API Key | ✅ | ✅ |
| [MX](https://docs.mx.com/) | Financial data connectivity and enrichment for open finance use cases | 🟡 API Key | ✅ | ✅ |
| [Finicity](https://docs.finicity.com/) | Mastercard Open Finance platform for US open banking and data access | 🟡 API Key | ✅ | ✅ |
| [Belvo](https://developers.belvo.com/apis/belvoopenapispec) | Open finance API for Latin America covering banking and fiscal data | 🟡 API Key | ✅ | ✅⭐ |
| [Basiq](https://api.basiq.io/reference/introduction) | Consumer data right accredited API platform for Australia and NZ | 🟡 API Key | ✅ | ✅ |
| [Yapily](https://docs.yapily.com/api/reference/) | Open banking API infrastructure connecting 1900+ institutions in 19 countries | 🟡 API Key | ✅ | ✅ |
| [Salt Edge](https://docs.saltedge.com/v6/api_reference/) | Open banking connectivity to 5000+ banks across 70 countries | 🟡 API Key | ✅ | ✅ |
| [Mono](https://docs.mono.co/docs) | Open banking infrastructure powering Africa's digital economy | 🟡 API Key | ✅ | ✅ |

---

## 🗄️ Database & Backend-as-a-Service APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Firebase](https://firebase.google.com/docs/reference) | Google's app development platform with real-time database and auth | 🟡 API Key | ✅ | ✅⭐ |
| [Supabase](https://supabase.com/docs/guides/api) | Open source Firebase alternative with Postgres, auth, and storage | 🟡 API Key | ✅ | ✅⭐ |
| [PlanetScale](https://planetscale.com/docs) | Serverless MySQL-compatible database platform with branching | 🟡 API Key | ✅ | ✅ |
| [Fauna](https://docs.fauna.com/fauna/current/) | Distributed serverless document-relational database with native GraphQL | 🟡 API Key | ✅ | ✅ |
| [MongoDB Atlas](https://www.mongodb.com/docs/atlas/api/) | Cloud-hosted MongoDB with administration and data APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Hasura](https://hasura.io/docs/2.0/api-reference/overview/) | Instant GraphQL and REST APIs on your data with fine-grained access control | 🟡 API Key | ✅ | ✅⭐ |
| [Convex](https://docs.convex.dev/http-api/) | Reactive backend platform with real-time database and serverless functions | 🟡 API Key | ✅ | ✅ |
| [Neon](https://neon.com/docs/introduction) | Serverless Postgres with autoscaling, branching, and scale to zero | 🟡 API Key | ✅ | ✅ |
| [Upstash](https://upstash.com/docs/redis/features/restapi) | Serverless Redis and Kafka with REST API for edge and serverless | 🟡 API Key | ✅ | ✅⭐ |
| [CockroachDB](https://www.cockroachlabs.com/docs/cockroachcloud/cloud-api) | Distributed SQL database with Cloud API for programmatic management | 🟡 API Key | ✅ | ✅ |
| [Turso](https://docs.turso.tech/) | Edge-hosted distributed database based on libSQL, a fork of SQLite | 🟡 API Key | ✅ | ✅ |
| [Appwrite](https://appwrite.io/docs/references) | Open source backend server with auth, databases, storage, and functions | 🟡 API Key | ✅ | ✅⭐ |

---

## 📊 Data Visualization & BI APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Tableau](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api.htm) | REST API to manage and change Tableau Server and Cloud resources | 🔴 OAuth | ✅ | ✅ |
| [Looker](https://docs.cloud.google.com/looker/docs/api-intro) | Google Cloud BI platform API for programmatic data exploration | 🔴 OAuth | ✅ | ✅ |
| [Metabase](https://www.metabase.com/docs/latest/api) | Open source BI tool with REST API for dashboards and questions | 🟡 API Key | ✅ | ✅⭐ |
| [Apache Superset](https://superset.apache.org/docs/api/) | Open source data visualization platform with OpenAPI-compliant REST API | 🟡 API Key | ✅ | ✅⭐ |
| [Grafana](https://grafana.com/docs/grafana/latest/developer-resources/api-reference/http-api/) | Observability platform with HTTP API for dashboards and data sources | 🟡 API Key | ✅ | ✅⭐ |
| [Power BI Embedded](https://learn.microsoft.com/en-us/rest/api/power-bi/) | Microsoft REST APIs for embedding analytics and automating BI processes | 🔴 OAuth | ✅ | ✅ |
| [Cube.js](https://cube.dev/docs/product/apis-integrations/rest-api) | Semantic layer for building data apps with REST and GraphQL APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Observable](https://observablehq.com/) | Modern data visualization platform with reactive notebooks and Framework | 🟡 API Key | ✅ | ✅ |
| [Plotly](https://plotly.com/chart-studio-help/) | Interactive graphing library with Chart Studio cloud API for chart hosting | 🟡 API Key | ✅ | ✅ |
| [QuickSight](https://docs.aws.amazon.com/quicksight/latest/APIReference/Welcome.html) | AWS cloud-native BI service with embeddable analytics API | 🟡 API Key | ✅ | ✅ |
| [Sisense](https://developer.sisense.com/guides/restApi/) | Analytics platform with REST API and JavaScript API for embedded BI | 🟡 API Key | ✅ | ✅ |
| [Domo](https://developer.domo.com/) | Cloud BI platform with APIs for datasets, users, pages, and workflows | 🟡 API Key | ✅ | ✅ |

---

## 🔐 Cybersecurity & Threat Intelligence APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [VirusTotal](https://docs.virustotal.com/reference/overview) | Analyze suspicious files, URLs, domains, and IPs for malware | 🟡 API Key | ✅ | ✅⭐ |
| [Shodan](https://developer.shodan.io/api) | Search engine for internet-connected devices and security intelligence | 🟡 API Key | ✅ | ✅⭐ |
| [CrowdStrike](https://developer.crowdstrike.com/) | Falcon platform APIs for endpoint protection and threat intelligence | 🔴 OAuth | ✅ | ✅ |
| [SecurityTrails](https://docs.securitytrails.com/docs/overview) | IP, DNS, WHOIS, and company data for security intelligence | 🟡 API Key | ✅ | ✅⭐ |
| [AlienVault OTX](https://otx.alienvault.com/api) | Open threat exchange platform for community-driven threat data | 🟡 API Key | ✅ | ✅ |
| [GreyNoise](https://docs.greynoise.io/) | Internet-wide scan and attack traffic intelligence API | 🟡 API Key | ✅ | ✅⭐ |
| [Censys](https://docs.censys.com/reference/get-started) | Internet-wide scanning platform for hosts, certificates, and services | 🟡 API Key | ✅ | ✅ |
| [Recorded Future](https://api.recordedfuture.com/) | Threat intelligence platform with real-time security insights | 🟡 API Key | ✅ | ⚠️ |
| [ThreatConnect](https://docs.threatconnect.com/) | Threat intelligence platform with REST API for indicators and groups | 🟡 API Key | ✅ | ✅ |
| [AbuseIPDB](https://docs.abuseipdb.com/) | IP address abuse reporting and checking database API | 🟡 API Key | ✅ | ✅⭐ |
| [URLScan](https://urlscan.io/docs/api/) | URL scanning and analysis service for phishing and malware detection | 🟡 API Key | ✅ | ✅⭐ |
| [Have I Been Pwned](https://haveibeenpwned.com/API/v3) | Check if accounts or passwords have been compromised in data breaches | 🟡 API Key | ✅ | ✅⭐ |

---

## 🤖 Chatbot & Conversational AI APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Dialogflow](https://cloud.google.com/dialogflow/es/docs/reference/rest/v2-overview) | Google Cloud natural language understanding for conversational interfaces | 🔴 OAuth | ✅ | ✅ |
| [Amazon Lex](https://docs.aws.amazon.com/lexv2/latest/APIReference/welcome.html) | AWS service for building conversational interfaces with voice and text | 🟡 API Key | ✅ | ✅ |
| [Microsoft Bot Framework](https://learn.microsoft.com/en-us/azure/bot-service/rest-api/bot-framework-rest-overview) | Comprehensive platform for building enterprise-grade conversational bots | 🔴 OAuth | ✅ | ✅ |
| [Rasa](https://rasa.com/docs/openapi/http-api/) | Open source conversational AI framework with HTTP server endpoints | 🟡 API Key | ✅ | ✅⭐ |
| [Botpress](https://docs.botpress.cloud/docs/api-documentation/) | Open source GPT/LLM-powered chatbot platform with Cloud API | 🟡 API Key | ✅ | ✅⭐ |
| [Voiceflow](https://docs.voiceflow.com/reference/api-overview) | Visual design platform for building chat and voice AI agents | 🟡 API Key | ✅ | ✅ |
| [Cognigy](https://docs.cognigy.com/) | Enterprise conversational AI platform with REST and OpenAPI endpoints | 🟡 API Key | ✅ | ✅ |
| [Yellow.ai](https://docs.yellow.ai/api) | Agentic AI platform for autonomous, human-like customer conversations | 🟡 API Key | ✅ | ✅ |
| [Ada](https://developers.ada.cx/) | AI-powered customer service automation platform with REST APIs | 🟡 API Key | ✅ | ✅ |
| [Kore.ai](https://docs.kore.ai/) | Enterprise AI platform for multi-agent orchestration with no-code tools | 🟡 API Key | ✅ | ✅ |
| [OneReach](https://docs-dev.onereach.ai/) | No-code platform for orchestrating AI agents across channels | 🟡 API Key | ✅ | ⚠️ |
| [ManyChat](https://api.manychat.com/swagger) | Chat marketing platform API for Facebook Messenger and Instagram bots | 🟡 API Key | ✅ | ✅ |

---

## 📦 Warehouse & Inventory Management APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [ShipBob](https://developer.shipbob.com/) | E-commerce fulfillment API for orders, inventory, and shipments | 🟡 API Key | ✅ | ✅⭐ |
| [Cin7](https://api.cin7.com/) | Omnichannel inventory management with connected supply chain APIs | 🟡 API Key | ✅ | ✅ |
| [Fishbowl](https://fishbowlhelp.com/files/apidocs/introduction.html) | Advanced inventory management and manufacturing REST API for QuickBooks | 🟡 API Key | ✅ | ✅ |
| [Katana](https://developer.katanamrp.com/) | Cloud manufacturing and inventory management API with ERP integration | 🟡 API Key | ✅ | ✅⭐ |
| [Ordoro](https://docs.ordoro.com/) | Multi-channel inventory and shipping management REST API | 🟡 API Key | ✅ | ✅ |
| [TradeGecko](https://support.tradegecko.com/hc/en-us/articles/115001047190) | QuickBooks Commerce inventory and order management API (legacy) | 🔴 OAuth | ✅ | ⚠️ |
| [Brightpearl](https://api-docs.brightpearl.com/) | Retail operations platform API for orders, inventory, and accounting | 🔴 OAuth | ✅ | ✅ |
| [NetSuite](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/book_1559132836.html) | Oracle ERP suite with SuiteTalk REST web services for full business ops | 🔴 OAuth | ✅ | ✅ |
| [Unleashed](https://apidocs.unleashedsoftware.com/) | Cloud inventory management API supporting JSON and XML formats | 🟡 API Key | ✅ | ✅ |
| [Dear Systems](https://dearinventory.docs.apiary.io/) | Cin7 Core inventory management API with advanced manufacturing features | 🟡 API Key | ✅ | ✅ |
| [Zoho Inventory](https://www.zoho.com/inventory/api/v1/introduction/) | Online inventory management API with multichannel selling support | 🔴 OAuth | ✅ | ✅ |
| [inFlow](https://cloudapi.inflowinventory.com/docs/index.html) | Cloud inventory management REST API for small businesses | 🟡 API Key | ✅ | ✅ |

---

## 🎯 Advertising & Ad Tech APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Google Ads](https://developers.google.com/google-ads/api) | Programmatically manage Google Ads campaigns, keywords, and reporting | 🔴 OAuth | ✅ | ✅⭐ |
| [Meta Ads](https://developers.facebook.com/docs/marketing-api/) | Create, manage, and report on Facebook and Instagram advertising | 🔴 OAuth | ✅ | ✅ |
| [X Ads](https://developer.x.com/en/docs/x-ads-api) | Manage ad campaigns, targeting, creatives, and analytics on X/Twitter | 🔴 OAuth | ✅ | ✅ |
| [LinkedIn Ads](https://developer.linkedin.com/product-catalog/marketing/advertising-api) | Campaign management and analytics for LinkedIn advertising | 🔴 OAuth | ✅ | ✅ |
| [TikTok Ads](https://business-api.tiktok.com/portal/docs) | Build solutions for TikTok advertisers with campaign and reporting APIs | 🔴 OAuth | ✅ | ✅ |
| [Amazon Ads](https://advertising.amazon.com/API/docs/en-us/guides/overview) | Programmatically manage Amazon advertising campaigns and reports | 🔴 OAuth | ✅ | ✅ |
| [Snapchat Ads](https://developers.snap.com/api/marketing-api/Ads-API/introduction) | Marketing API for creating and managing Snapchat ad campaigns | 🔴 OAuth | ✅ | ✅ |
| [Pinterest Ads](https://developers.pinterest.com/docs/api/v5/) | Manage ad campaigns, targeting, and performance reporting on Pinterest | 🔴 OAuth | ✅ | ✅ |
| [The Trade Desk](https://partner.thetradedesk.com/v3/portal/api/overview) | Programmatic advertising platform API for demand-side operations | 🟡 API Key | ✅ | ✅ |
| [Criteo](https://developers.criteo.com/) | Performance marketing API for the world's largest advertising network | 🔴 OAuth | ✅ | ✅ |
| [Taboola](https://developers.taboola.com/backstage-api/reference/welcome) | Native advertising Backstage API for campaign management and reporting | 🔴 OAuth | ✅ | ✅ |
| [Outbrain](https://developer.outbrain.com/home-page/amplify-api/documentation/) | Amplify API for native content promotion and campaign management | 🔴 OAuth | ✅ | ✅ |

---

## 🔊 Push Notification & In-App Messaging APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [OneSignal](https://documentation.onesignal.com/reference/rest-api-overview) | Multi-channel push notification and messaging REST API | 🟡 API Key | ✅ | ✅⭐ |
| [Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/send/v1-api) | Google's cross-platform messaging solution for notifications | 🔴 OAuth | ✅ | ✅⭐ |
| [Pushover](https://pushover.net/api) | Simple real-time push notification API for Android, iOS, and desktop | 🟡 API Key | ✅ | ✅⭐ |
| [Braze](https://www.braze.com/docs/api/home) | Customer engagement platform API for messaging, campaigns, and data | 🟡 API Key | ✅ | ✅ |
| [Airship](https://docs.airship.com/api/ua/) | Customer engagement platform with push, SMS, and in-app messaging | 🟡 API Key | ✅ | ✅ |
| [Leanplum](https://docs.leanplum.com/reference/api-introduction) | Mobile engagement platform API for A/B testing and messaging | 🟡 API Key | ✅ | ✅ |
| [CleverTap](https://developer.clevertap.com/docs/api-overview) | All-in-one customer engagement API for analytics and push notifications | 🟡 API Key | ✅ | ✅ |
| [MoEngage](https://developers.moengage.com/hc/en-us) | Customer engagement API for push, in-app, email, and SMS messaging | 🟡 API Key | ✅ | ✅ |
| [Pusher](https://pusher.com/docs/channels/library_auth_reference/rest-api/) | Real-time communication API with Channels for WebSocket messaging | 🟡 API Key | ✅ | ✅⭐ |
| [Iterable](https://api.iterable.com/api/docs) | Cross-channel marketing automation API for email, push, SMS, and more | 🟡 API Key | ✅ | ✅ |
| [Customer.io](https://docs.customer.io/integrations/api/customerio-apis/) | Messaging automation API with track, app, and transactional APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Intercom](https://developers.intercom.com/) | Customer communications platform API for messaging and support | 🔴 OAuth | ✅ | ✅⭐ |

---

## 📞 Contact Center & Telephony APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Twilio](https://www.twilio.com/docs/usage/api) | Cloud communications platform for voice, SMS, video, and messaging | 🟡 API Key | ✅ | ✅⭐ |
| [Vonage](https://developer.vonage.com/) | Communications APIs for voice, messages, video, and verification | 🟡 API Key | ✅ | ✅⭐ |
| [RingCentral](https://developers.ringcentral.com/api-reference) | Cloud communications APIs for voice, SMS, meetings, and fax | 🔴 OAuth | ✅ | ✅⭐ |
| [Plivo](https://www.plivo.com/docs/voice/api/call/) | Communication platform APIs for global voice calls and SMS messaging | 🟡 API Key | ✅ | ✅ |
| [Telnyx](https://developers.telnyx.com/) | Telecom API platform for voice, messaging, fax, and networking | 🟡 API Key | ✅ | ✅⭐ |
| [Bandwidth](https://dev.bandwidth.com/) | Enterprise communications APIs for voice, messaging, and 911 services | 🟡 API Key | ✅ | ✅ |
| [Sinch](https://developers.sinch.com/) | Communication APIs for SMS, voice, verification, and conversation | 🟡 API Key | ✅ | ✅ |
| [MessageBird](https://developers.messagebird.com/api) | Omnichannel communications API for SMS, voice, and chat apps | 🟡 API Key | ✅ | ✅ |
| [Five9](https://www.five9.com/development) | Cloud contact center platform with REST and SOAP APIs for CCaaS | 🟡 API Key | ✅ | ⚠️ |
| [NICE CXone](https://developer.niceincontact.com/API) | Contact center REST APIs for agents, admin, reporting, and routing | 🟡 API Key | ✅ | ✅ |
| [Genesys Cloud](https://developer.genesys.cloud/) | Cloud CX platform with REST API, SDKs, and API explorer tool | 🔴 OAuth | ✅ | ✅ |
| [8x8](https://developer.8x8.com/) | Cloud communications and contact center APIs for voice, video, and SMS | 🟡 API Key | ✅ | ✅ |

---

## 🧬 Bioinformatics & Life Sciences APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [NCBI E-utilities](https://www.ncbi.nlm.nih.gov/books/NBK25501/) | Entrez programming utilities for PubMed, Gene, Protein, and more | 🟡 API Key | ✅ | ✅⭐ |
| [UniProt](https://www.uniprot.org/api-documentation) | REST API for comprehensive protein sequence and functional data | 🟢 No | ✅ | ✅⭐ |
| [Ensembl](https://rest.ensembl.org/) | Genomic data REST API for sequences, variations, and comparative data | 🟢 No | ✅ | ✅⭐ |
| [RCSB PDB](https://data.rcsb.org/) | Protein Data Bank API for 3D structure data and search | 🟢 No | ✅ | ✅⭐ |
| [ChEMBL](https://www.ebi.ac.uk/chembl/api/data/docs) | Bioactivity database API for drug discovery data and chemical compounds | 🟢 No | ✅ | ✅⭐ |
| [KEGG](https://www.kegg.jp/kegg/rest/keggapi.html) | REST API for biological pathways, genomes, and chemical information | 🟢 No | ✅ | ✅ |
| [BioGRID](https://wiki.thebiogrid.org/doku.php/biogridrest) | REST service for protein and genetic interaction data | 🟡 API Key | ✅ | ✅ |
| [STRING](https://string-db.org/help/api/) | Protein-protein interaction network database REST API | 🟢 No | ✅ | ✅ |
| [Reactome](https://reactome.org/dev/content-service) | Biological pathway database with Content Service REST API | 🟢 No | ✅ | ✅⭐ |
| [ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/docs/api_http/) | NCBI genomic variation and clinical significance submission API | 🟡 API Key | ✅ | ✅ |
| [PharmGKB](https://api.pharmgkb.org/) | Pharmacogenomics knowledge base API for drug-gene relationships | 🟢 No | ✅ | ✅ |
| [InterPro](https://www.ebi.ac.uk/interpro/api/) | Protein families, domains, and functional sites classification API | 🟢 No | ✅ | ✅ |

---

## 🏗️ Construction & Building APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Procore](https://developers.procore.com/documentation/introduction) | Construction management REST API for projects, RFIs, and submittals | 🔴 OAuth | ✅ | ✅⭐ |
| [PlanGrid](https://developer.autodesk.com/) | Construction productivity software API (now part of Autodesk) | 🔴 OAuth | ✅ | ✅ |
| [Autodesk Construction Cloud](https://aps.autodesk.com/en/docs/acc/v1/overview/) | APIs for BIM, project management, and construction data on Autodesk Platform | 🔴 OAuth | ✅ | ✅ |
| [Trimble](https://developer.trimble.com/) | Construction technology APIs for project management and field solutions | 🔴 OAuth | ✅ | ⚠️ |
| [Bluebeam](https://developers.bluebeam.com/) | Construction document management and markup collaboration APIs | 🔴 OAuth | ✅ | ⚠️ |
| [Fieldwire](https://developers.fieldwire.com/) | Field management platform API for tasks, plans, and inspections | 🟡 API Key | ✅ | ✅ |
| [BuildingConnected](https://aps.autodesk.com/developer/overview/autodesk-construction-cloud) | Preconstruction bid management API (part of Autodesk ACC) | 🔴 OAuth | ✅ | ✅ |
| [Aconex](https://aps.autodesk.com/en/docs/acc/v1/reference) | Construction document and project management API (Oracle/Autodesk) | 🔴 OAuth | ✅ | ⚠️ |
| [Newforma](https://www.newforma.com/) | Project information management for AEC industry | 🟡 API Key | ✅ | ⚠️ |
| [CoConstruct](https://www.coconstruct.com/) | Custom home builder and remodeler project management platform | 🟡 API Key | ✅ | ⚠️ |
| [Buildertrend](https://buildertrend.com/) | Cloud-based construction project management platform | 🟡 API Key | ✅ | ⚠️ |
| [Sage 300 CRE](https://www.sage.com/en-us/sage-business-cloud/sage-300/) | Construction real estate ERP with accounting and project management | 🟡 API Key | ✅ | ⚠️ |

---

## 🎓 EdTech & Student Management APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Canvas LMS](https://www.canvas.instructure.com/doc/api/) | Instructure learning management system REST API with OpenAPI spec | 🔴 OAuth | ✅ | ✅⭐ |
| [Blackboard](https://developer.blackboard.com/portal/displayApi/Learn) | Learn REST API for courses, content, grades, and user management | 🔴 OAuth | ✅ | ✅ |
| [Clever](https://dev.clever.com/docs/api-overview) | Secure student data platform API connecting SIS to ed-tech apps | 🔴 OAuth | ✅ | ✅⭐ |
| [ClassLink](https://developer.classlink.com/) | Single sign-on and rostering API for K-12 education data exchange | 🔴 OAuth | ✅ | ✅ |
| [Google Classroom](https://developers.google.com/classroom) | API for managing Classroom courses, rosters, assignments, and grades | 🔴 OAuth | ✅ | ✅⭐ |
| [Schoology](https://developers.schoology.com/) | Learning management system API for courses, assignments, and grades | 🔴 OAuth | ✅ | ✅ |
| [PowerSchool](https://support.powerschool.com/developer) | Student information system API for enrollment, grades, and attendance | 🔴 OAuth | ✅ | ⚠️ |
| [Infinite Campus](https://www.infinitecampus.com/) | K-12 student information system with data interoperability APIs | 🟡 API Key | ✅ | ⚠️ |
| [Skyward](https://www.skyward.com/) | Student management and school ERP platform with data exchange APIs | 🟡 API Key | ✅ | ⚠️ |
| [Ellucian](https://www.ellucian.com/solutions/ellucian-ethos) | Higher education ERP with Ethos integration platform APIs | 🔴 OAuth | ✅ | ✅ |
| [Brightspace](https://docs.valence.desire2learn.com/) | D2L learning platform API for courses, content, and user management | 🔴 OAuth | ✅ | ✅ |
| [Moodle](https://docs.moodle.org/dev/Web_services_API) | Open source LMS with web services API supporting REST, XML-RPC, and SOAP | 🟡 API Key | ✅ | ✅ |

---

## ⚡ Energy & Utilities APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [ENTSO-E](https://transparency.entsoe.eu/content/static_content/Static%20content/web%20api/Guide.html) | European electricity transparency platform API for generation and load data | 🟡 API Key | ✅ | ✅ |
| [EIA](https://www.eia.gov/opendata/documentation.php) | U.S. Energy Information Administration open data API for energy statistics | 🟡 API Key | ✅ | ✅⭐ |
| [Carbon Interface](https://docs.carboninterface.com/) | Carbon emissions estimation API for electricity, flights, and shipping | 🟡 API Key | ✅ | ✅⭐ |
| [WattTime](https://docs.watttime.org/) | Real-time and forecast grid emissions data API for carbon-aware computing | 🟡 API Key | ✅ | ✅⭐ |
| [Genability](https://developer.genability.com/) | Utility rate and tariff database API for energy cost calculations | 🟡 API Key | ✅ | ✅ |
| [UtilityAPI](https://utilityapi.com/docs) | Automated utility data access API for energy usage and bill data | 🟡 API Key | ✅ | ✅ |
| [GridX](https://developer.gridx.de/) | Smart energy management platform API for distributed energy resources | 🟡 API Key | ✅ | ⚠️ |
| [Arcadia](https://docs.arcadia.com/) | Utility data platform API for energy account access and data extraction | 🟡 API Key | ✅ | ✅ |
| [Bidgely](https://www.bidgely.com/) | AI-powered energy analytics API for utility customer insights | 🟡 API Key | ✅ | ⚠️ |
| [OhmConnect](https://www.ohmconnect.com/) | Demand response and energy savings platform for smart grid integration | 🟡 API Key | ✅ | ⚠️ |
| [EnergyStar](https://portfoliomanager.energystar.gov/webservices/) | EPA Portfolio Manager web services API for building energy benchmarking | 🟡 API Key | ✅ | ✅ |
| [OpenEI](https://openei.org/wiki/OpenEI:API) | Open energy information API for utility rates, renewable energy, and datasets | 🟡 API Key | ✅ | ✅ |

---

## 🗳️ Election & Civic Data APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Google Civic Info](https://developers.google.com/civic-information) | Voter info, election data, and representative lookup by address | 🟡 API Key | ✅ | ✅⭐ |
| [OpenSecrets](https://www.opensecrets.org/open-data/api-documentation) | Campaign finance and lobbying data from Center for Responsive Politics | 🟡 API Key | ✅ | ✅ |
| [FEC](https://api.open.fec.gov/developers/) | Federal Election Commission campaign finance RESTful API | 🟡 API Key | ✅ | ✅⭐ |
| [Ballotpedia](https://developer.ballotpedia.org) | Elections, candidates, and ballot measures data for all levels of government | 🟡 API Key | ✅ | ✅ |
| [Vote.org](https://www.vote.org/) | Voter registration, absentee ballot, and election reminders platform | 🟡 API Key | ✅ | ⚠️ |
| [Democracy Works](https://www.democracy.works/) | TurboVote platform for election information and voter engagement | 🟡 API Key | ✅ | ⚠️ |
| [Cicero](https://www.cicerodata.com/) | Legislative district and elected official data by address lookup | 🟡 API Key | ✅ | ✅ |
| [VoteSmart](https://votesmart.org/share/api) | Politician voting records, bios, and ratings for transparency | 🟡 API Key | ✅ | ✅ |
| [ProPublica Congress](https://projects.propublica.org/api-docs/congress-api/) | Congressional bills, votes, and member data | 🟡 API Key | ✅ | ✅⭐ |
| [Open States](https://docs.openstates.org/api-v3/) | State legislative data API for bills, legislators, and votes across 50 states | 🟡 API Key | ✅ | ✅⭐ |
| [Represent](https://represent.opennorth.ca/) | Canadian politician and electoral district lookup API by Open North | 🟢 No | ✅ | ✅ |
| [GovTrack](https://www.govtrack.us/developers/api) | U.S. Congress tracking API for bills, votes, and legislative activities | 🟢 No | ✅ | ✅⭐ |

---

## 🎭 Arts & Culture APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Europeana](https://apis.europeana.eu/en) | Access millions of European cultural heritage items across museums | 🟡 API Key | ✅ | ✅⭐ |
| [IIIF](https://iiif.io/api/) | International Image Interoperability Framework for sharing digital images | 🟢 No | ✅ | ✅⭐ |
| [Harvard Art Museums](https://github.com/harvardartmuseums/api-docs) | REST API for 250,000+ objects, people, exhibitions, and publications | 🟡 API Key | ✅ | ✅⭐ |
| [Rijksmuseum](https://data.rijksmuseum.nl/docs/api/) | Dutch national museum API for 500,000+ art objects and images | 🟡 API Key | ✅ | ✅⭐ |
| [Met Museum](https://metmuseum.github.io/) | Metropolitan Museum of Art collection API with 470,000+ artworks | 🟢 No | ✅ | ✅⭐ |
| [Artsy](https://developers.artsy.net/v2) | Art world API for artists, artworks, genes, shows, and galleries | 🔴 OAuth | ✅ | ✅ |
| [Google Arts & Culture](https://developers.google.com/knowledge-graph/) | Google Knowledge Graph API covering cultural entities and art data | 🟡 API Key | ✅ | ✅ |
| [British Museum](https://www.britishmuseum.org/collection) | Collection online search with structured data for research access | 🟢 No | ✅ | ⚠️ |
| [Cooper Hewitt](https://collection.cooperhewitt.org/api/) | Smithsonian Design Museum collection API for design objects and data | 🟡 API Key | ✅ | ✅⭐ |
| [Smithsonian](https://www.si.edu/openaccess/devtools) | Open access API to millions of Smithsonian Institution collection items | 🟡 API Key | ✅ | ✅ |
| [Unsplash](https://unsplash.com/documentation) | Free HD photo API with millions of high-quality images from photographers | 🟡 API Key | ✅ | ✅⭐ |
| [Artstor](https://www.jstor.org/) | Digital library of art images and scholarly content (now part of JSTOR) | 🔴 OAuth | ✅ | ⚠️ |

---

## 🧪 Chemistry & Material Science APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [PubChem](https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest) | NCBI chemical database REST API for compounds, substances, and bioassays | 🟢 No | ✅ | ✅⭐ |
| [ChemSpider](https://developer.rsc.org/compounds-v1/apis) | Royal Society of Chemistry compound search and structure API | 🟡 API Key | ✅ | ✅ |
| [Open Babel](https://open-babel.readthedocs.io/) | Open source chemical toolbox library API for file format conversion | 🟢 No | ✅ | ✅ |
| [RDKit](https://www.rdkit.org/docs/) | Cheminformatics and machine learning toolkit with Python/C++ API | 🟢 No | ✅ | ✅⭐ |
| [Materials Project](https://api.materialsproject.org/docs) | Materials science database API for computed material properties | 🟡 API Key | ✅ | ✅⭐ |
| [NIST Chemistry WebBook](https://webbook.nist.gov/chemistry/) | Standard reference thermochemical, spectral, and ion data from NIST | 🟢 No | ✅ | ⚠️ |
| [ChEBI](https://www.ebi.ac.uk/chebi/backend/api/docs/) | Chemical Entities of Biological Interest ontology and database API | 🟢 No | ✅ | ✅ |
| [Chemeo](https://www.chemeo.com/api) | Chemical and physical properties database API for engineering data | 🟡 API Key | ✅ | ✅ |
| [Chemical Book](https://www.chemicalbook.com/) | Chemical product database with CAS numbers, MSDS, and properties | 🟢 No | ✅ | ⚠️ |
| [Reaxys](https://www.reaxys.com/) | Elsevier curated chemistry database for reactions and substances | 🔴 OAuth | ✅ | ⚠️ |
| [SciFinder](https://scifinder.cas.org/) | CAS chemical abstracts database for literature and substance searching | 🔴 OAuth | ✅ | ⚠️ |
| [LabArchives](https://docs.labarchives.com/) | Electronic lab notebook platform API for research data management | 🟡 API Key | ✅ | ✅ |

---

## 🏥 Clinical Trials & Drug Data APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [ClinicalTrials.gov](https://clinicaltrials.gov/data-api/api) | REST API v2 for searching clinical trial studies, conditions, and interventions | 🟢 No | ✅ | ✅⭐ |
| [OpenFDA](https://open.fda.gov/apis/) | FDA open data on drugs, devices, foods, and adverse events | 🟡 API Key | ✅ | ✅⭐ |
| [DailyMed](https://dailymed.nlm.nih.gov/dailymed/app-support-web-services.cfm) | NLM structured product labeling data for FDA-approved drug labels | 🟢 No | ✅ | ✅ |
| [DrugBank](https://docs.drugbank.com/) | Comprehensive drug data including interactions, targets, and pharmacology | 🟡 API Key | ✅ | ✅ |
| [RxNorm](https://lhncbc.nlm.nih.gov/RxNav/APIs/RxNormAPIs.html) | NLM normalized names and codes for clinical drugs and dose forms | 🟢 No | ✅ | ✅⭐ |
| [DGIdb](https://dgidb.org/api) | Drug-gene interaction database with GraphQL API for druggable genome queries | 🟢 No | ✅ | ✅ |
| [PharmVar](https://www.pharmvar.org/documentation) | Pharmacogene variation consortium data for allele definitions and nomenclature | 🟡 API Key | ✅ | ✅ |
| [SIDER](http://sideeffects.embl.de/) | Database of marketed drugs and their recorded adverse drug reactions | 🟢 No | ❌ | ⚠️ |
| [PubChem](https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest) | NCBI chemical database with compound, substance, and bioassay data | 🟢 No | ✅ | ✅⭐ |
| [ChEMBL](https://chembl.gitbook.io/chembl-interface-documentation) | EBI bioactivity database for drug-like molecules with REST and GraphQL APIs | 🟢 No | ✅ | ✅ |
| [NDF-RT](https://lhncbc.nlm.nih.gov/RxNav/APIs/index.html) | National Drug File Reference Terminology for drug classifications via RxNav | 🟢 No | ✅ | ✅ |
| [WHO Drug (Koda)](https://who-umc.org/media/skclibnl/whodrug-koda-api-user-guide.pdf) | WHO global drug dictionary for automated drug name and ATC coding | 🟡 API Key | ✅ | ⚠️ |
| [TTD](https://idrblab.org/ttd/) | Therapeutic Targets Database for known and explored therapeutic protein targets | 🟢 No | ✅ | ⚠️ |

---

## 🎪 Ticketing & Events Discovery APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Ticketmaster Discovery](https://developer.ticketmaster.com/products-and-docs/apis/discovery-api/v2/) | Search events, attractions, venues, and classifications worldwide | 🟡 API Key | ✅ | ✅⭐ |
| [Eventbrite](https://www.eventbrite.com/platform/docs/introduction) | Create, manage, and search events with ticketing and attendee data | 🔴 OAuth | ✅ | ✅ |
| [StubHub](https://developer.stubhub.com/) | World's largest ticket marketplace with event search and ticket purchasing | 🔴 OAuth | ✅ | ✅ |
| [SeatGeek](https://platform.seatgeek.com/) | Event, performer, and venue data with ticket pricing and availability | 🟡 API Key | ✅ | ✅⭐ |
| [DICE](https://partners-endpoint.dice.fm/graphql/docs/index.html) | GraphQL API for ticket holder data, event finances, and access management | 🟡 API Key | ✅ | ✅ |
| [Bandsintown](https://help.artists.bandsintown.com/en/articles/9186477-api-documentation) | Largest database of upcoming concert listings and artist tour data | 🟡 API Key | ✅ | ✅ |
| [Songkick](https://www.songkick.com/developer) | Live music database with 6M+ upcoming and past concerts worldwide | 🟡 API Key | ✅ | ✅ |
| [Fever](https://data-reporting-api.prod.feverup.com/v1/redoc) | Reporting API for event sales, ticketing data, and real-time analytics | 🟡 API Key | ✅ | ✅ |
| [Universe](https://developers.universe.com/) | Event creation, ticketing, and attendee management with OAuth2 | 🔴 OAuth | ✅ | ✅ |
| [Luma](https://docs.luma.com/reference/getting-started-with-your-api) | Programmatic event and calendar management with registration handling | 🟡 API Key | ✅ | ✅ |
| [Brown Paper Tickets](https://www.brownpapertickets.com/apidocs/index.html) | Event creation, sales data retrieval, and ticket management | 🟡 API Key | ✅ | ✅ |
| [PredictHQ](https://docs.predicthq.com/) | Demand intelligence API aggregating events that impact business demand | 🟡 API Key | ✅ | ✅⭐ |

---

## 🚀 Space & Astronomy APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [NASA](https://api.nasa.gov/) | Open APIs for APOD, Mars Rover Photos, NEO, EPIC, and more NASA data | 🟡 API Key | ✅ | ✅⭐ |
| [SpaceX](https://github.com/r-spacex/SpaceX-API) | Open source REST API for SpaceX launches, rockets, capsules, and Starlink | 🟢 No | ✅ | ✅⭐ |
| [Open Notify](http://open-notify.org/Open-Notify-API/) | ISS current location, pass times, and people currently in space | 🟢 No | ❌ | ✅⭐ |
| [N2YO](https://www.n2yo.com/api/) | Real-time satellite tracking with TLE data, positions, and pass predictions | 🟡 API Key | ✅ | ✅ |
| [JPL Horizons](https://ssd-api.jpl.nasa.gov/doc/horizons.html) | Solar system ephemeris computation for planets, moons, asteroids, and comets | 🟢 No | ✅ | ✅ |
| [AstroBin](https://www.astrobin.com/help/api/) | Read-only API for astrophotography images and equipment metadata | 🟡 API Key | ✅ | ✅ |
| [WorldWide Telescope](https://docs.worldwidetelescope.org/) | AAS multi-terabyte astronomical visualization engine with LCAPI and WebGL | 🟢 No | ✅ | ⚠️ |
| [SDSS SkyServer](https://skyserver.sdss.org/dr19/) | Sloan Digital Sky Survey catalog data with SQL-based CasJobs queries | 🟢 No | ✅ | ✅ |
| [Solar System OpenData](https://api.le-systeme-solaire.net/en/) | REST API for planets, moons, dwarf planets, and asteroids with orbital data | 🟢 No | ✅ | ✅⭐ |
| [Space-Track](https://www.space-track.org/documentation) | US Space Command satellite catalog with TLE and orbital element data | 🟡 API Key | ✅ | ✅ |
| [The Space Devs](https://thespacedevs.com/llapi) | Launch Library 2 API for upcoming and historical rocket launches worldwide | 🟢 No | ✅ | ✅⭐ |
| [Astronomy API](https://astronomyapi.com/) | Sun, moon, and planet positions with star charts and moon phase calculations | 🟡 API Key | ✅ | ✅ |

---

## 🌊 Ocean & Marine APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [NOAA Tides & Currents](https://api.tidesandcurrents.noaa.gov/api/prod/) | CO-OPS water level, tide prediction, current, and meteorological data | 🟢 No | ✅ | ✅⭐ |
| [EMODnet](https://emodnet.ec.europa.eu/en/emodnet-web-service-documentation) | European Marine Observation Network with OGC web services for bathymetry | 🟢 No | ✅ | ✅ |
| [Copernicus Marine](https://marine.copernicus.eu/access-data/) | EU ocean monitoring with Toolbox API for temperature, salinity, and currents | 🟡 API Key | ✅ | ✅ |
| [SeaBASS](https://seabass.gsfc.nasa.gov/) | NASA bio-optical marine data archive for satellite validation and algorithms | 🟢 No | ✅ | ⚠️ |
| [MarineTraffic](https://servicedocs.marinetraffic.com/) | AIS vessel tracking with positions, routes, port calls, and vessel events | 🟡 API Key | ✅ | ✅ |
| [VesselFinder](https://api.vesselfinder.com/docs/) | Real-time AIS position, voyage data, and vessel particulars in JSON/XML | 🟡 API Key | ✅ | ✅ |
| [BarentsWatch](https://developer.barentswatch.no/) | Norwegian marine APIs for fish health, AIS, wave forecasts, and aquaculture | 🟡 API Key | ✅ | ✅ |
| [IOC Sea Level](https://api.ioc-sealevelmonitoring.org/) | UNESCO global sea level station monitoring with 1000+ station data feeds | 🟡 API Key | ✅ | ✅ |
| [GEBCO](https://www.gebco.net/data_and_products/gridded_bathymetry_data/) | General Bathymetric Chart of the Oceans with global terrain model downloads | 🟢 No | ✅ | ⚠️ |
| [OceanSITES](https://dods.ndbc.noaa.gov/oceansites/) | Global deep-ocean time series data via GDAC in NetCDF format | 🟢 No | ✅ | ⚠️ |
| [Argo (Argovis)](https://argovis.colorado.edu/) | Global ocean profiling float data with temperature, salinity, and BGC | 🟢 No | ✅ | ✅ |
| [Stormglass](https://stormglass.io/) | Global marine weather data including tides, waves, and weather forecasts | 🟡 API Key | ✅ | ✅⭐ |

---

## 🏛️ Museum & Archive APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Europeana](https://apis.europeana.eu/en) | 50M+ European cultural heritage items with Search, Record, and Entity APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Internet Archive](https://archive.org/developers/) | Wayback Machine, metadata, S3-like storage, and book APIs for digital archives | 🟢 No | ✅ | ✅ |
| [Library of Congress](https://www.loc.gov/apis/) | JSON/YAML API for LOC digital collections, images, text, and streaming media | 🟢 No | ✅ | ✅⭐ |
| [DPLA](https://pro.dp.la/developers/api-codex) | Digital Public Library of America with 40M+ items from US libraries and archives | 🟡 API Key | ✅ | ✅⭐ |
| [Biodiversity Heritage Library](https://www.biodiversitylibrary.org/docs/api3.html) | API v3 for natural history literature with title, author, and part searches | 🟡 API Key | ✅ | ✅ |
| [HathiTrust](https://www.hathitrust.org/member-libraries/resources-for-librarians/data-resources/) | Data and Bibliographic APIs for page images, OCR text, and METS metadata | 🟢 No | ✅ | ✅ |
| [Chronicling America](https://chroniclingamerica.loc.gov/about/api/) | Historic US newspaper pages and metadata via LOC JSON API | 🟢 No | ✅ | ✅⭐ |
| [US National Archives](https://www.archives.gov/developer) | NARA Catalog API for searching, exporting metadata, and posting transcriptions | 🟡 API Key | ✅ | ✅ |
| [UK National Archives](https://www.nationalarchives.gov.uk/help/discovery-for-developers-about-the-application-programming-interface-api/) | Discovery API for 35M+ record descriptions across 2500+ UK institutions | 🟡 API Key | ✅ | ✅ |
| [Gallica (BnF)](https://api.bnf.fr/fr/api-document-de-gallica) | French National Library digital documents, IIIF images, and SRU search | 🟢 No | ✅ | ✅ |
| [Trove](https://trove.nla.gov.au/about/create-something/using-api) | National Library of Australia with books, newspapers, images, and maps | 🟡 API Key | ✅ | ✅ |
| [WorldCat](https://www.oclc.org/developer/api/oclc-apis/worldcat-search-api.en.html) | OCLC global library catalog with search, metadata, and entity APIs | 🟡 API Key | ✅ | ✅ |

---

## 🔬 Research & Academic APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Semantic Scholar](https://api.semanticscholar.org/api-docs/) | AI-powered academic search with 200M+ papers, authors, and citations | 🟢 No | ✅ | ✅⭐ |
| [OpenAlex](https://docs.openalex.org/) | Fully open index of 240M+ scholarly works, authors, sources, and institutions | 🟢 No | ✅ | ✅⭐ |
| [Crossref](https://www.crossref.org/documentation/retrieve-metadata/rest-api/) | DOI metadata retrieval with full-text search across 150M+ scholarly records | 🟢 No | ✅ | ✅⭐ |
| [ORCID](https://info.orcid.org/documentation/) | Researcher identifier registry with OAuth2-based profile and works management | 🔴 OAuth | ✅ | ✅ |
| [Unpaywall](https://unpaywall.org/products/api) | Open access status and full-text links for 30M+ DOI-indexed papers | 🟢 No | ✅ | ✅⭐ |
| [CORE](https://core.ac.uk/documentation/api) | World's largest open access research corpus with full-text and metadata access | 🟡 API Key | ✅ | ✅ |
| [BASE](https://www.api.base-search.net/) | Bielefeld Academic Search Engine indexing 400M+ documents from 12000+ sources | 🟡 API Key | ✅ | ✅ |
| [Dimensions](https://docs.dimensions.ai/dsl/) | Linked research database with DSL query language for pubs, grants, and patents | 🟡 API Key | ✅ | ✅ |
| [PubMed (E-utilities)](https://www.ncbi.nlm.nih.gov/books/NBK25497/) | NCBI Entrez API for searching 36M+ biomedical literature citations | 🟡 API Key | ✅ | ✅⭐ |
| [arXiv](https://info.arxiv.org/help/api/index.html) | Open access preprint repository with Atom-based search API for e-prints | 🟢 No | ✅ | ✅ |
| [DOAJ](https://doaj.org/api/v4/docs) | Directory of Open Access Journals with search and article CRUD endpoints | 🟡 API Key | ✅ | ✅ |
| [Altmetric](https://explorer-api-docs.altmetric.com/) | Research attention data tracking mentions across news, social, and policy sources | 🟡 API Key | ✅ | ✅ |

---

## 🗃️ Data Warehouse & ETL APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Snowflake SQL API](https://docs.snowflake.com/en/developer-guide/sql-api/index) | REST API for executing SQL, checking status, and fetching results concurrently | 🔴 OAuth | ✅ | ✅ |
| [Google BigQuery](https://cloud.google.com/bigquery/docs/reference/rest) | Petabyte-scale analytics warehouse with REST API and Storage Read/Write APIs | 🔴 OAuth | ✅ | ✅ |
| [AWS Redshift Data API](https://docs.aws.amazon.com/redshift/latest/mgmt/data-api.html) | Serverless HTTP API for Redshift SQL execution without persistent connections | 🟡 API Key | ✅ | ✅ |
| [Databricks](https://docs.databricks.com/api/workspace/introduction) | Lakehouse platform REST API for clusters, jobs, notebooks, and SQL warehouses | 🟡 API Key | ✅ | ✅ |
| [Fivetran](https://fivetran.com/docs/rest-api) | Automated data pipeline management with connector, sync, and destination control | 🟡 API Key | ✅ | ✅ |
| [Airbyte](https://docs.airbyte.com/developers/api-documentation) | Open source data integration platform with programmatic source and sync management | 🟡 API Key | ✅ | ✅ |
| [Stitch](https://www.stitchdata.com/docs/integrations/) | Singer-powered ELT with Import API for pushing arbitrary data to warehouses | 🟡 API Key | ✅ | ✅ |
| [dbt Cloud](https://docs.getdbt.com/docs/dbt-cloud-apis/overview) | Administrative, Discovery, and Semantic Layer APIs for data transformation | 🟡 API Key | ✅ | ✅ |
| [Matillion](https://docs.matillion.com/metl/docs/2916124/) | ETL API v1 for programmatic job execution and high-volume data transfers | 🟡 API Key | ✅ | ✅ |
| [Talend](https://talend.qlik.dev/) | Qlik Talend APIs for environments, connections, crawlers, and data management | 🟡 API Key | ✅ | ✅ |
| [Hevo Data](https://api-docs.hevodata.com/reference/introduction) | REST API for pipeline automation, monitoring, and bulk data operations | 🟡 API Key | ✅ | ✅ |
| [Census](https://developers.getcensus.com/embedded/overview) | Reverse ETL management API for syncing warehouse data to SaaS destinations | 🟡 API Key | ✅ | ✅ |

---

## 🧠 Knowledge Management & Wiki APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Confluence](https://developer.atlassian.com/cloud/confluence/rest/v2/) | Atlassian Cloud REST API v2 for spaces, pages, comments, and content management | 🔴 OAuth | ✅ | ✅⭐ |
| [Notion](https://developers.notion.com/) | Create, read, and update databases, pages, and blocks programmatically | 🟡 API Key | ✅ | ✅⭐ |
| [Guru](https://developer.getguru.com/) | REST API for programmatic knowledge card management with team verification | 🟡 API Key | ✅ | ✅ |
| [Slite](https://developers.slite.com/) | OpenAPI v3 interface for document management, search, and markdown content | 🟡 API Key | ✅ | ✅ |
| [Tettra](https://support.tettra.com/api-overview) | Knowledge base API for creating pages, searching content, and asking questions | 🟡 API Key | ✅ | ⚠️ |
| [Document360](https://apidocs.document360.com/apidocs/getting-started) | Knowledge base platform API for articles, categories, and project management | 🟡 API Key | ✅ | ✅ |
| [GitBook](https://developer.gitbook.com/) | REST API for content management, collaboration, and documentation integration | 🟡 API Key | ✅ | ✅ |
| [BookStack](https://demo.bookstackapp.com/api/docs) | Self-hosted wiki REST API for books, chapters, pages, and shelves | 🟡 API Key | ✅ | ✅ |
| [Wiki.js](https://docs.requarks.io/dev/api) | GraphQL API for accessing and modifying all wiki resources with token auth | 🟡 API Key | ✅ | ✅ |
| [MediaWiki](https://www.mediawiki.org/wiki/API:Action_API) | Action API powering Wikipedia for page operations, search, and authentication | 🟢 No | ✅ | ✅⭐ |
| [Nuclino](https://help.nuclino.com/d3a29686-api) | REST API for team wiki content in Markdown with workspace management | 🟡 API Key | ✅ | ✅ |
| [Slab](https://help.slab.com/en/articles/6545629-developer-tools-api-webhooks) | GraphQL API for knowledge base posts, topics, and team collaboration | 🟡 API Key | ✅ | ✅ |

---

## 📊 Survey & Market Research APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Qualtrics](https://api.qualtrics.com/) | Enterprise survey platform API for survey creation, distribution, and responses | 🟡 API Key | ✅ | ✅⭐ |
| [SurveyMonkey](https://api.surveymonkey.com/v3/docs) | REST API v3 with OAuth2 for surveys, collectors, responses, and contacts | 🔴 OAuth | ✅ | ✅ |
| [Typeform](https://www.typeform.com/developers/) | Create, customize, and retrieve responses for conversational forms and surveys | 🔴 OAuth | ✅ | ✅⭐ |
| [Pollfish](https://www.pollfish.com/docs/api-documentation) | Mobile survey platform API for app monetization and audience research | 🟡 API Key | ✅ | ✅ |
| [Cint](https://developer.cint.com/en) | Programmatic research exchange API for the largest global sample marketplace | 🟡 API Key | ✅ | ✅ |
| [Lucid](https://developer.lucidhq.com/) | Marketplace API for automated survey sampling and audience targeting | 🟡 API Key | ✅ | ✅ |
| [Dynata](https://www.dynata.com/) | Global sample provider API for first-party consumer and B2B research data | 🟡 API Key | ✅ | ⚠️ |
| [SurveyJS](https://surveyjs.io/documentation/survey-creator) | Open-source JavaScript library for building self-hosted surveys and forms | 🟢 No | ✅ | ✅ |
| [QuestionPro](https://www.questionpro.com/api/) | Survey creation, distribution, and response collection with v2 REST API | 🟡 API Key | ✅ | ✅ |
| [Alchemer](https://apihelp.alchemer.com/help) | RESTful API for survey CRUD, question management, and response data retrieval | 🟡 API Key | ✅ | ✅ |
| [Forsta](https://www.forsta.com/) | Enterprise experience and research platform with survey and analytics APIs | 🟡 API Key | ✅ | ⚠️ |
| [SurveyLegend](https://www.surveylegend.com/) | Mobile-friendly survey builder with response collection and analytics | 🟡 API Key | ✅ | ⚠️ |

---

## 🏋️ Fitness & Wellness APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Fitbit Web API](https://dev.fitbit.com/build/reference/web-api/) | Activity, sleep, heart rate, and nutrition data from Fitbit devices | 🔴 OAuth | ✅ | ✅⭐ |
| [Strava](https://developers.strava.com/docs/reference/) | GPS activity data, segments, leaderboards, and athlete profiles | 🔴 OAuth | ✅ | ✅⭐ |
| [Apple HealthKit](https://developer.apple.com/documentation/healthkit) | Central health and fitness data repository for iOS, watchOS, and visionOS | 🔴 OAuth | ✅ | ⚠️ |
| [Google Fit](https://developers.google.com/fit) | Android and REST APIs for fitness data aggregation and health metrics | 🔴 OAuth | ✅ | ✅ |
| [Garmin Connect](https://developer.garmin.com/gc-developer-program/) | Activity, health, training, and FIT file data from Garmin wearables | 🔴 OAuth | ✅ | ✅ |
| [WHOOP](https://developer.whoop.com/api/) | Recovery, strain, sleep, and HRV data with OAuth2 and webhooks | 🔴 OAuth | ✅ | ✅ |
| [Oura](https://cloud.ouraring.com/v2/docs) | Ring-based sleep, readiness, and activity insights via REST API v2 | 🔴 OAuth | ✅ | ✅ |
| [Peloton](https://www.peloton.com/) | Connected fitness workout data, performance metrics, and class information | 🟡 API Key | ✅ | ⚠️ |
| [MyFitnessPal](https://www.myfitnesspal.com/apps/api/version) | Nutrition tracking with 14M+ food item database for calorie and macro logging | 🔴 OAuth | ✅ | ⚠️ |
| [Cronometer](https://cronometer.com/) | Detailed micronutrient tracking with verified nutrition data via partner APIs | 🟡 API Key | ✅ | ⚠️ |
| [Nutritionix](https://developer.nutritionix.com/) | 800K+ food item database with natural language nutrition parsing | 🟡 API Key | ✅ | ✅⭐ |
| [Withings](https://developer.withings.com/api-reference/) | Medical-grade health metrics from scales, watches, and blood pressure monitors | 🔴 OAuth | ✅ | ✅ |

---

## 🎲 Random & Fun APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Random.org](https://api.random.org/json-rpc/2/basic) | True random number generation from atmospheric noise via JSON-RPC | 🟡 API Key | ✅ | ✅⭐ |
| [Fun Translations](https://funtranslations.com/api) | 72+ translators including Yoda, Pirate, Shakespeare, and Pig Latin | 🟢 No | ✅ | ✅⭐ |
| [Advice Slip](https://api.adviceslip.com/) | Random advice slips and search for advice by keyword | 🟢 No | ✅ | ✅⭐ |
| [Bored API](https://www.boredapi.com/documentation) | Random activity suggestions when you have nothing to do | 🟢 No | ✅ | ✅⭐ |
| [Chuck Norris](https://api.chucknorris.io/) | Hand-curated Chuck Norris jokes with categories and free text search | 🟢 No | ✅ | ✅⭐ |
| [Kanye.rest](https://kanye.rest/) | Random Kanye West quotes delivered as JSON via Cloudflare Workers | 🟢 No | ✅ | ✅⭐ |
| [Cat Facts](https://catfact.ninja/) | Random cat facts with pagination and breed information | 🟢 No | ✅ | ✅⭐ |
| [Dog API](https://dog.ceo/dog-api/) | Random dog images by breed with 20,000+ photos from Stanford dataset | 🟢 No | ✅ | ✅⭐ |
| [Useless Facts](https://uselessfacts.jsph.pl/) | Random real-world trivia facts in JSON format, daily or random | 🟢 No | ✅ | ✅⭐ |
| [Numbers API](http://numbersapi.com/) | Interesting math, date, year, and trivia facts about numbers | 🟢 No | ❌ | ✅⭐ |
| [Open Trivia DB](https://opentdb.com/api_config.php) | User-contributed trivia questions with categories, difficulty, and answer types | 🟢 No | ✅ | ✅⭐ |
| [JokeAPI](https://jokeapi.dev/) | Jokes in multiple categories and languages with custom filtering options | 🟢 No | ✅ | ✅⭐ |

---

## 🌐 CDN & Edge Computing APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Cloudflare](https://developers.cloudflare.com/api/) | CDN, DNS, Workers edge computing, and security with comprehensive REST API | 🟡 API Key | ✅ | ✅⭐ |
| [Fastly](https://www.fastly.com/documentation/reference/api/) | Programmable edge cloud with real-time purging, VCL, and Compute@Edge | 🟡 API Key | ✅ | ✅⭐ |
| [Akamai](https://techdocs.akamai.com/home/page/apis) | Global CDN with EdgeGrid-authenticated APIs for property, purge, and WAF management | 🟡 API Key | ✅ | ✅ |
| [AWS CloudFront](https://docs.aws.amazon.com/cloudfront/latest/APIReference/Welcome.html) | AWS CDN with distribution management, invalidation, and CloudFront Functions | 🟡 API Key | ✅ | ✅ |
| [Azure CDN](https://learn.microsoft.com/en-us/rest/api/cdn/) | Microsoft CDN REST API for profile, endpoint, and custom domain management | 🔴 OAuth | ✅ | ✅ |
| [Google Cloud CDN](https://cloud.google.com/cdn/docs/apis) | Google's edge caching with backend service, URL map, and cache invalidation APIs | 🔴 OAuth | ✅ | ✅ |
| [StackPath](https://stackpath.dev/docs) | Edge computing platform with CDN, WAF, and serverless scripting APIs | 🟡 API Key | ✅ | ✅ |
| [KeyCDN](https://www.keycdn.com/api) | Pay-per-usage CDN with zone management, purge, and real-time analytics API | 🟡 API Key | ✅ | ✅ |
| [BunnyCDN](https://docs.bunny.net/) | Developer hub with pull zone, storage zone, and stream API documentation | 🟡 API Key | ✅ | ✅⭐ |
| [Imperva](https://docs.imperva.com/bundle/cloud-application-security) | Cloud WAF and CDN with site management, rules, and cache control APIs | 🟡 API Key | ✅ | ✅ |
| [Limelight (Edgio)](https://docs.edg.io/) | Edge platform with CDN, security, and serverless compute APIs | 🟡 API Key | ✅ | ✅ |
| [Netlify](https://open-api.netlify.com/) | JAMstack deployment platform with Edge Functions, forms, and build hook APIs | 🟡 API Key | ✅ | ✅⭐ |

---

## 🔑 Authentication & Identity APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Auth0](https://auth0.com/docs) | Universal login, MFA, and identity management with Management and Auth APIs | 🔴 OAuth | ✅ | ✅⭐ |
| [Okta](https://developer.okta.com/docs/reference/api/authn/) | Enterprise identity with Authentication, Users, Groups, and Policy APIs | 🟡 API Key | ✅ | ✅⭐ |
| [Firebase Auth](https://firebase.google.com/docs/auth) | Google-backed authentication with email, phone, social, and anonymous sign-in | 🟡 API Key | ✅ | ✅⭐ |
| [Clerk](https://clerk.com/docs) | React and Next.js-first auth with pre-built UI components and session management | 🟡 API Key | ✅ | ✅⭐ |
| [Stytch](https://stytch.com/docs) | Passwordless auth platform with passkeys, magic links, OTP, and OAuth APIs | 🟡 API Key | ✅ | ✅ |
| [WorkOS](https://workos.com/docs) | Enterprise SSO, Directory Sync, and Admin Portal for B2B applications | 🟡 API Key | ✅ | ✅ |
| [FusionAuth](https://fusionauth.io/docs/) | Self-hosted or cloud auth platform with login, registration, and MFA APIs | 🟡 API Key | ✅ | ✅ |
| [Keycloak](https://www.keycloak.org/docs/latest/server_admin/) | Open source IAM with SSO, identity brokering, and admin REST API | 🟡 API Key | ✅ | ✅ |
| [SuperTokens](https://supertokens.com/docs) | Open source auth with self-hosted UI, session management, and RBAC | 🟡 API Key | ✅ | ✅ |
| [Descope](https://docs.descope.com/) | No-code/low-code auth flows with drag-and-drop workflow builder and APIs | 🟡 API Key | ✅ | ✅ |
| [Passage](https://docs.passage.id/home) | 1Password-backed passkey authentication with REST APIs and frontend SDKs | 🟡 API Key | ✅ | ✅ |
| [Ory](https://www.ory.com/docs/kratos/reference/api) | Open source modular identity with Kratos (identity), Hydra (OAuth), and Keto (authz) | 🟡 API Key | ✅ | ✅ |

---

## 📐 CAD & 3D Modeling APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Autodesk Platform Services](https://aps.autodesk.com/en/docs/data/v2/overview/basics) | 50+ APIs for 3D viewing, design automation, data management (formerly Forge) | 🔴 OAuth | ✅ | ✅ |
| [Onshape](https://onshape-public.github.io/docs/) | Full-cloud CAD with REST API for parts, assemblies, drawings, and versioning | 🔴 OAuth | ✅ | ✅⭐ |
| [Trimble Connect](https://developer.trimble.com/docs/connect/model-api/) | Cloud collaboration API for 3D models, project management, and BIM data | 🔴 OAuth | ✅ | ✅ |
| [Speckle](https://docs.speckle.systems/developers/looking-for-developer-docs) | Open source data platform for AEC with connectors for Revit, Rhino, and more | 🟡 API Key | ✅ | ✅ |
| [ShapeDiver](https://help.shapediver.com/doc/shapediver-for-speckle) | Cloud platform for parametric 3D Grasshopper models with viewer API | 🟡 API Key | ✅ | ✅ |
| [Three.js](https://threejs.org/docs/) | JavaScript 3D library for WebGL rendering with extensive scene graph API | 🟢 No | ✅ | ✅⭐ |
| [Babylon.js](https://doc.babylonjs.com/) | Microsoft-backed WebGL/WebGPU engine with scene, mesh, and physics APIs | 🟢 No | ✅ | ✅⭐ |
| [Open3D](https://www.open3d.org/docs/release/) | Open source library for 3D data processing with Python and C++ frontends | 🟢 No | ✅ | ✅ |
| [CesiumJS](https://cesium.com/platform/cesiumjs/) | Open source 3D geospatial visualization with globe, terrain, and 3D Tiles | 🟡 API Key | ✅ | ✅⭐ |
| [Sketchfab](https://sketchfab.com/developers) | 3D model platform API for searching, downloading, and embedding glTF models | 🟡 API Key | ✅ | ✅ |
| [ManifoldCAD](https://manifoldcad.org/) | Open source geometry kernel with Boolean operations for solid 3D modeling | 🟢 No | ✅ | ⚠️ |
| [OpenCascade](https://dev.opencascade.org/doc/overview/html/) | Industrial-strength open source CAD kernel with BREP modeling and STEP I/O | 🟢 No | ✅ | ⚠️ |

---

## 🏘️ Community & HOA Management APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [AppFolio](https://www.appfolio.com/stack/partners/api) | Property management API for units, tenants, leases, and accounting data | 🟡 API Key | ✅ | ✅ |
| [Buildium](https://developer.buildium.com/) | Open API v1 for property, tenant, lease, accounting, and maintenance management | 🟡 API Key | ✅ | ✅⭐ |
| [TownSq](https://townsq.io/) | HOA communication platform with maintenance requests and community announcements | 🟡 API Key | ✅ | ⚠️ |
| [PayHOA](https://www.payhoa.com/) | Cloud-based HOA payment processing with dues collection and financial reporting | 🟡 API Key | ✅ | ⚠️ |
| [CommunityBoss](https://communityboss.com/hoa) | Parking, amenity scheduling, and resident management for HOA communities | 🟡 API Key | ✅ | ⚠️ |
| [Enumerate](https://www.enumerate.com/) | Community association management with accounting, compliance, and communication | 🟡 API Key | ✅ | ⚠️ |
| [ManageCasa](https://managecasa.com/) | All-in-one HOA and rental management with accounting and maintenance automation | 🟡 API Key | ✅ | ⚠️ |
| [HOAlife](https://docs.hoalife.com/) | REST API with scoped CRUD actions for violations, inspections, and compliance | 🟡 API Key | ✅ | ✅ |
| [AvidXchange](https://www.avidxchange.com/) | AP automation platform integrating with Caliber, TOPS, and HOA accounting systems | 🟡 API Key | ✅ | ✅ |
| [TOPS Software](https://topssoft.com/) | Community association management with accounting, violations, and resident portals | 🟡 API Key | ✅ | ⚠️ |
| [Caliber (Frontsteps)](https://frontsteps.com/) | HOA accounting and management platform with integrated access control | 🟡 API Key | ✅ | ⚠️ |
| [Condo Control](https://www.condocontrol.com/) | Condo and HOA management with amenity booking, deliveries, and visitor management | 🟡 API Key | ✅ | ⚠️ |

---

## 🎵 Audio & Sound APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Spotify Web API](https://developer.spotify.com/documentation/web-api/) | Music catalog search, playback control, audio features, and playlist management | 🔴 OAuth | ✅ | ✅⭐ |
| [SoundCloud](https://developers.soundcloud.com/docs/api/guide) | Track search, streaming, user profiles, and playlist management | 🔴 OAuth | ✅ | ✅ |
| [Dolby.io Media](https://docs.dolby.io/media-apis/docs) | Audio enhancement, analysis, transcoding, and loudness normalization APIs | 🟡 API Key | ✅ | ✅ |
| [AudioStack](https://docs.audiostack.ai/) | AI-first platform for producing audio at scale with speech and music generation | 🟡 API Key | ✅ | ✅ |
| [Mubert](https://mubert.com/render/faq) | AI-generated royalty-free music with customizable mood, genre, and duration | 🟡 API Key | ✅ | ✅ |
| [AIVA](https://www.aiva.ai/) | AI composer for emotional soundtrack music across multiple genres and styles | 🟡 API Key | ✅ | ⚠️ |
| [Epidemic Sound](https://developers.epidemicsound.com/docs/) | Partner API for royalty-free music licensing with track search and download | 🟡 API Key | ✅ | ✅ |
| [AudioJungle (Envato)](https://build.envato.com/) | Envato Market API for searching and licensing royalty-free audio tracks | 🔴 OAuth | ✅ | ✅ |
| [Freesound](https://freesound.org/docs/api/) | Collaborative database of Creative Commons licensed sounds with search and download | 🔴 OAuth | ✅ | ✅⭐ |
| [BBC Sound Effects](https://sound-effects.bbcrewind.co.uk/) | 33,000+ BBC sound effects from the Rewind archive available for download | 🟢 No | ✅ | ⚠️ |
| [Descript](https://www.descript.com/) | Transcript-first audio/video editing platform with Overdub AI voice cloning | 🟡 API Key | ✅ | ⚠️ |
| [ElevenLabs](https://elevenlabs.io/docs/api-reference/introduction) | State-of-the-art AI text-to-speech, voice cloning, and audio generation APIs | 🟡 API Key | ✅ | ✅⭐ |

---

## 🏢 Coworking & Space Management APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [OfficeRnD](https://developer.officernd.com/) | Coworking and flex-space management with bookings, members, and billing | 🟡 API Key | ✅ | ✅⭐ |
| [Nexudus](https://developers.nexudus.com/) | White-label coworking platform with CRM, billing, and resource booking | 🟡 API Key | ✅ | ✅⭐ |
| [Cobot](https://www.cobot.me/api-docs) | Coworking management with member plans, check-ins, and invoicing | 🔴 OAuth | ✅ | ✅ |
| [Optix](https://www.optixapp.com/) | Workspace management app with booking, access control, and analytics | 🟡 API Key | ✅ | ✅ |
| [Archie](https://archieapp.co/) | Coworking platform with hot-desk booking, meeting rooms, and member portals | 🟡 API Key | ✅ | ✅ |
| [Satellite Deskworks](https://www.yourcoworkingspace.com/) | Coworking operations software with billing, door access, and utilization reports | 🟡 API Key | ✅ | ⚠️ |
| [Yardi Kube](https://www.yardi.com/products/coworking-software/) | Enterprise coworking and flex-space management within Yardi property ecosystem | 🟡 API Key | ✅ | ⚠️ |
| [Essensys](https://www.essensys.tech/) | Flex workspace technology platform for operators with occupancy and billing APIs | 🟡 API Key | ✅ | ✅ |
| [Proximity](https://www.proximity.space/) | Community-focused coworking management with events, benefits, and member directory | 🟡 API Key | ✅ | ⚠️ |
| [Robin](https://docs.robinpowered.com/) | Hybrid workplace platform for desk booking, room scheduling, and office analytics | 🟡 API Key | ✅ | ✅⭐ |
| [Teem (iOFFICE)](https://www.iofficecorp.com/) | Workplace experience platform with room booking and visitor management | 🟡 API Key | ✅ | ✅ |
| [Kadence](https://www.kadence.co/) | Hybrid work scheduling and desk booking with team coordination features | 🟡 API Key | ✅ | ✅ |

---

## 💎 Jewelry & Luxury Goods APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [RapNet](https://technet.rapaport.com/) | World's largest diamond trading network with real-time pricing and inventory | 🟡 API Key | ✅ | ✅⭐ |
| [Nivoda](https://nivoda.com/) | B2B marketplace API for loose diamonds and gemstones with global inventory | 🟡 API Key | ✅ | ✅⭐ |
| [Stuller](https://www.stuller.com/) | Wholesale jewelry supplier API with product catalog, metals pricing, and orders | 🟡 API Key | ✅ | ✅ |
| [IDEX Online](https://idexonline.com/) | Diamond price index and polished diamond trading platform with market data | 🟡 API Key | ✅ | ✅ |
| [Polygon.io (Metals)](https://polygon.io/) | Real-time and historical precious metals pricing including gold, silver, platinum | 🟡 API Key | ✅ | ✅⭐ |
| [GIA Report Check](https://www.gia.edu/report-check-landing) | Verify GIA diamond grading reports and access certification data | 🟢 No | ✅ | ⚠️ |
| [Valigara](https://www.valigara.com/) | Multi-channel jewelry e-commerce management with inventory sync and listing | 🟡 API Key | ✅ | ✅ |
| [JewelCloud](https://jewelcloud.com/) | Diamond and jewelry virtual inventory platform connecting retailers and suppliers | 🟡 API Key | ✅ | ✅ |
| [Kitco](https://www.kitco.com/) | Precious metals market data with spot prices, charts, and news feeds | 🟢 No | ✅ | ⚠️ |
| [Rapaport Price List](https://www.diamonds.net/) | Industry-standard diamond pricing benchmark updated weekly | 🟡 API Key | ✅ | ✅ |
| [VDB (Virtual Diamond Boutique)](https://www.vfrapp.com/) | 3D diamond and jewelry visualization platform for virtual try-on | 🟡 API Key | ✅ | ⚠️ |
| [Gemological Institute](https://aglgemlab.com/) | Colored gemstone identification and grading report verification | 🟡 API Key | ✅ | ⚠️ |

---

## 🌾 Agriculture & Farming APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [aWhere](https://www.awhere.com/) | Hyperlocal weather, agronomic models, and field-level crop insights | 🟡 API Key | ✅ | ✅⭐ |
| [Planet Labs (Agriculture)](https://developers.planet.com/) | Daily satellite imagery for crop monitoring, yield prediction, and land analysis | 🟡 API Key | ✅ | ✅⭐ |
| [CropIn](https://www.cropin.com/) | AI-powered agri-intelligence platform with crop monitoring and farm management | 🟡 API Key | ✅ | ✅ |
| [Agworld](https://www.agworld.com/) | Farm management platform with field records, budgets, and agronomic planning | 🟡 API Key | ✅ | ✅ |
| [FarmLogs (Bushel)](https://bushelpowered.com/) | Grain marketing and farm management with field tracking and market data | 🟡 API Key | ✅ | ✅ |
| [Arable](https://www.arable.com/developer) | In-field crop and weather sensing with evapotranspiration and growth stage data | 🟡 API Key | ✅ | ✅⭐ |
| [OneSoil](https://onesoil.ai/) | Free satellite-based crop monitoring with field boundaries and vegetation indices | 🟢 No | ✅ | ✅ |
| [Agrimap](https://www.agrimap.com/) | Precision agriculture mapping with soil analysis and variable-rate prescriptions | 🟡 API Key | ✅ | ⚠️ |
| [USDA NASS](https://quickstats.nass.usda.gov/api/) | US agricultural statistics including crop production, prices, and census data | 🟡 API Key | ✅ | ✅⭐ |
| [Open Food Facts](https://world.openfoodfacts.org/data) | Collaborative food product database with ingredients, nutrition, and labels | 🟢 No | ✅ | ✅⭐ |
| [Cropwise (Syngenta)](https://www.cropwise.com/) | Digital agriculture platform for crop protection recommendations and field scouting | 🟡 API Key | ✅ | ✅ |
| [FarmHack](https://farmhack.org/) | Open-source farm tool and knowledge sharing community with project APIs | 🟢 No | ✅ | ⚠️ |

---

## 🏭 Manufacturing & Industrial IoT APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Siemens MindSphere](https://developer.mindsphere.io/) | Industrial IoT platform for asset monitoring, predictive maintenance, and analytics | 🟡 API Key | ✅ | ✅⭐ |
| [AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/) | Collect, organize, and analyze industrial equipment data at scale | 🟡 API Key | ✅ | ✅⭐ |
| [Samsara](https://developers.samsara.com/) | Fleet and industrial IoT platform with sensors, telematics, and workflows | 🟡 API Key | ✅ | ✅⭐ |
| [PTC ThingWorx](https://developer.thingworx.com/) | Industrial IoT platform for connected product and factory applications | 🟡 API Key | ✅ | ✅ |
| [Tulip](https://support.tulip.co/docs/tulip-api) | No-code manufacturing app platform with machine monitoring and quality workflows | 🟡 API Key | ✅ | ✅ |
| [MachineMetrics](https://www.machinemetrics.com/) | Real-time machine monitoring and analytics for CNC and manufacturing equipment | 🟡 API Key | ✅ | ✅ |
| [Litmus Edge](https://litmus.io/) | Industrial IoT edge platform for OT data collection and integration | 🟡 API Key | ✅ | ✅ |
| [Fictiv](https://www.fictiv.com/api) | On-demand manufacturing platform API for quoting, ordering, and tracking parts | 🟡 API Key | ✅ | ✅ |
| [Xometry](https://www.xometry.com/) | Instant quoting and ordering for CNC, 3D printing, and injection molding | 🟡 API Key | ✅ | ✅ |
| [Sight Machine](https://sightmachine.com/) | Manufacturing analytics platform with AI-driven plant floor visibility | 🟡 API Key | ✅ | ⚠️ |
| [Uptake](https://www.uptake.com/) | Industrial AI platform for asset performance management and predictive analytics | 🟡 API Key | ✅ | ⚠️ |
| [Augury](https://www.augury.com/) | Machine health monitoring using vibration and temperature AI diagnostics | 🟡 API Key | ✅ | ✅ |

---

## 🎰 Casino & Gaming Regulation APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [GLI (Gaming Laboratories)](https://gaminglabs.com/) | Gaming device testing and certification status verification | 🟡 API Key | ✅ | ⚠️ |
| [Hub88](https://hub88.io/) | iGaming aggregation platform with casino game integration and wallet management | 🟡 API Key | ✅ | ✅⭐ |
| [SoftSwiss](https://www.softswiss.com/) | Online casino platform with game aggregation, bonus engine, and compliance tools | 🟡 API Key | ✅ | ✅ |
| [EveryMatrix](https://everymatrix.com/) | B2B iGaming platform with casino, sportsbook, and payment integration | 🟡 API Key | ✅ | ✅ |
| [BetConstruct](https://www.betconstruct.com/) | Full-stack gaming platform with sportsbook, casino, and poker APIs | 🟡 API Key | ✅ | ✅ |
| [Pragmatic Play](https://www.pragmaticplay.com/) | Leading slot and live casino game provider with seamless integration API | 🟡 API Key | ✅ | ✅ |
| [Evolution Gaming](https://www.evolution.com/) | Live casino streaming platform with game history and table management APIs | 🟡 API Key | ✅ | ✅ |
| [Microgaming](https://www.microgaming.co.uk/) | Pioneer casino game supplier with massive portfolio and progressive jackpot network | 🟡 API Key | ✅ | ⚠️ |
| [Playtech](https://www.playtech.com/) | Enterprise gaming platform with omni-channel casino and sports integration | 🟡 API Key | ✅ | ✅ |
| [iSoftBet](https://www.isoftbet.com/) | Online casino game aggregation with GAP platform for multi-provider integration | 🟡 API Key | ✅ | ✅ |
| [Slotegrator](https://slotegrator.pro/) | Turnkey casino solution with 15,000+ games and unified integration API | 🟡 API Key | ✅ | ✅ |
| [GammaStack](https://www.gammastack.com/) | Custom iGaming development platform with sports betting and casino APIs | 🟡 API Key | ✅ | ⚠️ |

---

## 🧹 Cleaning & Facility Services APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Jobber](https://developer.getjobber.com/) | Field service management with scheduling, quoting, invoicing, and client CRM | 🔴 OAuth | ✅ | ✅⭐ |
| [Deputy](https://developer.deputy.com/) | Workforce management with shift scheduling, time tracking, and team communication | 🟡 API Key | ✅ | ✅⭐ |
| [ZenMaid](https://www.zenmaid.com/) | Maid service software with booking, scheduling, payroll, and customer management | 🟡 API Key | ✅ | ✅ |
| [Swept](https://www.sweptworks.com/) | Janitorial management platform with inspections, time tracking, and communication | 🟡 API Key | ✅ | ⚠️ |
| [CleanGuru](https://www.cleanguru.net/) | Bidding and workloading calculator for cleaning businesses with job estimation | 🟡 API Key | ✅ | ⚠️ |
| [Connecteam](https://developer.connecteam.com/) | All-in-one employee app with scheduling, time clock, forms, and task management | 🟡 API Key | ✅ | ✅ |
| [ServiceM8](https://developer.servicem8.com/) | Field service management with job dispatch, quotes, invoices, and GPS tracking | 🟡 API Key | ✅ | ✅ |
| [Loc8](https://loc8.com/) | Asset and maintenance management with work orders and preventive schedules | 🟡 API Key | ✅ | ✅ |
| [FMX (Facilities Management eXpress)](https://www.gofmx.com/) | Maintenance and facilities request management with work order tracking | 🟡 API Key | ✅ | ✅ |
| [UpKeep](https://developer.onupkeep.com/) | Mobile-first CMMS for maintenance management with asset tracking and work orders | 🟡 API Key | ✅ | ✅⭐ |
| [Limble CMMS](https://limblecmms.com/) | Computerized maintenance management with preventive maintenance and asset tracking | 🟡 API Key | ✅ | ✅ |
| [Fiix (Rockwell)](https://www.fiixsoftware.com/) | AI-powered CMMS for maintenance scheduling, parts management, and analytics | 🟡 API Key | ✅ | ✅ |

---

## 📻 Radio & Broadcast APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [TuneIn](https://tunein.com/broadcasters/) | Access live radio streams, podcasts, and station metadata from 100,000+ stations | 🟡 API Key | ✅ | ✅ |
| [Spreaker](https://developers.spreaker.com/) | Podcast hosting and distribution platform with episode management and analytics | 🔴 OAuth | ✅ | ✅⭐ |
| [Radio Garden](http://radio.garden/) | Explore live radio stations globally on an interactive globe interface | 🟢 No | ✅ | ⚠️ |
| [Dirble](https://dirble.com/developer/api) | Internet radio station directory with stream URLs and metadata search | 🟡 API Key | ✅ | ✅ |
| [RadioBrowser](https://www.radio-browser.info/) | Community-maintained open database of internet radio stations worldwide | 🟢 No | ✅ | ✅⭐ |
| [Icecast](https://icecast.org/) | Open-source streaming media server with directory and statistics APIs | 🟢 No | ✅ | ✅ |
| [SHOUTcast](https://www.shoutcast.com/) | Internet radio streaming platform with station directory and stream management | 🟡 API Key | ✅ | ✅ |
| [Podcast Index](https://podcastindex.org/) | Open podcast search engine with 4M+ podcasts, episodes, and value4value support | 🟡 API Key | ✅ | ✅⭐ |
| [NPR One](https://dev.npr.org/) | NPR personalized listening experience with story recommendations and playback | 🔴 OAuth | ✅ | ✅ |
| [BBC Sounds](https://www.bbc.co.uk/sounds) | BBC radio programs, podcasts, and music mixes with scheduling data | 🟢 No | ✅ | ⚠️ |
| [Radioline](https://www.radioline.co/) | Multi-platform radio and podcast aggregator with worldwide station discovery | 🟡 API Key | ✅ | ✅ |
| [StreamGuys](https://www.streamguys.com/) | Enterprise audio streaming with CDN, monetization, and analytics APIs | 🟡 API Key | ✅ | ⚠️ |

---

## ⛰️ Outdoor & Adventure APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [OpenSnow](https://opensnow.com/) | Ski and snow forecasts with resort-level powder alerts and historical data | 🟡 API Key | ✅ | ✅ |
| [Strava](https://developers.strava.com/) | Social fitness platform with GPS activity tracking, segments, and athlete data | 🔴 OAuth | ✅ | ✅⭐ |
| [Outdooractive](https://developers.outdooractive.com/) | Outdoor recreation platform with hiking, biking, and ski touring routes worldwide | 🟡 API Key | ✅ | ✅⭐ |
| [AllTrails](https://www.alltrails.com/) | Trail discovery platform with 400,000+ hiking, biking, and running trails | 🟡 API Key | ✅ | ✅ |
| [Mountain Project](https://www.mountainproject.com/data) | Rock climbing route database with ratings, photos, and location data | 🟡 API Key | ✅ | ✅ |
| [REI Co-op](https://www.rei.com/) | Outdoor retail product catalog with gear specs and availability | 🟡 API Key | ✅ | ⚠️ |
| [Windy](https://api.windy.com/) | Advanced weather visualization with wind, waves, and paragliding forecasts | 🟡 API Key | ✅ | ✅⭐ |
| [Avalanche.org](https://avalanche.org/) | US avalanche forecasts and observations from regional avalanche centers | 🟢 No | ✅ | ✅ |
| [Komoot](https://developer.komoot.com/) | Route planning and navigation for hiking, cycling, and mountain biking | 🔴 OAuth | ✅ | ✅ |
| [PeakVisor](https://peakvisor.com/) | Mountain identification and 3D panorama maps with peak database | 🟡 API Key | ✅ | ✅ |
| [Campflare](https://www.campflare.com/) | Campground availability monitoring and booking data for national parks | 🟡 API Key | ✅ | ✅ |
| [Recreation.gov](https://ridb.recreation.gov/) | Federal recreation areas, campgrounds, and permit availability data | 🟡 API Key | ✅ | ✅⭐ |

---

## 🧸 Toy & Children Product APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Amazon Product Advertising](https://webservices.amazon.com/paapi5/documentation/) | Product search and detail retrieval for toys, games, and children's products | 🟡 API Key | ✅ | ✅⭐ |
| [eBay Browse API](https://developer.ebay.com/api-docs/buy/browse/overview.html) | Search and browse toy listings with pricing, condition, and seller data | 🔴 OAuth | ✅ | ✅⭐ |
| [CPSC (Consumer Product Safety)](https://www.cpsc.gov/Recalls/CPSC-Recalls-Application-Program-Interface) | Product recall data including toys and children's product safety alerts | 🟢 No | ✅ | ✅⭐ |
| [UPC Database](https://upcdatabase.org/api) | Barcode lookup for toy products with manufacturer and product details | 🟡 API Key | ✅ | ✅ |
| [BoardGameGeek](https://boardgamegeek.com/wiki/page/BGG_XML_API2) | Board game database with ratings, reviews, and collection management | 🟢 No | ✅ | ✅⭐ |
| [LEGO Rebrickable](https://rebrickable.com/api/) | LEGO set database with parts inventories, colors, and minifigure data | 🟡 API Key | ✅ | ✅⭐ |
| [TCGplayer](https://docs.tcgplayer.com/) | Trading card game marketplace with pricing, inventory, and product data | 🟡 API Key | ✅ | ✅ |
| [Brickset](https://brickset.com/article/52664/brickset-api-version-3) | Comprehensive LEGO set database with themes, years, prices, and images | 🟡 API Key | ✅ | ✅ |
| [Toy Retailers Association](https://www.toyretailersassociation.co.uk/) | UK toy industry data and trending toys information | 🟢 No | ✅ | ⚠️ |
| [PriceCharting](https://www.pricecharting.com/api-documentation) | Collectible toy and game price guide with historical market values | 🟡 API Key | ✅ | ✅ |
| [Scryfall](https://scryfall.com/docs/api) | Magic: The Gathering card database with imagery, pricing, and rulings | 🟢 No | ✅ | ✅⭐ |
| [Pokemon TCG API](https://pokemontcg.io/) | Pokemon trading card game database with card data, sets, and types | 🟡 API Key | ✅ | ✅⭐ |

---

## 🔋 Battery & EV Charging APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Open Charge Map](https://openchargemap.org/site/develop/api) | Crowdsourced global EV charging station registry with 300,000+ locations | 🟡 API Key | ✅ | ✅⭐ |
| [Enode](https://developers.enode.com/) | Unified API for EV charging, solar, and battery integrations across brands | 🟡 API Key | ✅ | ✅⭐ |
| [ChargePoint](https://developer.chargepoint.com/) | Largest EV charging network with station availability and session management | 🟡 API Key | ✅ | ✅⭐ |
| [Tesla Fleet API](https://developer.tesla.com/) | Vehicle and charging data with Supercharger network status and energy products | 🔴 OAuth | ✅ | ✅ |
| [EVgo](https://www.evgo.com/) | Fast charging network with station availability and pricing data | 🟡 API Key | ✅ | ✅ |
| [Electrify America](https://www.electrifyamerica.com/) | Ultra-fast EV charging network with real-time station status and pricing | 🟡 API Key | ✅ | ✅ |
| [OCPI (Open Charge Point Interface)](https://evroaming.org/) | Standard protocol for EV roaming between charging networks | 🟡 API Key | ✅ | ✅ |
| [Smartcar](https://smartcar.com/docs/api/) | Unified EV API for battery level, charging status, and vehicle data across makes | 🔴 OAuth | ✅ | ✅⭐ |
| [Wallbox](https://wallbox.com/) | Home and commercial EV charger management with scheduling and energy control | 🟡 API Key | ✅ | ✅ |
| [Zap-Map](https://www.zap-map.com/) | UK EV charging point database with availability, connector types, and routing | 🟡 API Key | ✅ | ✅ |
| [Shell Recharge](https://developer.shellrecharge.com/) | Global EV charging network with roaming, session data, and tariff information | 🟡 API Key | ✅ | ✅ |
| [IONITY](https://ionity.eu/) | European high-power charging network with real-time station availability | 🟡 API Key | ✅ | ✅ |

---

## 💇 Beauty & Salon APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Zenoti](https://docs.zenoti.com/) | Enterprise salon and spa management with appointments, POS, and marketing | 🟡 API Key | ✅ | ✅⭐ |
| [Mindbody](https://developers.mindbodyonline.com/) | Wellness business platform with booking, payments, and staff management | 🔴 OAuth | ✅ | ✅⭐ |
| [Square Appointments](https://developer.squareup.com/) | Booking and POS platform for beauty professionals with integrated payments | 🔴 OAuth | ✅ | ✅⭐ |
| [Vagaro](https://www.vagaro.com/) | Salon, spa, and fitness booking platform with client management and POS | 🟡 API Key | ✅ | ✅ |
| [Booksy](https://www.booksy.com/) | Beauty service marketplace with appointment booking and business management | 🟡 API Key | ✅ | ✅ |
| [Fresha](https://www.fresha.com/) | Free salon software with online booking, POS, and payment processing | 🟡 API Key | ✅ | ✅ |
| [Boulevard](https://developer.joinblvd.com/) | Premium salon and spa management platform with self-booking and duo scheduling | 🟡 API Key | ✅ | ✅⭐ |
| [GlossGenius](https://www.glossgenius.com/) | Beauty professional platform with booking, payments, and client management | 🟡 API Key | ✅ | ⚠️ |
| [Phorest](https://www.phorest.com/) | Salon management software with client retention tools and marketing automation | 🟡 API Key | ✅ | ✅ |
| [Treatwell](https://www.treatwell.co.uk/) | European beauty booking marketplace with salon discovery and appointment APIs | 🟡 API Key | ✅ | ✅ |
| [StyleSeat](https://www.styleseat.com/) | Beauty professional marketplace with booking, payments, and client management | 🟡 API Key | ✅ | ⚠️ |
| [Rosy Salon Software](https://www.rosysalonsoftware.com/) | Cloud salon management with scheduling, inventory, and marketing tools | 🟡 API Key | ✅ | ⚠️ |

---

## ❄️ Cold Chain & Temperature Monitoring APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Monnit](https://www.monnit.com/support/api/) | Wireless sensor monitoring with temperature, humidity, and environmental alerts | 🟡 API Key | ✅ | ✅⭐ |
| [DeltaTrak](https://www.deltatrak.com/) | Cold chain monitoring with real-time temperature tracking and compliance reports | 🟡 API Key | ✅ | ✅ |
| [Sensitech (Carrier)](https://www.sensitech.com/) | End-to-end cold chain visibility with in-transit temperature monitoring | 🟡 API Key | ✅ | ✅ |
| [Emerson Cargo Solutions](https://www.emerson.com/) | Cold chain tracking with GO real-time loggers and data analytics platform | 🟡 API Key | ✅ | ✅ |
| [Tive](https://www.tive.com/) | Real-time supply chain and cold chain tracking with multi-sensor trackers | 🟡 API Key | ✅ | ✅⭐ |
| [Controlant](https://controlant.com/) | Pharma cold chain monitoring with real-time visibility and automated compliance | 🟡 API Key | ✅ | ✅ |
| [ELPRO](https://www.elpro.com/) | Temperature monitoring and validation for pharma and life science cold chains | 🟡 API Key | ✅ | ⚠️ |
| [Onset HOBO](https://www.onsetcomp.com/) | Environmental data loggers with cloud-connected temperature and humidity sensors | 🟡 API Key | ✅ | ✅ |
| [SenseAnywhere](https://www.senseanywhere.com/) | Wireless monitoring system for temperature-critical environments with cloud API | 🟡 API Key | ✅ | ✅ |
| [SmartSense (Digi)](https://www.smartsense.com/) | IoT condition monitoring for food safety, pharmacy, and healthcare compliance | 🟡 API Key | ✅ | ✅ |
| [Dickson](https://www.dicksondata.com/) | Data logger and environmental monitoring with cloud platform and alerting | 🟡 API Key | ✅ | ✅ |
| [Logmore](https://www.logmore.com/) | QR-based environmental data loggers with cloud dashboard for cold chain | 🟡 API Key | ✅ | ✅ |

---

## 📝 Certification & E-Exam APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [ClassMarker](https://www.classmarker.com/online-testing/api/) | Online exam platform with auto-grading, question banks, and result analytics | 🟡 API Key | ✅ | ✅⭐ |
| [Honorlock](https://honorlock.com/) | AI-powered online exam proctoring with browser lockdown and behavior analysis | 🟡 API Key | ✅ | ✅ |
| [ProctorU (Meazure Learning)](https://www.meazurelearning.com/) | Live and AI proctoring for online exams with identity verification | 🟡 API Key | ✅ | ✅ |
| [ExamSoft (Turnitin)](https://examsoft.com/) | Secure exam platform with offline testing, analytics, and accreditation support | 🟡 API Key | ✅ | ⚠️ |
| [Questionmark](https://www.questionmark.com/) | Enterprise assessment platform with item banking, delivery, and psychometrics | 🟡 API Key | ✅ | ✅ |
| [Certiport (Pearson)](https://certiport.pearsonvue.com/) | IT certification exam delivery for Microsoft, Adobe, and other vendor programs | 🟡 API Key | ✅ | ⚠️ |
| [Credly](https://developers.credly.com/) | Digital badge and credential platform with issuing, verification, and sharing | 🟡 API Key | ✅ | ✅⭐ |
| [Accredible](https://accredible.com/docs/api/) | Digital certificates and badges with blockchain verification and analytics | 🟡 API Key | ✅ | ✅⭐ |
| [Testgorilla](https://www.testgorilla.com/) | Pre-employment assessment platform with skills tests and candidate evaluation | 🟡 API Key | ✅ | ✅ |
| [Caveon](https://www.caveon.com/) | Exam security and test development platform with item exposure analytics | 🟡 API Key | ✅ | ⚠️ |
| [Prometric](https://www.prometric.com/) | Global test center network for professional certification exam delivery | 🟡 API Key | ✅ | ⚠️ |
| [Badgr](https://badgr.com/docs/) | Open Badges platform for issuing, collecting, and sharing digital credentials | 🔴 OAuth | ✅ | ✅⭐ |

---

## 🛰️ Satellite & Remote Sensing APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Planet Labs](https://developers.planet.com/) | Daily satellite imagery of Earth with global coverage and 3m resolution | 🟡 API Key | ✅ | ✅⭐ |
| [Sentinel Hub](https://www.sentinel-hub.com/) | Multi-source satellite imagery processing with on-the-fly analysis and rendering | 🟡 API Key | ✅ | ✅⭐ |
| [Google Earth Engine](https://developers.google.com/earth-engine/) | Planetary-scale geospatial analysis platform with 40+ years of satellite data | 🔴 OAuth | ✅ | ✅⭐ |
| [Maxar](https://www.maxar.com/products/imagery) | High-resolution satellite imagery (30cm) with 3D elevation and change detection | 🟡 API Key | ✅ | ✅ |
| [Airbus Defence & Space](https://www.intelligence-airbusds.com/) | Optical and radar satellite imagery with Pleiades and SPOT constellation data | 🟡 API Key | ✅ | ✅ |
| [UP42](https://docs.up42.com/) | Geospatial marketplace and platform for satellite data processing and analytics | 🟡 API Key | ✅ | ✅⭐ |
| [Spire Global](https://spire.com/) | Maritime, aviation, and weather satellite data from proprietary nanosatellite constellation | 🟡 API Key | ✅ | ✅ |
| [EOSDIS (NASA)](https://earthdata.nasa.gov/eosdis/daacs) | NASA Earth science data from multiple satellite missions and instruments | 🟢 No | ✅ | ✅⭐ |
| [Copernicus Open Access Hub](https://scihub.copernicus.eu/) | Free Sentinel satellite data with systematic global coverage for land and ocean | 🟢 No | ✅ | ✅⭐ |
| [Descartes Labs](https://descarteslabs.com/) | Cloud-native geospatial platform for satellite imagery analysis and modeling | 🟡 API Key | ✅ | ✅ |
| [SkyWatch](https://www.skywatch.com/) | Satellite imagery aggregator with multi-source data access and processing | 🟡 API Key | ✅ | ✅ |
| [Orbital Insight](https://orbitalinsight.com/) | Geospatial analytics using satellite and aerial imagery with AI-driven insights | 🟡 API Key | ✅ | ⚠️ |

---

## 🍷 Wine & Spirits APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [Wine-Searcher](https://www.wine-searcher.com/ws-api) | Global wine price comparison with 18M+ listings and merchant data | 🟡 API Key | ✅ | ✅⭐ |
| [Vivino](https://www.vivino.com/) | World's largest wine marketplace with ratings, reviews, and food pairing data | 🟡 API Key | ✅ | ✅ |
| [Global Wine Score](https://www.globalwinescore.com/api/) | Aggregated wine scores from top critics normalized to a single 100-point scale | 🟡 API Key | ✅ | ✅⭐ |
| [Wine.com](https://api.wine.com/) | Online wine retailer with product catalog, ratings, and recommendation engine | 🟡 API Key | ✅ | ✅ |
| [CellarTracker](https://www.cellartracker.com/) | Community wine database with 10M+ tasting notes and cellar management | 🟢 No | ✅ | ⚠️ |
| [Distiller](https://distiller.com/) | Spirits review platform with whiskey, bourbon, and craft spirit ratings | 🟡 API Key | ✅ | ✅ |
| [Open Food Facts (Wine)](https://world.openfoodfacts.org/) | Open database with wine product data including labels, origins, and ingredients | 🟢 No | ✅ | ✅⭐ |
| [LCBO API](https://lcboapi.com/) | Ontario's liquor store product inventory with pricing and availability | 🟡 API Key | ✅ | ✅ |
| [Untappd](https://untappd.com/api/docs) | Social beer and spirits platform with check-ins, venue data, and ratings | 🔴 OAuth | ✅ | ✅ |
| [BreweryDB](https://www.brewerydb.com/developers) | Beer and brewery database with styles, ingredients, and location data | 🟡 API Key | ✅ | ✅ |
| [TheDrinksBusiness](https://www.thedrinksbusiness.com/) | Drinks industry news and market data for wine, beer, and spirits | 🟢 No | ✅ | ⚠️ |
| [Vinmonopolet](https://www.vinmonopolet.no/) | Norwegian alcohol retail monopoly with product catalog and store data | 🟢 No | ✅ | ✅ |

---

## 🔧 Plumbing & HVAC APIs

| API | Description | Auth | HTTPS | Agent-Friendly |
|-----|-------------|------|-------|----------------|
| [ServiceTitan](https://developer.servicetitan.io/) | All-in-one field service platform for plumbing, HVAC, and electrical businesses | 🟡 API Key | ✅ | ✅⭐ |
| [Jobber](https://developer.getjobber.com/) | Home service management with quoting, scheduling, invoicing, and CRM | 🔴 OAuth | ✅ | ✅⭐ |
| [FieldEdge](https://fieldedge.com/) | Service management for HVAC and plumbing with dispatch, invoicing, and reporting | 🟡 API Key | ✅ | ✅ |
| [Housecall Pro](https://www.housecallpro.com/) | Home service business platform with online booking, dispatching, and payments | 🟡 API Key | ✅ | ✅ |
| [Successware](https://successware.com/) | Contractor business management for HVAC, plumbing, and electrical with flat-rate pricing | 🟡 API Key | ✅ | ⚠️ |
| [Service Fusion](https://www.servicefusion.com/) | Field service management with GPS tracking, estimates, and customer management | 🟡 API Key | ✅ | ✅ |
| [Ecobee](https://www.ecobee.com/developers/) | Smart thermostat API with temperature data, HVAC runtime, and occupancy sensing | 🔴 OAuth | ✅ | ✅⭐ |
| [Nest (Google)](https://developers.google.com/nest) | Smart home thermostat and HVAC control with energy usage and temperature data | 🔴 OAuth | ✅ | ✅⭐ |
| [Honeywell Home](https://developer.honeywellhome.com/) | Connected thermostat and home comfort API with HVAC system monitoring | 🔴 OAuth | ✅ | ✅ |
| [Carrier HVAC](https://www.carrier.com/) | Commercial HVAC system monitoring with building automation integration | 🟡 API Key | ✅ | ⚠️ |
| [Trane (Trane Technologies)](https://www.trane.com/) | HVAC equipment monitoring and building management system integration | 🟡 API Key | ✅ | ⚠️ |
| [Ferguson](https://www.ferguson.com/) | Plumbing supply distributor with product catalog and availability data | 🟡 API Key | ✅ | ⚠️ |

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
