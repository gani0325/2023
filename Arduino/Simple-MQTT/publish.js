import mqtt from "mqtt";

const options = {
  host: "43.201.76.117",
  port: 1883,
};

const client = mqtt.connect(options);

client.on("connect", () => {
  setInterval(() => {
    console.log("publishing .... ");
    client.publish("test_topic", "hello wolrd");
  }, 1000);
});
