import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import tkinter as tk


class RobotControlGUI(Node):
    def __init__(self):
        super().__init__('robot_control')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.get_logger().info("Robot Control GUI Initialized!")

        # Crear la ventana gráfica
        self.window = tk.Tk()
        self.window.title("Robot Control Interface")
        self.window.geometry("400x400")  # Tamaño de la ventana

        # Dividir la ventana en dos áreas
        self.canvas = tk.Canvas(self.window, width=400, height=400)
        self.canvas.pack()

        # Línea divisoria en el centro
        self.canvas.create_line(0, 200, 400, 200, fill="black")

        # Detectar clics en la ventana
        self.canvas.bind("<Button-1>", self.handle_click)  # Click izquierdo del mouse

    def handle_click(self, event):
        twist = Twist()  # Mensaje para controlar el robot
        if event.y < 200:  # Parte superior de la ventana
            twist.linear.x = 0.5  # Mover hacia adelante
            self.get_logger().info("Moving forward!")
        elif event.y > 200:  # Parte inferior de la ventana
            twist.linear.x = -0.5  # Mover hacia atrás
            self.get_logger().info("Moving backward!")
        else:
            twist.linear.x = 0.0  # Detener el robot
        self.publisher_.publish(twist)

    def run(self):
        self.window.mainloop()


def main(args=None):
    rclpy.init(args=args)

    gui_node = RobotControlGUI()
    try:
        gui_node.run()
    except KeyboardInterrupt:
        gui_node.get_logger().info("Shutting down GUI.")
    finally:
        gui_node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
