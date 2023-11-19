# Importing necessary modules
import pygame # Pygame is a set of Python modules designed for writing video games.
import unittest # unittest is a built-in Python module for testing small chunks of code.
from tetris import Tetris # Importing the Tetris class from the tetris module.
import pygame as pg # Importing pygame again with an alias 'pg' for convenience.
from main import App # Importing the App class from the main module.
from tetris import Text, Tetris # Importing the Text and Tetris classes from the tetris module.


# Test case for App class
class TestApp(unittest.TestCase):
 # Initialize App instance
 def setUp(self):
     self.app = App()

 # Test App initialization
 def test_initialization(self):
     # Check if App instance is not None
     self.assertIsNotNone(self.app)
     # Check if screen attribute is not None
     self.assertIsNotNone(self.app.screen)
     # Check if clock attribute is not None
     self.assertIsNotNone(self.app.clock)
     # Check if tetris attribute is not None
     self.assertIsNotNone(self.app.tetris)
     # Check if text attribute is not None
     self.assertIsNotNone(self.app.text)

# Defining a test case for the Text class
class TestText(unittest.TestCase):
   # This method is called before each test method is executed
   def setUp(self):
       # Initializing the pygame library
       pygame.init()
       # Initializing the freetype module of pygame
       pygame.freetype.init()
       # Creating an instance of the App class
       self.app = App()
       # Creating an instance of the Text class
       self.text = Text(self.app)

   # This is a test method for the get_color method of the Text class
   def test_get_color(self):
       # Calling the get_color method of the Text class
       color = self.text.get_color()
       # Checking that the returned value is a tuple
       self.assertIsInstance(color, tuple)
       # Checking that the tuple has exactly 3 elements
       self.assertEqual(len(color), 3)
       # Iterating over each element in the tuple
       for component in color:
           # Checking that each element is a float
           self.assertIsInstance(component, float)
           # Checking that each element is greater than or equal to 0
           self.assertGreaterEqual(component, 0)
           # Checking that each element is less than or equal to 255
           self.assertLessEqual(component, 255)

# Defining a test case for the scoring system
class TestScoring(unittest.TestCase):
  # This method is called before each test method is executed
  def setUp(self):
      # Initializing the score and lines variables
      self.score = 0
      self.lines = 0
      # Setting up a dictionary for scoring
      self.scores = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500}

  # This is a test method for the calculate_score method when no lines have been cleared
  def test_score_no_lines(self):
      # Checking that the calculate_score method returns 0 when no lines have been cleared
      self.assertEqual(self.calculate_score(self.score, self.lines), 0)

  # This is a test method for the calculate_score method when one line has been cleared
  def test_score_one_line(self):
      # Setting the number of lines cleared to 1
      self.lines = 1
      # Checking that the calculate_score method returns 100 when one line has been cleared
      self.assertEqual(self.calculate_score(self.score, self.lines), 100)

  # This is a test method for the calculate_score method when two lines have been cleared
  def test_score_two_lines(self):
      # Setting the number of lines cleared to 2
      self.lines = 2
      # Checking that the calculate_score method returns 300 when two lines have been cleared
      self.assertEqual(self.calculate_score(self.score, self.lines), 300)

  # This is a test method for the calculate_score method when three lines have been cleared
  def test_score_three_lines(self):
      # Setting the number of lines cleared to 3
      self.lines = 3
      # Checking that the calculate_score method returns 700 when three lines have been cleared
      self.assertEqual(self.calculate_score(self.score, self.lines), 700)

  # This is a test method for the calculate_score method when four lines have been cleared
  def test_score_four_lines(self):
      # Setting the number of lines cleared to 4
      self.lines = 4
      # Checking that the calculate_score method returns 1500 when four lines have been cleared
      self.assertEqual(self.calculate_score(self.score, self.lines), 1500)

  # This is the method that is being tested. It calculates the score based on the number of lines cleared
  def calculate_score(self, score, lines):
      # Returning the score plus the score for the number of lines cleared
      return score + self.scores[lines]


# Defining a test case for your module
class TestYourModule(unittest.TestCase):
 # This is a test method for the get_color method of the Text class
 def test_text_get_color(self):
     # This is where you would put the code to test the get_color method
     pass

 # This is a test method for the check_full_lines method of the Tetris class
 def test_tetris_check_full_lines(self):
     # This is where you would put the code to test the check_full_lines method
     pass
 
class TestTetris(unittest.TestCase):
 def setUp(self):
     self.app = App()
     self.tetris = Tetris(self.app)

 def test_move_down(self):
   self.tetris.tetromino.blocks[0].pos.y = 1
   self.tetris.tetromino.move('down')
   self.assertEqual(self.tetris.tetromino.blocks[0].pos.y, 2)

def test_move_left(self):
   self.tetris.tetromino.blocks[0].pos.x = 1
   self.tetris.tetromino.move('left')
   self.assertEqual(self.tetris.tetromino.blocks[0].pos.x, 0)

def test_move_right(self):
   self.tetris.tetromino.blocks[0].pos.x = 1
   self.tetris.tetromino.move('right')
   self.assertEqual(self.tetris.tetromino.blocks[0].pos.x, 2)

def test_move_up(self):
   self.tetris.tetromino.blocks[0].pos.y = 1
   self.tetris.tetromino.move('up')
   self.assertEqual(self.tetris.tetromino.blocks[0].pos.y, 0)

# This is a special Python construct that checks if the script is being run directly or being imported.
# If the script is being run directly, __name__ is set to '__main__'.
# If the script is being imported, __name__ is set to the name of the script/module.
if __name__ == '__main__':
   # This line runs the unit tests. unittest is a built-in Python module for creating and running tests.
   unittest.main()
