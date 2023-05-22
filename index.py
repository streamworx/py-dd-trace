from flask import Flask
import os

### kalo mau RAW pake yang ini
# import logging
# FORMAT = ('%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] [dd.service=%(dd.service)s dd.env=%(dd.env)s dd.version=%(dd.version)s dd.trace_id=%(dd.trace_id)s dd.span_id=%(dd.span_id)s] - %(message)s')
# logging.basicConfig(format=FORMAT)


### kalo mau JSON pake yang ini
# import logging
# import json_log_formatter
# json_handler = logging.StreamHandler() #FileHandler(filename='/tmp/my-log.json')
# formatter = json_log_formatter.JSONFormatter()
# json_handler.setFormatter(formatter)
# logger = logging.getLogger()
# logger.addHandler(json_handler)

# logger.setLevel(logging.INFO)
    
app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info("Program running correctly!")
    return "Flask inside Docker!!"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)






