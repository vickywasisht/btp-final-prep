"""
Comprehensive test suite for the BST class in work-here.py
Tests all methods: print_between, height, and inorder_successor
"""

import unittest
import sys
import os

# Add the current directory to the path to import work-here module
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import with proper module name (work-here.py becomes work_here when imported)
import importlib.util
spec = importlib.util.spec_from_file_location("work_here", "work-here.py")
work_here = importlib.util.module_from_spec(spec)
spec.loader.exec_module(work_here)

BST = work_here.BST


class TestBST(unittest.TestCase):
    
    def setUp(self):
        """Set up test BSTs for each test method"""
        self.bst = BST()
        self.empty_bst = BST()
        
        # Create a balanced BST: 
        #       5
        #      / \
        #     3   7
        #    / \ / \
        #   2  4 6  8
        self.balanced_bst = BST()
        for value in [5, 3, 7, 2, 4, 6, 8]:
            self.balanced_bst.insert(value)
        
        # Create a single node BST
        self.single_node_bst = BST()
        self.single_node_bst.insert(10)
        
        # Create a left-heavy BST
        #     5
        #    /
        #   3
        #  /
        # 1
        self.left_heavy_bst = BST()
        for value in [5, 3, 1]:
            self.left_heavy_bst.insert(value)
        
        # Create a right-heavy BST
        # 1
        #  \
        #   3
        #    \
        #     5
        self.right_heavy_bst = BST()
        for value in [1, 3, 5]:
            self.right_heavy_bst.insert(value)

    def test_print_between_empty_tree(self):
        """Test print_between on empty tree"""
        result = self.empty_bst.print_between(1, 10)
        self.assertEqual(result, [])

    def test_print_between_single_node_in_range(self):
        """Test print_between with single node in range"""
        result = self.single_node_bst.print_between(5, 15)
        self.assertEqual(result, [10])

    def test_print_between_single_node_out_of_range(self):
        """Test print_between with single node out of range"""
        result = self.single_node_bst.print_between(1, 5)
        self.assertEqual(result, [])

    def test_print_between_balanced_tree_full_range(self):
        """Test print_between on balanced tree with full range"""
        result = self.balanced_bst.print_between(1, 10)
        self.assertEqual(result, [2, 3, 4, 5, 6, 7, 8])

    def test_print_between_balanced_tree_partial_range(self):
        """Test print_between on balanced tree with partial range"""
        result = self.balanced_bst.print_between(3, 6)
        self.assertEqual(result, [3, 4, 5, 6])

    def test_print_between_balanced_tree_narrow_range(self):
        """Test print_between on balanced tree with narrow range"""
        result = self.balanced_bst.print_between(4, 5)
        self.assertEqual(result, [4, 5])

    def test_print_between_no_matches(self):
        """Test print_between with range that has no matches"""
        result = self.balanced_bst.print_between(9, 15)
        self.assertEqual(result, [])

    def test_print_between_left_heavy_tree(self):
        """Test print_between on left-heavy tree"""
        result = self.left_heavy_bst.print_between(1, 5)
        self.assertEqual(result, [1, 3, 5])

    def test_print_between_right_heavy_tree(self):
        """Test print_between on right-heavy tree"""
        result = self.right_heavy_bst.print_between(1, 5)
        self.assertEqual(result, [1, 3, 5])

    def test_height_empty_tree(self):
        """Test height of empty tree"""
        self.assertEqual(self.empty_bst.height(), 0)

    def test_height_single_node(self):
        """Test height of single node tree"""
        self.assertEqual(self.single_node_bst.height(), 1)

    def test_height_balanced_tree(self):
        """Test height of balanced tree"""
        self.assertEqual(self.balanced_bst.height(), 3)

    def test_height_left_heavy_tree(self):
        """Test height of left-heavy tree"""
        self.assertEqual(self.left_heavy_bst.height(), 3)

    def test_height_right_heavy_tree(self):
        """Test height of right-heavy tree"""
        self.assertEqual(self.right_heavy_bst.height(), 3)

    def test_height_two_level_tree(self):
        """Test height of two-level tree"""
        bst = BST()
        bst.insert(5)
        bst.insert(3)
        self.assertEqual(bst.height(), 2)

    def test_inorder_successor_empty_tree(self):
        """Test inorder successor in empty tree"""
        self.assertIsNone(self.empty_bst.inorder_successor(5))

    def test_inorder_successor_single_node(self):
        """Test inorder successor of single node (should be None)"""
        self.assertIsNone(self.single_node_bst.inorder_successor(10))

    def test_inorder_successor_nonexistent_value(self):
        """Test inorder successor of non-existent value"""
        self.assertIsNone(self.balanced_bst.inorder_successor(9))

    def test_inorder_successor_balanced_tree_with_right_subtree(self):
        """Test inorder successor when node has right subtree"""
        # Successor of 3 should be 4
        self.assertEqual(self.balanced_bst.inorder_successor(3), 4)
        # Successor of 5 should be 6
        self.assertEqual(self.balanced_bst.inorder_successor(5), 6)

    def test_inorder_successor_balanced_tree_without_right_subtree(self):
        """Test inorder successor when node has no right subtree"""
        # Successor of 2 should be 3
        self.assertEqual(self.balanced_bst.inorder_successor(2), 3)
        # Successor of 4 should be 5
        self.assertEqual(self.balanced_bst.inorder_successor(4), 5)
        # Successor of 6 should be 7
        self.assertEqual(self.balanced_bst.inorder_successor(6), 7)

    def test_inorder_successor_rightmost_node(self):
        """Test inorder successor of rightmost node (should be None)"""
        self.assertIsNone(self.balanced_bst.inorder_successor(8))

    def test_inorder_successor_left_heavy_tree(self):
        """Test inorder successor in left-heavy tree"""
        self.assertEqual(self.left_heavy_bst.inorder_successor(1), 3)
        self.assertEqual(self.left_heavy_bst.inorder_successor(3), 5)
        self.assertIsNone(self.left_heavy_bst.inorder_successor(5))

    def test_inorder_successor_right_heavy_tree(self):
        """Test inorder successor in right-heavy tree"""
        self.assertEqual(self.right_heavy_bst.inorder_successor(1), 3)
        self.assertEqual(self.right_heavy_bst.inorder_successor(3), 5)
        self.assertIsNone(self.right_heavy_bst.inorder_successor(5))

    def test_edge_cases(self):
        """Test various edge cases"""
        # Test with duplicate values (though BST typically doesn't allow duplicates)
        bst = BST()
        bst.insert(5)
        bst.insert(5)  # This should not create a duplicate in a proper BST
        self.assertEqual(bst.height(), 1)
        
        # Test with negative numbers
        bst_negative = BST()
        for value in [-5, -3, -7, -2, -4, -6, -8]:
            bst_negative.insert(value)
        
        result = bst_negative.print_between(-6, -3)
        self.assertEqual(result, [-6, -5, -4, -3])
        
        self.assertEqual(bst_negative.inorder_successor(-5), -4)

    def test_complex_tree_structure(self):
        """Test with a more complex tree structure"""
        complex_bst = BST()
        # Insert values: [15, 10, 20, 8, 12, 25, 6, 11, 13, 22, 27]
        for value in [15, 10, 20, 8, 12, 25, 6, 11, 13, 22, 27]:
            complex_bst.insert(value)
        
        # Test print_between
        result = complex_bst.print_between(10, 22)
        self.assertEqual(result, [10, 11, 12, 13, 15, 20, 22])
        
        # Test height
        self.assertEqual(complex_bst.height(), 4)
        
        # Test various successor cases
        self.assertEqual(complex_bst.inorder_successor(8), 10)
        self.assertEqual(complex_bst.inorder_successor(12), 13)
        self.assertEqual(complex_bst.inorder_successor(15), 20)
        self.assertEqual(complex_bst.inorder_successor(25), 27)
        self.assertIsNone(complex_bst.inorder_successor(27))


def run_tests():
    """Run all tests and provide detailed output"""
    # Create a test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBST)
    
    # Run tests with detailed output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "="*50)
    print("TEST SUMMARY")
    print("="*50)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.failures:
        print("\nFAILURES:")
        for test, traceback in result.failures:
            print(f"- {test}: {traceback}")
    
    if result.errors:
        print("\nERRORS:")
        for test, traceback in result.errors:
            print(f"- {test}: {traceback}")
    
    if result.wasSuccessful():
        print("\n✅ ALL TESTS PASSED!")
    else:
        print(f"\n❌ {len(result.failures) + len(result.errors)} TEST(S) FAILED!")
    
    return result.wasSuccessful()


if __name__ == "__main__":
    # Run the tests when script is executed directly
    run_tests()
