import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class BatterySubscriber(Node):
    def __init__(self):
        super().__init__("battery_subscriber")
        self.subscription = self.create_subscription(
            Int32, "battery_level", self.callback, 10)

    def callback(self, msg):
        status = "LOW BATTERY" if msg.data <= 20 else "OK"
        self.get_logger().info(f"Received {msg.data}% - {status}")

def main(args=None):
    rclpy.init(args=args)
    node = BatterySubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()

if __name__ == "__main__":
    main()
