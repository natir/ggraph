
# std import
import sys

# package import
from ggraph import app

if __name__ == '__main__':
    
    if len(sys.argv) == 1:
        # production mode
        app.run()
    elif len(sys.argv) == 2:
        app.run(port=int(sys.argv[1]))
    elif len(sys.argv) == 3:
        app.debug = sys.argv[2].startswith("T")
        app.run(port=int(sys.argv[1]))
    else:
        print("Usage : ./run.py [port number] [if begin with T activate debug mode]")
