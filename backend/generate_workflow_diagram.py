"""
Generate workflow diagram for the LangGraph agent.
Run this script to create a PNG visualization of the workflow.
"""
import os
import sys

# Add app to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from app.agent.workflow import build_workflow


def generate_diagram():
    """Generate and save the workflow diagram."""
    
    # Build the workflow
    workflow = build_workflow()
    
    # Get the graph
    graph = workflow.get_graph()
    
    try:
        # Try to generate PNG using Mermaid
        png_data = graph.draw_mermaid_png()
        
        # Save to file
        output_path = os.path.join(os.path.dirname(__file__), '..', 'workflow_diagram.png')
        with open(output_path, 'wb') as f:
            f.write(png_data)
        
        print(f"✅ Workflow diagram saved to: {output_path}")
        return output_path
        
    except Exception as e:
        print(f"❌ Could not generate PNG: {e}")
        print("\nTrying to generate Mermaid text instead...")
        
        # Fallback: generate Mermaid text
        try:
            mermaid_text = graph.draw_mermaid()
            output_path = os.path.join(os.path.dirname(__file__), '..', 'workflow_diagram.mmd')
            with open(output_path, 'w') as f:
                f.write(mermaid_text)
            
            print(f"✅ Mermaid diagram saved to: {output_path}")
            print("\nTo convert to PNG, use:")
            print(f"  npx @mermaid-js/mermaid-cli -i {output_path} -o workflow_diagram.png")
            return output_path
            
        except Exception as e2:
            print(f"❌ Could not generate Mermaid text: {e2}")
            return None


if __name__ == "__main__":
    print("🎨 Generating LangGraph workflow diagram...\n")
    generate_diagram()
