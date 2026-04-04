from reportlab.platypus import Paragraph

from .config import styles, FREE, OFFICIAL, COMMUNITY
from .helpers import section_divider, resource_block


def build_section_agent_skills():
    """1. Agent Skills"""
    elements = section_divider("Agent Skills (Estándar Abierto)", "1")
    elements.append(Paragraph(
        "Agent Skills es un estandar abierto: carpetas con SKILL.md que "
        "cualquier LLM o agente puede usar. Adoptado por Claude, OpenAI Codex, "
        "Cursor, OpenClaw, Spring AI, Letta, Roo Code, y mas. Escribe una vez, "
        "usa en cualquier plataforma.",
        styles["BD"],
    ))
    elements.extend(resource_block(
        "Introducing Agent Skills — Video oficial (YouTube)",
        "Presentacion oficial del estandar Agent Skills: que son, como "
        "funcionan, y por que son la forma mas eficiente de extender "
        "capacidades de cualquier agente o LLM.",
        "https://www.youtube.com/watch?v=hXgunHDwMR8 | https://youtu.be/eWY6bHtid1o",
        [("GRATUITO", FREE), ("OFICIAL", OFFICIAL)],
    ))
    elements.extend(resource_block(
        "Anthropic Academy — Introduction to Agent Skills",
        "Curso oficial: crear Skills, distribuir con plugins, conexion con "
        "subagentes, troubleshooting.",
        "https://anthropic.skilljar.com/introduction-to-agent-skills",
        [("GRATUITO", FREE), ("OFICIAL", OFFICIAL)],
    ))
    elements.extend(resource_block(
        "Repositorios de Skills",
        "github.com/anthropics/skills: 17+ skills open-source oficiales "
        "(docx, pdf, pptx, xlsx, frontend-design, MCP builder). "
        "skills.sh: directorio de la comunidad con skills de terceros "
        "listos para instalar. "
        "agentskill.sh: directorio de 44k+ skills con escaneo de seguridad "
        "en dos capas e instalador /learn. "
        "Skillstore: marketplace curado de Agent Skills. "
        "SkillsDirectory: directorio de las skills mas populares.",
        "https://github.com/anthropics/skills | https://skills.sh/ | "
        "https://agentskill.sh | https://skillstore.io | https://www.skillsdirectory.org",
        [("GRATUITO", FREE), ("OPEN SOURCE", COMMUNITY)],
    ))
    elements.extend(resource_block(
        "Especificacion oficial — agentskills.io",
        "La especificacion completa del estandar. Formato SKILL.md con YAML "
        "frontmatter, progressive disclosure (metadata -> body -> archivos "
        "extra), y guias de integracion.",
        "https://agentskills.io/specification",
        [("GRATUITO", FREE), ("ESTANDAR ABIERTO", COMMUNITY)],
    ))
    elements.extend(resource_block(
        "awesome-agent-skills — Indice del ecosistema completo",
        "Catalogos de skills de Anthropic, OpenAI, Microsoft, Google, Vercel, "
        "Supabase, HuggingFace, OpenClaw. Herramientas de authoring, "
        "validacion, y papers academicos.",
        "https://github.com/skillmatic-ai/awesome-agent-skills",
        [("GRATUITO", FREE), ("OPEN SOURCE", COMMUNITY)],
    ))
    return elements


