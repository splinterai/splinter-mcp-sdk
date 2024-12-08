# Project Splinter MCP SDK

This repository is a fork of the Model Context Protocol Python SDK (https://github.com/modelcontextprotocol/python-sdk) customized for Project Splinter. It provides the foundation for creating custom Model Context Protocol (MCP) servers tailored to Splinter's specific needs.

## Repository Structure

```
python-mcp-sdk/
├── docs/
│   └── MCP_Development_Guide.md
├── examples/
│   └── memory_mcp.py
├── src/
├── tests/
└── README.md
```

## Documentation

See the [MCP Development Guide](docs/MCP_Development_Guide.md) for detailed instructions on creating and implementing custom MCPs for Project Splinter.

## Examples

- `memory_mcp.py`: Demonstrates a basic memory storage and retrieval system using the MCP protocol

## Getting Started

1. Clone this repository
2. Follow the setup instructions in the MCP Development Guide
3. Review the example implementations
4. Create your custom MCP implementation in the `src` directory

## Windows-Specific Configuration

For Windows environments, MCPs are configured in:
```
C:\Users\[Username]\AppData\Roaming\Claude\claude_desktop_config.json
```

## Development Notes

- All MCPs must follow the Model Context Protocol specification
- Test thoroughly before deployment
- Remember to restart Claude Desktop after adding new MCPs
- Follow security best practices outlined in the development guide