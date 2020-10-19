import pygame
from pygame.draw import *
import numpy as np

# define color set
BLUE = (170, 238, 255)
GREEN = (55, 200, 113)
SKIN = (244, 227, 215)
PURPLE = (255, 85, 221)
BLACK = (0, 0, 0)
GRAY = (167, 147, 172)
ORANGE = (255, 204, 0)
BROWN = (85, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)


def draw_polyline(screen, color, point_set, basic_line_width=1):
	"""
	Function draws each new element
	color - line color
	point set - a number of points, which is connected be the line drawn
	"""
	for i in range(len(point_set) - 1):
		line(screen, color, make_integer(point_set[i]), make_integer(point_set[i+1]), basic_line_width)
	pass


def normal_vector(vector):
	"""
	Function defines the coordinates of normal vector to the vector given
	vector - a pair of vector coordinates
	"""
	return np.array([-vector[1], vector[0]])


def vector_length(vector):
	"""
	Function returns length of vector
	vector - a pair of vector coordinates
	"""
	return (vector[0]**2 + vector[1]**2)**0.5


# - OBJECT FUNCTIONS - OBJECT FUNCTIONS - OBJECT FUNCTIONS -
def draw_head(screen, head_color, head_center, size):
	"""
	function draws a head as a colored ellipse
	screen - surface
	head_color - color of the head
	head_center - pair of center of ellipse's coordinates
	size - radius of the head
	"""
	# define a rectangle, curcumscribed around the ellipse
	k = 1.2  # parameter, that defines a relation between head_width and head_height
	head_rect = (int(head_center[0] - size * k // 2), head_center[1] - size // 2, int(size * k), size)
	ellipse(screen, head_color,	head_rect, 0)
	pass


def draw_dress(screen, color, base_point, height):
	"""
	Function is draws triangle dress(body)
	screen - surface
	color - dress_color
	base_point - central top point of a dress (isosceles triangle)
	height - dress vertical size
	"""
	k = 3  # defines relation between dress height and width

	left_corner = [base_point[0] - height // k,	base_point[1] + height]  # left-bottom point
	right_corner = [base_point[0] + height // k, base_point[1] + height]  # right-bottom point

	polygon(screen,	color, [base_point,	left_corner, right_corner])
	pass


def draw_suite(screen, color, center, base_point, height):
	"""
	Function draws ellipsoid suite (body)
	screen - surface
	color - color of suite
	center - main image point
	base_point - center of the ellipse
	height = big axis of an ellipse
	"""
	k = 0.4  # defines relation between suite width and height
	ellipse(screen,	color,(int(base_point[0] - height * k // 2), center[1] - height // 2 + 10, int(height * 0.4), height),0)
	pass


def draw_legs(screen, color, base_point, length, type):
	"""
	Function draws two legs in two polylines
	screen - surface
	color - legs color
	base_point - point of legs intersection (is below drawn human's head)
	length - legs length
	type - value, that defines, whether legs are drawn symmetrically  ('symmetry') or not ('assymetry')
	"""

	# Right leg (is always symmetrical)
	left_point_set = [
		(base_point[0] + length // 8, base_point[1]),
		(base_point[0] + length // 8, base_point[1] + length),
		(base_point[0] + length // 3, base_point[1] + length + length // 30),
		]

	# Left leg
	if type == 'symmetry':
		right_point_set = [
			(base_point[0] - length // 8, base_point[1]),
			(base_point[0] - length // 8, base_point[1] + length),
			(base_point[0] - length // 3, base_point[1] + length + length // 30),
			]
	else:
		right_point_set = [
			(base_point[0] - length // 8, base_point[1]),
			(base_point[0] - length // 2, base_point[1] + length),
			(base_point[0] - length // 1.5, base_point[1] + length)
			]

	draw_polyline(screen, color, left_point_set)
	draw_polyline(screen, color, right_point_set)
	pass


def draw_arms(screen, color, base_point, length, type):
	"""
	Function draws two arms in one polyline
	screen - surface
	color - arms color
	base_point - coordinates of arms intersection (is below drawn humans head)
	length - arm length
	arms - special pair of values:
	{'left' = 'straight' (normal line) or 'bend' (bent line)}
	"""
	# Left arm
	if type['left'] == 'bend':
		# set two points to show a bend
		point = [(base_point[0] - length, base_point[1]), (base_point[0] - length // 2, base_point[1] + length // 2)]
	else:
		point = [(base_point[0] - length, base_point[1] + length)]

	point += [base_point]

	# Right arm
	if type['right'] == 'bend':
		# set two points to show a bend
		point += [(base_point[0] + length // 2, base_point[1] + length // 2), (base_point[0] + length, base_point[1])]
	else:
		point += [(base_point[0] + length, base_point[1] + length)]

	# draw two arms as one line
	draw_polyline(screen, color, point)
	pass


def draw_girl(screen, center, horizontal_shift, height, arms_type):
	"""
	Function draws a girl in given place
	screen - surface
	center - picture center
	horizontal_shift - a horizontal shift from center, that is required to define girl's head center
	height - girl's height
	arms_type - defines arms type (bent or straight)
	"""
	head_center = [center[0] + horizontal_shift, center[1] - height // 2]
	k = 3  # defines a relation between girl's height and her head height

	head_size = height // k

	legs_main_point = [head_center[0], head_center[1] + height]
	arms_main_point = [head_center[0], head_center[1] + height // 4]

	draw_legs(screen, BLACK, legs_main_point, height // 2, 'symmetry')
	draw_arms(screen, BLACK, arms_main_point, height // 2, arms_type)
	draw_dress(screen, PURPLE, head_center, height)
	draw_head(screen, SKIN, head_center, head_size)
	pass


def draw_boy(screen, center, horizontal_shift, height, arms_type):
	"""
	Function draws a boy in given place
	screen - surface
	center - picture center
	horizontal_shift - a horizontal shift from center, that is required to define girl's head center
	height - girl's height
	arms_type - defines arms type (bent or straight)
	"""
	center_of_head = [center[0] + horizontal_shift, center[1] - height // 2]
	k = 3  # defines a relation between girl's height and her head height
	head_size = height // k

	legs_main_point = [center_of_head[0], center_of_head[1] + height]
	arms_main_point = [center_of_head[0], center_of_head[1] + height // 4]

	draw_legs(screen, BLACK, legs_main_point, height // 2, 'assymmetry')
	draw_arms(screen, BLACK, arms_main_point, height // 2, arms_type)
	draw_suite(screen, GRAY, center, center_of_head, height)
	draw_head(screen, SKIN, center_of_head, head_size)
	pass


def normalize_vector(vector, size):
	"""
	Normalizes a vector
	vector - pair of coordinates
	"""
	length = vector_length(vector)
	if length != 0:
		vector = size * vector / length
	return vector


def draw_fiber(screen, base_point, fiber_vector):
	"""
	Draws the fiber
	screen = surface
	base_point = point where human holds a balloon
	"""
	cone_bottom = [base_point[0] + fiber_vector[0], base_point[1] + fiber_vector[1]]
	int_cone_bottom = [int(cone_bottom[0]), int(cone_bottom[1])]
	fiber_point_set = [base_point, int_cone_bottom]

	draw_polyline(screen, BLACK, fiber_point_set)
	return int_cone_bottom


def make_integer(array):
	"""
	Makes every element of an array integer
	array - array
	"""
	new = []
	for i in array:
		new.append(round(i))
	return new


def draw_cone(screen, base_point, fiber_vector, icecream_vector, colors):
	"""
	Function draws a the cone for an icecream
		screen - surface
		base_point - defines the position of a fibre and icecream
		colors - special set of colors:
			'cone': cone color, 'ball_1': 1st ball color, 'ball_2': 2nd ball color, 'ball_3': 3rd ball color
		icecream_vector - defines the direction of the ice cream
	"""
	cone_bottom = draw_fiber(screen, base_point, fiber_vector)
	normal_icecream = normal_vector(icecream_vector)

	# Drawing the cone
	left_triangle_point = make_integer((np.array(cone_bottom) + icecream_vector + normal_icecream // 2).tolist())
	right_triangle_point = make_integer((np.array(cone_bottom) + icecream_vector - normal_icecream // 2).tolist())
	cone_bottom = make_integer(cone_bottom)
	cone_point_set = [cone_bottom, left_triangle_point, right_triangle_point]

	polygon(screen, colors['cone'], cone_point_set)
	return cone_point_set


def draw_balls(screen, colors, icecream_vector, icecream_size, point_set):
	"""
		Function draws a the balls
		screen - surface
		colors - special set of colors:
			'cone': cone color, 'ball_1': 1st ball color, 'ball_2': 2nd ball color, 'ball_3': 3rd ball color
		icecream_vector - defines the direction of the ice cream
		icecream_size - size of an icecream
		point_set - array of coordinates of icecream's cone
	"""
	rotation_angle = np.arctan(icecream_vector[0] / icecream_vector[1]) * 180 / np.pi

	surface_for_ball = []
	ball = []

	for i in range(len(colors) - 1):
		surface_for_ball += [pygame.Surface((int(icecream_size / 2), int(icecream_size / 2.5)), pygame.SRCALPHA, 32)]
		ball_rect = [0, 0, int(icecream_size / 2), int(icecream_size / 2.5)]
		ball += [ellipse(surface_for_ball[i], colors['ball_' + str(i + 1)], ball_rect, 0)]

		surface_for_ball[i] = pygame.transform.rotate(surface_for_ball[i], int(rotation_angle))

		screen.blit(surface_for_ball[i], make_integer(point_set[-1] + icecream_vector / 5))

		if i == 0:
			point_set += [make_integer(((np.array(point_set[1]) + np.array(point_set[2])) / 2).tolist())]
		elif i == 1:
			point_set += [make_integer(((np.array(point_set[2]) + np.array(point_set[3])) / 2 + icecream_vector / 5).tolist())]

	return


def draw_icecream(screen, colors, base_point, icecream_size, fiber_vector, icecream_vector, fiber_length=0):
	"""
	Function draws an icecream with/without a fibre
	screen - surface
	colors - special set of colors:
		'cone': cone color, 'ball_1': 1st ball color, 'ball_2': 2nd ball color, 'ball_3': 3rd ball color
	base_point - main point for a fibre
	fiber_length - length of a fibre, that connects humans with an icecream
	icecream_size - size of an icecream
	fiber_vector - defines the direction of the fibre
	icecream_vector - defines the direction of the ice cream
	"""
	# Vectors normalizing
	fiber_vector = normalize_vector(fiber_vector, fiber_length)
	icecream_vector = normalize_vector(icecream_vector, icecream_size)

	balls_point_set = draw_cone(screen, base_point, fiber_vector, icecream_vector, colors)

	draw_balls(screen, colors, icecream_vector, icecream_size, balls_point_set)

	pass


def paint_sky(screen, height, length):
	"""
	Draws sky and ground
	screen - surface
	height - height of the screen
	length - length of the screen
	"""
	# Drawing background color (sky)
	screen.fill(BLUE)
	# Drawing background color (grass)
	rect(screen, GREEN, [0, height, length, - height // 2], 0)
	pass


def draw_characters(screen, center, height):
	"""
	draws two boys, two girls, two ice creams and a heart-balloon
	screen - surface
	center - pair of coordinates of central point of the picture
	height - height of the screen
	"""

	draw_girl(screen, center, -height // 12, height // 6, arms_type={'left': 'straight', 'right': 'bend'})
	draw_girl(screen, center, height // 12, height // 6, arms_type={'left': 'bend', 'right': 'straight'})

	draw_boy(screen, center, -height // 4, height // 6, arms_type={'left': 'straight', 'right': 'straight'})
	draw_boy(screen, center, height // 4, height // 6, arms_type={'left': 'straight', 'right': 'straight'})
	draw_girl(screen, center, height * 5 // 12, height // 6, arms_type={'left': 'straight', 'right': 'straight'})

	draw_icecream(
		screen,
		colors={'cone': ORANGE, 'ball_1': BROWN, 'ball_2': WHITE, 'ball_3': RED},
		base_point=(center + np.array([0, -height // 24])),
		fiber_length=height // 6,
		icecream_size=height // 10,
		fiber_vector=np.array([0.1, -0.8]),
		icecream_vector=np.array([-0.1, -1])
		)
	draw_icecream(
		screen,
		colors={'cone': ORANGE, 'ball_1': BROWN, 'ball_2': WHITE, 'ball_3': RED},
		base_point=(center + np.array([height // 3, height // 25])),
		icecream_size=height // 20,
		fiber_vector=np.array([1, 1]),
		icecream_vector=np.array([0.1, -0.6])
		)
	draw_icecream(
		screen,
		colors={'cone': RED,
				'ball_1': RED,
				'ball_2': RED},
		base_point=(center + np.array([-height // 3, height // 25])),
		fiber_length=height // 10,
		icecream_size=height // 15,
		fiber_vector=np.array([-0.1, -1]),
		icecream_vector=np.array([-0.1, -1])
		)
	pass


def main():

	fps = 30
	length = 800
	height = 600
	pygame.init()

	center = make_integer([length / 2, height / 2])  # set central point

	screen = pygame.display.set_mode((length, height))

	paint_sky(screen, height, length)

	draw_characters(screen, center, height)

	pygame.display.update()
	clock = pygame.time.Clock()
	finished = False

	while not finished:
		clock.tick(fps)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				finished = True

	pygame.quit()
	pass


main()
