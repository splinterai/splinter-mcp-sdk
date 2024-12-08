"""
Example Memory MCP Implementation for Project Splinter
This demonstrates a basic memory storage and retrieval system using the MCP protocol.
"""

from modelcontextprotocol import MCPServer, Request, Response
import asyncio
import json
from datetime import datetime
from typing import Dict, Any

class MemoryMCP(MCPServer):
    def __init__(self):
        super().__init__()
        self.memory_store: Dict[str, Any] = {}
        
        # Register methods
        self.register_method("store_memory", self.store_memory)
        self.register_method("retrieve_memory", self.retrieve_memory)
        self.register_method("list_memories", self.list_memories)
        
    async def store_memory(self, request: Request) -> Response:
        """Store a new memory with timestamp and metadata"""
        try:
            memory_data = request.params.get("data")
            memory_type = request.params.get("type", "general")
            
            if not memory_data:
                return Response(error={"code": -32602, "message": "Memory data is required"})
                
            memory_id = datetime.now().isoformat()
            memory_entry = {
                "id": memory_id,
                "type": memory_type,
                "data": memory_data,
                "timestamp": memory_id,
                "metadata": request.params.get("metadata", {})
            }
            
            self.memory_store[memory_id] = memory_entry
            
            return Response(result={
                "status": "success",
                "memory_id": memory_id
            })
            
        except Exception as e:
            return Response(error={"code": -32603, "message": str(e)})
            
    async def retrieve_memory(self, request: Request) -> Response:
        """Retrieve a specific memory by ID"""
        try:
            memory_id = request.params.get("memory_id")
            
            if not memory_id:
                return Response(error={"code": -32602, "message": "Memory ID is required"})
                
            memory = self.memory_store.get(memory_id)
            if not memory:
                return Response(error={"code": -32602, "message": "Memory not found"})
                
            return Response(result=memory)
            
        except Exception as e:
            return Response(error={"code": -32603, "message": str(e)})
            
    async def list_memories(self, request: Request) -> Response:
        """List all stored memories with optional filtering"""
        try:
            memory_type = request.params.get("type")
            start_date = request.params.get("start_date")
            end_date = request.params.get("end_date")
            
            memories = list(self.memory_store.values())
            
            # Apply filters if specified
            if memory_type:
                memories = [m for m in memories if m["type"] == memory_type]
            if start_date:
                memories = [m for m in memories if m["timestamp"] >= start_date]
            if end_date:
                memories = [m for m in memories if m["timestamp"] <= end_date]
                
            return Response(result={"memories": memories})
            
        except Exception as e:
            return Response(error={"code": -32603, "message": str(e)})

if __name__ == "__main__":
    server = MemoryMCP()
    asyncio.run(server.run())
