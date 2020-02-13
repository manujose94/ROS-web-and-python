#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt

class TurtleBot:
	
	def __init__(self):
		# Crear un nodo con el nombre "turtlebot_controller"
		# Asegurarse que el nombre sea unico (usando anonymoues = True)
		rospy.init_node('turtlebot_controller', anonymous = True)
		
		# La informacion sera publicada en el topic "/turtle1/cmd_vel
		self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
		# La informacion de posicion se tomara del topic "/turtle1/pose"
		self.sub = rospy.Subscriber('/turtle1/pose', Pose, self.update_pose)
	

		self.pose = Pose()
		self.rate = rospy.Rate(10)
	
	def update_pose(self,data): # Actualizacion de posicion
		""" Esta funcion sera llamada cada vez que un mensaje nuevo es recibido por el subscriptor"""
		self.pose = data
		self.pose.x = round(self.pose.x, 4)
		self.pose.y = round(self.pose.y, 4)

	def euclidean_distance(self, goal_pose): # Distancia euclidiana	
		""" Distancia euclideana entre la pose y el objetivo"""
		return sqrt(pow((goal_pose.x - self.pose.x), 2) + pow((goal_pose.y -self.pose.y), 2))
	
	def linear_vel(self, goal_pose, constant = 1.5): # Velocidad linear
		""" See video: https://www.youtuve.com/whatch?v=Qh15No15htM."""
		return constant * self.euclidean_distance(goal_pose)

	def steering_angle(self, goal_pose): # Angulo de direccion
		return atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x) 

	def angular_vel(self, goal_pose, constant = 6): # Velocidad angular
		return constant * (self.steering_angle(goal_pose) - self.pose.theta)
	
	def move2goal(self): # Movimiento del robot
		""" Mueve la tortuga al objetivo"""
		goal_pose = Pose()

		# Valores dados por el usuario
		goal_pose.x = input("Coloca valor x objetivo: ")
		goal_pose.y = input("Coloca valor y objetivo: ")

		# Insetar un numero ligeramente mayor que 0 (e.g. 0.01).
		distance_tolerance = input("Coloca valor de tolerancia: ")

		vel_msg = Twist()
		
		while self.euclidean_distance(goal_pose) >= distance_tolerance:
		
			# Control proporcional
			
			# Velocidad linear en el eje-x
			vel_msg.linear.x = self.linear_vel(goal_pose)
			vel_msg.linear.y = 0
			vel_msg.linear.z = 0

			# Velocidad angular en el eje-z
			vel_msg.angular.x = 0
			vel_msg.angular.y = 0
			vel_msg.angular.z = self.angular_vel(goal_pose)

			# Publicar velocidad
			self.pub.publish(vel_msg)
		
			# Publicar la velocidad deseada
			self.rate.sleep()

		# Detener el robot cuando el movimiento ha terminado
		vel_msg.linear.x = 0
		vel_msg.angular.z = 0
		self.pub.publish(vel_msg)
		
		# Si presionamos Ctrl + c el movimiento se detendra
		rospy.spin()

if __name__ == '__main__':
	try:
		x = TurtleBot()
		x.move2goal()
	except rospy.ROSInterruptException:
		pass

