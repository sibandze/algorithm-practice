import java.util.HashMap;
import java.util.Map;

public class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> num_map = new HashMap<>();
        for (int idx = 0; idx < nums.length; idx++) {
            int target_num = target - nums[idx];
            if (num_map.containsKey(target_num)) {
                return new int[] { num_map.get(target_num), idx };
            }
            num_map.put(nums[idx], idx);
        }
        throw new IllegalArgumentException("No solution found");
    }
}
