# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

PocketFlow is a minimalist LLM framework with only 100 lines of core code. It provides a simple abstraction for building LLM applications using a graph-based approach with Nodes and Flows.

## Key Architecture Components

1. **BaseNode**: The fundamental building block with `prep()`, `exec()`, and `post()` methods
2. **Node**: Extends BaseNode with retry logic and fallback handling
3. **Flow**: Orchestrates the execution of nodes in a sequence with conditional transitions
4. **BatchNode/Flow**: Handle batch processing of data
5. **AsyncNode/Flow**: Support asynchronous execution patterns
6. **ParallelBatch**: Enable parallel processing for performance

## Core Concepts

- **Nodes** represent individual processing steps with three lifecycle methods:
  - `prep()`: Prepare data for execution
  - `exec()`: Execute the main logic
  - `post()`: Process results and determine next steps

- **Flows** orchestrate nodes using transitions:
  - Default transitions (`>>`) for sequential execution
  - Conditional transitions (`- "action" >>`) for branching logic

## Common Development Tasks

### Running Tests
```bash
python3 -m pytest tests/ -v
```

### Installing Dependencies
```bash
pip install -r cookbook/pocketflow-<example>/requirements.txt
```

### Installing Package in Development Mode
```bash
pip install -e .
```

## Code Structure

- `pocketflow/`: Core framework implementation (only 100 lines)
- `cookbook/`: Examples and tutorials showing various patterns
- `tests/`: Unit tests for the framework
- `docs/`: Documentation and guides

## Key Patterns

1. **Linear Flow**: Nodes connected with `>>` operator
2. **Conditional Branching**: Nodes that return actions in `post()` method
3. **Loops**: Nodes that transition back to themselves
4. **Batch Processing**: Processing multiple items with shared state
5. **Async Processing**: Non-blocking execution patterns

## Working with Examples

Each example in `cookbook/` demonstrates a specific pattern:
- Start with simple examples like `pocketflow-chat` or `pocketflow-workflow`
- Most examples require API keys (e.g., OPENAI_API_KEY) set in environment variables
- Each example has a `main.py` that can be run directly
- always use python3 to run this project