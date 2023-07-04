from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

# For certificate based connection
myMQTTClient = AWSIoTMQTTClient("myClientID")
# For Websocket connection

# Configurations
# For TLS mutual authentication
myMQTTClient.configureEndpoint("a2d7b4vsi90j5r-ats.iot.eu-north-1.amazonaws.com", 8883)
# For Websocket


myMQTTClient.configureCredentials("/home/ankur/Documents/awsiot/aws/RootCA1.pem", "/home/ankur/Documents/awsiot/aws/private.pem.key", "/home/ankur/Documents/awsiot/aws/certificate.pem.crt")
# For Websocket, we only need to configure the root CA

myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

myMQTTClient.connect()
for i in range(5):
    myMQTTClient.publish(topic="myTopic",QoS=1,payload='{"ankur":"79"}')


#myMQTTClient.subscribe("myTopic", 1, customCallback)
#myMQTTClient.unsubscribe("myTopic")
myMQTTClient.disconnect()