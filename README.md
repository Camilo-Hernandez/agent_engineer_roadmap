# Especialización Gratuita de Ingeniería de Sistemas Multiagente

Transformers, RAG, Agentic AI, Agent Skills, MCP, LLMs Locales y Superagentes

Alternativa gratuita a la especializacion paga de IBM [RAG and Agentic AI Professional Certificate](https://www.coursera.org/professional-certificates/ibm-rag-and-agentic-ai) en Coursera. Estos recursos cubren el mismo conocimiento y más, provenientes directamente de los creadores de cada herramienta.

**Camilo Hernandez Ruiz - Ingeniero de Software y Automatizaciones**

## Tabla Resumen: Especializacion Paga de IBM vs. Ruta Gratuita

| Tema | IBM (Paga) | Ruta Gratuita |
|---|---|---|
| Fundamentos de Transformers y LLMs | Parcial | Hugging Face - LLM Course |
| Agent Skills (estandar abierto agentskills.io) | NO cubre | agentskills.io + Anthropic Academy + skills.sh + agentskill.sh |
| RAG pipelines, FAISS, vectores | Cubre | DeepLearning.AI - RAG course |
| LangChain + LangGraph | Cubre | LangChain Academy + DeepLearning.AI (3 cursos) |
| MCP (Model Context Protocol) | Cubre (FastMCP) | HuggingFace + Anthropic + Microsoft |
| LLMs locales: fine-tuning, Ollama, open-weight | NO cubre | Unsloth + HF TRL + Ollama + Decoding AI Magazine |
| Multi-agente (CrewAI, AG2) | Cubre | DeepLearning.AI + docs oficiales |
| Multimodal AI | Cubre | DeepLearning.AI short courses |
| Deploy multi-cloud (AWS, Railway, Fly.io, etc.) | Parcial (Gradio, Flask) | Advent of Agents + AWS Lambda docs + Railway/Render/Fly.io/DO |
| Super 24/7 Agents | NO cubre | OpenClaw + MaxClaw + KimiClaw + KiloClaw + NemoClaw + Perplexity Computer + n8n |

> Ventaja de la ruta gratuita: La especializacion paga de IBM no cubre Agent Skills (estandar abierto), fine-tuning/deployment local de modelos open-weight, ni superagentes personales (OpenClaw/MaxClaw). Estos tres temas son criticos para privacidad de datos, reduccion de costos, modelos especializados, y asistentes autonomos que funcionan con cualquier LLM.

Compilado en abril 2026. Todos los recursos listados son gratuitos al momento de publicacion.

## 1. Agent Skills (Estándar Abierto)

Agent Skills es un estandar abierto: carpetas con SKILL.md que cualquier LLM o agente puede usar. Adoptado por Claude, OpenAI Codex, Cursor, OpenClaw, Spring AI, Letta, Roo Code, y mas. Escribe una vez, usa en cualquier plataforma.

### Courses

- **Introducing Agent Skills - Video oficial (YouTube)** [GRATUITO | OFICIAL]
  Presentacion oficial del estandar y su flujo de trabajo basico.
  - https://www.youtube.com/watch?v=hXgunHDwMR8

## 2. Fundamentos de Transformers y LLMs

Antes de meterse en RAG, agentes, MCP o fine-tuning local, conviene entender que es un Transformer, como se diferencian las arquitecturas encoder, decoder y encoder-decoder, como usar modelos desde el Hub de Hugging Face, y que papel juegan tokenization, datasets y ajuste fino.

### Courses

- **Hugging Face - LLM Course** [GRATUITO | OFICIAL]
  Curso oficial, gratuito y muy solido para entender Transformers, usar pipeline(), trabajar con el Hub, hacer fine-tuning y dominar Datasets/Tokenizers antes de pasar a RAG y agentes.
  - https://huggingface.co/learn/llm-course/es/chapter1/1
  - https://huggingface.co/learn/llm-course/es

## 3. RAG (Retrieval-Augmented Generation)

Tecnica que permite a los LLMs consultar fuentes externas (documentos, bases de datos, APIs) antes de responder, produciendo respuestas mas precisas y actualizadas en lugar de depender solo de su entrenamiento.

### Courses

- **DeepLearning.AI - Retrieval Augmented Generation (RAG)** [GRATUITO]
  Curso gratis de Andrew Ng para dominar chunking, embeddings, vector search y agentic RAG.
  - https://www.deeplearning.ai/courses/retrieval-augmented-generation-rag/

- **DeepLearning.AI - Building Applications with Vector Databases** [GRATUITO | RAPIDO]
  Curso corto y practico para embeddings, similarity search y patrones de retrieval.
  - https://www.deeplearning.ai/short-courses/building-applications-vector-databases/

- **DeepLearning.AI - Knowledge Graphs for RAG** [GRATUITO | RAPIDO]
  Curso para sumar grafos de conocimiento y retrieval estructurado a un RAG.
  - https://www.deeplearning.ai/short-courses/knowledge-graphs-rag/

- **Google Developers Codelabs - Building AI Agents with Vertex AI Agent Builder** [GRATUITO | OFICIAL]
  Codelab oficial y gratuito para construir agentes y apps LLM con Vertex AI Agent Builder; muy buen fit para patrones agenticos y retrieval.
  - https://codelabs.developers.google.com/devsite/codelabs/building-ai-agents-vertexai

## 4. MCP (Model Context Protocol)

Protocolo abierto creado por Anthropic que estandariza como los LLMs se conectan a herramientas externas, bases de datos, y APIs. Funciona como un USB-C universal: un solo protocolo para que cualquier modelo acceda a cualquier servicio, reemplazando integraciones custom por conexion via servidores MCP reutilizables.

- **Hugging Face - MCP Course (con Anthropic)** [GRATUITO | CERTIFICADO]
  Curso gratuito con Anthropic. Asignaciones practicas, challenges, certificado.
  - https://huggingface.co/learn/mcp-course/

- **Anthropic - Introduction to Model Context Protocol** [GRATUITO | OFICIAL]
  Arquitectura MCP, primitivas (tools, resources, prompts), Python SDK, MCP Inspector.
  - https://anthropic.skilljar.com/introduction-to-model-context-protocol

- **Microsoft - MCP for Beginners (GitHub)** [GRATUITO | OPEN SOURCE]
  Open-source: Python, TypeScript, .NET, Java, Rust. Spec MCP 2025-11-25.
  - https://github.com/microsoft/mcp-for-beginners

## 5. Sistemas multiagente con LangChain + LangGraph

LangChain es el framework mas popular para construir aplicaciones con LLMs: cadenas de prompts, herramientas, y agentes. LangGraph lo extiende con grafos de estado que permiten memoria, iteracion, logica condicional, y workflows multi-agente complejos.

- **LangChain Academy - Introduction to LangGraph** [GRATUITO | OFICIAL]
  Curso oficial gratuito. 6 modulos: state, nodes, edges, memory, human-in-the-loop, deployment.
  - https://academy.langchain.com/courses/intro-to-langgraph

- **DeepLearning.AI - AI Agents in LangGraph** [GRATUITO]
  Por Harrison Chase. Agente desde cero, LangGraph, agentic search, persistencia.
  - https://deeplearning.ai/short-courses/ai-agents-in-langgraph/

- **DeepLearning.AI - Long-Term Agentic Memory** [GRATUITO]
  Memoria semantica, episodica, procedural. Proyecto: email agent con routing.
  - https://deeplearning.ai/short-courses/long-term-agentic-memory-with-langgraph/

- **Docs oficiales LangChain/LangGraph** [GRATUITO | OFICIAL]
  Tutoriales, RAG agents, SQL agents, multi-agent patterns. Codigo fuente completo.
  - https://docs.langchain.com/oss/python/learn
  - https://github.com/langchain-ai/langgraph

## 6. Sistemas Multi-Agente (CrewAI, AG2/AutoGen, Google ADK, AWS Bedrock + AgentCore)

Frameworks para crear equipos de agentes de IA que colaboran entre sí adicionales a LangChain & LangGraph. En un sistema multi-agente, cada agente tiene un rol especializado (investigador, planeador, ejecutor, critico, archivador, ...) y se comunican para resolver tareas complejas que un solo agente no podria manejar.

### AWS / Bedrock - Fundamentos y Ecosistema

- **DeepLearning.AI - Design, Develop, and Deploy Multi-Agent Systems with CrewAI** [GRATUITO]
  Aprende a construir sistemas multi-agente que automaticen flujos de trabajo complejos end-to-end.
  - https://learn.deeplearning.ai/courses/design-develop-and-deploy-multi-agent-systems-with-crewai/lesson/rc39v/welcome
  - https://docs.crewai.com

- **Framework AutoGen para sistemas multi-agente** [GRATUITO | OFICIAL]
  AutoGen: conversaciones multi-agente.
  - https://www.deeplearning.ai/short-courses/ai-agentic-design-patterns-with-autogen/
  - https://microsoft.github.io/autogen

- **AG2 - Fork open source de AutoGen** [GRATUITO | OPEN SOURCE]
  AG2 es la evolucion independiente de AutoGen 0.2, mantenida por la comunidad bajo la org ag2ai. Misma API (import autogen), licencia Apache 2.0, con roadmap propio separado de Microsoft.
  - https://ag2.ai
  - https://github.com/ag2ai/ag2
  - https://docs.ag2.ai

- **AWS - Learn About AI (portal oficial)** [GRATUITO | OFICIAL]
  Portal de aprendizaje oficial de AWS para IA y ML: rutas de aprendizaje, certificaciones, tutoriales de Bedrock, SageMaker y servicios de IA gestionados.
  - https://aws.amazon.com/es/training/learn-about/ai/

- **AWS Skill Builder - Introduction to Generative AI: Art of the Possible** [GRATUITO | OFICIAL]
  Modulo oficial introductorio de AWS Skill Builder: conceptos clave de GenAI, casos de uso empresariales y posibilidades con los servicios de AWS.
  - https://skillbuilder.aws/learn/ZEVZZ1D4AS/introduction-to-generative-ai--art-of-the-possible/

- **AWS Skill Builder - Building Production-Ready AI Agents with Amazon Bedrock AgentCore** [GRATUITO | OFICIAL]
  Modulo oficial introductorio de AWS Skill Builder: conceptos clave de GenAI, casos de uso empresariales y posibilidades con los servicios de AWS.
  - https://skillbuilder.aws/learn/4G7V8NQB5B/building-productionready-ai-agents-with-amazon-bedrock-agentcore/7DY16CFWTC

- **Google ADK - Agent Development Kit** [GRATUITO | OFICIAL]
  Framework oficial de Google para construir sistemas multi-agente. Disponible en Python, TypeScript, Go y Java. Soporta LLM agents, Workflow agents (sequential, loop, parallel nativo) y Custom agents. Incluye el protocolo A2A (Agent-to-Agent) para comunicacion entre agentes de distintos frameworks. Integracion nativa con Google Cloud (Vertex AI, Cloud Run, GKE).
  - https://google.github.io/adk-docs/
  - https://github.com/google/adk-python

- **Amazon Bedrock Agents - Multi-agent en AWS** [PAGO | AWS]
  Servicio administrado de AWS para construir sistemas multi-agente sin gestionar infraestructura. Modelo supervisor + colaboradores: cada agente tiene rol especializado, acceso a APIs (action groups), knowledge bases (RAG), guardrails y memory retention. Ideal para stacks AWS enterprise. Alto vendor lock-in vs frameworks open source. AgentCore permite ademas desplegar agentes de cualquier framework (AG2, ADK) en infraestructura AWS.
  - https://aws.amazon.com/bedrock/agents/
  - https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html

- **DeepLearning.AI - Serverless Agentic Workflows with Amazon Bedrock** [GRATUITO]
  Curso practico para construir flujos agenticos serverless directamente sobre Bedrock: invocacion de agentes, action groups, tool use y despliegue sin gestionar infraestructura.
  - https://learn.deeplearning.ai/courses/serverless-agentic-workflows-with-amazon-bedrock/

## 7. LLMs Locales - Fine-Tuning y Deploy On-Premise

Descargar modelos open-weight (Gemma, Llama, Qwen, DeepSeek, Mistral, gpt-oss de OpenAI), hacer fine-tuning con LoRA/QLoRA para tareas especificas de empresa, convertir a GGUF, y servir localmente con Ollama, LM Studio, o vLLM. Privacidad total, sin costos por token, y modelos especializados en tu dominio.

- **Google - Gemma 4 (introduccion)** [GRATUITO | OPEN SOURCE]
  Familia open-weight de Google con licencia Apache 2.0. Multimodal, multilingual, contexto 128K. Corre en Ollama y HF.
  - https://youtu.be/W2xVSO6eUWY
  - https://youtu.be/p2zZ6zuaCDM

- **Unsloth - Docs + Notebooks en Google Colab** [GRATUITO | OPEN SOURCE]
  Fine-tuning completo: QLoRA vs LoRA, datasets, GGUF para Ollama. Modelo 8B en GPU 12GB.
  - https://unsloth.ai/docs
  - https://github.com/unslothai/unsloth

- **Hugging Face - Unsloth + TRL** [GRATUITO | OFICIAL]
  Tutorial oficial HF. Compatible con Hub, transformers, PEFT.
  - https://huggingface.co/blog/unsloth-trl

- **HF + Unsloth - Fine-tuning gratis en HF Jobs** [GRATUITO | CREDITOS GRATIS]
  Creditos gratuitos para fine-tunear en infra cloud de HF.
  - https://huggingface.co/blog/unsloth-jobs

- **Decodingml - Fine-tune and Deploy Open-Source LLMs** [GRATUITO | OPEN SOURCE]
  Pipeline completo: APIs de prototipo a modelos open-source on-prem.
  - https://www.decodingai.com/

- **Ollama - Docs oficiales** [GRATUITO | OPEN SOURCE]
  Llama, DeepSeek, Qwen local. Compatible LangChain/RAG. macOS/Linux/Windows/Docker.
  - https://ollama.com
  - https://github.com/ollama/ollama

- **SitePoint - Fine-Tune Local LLMs 2026** [GRATUITO]
  Guia end-to-end: fine-tuning vs RAG vs prompting, Unsloth, GGUF, Ollama + FastAPI.
  - https://www.sitepoint.com/fine-tune-local-llms-2026/

## 8. IA Multimodal

Modelos que procesan y generan multiples tipos de datos: texto, imagenes, audio, y video. Permite construir aplicaciones que entienden fotos, transcriben voz, generan imagenes, y combinan todo en un solo flujo de trabajo.

- **DeepLearning.AI - Short courses (multimodal)** [GRATUITO]
  Catalogo corto con cursos sobre audio, vision y generacion multimodal.
  - https://deeplearning.ai/short-courses/

## 9. Deploy a Produccion (Multi-Cloud)

Llevar tu aplicacion de IA desde tu maquina local a servidores accesibles al mundo. Desde plataformas simples (push-to-deploy en un click) hasta AWS enterprise con Lambda serverless. Cada opcion tiene trade-offs de costo, complejidad, y escalabilidad.

- **Advent of Agents - Google Cloud (31 dias)** [GRATUITO | GOOGLE CLOUD]
  Ruta de 31 capítulos para hacer 1 por día, desde agente basico a multi-agente en produccion. Gemini, ADK, Vertex AI, MCP.
  - https://adventofagents.com

- **AWS Lambda - Container images** [GRATUITO]
  Docs oficiales para desplegar funciones Lambda como imagenes Docker.
  - https://docs.aws.amazon.com/lambda/latest/dg/images-create.html
  - https://docs.aws.amazon.com/lambda/latest/dg/python-image.html

- **DEV Community - FastAPI on AWS Lambda with Docker** [GRATUITO]
  Guia practica con FastAPI, Mangum, ECR y Lambda para un deploy end-to-end.
  - https://dev.to/dev_insights/deploy-fastapi-on-aws-lambda-with-docker-2025-3a3a

- **Railway - Push-to-deploy desde GitHub** [TIER GRATIS]
  Conecta GitHub, click deploy, URL publica. $5 creditos. Ideal MVPs.
  - https://railway.app

- **Render - Deploy con free tier y workers** [TIER GRATIS]
  Free tier, Postgres/Redis managed, background workers incluidos.
  - https://render.com

- **Fly.io - Deploy global en edge** [TIER GRATIS]
  35+ regiones, GPUs, scale-to-zero, static IPs. Baja latencia global.
  - https://fly.io

- **DigitalOcean App Platform** [TIER GRATIS]
  Source builds, Postgres/Redis, CDN. Balance precio/simplicidad.
  - https://www.digitalocean.com/products/app-platform

## 10. Super 24/7 Agents

Agentes de IA que corren continuamente, sin supervision humana constante, y toman el control de sistemas reales: navegan la web, abren apps, ejecutan comandos, gestionan archivos, envian emails y responden mensajes. Operan 24/7 en tu servidor local o en la nube, y los controlas desde un simple chat como si hablaras con un asistente humano.

OpenClaw, proyecto independiente creado por Peter Steinberger y presentado a inicios de 2026, ayudo a empujar esta tendencia de agentes que operan computadoras reales. Su propuesta llamo la atencion por el control total del computador y las cuentas del usuario, convirtiendose en un asistente personal siempre activo.

### n8n - Automatizacion low-code personal y empresarial

### Agentes tipo OpenClaw

- **n8n - Workflow Automation (open source)** [GRATUITO | OPEN SOURCE]
  Herramienta low-code de automatizacion de flujos que conecta mas de 500 apps (Slack, GitHub, Gmail, Postgres, HubSpot, Stripe, Google Workspace) mediante nodos visuales en un canvas. Permite escribir codigo JavaScript o Python directamente cuando se necesita logica avanzada, sin depender exclusivamente del enfoque low-code. Soporta MCP para integraciones con agentes de IA. Funciona para uso personal (self-hosted gratis con Docker) y para empresas (RBAC, SSO/SAML, audit logs, control de versiones con git). Sin vendor lock-in: tu infra, tus datos.
  - https://n8n.io
  - https://github.com/n8n-io/n8n

- **OpenClaw - Proyecto independiente** [COMUNIDAD]
  Proyecto de computer use creado por Peter Steinberger. Se enfoca en automatizar tareas sobre una computadora real o virtual, llevando la idea de un asistente personal que puede operar interfaces, coordinar acciones y mantener flujos de trabajo continuos.
  - https://openclaw.ai/

- **MaxClaw - Agente local en Go** [OPEN SOURCE]
  Agente open-source autoalojado escrito en Go. Ofrece CLI, interfaz web y desktop con sesiones, memoria persistente, tareas programadas e integraciones multi-canal (Telegram, WhatsApp, Discord). Implementa un ciclo de vida adaptativo de seis capas con recuperacion de errores, compresion de contexto y fallback de modelos. Compatible con Anthropic y OpenAI.
  - https://github.com/Lichas/maxclaw

- **KimiClaw** [OPEN SOURCE]
  Variante de agente de uso de computadora construida sobre los modelos Kimi de Moonshot AI, enfocada en tareas de automatizacion web y procesamiento de documentos de larga duracion.
  - https://www.kimi.com/bot

- **KiloClaw - Extension de KiloCode** [OPEN SOURCE]
  Extension de KiloCode para ser alternativa a OpenClaw.
  - https://kilo.ai/kiloclaw

- **NemoClaw - Agente basado en NVIDIA NeMo** [OPEN SOURCE]
  Agente de uso de computadora construido sobre el ecosistema NeMo de NVIDIA, orientado a automatizacion de flujos de trabajo en entornos con aceleracion GPU y modelos LLM on-premise.
  - https://www.nvidia.com/es-la/ai/nemoclaw/

- **Perplexity Computer - Agente de Perplexity AI** [OFICIAL]
  Agente de uso de computadora de Perplexity AI que combina busqueda en tiempo real con control de escritorio, permitiendo investigar, resumir y ejecutar tareas basadas en informacion actualizada de la web.
  - https://www.perplexity.ai/computer/new
