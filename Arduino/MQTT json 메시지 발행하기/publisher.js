import mqtt from 'mqtt'

const options = {
  host: EC2_PUBLIC_IP, // EC2_PUBLIC_IP에 AWS EC2에서 받은 public IP를 입력해 주세요.
  port: 1883,
};
const client = mqtt.connect(options);

client.on('connect', function () {
  setInterval(()=>{
    client.publish(TOPIC, 'hello world'); // TOPIC에 발행하려는 토픽 이름을 입력하세요
  }, 3000)
})