import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class BatteryPublisher(Node):
    def __init__(self):
        super().__init__("battery_publisher")
        self.publisher = self.create_publisher(Int32, "battery_level", 10)
        self.level = 100
        self.timer = self.create_timer(1.0, self.publish_battery)

    def publish_battery(self):
        msg = Int32()
        msg.data = self.level
        self.publisher.publish(msg)
        self.get_logger().info(f"Battery: {msg.data}%")
        self.level = max(0, self.level - 5)

def main(args=None):
    rclpy.init(args=args)
    node = BatteryPublisher()
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
