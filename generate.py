import json
import requests

url = 'https://raw.githubusercontent.com/awslabs/goformation/master/schema/cloudformation.schema.json'
response = requests.get(url)
data = response.json()

data["definitions"]["Syde::SNS::Topic::MODULE"] = {
  "additionalProperties": False,
  "properties": {
      "Condition": {
          "type": "string"
      },
      "Properties": {
          "additionalProperties": False,
          "type": "object",
          "properties": {
              "TopicName": {
                  "type": "string"
              }
          },
          "required": [
            "TopicName"
          ]
      },
      "Type": {
          "enum": [
              "Syde::SNS::Topic::MODULE"
          ],
          "type": "string"
      }
  },
  "required": [
      "Type"
  ],
  "type": "object"
}
data["properties"]["Resources"]["patternProperties"]["^[a-zA-Z0-9]+$"]["anyOf"].append( {
  "$ref": "#/definitions/Syde::SNS::Topic::MODULE"
})


data["definitions"]["Syde::SQS::Queue::MODULE"] = {
  "additionalProperties": False,
  "properties": {
      "Condition": {
          "type": "string"
      },
      "Properties": {
        "additionalProperties": False,
        "type": "object",
        "properties": {
            "PreviewName": {
              "type": "string",
              "description": "Preview Name of SQS."
            },
            "DelaySeconds": {
                "type": "number",
                "description": "The time in seconds that the delivery of all messages in the queue is delayed. You can specify an integer value of 0 to 900 (15 minutes)."
            },
            "MaximumMessageSize": {
                "type": "number",
                "description": "The limit of how many bytes that a message can contain before Amazon SQS rejects it, 1024 bytes (1 KiB) to 262144 bytes (256 KiB)"
            },
            "MessageRetentionPeriod": {
                "type": "number",
                "description": "The number of seconds that Amazon SQS retains a message. You can specify an integer value from 60 seconds (1 minute) to 1209600 seconds (14 days). "
            },
            "ReceiveMessageWaitTimeSeconds": {
                "type": "number",
                "description": "Specifies the duration, in seconds, that the ReceiveMessage action call waits until a message is in the queue in order to include it in the response, as opposed to returning an empty response if a message is not yet available. 1 to 20"
            },
            "UseDeadLetterQueue": {
                "type": "string",
                "description": "A dead-letter queue is a queue that other (source) queues can target for messages that can't be processed (consumed) successfully. You can set aside and isolate these messages in the dead-letter queue to determine why their processing doesn't succeed."
            },
            "VisibilityTimeout": {
                "type": "number",
                "description": "Time in seconds. This should be longer than the time it would take to process and delete a message, this should not exceed 12 hours."
            },
            "KmsMasterKeyIdForSqs": {
                "type": "string",
                "description": "(Optional) For unencrypted leave blank. The ID or Alias of an AWS managed or a custom CMK."
            },
            "SNSTopicToSubscribeArn": {
                "type": "string",
                "description": "(Optional) When will subscribe on a topic sns, set the arn."
            }
        },
        "required": [
          "PreviewName"
        ]
      },
      "Type": {
          "enum": [
              "Syde::SQS::Queue::MODULE"
          ],
          "type": "string"
      }
  },
  "required": [
      "Type",
      "Properties"
  ],
  "type": "object"
}

data["properties"]["Resources"]["patternProperties"]["^[a-zA-Z0-9]+$"]["anyOf"].append( {
  "$ref": "#/definitions/Syde::SQS::Queue::MODULE"
})

# Step 4: Save the modified data
with open('cloudformation-with-syde-modules-v2.schema.json', 'w') as f:
    json.dump(data, f, indent=4)