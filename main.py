# -*- coding: utf-8 -*-
from typing import Any, List
import numpy as np
import dawdreamer as daw

def main():
  engine = daw.RenderEngine(44100, 512)
  
  try:
      plugin = engine.make_plugin_processor("test", "/path/to/plugin.dll")
      print(f"✔️ Plugin loaded successfully")
      print(f"Inputs: {plugin.get_num_input_channels()}")
      print(f"Outputs: {plugin.get_num_output_channels()}")
  
      # Try rendering
      engine.load_graph([(plugin, [])])
      engine.render(1.0)
      audio = engine.get_audio()
  
      # Check for NaN
      if np.isnan(audio).any():
          print("❌ Output contains NaN values")
      else:
          print("✔️ Rendering successful")
  
  except Exception as e:
      print(f"❌ Error: {e}")

if __name__ == "__main__":
  main()



