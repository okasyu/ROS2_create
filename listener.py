import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class ListenerNode(Node):

    def __init__(self):
        super().__init__("Listener")
        self.create_subscription(Int16, "countup", self.cb, 10)

    def cb(self, msg):
        if msg.data == 0 :
            self.get_logger().info("RX-78-2/FA-78 ガンダム/フルアーマー・ガンダム")
        elif msg.data == 1 :
            self.get_logger().info("RX-79[G] 陸戦型ガンダム")
        elif msg.data == 2 :
            self.get_logger().info("RX-78NT-1 ガンダムNT-1 アレックス")
        elif msg.data == 3 :
            self.get_logger().info("RX-78GP01 ガンダム試作1号機ゼフィランサス")
        elif msg.data == 4 :
            self.get_logger().info("RX-78GP01-Fb ガンダム試作1号機・フルバーニアン")
        elif msg.data == 5 : 
            self.get_logger().info("RX-78GP02A ガンダム試作2号機サイサリス")
        elif msg.data == 6 :
            self.get_logger().info("RX-78GP03S ガンダム試作3号機ステイメン")
        elif msg.data == 7 :
            self.get_logger().info("RX-178 ガンダムMK-Ⅱ")
        elif msg.data == 8 :
            self.get_logger().info("MSZ-006 Zガンダム")
        elif msg.data == 9 :
            self.get_logger().info("MSZ-010 ZZガンダム")
        elif msg.data == 10 :
            self.get_logger().info("RX-93 νガンダム")
        elif msg.data == 11 :
            self.get_logger().info("RX-0 ユニコーンガンダム")
        elif msg.data == 12 :
            self.get_logger().info("RX-9 ナラティブガンダム")
        elif msg.data == 13 :
            self.get_logger().info("RX-104/RX-104FF オデュッセウスガンダム/ペーネロペー")
        elif msg.data == 14 :
            self.get_logger().info("RX-105 Ξガンダム")
        elif msg.data == 15 :
            self.get_logger().info("F91 ガンダムF91")
        elif msg.data == 16 :
            self.get_logger().info("LM312V04 Vガンダム")
        elif msg.data == 17 :
            self.get_logger().info("LM314V21 V2ガンダム")
        else :
            exit("以上が宇宙世紀に存在するガンダムとなる。")

rclpy.init()
rclpy.spin( ListenerNode() )

