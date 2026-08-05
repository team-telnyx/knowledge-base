---
title: CrewAI Integration
summary: Use Telnyx as an OpenAI-compatible LLM backend for CrewAI agents, with global
  environment-variable routing or per-agent configuration, including support for custom
  tool calling.
sources:
- url: https://developers.telnyx.com/docs/inference/crewai
updated_at: 2026-08-05T13:45:47Z
---

# CrewAI Integration

Use Telnyx as an OpenAI-compatible LLM backend for CrewAI agents, with global environment-variable routing or per-agent configuration, including support for custom tool calling.

## Overview

Telnyx provides an OpenAI-compatible inference endpoint that can be used directly as the LLM backend for [CrewAI](crewai.md) agents. By pointing CrewAI at the Telnyx base URL and authenticating with a Telnyx API key, you can power multi-agent crews with Telnyx-hosted models without changing the CrewAI programming model.

## Setup

Install the CrewAI package:

```
pip install crewai
```

## Usage

You can route all CrewAI requests through Telnyx globally by exporting environment variables before running your application:

```
export TELNYX_API_KEY=your_telnyx_api_key
export OPENAI_BASE_URL=https://api.telnyx.com/v2/ai/openai
```

Alternatively, configure the Telnyx endpoint on a per-agent basis by constructing an `LLM` explicitly and passing it to each agent:

```
import os
from crewai import Agent, Task, Crew, LLM

llm = LLM(
    model="zai-org/GLM-5.2",
    base_url="https://api.telnyx.com/v2/ai/openai",
    api_key=os.getenv("TELNYX_API_KEY"),
)

researcher = Agent(
    role="Research Analyst",
    goal="Find and analyze information",
    backstory="You are an experienced research analyst.",
    llm=llm,
)

writer = Agent(
    role="Technical Writer",
    goal="Write clear, accurate reports",
    backstory="You are a skilled technical writer.",
    llm=llm,
)

research_task = Task(
    description="Research the latest trends in AI infrastructure",
    agent=researcher,
)

write_task = Task(
    description="Write a summary report based on the research findings",
    agent=writer,
)

crew = Crew(agents=[researcher, writer], tasks=[research_task, write_task])
result = crew.kickoff()
print(result)
```

## Tool Calling

CrewAI tools work normally when Telnyx is used as the backend. Define a tool with the `@tool` decorator and attach it to an agent via the `tools` argument:

```
from crewai.tools import tool

@tool("Search the web")
def search_web(query: str) -> str:
    """Search the web for information."""
    return f"Results for: {query}"

researcher = Agent(
    role="Research Analyst",
    goal="Find and analyze information",
    backstory="You are an experienced research analyst.",
    llm=llm,
    tools=[search_web],
)
```

The agent can then invoke `search_web` during task execution, and the tool's return value is fed back into the LLM through the Telnyx inference endpoint.
