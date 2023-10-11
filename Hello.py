# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
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

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)





questions_responses_scores = [
    {
        "question": "How many locations does the Vendor have where Protected Data will be handled, processed, or stored?",
        "responses": [
            {"response": "One Central Location", "score": 1},
            {"response": "Multiple Locations", "score": 3}
        ]
    },
    {
        "question": "Where are the Vendor’s operations (handling Protected Data) located?",
        "responses": [
            {"response": "Exclusively onshore (within the United States)", "score": 1},
            {"response": "Combination of onshore and offshore", "score": 3},
            {"response": "Exclusively offshore", "score": 5}
        ]
    },
    {
        "question": "Does the Vendor share Protected Data with another entity?",
        "responses": [
            {"response": "No – Only the Vendor handles data", "score": 1},
            {"response": "Yes – The Vendor shares the data with other onshore entities", "score": 3},
            {"response": "Yes – The Vendor shares the data with other offshore entities", "score": 5}
        ]
    },
    {
        "question": "Approximately how many records are handled by the Vendor per year?",
        "responses": [
            {"response": "1 to 250 records or less", "score": 1},
            {"response": "251 to 500 records", "score": 3},
            {"response": "501 to 1000 records", "score": 5},
            {"response": "1001 to 5000 records", "score": 7},
            {"response": "More than 5000 records", "score": 10}
        ]
    },
    {
        "question": "Does the Vendor have access to systems (e.g., VPN)?",
        "responses": [
            {"response": "No", "score": 1},
            {"response": "Yes", "score": 3}
        ]
    },
    {
        "question": "Is data exchanged electronically between the and the Vendor?",
        "responses": [
            {"response": "No – There is no data exchanged electronically", "score": 1},
            {"response": "Yes – electronically sends data to the Vendor", "score": 3},
            {"response": "Yes – electronically sends and receives data from the Vendor", "score": 5}
        ]
    }
]


def main():
    st.title('Vendor Security Scorecard')
    st.write('### Section 4: Vendor Services and Scope')
    
    total_score = 0
    for item in questions_responses_scores:
        question = item["question"]
        options = [resp["response"] for resp in item["responses"]]
        response = st.selectbox(question, options)
        
        # Add the score of the selected response to the total score
        for resp in item["responses"]:
            if resp["response"] == response:
                total_score += resp["score"]
                break
    
    st.write('### Total Risk Score:', total_score)

if __name__ == "__main__":
    main()
