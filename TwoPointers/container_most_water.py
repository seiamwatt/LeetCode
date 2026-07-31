class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        
        left_pointer = 0 
        right_pointer = len(height) - 1

        while left_pointer < right_pointer:
            temp_height = 0

            if height[left_pointer] > height[right_pointer]:
                temp_height = height[right_pointer]
                left_position = left_pointer + 1
                right_position = right_pointer + 1

                temp_area = temp_height * (right_position - left_position)
                if temp_area > max_area:
                    max_area = temp_area

                right_pointer -= 1

            if height[left_pointer] < height[right_pointer]:
                temp_height = height[left_pointer]
                left_position = left_pointer + 1
                right_position = right_pointer + 1

                temp_area = temp_height * (right_position - left_position)
                if temp_area > max_area:
                    max_area = temp_area

                left_pointer += 1

            if height[left_pointer] == height[right_pointer]:
                temp_height = height[left_pointer]
                left_position = left_pointer + 1
                right_position = right_pointer + 1

                temp_area = temp_height * (right_position - left_position)
                if temp_area > max_area:
                    max_area = temp_area

                # right_pointer -= 1
                left_pointer += 1




        return max_area

        