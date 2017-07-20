# wm_speech_recognition

This repo contains the node for speech recognition that we use. This node has two speech recognition engine (pocketsphinx and google cloud)

## Requirements

### python
```
speech_recognition
google cloud api
```
## Using
To use this node, you must launch the appropriate launch file. If you want online speech recogniton you will use the ```online_speech.launch```. To use the offline speech recognition, you will launch ```offline_speech.launch```.  

The node will then publish all recognised speeches as ```std_msgs.msg.String``` into the ```"speech"``` topic.
