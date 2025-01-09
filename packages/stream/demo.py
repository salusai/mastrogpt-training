#--web true

# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import socket
import time
import json

example_data = [
    "Hello, World!\n",
    "This is a test\n",
    "from an HTTP SSE request\n",
    "Through an openwhisk action\n",
    "To a socket server\n",
    "Back to the HTTP client\n"
]

def main(args):

    strhost = args.get("STREAM_HOST")
    strport = args.get("STREAM_PORT")
    sock = None
    if strhost and strport:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((strhost, int(strport)))
        
    res = ""    
    for ex in example_data:
        time.sleep(1)
        res += ex 
        if sock:
            sock.sendall(json.dumps({"stream": ex}).encode('utf-8'))

    if sock:
        sock.sendall(json.dumps({"stream": ""}).encode('utf-8'))
        sock.close()
    
    return {"body": res}
