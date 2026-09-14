from collections import Counter
class Solution:
    def compare_counters(self, counter_1, counter_2):
        for item, count in counter_1.items():
            if counter_2[item] < count:
                return False;
        return True;
            

    def rows_valid(self, board: List[List[str]]) -> bool:
        valid_set = Counter(["1","2","3","4","5","6","7","8","9"])
        for curr_row in range(0,9):
            elements = []
            for curr_col in range(0,9):
                curr_item = board[curr_row][curr_col]
                if curr_item != ".":
                    elements.append(curr_item)
            current_set = Counter(elements)
            if self.compare_counters(current_set, valid_set) == False:
                return False
        return True


    def cols_valid(self, board: List[List[str]]) -> bool:
        valid_set = Counter(["1","2","3","4","5","6","7","8","9"])
        for curr_col in range(0,9):
            elements = []
            for curr_row in range(0,9):
                curr_item = board[curr_row][curr_col]
                if curr_item != ".":
                    elements.append(curr_item)
            current_set = Counter(elements)
            if self.compare_counters(current_set, valid_set) == False:
                return False
        return True

    def sub_boxes_valid(self, board):
        valid_set = Counter(["1","2","3","4","5","6","7","8","9"])
        for start_row, start_col in [[0,0], [0,3], [0,6],[3,0], [3,3], [3,6],[6,0], [6,3], [6,6] ]:
            curr_elements = []
            for i in range(0,3):
                for j in range(0,3):
                    new_elem = board[start_row + i][start_col + j]
                    if new_elem != ".":
                        curr_elements.append(board[start_row + i][start_col + j])
            current_set = Counter(curr_elements)
            if self.compare_counters(current_set, valid_set) == False:
                return False
        return True



        
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.rows_valid(board) and self.cols_valid(board) and self.sub_boxes_valid(board)
        