def build_section_rag():
    """2. RAG (Retrieval-Augmented Generation)"""
    elements = section_divider("RAG (Retrieval-Augmented Generation)", "2")
    elements.append(Paragraph(
        "Tecnica que permite a los LLMs consultar fuentes externas "
        "(documentos, bases de datos, APIs) antes de responder, produciendo "
        "respuestas mas precisas y actualizadas en lugar de depender solo de "
        "su entrenamiento.",
        styles["BD"],
    ))
    elements.append(Paragraph("<b>Courses</b>", styles["BD"]))
    elements.extend(resource_block(
        "DeepLearning.AI — Retrieval Augmented Generation (RAG)",
        "Curso gratis de Andrew Ng para dominar chunking, embeddings, vector search y agentic RAG.",
        "https://www.deeplearning.ai/courses/retrieval-augmented-generation-rag/",
        [("GRATUITO", FREE)],
    ))
    elements.extend(resource_block(
        "DeepLearning.AI — Building Applications with Vector Databases",
        "Curso corto y practico para embeddings, similarity search y patrones de retrieval.",
        "https://www.deeplearning.ai/short-courses/building-applications-vector-databases/",
        [("GRATUITO", FREE)],
    ))
    elements.extend(resource_block(
        "DeepLearning.AI — Knowledge Graphs for RAG",
        "Curso para sumar grafos de conocimiento y retrieval estructurado a un RAG.",
        "https://www.deeplearning.ai/short-courses/knowledge-graphs-rag/",
        [("GRATUITO", FREE)],
    ))
    elements.append(Paragraph("<b>Docs/Tutorials</b>", styles["BD"]))
    elements.extend(resource_block(
        "Google Cloud — Vertex AI RAG Engine",
        "Docs y quickstart oficiales para RAG administrado en Vertex AI, con ingestion y grounding sobre datos propios.",
        "https://cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/rag-overview | https://cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/rag-quickstart",
        [("GRATUITO", FREE), ("OFICIAL", OFFICIAL)],
    ))
    elements.extend(resource_block(
        "Google Cloud — Grounding with Vertex AI Search",
        "Guia oficial para conectar Gemini a data stores y buscadores propios con grounding enterprise.",
        "https://cloud.google.com/vertex-ai/generative-ai/docs/grounding/grounding-with-vertex-ai-search",
        [("GRATUITO", FREE), ("OFICIAL", OFFICIAL)],
    ))
    elements.extend(resource_block(
        "NVIDIA — Deep Agents for Enterprise Search with AI-Q and LangChain",
        "Tutorial oficial para agentes de busqueda enterprise con RAG, subagentes y tracing.",
        "https://developer.nvidia.com/blog/how-to-build-deep-agents-for-enterprise-search-with-nvidia-ai-q-and-langchain/",
        [("GRATUITO", FREE), ("OFICIAL", OFFICIAL)],
    ))
    elements.extend(resource_block(
        "NVIDIA — Document Processing Pipeline for RAG with Nemotron",
        "Guia oficial para extraer PDFs, generar embeddings, rerankear y citar fuentes.",
        "https://developer.nvidia.com/blog/how-to-build-a-document-processing-pipeline-for-rag-with-nemotron/",
        [("GRATUITO", FREE), ("OFICIAL", OFFICIAL)],
    ))
    elements.extend(resource_block(
        "Google Developers Codelabs — Building AI Agents with Vertex AI Agent Builder",
        "Codelab oficial y gratuito para construir agentes y apps LLM con Vertex AI Agent Builder; muy buen fit para patrones agenticos y retrieval.",
        "https://codelabs.developers.google.com/devsite/codelabs/building-ai-agents-vertexai",
        [("GRATUITO", FREE), ("OFICIAL", OFFICIAL)],
    ))
    elements.extend(resource_block(
        "OpenAI — File search y function calling",
        "Docs oficiales para retrieval sobre archivos y tool use en asistentes y flujos agenticos.",
        "https://platform.openai.com/docs/guides/file-search | https://platform.openai.com/docs/guides/function-calling",
        [("GRATUITO", FREE), ("OFICIAL", OFFICIAL)],
    ))
    return elements


def build_section_langchain():
    """3. LangChain + LangGraph"""
    elements = section_divider("LangChain + LangGraph", "3")
    elements.append(Paragraph(
        "LangChain es el framework mas popular para construir aplicaciones "
        "con LLMs: cadenas de prompts, herramientas, y agentes. LangGraph lo "
        "extiende con grafos de estado que permiten memoria, iteracion, logica "
        "condicional, y workflows multi-agente complejos.",
        styles["BD"],
    ))
    elements.extend(resource_block(
        "LangChain Academy — Introduction to LangGraph",
        "Curso oficial gratuito. 6 modulos: state, nodes, edges, memory, "
        "human-in-the-loop, deployment.",
        "https://academy.langchain.com/courses/intro-to-langgraph",
        [("GRATUITO", FREE), ("OFICIAL", OFFICIAL)],
    ))
    elements.extend(resource_block(
        "DeepLearning.AI — AI Agents in LangGraph",
        "Por Harrison Chase. Agente desde cero, LangGraph, agentic search, "
        "persistencia.",
        "https://deeplearning.ai/short-courses/ai-agents-in-langgraph/",
        [("GRATUITO", FREE)],
    ))
    elements.extend(resource_block(
        "DeepLearning.AI — Long-Term Agentic Memory",
        "Memoria semantica, episodica, procedural. Proyecto: email agent con "
        "routing.",
        "https://deeplearning.ai/short-courses/long-term-agentic-memory-with-langgraph/",
        [("GRATUITO", FREE)],
    ))
    elements.extend(resource_block(
        "Docs oficiales LangChain/LangGraph",
        "Tutoriales, RAG agents, SQL agents, multi-agent patterns. Codigo "
        "fuente completo.",
        "https://docs.langchain.com/oss/python/learn | https://github.com/langchain-ai/langgraph",
        [("GRATUITO", FREE), ("OFICIAL", OFFICIAL)],
    ))
    return elements


