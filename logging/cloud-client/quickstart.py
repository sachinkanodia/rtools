#!/usr/bin/env python

# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START logging_quickstart]
# Imports the Google Cloud client library
from google.cloud import logging

# Your Google Cloud Platform project ID
project_id = 'YOUR_PROJECT_ID'

# Instantiates a client
logging_client = logging.Client(project=project_id)

# The name of the log to write to
log_name = 'my-log'
# Selects the log to write to
logger = logging_client.logger(log_name)

# The data to log
text = 'Hello, world!'

# Writes the log entry
logger.log_text(text)
# [END logging_quickstart]
