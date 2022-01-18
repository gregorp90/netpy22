1. Run the container:
   ```
   docker run -p 8888:8888 -p 6006:6006 -it -u user -w /home/user tiagopeixoto/graph-tool bash
   ```

2. Run the jupyter notebook:
   ```
   [user@c20b92b8c4bf ~]$ jupyter notebook --ip 0.0.0.0
   ```

Setup: https://git.skewed.de/count0/graph-tool/-/wikis/installation-instructions
Example: https://graph-tool.skewed.de/static/doc/demos/inference/inference.html