def build_section_mcp():
    """4. MCP (Model Context Protocol)"""
    elements = section_divider("MCP (Model Context Protocol)", "4")
    elements.append(Paragraph(
        "Protocolo abierto creado por Anthropic que estandariza como los LLMs "
        "se conectan a herramientas externas, bases de datos, y APIs. Funciona "
        "como un USB-C universal: un solo protocolo para que cualquier modelo "
        "acceda a cualquier servicio, reemplazando integraciones custom por "
        "conexion via servidores MCP reutilizables.",
        styles["BD"],
    ))
    elements.extend(resource_block(
        "Hugging Face — MCP Course (con Anthropic)",
        "Curso gratuito con Anthropic. Asignaciones practicas, challenges, "
        "certificado.",
        "https://huggingface.co/learn/mcp-course/",
        [("GRATUITO", FREE), ("CERTIFICADO", COMMUNITY)],
    ))
    elements.extend(resource_block(
        "Anthropic — Introduction to Model Context Protocol",
        "Arquitectura MCP, primitivas (tools, resources, prompts), Python SDK, "
        "MCP Inspector.",
        "https://anthropic.skilljar.com/introduction-to-model-context-protocol",
        [("GRATUITO", FREE), ("OFICIAL", OFFICIAL)],
    ))
    elements.extend(resource_block(
        "Microsoft — MCP for Beginners (GitHub)",
        "Open-source: Python, TypeScript, .NET, Java, Rust. Spec MCP 2025-11-25.",
        "https://github.com/microsoft/mcp-for-beginners",
        [("GRATUITO", FREE), ("OPEN SOURCE", COMMUNITY)],
    ))
    return elements


def build_section_local_llms():
    """5. LLMs Locales — Fine-Tuning y Deploy On-Premise"""
    elements = section_divider("LLMs Locales — Fine-Tuning y Deploy On-Premise", "5")
    elements.append(Paragraph(
        "Descargar modelos open-weight (Llama, Qwen, DeepSeek, Mistral, "
        "gpt-oss de OpenAI), hacer fine-tuning con LoRA/QLoRA para tareas "
        "especificas de empresa, convertir a GGUF, y servir localmente con "
        "Ollama, LM Studio, o vLLM. Privacidad total, sin costos por token, "
        "y modelos especializados en tu dominio.",
        styles["BD"],
    ))
    elements.extend(resource_block(
        "Unsloth — Docs + Notebooks en Google Colab",
        "Fine-tuning completo: QLoRA vs LoRA, datasets, GGUF para Ollama. "
        "Modelo 8B en GPU 12GB.",
        "https://unsloth.ai/docs | https://github.com/unslothai/unsloth",
        [("GRATUITO", FREE), ("OPEN SOURCE", COMMUNITY)],
    ))
    elements.extend(resource_block(
        "Hugging Face — Unsloth + TRL",
        "Tutorial oficial HF. Compatible con Hub, transformers, PEFT.",
        "https://huggingface.co/blog/unsloth-trl",
        [("GRATUITO", FREE), ("OFICIAL", OFFICIAL)],
    ))
    elements.extend(resource_block(
        "HF + Unsloth — Fine-tuning gratis en HF Jobs",
        "Creditos gratuitos para fine-tunear en infra cloud de HF.",
        "https://huggingface.co/blog/unsloth-jobs",
        [("GRATUITO", FREE), ("CREDITOS GRATIS", COMMUNITY)],
    ))
    elements.extend(resource_block(
        "Decodingml — Fine-tune and Deploy Open-Source LLMs",
        "Pipeline completo: APIs de prototipo a modelos open-source on-prem.",
        "https://www.decodingai.com/",
        [("GRATUITO", FREE), ("OPEN SOURCE", COMMUNITY)],
    ))
    elements.extend(resource_block(
        "Ollama — Docs oficiales",
        "Llama, DeepSeek, Qwen local. Compatible LangChain/RAG. "
        "macOS/Linux/Windows/Docker.",
        "https://ollama.com | https://github.com/ollama/ollama",
        [("GRATUITO", FREE), ("OPEN SOURCE", COMMUNITY)],
    ))
    elements.extend(resource_block(
        "SitePoint — Fine-Tune Local LLMs 2026",
        "Guia end-to-end: fine-tuning vs RAG vs prompting, Unsloth, GGUF, "
        "Ollama + FastAPI.",
        "https://www.sitepoint.com/fine-tune-local-llms-2026/",
        [("GRATUITO", FREE)],
    ))
    return elements


def build_section_multi_agent():
    """6. Sistemas Multi-Agente"""
    elements = section_divider("Sistemas Multi-Agente (CrewAI, AG2/AutoGen)", "6")
    elements.append(Paragraph(
        "Frameworks para crear equipos de agentes de IA que colaboran entre "
        "si: cada agente tiene un rol especializado (investigador, escritor, "
        "critico) y se comunican para resolver tareas complejas que un solo "
        "agente no podria manejar.",
        styles["BD"],
    ))
    elements.extend(resource_block(
        "DeepLearning.AI — CrewAI y multi-agent systems",
        "Orquestacion, collaboration patterns, workflows especializados.",
        "https://deeplearning.ai/short-courses/",
        [("GRATUITO", FREE)],
    ))
    elements.extend(resource_block(
        "Docs oficiales CrewAI y AutoGen",
        "CrewAI: workflows estructurados. AutoGen: conversaciones multi-agente.",
        "https://docs.crewai.com | https://microsoft.github.io/autogen",
        [("GRATUITO", FREE), ("OFICIAL", OFFICIAL)],
    ))
    return elements


def build_section_multimodal():
    """7. IA Multimodal"""
    elements = section_divider("IA Multimodal", "7")
    elements.append(Paragraph(
        "Modelos que procesan y generan multiples tipos de datos: texto, "
        "imagenes, audio, y video. Permite construir aplicaciones que entienden "
        "fotos, transcriben voz, generan imagenes, y combinan todo en un solo "
        "flujo de trabajo.",
        styles["BD"],
    ))
    elements.extend(resource_block(
        "DeepLearning.AI — Short courses multimodales",
        "Whisper (audio), CLIP (imagen-texto), vision, generacion de imagenes.",
        "https://deeplearning.ai/short-courses/",
        [("GRATUITO", FREE)],
    ))
    return elements


def build_section_deploy():
    """8. Deploy a Produccion (Multi-Cloud)"""
    elements = section_divider("Deploy a Produccion (Multi-Cloud)", "8")
    elements.append(Paragraph(
        "Llevar tu aplicacion de IA desde tu maquina local a servidores "
        "accesibles al mundo. Desde plataformas simples (push-to-deploy en un "
        "click) hasta AWS enterprise con Lambda serverless. Cada opcion tiene "
        "trade-offs de costo, complejidad, y escalabilidad.",
        styles["BD"],
    ))
    elements.extend(resource_block(
        "Advent of Agents — Google Cloud (25 dias)",
        "Agente basico a multi-agente en produccion. Gemini, ADK, Vertex AI, MCP.",
        "https://adventofagents.com",
        [("GRATUITO", FREE), ("GOOGLE CLOUD", COMMUNITY)],
    ))
    elements.extend(resource_block(
        "AWS — FastAPI + Lambda + Docker",
        "Deploy serverless con FastAPI, Mangum, Lambda, API Gateway, ECR, SAM.",
        "https://aws.amazon.com/blogs/machine-learning/ | https://dev.to/dev_insights/deploy-fastapi-on-aws-lambda-with-docker-2025-3a3a",
        [("GRATUITO", FREE)],
    ))
    elements.extend(resource_block(
        "Railway — Push-to-deploy desde GitHub",
        "Conecta GitHub, click deploy, URL publica. $5 creditos. Ideal MVPs.",
        "https://railway.app",
        [("TIER GRATIS", FREE)],
    ))
    elements.extend(resource_block(
        "Render — Deploy con free tier y workers",
        "Free tier, Postgres/Redis managed, background workers incluidos.",
        "https://render.com",
        [("TIER GRATIS", FREE)],
    ))
    elements.extend(resource_block(
        "Fly.io — Deploy global en edge",
        "35+ regiones, GPUs, scale-to-zero, static IPs. Baja latencia global.",
        "https://fly.io",
        [("TIER GRATIS", FREE)],
    ))
    elements.extend(resource_block(
        "DigitalOcean App Platform",
        "Source builds, Postgres/Redis, CDN. Balance precio/simplicidad.",
        "https://www.digitalocean.com/products/app-platform",
        [("TIER GRATIS", FREE)],
    ))
    return elements


def build_section_superagents():
    """9. Superagentes Personales"""
    elements = section_divider("Superagentes Personales (OpenClaw / MaxClaw)", "9")
    elements.append(Paragraph(
        "La nueva generacion de asistentes de IA que se conectan con tus "
        "cuentas reales (WhatsApp, Telegram, Slack, email, calendario, GitHub) "
        "y ejecutan tareas autonomamente. Corren en tu servidor local o en la "
        "nube, y los controlas desde un chat en el celular como si hablaras "
        "con un asistente humano.",
        styles["BD"],
    ))
    return elements
